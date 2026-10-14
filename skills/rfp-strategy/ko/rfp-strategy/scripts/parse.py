#!/usr/bin/env python3
"""
문서 파일을 마크다운(.md)으로 변환한다.

엔진 매핑
    PDF  -> markitdown(본문) + pdfplumber(표, 표가 있을 때만 별도 파일)
    HWPX -> python-hwpx export_markdown -> TextExtractor -> BeautifulSoup XML 해석
    HWP  -> pyhwp hwp5txt -> olefile 바이너리 해석
    기타 -> markitdown

사용법
    python parse.py <입력 파일> <출력 파일.md>
    python parse.py <입력 파일> <출력 폴더> --chunk [--chunk-size 2000]

HWP 바이너리 해석(_parse_hwp_olefile) 관련 표기
    본 제품은 한컴의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.
"""

import argparse
import os
import re
import struct
import subprocess
import sys
import zlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# 설정값
# ---------------------------------------------------------------------------
DEFAULT_CHUNK_SIZE = 2000          # 청크 기본 글자 수
CHUNK_OVERSIZE_RATIO = 1.5         # 제목 단위 청크가 이 배수를 넘으면 문단 단위로 다시 나눔
HWP5TXT_TIMEOUT_SEC = 60           # hwp5txt 실행 제한 시간

# HWP 5.0 공개 문서 기준 값
HWP_PROPERTY_OFFSET = 36           # FileHeader 안의 속성 필드 위치
HWP_COMPRESSED_FLAG = 0x01         # 속성 필드 0번 비트: 본문 압축 여부
HWPTAG_PARA_TEXT = 67              # HWPTAG_BEGIN(16) + 51, 문단 텍스트 레코드
HWP_TAG_ID_MASK = 0x3FF            # 레코드 헤더 하위 10비트: 태그 ID
HWP_SIZE_SHIFT = 20                # 레코드 헤더 상위 12비트: 레코드 크기
HWP_SIZE_MASK = 0xFFF
HWP_RECORD_HEADER_BYTES = 4

MARKITDOWN_FORMATS = {
    ".docx", ".doc", ".pptx", ".ppt", ".xlsx", ".xls",
    ".csv", ".json", ".xml", ".html", ".htm", ".txt", ".epub",
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".wav", ".mp3", ".zip",
}


# ---------------------------------------------------------------------------
# 형식 판별
# ---------------------------------------------------------------------------
def detect_format(filepath: str) -> str:
    ext = Path(filepath).suffix.lower()
    if ext == ".hwpx":
        return "hwpx"
    if ext == ".hwp":
        return "hwp"
    if ext == ".pdf":
        return "pdf"
    if ext in MARKITDOWN_FORMATS:
        return "markitdown"
    return "unknown"


# ---------------------------------------------------------------------------
# PDF: 본문은 markitdown, 표는 pdfplumber
# ---------------------------------------------------------------------------
def parse_pdf(filepath: str) -> tuple:
    """PDF 본문을 추출한다. 표 구조는 보존되지 않으므로 표는 extract_pdf_tables가 맡는다."""
    return parse_with_markitdown(filepath), "markitdown"


def extract_pdf_tables(filepath: str) -> Optional[str]:
    """PDF의 표를 마크다운 표로 반환한다. 표가 없으면 None을 반환한다."""
    import pdfplumber

    all_tables_md = []
    with pdfplumber.open(filepath) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            for tbl_num, tbl in enumerate(page.extract_tables(), 1):
                md = _table_to_md(tbl)
                if md:
                    all_tables_md.append(f"### Page {page_num} Table {tbl_num}\n\n{md}")
    return "\n\n".join(all_tables_md) if all_tables_md else None


# ---------------------------------------------------------------------------
# markitdown 공통
# ---------------------------------------------------------------------------
def parse_with_markitdown(filepath: str) -> str:
    from markitdown import MarkItDown

    result = MarkItDown(enable_plugins=False).convert(filepath)
    return result.text_content or ""


