"""Market concentration: HHI and CRk.

HHI = sum of squared market shares in percent (0 - 10,000).
CRk = combined share of the k largest firms.
Merger change: delta HHI = 2 * share_a * share_b.
"""
import argparse

import chart
from common import (InputError, Report, add_common_args, fmt_num, load_table, num, pct,
                    require_columns, run_main, to_float)
from labels import T

SHARE_TOLERANCE = 0.5  # percentage points allowed above 100 for rounding in published shares


def main():
    parser = argparse.ArgumentParser(description="HHI and concentration ratios")
    parser.add_argument("--input", required=True, help="CSV or XLSX, one row per firm")
    parser.add_argument("--firm-col", default="firm")
    parser.add_argument("--value-col", default="value")
    parser.add_argument("--shares", action="store_true",
                        help="values are market shares in percent (otherwise sales amounts)")
    parser.add_argument("--k", default="1,3,4", help="comma-separated k values for CRk")
    parser.add_argument("--merge", help="two firm names joined by a comma, to test a merger")
    add_common_args(parser)
    args = parser.parse_args()
    d = args.decimals

    frame = load_table(args.input)
    require_columns(frame, [args.firm_col, args.value_col], args.input)
    firms = [(str(r[args.firm_col]).strip(), to_float(r[args.value_col], args.value_col))
             for _, r in frame.dropna(subset=[args.firm_col]).iterrows()]
    if any(v < 0 for _, v in firms):
        raise InputError(T("hhi_negative"))
    warnings = []
    if args.shares:
        shares = dict(firms)
        covered = sum(shares.values())
        if covered > 100 + SHARE_TOLERANCE:
            raise InputError(T("hhi_share_over", total=fmt_num(covered, d)))
    else:
        total = sum(v for _, v in firms)
        if total <= 0:
            raise InputError(T("hhi_total_zero"))
        shares = {f: v / total * 100 for f, v in firms}
        covered = 100.0
    residual = max(0.0, 100 - covered)
    ranked = sorted(shares.items(), key=lambda x: -x[1])
    hhi_known = sum(s ** 2 for _, s in ranked)
    hhi_upper = hhi_known + residual ** 2
    if residual > 0:
        warnings.append(T("hhi_residual", residual=fmt_num(residual, d)))

    ks = [int(k) for k in args.k.split(",") if k.strip()]
    cr = {k: sum(s for _, s in ranked[:k]) for k in ks}

    report = Report(d)
    report.table(T("inputs"), [T("item"), T("value")], [
        [T("firms"), len(ranked)], [T("input_type"), T("shares_pct") if args.shares else T("sales_amount")],
        [T("share_covered"), pct(covered / 100)]])
    report.table(T("steps"), [T("rank"), T("firm"), T("share"), T("share_squared")],
                 [[i + 1, f, pct(s / 100), num(s ** 2)] for i, (f, s) in enumerate(ranked)])
    if residual == 0:
        result_rows = [["HHI", num(hhi_known)]]
    else:
        result_rows = [[T("hhi_low"), num(hhi_known)], [T("hhi_high"), num(hhi_upper)]]
    result_rows += [[f"CR{k}", pct(v / 100)] for k, v in cr.items()]
    output = {"shares": dict(ranked), "residual": residual, "hhi": hhi_known,
              "hhi_upper": hhi_upper, "cr": cr}
    if args.merge:
        names = [n.strip() for n in args.merge.split(",")]
        if len(names) != 2 or any(n not in shares for n in names):
            raise InputError(T("hhi_merge_names", names=args.merge))
        delta = 2 * shares[names[0]] * shares[names[1]]
        result_rows.append([T("hhi_delta"), num(delta)])
        if residual == 0:
            result_rows.append([T("hhi_post"), num(hhi_known + delta)])
        else:
            result_rows += [[T("hhi_post_low"), num(hhi_known + delta)],
                            [T("hhi_post_high"), num(hhi_upper + delta)]]
        result_rows.append([T("merged_share"), pct((shares[names[0]] + shares[names[1]]) / 100)])
        output["merge"] = {"firms": names, "delta": delta, "post_hhi": hhi_known + delta}
    report.table(T("result"), [T("indicator"), T("value")], result_rows)
    report.warnings(warnings)
    report.finish(args, output)
    if args.chart:
        chart.barh([f for f, _ in ranked], [s for _, s in ranked], args.chart,
                   lambda v: fmt_num(v, 1) + "%")


if __name__ == "__main__":
    run_main(main)
