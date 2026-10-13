"""Convert input documents to Markdown so figures can be read and checked.

Engines
  .pdf                       markitdown (text) + pdfplumber (tables, separate file if any)
  .hwpx                      python-hwpx export_markdown -> TextExtractor -> raw XML text
  .hwp                       built-in HWP 5.0 reader (olefile); tables come out as plain paragraphs
  .docx .pptx .xlsx .xls .csv .json .xml .html .htm .txt .md .epub .zip   markitdown
Only local files are accepted.

HWP reader notice: 본 제품은 한컴의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.
(This product was developed with reference to Hancom's published HWP document file format.)

Usage
  python parse_input.py INPUT OUTPUT.md
  python parse_input.py INPUT OUTPUT_DIR --chunk [--chunk-size 2000]
"""

import argparse
import re
import struct
import sys
import zlib
from datetime import datetime, timezone
from pathlib import Path

MARKITDOWN_EXTENSIONS = {".docx", ".pptx", ".xlsx", ".xls", ".csv", ".json", ".xml",
                         ".html", ".htm", ".txt", ".md", ".epub", ".zip"}
CHUNK_SIZE_DEFAULT = 2000
CHUNK_OVERFLOW_RATIO = 1.5

# HWP 5.0 binary constants (Hancom published format, revision 1.3)
HWP_SIGNATURE = b"HWP Document File"
HWP_PROPERTY_OFFSET = 36
HWP_FLAG_COMPRESSED, HWP_FLAG_PASSWORD, HWP_FLAG_DISTRIBUTION = 0x1, 0x2, 0x4
HWPTAG_PARA_TEXT = 67
RECORD_SIZE_EXTENDED = 0xFFF
CONTROL_CHAR_SIZE_1 = {0, 10, 13, 24, 25, 26, 27, 28, 29, 30, 31}   # 1 WCHAR
CONTROL_WIDE_SIZE = 8                                               # inline/extended: 8 WCHAR
CONTROL_TEXT = {9: "\t", 10: "\n", 24: "-", 30: " ", 31: " "}


class ParseError(RuntimeError):
    """Raised when a document cannot be converted; message is shown to the user."""


# ---------------------------------------------------------------- engines
def parse_markitdown(path):
    from markitdown import MarkItDown
    return MarkItDown(enable_plugins=False).convert(str(path)).text_content or ""


def parse_pdf_tables(path):
    """Return Markdown for every table pdfplumber detects, or None."""
    import pdfplumber
    blocks = []
    with pdfplumber.open(str(path)) as pdf:
        for page_no, page in enumerate(pdf.pages, 1):
            for table_no, table in enumerate(page.extract_tables(), 1):
                md = rows_to_markdown(table)
                if md:
                    blocks.append(f"### Page {page_no} Table {table_no}\n\n{md}")
    return "\n\n".join(blocks) or None


def parse_hwpx(path):
    try:
        from hwpx.tools.exporter import export_markdown
        return export_markdown(path.read_bytes(), include_tables=True), "python-hwpx export_markdown"
    except Exception as first:  # library API differences across versions
        print(f"[INFO] export_markdown failed: {first}", file=sys.stderr)
    try:
        from hwpx.tools.text_extractor import TextExtractor
        with TextExtractor(str(path)) as extractor:
            return extractor.extract_text(paragraph_separator="\n\n", skip_empty=True,
                                          include_nested=True, object_behavior="skip",
                                          preserve_breaks=True), "python-hwpx TextExtractor"
    except Exception as second:
        print(f"[INFO] TextExtractor failed: {second}", file=sys.stderr)
    return parse_hwpx_xml(path), "raw XML text"


