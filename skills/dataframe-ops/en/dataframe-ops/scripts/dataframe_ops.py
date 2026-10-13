"""Helper functions for the dataframe-ops skill.

Why this file exists: the skill promises the same output for the same input.
Coordinate parsing, table rendering, paging, checkpoints and environment
checks are written once here and tested, so the model does not re-invent
them in every session.

Dependencies: Python standard library and pandas. Optional packages
(pdfplumber, python-docx, pyarrow, ...) are imported only inside the
function that needs them, so the core works without them.
"""
from __future__ import annotations

import difflib
import math
import os
import pickle
import platform
import re
import shutil
import subprocess
import sys
import time
import unicodedata
import zipfile
from datetime import datetime
from importlib.util import find_spec
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# Settings. Change values here; functions below read them.
# ---------------------------------------------------------------------------
DEFAULT_ROWS = 10            # rows shown when the user gives no count
HEAD_TAIL_DEFAULT = 5        # /h and /t without a number (same as df.head())
MAX_ROWS = 100               # upper limit for one rendered table
PAGE_SIZE = 20
CELL_WIDTH = 30              # characters kept per cell before "..."
NEAR_RADIUS = 10             # "around row N" shows N-10 .. N+10
MID_DEFAULT = 20             # rows shown by /mid without a number
CHECKPOINT_EVERY = 5         # executed commands between automatic checkpoints
HISTORY_SHOWN = 10           # rows shown by /history
MEMORY_WARN_MB = 500         # file size or DataFrame memory that needs a question
TIME_WARN_SEC = 5            # estimated run time that needs a question
SAMPLE_ROWS_FOR_TIMING = 1000
MISSING_TEXT = "NaN"
CHECKPOINT_DIR = "dataframe_ops_checkpoints"
CODE_EXPORT_NAME = "dataframe_ops_session.py"
# utf-8-sig also reads plain utf-8 and strips a BOM; cp949 covers Korean Excel exports.
TEXT_ENCODINGS = ("utf-8-sig", "cp949")
VENV_CANDIDATES = (
    "~/.dataframe_ops_env", "~/dataframe_ops_env", "./.dataframe_ops_env",
    "./dataframe_ops_env", "./.venv", "./venv",
)
VENV_DEFAULT = "~/.dataframe_ops_env"
CONDA_NAME_HINTS = ("dataframe_ops", "dataframe-ops")
CONDA_DEFAULT_NAME = "dataframe_ops"
CORE_PACKAGES = ("pandas", "openpyxl")
# pip name -> import name, installed only when a feature needs it
OPTIONAL_PACKAGES = {
    "openpyxl": "openpyxl", "xlrd": "xlrd", "odfpy": "odf",
    "pyarrow": "pyarrow", "tabulate": "tabulate", "matplotlib": "matplotlib",
    "pdfplumber": "pdfplumber", "tabula-py": "tabula", "python-docx": "docx",
}
PROBE_TIMEOUT_SEC = 60
SENSITIVE_NAME_HINTS = (
    "주민", "외국인등록", "여권", "운전면허", "계좌", "카드번호", "전화", "휴대폰",
    "핸드폰", "연락처", "이메일", "주소",
    "ssn", "social security", "national id", "passport", "driver", "account",
    "card", "phone", "mobile", "email", "e-mail", "address",
)
SENSITIVE_VALUE_PATTERNS = {
    "korean_resident_number": re.compile(r"\b\d{6}-?[1-8]\d{6}\b"),
    "us_ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
}
SENSITIVE_SCAN_ROWS = 200


# ---------------------------------------------------------------------------
# Excel-style coordinates. Row 1 is the first data row (the header is not a row).
# ---------------------------------------------------------------------------
_CELL = re.compile(r"^([A-Z]+)(\d+)$")


def col_to_alpha(position: int) -> str:
    """0 -> A, 25 -> Z, 26 -> AA."""
    if position < 0:
        raise ValueError("column position must be 0 or more")
    letters = ""
    n = position
    while n >= 0:
        letters = chr(n % 26 + ord("A")) + letters
        n = n // 26 - 1
    return letters


def alpha_to_col(letters: str) -> int:
    """A -> 0, Z -> 25, AA -> 26."""
    letters = letters.strip().upper()
    if not letters.isalpha():
        raise ValueError(f"not a column letter: {letters!r}")
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch) - ord("A") + 1)
    return n - 1


