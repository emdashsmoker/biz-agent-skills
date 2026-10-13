"""Variance decomposition and forecast accuracy.

mix mode (per item i, B = budget or prior, A = actual):
  price effect    = (AP_i - BP_i) * AQ_i
  mix effect      = (AQ_i - AQ_total * Bmix_i) * BP_i
  quantity effect = (AQ_total * Bmix_i - BQ_i) * BP_i
  total           = AP_i * AQ_i - BP_i * BQ_i   (the three effects add up exactly)
accuracy mode:
  accuracy = 1 - |A - F| / |A| ; MAPE = mean of |A - F| / |A| over periods with A != 0
"""
import argparse

import chart
from common import (InputError, Report, add_common_args, chart_formatter, load_table, num, pct,
                    require_columns, run_main, to_float)
from labels import T

RECONCILE_TOLERANCE = 1e-6


def optional(row, col):
    value = row.get(col)
    if value is None or (isinstance(value, float) and value != value):
        return None
    return to_float(value, col)


def decompose(items):
    """items: list of dicts with bq, bp, aq, ap (None allowed for new or dropped items)."""
    notes = []
    for it in items:
        if it["bq"] == 0 and it["bp"] is None:
            it["bp"] = it["ap"]
            notes.append(T("var_new_item", item=it["name"]))
        if it["aq"] == 0 and it["ap"] is None:
            it["ap"] = it["bp"]
            notes.append(T("var_dropped_item", item=it["name"]))
        if it["bp"] is None or it["ap"] is None:
            raise InputError(T("var_missing_price", item=it["name"]))
    bq_total = sum(it["bq"] for it in items)
    aq_total = sum(it["aq"] for it in items)
    if bq_total <= 0:
        raise InputError(T("var_budget_qty_zero"))
    for it in items:
        bmix = it["bq"] / bq_total
        it["budget"] = it["bq"] * it["bp"]
        it["actual"] = it["aq"] * it["ap"]
        it["price"] = (it["ap"] - it["bp"]) * it["aq"]
        it["mix"] = (it["aq"] - aq_total * bmix) * it["bp"]
        it["quantity"] = (aq_total * bmix - it["bq"]) * it["bp"]
        it["total"] = it["actual"] - it["budget"]
        check = it["price"] + it["mix"] + it["quantity"] - it["total"]
        if abs(check) > RECONCILE_TOLERANCE * max(1.0, abs(it["total"])):
            raise InputError(T("var_reconcile_fail", item=it["name"]))
    return items, notes


def run_mix(args):
    d = args.decimals
    frame = load_table(args.input)
    cols = [args.item_col, args.bq_col, args.bp_col, args.aq_col, args.ap_col]
    require_columns(frame, cols, args.input)
    items = []
    for _, r in frame.dropna(subset=[args.item_col]).iterrows():
        items.append({"name": str(r[args.item_col]), "bq": optional(r, args.bq_col) or 0.0,
                      "bp": optional(r, args.bp_col), "aq": optional(r, args.aq_col) or 0.0,
                      "ap": optional(r, args.ap_col)})
    items, notes = decompose(items)
    keys = ("budget", "actual", "price", "mix", "quantity", "total")
    rows = [[it["name"]] + [num(it[k]) for k in keys] for it in items]
    sums = {k: sum(it[k] for it in items) for k in keys}
    rows.append([T("total")] + [num(sums[k]) for k in keys])
    basis = T("var_basis_margin") if args.basis == "margin" else T("var_basis_revenue")
    report = Report(d)
    report.table(T("inputs"), [T("item"), T("value")], [[T("basis"), basis], [T("items"), len(items)]])
    report.table(T("steps"), [T("item"), T("var_budget"), T("var_actual"), T("var_price"),
                              T("var_mix"), T("var_quantity"), T("var_total")], rows, bold_last=True)

    def share(key):
        return pct(sums[key] / sums["total"]) if sums["total"] else None

    report.table(T("result"), [T("indicator"), T("value"), T("share_of_total")], [
        [T("var_price"), num(sums["price"]), share("price")],
        [T("var_mix"), num(sums["mix"]), share("mix")],
        [T("var_quantity"), num(sums["quantity"]), share("quantity")],
        [T("var_total"), num(sums["total"]), share("total")]])
    report.warnings(notes)
    report.finish(args, {"basis": args.basis, "items": items, "totals": sums})
    if args.chart:
        chart.waterfall((T("var_budget"), sums["budget"]),
                        [(T("var_price"), sums["price"]), (T("var_mix"), sums["mix"]),
                         (T("var_quantity"), sums["quantity"])],
                        (T("var_actual"), sums["actual"]), args.chart,
                        chart_formatter([sums["budget"], sums["actual"]], d))


def run_accuracy(args):
    d = args.decimals
    frame = load_table(args.input)
    require_columns(frame, [args.period_col, args.forecast_col, args.actual_col], args.input)
    rows, errors, skipped = [], [], []
    for _, r in frame.dropna(subset=[args.period_col]).iterrows():
        f, a = to_float(r[args.forecast_col], args.forecast_col), to_float(r[args.actual_col], args.actual_col)
        if a == 0:
            skipped.append(str(r[args.period_col]))
            rows.append([r[args.period_col], num(f), num(a), num(a - f), None])
            continue
        ape = abs(a - f) / abs(a)
        errors.append(ape)
        rows.append([r[args.period_col], num(f), num(a), num(a - f), pct(1 - ape)])
    if not errors:
        raise InputError(T("acc_no_valid"))
    mape = sum(errors) / len(errors)
    report = Report(d)
    report.table(T("steps"), [T("period"), T("forecast"), T("actual"), T("error"), T("accuracy")], rows)
    report.table(T("result"), [T("indicator"), T("value")],
                 [["MAPE", pct(mape)], [T("mean_accuracy"), pct(1 - mape)]])
    report.warnings([T("acc_skipped", periods=", ".join(skipped))] if skipped else [])
    report.finish(args, {"mape": mape, "periods_used": len(errors), "skipped": skipped})


def main():
    parser = argparse.ArgumentParser(description="Variance decomposition and forecast accuracy")
    parser.add_argument("mode", choices=["mix", "accuracy"])
    parser.add_argument("--input", required=True, help="CSV or XLSX")
    parser.add_argument("--item-col", default="item")
    parser.add_argument("--bq-col", default="budget_qty")
    parser.add_argument("--bp-col", default="budget_price")
    parser.add_argument("--aq-col", default="actual_qty")
    parser.add_argument("--ap-col", default="actual_price")
    parser.add_argument("--basis", choices=["revenue", "margin"], default="revenue",
                        help="price columns hold unit prices (revenue) or unit margins (margin)")
    parser.add_argument("--period-col", default="period")
    parser.add_argument("--forecast-col", default="forecast")
    parser.add_argument("--actual-col", default="actual")
    add_common_args(parser)
    args = parser.parse_args()
    run_mix(args) if args.mode == "mix" else run_accuracy(args)


if __name__ == "__main__":
    run_main(main)
