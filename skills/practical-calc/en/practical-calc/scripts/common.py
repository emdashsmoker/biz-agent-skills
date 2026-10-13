"""Shared helpers: input loading, number formatting, markdown tables, errors.

Every calculation script imports this module so that formatting and error
handling stay identical across tools.
"""
import json
import math
import sys
from pathlib import Path

from labels import T

DEFAULT_DECIMALS = 2
TABLE_ENCODINGS = ("utf-8-sig", "cp949")  # cp949 is the Windows Korean code page, tried when a file is not UTF-8
FLOAT_TOLERANCE = 1e-9
EXCEL_SHEET_NAME_LIMIT = 31
CSV_EXPORT_ENCODING = "utf-8-sig"  # BOM lets spreadsheet programs detect UTF-8 Korean text


class InputError(Exception):
    """Raised when user input cannot be used as given."""


def run_main(main_func):
    """Run a script entry point and turn InputError into a readable exit."""
    try:
        main_func()
    except InputError as err:
        print(f"{T('input_error')}: {err}", file=sys.stderr)
        sys.exit(2)
    except KeyError as err:
        # JSON inputs raise KeyError when a required field is absent
        print(f"{T('input_error')}: {T('missing_field', field=err)}", file=sys.stderr)
        sys.exit(2)