# ---------------------------------------------------------------------------
# HWPX: 표를 마크다운 표로 바로 만드는 export_markdown을 먼저 쓴다
# ---------------------------------------------------------------------------
def parse_hwpx(filepath: str) -> tuple:
    """앞 엔진이 오류를 내거나 빈 결과를 내면 다음 엔진으로 넘어간다."""
    engines = [
        (_parse_hwpx_export_markdown, "python-hwpx/export_markdown"),
        (_parse_hwpx_text_extractor, "python-hwpx/TextExtractor"),
    ]
    for func, name in engines:
        try:
            text = func(filepath)
        except Exception as e:
            print(f"[INFO] {name} 실패: {e}", file=sys.stderr)
            continue
        if text and text.strip():
            return text, name
        print(f"[INFO] {name} 결과 없음", file=sys.stderr)
    return _parse_hwpx_xml(filepath), "BeautifulSoup/XML"


def _parse_hwpx_export_markdown(filepath: str) -> str:
    from hwpx.tools.exporter import export_markdown

    with open(filepath, "rb") as f:
        return export_markdown(f.read(), include_tables=True)


def _parse_hwpx_text_extractor(filepath: str) -> str:
    from hwpx.tools.text_extractor import TextExtractor

    with TextExtractor(filepath) as ext:
        return ext.extract_text(
            paragraph_separator="\n\n", skip_empty=True,
            include_nested=True, object_behavior="skip", preserve_breaks=True,
        )


def _parse_hwpx_xml(filepath: str) -> str:
    """HWPX는 ZIP 안의 XML이므로 section XML을 직접 읽는다."""
    import zipfile
    from bs4 import BeautifulSoup

    texts, tables_md = [], []
    with zipfile.ZipFile(filepath, "r") as zf:
        sections = sorted(n for n in zf.namelist()
                          if n.startswith("Contents/section") and n.endswith(".xml"))
        for name in sections:
            soup = BeautifulSoup(zf.read(name).decode("utf-8"), "lxml-xml")
            for p in soup.find_all("hp:p"):
                t = p.get_text(strip=True)
                if t:
                    texts.append(t)
            for tbl in soup.find_all("hp:tbl"):
                rows = [[c.get_text(strip=True) for c in r.find_all("hp:tc")]
                        for r in tbl.find_all("hp:tr")]
                if rows:
                    tables_md.append(_rows_to_md(rows))
    body = "\n\n".join(texts)
    if tables_md:
        body += "\n\n" + "\n\n".join(tables_md)
    return body


# ---------------------------------------------------------------------------
# HWP: pyhwp가 기본, 설치나 실행이 실패하면 olefile 해석으로 전환
# ---------------------------------------------------------------------------
def parse_hwp(filepath: str) -> tuple:
    try:
        return _parse_hwp_pyhwp(filepath), "pyhwp/hwp5txt"
    except Exception as e1:
        print(f"[INFO] pyhwp 실패: {e1}", file=sys.stderr)
        print("[INFO] olefile 경로로 전환", file=sys.stderr)
        return _parse_hwp_olefile(filepath), "olefile"


def _parse_hwp_pyhwp(filepath: str) -> str:
    """pyhwp의 hwp5txt를 별도 프로세스로 실행한다. 표는 <표>로 대체된다."""
    result = subprocess.run(
        ["hwp5txt", filepath], capture_output=True, text=True,
        timeout=HWP5TXT_TIMEOUT_SEC,
    )
    if result.returncode != 0:
        raise RuntimeError(f"hwp5txt 실패: {result.stderr.strip()}")
    if not result.stdout.strip():
        raise RuntimeError("hwp5txt 출력이 비어 있음")
    return result.stdout


def _parse_hwp_olefile(filepath: str) -> str:
    """HWP 5.0 공개 문서의 레코드 구조를 따라 문단 텍스트 레코드만 읽는다.

    표 안의 문단도 같은 레코드이므로 표 내용이 함께 추출된다.
    본문 안의 개체 제어 문자가 깨진 글자로 섞일 수 있어서 아래 정제를 거친다.
    이 정제는 연속된 한자 2자 이상도 지우므로 한자 표기가 빠질 수 있다.
    """
    import olefile

    f = olefile.OleFileIO(filepath)
    try:
        dirs = f.listdir()
        if ["FileHeader"] not in dirs:
            raise ValueError("유효하지 않은 HWP 파일")
        header = f.openstream("FileHeader").read()
        is_compressed = (header[HWP_PROPERTY_OFFSET] & HWP_COMPRESSED_FLAG) == HWP_COMPRESSED_FLAG
        section_names = sorted(
            [d[1] for d in dirs if d[0] == "BodyText"],
            key=lambda x: int(x.replace("Section", "")),
        )
        all_texts = []
        for sec_name in section_names:
            data = f.openstream(f"BodyText/{sec_name}").read()
            if is_compressed:
                data = zlib.decompress(data, -15)  # raw deflate
            all_texts.extend(_read_para_text_records(data))
    finally:
        f.close()
    return "\n\n".join(all_texts)


