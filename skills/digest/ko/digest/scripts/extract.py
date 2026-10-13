#!/usr/bin/env python3
"""digest 입력 자료 텍스트 추출 스크립트

입력 1건의 종류를 판별하여 마크다운 파일로 변환하고 결과 요약을 JSON으로 출력

입력 종류별 처리 경로
    웹 주소(http, https)   httpx로 수신 후 웹페이지는 trafilatura로 본문 추출, 파일이면 파일 처리 경로로 전달
    자막 파일(.srt, .vtt)  시간 정보, 서식 태그, 연속 중복 줄 제거
    음성 및 영상 파일      faster-whisper 로컬 전사 (ffmpeg 우선, 미설치 시 PyAV 디코딩)
    문서 파일              PDF는 markitdown과 pdfplumber, HWPX는 python-hwpx, HWP는 pyhwp와 olefile, 그 외는 markitdown

HWP 대체 파서(parse_hwp_olefile) 고지
    본 제품은 한글과컴퓨터의 한/글 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.

사용 예
    python extract.py report.pdf
    python extract.py "https://example.com/news/123" --max-chars 50000
    python extract.py meeting.m4a --model small --language ko
    python extract.py lecture.vtt --start 00:10:00 --end 00:25:00
    python extract.py --bundle
    python extract.py --clean
"""

import argparse
import hashlib
import html
import importlib
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import traceback
import zipfile
import zlib
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

# ── 설정 ─────────────────────────────────────────────────────
WORK_DIR = Path(os.environ.get("DIGEST_WORK_DIR", "digest_work"))
DOWNLOAD_SUBDIR = "downloads"
ACCEPT_LANGUAGE = os.environ.get(
    "DIGEST_ACCEPT_LANGUAGE", "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
)
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
DEFAULT_TIMEOUT_SEC = 15
DEFAULT_CHUNK_SIZE = 2000
DEFAULT_MODEL = "tiny"
DEFAULT_BEAM_SIZE = 5
DEFAULT_BUNDLE_NAME = "digest_documents.zip"
MODEL_CHOICES = ["tiny", "base", "small", "medium", "large-v3"]

# 매직넘버 대신 이름을 붙인 기준값
CHUNK_OVERFLOW_RATIO = 1.5   # 제목 단위 청크가 기준의 1.5배를 넘으면 문단 단위로 다시 분할
MIN_WEB_TEXT_CHARS = 50      # trafilatura 결과가 이보다 짧으면 추출 실패로 보고 대체 추출기 사용
MIN_DOC_TEXT_CHARS = 10      # 문서 추출 결과가 이보다 짧으면 이미지 기반 문서로 판단
SAMPLE_RATE = 16000          # Whisper 입력 규격(16kHz 모노)
FFMPEG_TIMEOUT_SEC = 600
HWP5TXT_TIMEOUT_SEC = 60
TRUNCATION_MARK = "\n\n[... 이하 생략 ...]"

# HWP 5.0 레코드 규격 (한/글 문서 파일 형식 5.0 공개 문서 기준)
HWPTAG_PARA_TEXT = 67        # HWPTAG_BEGIN(0x10) + 51
HWP_EXTENDED_SIZE = 0xFFF    # 크기 필드가 이 값이면 뒤따르는 4바이트가 실제 크기
HWP_COMPRESS_OFFSET = 36     # FileHeader 속성 필드 위치, 비트 0이 압축 여부

# ── 확장자 분류 ───────────────────────────────────────────────
CAPTION_EXTS = {".srt", ".vtt"}
MEDIA_EXTS = {
    ".ogg", ".opus", ".m4a", ".aac", ".mp3", ".wav", ".flac",
    ".wma", ".webm", ".amr", ".mp4", ".mkv", ".avi", ".mov",
}
MARKITDOWN_EXTS = {
    ".docx", ".pptx", ".xlsx", ".xls", ".csv", ".json", ".xml",
    ".html", ".htm", ".txt", ".md", ".epub", ".jpg", ".jpeg", ".png", ".zip",
}
DOCUMENT_EXTS = MARKITDOWN_EXTS | {".pdf", ".hwpx", ".hwp"}
DOWNLOAD_ONLY_EXTS = {".doc", ".ppt"}  # 텍스트 추출 엔진이 없는 구형 형식
SUPPORTED_EXTS = CAPTION_EXTS | MEDIA_EXTS | DOCUMENT_EXTS