def load_json(path):
    try:
        with open(path, encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        raise InputError(T("file_not_found", path=path))
    except json.JSONDecodeError as err:
        raise InputError(T("json_invalid", path=path, detail=str(err)))


def load_table(path, sheet=None):
    """Read CSV or XLSX into a pandas DataFrame."""
    import pandas as pd

    file_path = Path(path)
    if not file_path.exists():
        raise InputError(T("file_not_found", path=path))
    if file_path.suffix.lower() in (".xlsx", ".xls"):
        try:
            return pd.read_excel(file_path, sheet_name=sheet or 0)
        except ImportError:
            raise InputError(T("xlsx_needs_openpyxl"))
    for encoding in TABLE_ENCODINGS:
        try:
            return pd.read_csv(file_path, encoding=encoding)
        except UnicodeDecodeError:
            continue
    raise InputError(T("encoding_unknown", path=path))


def require_columns(frame, columns, path):
    missing = [col for col in columns if col not in frame.columns]
    if missing:
        raise InputError(T("missing_columns", path=path, columns=", ".join(missing),
                           available=", ".join(map(str, frame.columns))))


def parse_number(value):
    """Convert a cell to float. Accepts thousands separators and accounting negatives such as (1,234)."""
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace(",", "").replace(" ", "").replace("\u00a0", "").replace("\u2212", "-")
    negative = text.startswith("(") and text.endswith(")")
    if negative:
        text = text[1:-1]
    number = float(text)
    return -number if negative else number


def to_float(value, field):
    try:
        number = parse_number(value)
    except (TypeError, ValueError):
        raise InputError(T("not_a_number", field=field, value=value))
    if math.isnan(number):
        raise InputError(T("not_a_number", field=field, value=value))
    return number


def fmt_num(value, decimals=DEFAULT_DECIMALS):
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "-"
    return f"{value:,.{decimals}f}"


def fmt_pct(ratio, decimals=DEFAULT_DECIMALS):
    """Format a ratio (0.1234) as a percentage string (12.34%)."""
    if ratio is None or (isinstance(ratio, float) and math.isnan(ratio)):
        return "-"
    return f"{ratio * 100:,.{decimals}f}%"


def md_table(headers, rows):
    """Build a GitHub-flavored markdown table without extra dependencies."""
    lines = ["| " + " | ".join(str(h) for h in headers) + " |",
             "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(lines)


def section(title, body):
    print(f"\n## {title}\n")
    print(body)


def is_missing(value):
    return value is None or (isinstance(value, float) and math.isnan(value))


class Cell:
    """A table value with its display kind: num, pct or text."""

    def __init__(self, raw, kind="num", places=None):
        self.raw, self.kind, self.places = raw, kind, places


def num(raw, places=None):
    return Cell(raw, "num", places)


def gen(raw):
    """Number shown in its shortest form (0.25, 50,000), for user-entered factors."""
    return Cell(raw, "gen")


def pct(raw, places=None):
    """Percentage cell. raw is a ratio (0.1234 is shown as 12.34%)."""
    return Cell(raw, "pct", places)


class Report:
    """Prints markdown tables and keeps the raw values for CSV, XLSX and JSON export."""

    def __init__(self, decimals=DEFAULT_DECIMALS):
        self.decimals = decimals
        self.tables = []

    def _display(self, cell):
        if isinstance(cell, Cell):
            if is_missing(cell.raw):
                return "-"
            places = self.decimals if cell.places is None else cell.places
            if cell.kind == "pct":
                return fmt_pct(cell.raw, places)
            if cell.kind == "num":
                return fmt_num(cell.raw, places)
            if cell.kind == "gen":
                return f"{cell.raw:,.10g}"
            return str(cell.raw)
        if isinstance(cell, float):
            return fmt_num(cell, self.decimals)
        return "-" if cell is None else str(cell)

    def table(self, title, headers, rows, bold_last=False):
        shown = [[self._display(c) for c in row] for row in rows]
        if bold_last and shown:
            shown[-1] = [f"**{c}**" if c not in ("", "-") else c for c in shown[-1]]
        section(title, md_table(headers, shown))
        self.tables.append((title, list(headers), [list(r) for r in rows]))

    def note(self, title, text):
        """Printed only. Use for free text that repeats values already in a table."""
        section(title, text)

    def warnings(self, messages):
        if messages:
            section(T("warnings"), "\n".join(f"- {m}" for m in messages))
            self.tables.append((T("warnings"), [T("warnings")], [[m] for m in messages]))

    def finish(self, args, payload):
        save_json(args.out, payload)
        if args.export:
            export_tables(args.export, self.tables)


def _export_value(cell):
    if isinstance(cell, Cell):
        if is_missing(cell.raw):
            return None
        return cell.raw * 100 if cell.kind == "pct" else cell.raw
    return None if is_missing(cell) else cell


def _export_frame(headers, rows):
    """Raw values with percentages as numbers x100 and '(%)' added to the matching header or row label."""
    import pandas as pd

    out_headers = list(headers)
    out_rows = [[_export_value(c) for c in row] for row in rows]
    for j in range(len(headers)):
        kinds = set()
        for row in rows:
            cell = row[j] if j < len(row) else None
            if isinstance(cell, Cell):
                if not is_missing(cell.raw):
                    kinds.add(cell.kind)
            elif not is_missing(cell) and cell != "":
                kinds.add("text")
        if kinds == {"pct"}:
            out_headers[j] = f"{headers[j]} (%)"
        elif "pct" in kinds:
            for i, row in enumerate(rows):
                if isinstance(row[j], Cell) and row[j].kind == "pct" and isinstance(out_rows[i][0], str):
                    out_rows[i][0] = f"{out_rows[i][0]} (%)"
    return pd.DataFrame(out_rows, columns=out_headers)


def _safe_name(text, limit):
    cleaned = "".join("_" if ch in '[]:*?/\\<>|"' else ch for ch in str(text)).strip()
    return cleaned[:limit] or "table"


def export_tables(path, tables):
    """Write every table to one XLSX (one sheet per table) or to CSV files."""
    target = Path(path)
    suffix = target.suffix.lower()
    if suffix not in (".csv", ".xlsx"):
        raise InputError(T("export_format", path=path))
    frames = [(title, _export_frame(headers, rows)) for title, headers, rows in tables]
    if suffix == ".xlsx":
        import pandas as pd
        try:
            with pd.ExcelWriter(target, engine="openpyxl") as writer:
                used = set()
                for index, (title, frame) in enumerate(frames, start=1):
                    name = _safe_name(f"{index}_{title}", EXCEL_SHEET_NAME_LIMIT)
                    while name in used:
                        name = name[:-1] + "_"
                    used.add(name)
                    frame.to_excel(writer, sheet_name=name, index=False)
        except ImportError:
            raise InputError(T("xlsx_needs_openpyxl"))
        print(f"{T('saved_tables')}: {target}")
        return
    if len(frames) == 1:
        frames[0][1].to_csv(target, index=False, encoding=CSV_EXPORT_ENCODING)
        print(f"{T('saved_tables')}: {target}")
        return
    for index, (title, frame) in enumerate(frames, start=1):
        file_path = target.with_name(f"{target.stem}_{index:02d}_{_safe_name(title, 40)}.csv")
        frame.to_csv(file_path, index=False, encoding=CSV_EXPORT_ENCODING)
        print(f"{T('saved_tables')}: {file_path}")


def save_json(path, payload):
    if not path:
        return
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, default=float)
    print(f"\n{T('saved_result')}: {path}")


LARGE_VALUE = 1000  # chart labels drop decimals at or above this magnitude


def chart_formatter(values, decimals=DEFAULT_DECIMALS):
    """Label formatter for charts: whole numbers for large values keep labels short."""
    largest = max((abs(v) for v in values), default=0)
    places = 0 if largest >= LARGE_VALUE else decimals
    return lambda v: fmt_num(v, places)


def add_common_args(parser):
    parser.add_argument("--decimals", type=int, default=DEFAULT_DECIMALS,
                        help="decimal places in printed tables")
    parser.add_argument("--out", help="save results as JSON")
    parser.add_argument("--export", help="save the printed tables as .xlsx (one sheet each) or .csv")
    parser.add_argument("--chart", help="save a PNG chart to this path")