def _read_para_text_records(data: bytes) -> list:
    texts = []
    i, size = 0, len(data)
    while i + HWP_RECORD_HEADER_BYTES <= size:
        header = struct.unpack_from("<I", data, i)[0]
        tag_id = header & HWP_TAG_ID_MASK
        rec_len = (header >> HWP_SIZE_SHIFT) & HWP_SIZE_MASK
        start = i + HWP_RECORD_HEADER_BYTES
        if rec_len == HWP_SIZE_MASK:
            # 크기 필드가 최댓값이면 실제 크기는 다음 4바이트에 있다(긴 문단)
            if start + HWP_RECORD_HEADER_BYTES > size:
                break
            rec_len = struct.unpack_from("<I", data, start)[0]
            start += HWP_RECORD_HEADER_BYTES
        if tag_id == HWPTAG_PARA_TEXT:
            raw = data[start:min(start + rec_len, size)].decode("utf-16-le", errors="ignore")
            text = _clean_hwp_text(raw)
            if len(text) > 1:
                texts.append(text)
        i = start + rec_len
    return texts


def _clean_hwp_text(text: str) -> str:
    text = re.sub(r"[\x00-\x1f]", "", text)
    text = re.sub(r"[\u4E00-\u9FFF]{2,}", "", text)
    text = re.sub(
        r"[^\u0020-\u007E\uAC00-\uD7AF\u3131-\u318E"
        r"\u2000-\u206F\u00A0-\u00FF\u2010-\u2027"
        r"\u2030-\u205E\u0100-\u024F\u2500-\u25FF"
        r"\u00B7\u25A1\u25A0\u25CB\u25CF\u25E6]+", "", text)
    text = re.sub(r"^[^a-zA-Z0-9\uAC00-\uD7AF\u3131-\u318E(\u25A1\u25A0\u25CB\u25CF\u25E6\-]+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\uAC00-\uD7AF\u3131-\u318E)\u25A1\u25A0\u25CB\u25CF\u25E6.\-?!]+$", "", text)
    return text.strip()


# ---------------------------------------------------------------------------
# 표와 텍스트 정리
# ---------------------------------------------------------------------------
def _clean_cell(text: Optional[str]) -> str:
    if not text:
        return ""
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    text = re.sub(r"[^\S\n]{2,}", " ", text)
    return text.strip()


def _table_to_md(table: list) -> str:
    if not table or not table[0]:
        return ""
    max_cols = max(len(r) for r in table)
    rows = []
    for row in table:
        cells = [_clean_cell(c).replace("\n", " ") for c in row]
        rows.append(cells + [""] * (max_cols - len(cells)))
    return _build_md_table(rows)


def _rows_to_md(rows: list) -> str:
    if not rows:
        return ""
    max_cols = max(len(r) for r in rows)
    return _build_md_table([r + [""] * (max_cols - len(r)) for r in rows])


def _build_md_table(rows: list) -> str:
    if not rows:
        return ""
    head = "| " + " | ".join(rows[0]) + " |"
    sep = "| " + " | ".join(["---"] * len(rows[0])) + " |"
    body = ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join([head, sep] + body)


def postprocess(text: str) -> str:
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    text = re.sub(r"[^\S\n]{2,}", " ", text)
    text = text.replace("\f", "\n\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def build_metadata(source, fmt, engine, char_count, chunk_idx=None, total=None) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = ["---", f"source: {source}", f"format: {fmt}", f"parsed_at: {now}",
             f"engine: {engine}", f"char_count: {char_count}"]
    if chunk_idx is not None:
        lines.append(f"chunk: {chunk_idx}")
    if total is not None:
        lines.append(f"total_chunks: {total}")
    lines.append("---")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 청크 분할: 제목 단위로 묶고, 너무 긴 묶음은 문단 단위로 다시 나눈다
