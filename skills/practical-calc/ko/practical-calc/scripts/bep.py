"""Break-even point (cost-volume-profit analysis) for one or more products.

Contribution margin per unit = price - variable cost
Break-even units = fixed cost / weighted contribution margin per unit
Break-even sales = fixed cost / contribution margin ratio
Several products are combined by their unit sales mix.
"""
import argparse

import chart
from common import InputError, Report, add_common_args, fmt_num, load_json, num, pct, run_main, to_float
from labels import T

CHART_RANGE_FACTOR = 1.6  # chart x-axis extends past the break-even point


def main():
    parser = argparse.ArgumentParser(description="Break-even analysis")
    parser.add_argument("--input", required=True, help="JSON file, see references/corporate.md")
    add_common_args(parser)
    args = parser.parse_args()
    d = args.decimals
    cfg = load_json(args.input)
    warnings = []

    unit = cfg.get("unit", "")
    fixed = to_float(cfg["fixed_cost"], "fixed_cost")
    products = cfg["products"]
    weights = [to_float(p.get("mix", 1), f"{p['name']}.mix") for p in products]
    if any(w < 0 for w in weights) or sum(weights) <= 0:
        raise InputError(T("bep_mix_invalid"))
    mix = [w / sum(weights) for w in weights]
    if abs(sum(weights) - 1) > 1e-9:
        warnings.append(T("bep_mix_normalized"))
    rows = []
    for p, m in zip(products, mix):
        price = to_float(p["price"], f"{p['name']}.price")
        vc = to_float(p["variable_cost"], f"{p['name']}.variable_cost")
        rows.append({"name": p["name"], "mix": m, "price": price, "variable_cost": vc, "cm": price - vc})
    w_price = sum(r["mix"] * r["price"] for r in rows)
    w_cm = sum(r["mix"] * r["cm"] for r in rows)
    if w_cm <= 0:
        raise InputError(T("bep_cm_nonpositive"))
    cm_ratio = w_cm / w_price
    bep_units = fixed / w_cm
    bep_sales = fixed / cm_ratio

    report = Report(d)
    report.table(T("inputs"), [T("item"), T("value")], [
        [T("unit"), unit or "-"], [T("fixed_cost"), num(fixed)], [T("products"), len(rows)]])
    report.table(T("steps"),
                 [T("product"), T("unit_mix"), T("price"), T("variable_cost"), T("cm_per_unit"), T("cm_ratio")],
                 [[r["name"], pct(r["mix"]), num(r["price"]), num(r["variable_cost"]), num(r["cm"]),
                   pct(r["cm"] / r["price"]) if r["price"] else None] for r in rows]
                 + [[T("weighted"), pct(1.0), num(w_price), num(w_price - w_cm), num(w_cm), pct(cm_ratio)]],
                 bold_last=True)

    result = [[T("bep_units"), num(bep_units)], [T("bep_sales"), num(bep_sales)]]
    if len(rows) > 1:
        result += [[f"{T('bep_units')} ({r['name']})", num(bep_units * r["mix"])] for r in rows]
    output = {"unit": unit, "fixed_cost": fixed, "products": rows, "weighted_price": w_price,
              "weighted_cm": w_cm, "cm_ratio": cm_ratio, "bep_units": bep_units, "bep_sales": bep_sales}

    if "target_profit" in cfg:
        target = to_float(cfg["target_profit"], "target_profit")
        tax = cfg.get("tax_rate")
        pretax = target / (1 - to_float(tax, "tax_rate")) if tax is not None else target
        result += [[T("target_pretax"), num(pretax)],
                   [T("target_units"), num((fixed + pretax) / w_cm)],
                   [T("target_sales"), num((fixed + pretax) / cm_ratio)]]
        output.update({"target_pretax_profit": pretax, "target_units": (fixed + pretax) / w_cm})

    if "current_units" in cfg:
        units = to_float(cfg["current_units"], "current_units")
        sales = units * w_price
        profit = units * w_cm - fixed
        mos = sales - bep_sales
        result += [[T("current_sales"), num(sales)], [T("operating_profit"), num(profit)],
                   [T("mos_amount"), num(mos)], [T("mos_ratio"), pct(mos / sales) if sales else None]]
        if profit > 0:
            result.append([T("dol"), num(units * w_cm / profit)])
        else:
            warnings.append(T("dol_undefined"))
        output.update({"current_units": units, "current_sales": sales, "operating_profit": profit,
                       "margin_of_safety": mos})
    report.table(T("result"), [T("indicator"), T("value")], result)
    report.warnings(warnings)
    report.finish(args, output)
    if args.chart:
        top = max(bep_units, output.get("current_units", 0)) * CHART_RANGE_FACTOR
        xs = [top * i / 50 for i in range(51)]
        chart.lines(xs, [(T("revenue"), [x * w_price for x in xs]),
                         (T("total_cost"), [fixed + x * (w_price - w_cm) for x in xs])],
                    args.chart, T("units_axis"), f"{T('amount')} ({unit})" if unit else T("amount"),
                    marker=(bep_units, bep_sales, f"BEP {fmt_num(bep_units, 0)}"))


if __name__ == "__main__":
    run_main(main)
