"""CAPEX measurement, CAPEX intensity, free cash flow and depreciation schedules.

Cash basis:        CAPEX = purchases of PP&E + purchases of intangible assets
Roll-forward basis: CAPEX = net PP&E(end) - net PP&E(begin) + depreciation
                            + book value of disposals + impairment
                    (same pattern for intangible assets with amortization)
Free cash flow = operating cash flow - CAPEX
"""
import argparse

import chart
from common import (InputError, Report, add_common_args, chart_formatter, load_json, num, pct, run_main,
                    to_float)
from labels import T


def field_value(entry, key, default=None):
    if key not in entry or entry[key] is None:
        return default
    return to_float(entry[key], key)


def capex_for_period(p):
    """Return (capex, basis) for one period dict."""
    ppe_buy, int_buy = field_value(p, "ppe_purchase"), field_value(p, "intangible_purchase")
    if ppe_buy is not None or int_buy is not None:
        return (ppe_buy or 0.0) + (int_buy or 0.0), "cash"
    if all(field_value(p, k) is not None for k in ("net_ppe_begin", "net_ppe_end", "depreciation")):
        capex = (field_value(p, "net_ppe_end") - field_value(p, "net_ppe_begin")
                 + field_value(p, "depreciation") + field_value(p, "ppe_disposals_nbv", 0.0)
                 + field_value(p, "ppe_impairment", 0.0))
        intangible_keys = ("net_intangible_begin", "net_intangible_end", "amortization")
        if all(field_value(p, k) is not None for k in intangible_keys):
            capex += (field_value(p, "net_intangible_end") - field_value(p, "net_intangible_begin")
                      + field_value(p, "amortization") + field_value(p, "intangible_disposals_nbv", 0.0)
                      + field_value(p, "intangible_impairment", 0.0))
        return capex, "rollforward"
    raise InputError(T("capex_needs_inputs", period=p.get("period", "?")))


def schedule(asset):
    """Yearly depreciation for one asset: straight-line or fixed-rate declining balance."""
    name = asset.get("name", "asset")
    cost, residual = to_float(asset["cost"], f"{name}.cost"), to_float(asset.get("residual", 0), f"{name}.residual")
    life, start = int(asset["life"]), int(asset["start_year"])
    method = asset.get("method", "straight")
    if life <= 0 or cost <= 0 or residual < 0 or residual >= cost:
        raise InputError(T("dep_invalid", name=name))
    rows, book = [], cost
    if method == "straight":
        charge = (cost - residual) / life
        for k in range(life):
            rows.append((start + k, book, charge, book - charge))
            book -= charge
    elif method == "declining":
        if residual <= 0:
            raise InputError(T("dep_declining_residual", name=name))
        rate = 1 - (residual / cost) ** (1 / life)
        for k in range(life):
            charge = book * rate
            rows.append((start + k, book, charge, book - charge))
            book -= charge
    else:
        raise InputError(T("dep_method_invalid", name=name, method=method))
    return rows


def main():
    parser = argparse.ArgumentParser(description="CAPEX, FCF and depreciation")
    parser.add_argument("--input", required=True, help="JSON file, see references/corporate.md")
    add_common_args(parser)
    args = parser.parse_args()
    d = args.decimals
    cfg = load_json(args.input)
    unit = cfg.get("unit", "")
    warnings, output = [], {"unit": unit, "periods": [], "schedules": {}}

    period_rows = []
    for p in cfg.get("periods", []):
        capex, basis = capex_for_period(p)
        revenue, ocf = field_value(p, "revenue"), field_value(p, "operating_cash_flow")
        intensity = capex / revenue if revenue else None
        fcf = ocf - capex if ocf is not None else None
        if basis == "rollforward":
            warnings.append(T("capex_rollforward_note", period=p.get("period", "?")))
        output["periods"].append({"period": p.get("period"), "capex": capex, "basis": basis,
                                  "capex_intensity": intensity, "fcf": fcf})
        period_rows.append([p.get("period", "-"), T(f"capex_basis_{basis}"), num(capex),
                            pct(intensity), num(ocf), num(fcf)])
    report = Report(d)
    if period_rows:
        report.table(T("capex_table") + (f" ({unit})" if unit else ""),
                     [T("period"), T("basis"), "CAPEX", T("capex_intensity"), T("ocf"), T("fcf")], period_rows)

    totals = {}
    for asset in cfg.get("assets", []):
        rows = schedule(asset)
        name = asset.get("name", "asset")
        output["schedules"][name] = [{"year": y, "begin": b, "depreciation": c, "end": e} for y, b, c, e in rows]
        for y, _, c, _ in rows:
            totals[y] = totals.get(y, 0.0) + c
        report.table(f"{T('dep_schedule')}: {name} ({T('dep_' + asset.get('method', 'straight'))})",
                     [T("year"), T("book_begin"), T("depreciation"), T("book_end")],
                     [[y, num(b), num(c), num(e)] for y, b, c, e in rows])
    if len(cfg.get("assets", [])) > 1:
        report.table(T("dep_total"), [T("year"), T("depreciation")],
                     [[y, num(v)] for y, v in sorted(totals.items())])
    output["depreciation_total"] = totals
    if not period_rows and not totals:
        raise InputError(T("capex_empty"))
    report.warnings(warnings)
    report.finish(args, output)
    if args.chart and output["periods"]:
        values = [p["capex"] for p in output["periods"]]
        chart.bar([p["period"] for p in output["periods"]], values, args.chart, chart_formatter(values, d))


if __name__ == "__main__":
    run_main(main)
