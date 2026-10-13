"""Economic ripple effects from input-output inducement coefficients.

induced output       = spending * output inducement coefficient
induced value added  = spending * value-added inducement coefficient
induced employment   = spending / coefficient base amount * employment coefficient
                       (Bank of Korea tables state persons per 1 billion KRW)
"""
import argparse

import chart
from common import (InputError, Report, add_common_args, chart_formatter, fmt_num, load_table, num,
                    require_columns, run_main, to_float)
from labels import LANG, T

UNIT_TO_WON = {"원": 1, "천원": 1e3, "백만원": 1e6, "억원": 1e8, "십억원": 1e9,
               "KRW": 1, "thousand KRW": 1e3, "million KRW": 1e6, "100 million KRW": 1e8,
               "billion KRW": 1e9}
EMPLOYMENT_BASE_WON = 1e9  # coefficients are published as persons per 1 billion won


def main():
    parser = argparse.ArgumentParser(description="Input-output ripple effects")
    parser.add_argument("--input", required=True, help="CSV or XLSX, one row per product group")
    parser.add_argument("--unit", default="억원" if LANG == "ko" else "100 million KRW",
                        help="unit of the amount column: " + ", ".join(UNIT_TO_WON))
    parser.add_argument("--total", type=float, help="total spending to check the allocation against")
    parser.add_argument("--item-col", default="item")
    parser.add_argument("--amount-col", default="amount")
    parser.add_argument("--output-col", default="output_coef")
    parser.add_argument("--va-col", default="va_coef")
    parser.add_argument("--emp-col", default="emp_coef")
    parser.add_argument("--emp-type", default="employment", choices=["employment", "jobs"],
                        help="employment = wage employees (고용), jobs = incl. self-employed (취업)")
    parser.add_argument("--emp-base", type=float,
                        help="amount, in --unit, per which the employment coefficient is stated; "
                             "needed for non-KRW tables (e.g. 1 for persons per 1 USD million)")
    add_common_args(parser)
    args = parser.parse_args()
    d = args.decimals
    if args.emp_base is not None:
        if args.emp_base <= 0:
            raise InputError(T("emp_base_positive"))
        emp_factor = 1 / args.emp_base
        basis_text = T("emp_base_desc", base=fmt_num(args.emp_base, 6).rstrip("0").rstrip("."), unit=args.unit)
    elif args.unit in UNIT_TO_WON:
        emp_factor = UNIT_TO_WON[args.unit] / EMPLOYMENT_BASE_WON
        basis_text = T("emp_coef_unit")
    else:
        raise InputError(T("unit_needs_emp_base", unit=args.unit, options=", ".join(UNIT_TO_WON)))

    frame = load_table(args.input)
    cols = [args.item_col, args.amount_col, args.output_col, args.va_col, args.emp_col]
    require_columns(frame, cols, args.input)
    warnings, rows = [], []
    for _, r in frame.dropna(subset=[args.item_col]).iterrows():
        item = str(r[args.item_col])
        amount = to_float(r[args.amount_col], f"{item}.amount")
        pc = to_float(r[args.output_col], f"{item}.output_coef")
        vc = to_float(r[args.va_col], f"{item}.va_coef")
        ec = to_float(r[args.emp_col], f"{item}.emp_coef")
        if amount < 0:
            raise InputError(T("amount_negative", item=item))
        if pc < 1:
            warnings.append(T("io_output_below_one", item=item, value=pc))
        if vc > 1:
            warnings.append(T("io_va_above_one", item=item, value=vc))
        rows.append({"item": item, "amount": amount, "output_coef": pc, "va_coef": vc, "emp_coef": ec,
                     "output": amount * pc, "value_added": amount * vc,
                     "employment": amount * emp_factor * ec})
    if not rows:
        raise InputError(T("no_rows"))
    spend = sum(r["amount"] for r in rows)
    if args.total is not None and abs(spend - args.total) > 1e-6 * max(1.0, abs(args.total)):
        warnings.append(T("io_total_mismatch", allocated=fmt_num(spend, d), total=fmt_num(args.total, d)))

    emp_label = T("emp_employment") if args.emp_type == "employment" else T("emp_jobs")
    emp_coef_label = T("emp_coef_employment") if args.emp_type == "employment" else T("emp_coef_jobs")
    report = Report(d)
    report.table(T("inputs"), [T("item"), T("value")], [
        [T("unit"), args.unit], [T("total_spending"), num(spend)],
        [T("emp_coef_basis"), basis_text],
        [T("unit_conversion"), T("unit_conversion_desc", unit=args.unit, factor=fmt_num(emp_factor, 6))]])
    totals = {k: sum(r[k] for r in rows) for k in ("output", "value_added", "employment")}
    step_rows = [[r["item"], num(r["amount"]), num(r["output_coef"], 4), num(r["va_coef"], 4),
                  num(r["emp_coef"], 4), num(r["output"]), num(r["value_added"]), num(r["employment"])]
                 for r in rows]
    step_rows.append([T("total"), num(spend), "", "", "", num(totals["output"]),
                      num(totals["value_added"]), num(totals["employment"])])
    report.table(T("steps"),
                 [T("product_group"), f"{T('spending')} ({args.unit})", T("output_coef"), T("va_coef"),
                  emp_coef_label, f"{T('induced_output')} ({args.unit})",
                  f"{T('induced_va')} ({args.unit})", f"{emp_label} ({T('persons')})"],
                 step_rows, bold_last=True)
    report.table(T("result"), [T("indicator"), T("value")], [
        [f"{T('induced_output')} ({args.unit})", num(totals["output"])],
        [f"{T('induced_va')} ({args.unit})", num(totals["value_added"])],
        [f"{emp_label} ({T('persons')})", num(totals["employment"])],
        [T("output_multiplier"), num(totals["output"] / spend if spend else float("nan"), 4)]])
    report.warnings(warnings)
    report.finish(args, {"unit": args.unit, "spending": spend, "rows": rows, "totals": totals,
                         "employment_type": args.emp_type, "warnings": warnings})
    if args.chart:
        ordered = sorted(rows, key=lambda r: -r["output"])
        values = [r["output"] for r in ordered]
        chart.barh([r["item"] for r in ordered], values, args.chart, chart_formatter(values, d))


if __name__ == "__main__":
    run_main(main)
