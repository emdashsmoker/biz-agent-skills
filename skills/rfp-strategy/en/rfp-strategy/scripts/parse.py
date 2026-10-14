#!/usr/bin/env python3
"""
Convert document files to Markdown (.md).

Engine mapping
    PDF  -> markitdown (body) + pdfplumber (tables, separate file only when tables exist)
    HWPX -> python-hwpx export_markdown -> TextExtractor -> BeautifulSoup XML parsing
    HWP  -> pyhwp hwp5txt -> olefile binary parsing
    Other -> markitdown

Usage
    python parse.py <input file> <output file.md>
    python parse.py <input file> <output folder> --chunk [--chunk-size 2000]

Notice for the HWP binary parsing path (_parse_hwp_olefile)
    본 제품은 한컴의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.
    (This product was developed with reference to the HWP document file (.hwp) specification published by Hancom.)
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
# Settings
# ---------------------------------------------------------------------------
DEFAULT_CHUNK_SIZE = 2000          # default characters per chunk
CHUNK_OVERSIZE_RATIO = 1.5         # re-split by paragraph when a heading chunk exceeds this multiple
HWP5TXT_TIMEOUT_SEC = 60           # time limit for hwp5txt

# Values from the public HWP 5.0 file format document
HWP_PROPERTY_OFFSET = 36           # offset of the properties field in FileHeader
HWP_COMPRESSED_FLAG = 0x01         # bit 0 of properties: body is compressed
HWPTAG_PARA_TEXT = 67              # HWPTAG_BEGIN(16) + 51, paragraph text record
HWP_TAG_ID_MASK = 0x3FF            # lower 10 bits of record header: tag ID
HWP_SIZE_SHIFT = 20                # upper 12 bits of record header: record size
HWP_SIZE_MASK = 0xFFF
HWP_RECORD_HEADER_BYTES = 4

MARKITDOWN_FORMATS = {
    ".docx", ".doc", ".pptx", ".ppt", ".xlsx", ".xls",
    ".csv", ".json", ".xml", ".html", ".htm", ".txt", ".epub",
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".wav", ".mp3", ".zip",
}


# ---------------------------------------------------------------------------
# Format detection
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
# PDF: body with markitdown, tables with pdfplumber
# ---------------------------------------------------------------------------
def parse_pdf(filepath: str) -> tuple:
    """Extract PDF body text. Table structure is lost here, so extract_pdf_tables handles tables."""
    return parse_with_markitdown(filepath), "markitdown"


def extract_pdf_tables(filepath: str) -> Optional[str]:
    """Return PDF tables as Markdown tables, or None if there are no tables."""
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
# markitdown (shared)
# ---------------------------------------------------------------------------
def parse_with_markitdown(filepath: str) -> str:
    from markitdown import MarkItDown

    result = MarkItDown(enable_plugins=False).convert(filepath)
    return result.text_content or ""


# ---------------------------------------------------------------------------
# HWPX: try export_markdown first because it renders tables as Markdown tables
# ---------------------------------------------------------------------------
def parse_hwpx(filepath: str) -> tuple:
    """Move to the next engine when one raises an error or returns nothing."""
    engines = [
        (_parse_hwpx_export_markdown, "python-hwpx/export_markdown"),
        (_parse_hwpx_text_extractor, "python-hwpx/TextExtractor"),
    ]
    for func, name in engines:
        try:
            text = func(filepath)
        except Exception as e:
            print(f"[INFO] {name} failed: {e}", file=sys.stderr)
            continue
        if text and text.strip():
            return text, name
        print(f"[INFO] {name} returned no text", file=sys.stderr)
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
    """HWPX is XML inside a ZIP, so read the section XML directly."""
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
# HWP: pyhwp by default, olefile parsing if pyhwp is missing or fails
# ---------------------------------------------------------------------------
def parse_hwp(filepath: str) -> tuple:
    try:
        return _parse_hwp_pyhwp(filepath), "pyhwp/hwp5txt"
    except Exception as e1:
        print(f"[INFO] pyhwp failed: {e1}", file=sys.stderr)
        print("[INFO] switching to olefile path", file=sys.stderr)
        return _parse_hwp_olefile(filepath), "olefile"


def _parse_hwp_pyhwp(filepath: str) -> str:
    """Run pyhwp's hwp5txt as a separate process. Tables are replaced with <표>."""
    result = subprocess.run(
        ["hwp5txt", filepath], capture_output=True, text=True,
        timeout=HWP5TXT_TIMEOUT_SEC,
    )
    if result.returncode != 0:
        raise RuntimeError(f"hwp5txt failed: {result.stderr.strip()}")
    if not result.stdout.strip():
        raise RuntimeError("hwp5txt returned empty output")
    return result.stdout