def column_map(df: pd.DataFrame) -> dict:
    """{'A': 'name', 'B': 'age', ...} for the given DataFrame."""
    return {col_to_alpha(i): c for i, c in enumerate(df.columns)}


def similar_columns(df: pd.DataFrame, name: str, limit: int = 3) -> list:
    """Column names close to a misspelled one, for the error message."""
    names = [str(c) for c in df.columns]
    close = difflib.get_close_matches(str(name), names, n=limit, cutoff=0.4)
    partial = [n for n in names if str(name) in n or n in str(name)]
    return list(dict.fromkeys(close + partial))[:limit]


def column_map_rows(df: pd.DataFrame) -> list:
    """Rows for the /map table: letter, column name, dtype, first non-missing value."""
    rows = []
    for i, c in enumerate(df.columns):
        non_missing = df[c].dropna()
        sample = non_missing.iloc[0] if len(non_missing) else MISSING_TEXT
        rows.append([col_to_alpha(i), str(c), str(df[c].dtype), sample])
    return rows


def parse_ref(ref: str, shape: tuple | None = None):
    """Turn A1, A1:C5, B:D, A:A, 2:5, 3:3, A,C,E into (rows, cols) for iloc.

    Each part is an int, a slice or a list of ints. When shape=(n_rows, n_cols)
    is given, references outside the table raise IndexError.
    """
    text = ref.replace(" ", "").upper()
    rows, cols = slice(None), slice(None)
    if "," in text:
        cols = [alpha_to_col(p) for p in text.split(",") if p]
    elif ":" in text:
        left, right = text.split(":", 1)
        if left.isdigit() and right.isdigit():
            a, b = sorted((int(left), int(right)))
            rows = a - 1 if a == b else slice(a - 1, b)
        elif left.isalpha() and right.isalpha():
            a, b = sorted((alpha_to_col(left), alpha_to_col(right)))
            cols = a if a == b else slice(a, b + 1)
        else:
            m1, m2 = _CELL.match(left), _CELL.match(right)
            if not (m1 and m2):
                raise ValueError(f"cannot read reference: {ref!r}")
            r1, r2 = sorted((int(m1.group(2)), int(m2.group(2))))
            c1, c2 = sorted((alpha_to_col(m1.group(1)), alpha_to_col(m2.group(1))))
            rows, cols = slice(r1 - 1, r2), slice(c1, c2 + 1)
    elif _CELL.match(text):
        m = _CELL.match(text)
        rows, cols = int(m.group(2)) - 1, alpha_to_col(m.group(1))
    elif text.isalpha():
        cols = alpha_to_col(text)
    elif text.isdigit():
        rows = int(text) - 1
    else:
        raise ValueError(f"cannot read reference: {ref!r}")
    if shape is not None:
        _check_bounds(rows, shape[0], "row")
        _check_bounds(cols, shape[1], "column")
    return rows, cols


def _check_bounds(part, size: int, label: str) -> None:
    if isinstance(part, int):
        highest = part
    elif isinstance(part, list):
        highest = max(part) if part else -1
    else:
        highest = (part.stop - 1) if part.stop is not None else -1
    if highest >= size or (isinstance(part, int) and part < 0):
        raise IndexError(f"{label} reference is outside the table (size {size})")


def _index_code(part) -> str:
    if isinstance(part, int):
        return str(part)
    if isinstance(part, list):
        return "[" + ", ".join(str(p) for p in part) + "]"
    start = "" if part.start is None else str(part.start)
    stop = "" if part.stop is None else str(part.stop)
    return f"{start}:{stop}"


def ref_to_code(ref: str, var: str = "df") -> str:
    """'A1:C5' -> "df.iloc[0:5, 0:3]" (plain pandas code shown to the user)."""
    rows, cols = parse_ref(ref)
    return f"{var}.iloc[{_index_code(rows)}, {_index_code(cols)}]"


# ---------------------------------------------------------------------------
# Row windows. All row numbers here are 1-based and inclusive.
# ---------------------------------------------------------------------------
def rows_between(n_rows: int, first: int, last: int) -> slice:
    first, last = sorted((first, last))
    return slice(max(first - 1, 0), min(last, n_rows))


