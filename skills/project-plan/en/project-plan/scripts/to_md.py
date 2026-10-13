#!/usr/bin/env python3
"""Convert input documents (RFP, proposal, kickoff report, admin papers) to Markdown text.

Why this script exists: the plan is drafted from documents, and a language model reads
Markdown more reliably than binary office files. Use it when the environment cannot
read a file directly.

Usage:
    python to_md.py rfp.pdf proposal.hwpx -o inputs.md

Formats:
    .md .txt          read as is
    .hwpx             python-hwpx if installed, otherwise built-in XML text extraction
    .hwp              not converted; save the file as HWPX or PDF first
    .pdf .docx .xlsx .pptx .html .csv   markitdown (pip install "markitdown[pdf,docx,xlsx,pptx]")
"""
import argparse
import os
import shutil
import subprocess
import sys
import zipfile
import xml.etree.ElementTree as ET

TEXT_TYPES = (".md", ".txt")
MARKITDOWN_TYPES = (".pdf", ".docx", ".xlsx", ".pptx", ".html", ".htm", ".csv")


def local(tag):
    """XML tag name without its namespace."""
    return tag.rsplit("}", 1)[-1]


def paragraph_text(p):
    return "".join(t.text or "" for t in p.iter() if local(t.tag) == "t").strip()


def table_lines(tbl):
    """Render an HWPX table as a Markdown table, one row per <tr>."""
    rows = []
    for tr in (e for e in tbl.iter() if local(e.tag) == "tr"):
        cells = []
        for tc in (e for e in tr if local(e.tag) == "tc"):
            text = " ".join(paragraph_text(p) for p in tc.iter() if local(p.tag) == "p")
            cells.append(text.replace("|", "/").strip())
        rows.append(cells)
    if not rows:
        return []
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * width]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return out


def walk(node, out):
    """Emit paragraphs and tables in document order without repeating table text."""
    for child in node:
        name = local(child.tag)
        if name == "tbl":
            out.extend([""] + table_lines(child) + [""])
        elif name == "p":
            nested = [e for e in child.iter() if local(e.tag) == "tbl"]
            if nested:
                walk(child, out)
            else:
                text = paragraph_text(child)
                if text:
                    out.append(text)
        else:
            walk(child, out)


def hwpx_builtin(path):
    with zipfile.ZipFile(path) as z:
        sections = sorted(n for n in z.namelist()
                          if n.startswith("Contents/section") and n.endswith(".xml"))
        out = []
        for name in sections:
            walk(ET.fromstring(z.read(name)), out)
    return "\n".join(out)


def hwpx_to_md(path):
    try:
        from hwpx.tools.exporter import export_markdown
        with open(path, "rb") as f:
            return export_markdown(f.read(), include_tables=True)
    except Exception:  # library missing or API changed: fall back to plain XML reading
        return hwpx_builtin(path)


def markitdown_to_md(path):
    try:
        from markitdown import MarkItDown
    except ImportError:
        sys.exit('Install first: pip install "markitdown[pdf,docx,xlsx,pptx]"')
    return MarkItDown(enable_plugins=False).convert(path).text_content


def convert(path):
    ext = os.path.splitext(path)[1].lower()
    if ext in TEXT_TYPES:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    if ext == ".hwpx":
        return hwpx_to_md(path)
    if ext == ".hwp":
        return "[HWP is not converted. Save the file as HWPX or PDF and run again.]"
    if ext in MARKITDOWN_TYPES:
        text = markitdown_to_md(path)
        if not text.strip() and ext == ".pdf":
            text = pdftotext(path)
        return text or "[No text extracted. The file may be a scan and need OCR.]"
    return f"[Unsupported file type: {ext}]"


def pdftotext(path):
    """Second try for PDFs whose embedded fonts the first reader cannot map."""
    if not shutil.which("pdftotext"):
        return ""
    result = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True)
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description="Convert documents to Markdown.")
    parser.add_argument("files", nargs="+")
    parser.add_argument("-o", "--output", help="write all results into one Markdown file")
    args = parser.parse_args()
    parts = []
    for path in args.files:
        text = convert(path).strip()
        parts.append(f"<!-- source: {os.path.basename(path)} ({len(text)} chars) -->\n\n{text}\n")
    result = "\n".join(parts)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"OK {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
