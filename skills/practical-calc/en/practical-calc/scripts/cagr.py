"""CAGR (compound annual growth rate) between two points in time.

CAGR = (end value / start value) ** (1 / years) - 1, years = end year - start year.
"""
import argparse

import chart
from common import (InputError, Report, add_common_args, chart_formatter, fmt_pct, load_table,
                    num, pct, require_columns, run_main, to_float)
from labels import T


def compute_cagr(start_value, end_value, years):
    """Return CAGR as a ratio. Raises InputError where CAGR is undefined."""
    if years <= 0:
        raise InputError(T("cagr_years_positive", years=years))
    if start_value <= 0:
        raise InputError(T("cagr_start_positive", value=start_value))
    if end_value < 0:
        raise InputError(T("cagr_end_negative", value=end_value))
    return (end_value / start_value) ** (1 / years) - 1


def read_series(path, year_col, value_col):
    frame = load_table(path)
    require_columns(frame, [year_col, value_col], path)
    frame = frame[[year_col, value_col]].dropna().sort_values(year_col)
    if len(frame) < 2:
        raise InputError(T("series_too_short"))
    return [(int(row[year_col]), to_float(row[value_col], value_col))
            for _, row in frame.iterrows()]


def main():
    parser = argparse.ArgumentParser(description="CAGR calculator")
    parser.add_argument("--start-value", type=float)
    parser.add_argument("--end-value", type=float)
    parser.add_argument("--start-year", type=int)
    parser.add_argument("--end-year", type=int)
    parser.add_argument("--years", type=float,
                        help="override the period length (for non-annual spacing)")
    parser.add_argument("--input", help="CSV or XLSX with a year column and a value column")
    parser.add_argument("--year-col", default="year")
    parser.add_argument("--value-col", default="value")
    add_common_args(parser)
    args = parser.parse_args()
    d = args.decimals
    report = Report(d)

    series = None
    if args.input:
        series = read_series(args.input, args.year_col, args.value_col)
        (start_year, start_value), (end_year, end_value) = series[0], series[-1]
    else:
        needed = [args.start_value, args.end_value, args.start_year, args.end_year]
        if any(v is None for v in needed):
            raise InputError(T("cagr_missing_args"))
        start_year, end_year = args.start_year, args.end_year
        start_value, end_value = args.start_value, args.end_value
    years = args.years if args.years is not None else end_year - start_year
    rate = compute_cagr(start_value, end_value, years)

    report.table(T("inputs"), [T("item"), T("value")],
                 [[T("start_year"), start_year], [T("end_year"), end_year],
                  [T("start_value"), num(start_value)], [T("end_value"), num(end_value)],
                  [T("period_years"), num(years)]])
    report.table(T("steps"), [T("step"), T("formula"), T("value")],
                 [[T("growth_multiple"), T("end_div_start"), num(end_value / start_value, 6)],
                  [T("cagr"), T("cagr_formula"), pct(rate, d + 2)]])
    if series:
        rows, previous = [], None
        for year, value in series:
            change = pct(value / previous - 1) if previous not in (None, 0) else None
            rows.append([year, num(value), change])
            previous = value
        report.table(T("yearly_series"), [T("year"), T("value"), T("yoy")], rows)
    report.note(T("result"), f"```\n{fmt_pct(rate, d)}\n```")

    report.finish(args, {"start_year": start_year, "end_year": end_year,
                         "start_value": start_value, "end_value": end_value,
                         "years": years, "cagr": rate})
    if args.chart:
        if not series:
            raise InputError(T("chart_needs_series"))
        values = [v for _, v in series]
        chart.bar([y for y, _ in series], values, args.chart, chart_formatter(values, d))


if __name__ == "__main__":
    run_main(main)