# ---------------------------------------------------------------------------
def chunk_by_heading(text: str, size: int = DEFAULT_CHUNK_SIZE) -> list:
    pat = re.compile(r"^(#{1,6}\s)", re.MULTILINE)
    parts = pat.split(text)
    sections, i = [], 0
    while i < len(parts):
        if pat.match(parts[i]) and i + 1 < len(parts):
            sections.append(parts[i] + parts[i + 1])
            i += 2
        else:
            if parts[i].strip():
                sections.append(parts[i])
            i += 1

    chunks, cur = [], ""
    for sec in sections:
        if len(cur) + len(sec) > size and cur.strip():
            chunks.append(cur.strip())
            cur = sec
        else:
            cur = cur + "\n\n" + sec if cur else sec
    if cur.strip():
        chunks.append(cur.strip())

    final = []
    for c in chunks:
        if len(c) <= size * CHUNK_OVERSIZE_RATIO:
            final.append(c)
            continue
        sub = ""
        for p in c.split("\n\n"):
            if len(sub) + len(p) > size and sub.strip():
                final.append(sub.strip())
                sub = p
            else:
                sub = sub + "\n\n" + p if sub else p
        if sub.strip():
            final.append(sub.strip())
    return final if final else [text]


# ---------------------------------------------------------------------------
# 실행
# ---------------------------------------------------------------------------
def parse(filepath: str, fmt: str) -> tuple:
    if fmt == "hwpx":
        return parse_hwpx(filepath)
    if fmt == "hwp":
        return parse_hwp(filepath)
    if fmt == "pdf":
        return parse_pdf(filepath)
    return parse_with_markitdown(filepath), "markitdown"


def write_outputs(args, text: str, src: str, stem: str, ext: str, engine: str) -> None:
    if args.chunk:
        out_dir = Path(args.output)
        out_dir.mkdir(parents=True, exist_ok=True)
        chunks = chunk_by_heading(text, args.chunk_size)
        print(f"[INFO] 청크: {len(chunks)}개")
        for idx, chunk in enumerate(chunks, 1):
            meta = build_metadata(src, ext, engine, len(chunk), idx, len(chunks))
            (out_dir / f"{stem}_chunk_{idx:03d}.md").write_text(meta + "\n\n" + chunk, encoding="utf-8")
    else:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build_metadata(src, ext, engine, len(text)) + "\n\n" + text, encoding="utf-8")
        print(f"[INFO] 저장: {out}")


def write_pdf_tables(args, src: str, stem: str, ext: str) -> None:
    try:
        tables_md = extract_pdf_tables(args.input)
    except Exception as e:
        print(f"[WARN] 표 추출 실패: {e}", file=sys.stderr)
        return
    if not tables_md:
        print("[INFO] PDF 안에 표 없음(표 파일 미생성)")
        return
    base = Path(args.output) if args.chunk else Path(args.output).parent
    tbl_path = base / f"{stem}_tables.md"
    meta = build_metadata(src, ext, "pdfplumber", len(tables_md))
    tbl_path.write_text(meta + "\n\n" + tables_md, encoding="utf-8")
    print(f"[INFO] 표 파일: {tbl_path}")


def main():
    ap = argparse.ArgumentParser(description="문서 파일을 마크다운으로 변환")
    ap.add_argument("input", help="입력 파일 경로")
    ap.add_argument("output", help="출력 파일 경로 또는 청크 출력 폴더")
    ap.add_argument("--chunk", action="store_true", help="제목 단위로 나눠 여러 파일로 저장")
    ap.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE)
    args = ap.parse_args()

    if not os.path.exists(args.input):
        print(f"[ERROR] 파일 없음: {args.input}", file=sys.stderr)
        sys.exit(1)

    fmt = detect_format(args.input)
    if fmt == "unknown":
        print(f"[ERROR] 지원하지 않는 형식: {Path(args.input).suffix}", file=sys.stderr)
        sys.exit(1)

    src = Path(args.input).name
    stem = Path(args.input).stem
    ext = Path(args.input).suffix.lower().lstrip(".")
    print(f"[INFO] 입력: {src} | 형식: {fmt}")

    try:
        text, engine = parse(args.input, fmt)
    except Exception as e:
        print(f"[ERROR] 변환 실패: {e}", file=sys.stderr)
        sys.exit(1)

    text = postprocess(text)
    print(f"[INFO] 엔진: {engine} | 글자 수: {len(text):,}")
    if not text:
        print("[WARN] 추출된 텍스트 없음. 스캔 이미지 문서이면 OCR이 필요함", file=sys.stderr)

    write_outputs(args, text, src, stem, ext, engine)
    if fmt == "pdf":
        write_pdf_tables(args, src, stem, ext)
    print("[INFO] 완료")


if __name__ == "__main__":
    main()
