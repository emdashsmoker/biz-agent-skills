"""Render a before/after comparison image for one demo folder.

A demo folder holds either before.md and after.md (writing demos) or
before.png and after.png (chart and diagram demos). The script lays the
two results side by side and saves compare.png in the same folder.
A long text is cut at a block boundary and marked with a note that
points to the full Markdown file.

Usage:
    python demos/tools/render.py demos/logical-write
    python demos/tools/render.py demos/onto-mece --max-height 0
    python demos/tools/render.py demos/biz-code-style --stack

--max-height sets the text height limit in CSS pixels. 0 keeps the full text.
--stack puts the two results one above the other, for figures whose
shapes differ too much to sit side by side.

Requirements: Python 3.10+, markdown-it-py, playwright, a Chromium build
and the NanumGothic font. Set CHROMIUM_PATH when Playwright cannot find
Chromium.
"""

import argparse
import base64
import os
import sys
from pathlib import Path

from markdown_it import MarkdownIt
from playwright.sync_api import sync_playwright

# Layout and colour settings, kept here so the look can change in one place.
CANVAS_WIDTH_PX = 1200
DEVICE_SCALE_FACTOR = 2
# A short viewport lets the full-page capture shrink to the content height.
MIN_VIEWPORT_HEIGHT_PX = 100
# Text taller than this is cut so the image stays legible when scaled down.
DEFAULT_MAX_BODY_HEIGHT_PX = 1500
OUTPUT_NAME = "compare.png"
BEFORE_LABEL = "스킬 미적용"
AFTER_LABEL_TEMPLATE = "{skill} 적용"
TRIM_NOTE_TEMPLATE = "이하 생략, 전문은 {name} 참고"
# Caps a tall figure in the stacked layout so the page does not run too long.
STACK_IMAGE_MAX_HEIGHT_PX = 1100
NAVY = "#6B8EC2"
NAVY_TINT = "#DCE5F2"
TEXT_COLOR = "#111111"
NOTE_COLOR = "#4A5D7E"

# CommonMark with tables matches how GitHub shows the Markdown files.
MARKDOWN = MarkdownIt("commonmark").enable("table").enable("strikethrough")

PAGE_TEMPLATE = """<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@700;800&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: #FFFFFF; color: {text}; width: {width}px;
         font-family: 'NanumGothic', 'Nanum Gothic', sans-serif; font-weight: 700; }}
  .grid {{ display: grid; grid-template-columns: 1fr 1fr; column-gap: 40px; padding: 44px; }}
  .col {{ min-width: 0; }}
  .col + .col {{ border-left: 1px solid {tint}; padding-left: 40px; }}
  .label {{ display: inline-block; font-size: 22px; font-weight: 800; padding: 6px 14px;
            margin-bottom: 14px; }}
  .before .label {{ background: {tint}; color: {text}; }}
  .after .label {{ background: {navy}; color: #FFFFFF; }}
  .body {{ font-size: 16px; line-height: 1.6; word-break: keep-all; overflow-wrap: anywhere; }}
  .body > :first-child {{ margin-top: 0; }}
  .body h1 {{ font-size: 21px; font-weight: 800; margin: 18px 0 8px; }}
  .body h2 {{ font-size: 18px; font-weight: 800; margin: 16px 0 6px; }}
  .body h3, .body h4 {{ font-size: 16px; font-weight: 800; margin: 14px 0 4px; }}
  .body p {{ margin: 6px 0; }}
  .body ul, .body ol {{ margin: 4px 0; padding-left: 22px; }}
  .body blockquote {{ margin: 8px 0; padding-left: 12px; border-left: 3px solid {tint}; }}
  .body table {{ border-collapse: collapse; margin: 10px 0; font-size: 14px; }}
  .body th, .body td {{ border: 1px solid {tint}; padding: 5px 8px; vertical-align: top; }}
  .body th {{ background: {tint}; }}
  .body code {{ font-family: 'NanumGothic', 'Nanum Gothic', monospace; }}
  .body pre {{ white-space: pre-wrap; margin: 8px 0; }}
  .body hr {{ border: 0; border-top: 1px solid {tint}; margin: 12px 0; }}
  .body img {{ width: 100%; height: auto; display: block; }}
  .stack .grid {{ grid-template-columns: 1fr; row-gap: 36px; }}
  .stack .col + .col {{ border-left: 0; padding-left: 0; border-top: 1px solid {tint}; padding-top: 36px; }}
  .stack .body img {{ width: auto; max-width: 100%; max-height: {stack_image_height}px; }}
  .note {{ display: none; margin-top: 12px; padding-top: 10px; border-top: 1px solid {tint};
           font-size: 15px; color: {note}; }}
</style></head>
<body class="{layout}"><div class="grid">
  <div class="col before"><div class="label">{before_label}</div>
    <div class="body">{before}</div><div class="note">{before_note}</div></div>
  <div class="col after"><div class="label">{after_label}</div>
    <div class="body">{after}</div><div class="note">{after_note}</div></div>
</div></body></html>"""

