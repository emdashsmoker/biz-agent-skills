#!/usr/bin/env python3
"""digest input extraction script

Detects the type of one input, converts it to a markdown file, and prints a JSON summary

Processing path by input type
    Web address (http, https)  fetched with httpx; web pages go to trafilatura, files go to the file path
    Caption file (.srt, .vtt)  timing lines, markup tags, and consecutive duplicate lines removed
    Audio and video files      local transcription with faster-whisper (ffmpeg first, PyAV decoding if absent)
    Documents                  PDF via markitdown and pdfplumber, HWPX via python-hwpx, HWP via pyhwp and olefile, others via markitdown

Notice for the HWP fallback parser (parse_hwp_olefile)
    본 제품은 한글과컴퓨터의 한/글 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.
    (This product was developed with reference to the public HWP document file (.hwp) specification published by Hancom Inc.)

Examples
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

# ── Settings ─────────────────────────────────────────────────
WORK_DIR = Path(os.environ.get("DIGEST_WORK_DIR", "digest_work"))
DOWNLOAD_SUBDIR = "downloads"
ACCEPT_LANGUAGE = os.environ.get(
    "DIGEST_ACCEPT_LANGUAGE", "en-US,en;q=0.9"
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

# Named thresholds used across the script
CHUNK_OVERFLOW_RATIO = 1.5   # heading chunks larger than 1.5x the target are split again by paragraph
MIN_WEB_TEXT_CHARS = 50      # shorter trafilatura output counts as a failure and triggers the fallback extractor
MIN_DOC_TEXT_CHARS = 10      # shorter document text is treated as an image-based document
SAMPLE_RATE = 16000          # Whisper input format (16 kHz mono)
FFMPEG_TIMEOUT_SEC = 600
HWP5TXT_TIMEOUT_SEC = 60
TRUNCATION_MARK = "\n\n[... truncated ...]"

# HWP 5.0 record layout (per the public HWP document file format 5.0 specification)
HWPTAG_PARA_TEXT = 67        # HWPTAG_BEGIN(0x10) + 51
HWP_EXTENDED_SIZE = 0xFFF    # when the size field holds this value, the next 4 bytes carry the real size
HWP_COMPRESS_OFFSET = 36     # FileHeader attribute field offset, bit 0 marks compression

# ── Extension groups ─────────────────────────────────────────
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
DOWNLOAD_ONLY_EXTS = {".doc", ".ppt"}  # legacy formats with no text extraction engine
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


# ── Common utilities ─────────────────────────────────────────
class MissingDependency(Exception):
    """A required package is missing. Kept as its own exception so the install command reaches the user unchanged"""


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
    """Write YAML front matter and body. Values are JSON-quoted so special characters do not break the YAML"""
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
    """Convert '600', '10:00', '00:10:00', or '00:10:00.5' to seconds"""
    if value is None:
        return None
    parts = [float(p) for p in value.replace(",", ".").split(":")]
    seconds = 0.0
    for part in parts:
        seconds = seconds * 60 + part
    return seconds


# ── Table conversion ─────────────────────────────────────────
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
    """Group by headings (#), then split to the target size. Oversized chunks are split again by paragraph"""
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


# ── Document parsing ─────────────────────────────────────────
def parse_markitdown(path):
    markitdown = require("markitdown", "markitdown[pdf,docx,pptx,xlsx,xls]")
    converter = markitdown.MarkItDown(enable_plugins=False)
    return converter.convert(str(path)).text_content or ""


def extract_pdf_tables(path):
    """Convert tables on each page to markdown with pdfplumber. Returns None when there are no tables"""
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
    """Try export_markdown, then TextExtractor, then direct XML parsing"""
    require("hwpx", "python-hwpx")
    try:
        from hwpx.tools.exporter import export_markdown
        with open(path, "rb") as f:
            return export_markdown(f.read(), include_tables=True), "python-hwpx/export_markdown", []
    except Exception as exc:
        print(f"[INFO] export_markdown failed: {exc}", file=sys.stderr)
    try:
        from hwpx.tools.text_extractor import TextExtractor
        with TextExtractor(str(path)) as extractor:
            text = extractor.extract_text(
                paragraph_separator="\n\n", skip_empty=True, include_nested=True,
                object_behavior="skip", preserve_breaks=True,
            )
        return text, "python-hwpx/TextExtractor", []
    except Exception as exc:
        print(f"[INFO] TextExtractor failed: {exc}", file=sys.stderr)
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
    """Use pyhwp (hwp5txt) first. Fall back to olefile record parsing on failure"""
    try:
        result = subprocess.run(
            ["hwp5txt", str(path)], capture_output=True, text=True, timeout=HWP5TXT_TIMEOUT_SEC,
        )
        if result.returncode != 0 or not result.stdout.strip():
            raise RuntimeError(result.stderr.strip()[:200] or "hwp5txt produced no output")
        return result.stdout, "pyhwp/hwp5txt", ["hwp_table_placeholder"]
    except Exception as exc:
        print(f"[INFO] pyhwp failed, using the olefile fallback: {exc}", file=sys.stderr)
        return parse_hwp_olefile(path), "olefile", ["hwp_olefile_fallback"]


def clean_hwp_text(text):
    # Control-character payloads inside paragraphs decode into stray CJK ideographs, so runs of 2+ ideographs are removed
    text = re.sub(r"[\x00-\x1f]", "", text)
    text = re.sub(r"[\u4E00-\u9FFF]{2,}", "", text)
    text = re.sub(
        r"[^\u0020-\u007E\uAC00-\uD7AF\u3131-\u318E\u2000-\u206F\u00A0-\u00FF"
        r"\u2010-\u2027\u2030-\u205E\u0100-\u024F\u2500-\u25FF·□■○●◦]+", "", text)
    text = re.sub(r"^[^a-zA-Z0-9\uAC00-\uD7AF\u3131-\u318E(□■○●◦\-]+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\uAC00-\uD7AF\u3131-\u318E)□■○●◦.\-?!]+$", "", text)
    return text.strip()


def iter_hwp_para_texts(data):
    """Yield only paragraph text records from a BodyText record stream"""
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
            raise ValueError("not a valid HWP file")
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
    """Returns: (text, engine name, table markdown or None, warning list)"""
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


# ── Caption parsing ──────────────────────────────────────────
TIMING_LINE = re.compile(r"^\s*([\d:.,]+)\s*-->\s*([\d:.,]+)")
INLINE_TAG = re.compile(r"<[^>]+>")


def parse_captions(path, start, end, timestamps):
    """Returns: (cleaned lines, number of cues used). A line equal to the previous line is skipped, which removes rolling repeats in auto-generated captions"""
    raw = path.read_text(encoding="utf-8-sig", errors="replace").replace("\r\n", "\n")
    lines, last, cues = [], None, 0
    for block in re.split(r"\n\s*\n", raw):
        rows = block.strip().split("\n")
        timing_idx = next((k for k, r in enumerate(rows) if TIMING_LINE.match(r)), None)
        if timing_idx is None:
            continue  # WEBVTT header, NOTE, STYLE, or index-only block
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


# ── Transcription ────────────────────────────────────────────
def decode_audio(path):
    """Decode to 16 kHz mono PCM through an ffmpeg pipe when ffmpeg exists. Otherwise use the PyAV decoder bundled with faster-whisper"""
    np = require("numpy", "numpy")
    if shutil.which("ffmpeg"):
        cmd = [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(path),
            "-f", "f32le", "-ar", str(SAMPLE_RATE), "-ac", "1", "-",
        ]
        result = subprocess.run(cmd, capture_output=True, timeout=FFMPEG_TIMEOUT_SEC)
        if result.returncode != 0:
            raise RuntimeError(
                "ffmpeg decoding failed: " + result.stderr.decode("utf-8", errors="replace")[:500]
            )
        audio, decoder = np.frombuffer(result.stdout, dtype=np.float32), "ffmpeg"
    else:
        require("faster_whisper", "faster-whisper")
        from faster_whisper.audio import decode_audio as pyav_decode
        audio, decoder = pyav_decode(str(path), sampling_rate=SAMPLE_RATE), "pyav"
    if len(audio) == 0:
        raise RuntimeError("decoded audio is empty (damaged file or no audio track)")
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


# ── Web fetching ─────────────────────────────────────────────
class HtmlTextExtractor(HTMLParser):
    """Simple text extractor used when trafilatura fails"""
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


# ── File processing ──────────────────────────────────────────
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


# ── Download management ──────────────────────────────────────
def list_downloads(out_dir):
    folder = out_dir / DOWNLOAD_SUBDIR
    return [f for f in folder.glob("*") if f.is_file()] if folder.exists() else []


def bundle_downloads(out_dir, zip_name):
    files = list_downloads(out_dir)
    if not files:
        return {"bundled": False, "reason": "no downloaded files", "file_count": 0}
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


# ── Command line ─────────────────────────────────────────────
def build_parser():
    ap = argparse.ArgumentParser(description="digest input extraction")
    ap.add_argument("source", nargs="?", help="file path or http(s) address")
    ap.add_argument("--out-dir", type=Path, default=WORK_DIR, help="output folder")
    ap.add_argument("--max-chars", type=int, default=0, help="maximum characters of body text (0 means no limit)")
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SEC, help="web request timeout in seconds")
    ap.add_argument("--download", action="store_true", help="keep the original file of a web address in the downloads folder")
    ap.add_argument("--chunk", action="store_true", help="split documents into heading-based chunk files")
    ap.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE, help="target characters per chunk")
    ap.add_argument("--start", help="start time for captions and audio (e.g. 00:10:00)")
    ap.add_argument("--end", help="end time for captions and audio (e.g. 00:25:00)")
    ap.add_argument("--timestamps", action="store_true", help="prefix caption and transcript lines with a time")
    ap.add_argument("--model", default=DEFAULT_MODEL, choices=MODEL_CHOICES, help="Whisper model size")
    ap.add_argument("--language", default=None, help="audio language code (e.g. ko, en). Detected automatically when omitted")
    ap.add_argument("--beam-size", type=int, default=DEFAULT_BEAM_SIZE, help="beam search size")
    ap.add_argument("--bundle", nargs="?", const=DEFAULT_BUNDLE_NAME, help="bundle files in the downloads folder into one ZIP")
    ap.add_argument("--clean", action="store_true", help="delete files in the downloads folder")
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
            ap.error("one of source, --bundle, or --clean is required")
        elif re.match(r"^https?://", args.source, re.IGNORECASE):
            output = handle_url(args.source, args)
        else:
            path = Path(args.source)
            if not path.exists():
                raise FileNotFoundError(f"file not found: {path}")
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
