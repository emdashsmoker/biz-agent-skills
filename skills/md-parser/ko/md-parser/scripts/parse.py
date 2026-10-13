#!/usr/bin/env python3
"""md-parser: 문서 파일을 마크다운으로 변환하는 스크립트

엔진
    PDF   markitdown(본문) + pdfplumber(선이 그어진 표, 표가 있을 때만 별도 파일)
    HWPX  python-hwpx export_markdown -> TextExtractor -> BeautifulSoup
          글상자 같은 도형 안 글자가 있으면 TextExtractor 전체 텍스트를 별도 파일로 추가
    HWP   pyhwp hwp5txt -> olefile 직접 파싱
          hwp5txt 결과에 <표> 또는 <그림> 자리표시가 있으면 olefile 전체 텍스트를 별도 파일로 추가
    기타  markitdown

사용법
    python parse.py <입력 파일> <출력.md>
    python parse.py <입력 파일> <출력 폴더> --chunk [--chunk-size 2000]
    python parse.py <오디오 또는 오디오가 든 zip> <출력.md> --allow-audio-upload

본 제품은 한컴의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.
"""

import argparse
import json
import re
import struct
import subprocess
import sys
import zipfile
import zlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Optional

# ---------------------------------------------------------------------------
# 설정값
# ---------------------------------------------------------------------------
DEFAULT_CHUNK_SIZE = 2000
# 제목 단위로 묶은 청크가 기준 크기의 이 배수를 넘으면 문단 단위로 다시 나눔
OVERSIZE_CHUNK_FACTOR = 1.5
HWP5TXT_TIMEOUT_SEC = 60

# markitdown은 오디오를 Google 음성인식 서비스로 전송하므로 사용자 동의 없이 처리하지 않음
AUDIO_EXTENSIONS = {".wav", ".mp3", ".m4a", ".mp4"}

# pyhwp hwp5txt는 표와 도형을 이 문자열로 바꾸고 내용을 출력하지 않음
HWP5TXT_PLACEHOLDERS = ("<표>", "<그림>")

HWPX_SECTION_PATTERN = r"Contents/section\d+\.xml"
# python-hwpx export_markdown은 이 요소(도형 안 글자)를 출력하지 않음
HWPX_SHAPE_TEXT_TAG = b"drawText"

# HWP 5.0 공개 문서 기준 상수
HWPTAG_PARA_TEXT = 67                 # HWPTAG_BEGIN(16) + 51
HWP_RECORD_SIZE_EXTENDED = 0xFFF      # 크기 필드가 이 값이면 뒤따르는 4바이트가 실제 크기
HWP_FLAG_COMPRESSED = 0x1
HWP_FLAG_PASSWORD = 0x2
HWP_FLAG_DISTRIBUTION = 0x4
HWP_CONTROL_WCHARS = 8                # 인라인 및 확장 제어 문자가 차지하는 WCHAR 수
HWP_SINGLE_WCHAR_CONTROLS = {0, 10, 13, 24, 25, 26, 27, 28, 29, 30, 31}
HWP_CONTROL_TO_TEXT = {9: "\t", 10: "\n", 24: "-", 30: " ", 31: " "}


# ---------------------------------------------------------------------------
# 포맷 판별
# ---------------------------------------------------------------------------
def detect_format(filepath: str) -> str:
    ext = Path(filepath).suffix.lower()
    if ext in (".pdf", ".hwp", ".hwpx"):
        return ext.lstrip(".")
    # 나머지는 markitdown이 지원 여부를 판단하고 미지원이면 오류를 반환
    return "markitdown"


def contains_audio(filepath: str) -> bool:
    path = Path(filepath)
    if path.suffix.lower() in AUDIO_EXTENSIONS:
        return True
    # markitdown은 zip 안의 파일도 변환하므로 zip 안의 오디오도 전송 대상
    if path.suffix.lower() == ".zip" and zipfile.is_zipfile(filepath):
        with zipfile.ZipFile(filepath) as zf:
            return any(Path(n).suffix.lower() in AUDIO_EXTENSIONS for n in zf.namelist())
    return False


# ---------------------------------------------------------------------------
# 엔진 연쇄 실행: 빈 결과도 실패로 보고 다음 엔진으로 넘어감
# ---------------------------------------------------------------------------
def run_engine_chain(filepath: str, engines: list) -> tuple:
    errors, raised = [], False
    for name, engine in engines:
        try:
            text = engine(filepath)
            if text and text.strip():
                return text, name
            errors.append(f"{name}: 빈 결과")
        except Exception as e:
            errors.append(f"{name}: {e}")
            raised = True
        print(f"[INFO] {errors[-1]} -> 다음 엔진으로 전환", file=sys.stderr)
    # 모든 엔진이 오류 없이 빈 결과를 냈다면 원본이 비어 있는 문서로 봄
    if not raised:
        return "", engines[0][0]
    raise RuntimeError(" / ".join(errors))


