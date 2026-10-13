#!/usr/bin/env python3
"""Render a Markdown file (headings, lists, tables) to a plain PDF.

Why this script exists: the overview is kept as Markdown, and some readers need a
PDF to print or attach. The layout stays plain on purpose: black text, thin table
lines, page numbers.

Usage:
    python md2pdf.py overview.md -o overview.pdf
    python md2pdf.py overview.md -o overview.pdf --font /path/to/font.ttf

Requires: pip install fpdf2 markdown-it-py
"""
import argparse
import os
import re
import sys

# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------
BODY_PT = 10
TABLE_PT = 8
H1_PT, H2_PT, H3_PT = 15, 12, 11
MARGIN_MM = 15
WIDE_TABLE_COLUMNS = 9      # sections with tables this wide go on landscape pages
MIN_COL_CHARS, MAX_COL_CHARS = 3, 40
SHORT_COL_CHARS = 12        # columns this narrow (dates, numbers) never wrap
CELL_PAD_MM = 2.5
PT_TO_MM = 0.3528
HALF_WIDTH_EM = 0.62        # average half-width glyph width relative to font size
A4_SHORT_MM, A4_LONG_MM = 210, 297
BULLET = "\u2022"
FONT_CANDIDATES = [
    # (regular, bold) pairs; the first pair whose regular file exists is used
    ("C:/Windows/Fonts/malgun.ttf", "C:/Windows/Fonts/malgunbd.ttf"),
    ("/usr/share/fonts/truetype/nanum/NanumGothic.ttf", "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf"),
    ("/Library/Fonts/NanumGothic.ttf", "/Library/Fonts/NanumGothicBold.ttf"),
    ("~/Library/Fonts/NanumGothic.ttf", "~/Library/Fonts/NanumGothicBold.ttf"),
    ("/System/Library/Fonts/Supplemental/AppleGothic.ttf", None),
    ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"),
    ("/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc", "/usr/share/fonts/noto-cjk/NotoSansCJK-Bold.ttc"),
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ("C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/arialbd.ttf"),
]


def find_fonts(regular=None, bold=None):
    """Return (regular, bold) font paths. Bold falls back to the regular file."""
    if regular:
        return regular, bold or regular
    for reg, bld in FONT_CANDIDATES:
        reg = os.path.expanduser(reg)
        if os.path.exists(reg):
            bld = os.path.expanduser(bld) if bld else None
            return reg, bld if bld and os.path.exists(bld) else reg
    sys.exit("No usable font found. Pass one with --font /path/to/font.ttf")


def collection_index(path):
    """Pick the Korean face inside a .ttc collection, else the first face."""
    if not path.lower().endswith(".ttc"):
        return 0
    from fontTools.ttLib import TTCollection
    for i, face in enumerate(TTCollection(path).fonts):
        if "KR" in face["name"].getDebugName(1) or "Korean" in face["name"].getDebugName(1):
            return i
    return 0


# ---------------------------------------------------------------------------
# Markdown to HTML with table widths the PDF engine understands
# ---------------------------------------------------------------------------
def cell_width_chars(text):
    """Rough display width in half-width units: CJK characters count double."""
    return sum(2 if ord(ch) > 0x2E80 else 1 for ch in text)


def column_needs(tokens, i):
    """Widest cell per column (half-width units) for the table starting at tokens[i]."""
    needs, col, j = {}, 0, i
    while tokens[j].type != "table_close":
        t = tokens[j]
        if t.type == "tr_open":
            col = 0
        elif t.type in ("th_open", "td_open"):
            text = tokens[j + 1].content if tokens[j + 1].type == "inline" else ""
            needs[col] = max(needs.get(col, 0), min(max(cell_width_chars(text), MIN_COL_CHARS), MAX_COL_CHARS))
            col += 1
        j += 1
    return needs, j


def column_shares(needs, page_mm):
    """Short columns get their full width so dates and numbers never wrap;
    long text columns share the rest in proportion to their content."""
    char_mm = TABLE_PT * PT_TO_MM * HALF_WIDTH_EM
    want = {c: n * char_mm + CELL_PAD_MM for c, n in needs.items()}
    short = {c for c, n in needs.items() if n <= SHORT_COL_CHARS}
    fixed = sum(want[c] for c in short)
    rest = max(page_mm - fixed, 0)
    long_total = sum(want[c] for c in needs if c not in short) or 1
    widths = {c: want[c] if c in short else rest * want[c] / long_total for c in needs}
    total = sum(widths.values()) or 1
    return {c: 100 * w / total for c, w in widths.items()}


def is_wide(needs, orientation):
    if orientation == "auto":
        return len(needs) >= WIDE_TABLE_COLUMNS
    return orientation == "landscape"