# Drops whole blocks below the height limit so no line is cut in half.
# Lists are trimmed item by item because one list can fill a whole column.
# A heading, rule or emptied list left at the cut shows nothing, so it goes too.
TRIM_SCRIPT = """(maxHeight) => {
  const trimChildren = (parent, limit) => {
    let trimmed = false;
    for (const child of Array.from(parent.children)) {
      if (trimmed) { child.remove(); continue; }
      const box = child.getBoundingClientRect();
      if (box.bottom <= limit) continue;
      trimmed = true;
      if (child.matches('ul, ol') && box.top < limit) {
        trimChildren(child, limit);
      } else {
        child.remove();
      }
    }
    return trimmed;
  };
  const isEmptyTail = (node) =>
    node.matches('h1, h2, h3, h4, h5, h6, hr') ||
    (node.matches('ul, ol') && node.children.length === 0);
  const dropTrailingHeadings = (body) => {
    while (body.lastElementChild && isEmptyTail(body.lastElementChild)) {
      body.lastElementChild.remove();
    }
  };
  for (const body of document.querySelectorAll('.body')) {
    const limit = body.getBoundingClientRect().top + maxHeight;
    if (body.scrollHeight > maxHeight && trimChildren(body, limit)) {
      dropTrailingHeadings(body);
      body.nextElementSibling.style.display = 'block';
    }
  }
}"""


def markdown_to_html(path: Path) -> str:
    return MARKDOWN.render(path.read_text(encoding="utf-8"))


def image_to_html(path: Path) -> str:
    # Inline the image so the page renders without a file server.
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f'<img src="data:image/png;base64,{encoded}" alt="{path.stem}">'


def find_source(demo_dir: Path, side: str) -> Path:
    for suffix in (".md", ".png"):
        candidate = demo_dir / f"{side}{suffix}"
        if candidate.exists():
            return candidate
    raise FileNotFoundError(f"{side}.md or {side}.png is missing in {demo_dir}")


def source_to_html(path: Path) -> str:
    if path.suffix == ".md":
        return markdown_to_html(path)
    return image_to_html(path)


def build_page(demo_dir: Path, stack: bool) -> str:
    before_path = find_source(demo_dir, "before")
    after_path = find_source(demo_dir, "after")
    return PAGE_TEMPLATE.format(
        text=TEXT_COLOR, width=CANVAS_WIDTH_PX, navy=NAVY, tint=NAVY_TINT, note=NOTE_COLOR,
        layout="stack" if stack else "side", stack_image_height=STACK_IMAGE_MAX_HEIGHT_PX,
        before_label=BEFORE_LABEL,
        after_label=AFTER_LABEL_TEMPLATE.format(skill=demo_dir.name),
        before=source_to_html(before_path),
        after=source_to_html(after_path),
        before_note=TRIM_NOTE_TEMPLATE.format(name=before_path.name),
        after_note=TRIM_NOTE_TEMPLATE.format(name=after_path.name),
    )


def render_png(html: str, output_path: Path, max_body_height: int) -> None:
    executable_path = os.environ.get("CHROMIUM_PATH") or None
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=executable_path)
        page = browser.new_page(
            viewport={"width": CANVAS_WIDTH_PX, "height": MIN_VIEWPORT_HEIGHT_PX},
            device_scale_factor=DEVICE_SCALE_FACTOR,
        )
        page.set_content(html, wait_until="networkidle")
        if max_body_height > 0:
            page.evaluate(TRIM_SCRIPT, max_body_height)
        page.screenshot(path=str(output_path), full_page=True)
        browser.close()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render compare.png for one demo folder.")
    parser.add_argument("demo_dir", type=Path)
    parser.add_argument("--max-height", type=int, default=DEFAULT_MAX_BODY_HEIGHT_PX,
                        help="text height limit in CSS pixels, 0 keeps the full text")
    parser.add_argument("--stack", action="store_true",
                        help="place the two results one above the other")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    demo_dir = args.demo_dir.resolve()
    if not demo_dir.is_dir():
        print(f"Not a folder: {demo_dir}")
        return 1
    output_path = demo_dir / OUTPUT_NAME
    render_png(build_page(demo_dir, args.stack), output_path, args.max_height)
    print(f"Saved {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