def _parse_hwp_olefile(filepath: str) -> str:
    """Read only paragraph text records, following the record layout in the public HWP 5.0 document.

    Paragraphs inside tables use the same record, so table text is extracted too.
    Inline object control characters can turn into garbage characters, so the text is cleaned below.
    The cleaning also removes runs of two or more Chinese characters, so Hanja may drop out.
    """
    import olefile

    f = olefile.OleFileIO(filepath)
    try:
        dirs = f.listdir()
        if ["FileHeader"] not in dirs:
            raise ValueError("not a valid HWP file")
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
            # if the size field is at its maximum, the real size is in the next 4 bytes (long paragraphs)
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
# Table and text cleanup
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
# Chunking: group by heading, re-split oversized groups by paragraph
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
# Run
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
        print(f"[INFO] chunks: {len(chunks)}")
        for idx, chunk in enumerate(chunks, 1):
            meta = build_metadata(src, ext, engine, len(chunk), idx, len(chunks))
            (out_dir / f"{stem}_chunk_{idx:03d}.md").write_text(meta + "\n\n" + chunk, encoding="utf-8")
    else:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build_metadata(src, ext, engine, len(text)) + "\n\n" + text, encoding="utf-8")
        print(f"[INFO] saved: {out}")


def write_pdf_tables(args, src: str, stem: str, ext: str) -> None:
    try:
        tables_md = extract_pdf_tables(args.input)
    except Exception as e:
        print(f"[WARN] table extraction failed: {e}", file=sys.stderr)
        return
    if not tables_md:
        print("[INFO] no tables in PDF (no table file created)")
        return
    base = Path(args.output) if args.chunk else Path(args.output).parent
    tbl_path = base / f"{stem}_tables.md"
    meta = build_metadata(src, ext, "pdfplumber", len(tables_md))
    tbl_path.write_text(meta + "\n\n" + tables_md, encoding="utf-8")
    print(f"[INFO] table file: {tbl_path}")


def main():
    ap = argparse.ArgumentParser(description="Convert document files to Markdown")
    ap.add_argument("input", help="input file path")
    ap.add_argument("output", help="output file path, or output folder for chunks")
    ap.add_argument("--chunk", action="store_true", help="split by heading and save as multiple files")
    ap.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE)
    args = ap.parse_args()

    if not os.path.exists(args.input):
        print(f"[ERROR] file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    fmt = detect_format(args.input)
    if fmt == "unknown":
        print(f"[ERROR] unsupported format: {Path(args.input).suffix}", file=sys.stderr)
        sys.exit(1)

    src = Path(args.input).name
    stem = Path(args.input).stem
    ext = Path(args.input).suffix.lower().lstrip(".")
    print(f"[INFO] input: {src} | format: {fmt}")

    try:
        text, engine = parse(args.input, fmt)
    except Exception as e:
        print(f"[ERROR] conversion failed: {e}", file=sys.stderr)
        sys.exit(1)

    text = postprocess(text)
    print(f"[INFO] engine: {engine} | characters: {len(text):,}")
    if not text:
        print("[WARN] no text extracted. OCR is needed if this is a scanned image document", file=sys.stderr)

    write_outputs(args, text, src, stem, ext, engine)
    if fmt == "pdf":
        write_pdf_tables(args, src, stem, ext)
    print("[INFO] done")


if __name__ == "__main__":
    main()