# ---------------------------------------------------------------------------
# markitdown (PDF 본문 및 기타 포맷)
# ---------------------------------------------------------------------------
def parse_with_markitdown(filepath: str) -> str:
    from markitdown import MarkItDown
    result = MarkItDown(enable_plugins=False).convert(filepath)
    return result.text_content or ""


# ---------------------------------------------------------------------------
# PDF 표: pdfplumber
# ---------------------------------------------------------------------------
def extract_pdf_tables(filepath: str) -> Optional[str]:
    """표가 없으면 None을 반환"""
    import pdfplumber
    blocks = []
    with pdfplumber.open(filepath) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            for tbl_num, table in enumerate(page.extract_tables(), 1):
                md = table_to_md(table)
                if md:
                    blocks.append(f"### Page {page_num} Table {tbl_num}\n\n{md}")
    return "\n\n".join(blocks) if blocks else None


# ---------------------------------------------------------------------------
# HWPX: python-hwpx -> BeautifulSoup
# ---------------------------------------------------------------------------
def parse_hwpx_export_markdown(filepath: str) -> str:
    from hwpx.tools.exporter import export_markdown
    with open(filepath, "rb") as f:
        return export_markdown(f.read(), include_tables=True)


def parse_hwpx_text_extractor(filepath: str) -> str:
    from hwpx.tools.text_extractor import TextExtractor
    with TextExtractor(filepath) as ext:
        return ext.extract_text(
            paragraph_separator="\n\n", skip_empty=True,
            include_nested=True, object_behavior="skip", preserve_breaks=True,
        )


def parse_hwpx_xml(filepath: str) -> str:
    """python-hwpx가 모두 실패할 때 section XML을 직접 읽음. 표는 본문 뒤에 모아서 출력"""
    from bs4 import BeautifulSoup
    texts, tables_md = [], []
    with zipfile.ZipFile(filepath) as zf:
        sections = sorted(
            (n for n in zf.namelist() if re.fullmatch(HWPX_SECTION_PATTERN, n)),
            key=lambda n: int(re.search(r"\d+", n).group()),
        )
        for name in sections:
            soup = BeautifulSoup(zf.read(name), "lxml-xml")
            for p in soup.find_all("hp:p"):
                if p.find_parent("hp:tbl"):
                    continue  # 표 안 문단은 아래 표 변환에서 처리
                # 하위 문단(글상자 등)의 글자는 그 문단에서 따로 출력되므로 제외
                own = "".join(t.get_text() for t in p.find_all("hp:t")
                              if t.find_parent("hp:p") is p).strip()
                if own:
                    texts.append(own)
            for tbl in soup.find_all("hp:tbl"):
                rows = [[" ".join(t.get_text() for t in cell.find_all("hp:t")).strip()
                         for cell in row.find_all("hp:tc", recursive=False)]
                        for row in tbl.find_all("hp:tr", recursive=False)]
                if rows:
                    tables_md.append(rows_to_md(rows))
    return "\n\n".join(texts + tables_md)


def hwpx_has_shape_text(filepath: str) -> bool:
    try:
        with zipfile.ZipFile(filepath) as zf:
            return any(HWPX_SHAPE_TEXT_TAG in zf.read(n) for n in zf.namelist()
                       if re.fullmatch(HWPX_SECTION_PATTERN, n))
    except (zipfile.BadZipFile, OSError):
        return False


HWPX_ENGINES = [
    ("python-hwpx/export_markdown", parse_hwpx_export_markdown),
    ("python-hwpx/TextExtractor", parse_hwpx_text_extractor),
    ("BeautifulSoup/XML", parse_hwpx_xml),
]


# ---------------------------------------------------------------------------
# HWP: pyhwp -> olefile 직접 파싱
# ---------------------------------------------------------------------------
def parse_hwp_pyhwp(filepath: str) -> str:
    # 현재 파이썬으로 hwp5txt를 실행하여 PATH 설정과 무관하게 동일 환경의 pyhwp를 사용
    # hwp5txt는 UTF-8 바이트를 출력하므로 OS 기본 인코딩과 무관하게 UTF-8로 해독
    cmd = [sys.executable, "-c",
           "import sys; from hwp5.hwp5txt import main; sys.exit(main())", filepath]
    result = subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="replace",
                            timeout=HWP5TXT_TIMEOUT_SEC)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"종료 코드 {result.returncode}")
    return result.stdout