MIME_TO_EXT = {
    "application/pdf": ".pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
    "application/msword": ".doc",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": ".xlsx",
    "application/vnd.ms-excel": ".xls",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": ".pptx",
    "application/vnd.ms-powerpoint": ".ppt",
    "text/csv": ".csv",
    "application/zip": ".zip",
    "application/x-hwp": ".hwp",
    "application/haansofthwp": ".hwp",
    "application/vnd.hancom.hwpx": ".hwpx",
    "application/x-subrip": ".srt",
    "text/vtt": ".vtt",
    "audio/mpeg": ".mp3",
    "audio/mp4": ".m4a",
    "audio/wav": ".wav",
    "audio/ogg": ".ogg",
    "video/mp4": ".mp4",
}


# ── 공통 유틸리티 ─────────────────────────────────────────────
class MissingDependency(Exception):
    """필요 패키지 미설치. 설치 명령을 사용자에게 그대로 전달하기 위해 별도 예외로 분리"""


def require(module_name, pip_spec):
    try:
        return importlib.import_module(module_name)
    except ImportError as exc:
        raise MissingDependency(pip_spec) from exc


def truncate(text, max_chars):
    if max_chars > 0 and len(text) > max_chars:
        return text[:max_chars] + TRUNCATION_MARK, True
    return text, False


def unique_path(directory, filename):
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / filename
    stem, suffix, n = path.stem, path.suffix, 1
    while path.exists():
        path = directory / f"{stem}_{n}{suffix}"
        n += 1
    return path


def write_markdown(path, meta, body):
    """YAML 머리말과 본문을 저장. 값은 JSON 문자열로 기록하여 특수문자 오류 방지"""
    lines = ["---"]
    for key, value in meta.items():
        if value is None:
            continue
        lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    lines.append("---")
    path.write_text("\n".join(lines) + "\n\n" + body, encoding="utf-8")