def parse_hwpx_xml(path):
    """Last resort: read <hp:t> text runs paragraph by paragraph from the section XML."""
    import zipfile
    import xml.etree.ElementTree as ET
    texts = []
    with zipfile.ZipFile(path) as archive:
        sections = sorted(n for n in archive.namelist()
                          if re.fullmatch(r"Contents/section\d+\.xml", n))
        for name in sections:
            root = ET.fromstring(archive.read(name))
            for para in root.iter():
                if not para.tag.endswith("}p"):
                    continue
                # direct runs only, so text of nested table paragraphs is not repeated
                line = "".join("".join(t.itertext()) for run in para if run.tag.endswith("}run")
                               for t in run if t.tag.endswith("}t"))
                if line.strip():
                    texts.append(line.strip())
    return "\n\n".join(texts)


def decode_para_text(payload):
    """Decode one PARA_TEXT record, skipping inline and extended control characters."""
    out, i, count = [], 0, len(payload) // 2
    while i < count:
        code = struct.unpack_from("<H", payload, i * 2)[0]
        if code >= 32:
            out.append(chr(code))
            i += 1
        elif code in CONTROL_CHAR_SIZE_1:
            out.append(CONTROL_TEXT.get(code, ""))
            i += 1
        else:
            out.append(CONTROL_TEXT.get(code, ""))
            i += CONTROL_WIDE_SIZE
    return "".join(out).strip()


def iter_records(data):
    """Yield (tag_id, payload) from a decompressed BodyText section stream."""
    pos = 0
    while pos + 4 <= len(data):
        header = struct.unpack_from("<I", data, pos)[0]
        pos += 4
        tag, size = header & 0x3FF, (header >> 20) & 0xFFF
        if size == RECORD_SIZE_EXTENDED:
            size = struct.unpack_from("<I", data, pos)[0]
            pos += 4
        yield tag, data[pos:pos + size]
        pos += size


def parse_hwp(path):
    import olefile
    if not olefile.isOleFile(str(path)):
        raise ParseError("not an HWP 5.0 file (HWP 3.x and older are not supported)")
    with olefile.OleFileIO(str(path)) as ole:
        header = ole.openstream("FileHeader").read()
        if not header.startswith(HWP_SIGNATURE):
            raise ParseError("FileHeader signature is not 'HWP Document File'")
        flags = struct.unpack_from("<I", header, HWP_PROPERTY_OFFSET)[0]
        if flags & HWP_FLAG_PASSWORD:
            raise ParseError("password-protected HWP; save an unprotected copy first")
        if flags & HWP_FLAG_DISTRIBUTION:
            raise ParseError("distribution-locked HWP; save as HWPX or PDF first")
        sections = sorted((e for e in ole.listdir() if len(e) == 2 and e[0] == "BodyText"),
                          key=lambda e: int(re.sub(r"\D", "", e[1]) or 0))
        paragraphs = []
        for entry in sections:
            data = ole.openstream("/".join(entry)).read()
            if flags & HWP_FLAG_COMPRESSED:
                data = zlib.decompress(data, -15)
            for tag, payload in iter_records(data):
                if tag == HWPTAG_PARA_TEXT:
                    text = decode_para_text(payload)
                    if text:
                        paragraphs.append(text)
    return "\n\n".join(paragraphs)