def parse_hwp_olefile(filepath: str) -> str:
    """BodyText 섹션의 문단 텍스트 레코드를 HWP 5.0 공개 문서 구조대로 읽음"""
    import olefile
    with olefile.OleFileIO(filepath) as ole:
        if not ole.exists("FileHeader"):
            raise ValueError("HWP 5.0 문서가 아님")
        flags = struct.unpack_from("<I", ole.openstream("FileHeader").read(), 36)[0]
        if flags & HWP_FLAG_PASSWORD:
            raise ValueError("암호가 설정된 문서")
        if flags & HWP_FLAG_DISTRIBUTION:
            raise ValueError("배포용 문서라서 본문이 암호화되어 있음")
        sections = sorted(
            (entry[1] for entry in ole.listdir() if entry[0] == "BodyText"),
            key=lambda s: int(s.replace("Section", "")),
        )
        paragraphs = []
        for section in sections:
            data = ole.openstream(f"BodyText/{section}").read()
            if flags & HWP_FLAG_COMPRESSED:
                data = zlib.decompress(data, -15)
            paragraphs.extend(read_para_texts(data))
    return "\n\n".join(paragraphs)


def read_para_texts(data: bytes) -> list:
    """레코드 헤더는 태그 10비트, 레벨 10비트, 크기 12비트로 구성"""
    paragraphs, pos = [], 0
    while pos + 4 <= len(data):
        header = struct.unpack_from("<I", data, pos)[0]
        pos += 4
        tag, size = header & 0x3FF, (header >> 20) & 0xFFF
        if size == HWP_RECORD_SIZE_EXTENDED:
            size = struct.unpack_from("<I", data, pos)[0]
            pos += 4
        if tag == HWPTAG_PARA_TEXT:
            text = decode_para_text(data[pos:pos + size]).strip()
            if text:
                paragraphs.append(text)
        pos += size
    return paragraphs