def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def postprocess(text):
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text or "")
    text = re.sub(r"[^\S\n]{2,}", " ", text)
    text = text.replace("\f", "\n\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def format_duration(seconds):
    h, m, s = int(seconds // 3600), int(seconds % 3600 // 60), int(seconds % 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def parse_time_arg(value):
    """'600', '10:00', '00:10:00', '00:10:00.5' 형식을 초 단위로 변환"""
    if value is None:
        return None
    parts = [float(p) for p in value.replace(",", ".").split(":")]
    seconds = 0.0
    for part in parts:
        seconds = seconds * 60 + part
    return seconds


# ── 표 변환 ───────────────────────────────────────────────────
def build_md_table(rows):
    if not rows:
        return ""
    width = len(rows[0])
    header = "| " + " | ".join(rows[0]) + " |"
    divider = "| " + " | ".join(["---"] * width) + " |"
    body = ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join([header, divider] + body)


def rows_to_md(rows):
    if not rows or not rows[0]:
        return ""
    width = max(len(r) for r in rows)
    cells = [
        [re.sub(r"\s+", " ", (c or "")).strip() for c in r] + [""] * (width - len(r))
        for r in rows
    ]
    return build_md_table(cells)


def chunk_by_heading(text, size):
    """제목(#) 단위로 묶은 뒤 기준 크기로 분할. 과대 청크는 문단 단위로 재분할"""
    pattern = re.compile(r"^(#{1,6}\s)", re.MULTILINE)
    parts = pattern.split(text)
    sections, i = [], 0
    while i < len(parts):
        if pattern.match(parts[i]) and i + 1 < len(parts):
            sections.append(parts[i] + parts[i + 1])
            i += 2
        else:
            if parts[i].strip():
                sections.append(parts[i])
            i += 1
    chunks, current = [], ""
    for section in sections:
        if len(current) + len(section) > size and current.strip():
            chunks.append(current.strip())
            current = section
        else:
            current = current + "\n\n" + section if current else section
    if current.strip():
        chunks.append(current.strip())
    final = []
    for chunk in chunks:
        if len(chunk) <= size * CHUNK_OVERFLOW_RATIO:
            final.append(chunk)
            continue
        sub = ""
        for para in chunk.split("\n\n"):
            if len(sub) + len(para) > size and sub.strip():
                final.append(sub.strip())
                sub = para
            else:
                sub = sub + "\n\n" + para if sub else para
        if sub.strip():
            final.append(sub.strip())
    return final or [text]


# ── 문서 파싱 ─────────────────────────────────────────────────
def parse_markitdown(path):
    markitdown = require("markitdown", "markitdown[pdf,docx,pptx,xlsx,xls]")
    converter = markitdown.MarkItDown(enable_plugins=False)
    return converter.convert(str(path)).text_content or ""


def extract_pdf_tables(path):
    """pdfplumber로 페이지별 표를 마크다운으로 변환. 표가 없으면 None"""
    pdfplumber = require("pdfplumber", "pdfplumber")
    blocks = []
    with pdfplumber.open(str(path)) as pdf:
        for page_no, page in enumerate(pdf.pages, 1):
            for table_no, table in enumerate(page.extract_tables(), 1):
                md = rows_to_md(table)
                if md:
                    blocks.append(f"### Page {page_no} Table {table_no}\n\n{md}")
    return "\n\n".join(blocks) if blocks else None


def parse_hwpx(path):
    """export_markdown, TextExtractor, XML 직접 파싱 순서로 시도"""
    require("hwpx", "python-hwpx")
    try:
        from hwpx.tools.exporter import export_markdown
        with open(path, "rb") as f:
            return export_markdown(f.read(), include_tables=True), "python-hwpx/export_markdown", []
    except Exception as exc:
        print(f"[INFO] export_markdown 실패: {exc}", file=sys.stderr)
    try:
        from hwpx.tools.text_extractor import TextExtractor
        with TextExtractor(str(path)) as extractor:
            text = extractor.extract_text(
                paragraph_separator="\n\n", skip_empty=True, include_nested=True,
                object_behavior="skip", preserve_breaks=True,
            )
        return text, "python-hwpx/TextExtractor", []
    except Exception as exc:
        print(f"[INFO] TextExtractor 실패: {exc}", file=sys.stderr)
    return parse_hwpx_xml(path), "beautifulsoup/xml", []


def parse_hwpx_xml(path):
    bs4 = require("bs4", "beautifulsoup4 lxml")
    texts, tables = [], []
    with zipfile.ZipFile(path) as zf:
        sections = sorted(
            n for n in zf.namelist() if n.startswith("Contents/section") and n.endswith(".xml")
        )
        for name in sections:
            soup = bs4.BeautifulSoup(zf.read(name).decode("utf-8"), "lxml-xml")
            for para in soup.find_all("hp:p"):
                text = para.get_text(strip=True)
                if text:
                    texts.append(text)
            for tbl in soup.find_all("hp:tbl"):
                rows = [[c.get_text(strip=True) for c in r.find_all("hp:tc")] for r in tbl.find_all("hp:tr")]
                if rows:
                    tables.append(rows_to_md(rows))
    return "\n\n".join(texts + tables)


def parse_hwp(path):
    """pyhwp(hwp5txt) 우선. 실패하면 olefile 레코드 파싱으로 대체"""
    try:
        result = subprocess.run(
            ["hwp5txt", str(path)], capture_output=True, text=True, timeout=HWP5TXT_TIMEOUT_SEC,
        )
        if result.returncode != 0 or not result.stdout.strip():
            raise RuntimeError(result.stderr.strip()[:200] or "hwp5txt 출력 없음")
        return result.stdout, "pyhwp/hwp5txt", ["hwp_table_placeholder"]
    except Exception as exc:
        print(f"[INFO] pyhwp 실패, olefile 대체 경로 사용: {exc}", file=sys.stderr)
        return parse_hwp_olefile(path), "olefile", ["hwp_olefile_fallback"]


def clean_hwp_text(text):
    # 문단 안의 제어 문자 영역이 한자 조각으로 복호화되는 현상을 줄이기 위해 연속 한자 2자 이상 제거
    text = re.sub(r"[\x00-\x1f]", "", text)
    text = re.sub(r"[\u4E00-\u9FFF]{2,}", "", text)
    text = re.sub(
        r"[^\u0020-\u007E\uAC00-\uD7AF\u3131-\u318E\u2000-\u206F\u00A0-\u00FF"
        r"\u2010-\u2027\u2030-\u205E\u0100-\u024F\u2500-\u25FF·□■○●◦]+", "", text)
    text = re.sub(r"^[^a-zA-Z0-9\uAC00-\uD7AF\u3131-\u318E(□■○●◦\-]+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\uAC00-\uD7AF\u3131-\u318E)□■○●◦.\-?!]+$", "", text)
    return text.strip()


def iter_hwp_para_texts(data):
    """BodyText 레코드 열에서 문단 텍스트 레코드만 추출"""
    i, size = 0, len(data)
    while i + 4 <= size:
        header = struct.unpack_from("<I", data, i)[0]
        tag_id, rec_size = header & 0x3FF, (header >> 20) & 0xFFF
        i += 4
        if rec_size == HWP_EXTENDED_SIZE:
            if i + 4 > size:
                break
            rec_size = struct.unpack_from("<I", data, i)[0]
            i += 4
        if tag_id == HWPTAG_PARA_TEXT:
            yield data[i:min(i + rec_size, size)].decode("utf-16-le", errors="ignore")
        i += rec_size


def parse_hwp_olefile(path):
    olefile = require("olefile", "olefile")
    ole = olefile.OleFileIO(str(path))
    try:
        entries = ole.listdir()
        if ["FileHeader"] not in entries:
            raise ValueError("유효한 HWP 파일이 아님")
        compressed = (ole.openstream("FileHeader").read()[HWP_COMPRESS_OFFSET] & 1) == 1
        sections = sorted(
            (e[1] for e in entries if e[0] == "BodyText"),
            key=lambda name: int(name.replace("Section", "")),
        )
        texts = []
        for name in sections:
            data = ole.openstream(f"BodyText/{name}").read()
            if compressed:
                data = zlib.decompress(data, -15)
            for raw in iter_hwp_para_texts(data):
                text = clean_hwp_text(raw)
                if len(text) > 1:
                    texts.append(text)
        return "\n\n".join(texts)
    finally:
        ole.close()


def parse_document(path):
    """반환값: (본문, 엔진명, 표 마크다운 또는 None, 경고 목록)"""
    ext = path.suffix.lower()
    if ext == ".pdf":
        text = parse_markitdown(path)
        return text, "markitdown", extract_pdf_tables(path), []
    if ext == ".hwpx":
        text, engine, warnings = parse_hwpx(path)
        return text, engine, None, warnings
    if ext == ".hwp":
        text, engine, warnings = parse_hwp(path)
        return text, engine, None, warnings
    return parse_markitdown(path), "markitdown", None, []


# ── 자막 파싱 ─────────────────────────────────────────────────
TIMING_LINE = re.compile(r"^\s*([\d:.,]+)\s*-->\s*([\d:.,]+)")
INLINE_TAG = re.compile(r"<[^>]+>")


def parse_captions(path, start, end, timestamps):
    """반환값: (정제된 줄 목록, 사용한 자막 구간 수). 자동 생성 자막의 반복 줄은 직전 줄과 같으면 생략"""
    raw = path.read_text(encoding="utf-8-sig", errors="replace").replace("\r\n", "\n")
    lines, last, cues = [], None, 0
    for block in re.split(r"\n\s*\n", raw):
        rows = block.strip().split("\n")
        timing_idx = next((k for k, r in enumerate(rows) if TIMING_LINE.match(r)), None)
        if timing_idx is None:
            continue  # WEBVTT 머리글, NOTE, STYLE, 번호만 있는 블록
        cue_start = parse_time_arg(TIMING_LINE.match(rows[timing_idx]).group(1))
        if (start is not None and cue_start < start) or (end is not None and cue_start >= end):
            continue
        cues += 1
        for row in rows[timing_idx + 1:]:
            text = html.unescape(INLINE_TAG.sub("", row)).strip()
            if not text or text == last:
                continue
            last = text
            lines.append(f"[{format_duration(cue_start)}] {text}" if timestamps else text)
    return lines, cues


# ── 음성 전사 ─────────────────────────────────────────────────
def decode_audio(path):
    """ffmpeg가 있으면 16kHz 모노 PCM 파이프로 디코딩. 없으면 faster-whisper 내장 PyAV 디코더 사용"""
    np = require("numpy", "numpy")
    if shutil.which("ffmpeg"):
        cmd = [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(path),
            "-f", "f32le", "-ar", str(SAMPLE_RATE), "-ac", "1", "-",
        ]
        result = subprocess.run(cmd, capture_output=True, timeout=FFMPEG_TIMEOUT_SEC)
        if result.returncode != 0:
            raise RuntimeError(
                "ffmpeg 디코딩 실패: " + result.stderr.decode("utf-8", errors="replace")[:500]
            )
        audio, decoder = np.frombuffer(result.stdout, dtype=np.float32), "ffmpeg"
    else:
        require("faster_whisper", "faster-whisper")
        from faster_whisper.audio import decode_audio as pyav_decode
        audio, decoder = pyav_decode(str(path), sampling_rate=SAMPLE_RATE), "pyav"
    if len(audio) == 0:
        raise RuntimeError("디코딩 결과가 비어 있음 (파일 손상 또는 음성 트랙 없음)")
    return audio, decoder


def transcribe(path, model_size, language, beam_size, start, end, timestamps):
    audio, decoder = decode_audio(path)
    full_duration = len(audio) / SAMPLE_RATE
    offset = start or 0.0
    first = int(offset * SAMPLE_RATE)
    last = int(end * SAMPLE_RATE) if end is not None else len(audio)
    audio = audio[first:last]
    print(f"[DECODE] {path.name} {format_duration(full_duration)} ({decoder})", file=sys.stderr)

    require("faster_whisper", "faster-whisper")
    from faster_whisper import WhisperModel
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    options = {"beam_size": beam_size}
    if language:
        options["language"] = language
    segments, info = model.transcribe(audio, **options)

    lines = []
    for seg in segments:
        text = seg.text.strip()
        if text:
            lines.append(f"[{format_duration(offset + seg.start)}] {text}" if timestamps else text)
    meta = {
        "duration": format_duration(full_duration),
        "language": info.language,
        "language_probability": round(info.language_probability, 2),
        "model": model_size,
        "decoder": decoder,
    }
    return lines, meta


# ── 웹 수신 ───────────────────────────────────────────────────
class HtmlTextExtractor(HTMLParser):
    """trafilatura 실패 시 사용하는 단순 본문 추출기"""
    SKIP = frozenset({"script", "style", "nav", "header", "footer", "noscript", "svg", "iframe"})
    BLOCK = frozenset({
        "p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr", "br", "article", "section",
    })

    def __init__(self):
        super().__init__()
        self.parts, self.skip, self.title, self.in_title = [], 0, "", False

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        if tag == "title":
            self.in_title = True
        if tag in self.BLOCK and self.parts and self.parts[-1] != "\n":
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data.strip()
        if self.skip == 0 and data.strip():
            self.parts.append(data.strip())

    def text(self):
        raw = " ".join(self.parts)
        return re.sub(r"\n\s*\n+", "\n\n", re.sub(r" {2,}", " ", raw)).strip()


def detect_remote_ext(url, content_type):
    mime = content_type.lower().split(";")[0].strip()
    if mime in MIME_TO_EXT:
        return MIME_TO_EXT[mime]
    url_path = unquote(urlparse(url).path).lower()
    for ext in sorted(SUPPORTED_EXTS | DOWNLOAD_ONLY_EXTS, key=len, reverse=True):
        if url_path.endswith(ext) and ext not in {".html", ".htm"}:
            return ext
    return None


def filename_from_url(url, ext):
    base = Path(unquote(urlparse(url).path)).name
    if not base:
        return f"document_{hashlib.md5(url.encode()).hexdigest()[:8]}{ext}"
    return base if base.lower().endswith(ext) else base + ext


def extract_web_page(page_html, url):
    trafilatura = require("trafilatura", "trafilatura")
    fallback = HtmlTextExtractor()
    try:
        fallback.feed(page_html)
    except Exception:
        pass
    text, engine = None, "trafilatura"
    try:
        text = trafilatura.extract(
            page_html, include_comments=False, include_tables=True, output_format="txt"
        )
    except Exception:
        text = None
    if not text or len(text.strip()) <= MIN_WEB_TEXT_CHARS:
        text, engine = fallback.text(), "htmlparser_fallback"
    meta = {"title": fallback.title}
    try:
        found = trafilatura.extract_metadata(page_html, default_url=url)
        if found:
            meta.update({
                "title": found.title or fallback.title,
                "author": found.author,
                "date": found.date,
                "site": found.sitename,
            })
    except Exception:
        pass
    return text, engine, meta


def handle_url(url, args):
    httpx = require("httpx", "httpx")
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": ACCEPT_LANGUAGE,
    }
    if detect_remote_ext(url, "") is not None:
        headers["Accept"] = "*/*"
    resp = httpx.get(url, headers=headers, timeout=args.timeout, follow_redirects=True)
    resp.raise_for_status()
    final_url, content_type = str(resp.url), resp.headers.get("content-type", "")
    ext = detect_remote_ext(final_url, content_type)

    if ext is not None:
        filename = filename_from_url(final_url, ext)
        if args.download:
            local = unique_path(args.out_dir / DOWNLOAD_SUBDIR, filename)
            local.write_bytes(resp.content)
            print(f"[DOWNLOAD] {local} ({len(resp.content):,} bytes)", file=sys.stderr)
            result = process_file(local, args, source=final_url)
            result["download_path"] = str(local)
            return result
        with tempfile.TemporaryDirectory() as tmp:
            local = Path(tmp) / filename
            local.write_bytes(resp.content)
            return process_file(local, args, source=final_url)

    mime = content_type.lower().split(";")[0].strip()
    if "text/html" not in mime and "application/xhtml" not in mime:
        return {"source": final_url, "kind": "unsupported", "content_type": content_type,
                "warnings": ["unsupported_content_type"]}

    text, engine, meta = extract_web_page(resp.text, final_url)
    text, truncated = truncate(postprocess(text), args.max_chars)
    out = unique_path(args.out_dir, f"web_{hashlib.md5(final_url.encode()).hexdigest()[:8]}.md")
    write_markdown(out, {"source": final_url, **meta, "engine": engine,
                         "fetched_at": now_utc(), "char_count": len(text)}, text)
    return {"source": final_url, "kind": "web", "engine": engine, "output_path": str(out),
            "char_count": len(text), "truncated": truncated, **meta}


# ── 파일 처리 ─────────────────────────────────────────────────
def process_file(path, args, source=None):
    source = source or str(path)
    ext = path.suffix.lower()
    base = {"source": source, "format": ext.lstrip("."), "warnings": []}

    if ext in DOWNLOAD_ONLY_EXTS or ext not in SUPPORTED_EXTS:
        return {**base, "kind": "unsupported", "warnings": ["unsupported_extract"]}

    if ext in CAPTION_EXTS:
        lines, cues = parse_captions(path, args.start, args.end, args.timestamps)
        text, truncated = truncate("\n".join(lines), args.max_chars)
        out = unique_path(args.out_dir, f"{path.stem}_captions.md")
        write_markdown(out, {"source": source, "format": base["format"], "engine": "caption_cleaner",
                             "cue_count": cues, "parsed_at": now_utc(), "char_count": len(text)}, text)
        return {**base, "kind": "captions", "engine": "caption_cleaner", "output_path": str(out),
                "cue_count": cues, "char_count": len(text), "truncated": truncated}

    if ext in MEDIA_EXTS:
        lines, meta = transcribe(path, args.model, args.language, args.beam_size,
                                 args.start, args.end, args.timestamps)
        text, truncated = truncate("\n".join(lines), args.max_chars)
        out = unique_path(args.out_dir, f"{path.stem}_transcript.md")
        write_markdown(out, {"source": source, "format": base["format"], "engine": "faster-whisper",
                             **meta, "parsed_at": now_utc(), "char_count": len(text)}, text)
        return {**base, "kind": "media", "engine": "faster-whisper", "output_path": str(out),
                "char_count": len(text), "truncated": truncated, **meta}

    text, engine, tables_md, warnings = parse_document(path)
    text = postprocess(text)
    if len(text) < MIN_DOC_TEXT_CHARS:
        warnings.append("text_empty")
    result = {**base, "kind": "document", "engine": engine, "warnings": warnings}

    if args.chunk:
        chunk_dir = args.out_dir / f"{path.stem}_chunks"
        chunk_dir.mkdir(parents=True, exist_ok=True)
        chunks = chunk_by_heading(text, args.chunk_size)
        paths = []
        for idx, chunk in enumerate(chunks, 1):
            out = chunk_dir / f"{path.stem}_chunk_{idx:03d}.md"
            write_markdown(out, {"source": source, "format": base["format"], "engine": engine,
                                 "parsed_at": now_utc(), "char_count": len(chunk),
                                 "chunk": idx, "total_chunks": len(chunks)}, chunk)
            paths.append(str(out))
        result.update({"chunk_paths": paths, "char_count": len(text), "truncated": False})
    else:
        text, truncated = truncate(text, args.max_chars)
        out = unique_path(args.out_dir, f"{path.stem}_parsed.md")
        write_markdown(out, {"source": source, "format": base["format"], "engine": engine,
                             "parsed_at": now_utc(), "char_count": len(text)}, text)
        result.update({"output_path": str(out), "char_count": len(text), "truncated": truncated})

    if tables_md:
        out = unique_path(args.out_dir, f"{path.stem}_tables.md")
        write_markdown(out, {"source": source, "format": base["format"], "engine": "pdfplumber",
                             "parsed_at": now_utc(), "char_count": len(tables_md)}, tables_md)
        result["tables_path"] = str(out)
    return result


# ── 다운로드 관리 ─────────────────────────────────────────────
def list_downloads(out_dir):
    folder = out_dir / DOWNLOAD_SUBDIR
    return [f for f in folder.glob("*") if f.is_file()] if folder.exists() else []


def bundle_downloads(out_dir, zip_name):
    files = list_downloads(out_dir)
    if not files:
        return {"bundled": False, "reason": "다운로드 파일 없음", "file_count": 0}
    zip_path = unique_path(out_dir, zip_name)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, f.name)
    return {"bundled": True, "zip_path": str(zip_path), "file_count": len(files),
            "zip_bytes": zip_path.stat().st_size}