# ---------------------------------------------------------------- helpers
def rows_to_markdown(rows):
    if not rows or not rows[0]:
        return ""
    width = max(len(r) for r in rows)
    clean = [[re.sub(r"\s+", " ", str(c)).strip() if c is not None else "" for c in r]
             + [""] * (width - len(r)) for r in rows]
    lines = ["| " + " | ".join(clean[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    lines += ["| " + " | ".join(r) + " |" for r in clean[1:]]
    return "\n".join(lines)


def postprocess(text):
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text.replace("\f", "\n\n"))
    text = re.sub(r"[^\S\n]{2,}", " ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def front_matter(source, engine, chars, chunk=None, total=None):
    lines = ["---", f"source: {source}", f"engine: {engine}",
             f"parsed_at: {datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%SZ}", f"char_count: {chars}"]
    if chunk is not None:
        lines += [f"chunk: {chunk}", f"total_chunks: {total}"]
    return "\n".join(lines + ["---", ""])


def split_chunks(text, size):
    """Split at headings, then at paragraphs when a section is too long."""
    sections = [s for s in re.split(r"(?m)^(?=#{1,6}\s)", text) if s.strip()]
    chunks, current = [], ""
    for sec in sections:
        if current and len(current) + len(sec) > size:
            chunks.append(current.strip())
            current = sec
        else:
            current += sec
    if current.strip():
        chunks.append(current.strip())
    final = []
    for chunk in chunks:
        if len(chunk) <= size * CHUNK_OVERFLOW_RATIO:
            final.append(chunk)
            continue
        part = ""
        for para in chunk.split("\n\n"):
            if part and len(part) + len(para) > size:
                final.append(part.strip())
                part = para
            else:
                part = f"{part}\n\n{para}" if part else para
        if part.strip():
            final.append(part.strip())
    return final or [text]


def convert(path):
    """Return (markdown, engine, tables_markdown_or_None)."""
    ext = path.suffix.lower()
    if ext == ".pdf":
        text = parse_markitdown(path)
        try:
            tables = parse_pdf_tables(path)
        except Exception as exc:
            print(f"[WARN] table extraction failed: {exc}", file=sys.stderr)
            tables = None
        return text, "markitdown + pdfplumber", tables
    if ext == ".hwpx":
        text, engine = parse_hwpx(path)
        return text, engine, None
    if ext == ".hwp":
        return parse_hwp(path), "HWP 5.0 reader (olefile)", None
    if ext in MARKITDOWN_EXTENSIONS:
        return parse_markitdown(path), "markitdown", None
    raise ParseError(f"unsupported extension '{ext}'. Supported: .pdf .hwp .hwpx "
                     + " ".join(sorted(MARKITDOWN_EXTENSIONS))
                     + " (convert .doc/.ppt to .docx/.pptx first)")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input")
    parser.add_argument("output", help="output .md file, or a directory with --chunk")
    parser.add_argument("--chunk", action="store_true")
    parser.add_argument("--chunk-size", type=int, default=CHUNK_SIZE_DEFAULT)
    args = parser.parse_args()

    source = Path(args.input)
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", args.input) or not source.is_file():
        print(f"[ERROR] local file not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    try:
        raw, engine, tables = convert(source)
    except ParseError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"[ERROR] conversion failed ({type(exc).__name__}): {exc}", file=sys.stderr)
        sys.exit(1)

    text = postprocess(raw)
    print(f"[INFO] {source.name} | engine: {engine} | characters: {len(text):,}")
    if not text:
        print("[WARN] no text extracted (scanned image PDF needs OCR first)", file=sys.stderr)

    out = Path(args.output)
    if args.chunk:
        out.mkdir(parents=True, exist_ok=True)
        chunks = split_chunks(text, args.chunk_size)
        for i, chunk in enumerate(chunks, 1):
            (out / f"{source.stem}_chunk_{i:03d}.md").write_text(
                front_matter(source.name, engine, len(chunk), i, len(chunks)) + "\n" + chunk,
                encoding="utf-8")
        print(f"[INFO] {len(chunks)} chunks written to {out}")
        table_dir = out
    else:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(front_matter(source.name, engine, len(text)) + "\n" + text,
                       encoding="utf-8")
        print(f"[INFO] written: {out}")
        table_dir = out.parent
    if tables:
        table_path = table_dir / f"{source.stem}_tables.md"
        table_path.write_text(front_matter(source.name, "pdfplumber", len(tables)) + "\n" + tables,
                              encoding="utf-8")
        print(f"[INFO] tables written: {table_path}")
    elif source.suffix.lower() == ".pdf":
        print("[INFO] no tables detected in PDF")


if __name__ == "__main__":
    main()
