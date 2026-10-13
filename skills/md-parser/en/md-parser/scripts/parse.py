#!/usr/bin/env python3
"""md-parser: converts document files to Markdown

Engines
    PDF   markitdown (body) + pdfplumber (ruled tables, separate file only when tables exist)
    HWPX  python-hwpx export_markdown -> TextExtractor -> BeautifulSoup
          if shapes such as text boxes contain text, add the TextExtractor full text as a separate file
    HWP   pyhwp hwp5txt -> direct olefile parsing
          if the hwp5txt result contains <표> or <그림> placeholders, add the olefile full text as a separate file
    Other markitdown

Usage
    python parse.py <input file> <output.md>
    python parse.py <input file> <output folder> --chunk [--chunk-size 2000]
    python parse.py <audio file or zip with audio> <output.md> --allow-audio-upload

본 제품은 한컴의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.
(This product was developed with reference to the HWP document file (.hwp) specification published by Hancom.)
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
# Settings
# ---------------------------------------------------------------------------
DEFAULT_CHUNK_SIZE = 2000
# A heading-based chunk larger than this multiple of the target size is split again by paragraph
OVERSIZE_CHUNK_FACTOR = 1.5
HWP5TXT_TIMEOUT_SEC = 60

# markitdown sends audio to a Google speech recognition service, so audio is never processed without user consent
AUDIO_EXTENSIONS = {".wav", ".mp3", ".m4a", ".mp4"}

# pyhwp hwp5txt replaces tables and shapes with these strings and omits their content
HWP5TXT_PLACEHOLDERS = ("<표>", "<그림>")

HWPX_SECTION_PATTERN = r"Contents/section\d+\.xml"
# python-hwpx export_markdown does not output this element (text inside shapes)
HWPX_SHAPE_TEXT_TAG = b"drawText"

# Constants from the published HWP 5.0 specification
HWPTAG_PARA_TEXT = 67                 # HWPTAG_BEGIN(16) + 51
HWP_RECORD_SIZE_EXTENDED = 0xFFF      # when the size field has this value, the next 4 bytes hold the real size
HWP_FLAG_COMPRESSED = 0x1
HWP_FLAG_PASSWORD = 0x2
HWP_FLAG_DISTRIBUTION = 0x4
HWP_CONTROL_WCHARS = 8                # WCHARs taken by inline and extended control characters
HWP_SINGLE_WCHAR_CONTROLS = {0, 10, 13, 24, 25, 26, 27, 28, 29, 30, 31}
HWP_CONTROL_TO_TEXT = {9: "\t", 10: "\n", 24: "-", 30: " ", 31: " "}


# ---------------------------------------------------------------------------
# Format detection
# ---------------------------------------------------------------------------
def detect_format(filepath: str) -> str:
    ext = Path(filepath).suffix.lower()
    if ext in (".pdf", ".hwp", ".hwpx"):
        return ext.lstrip(".")
    # markitdown decides whether other formats are supported and raises an error if not
    return "markitdown"


def contains_audio(filepath: str) -> bool:
    path = Path(filepath)
    if path.suffix.lower() in AUDIO_EXTENSIONS:
        return True
    # markitdown also converts files inside a zip, so audio inside a zip would be sent too
    if path.suffix.lower() == ".zip" and zipfile.is_zipfile(filepath):
        with zipfile.ZipFile(filepath) as zf:
            return any(Path(n).suffix.lower() in AUDIO_EXTENSIONS for n in zf.namelist())
    return False


# ---------------------------------------------------------------------------
# Engine chain: an empty result also counts as a failure and moves on to the next engine
# ---------------------------------------------------------------------------
def run_engine_chain(filepath: str, engines: list) -> tuple:
    errors, raised = [], False
    for name, engine in engines:
        try:
            text = engine(filepath)
            if text and text.strip():
                return text, name
            errors.append(f"{name}: empty result")
        except Exception as e:
            errors.append(f"{name}: {e}")
            raised = True
        print(f"[INFO] {errors[-1]} -> switching to next engine", file=sys.stderr)
    # if every engine returned an empty result without errors, treat the source as an empty document
    if not raised:
        return "", engines[0][0]
    raise RuntimeError(" / ".join(errors))


# ---------------------------------------------------------------------------
# markitdown (PDF body and other formats)
# ---------------------------------------------------------------------------
def parse_with_markitdown(filepath: str) -> str:
    from markitdown import MarkItDown
    result = MarkItDown(enable_plugins=False).convert(filepath)
    return result.text_content or ""


# ---------------------------------------------------------------------------
# PDF tables: pdfplumber
# ---------------------------------------------------------------------------
def extract_pdf_tables(filepath: str) -> Optional[str]:
    """Return None when there are no tables"""
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
    """Read section XML directly when python-hwpx fails. Tables are collected after the body text"""
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
                    continue  # paragraphs inside tables are handled by the table conversion below
                # text of nested paragraphs (text boxes etc.) is output with that paragraph, so skip it here
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
# HWP: pyhwp -> direct olefile parsing
# ---------------------------------------------------------------------------
def parse_hwp_pyhwp(filepath: str) -> str:
    # run hwp5txt with the current Python so the same environment's pyhwp is used regardless of PATH
    # hwp5txt writes UTF-8 bytes, so decode as UTF-8 regardless of the OS default encoding
    cmd = [sys.executable, "-c",
           "import sys; from hwp5.hwp5txt import main; sys.exit(main())", filepath]
    result = subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="replace",
                            timeout=HWP5TXT_TIMEOUT_SEC)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"exit code {result.returncode}")
    return result.stdout


def parse_hwp_olefile(filepath: str) -> str:
    """Read paragraph text records in BodyText sections following the published HWP 5.0 structure"""
    import olefile
    with olefile.OleFileIO(filepath) as ole:
        if not ole.exists("FileHeader"):
            raise ValueError("not an HWP 5.0 document")
        flags = struct.unpack_from("<I", ole.openstream("FileHeader").read(), 36)[0]
        if flags & HWP_FLAG_PASSWORD:
            raise ValueError("password-protected document")
        if flags & HWP_FLAG_DISTRIBUTION:
            raise ValueError("distribution document with an encrypted body")
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
    """A record header holds a 10-bit tag, a 10-bit level, and a 12-bit size"""
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
    """Control characters (0-31) take 1 or 8 WCHARs depending on their type, so skip that many"""
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
# Markdown table conversion
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
# Post-processing, metadata, chunks
# ---------------------------------------------------------------------------
def postprocess(text: str) -> str:
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    # keep leading indentation because it defines list nesting and code blocks; collapse only spaces between characters
    text = re.sub(r"(?<=\S)[^\S\n]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def build_metadata(source: str, fmt: str, engine: str, char_count: int,
                   chunk_idx: Optional[int] = None, total: Optional[int] = None) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # write as a JSON string so YAML stays valid even if the file name contains a colon
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
    """Split at headings (#), group by size, and split oversized chunks again by paragraph"""
    sections = [s for s in re.split(r"(?m)^(?=#{1,6}\s)", text) if s.strip()]
    final = []
    for chunk in split_by_size(sections, size):
        if len(chunk) <= size * OVERSIZE_CHUNK_FACTOR:
            final.append(chunk)
        else:
            final.extend(split_by_size(chunk.split("\n\n"), size))
    return final or [text]


# ---------------------------------------------------------------------------
# File writing
# ---------------------------------------------------------------------------
def write_md(path: Path, metadata: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(metadata + "\n\n" + body, encoding="utf-8")
    print(f"[INFO] saved: {path}")


def write_extra_file(out_dir: Path, name: str, src: str, ext: str,
                     engine: str, producer: Callable[[], Optional[str]]) -> None:
    """Write a supplementary file (PDF tables, HWP or HWPX full text) next to the body file only when it has content"""
    try:
        content = producer()
    except Exception as e:
        print(f"[WARN] failed to create {name}: {e}", file=sys.stderr)
        return
    if not content or not content.strip():
        print(f"[INFO] {name} has no content (file not created)")
        return
    content = postprocess(content)
    write_md(out_dir / name, build_metadata(src, ext, engine, len(content)), content)


# ---------------------------------------------------------------------------
# Main
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
    ap = argparse.ArgumentParser(description="Convert document files to Markdown")
    ap.add_argument("input", help="input file path")
    ap.add_argument("output", help="output .md file path (output folder with --chunk)")
    ap.add_argument("--chunk", action="store_true", help="split by headings and paragraphs")
    ap.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE, help="target characters per chunk")
    ap.add_argument("--allow-audio-upload", action="store_true",
                    help="set only when the user agreed to send audio to an external speech recognition service")
    args = ap.parse_args()

    src_path = Path(args.input)
    if not src_path.is_file():
        print(f"[ERROR] file not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    if contains_audio(args.input) and not args.allow_audio_upload:
        print("[ERROR] audio conversion sends the audio to a Google speech recognition service. "
              "Get the user's consent, then run again with --allow-audio-upload", file=sys.stderr)
        sys.exit(2)

    fmt = detect_format(args.input)
    src, stem = src_path.name, src_path.stem
    ext = src_path.suffix.lower().lstrip(".")
    print(f"[INFO] input: {src} | format: {fmt}")

    try:
        text, engine = parse(args.input, fmt)
    except Exception as e:
        print(f"[ERROR] parsing failed: {e}", file=sys.stderr)
        sys.exit(1)

    text = postprocess(text)
    print(f"[INFO] engine: {engine} | characters: {len(text):,}")
    if not text:
        print("[WARN] no text extracted", file=sys.stderr)

    if args.chunk:
        out_dir = Path(args.output)
        chunks = chunk_by_heading(text, args.chunk_size)
        print(f"[INFO] chunks: {len(chunks)}")
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

    print("[INFO] done")


if __name__ == "__main__":
    main()
