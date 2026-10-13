"""Income statement summary: margins, EBITDA, OPEX and period comparison.

EBITDA (operating basis) = operating profit + depreciation + amortization
EBITDA (net income basis) = net income + income tax + interest expense + depreciation + amortization
OPEX = cost of sales + selling, general and administrative expenses - depreciation - amortization
"""
import argparse

import chart
from common import (InputError, Report, add_common_args, chart_formatter, fmt_num, load_table, num, pct,
                    run_main, to_float)
from labels import T

ALIASES = {
    "revenue": ["revenue", "sales", "매출액", "영업수익", "수익(매출액)"],
    "cogs": ["cogs", "cost of sales", "매출원가"],
    "sga": ["sga", "sg&a", "판매비와관리비", "판관비"],
    "operating_income": ["operating_income", "operating profit", "operating income", "영업이익", "영업이익(손실)"],
    "depreciation": ["depreciation", "감가상각비"],
    "amortization": ["amortization", "amortisation", "무형자산상각비"],
    "interest_expense": ["interest_expense", "interest expense", "이자비용"],
    "income_tax": ["income_tax", "income tax expense", "법인세비용"],
    "net_income": ["net_income", "net income", "net profit", "profit for the period", "당기순이익", "당기순이익(손실)"],
}
DEFAULT_THRESHOLD_PCT = 10.0
CONSISTENCY_TOLERANCE = 0.005  # share of revenue allowed between reported and computed operating profit
LINE_ORDER = ["revenue", "cogs", "gross_profit", "sga", "operating_income", "depreciation",
              "amortization", "ebitda", "opex", "interest_expense", "income_tax", "net_income", "ebitda_ni"]
MARGINS = [("gross_margin", "gross_profit"), ("operating_margin", "operating_income"),
           ("ebitda_margin", "ebitda"), ("net_margin", "net_income"), ("opex_ratio", "opex")]


def canonical(name):
    key = str(name).strip().lower()
    for canon, names in ALIASES.items():
        if key in [n.lower() for n in names]:
            return canon
    return None


def derive(values, period, warnings):
    """Add derived lines to one period's dict of canonical values."""
    v = dict(values)
    if "revenue" in v and "cogs" in v:
        v["gross_profit"] = v["revenue"] - v["cogs"]
    if "gross_profit" in v and "sga" in v:
        computed = v["gross_profit"] - v["sga"]
        if "operating_income" in v:
            gap = v["operating_income"] - computed
            if abs(gap) > CONSISTENCY_TOLERANCE * abs(v.get("revenue", 0) or 1):
                warnings.append(T("pl_oi_gap", period=period, gap=fmt_num(gap, 2)))
        else:
            v["operating_income"] = computed
    da = [v.get("depreciation"), v.get("amortization")]
    if "operating_income" in v and da[0] is not None:
        if da[1] is None:
            warnings.append(T("pl_no_amortization", period=period))
        v["ebitda"] = v["operating_income"] + sum(x for x in da if x is not None)
    if all(k in v for k in ("net_income", "income_tax", "interest_expense")) and da[0] is not None:
        v["ebitda_ni"] = (v["net_income"] + v["income_tax"] + v["interest_expense"]
                          + sum(x for x in da if x is not None))
    if all(k in v for k in ("cogs", "sga")) and da[0] is not None:
        v["opex"] = v["cogs"] + v["sga"] - sum(x for x in da if x is not None)
    for name, line in MARGINS:
        if line in v and v.get("revenue"):
            v[name] = v[line] / v["revenue"]
    return v