def annotate_tables(tokens, orientation):
    """Set column width shares, left-align body cells and mark wide tables.
    A wide table is laid out for a landscape page."""
    i = 0
    while i < len(tokens):
        if tokens[i].type != "table_open":
            i += 1
            continue
        needs, end = column_needs(tokens, i)
        wide = is_wide(needs, orientation)
        page_mm = (A4_LONG_MM if wide else A4_SHORT_MM) - 2 * MARGIN_MM
        shares = column_shares(needs, page_mm)
        tokens[i].attrSet("border", "1")
        tokens[i].attrSet("class", "wide" if wide else "normal")
        col = 0
        for t in tokens[i:end]:
            if t.type == "tr_open":
                col = 0
            elif t.type == "th_open":
                t.attrSet("width", f"{shares[col]:.1f}%")
                col += 1
            elif t.type == "td_open":
                t.attrSet("align", "LEFT")
                col += 1
        i = end + 1


def markdown_to_sections(text, orientation):
    """Split the rendered HTML at each h1. Sections holding a wide table
    are printed on landscape pages, the rest on portrait pages."""
    from markdown_it import MarkdownIt
    md = MarkdownIt("commonmark").enable("table")
    tokens = md.parse(text)
    annotate_tables(tokens, orientation)
    html = md.renderer.render(tokens, md.options, {})
    # Whitespace between tags becomes empty list items in the PDF engine.
    html = re.sub(r">\s+<", "><", html)
    html = html.replace("<table", f'<font size="{TABLE_PT}"><table').replace("</table>", "</table></font>")
    # Flat lists become bullet paragraphs: the engine's own list bullets sit below the text line.
    html = re.sub(r"</?ul>", "", html)
    html = html.replace("<li>", f'<p class="item">{BULLET} ').replace("</li>", "</p>")
    sections = [part for part in re.split(r"(?=<h1>)", html) if part.strip()]
    if orientation != "auto":
        return [(part, orientation == "landscape") for part in sections]
    return [(part, 'class="wide"' in part) for part in sections]


# ---------------------------------------------------------------------------
# PDF
# ---------------------------------------------------------------------------
def build_pdf(sections, regular, bold):
    from fpdf import FPDF, FontFace, TextStyle

    class PlainPDF(FPDF):
        def footer(self):
            self.set_y(-10)
            self.set_font("Body", size=8)
            self.cell(0, 5, str(self.page_no()), align="C")

    pdf = PlainPDF(format="A4")
    pdf.set_margins(MARGIN_MM, MARGIN_MM, MARGIN_MM)
    pdf.set_auto_page_break(True, margin=MARGIN_MM)
    pdf.add_font("Body", "", regular, collection_font_number=collection_index(regular))
    pdf.add_font("Body", "B", bold, collection_font_number=collection_index(bold))
    black = "#000000"
    styles = {
        # fpdf2 counts these margins in line heights, so the values stay small
        "h1": TextStyle(font_style="B", color=black, font_size_pt=H1_PT, t_margin=2.0, b_margin=0.4),
        "h2": TextStyle(font_style="B", color=black, font_size_pt=H2_PT, t_margin=1.0, b_margin=0.3),
        "h3": TextStyle(font_style="B", color=black, font_size_pt=H3_PT, t_margin=0.8, b_margin=0.2),
        "blockquote": TextStyle(color=black, t_margin=0.3, b_margin=0.3, l_margin=5),
        "p": TextStyle(l_margin=4, t_margin=0.3),
        "li": TextStyle(l_margin=5, t_margin=0.3),
        "ol": TextStyle(t_margin=0.2),
        "code": FontFace(family="Body"),
    }
    current = None
    for html, landscape in sections:
        orientation = "L" if landscape else "P"
        if orientation != current:
            pdf.add_page(orientation=orientation)
            pdf.set_font("Body", size=BODY_PT)
            current = orientation
        pdf.write_html(html, font_family="Body", tag_styles=styles, li_prefix_color=(0, 0, 0),
                       table_line_separators=True)
    return pdf


def main():
    parser = argparse.ArgumentParser(description="Render Markdown to a plain PDF.")
    parser.add_argument("markdown")
    parser.add_argument("-o", "--output")
    parser.add_argument("--font", help="regular TTF/OTF/TTC font path")
    parser.add_argument("--bold-font", help="bold font path (defaults to --font)")
    parser.add_argument("--orientation", choices=["auto", "portrait", "landscape"], default="auto")
    args = parser.parse_args()
    try:
        import fpdf  # noqa: F401
        import markdown_it  # noqa: F401
    except ImportError:
        sys.exit("Install first: pip install fpdf2 markdown-it-py")

    with open(args.markdown, encoding="utf-8") as f:
        sections = markdown_to_sections(f.read(), args.orientation)
    regular, bold = find_fonts(args.font, args.bold_font)
    pdf = build_pdf(sections, regular, bold)
    out = args.output or os.path.splitext(args.markdown)[0] + ".pdf"
    pdf.output(out)
    print(f"OK {out} (font: {os.path.basename(regular)}, pages: {pdf.page_no()})")


if __name__ == "__main__":
    main()
