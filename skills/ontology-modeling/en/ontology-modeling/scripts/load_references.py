"""
Print the engine-mode reference files in full. The output holds the axiom
patterns, SPARQL patterns, check signatures and templates used while
building and checking the ontology, so read it without truncation.

Usage:
    python scripts/load_references.py              # all engine references
    python scripts/load_references.py sparql-patterns.md   # selected files
"""
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REF_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "references")
ENGINE_REFERENCES = [
    "tbox-templates.md",
    "axiom-patterns.md",
    "sparql-patterns.md",
    "check-functions.md",
]

sys.path.insert(0, SCRIPT_DIR)
try:
    from onto_engine import LANG
except Exception:  # the engine needs owlready2; the banner does not
    LANG = "en"

BANNERS = {
    "ko": ("[참조 문서] 아래 내용은 엔진 모드에서 그대로 적용하는 패턴과 코드임",
           "[로드 완료]"),
    "en": ("[References] Apply the patterns and code below in engine mode",
           "[Loaded]"),
}


def main():
    head, tail = BANNERS.get(LANG, BANNERS["en"])
    names = sys.argv[1:] or ENGINE_REFERENCES
    print("=" * 60)
    print(head)
    print("=" * 60)
    for name in names:
        path = os.path.join(REF_DIR, name)
        if not os.path.exists(path):
            print(f"[WARN] {name} not found: {path}", file=sys.stderr)
            continue
        print(f"\n{'=' * 60}\n{name}\n{'=' * 60}\n")
        with open(path, encoding="utf-8") as f:
            print(f.read())
    print("=" * 60)
    print(tail)
    print("=" * 60)


if __name__ == "__main__":
    main()