def main():
    parser = argparse.ArgumentParser(description="Income statement summary")
    parser.add_argument("--input", required=True, help="CSV or XLSX: item column + one column per period")
    parser.add_argument("--item-col", default="item")
    parser.add_argument("--current", help="column to analyze (default: last column)")
    parser.add_argument("--compare", help="comparison column (default: column before current)")
    parser.add_argument("--threshold-pct", type=float, default=DEFAULT_THRESHOLD_PCT)
    parser.add_argument("--threshold-amount", type=float)
    parser.add_argument("--unit", default="")
    add_common_args(parser)
    args = parser.parse_args()
    d = args.decimals

    frame = load_table(args.input)
    if args.item_col not in frame.columns:
        raise InputError(T("missing_columns", path=args.input, columns=args.item_col,
                           available=", ".join(map(str, frame.columns))))
    periods = [c for c in frame.columns if c != args.item_col]
    if not periods:
        raise InputError(T("pl_no_periods"))
    current = args.current or periods[-1]
    compare = args.compare or (periods[periods.index(current) - 1] if periods.index(current) > 0 else None)
    warnings, data, unknown = [], {}, []
    for period in periods:
        values = {}
        for _, row in frame.iterrows():
            key = canonical(row[args.item_col])
            if key is None:
                if period == periods[0]:
                    unknown.append(str(row[args.item_col]))
                continue
            values[key] = to_float(row[period], f"{row[args.item_col]}.{period}")
        data[period] = derive(values, period, warnings)
    if unknown:
        warnings.append(T("pl_unknown_items", items=", ".join(unknown)))
    if "revenue" not in data[current]:
        raise InputError(T("pl_needs_revenue"))

    cols = [p for p in (compare, current) if p is not None]
    report = Report(d)
    rows = []
    for line in LINE_ORDER:
        if not any(line in data[p] for p in cols):
            continue
        row = [T(f"pl_{line}")] + [num(data[p].get(line)) for p in cols]
        if compare and line in data[current] and line in data[compare]:
            change = data[current][line] - data[compare][line]
            base = data[compare][line]
            rate = change / abs(base) if base else None
            flagged = (rate is not None and abs(rate) * 100 >= args.threshold_pct) or \
                      (args.threshold_amount is not None and abs(change) >= args.threshold_amount)
            row += [num(change), pct(rate), "O" if flagged else ""]
        elif compare:
            row += [None, None, ""]
        rows.append(row)
    headers = [T("line_item")] + [str(p) for p in cols]
    if compare:
        headers += [T("change"), T("change_pct"), T("flag")]
    unit_note = f" ({args.unit})" if args.unit else ""
    report.table(T("pl_table") + unit_note, headers, rows)

    margin_rows = []
    for name, _ in MARGINS:
        if name in data[current]:
            row = [T(f"pl_{name}")] + [pct(data[p].get(name)) for p in cols]
            if compare and name in data[compare]:
                row.append(num((data[current][name] - data[compare][name]) * 100))
            margin_rows.append(row)
    report.table(T("pl_margins"), [T("indicator")] + [str(p) for p in cols]
                 + ([T("change_pp")] if compare else []), margin_rows)
    if compare:
        rule = (T("pl_threshold_desc", pct=args.threshold_pct, amount=fmt_num(args.threshold_amount, d))
                if args.threshold_amount is not None else T("pl_threshold_pct_only", pct=args.threshold_pct))
        report.note(T("pl_threshold"), rule)
    report.warnings(warnings)
    report.finish(args, {"current": current, "compare": compare, "data": data, "warnings": warnings})

    if args.chart:
        if not compare or not all(k in data[p] for p in cols for k in ("revenue", "cogs", "sga", "operating_income")):
            raise InputError(T("pl_chart_needs"))
        c, p = data[current], data[compare]
        steps = [(T("pl_revenue"), c["revenue"] - p["revenue"]), (T("pl_cogs"), -(c["cogs"] - p["cogs"])),
                 (T("pl_sga"), -(c["sga"] - p["sga"]))]
        other = (c["operating_income"] - p["operating_income"]) - sum(s[1] for s in steps)
        if abs(other) > 1e-9:
            steps.append((T("other"), other))
        chart.waterfall((f"{compare}", p["operating_income"]), steps, (f"{current}", c["operating_income"]),
                        args.chart, chart_formatter([p["operating_income"], c["operating_income"]]
                                                    + [s[1] for s in steps], d))


if __name__ == "__main__":
    run_main(main)
