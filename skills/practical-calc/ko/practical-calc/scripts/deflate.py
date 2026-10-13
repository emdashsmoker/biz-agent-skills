"""Convert nominal (current-price) values to real (constant-price) values.

real value in year t = nominal value in year t * index(base year) / index(year t)
"""
import argparse

import chart
from cagr import compute_cagr
from common import (InputError, Report, add_common_args, chart_formatter, load_table, num, pct,
                    require_columns, run_main, to_float)
from labels import T


def deflate(rows, base_year):
    """rows: list of (year, nominal, index). Returns list of dicts."""
    index_by_year = {year: index for year, _, index in rows}
    if base_year not in index_by_year:
        raise InputError(T("base_year_missing", year=base_year))
    base_index = index_by_year[base_year]
    result = []
    for year, nominal, index in rows:
        if index <= 0:
            raise InputError(T("index_positive", year=year))
        factor = base_index / index
        result.append({"year": year, "nominal": nominal, "index": index,
                       "factor": factor, "real": nominal * factor})
    return result


def main():
    parser = argparse.ArgumentParser(description="Nominal to real conversion")
    parser.add_argument("--input", required=True, help="CSV or XLSX")
    parser.add_argument("--base-year", type=int, required=True)
    parser.add_argument("--year-col", default="year")
    parser.add_argument("--value-col", default="nominal")
    parser.add_argument("--index-col", default="index")
    add_common_args(parser)
    args = parser.parse_args()
    d = args.decimals
    report = Report(d)

    frame = load_table(args.input)
    require_columns(frame, [args.year_col, args.value_col, args.index_col], args.input)
    frame = frame.dropna(subset=[args.year_col, args.value_col, args.index_col]).sort_values(args.year_col)
    rows = [(int(r[args.year_col]), to_float(r[args.value_col], args.value_col),
             to_float(r[args.index_col], args.index_col)) for _, r in frame.iterrows()]
    result = deflate(rows, args.base_year)

    report.table(T("inputs"), [T("item"), T("value")],
                 [[T("price_base_year"), args.base_year], [T("rows"), len(result)]])
    report.table(T("steps"),
                 [T("year"), T("nominal"), T("price_index"), T("conversion_factor"), T("real")],
                 [[r["year"], num(r["nominal"]), num(r["index"]), num(r["factor"], 6), num(r["real"])]
                  for r in result])
    summary = {}
    if len(result) >= 2 and result[0]["nominal"] > 0 and result[0]["real"] > 0:
        years = result[-1]["year"] - result[0]["year"]
        summary = {"nominal_cagr": compute_cagr(result[0]["nominal"], result[-1]["nominal"], years),
                   "real_cagr": compute_cagr(result[0]["real"], result[-1]["real"], years)}
        report.table(T("result"), [T("item"), T("value")],
                     [[T("nominal_cagr"), pct(summary["nominal_cagr"])],
                      [T("real_cagr"), pct(summary["real_cagr"])]])

    report.finish(args, {"base_year": args.base_year, "rows": result, **summary})
    if args.chart:
        values = [r["real"] for r in result]
        chart.bar([r["year"] for r in result], values, args.chart, chart_formatter(values, d))


if __name__ == "__main__":
    run_main(main)