def clean_downloads(out_dir):
    files = list_downloads(out_dir)
    for f in files:
        f.unlink()
    return {"cleaned": True, "files_removed": len(files)}


# ── 명령행 ────────────────────────────────────────────────────
def build_parser():
    ap = argparse.ArgumentParser(description="digest 입력 자료 텍스트 추출")
    ap.add_argument("source", nargs="?", help="파일 경로 또는 http(s) 주소")
    ap.add_argument("--out-dir", type=Path, default=WORK_DIR, help="결과 저장 폴더")
    ap.add_argument("--max-chars", type=int, default=0, help="본문 최대 글자 수 (0은 제한 없음)")
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SEC, help="웹 요청 제한 시간(초)")
    ap.add_argument("--download", action="store_true", help="웹 주소의 원본 파일을 downloads 폴더에 보관")
    ap.add_argument("--chunk", action="store_true", help="문서를 제목 단위 청크 파일로 분할")
    ap.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE, help="청크 기준 글자 수")
    ap.add_argument("--start", help="자막 및 음성 처리 시작 시각 (예: 00:10:00)")
    ap.add_argument("--end", help="자막 및 음성 처리 종료 시각 (예: 00:25:00)")
    ap.add_argument("--timestamps", action="store_true", help="자막 및 전사 줄 앞에 시각 표기")
    ap.add_argument("--model", default=DEFAULT_MODEL, choices=MODEL_CHOICES, help="Whisper 모델 크기")
    ap.add_argument("--language", default=None, help="음성 언어 코드 (예: ko, en). 미지정 시 자동 감지")
    ap.add_argument("--beam-size", type=int, default=DEFAULT_BEAM_SIZE, help="빔 서치 크기")
    ap.add_argument("--bundle", nargs="?", const=DEFAULT_BUNDLE_NAME, help="downloads 폴더 파일을 ZIP으로 묶음")
    ap.add_argument("--clean", action="store_true", help="downloads 폴더 파일 삭제")
    return ap