def decode_para_text(raw: bytes) -> str:
    """제어 문자(0-31)는 종류에 따라 1 또는 8 WCHAR를 차지하므로 그만큼 건너뜀"""
    codes = struct.unpack(f"<{len(raw) // 2}H", raw[:len(raw) // 2 * 2])
    out, i = [], 0
    while i < len(codes):
        code = codes[i]
        if code >= 32:
            out.append(chr(code))
            i += 1
            continue
        out.append(HWP_CONTROL_TO_TEXT.get(code, ""))
        i += 1 if code in HWP_SINGLE_WCHAR_CONTROLS else HWP_CONTROL_WCHARS
    return "".join(out)


HWP_ENGINES = [
    ("pyhwp/hwp5txt", parse_hwp_pyhwp),
    ("olefile", parse_hwp_olefile),
]


# ---------------------------------------------------------------------------
# 마크다운 표 변환
# ---------------------------------------------------------------------------
def clean_cell(text: Optional[str]) -> str:
    if not text:
        return ""
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def table_to_md(table: list) -> str:
    if not table or not table[0]:
        return ""
    return rows_to_md([[clean_cell(c) for c in row] for row in table])


def rows_to_md(rows: list) -> str:
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [[c.replace("|", "\\|") for c in r] + [""] * (width - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 후처리, 메타데이터, 청크
# ---------------------------------------------------------------------------
def postprocess(text: str) -> str:
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    # 줄 앞 들여쓰기는 목록 계층과 코드 블록을 결정하므로 유지하고 글자 사이 공백만 줄임
    text = re.sub(r"(?<=\S)[^\S\n]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def build_metadata(source: str, fmt: str, engine: str, char_count: int,
                   chunk_idx: Optional[int] = None, total: Optional[int] = None) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # 파일명에 콜론 등이 있어도 YAML이 깨지지 않도록 JSON 문자열로 기록
    lines = ["---", f"source: {json.dumps(source, ensure_ascii=False)}", f"format: {fmt}",
             f"parsed_at: {now}", f"engine: {engine}", f"char_count: {char_count}"]
    if chunk_idx is not None:
        lines.append(f"chunk: {chunk_idx}")
    if total is not None:
        lines.append(f"total_chunks: {total}")
    lines.append("---")
    return "\n".join(lines)


def split_by_size(parts: list, size: int, joiner: str = "\n\n") -> list:
    chunks, cur = [], ""
    for part in parts:
        if len(cur) + len(part) > size and cur.strip():
            chunks.append(cur.strip())
            cur = part
        else:
            cur = cur + joiner + part if cur else part
    if cur.strip():
        chunks.append(cur.strip())
    return chunks


def chunk_by_heading(text: str, size: int = DEFAULT_CHUNK_SIZE) -> list:
    """제목(#) 단위로 나눈 뒤 크기 기준으로 묶고, 지나치게 큰 청크는 문단 단위로 다시 나눔"""
    sections = [s for s in re.split(r"(?m)^(?=#{1,6}\s)", text) if s.strip()]
    final = []
    for chunk in split_by_size(sections, size):
        if len(chunk) <= size * OVERSIZE_CHUNK_FACTOR:
            final.append(chunk)
        else:
            final.extend(split_by_size(chunk.split("\n\n"), size))
    return final or [text]


# ---------------------------------------------------------------------------
# 파일 쓰기
# ---------------------------------------------------------------------------
def write_md(path: Path, metadata: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(metadata + "\n\n" + body, encoding="utf-8")
    print(f"[INFO] 저장: {path}")


def write_extra_file(out_dir: Path, name: str, src: str, ext: str,
                     engine: str, producer: Callable[[], Optional[str]]) -> None:
    """본문 파일과 별도로 보조 파일(PDF 표, HWP와 HWPX 전체 텍스트)을 내용이 있을 때만 생성"""
    try:
        content = producer()
    except Exception as e:
        print(f"[WARN] {name} 생성 실패: {e}", file=sys.stderr)
        return
    if not content or not content.strip():
        print(f"[INFO] {name} 내용 없음 (파일 미생성)")
        return
    content = postprocess(content)
    write_md(out_dir / name, build_metadata(src, ext, engine, len(content)), content)


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------
def parse(filepath: str, fmt: str) -> tuple:
    if fmt == "pdf":
        return parse_with_markitdown(filepath), "markitdown"
    if fmt == "hwpx":
        return run_engine_chain(filepath, HWPX_ENGINES)
    if fmt == "hwp":
        return run_engine_chain(filepath, HWP_ENGINES)
    return parse_with_markitdown(filepath), "markitdown"


def main() -> None:
    ap = argparse.ArgumentParser(description="문서 파일을 마크다운으로 변환")
    ap.add_argument("input", help="입력 파일 경로")
    ap.add_argument("output", help="출력 .md 파일 경로 (--chunk 사용 시 출력 폴더)")
    ap.add_argument("--chunk", action="store_true", help="제목과 문단 기준으로 나누어 저장")
    ap.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE, help="청크 기준 글자 수")
    ap.add_argument("--allow-audio-upload", action="store_true",
                    help="오디오를 외부 음성인식 서비스로 전송하는 데 사용자가 동의한 경우에만 지정")
    args = ap.parse_args()

    src_path = Path(args.input)
    if not src_path.is_file():
        print(f"[ERROR] 파일 없음: {args.input}", file=sys.stderr)
        sys.exit(1)
    if contains_audio(args.input) and not args.allow_audio_upload:
        print("[ERROR] 오디오 변환은 음성 데이터를 Google 음성인식 서비스로 전송함. "
              "사용자 동의를 받은 뒤 --allow-audio-upload를 붙여 다시 실행", file=sys.stderr)
        sys.exit(2)

    fmt = detect_format(args.input)
    src, stem = src_path.name, src_path.stem
    ext = src_path.suffix.lower().lstrip(".")
    print(f"[INFO] 입력: {src} | 포맷: {fmt}")

    try:
        text, engine = parse(args.input, fmt)
    except Exception as e:
        print(f"[ERROR] 파싱 실패: {e}", file=sys.stderr)
        sys.exit(1)

    text = postprocess(text)
    print(f"[INFO] 엔진: {engine} | 글자 수: {len(text):,}")
    if not text:
        print("[WARN] 텍스트 미추출", file=sys.stderr)

    if args.chunk:
        out_dir = Path(args.output)
        chunks = chunk_by_heading(text, args.chunk_size)
        print(f"[INFO] 청크: {len(chunks)}개")
        for i, chunk in enumerate(chunks, 1):
            meta = build_metadata(src, ext, engine, len(chunk), i, len(chunks))
            write_md(out_dir / f"{stem}_chunk_{i:03d}.md", meta, chunk)
    else:
        out_dir = Path(args.output).parent
        write_md(Path(args.output), build_metadata(src, ext, engine, len(text)), text)

    path = args.input
    extras = []
    if fmt == "pdf":
        extras.append(("_tables.md", "pdfplumber", lambda: extract_pdf_tables(path)))
    if engine == "pyhwp/hwp5txt" and any(p in text for p in HWP5TXT_PLACEHOLDERS):
        extras.append(("_fulltext.md", "olefile", lambda: parse_hwp_olefile(path)))
    if engine == "python-hwpx/export_markdown" and hwpx_has_shape_text(path):
        extras.append(("_fulltext.md", "python-hwpx/TextExtractor",
                       lambda: parse_hwpx_text_extractor(path)))
    for suffix, extra_engine, producer in extras:
        write_extra_file(out_dir, stem + suffix, src, ext, extra_engine, producer)

    print("[INFO] 완료")


if __name__ == "__main__":
    main()
