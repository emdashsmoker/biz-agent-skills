"""Render a before/after comparison image for one demo folder.

A demo folder holds either before.md and after.md (writing demos) or
before.png and after.png (chart and diagram demos). The script lays the
two results side by side and saves compare.png in the same folder.

Usage:
    python demos/tools/render.py demos/logical-write

Requirements: Python 3.10+, markdown, playwright, a Chromium build and the
NanumGothic font. Set CHROMIUM_PATH when Playwright cannot find Chromium.
"""

import base64
import os
import sys
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

# Layout and colour settings, kept here so the look can change in one place.
CANVAS_WIDTH_PX = 1440
DEVICE_SCALE_FACTOR = 1.5
# A short viewport lets the full-page capture shrink to the content height.
MIN_VIEWPORT_HEIGHT_PX = 100
OUTPUT_NAME = "compare.png"
BEFORE_LABEL = "스킬 미적용"
AFTER_LABEL_TEMPLATE = "{skill} 적용"
NAVY = "#6B8EC2"
NAVY_TINT = "#DCE5F2"
TEXT_COLOR = "#111111"
MARKDOWN_EXTENSIONS = ["tables", "fenced_code", "sane_lists"]

PAGE_TEMPLATE = """<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@700;800&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: #FFFFFF; color: {text}; width: {width}px;
         font-family: 'NanumGothic', 'Nanum Gothic', sans-serif; font-weight: 700; }}
  .grid {{ display: grid; grid-template-columns: 1fr 1fr; column-gap: 48px; padding: 56px; }}
  .col + .col {{ border-left: 1px solid {tint}; padding-left: 48px; }}
  .label {{ display: inline-block; font-size: 22px; font-weight: 800; padding: 6px 14px;
            margin-bottom: 12px; }}
  .before .label {{ background: {tint}; color: {text}; }}
  .after .label {{ background: {navy}; color: #FFFFFF; }}
  .body {{ font-size: 15px; line-height: 1.65; word-break: keep-all; overflow-wrap: anywhere; }}
  .body h1 {{ font-size: 19px; font-weight: 800; margin: 18px 0 8px; }}
  .body h2 {{ font-size: 17px; font-weight: 800; margin: 16px 0 6px; }}
  .body h3, .body h4 {{ font-size: 15px; font-weight: 800; margin: 14px 0 4px; }}
  .body p {{ margin: 6px 0; }}
  .body ul, .body ol {{ margin: 4px 0; padding-left: 22px; }}
  .body blockquote {{ margin: 8px 0; padding-left: 12px; border-left: 3px solid {tint}; }}
  .body table {{ border-collapse: collapse; margin: 10px 0; font-size: 14px; }}
  .body th, .body td {{ border: 1px solid {tint}; padding: 5px 8px; vertical-align: top; }}
  .body th {{ background: {tint}; }}
  .body code {{ font-family: 'NanumGothic', 'Nanum Gothic', monospace; }}
  .body pre {{ white-space: pre-wrap; }}
  .body hr {{ border: 0; border-top: 1px solid {tint}; }}
  .body img {{ width: 100%; height: auto; display: block; }}
</style></head>
<body><div class="grid">
  <div class="col before"><div class="label">{before_label}</div><div class="body">{before}</div></div>
  <div class="col after"><div class="label">{after_label}</div><div class="body">{after}</div></div>
</div></body></html>"""


def markdown_to_html(path: Path) -> str:
    return markdown.markdown(path.read_text(encoding="utf-8"), extensions=MARKDOWN_EXTENSIONS)


def image_to_html(path: Path) -> str:
    # Inline the image so the page renders without a file server.
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f'<img src="data:image/png;base64,{encoded}" alt="{path.stem}">'


def load_side(demo_dir: Path, side: str) -> str:
    markdown_path = demo_dir / f"{side}.md"
    image_path = demo_dir / f"{side}.png"
    if markdown_path.exists():
        return markdown_to_html(markdown_path)
    if image_path.exists():
        return image_to_html(image_path)
    raise FileNotFoundError(f"{side}.md or {side}.png is missing in {demo_dir}")


def build_page(demo_dir: Path) -> str:
    return PAGE_TEMPLATE.format(
        text=TEXT_COLOR, width=CANVAS_WIDTH_PX, navy=NAVY, tint=NAVY_TINT,
        before_label=BEFORE_LABEL,
        after_label=AFTER_LABEL_TEMPLATE.format(skill=demo_dir.name),
        before=load_side(demo_dir, "before"),
        after=load_side(demo_dir, "after"),
    )


def render_png(html: str, output_path: Path) -> None:
    executable_path = os.environ.get("CHROMIUM_PATH") or None
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=executable_path)
        page = browser.new_page(
            viewport={"width": CANVAS_WIDTH_PX, "height": MIN_VIEWPORT_HEIGHT_PX},
            device_scale_factor=DEVICE_SCALE_FACTOR,
        )
        page.set_content(html, wait_until="networkidle")
        page.screenshot(path=str(output_path), full_page=True)
        browser.close()


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 1
    demo_dir = Path(argv[1]).resolve()
    if not demo_dir.is_dir():
        print(f"Not a folder: {demo_dir}")
        return 1
    output_path = demo_dir / OUTPUT_NAME
    render_png(build_page(demo_dir), output_path)
    print(f"Saved {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