def rows_mid(n_rows: int, count: int = MID_DEFAULT) -> slice:
    start = max(n_rows // 2 - count // 2, 0)
    return slice(start, min(start + count, n_rows))


def rows_near(n_rows: int, row: int, radius: int = NEAR_RADIUS) -> slice:
    return slice(max(row - 1 - radius, 0), min(row + radius, n_rows))


def page_count(n_rows: int, page_size: int = PAGE_SIZE) -> int:
    return max(math.ceil(n_rows / page_size), 1)


def page_rows(n_rows: int, page, page_size: int = PAGE_SIZE) -> tuple:
    """Return (slice, page_number). page accepts an int, 'first' or 'last'."""
    last_page = page_count(n_rows, page_size)
    if page == "first":
        page = 1
    elif page == "last":
        page = last_page
    page = min(max(int(page), 1), last_page)
    start = (page - 1) * page_size
    return slice(start, min(start + page_size, n_rows)), page


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def _cell_text(value, width: int = CELL_WIDTH) -> str:
    if pd.api.types.is_scalar(value) and pd.isna(value):
        text = MISSING_TEXT
    else:
        text = str(value)
    text = " ".join(text.split())  # newlines and tabs break table rows
    if len(text) > width:
        text = text[: width - 3] + "..."
    return text


def _prepare(view, base):
    """Return (frame, row_numbers, headers) for rendering.

    base is the main DataFrame. Pass it only when view is a row or column
    selection of base: row numbers and column letters then point at base.
    Leave base as None for aggregated or new tables: rows count from 1 and
    headers show names only, because coordinates always refer to base.
    """
    frame = view.to_frame() if isinstance(view, pd.Series) else view
    if isinstance(frame.columns, pd.MultiIndex):
        frame = frame.copy()
        frame.columns = ["_".join(str(p) for p in col if str(p)) for col in frame.columns]
    if base is not None and base.index.is_unique and frame.index.isin(base.index).all():
        numbers = list(base.index.get_indexer(frame.index) + 1)
        letters = column_map(base)
        by_name = {name: letter for letter, name in letters.items()}
        headers = [f"{by_name[c]}({c})" if c in by_name else str(c) for c in frame.columns]
        return frame, numbers, headers
    if not isinstance(frame.index, pd.RangeIndex):
        # group keys become visible columns; a key may share a column's name
        frame = frame.reset_index(allow_duplicates=True)
    numbers = list(range(1, len(frame) + 1))
    return frame, numbers, [str(c) for c in frame.columns]


def render_markdown(view, base=None, limit: int = DEFAULT_ROWS, first_number: int = 1) -> str:
    frame, numbers, headers = _prepare(view, base)
    if base is None:
        numbers = [n + first_number - 1 for n in numbers]
    limit = min(limit, MAX_ROWS)
    esc = lambda s: s.replace("|", "\\|")
    lines = [
        "|     | " + " | ".join(esc(h) for h in headers) + " |",
        "|:---:" + "|:---:" * len(headers) + "|",
    ]
    for num, (_, row) in zip(numbers[:limit], frame.head(limit).iterrows()):
        cells = " | ".join(esc(_cell_text(v)) for v in row)
        lines.append(f"| {num} | {cells} |")
    return "\n".join(lines)


def _display_width(text: str) -> int:
    return sum(2 if unicodedata.east_asian_width(ch) in "WF" else 1 for ch in text)


def _center(text: str, width: int) -> str:
    gap = width - _display_width(text)
    left = gap // 2
    return " " * left + text + " " * (gap - left)


def render_ascii(view, base=None, limit: int = DEFAULT_ROWS, first_number: int = 1) -> str:
    """Plain-text table for interfaces that do not render Markdown tables.

    Korean, Chinese and Japanese characters take two columns in a monospace
    font, so widths are counted with east_asian_width.
    """
    frame, numbers, headers = _prepare(view, base)
    if base is None:
        numbers = [n + first_number - 1 for n in numbers]
    limit = min(limit, MAX_ROWS)
    body = [
        [str(num)] + [_cell_text(v) for v in row]
        for num, (_, row) in zip(numbers[:limit], frame.head(limit).iterrows())
    ]
    table = [[""] + headers] + body
    widths = [max(_display_width(r[i]) for r in table) + 2 for i in range(len(table[0]))]
    render_row = lambda r: "|".join(_center(cell, w) for cell, w in zip(r, widths))
    lines = [render_row(table[0]), "|".join("-" * w for w in widths)]
    lines += [render_row(r) for r in body]
    return "\n".join(lines)


def render(view, base=None, mode: str = "markdown", limit: int = DEFAULT_ROWS,
           first_number: int = 1) -> str:
    if mode == "markdown":
        return render_markdown(view, base, limit, first_number)
    if mode == "ascii":
        return render_ascii(view, base, limit, first_number)
    raise ValueError("mode must be 'markdown' or 'ascii'")


# ---------------------------------------------------------------------------
# Loading files
# ---------------------------------------------------------------------------
def file_size_mb(path) -> float:
    return os.path.getsize(path) / 1024 ** 2


def frame_memory_mb(df: pd.DataFrame) -> float:
    return df.memory_usage(deep=True).sum() / 1024 ** 2


def excel_sheets(path) -> list:
    return pd.ExcelFile(path).sheet_names


def read_any(path, sheet_name=0) -> tuple:
    """Load a table by file extension. Returns (DataFrame, note).

    note records how the file was read (encoding or sheet) so the same call
    can be written into the reproduction code.
    """
    suffix = Path(path).suffix.lower()
    if suffix in (".csv", ".tsv", ".txt"):
        options = {".csv": {}, ".tsv": {"sep": "\t"}, ".txt": {"sep": None, "engine": "python"}}[suffix]
        for enc in TEXT_ENCODINGS:
            try:
                return pd.read_csv(path, encoding=enc, **options), f"encoding={enc}"
            except UnicodeDecodeError:
                continue
        raise UnicodeDecodeError("dataframe_ops", b"", 0, 1, f"tried {TEXT_ENCODINGS}")
    if suffix in (".xlsx", ".xlsm", ".xls", ".ods"):
        return pd.read_excel(path, sheet_name=sheet_name), f"sheet_name={sheet_name!r}"
    if suffix == ".json":
        return pd.read_json(path), ""
    if suffix == ".parquet":
        return pd.read_parquet(path), ""
    raise ValueError(f"unsupported file type: {suffix}")


def pdf_tables(path) -> list:
    """Tables found by pdfplumber; the first row of each table becomes the header."""
    import pdfplumber  # optional package
    frames = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            for table in page.extract_tables():
                if table and len(table) > 1:
                    frames.append(pd.DataFrame(table[1:], columns=table[0]))
    return frames


def docx_tables(path) -> list:
    """Tables in a Word file; the first row of each table becomes the header."""
    import docx  # optional package: python-docx
    frames = []
    for table in docx.Document(path).tables:
        cells = [[c.text for c in row.cells] for row in table.rows]
        if len(cells) > 1:
            frames.append(pd.DataFrame(cells[1:], columns=cells[0]))
    return frames


# ---------------------------------------------------------------------------
# Safety checks
# ---------------------------------------------------------------------------
def find_sensitive_columns(df: pd.DataFrame) -> list:
    """[(column, reason), ...] based on column names and sample values."""
    found = []
    for c in df.columns:
        name = str(c).lower()
        hint = next((h for h in SENSITIVE_NAME_HINTS if h in name), None)
        if hint:
            found.append((c, f"name:{hint}"))
            continue
        if pd.api.types.is_numeric_dtype(df[c]):
            continue
        sample = df[c].dropna().astype(str).head(SENSITIVE_SCAN_ROWS)
        for label, pattern in SENSITIVE_VALUE_PATTERNS.items():
            if sample.str.contains(pattern).any():
                found.append((c, f"value:{label}"))
                break
    return found


def estimate_seconds(func, df: pd.DataFrame, sample_rows: int = SAMPLE_ROWS_FOR_TIMING) -> float:
    """Run func on the first rows and scale the time to the full table."""
    sample = df.head(sample_rows)
    if len(sample) == 0:
        return 0.0
    start = time.perf_counter()
    func(sample)
    elapsed = time.perf_counter() - start
    return elapsed * len(df) / len(sample)


def profile(df: pd.DataFrame) -> dict:
    """Numbers for the data profile report, all computed here."""
    columns = []
    for c in df.columns:
        s = df[c]
        modes = s.mode(dropna=True)
        columns.append({
            "column": str(c), "dtype": str(s.dtype),
            "missing": int(s.isna().sum()), "unique": int(s.nunique(dropna=True)),
            "most_common": modes.iloc[0] if len(modes) else None,
        })
    numeric = df.select_dtypes("number")
    cells = df.shape[0] * df.shape[1]
    return {
        "rows": df.shape[0], "columns": df.shape[1],
        "memory_kb": round(df.memory_usage(deep=True).sum() / 1024, 1),
        "per_column": columns,
        "numeric": {c: {"mean": numeric[c].mean(), "median": numeric[c].median(),
                        "std": numeric[c].std()} for c in numeric.columns},
        "missing_rate_pct": round(df.isna().sum().sum() / cells * 100, 2) if cells else 0.0,
        "duplicate_rows": int(df.duplicated().sum()),
    }


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------
def env_report() -> dict:
    conda_env = os.environ.get("CONDA_DEFAULT_ENV")
    in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    return {
        "python": platform.python_version(),
        "pandas": pd.__version__,
        "venv": (os.environ.get("VIRTUAL_ENV") or sys.prefix) if in_venv else None,
        "conda_env": conda_env,
        "isolated": in_venv or (conda_env not in (None, "base")),
        "optional": {pip: find_spec(mod) is not None for pip, mod in OPTIONAL_PACKAGES.items()},
    }


def _version_tuple(text) -> tuple:
    return tuple(int(p) for p in re.findall(r"\d+", text or "")[:3])


def _probe(command: list) -> tuple:
    code = "import sys; import pandas as p; print(sys.version.split()[0], p.__version__)"
    try:
        out = subprocess.run(command + ["-c", code], capture_output=True, text=True,
                             timeout=PROBE_TIMEOUT_SEC)
    except (OSError, subprocess.TimeoutExpired):
        return None, None
    parts = out.stdout.split()
    return (parts[0], parts[1]) if out.returncode == 0 and len(parts) == 2 else (None, None)


def find_environments() -> list:
    """Existing venv folders from VENV_CANDIDATES and conda envs whose name matches CONDA_NAME_HINTS."""
    found = []
    for candidate in VENV_CANDIDATES:
        folder = Path(candidate).expanduser()
        for sub, exe in (("bin", "python"), ("Scripts", "python.exe")):
            if (folder / sub / "activate").exists():
                py, pdv = _probe([str(folder / sub / exe)])
                found.append({"type": "venv", "location": str(folder.resolve()), "python": py,
                              "pandas": pdv, "last_used": datetime.fromtimestamp(folder.stat().st_mtime)})
                break
    if shutil.which("conda"):
        listing = subprocess.run(["conda", "env", "list"], capture_output=True, text=True,
                                 timeout=PROBE_TIMEOUT_SEC)
        for line in listing.stdout.splitlines():
            parts = line.split()
            if not parts or line.startswith("#"):
                continue
            name, path = parts[0], parts[-1]
            if any(h in name.lower() for h in CONDA_NAME_HINTS):
                py, pdv = _probe(["conda", "run", "-n", name, "python"])
                used = datetime.fromtimestamp(Path(path).stat().st_mtime) if Path(path).exists() else None
                found.append({"type": "conda", "location": name, "python": py, "pandas": pdv,
                              "last_used": used})
    return found


def recommend_environment(envs: list):
    """Highest pandas version first; the most recently used wins a tie."""
    usable = [e for e in envs if e.get("pandas")]
    if not usable:
        return None
    return max(usable, key=lambda e: (_version_tuple(e["pandas"]), e.get("last_used") or datetime.min))


def create_venv(path: str = VENV_DEFAULT, packages=CORE_PACKAGES) -> str:
    """Run only after the user agreed. Installs from PyPI."""
    folder = Path(path).expanduser()
    subprocess.run([sys.executable, "-m", "venv", str(folder)], check=True)
    pip = folder / ("Scripts/pip.exe" if os.name == "nt" else "bin/pip")
    subprocess.run([str(pip), "install", "--upgrade", "pip"], check=True)
    subprocess.run([str(pip), "install", *packages], check=True)
    return str(folder)


def create_conda_env(name: str = CONDA_DEFAULT_NAME, packages=CORE_PACKAGES) -> str:
    """Run only after the user agreed. Uses conda-forge only (community channel)."""
    subprocess.run(["conda", "create", "-n", name, "-c", "conda-forge", "--override-channels",
                    *packages, "-y"], check=True)
    return name


# ---------------------------------------------------------------------------
# Session: history, undo, macros, checkpoints
# ---------------------------------------------------------------------------
class Session:
    def __init__(self, checkpoint_dir: str = CHECKPOINT_DIR):
        self.history = []          # every executed code block, in order
        self.command_count = 0
        self.change_count = 0      # commands that changed df, shown in the status line
        self.backup = None         # one level of undo
        self.macros = {}           # name -> list of code strings
        self.checkpoint_dir = Path(checkpoint_dir)

    def record(self, code: str, note: str = "", modifies: bool = False) -> bool:
        """Store one executed code block. Returns True when an automatic checkpoint is due.

        modifies=True when the block changed df (add, delete, rename, replace ...).
        """
        self.command_count += 1
        self.change_count += int(modifies)
        self.history.append({"no": self.command_count,
                             "time": datetime.now().strftime("%H:%M:%S"),
                             "code": code, "note": note})
        return self.command_count % CHECKPOINT_EVERY == 0

    def recent(self, n: int = HISTORY_SHOWN) -> list:
        return self.history[-n:]

    def code_of(self, number: int) -> str:
        return next(h["code"] for h in self.history if h["no"] == number)

    def keep_backup(self, df: pd.DataFrame) -> None:
        self.backup = df.copy()

    def undo(self):
        return None if self.backup is None else self.backup.copy()

    def full_code(self) -> str:
        lines = ["# dataframe-ops session: reproduction code",
                 f"# created: {datetime.now().isoformat(timespec='seconds')}",
                 f"# Python {platform.python_version()} / pandas {pd.__version__}",
                 "", "import pandas as pd", ""]
        for h in self.history:
            lines += [f"# [{h['no']}] {h['time']} {h['note']}".rstrip(), h["code"], ""]
        return "\n".join(lines)

    def export_code(self, filename: str = CODE_EXPORT_NAME) -> str:
        Path(filename).write_text(self.full_code(), encoding="utf-8")
        return filename

    def save_checkpoint(self, frames: dict, filename: str) -> str:
        """frames: {'df': df, 'df_original': ..., 'result': ...}. Writes a pickle file."""
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        env = env_report()
        state = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "environment": {"python": env["python"], "pandas": env["pandas"],
                            "venv": env["venv"] or env["conda_env"]},
            "dataframes": frames,
            "column_map": column_map(frames["df"]) if "df" in frames else {},
            "history": self.history,
            "macros": self.macros,
            "command_count": self.command_count,
            "change_count": self.change_count,
            "full_code": self.full_code(),
        }
        path = self.checkpoint_dir / filename
        with open(path, "wb") as f:
            pickle.dump(state, f)
        return str(path)

    def list_checkpoints(self) -> list:
        if not self.checkpoint_dir.exists():
            return []
        files = [p for p in self.checkpoint_dir.iterdir() if p.suffix in (".pkl", ".zip")]
        return sorted(files, key=lambda p: p.stat().st_mtime, reverse=True)

    def load_checkpoint(self, filename: str) -> dict:
        """Load only files this skill wrote in checkpoint_dir.

        pickle can run code while loading, so a file from anywhere else is refused.
        """
        path = (self.checkpoint_dir / Path(filename).name).resolve()
        if path.parent != self.checkpoint_dir.resolve() or path.suffix != ".pkl":
            raise PermissionError("only .pkl files inside the checkpoint folder can be loaded")
        with open(path, "rb") as f:
            state = pickle.load(f)
        self.history = state["history"]
        self.macros = state.get("macros", {})
        self.command_count = state["command_count"]
        self.change_count = state.get("change_count", 0)
        return state

    def save_all(self, frames: dict, filename: str) -> str:
        """Checkpoint + reproduction code in one zip file."""
        stem = Path(filename).stem
        pkl = self.save_checkpoint(frames, f"{stem}.pkl")
        zpath = self.checkpoint_dir / f"{stem}.zip"
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(pkl, arcname=Path(pkl).name)
            z.writestr(CODE_EXPORT_NAME, self.full_code())
        return str(zpath)


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")
