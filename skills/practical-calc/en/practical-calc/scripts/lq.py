"""Location quotient (LQ) and national share for one industry across regions.

LQ(region r, industry i) = (x_ri / X_r) / (x_Ni / X_N)
national share           = x_ri / x_Ni
x = employees or establishments, X = all-industry total, N = nation.
"""
import argparse

import chart
from common import (InputError, Report, add_common_args, fmt_num, load_table, num, pct,
                    require_columns, run_main, to_float)
from labels import T

DEFAULT_THRESHOLD = 1.0


def apply_filters(frame, filters, path):
    for expr in filters or []:
        if "=" not in expr:
            raise InputError(T("filter_format", expr=expr))
        col, value = expr.split("=", 1)
        require_columns(frame, [col], path)
        frame = frame[frame[col].astype(str).str.strip() == value.strip()]
    return frame


def main():
    parser = argparse.ArgumentParser(description="Location quotient")
    parser.add_argument("--input", required=True, help="CSV or XLSX in long format")
    parser.add_argument("--industry", required=True, help="target industry label")
    parser.add_argument("--region-col", default="region")
    parser.add_argument("--industry-col", default="industry")
    parser.add_argument("--value-col", default="value")
    parser.add_argument("--national-label", help="region label of the national row, e.g. 전국")
    parser.add_argument("--total-label", help="industry label of the all-industry row, e.g. 전체")
    parser.add_argument("--filter", action="append", help="keep rows where COLUMN=VALUE, repeatable")
    parser.add_argument("--measure", default="", help="label only, e.g. employees or establishments")
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    parser.add_argument("--sheet")
    add_common_args(parser)
    args = parser.parse_args()
    d = args.decimals

    frame = load_table(args.input, args.sheet)
    require_columns(frame, [args.region_col, args.industry_col, args.value_col], args.input)
    frame = apply_filters(frame, args.filter, args.input)
    frame = frame[[args.region_col, args.industry_col, args.value_col]].copy()
    frame.columns = ["region", "industry", "value"]
    frame["region"] = frame["region"].astype(str).str.strip()
    frame["industry"] = frame["industry"].astype(str).str.strip()
    frame["value"] = [to_float(v, args.value_col) for v in frame["value"]]
    frame = frame.groupby(["region", "industry"], as_index=False)["value"].sum()
    warnings = []

    if args.industry not in set(frame["industry"]):
        raise InputError(T("industry_not_found", industry=args.industry))
    table = frame.pivot(index="region", columns="industry", values="value").fillna(0.0)

    if args.total_label:
        if args.total_label not in table.columns:
            raise InputError(T("total_label_missing", label=args.total_label))
        totals = table[args.total_label]
    else:
        totals = table.sum(axis=1)
        warnings.append(T("lq_total_summed"))
    if args.national_label:
        if args.national_label not in table.index:
            raise InputError(T("national_label_missing", label=args.national_label))
        nat_ind = table.loc[args.national_label, args.industry]
        nat_total = totals[args.national_label]
        regions = [r for r in table.index if r != args.national_label]
    else:
        regions = list(table.index)
        nat_ind = table.loc[regions, args.industry].sum()
        nat_total = totals[regions].sum()
        warnings.append(T("lq_nation_summed"))
    if nat_ind <= 0 or nat_total <= 0:
        raise InputError(T("lq_nation_zero"))
    nat_share = nat_ind / nat_total

    results = []
    for region in regions:
        local_total = totals[region]
        if local_total <= 0:
            warnings.append(T("lq_region_zero", region=region))
            continue
        x = table.loc[region, args.industry]
        local_share = x / local_total
        results.append({"region": region, "value": x, "region_total": local_total,
                        "local_share": local_share, "lq": local_share / nat_share,
                        "national_share": x / nat_ind})
    results.sort(key=lambda r: -r["lq"])

    report = Report(d)
    report.table(T("inputs"), [T("item"), T("value")], [
        [T("industry_target"), args.industry], [T("measure"), args.measure or "-"],
        [T("filters"), "; ".join(args.filter) if args.filter else "-"],
        [T("national_industry"), num(nat_ind, 0)], [T("national_total"), num(nat_total, 0)],
        [T("national_ratio"), pct(nat_share)]])
    report.table(T("result"),
                 [T("rank"), T("region"), T("industry_value"), T("region_total"), T("region_ratio"),
                  "LQ", T("national_share")],
                 [[i + 1, r["region"], num(r["value"], 0), num(r["region_total"], 0),
                   pct(r["local_share"]), num(r["lq"]), pct(r["national_share"])]
                  for i, r in enumerate(results)])
    above = [r["region"] for r in results if r["lq"] >= args.threshold]
    report.note(T("lq_above_threshold", t=args.threshold), ", ".join(above) if above else "-")
    report.warnings(warnings)
    report.finish(args, {"industry": args.industry, "measure": args.measure, "threshold": args.threshold,
                         "national_ratio": nat_share, "rows": results, "warnings": warnings})
    if args.chart:
        colors = [chart.PALETTE["primary"] if r["lq"] >= args.threshold else chart.PALETTE["light"]
                  for r in results]
        chart.barh([r["region"] for r in results], [r["lq"] for r in results], args.chart,
                   lambda v: fmt_num(v, d), colors=colors, ref_line=args.threshold)


if __name__ == "__main__":
    run_main(main)