def main():
    ap = build_parser()
    args = ap.parse_args()
    args.start, args.end = parse_time_arg(args.start), parse_time_arg(args.end)
    try:
        if args.clean:
            output = clean_downloads(args.out_dir)
        elif args.bundle:
            output = bundle_downloads(args.out_dir, args.bundle)
        elif not args.source:
            ap.error("source, --bundle, --clean 중 하나 필요")
        elif re.match(r"^https?://", args.source, re.IGNORECASE):
            output = handle_url(args.source, args)
        else:
            path = Path(args.source)
            if not path.exists():
                raise FileNotFoundError(f"파일 없음: {path}")
            output = process_file(path, args)
        print(json.dumps(output, ensure_ascii=False, indent=2))
    except MissingDependency as exc:
        print(json.dumps({"error": "missing_dependency", "install": f"pip install {exc}"},
                         ensure_ascii=False, indent=2))
        sys.exit(2)
    except Exception as exc:
        message = str(exc)
        code = "encrypted" if re.search(r"password|encrypt", message, re.IGNORECASE) else "failed"
        status = getattr(getattr(exc, "response", None), "status_code", None)
        traceback.print_exc(file=sys.stderr)
        print(json.dumps({"error": code, "status_code": status, "detail": message[:500]},
                         ensure_ascii=False, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
