"""Break-even analysis (cost-volume-profit) for one or several products.

Unit contribution margin  CM_i = price_i - variable cost_i
Weighted CM per unit       WCM  = sum(mix_i * CM_i)        (mix = share of units sold)
Accounting break-even      Q*   = (cash fixed costs + depreciation) / WCM
Cash break-even            Qc   = cash fixed costs / WCM
Target volume              Qt   = (fixed costs + pre-tax target profit) / WCM
Pre-tax target from after-tax target = after-tax target / (1 - tax rate)
Margin of safety = (expected sales - break-even sales) / expected sales
Degree of operating leverage = contribution margin / operating income (at expected volume)
Straight-line depreciation = (CAPEX - salvage) / useful life
"""

from _common import (InputError, build_parser, load_input, md_table, pct,
                     require, run, section, to_number, write_json)

MIX_TOLERANCE = 1e-6

EXAMPLE = {
    "unit": "KRW",
    "products": [
        {"name": "Standard", "price": 50000, "variable_cost": 30000, "mix": 0.7},
        {"name": "Premium", "price": 90000, "variable_cost": 48000, "mix": 0.3},
    ],
    "cash_fixed_costs": 180000000,
    "depreciation": {"capex": 300000000, "useful_life_years": 5, "salvage": 0},
    "target_profit": {"after_tax": 40000000, "tax_rate": 0.20},
    "expected_units": 12000,
}


def read_products(raw):
    products = []
    for i, item in enumerate(raw):
        price = to_number(require(item, "price", f"products[{i}]"), "price")
        variable = to_number(require(item, "variable_cost", f"products[{i}]"), "variable_cost")
        if price <= variable:
            raise InputError(f"products[{i}]: price must exceed variable cost (no break-even)")
        mix = to_number(item.get("mix", 1.0 if len(raw) == 1 else None), "mix")
        products.append({"name": item.get("name", f"product {i + 1}"), "price": price,
                         "variable": variable, "mix": mix})
    total_mix = sum(p["mix"] for p in products)
    if abs(total_mix - 1) > MIX_TOLERANCE:
        raise InputError(f"unit mix must sum to 1, got {total_mix}")
    return products


def depreciation_amount(dep):
    if dep is None:
        return 0.0
    if isinstance(dep, (int, float)):
        return to_number(dep, "depreciation")
    capex = to_number(require(dep, "capex", "depreciation"), "capex")
    life = to_number(require(dep, "useful_life_years", "depreciation"), "useful_life_years")
    if life <= 0:
        raise InputError("useful_life_years must be positive")
    return (capex - to_number(dep.get("salvage", 0), "salvage")) / life


def main():
    args = build_parser(__doc__, EXAMPLE).parse_args()
    data = load_input(args)
    products = read_products(require(data, "products"))
    cash_fixed = to_number(require(data, "cash_fixed_costs"), "cash_fixed_costs")
    depreciation = depreciation_amount(data.get("depreciation"))
    fixed = cash_fixed + depreciation

    wcm = sum(p["mix"] * (p["price"] - p["variable"]) for p in products)
    wprice = sum(p["mix"] * p["price"] for p in products)
    cm_ratio = wcm / wprice
    q_acc, q_cash = fixed / wcm, cash_fixed / wcm
    unit = data.get("unit", "unit not stated")

    print(f"# Break-even analysis ({unit})\n")
    section("Products", md_table(
        ["product", "price", "variable cost", "unit CM", "CM ratio", "unit mix"],
        [[p["name"], p["price"], p["variable"], p["price"] - p["variable"],
          pct((p["price"] - p["variable"]) / p["price"]), pct(p["mix"])] for p in products]))
    rows = [["cash fixed costs", cash_fixed], ["depreciation", depreciation],
            ["total fixed costs", fixed], ["weighted CM per unit", wcm],
            ["weighted CM ratio", pct(cm_ratio)],
            ["accounting break-even units", q_acc], ["accounting break-even sales", q_acc * wprice],
            ["cash break-even units", q_cash], ["cash break-even sales", q_cash * wprice]]
    result = {"wcm": wcm, "cm_ratio": cm_ratio, "bep_units": q_acc, "bep_sales": q_acc * wprice,
              "cash_bep_units": q_cash}

    target = data.get("target_profit")
    if target:
        if "after_tax" in target:
            tax = to_number(require(target, "tax_rate", "target_profit"), "tax_rate")
            if not 0 <= tax < 1:
                raise InputError("tax_rate must be in [0, 1)")
            pre_tax = to_number(target["after_tax"], "after_tax") / (1 - tax)
        else:
            pre_tax = to_number(require(target, "pre_tax", "target_profit"), "pre_tax")
        q_target = (fixed + pre_tax) / wcm
        rows += [["pre-tax target profit", pre_tax], ["target units", q_target],
                 ["target sales", q_target * wprice]]
        result["target_units"] = q_target

    if data.get("expected_units") is not None:
        q = to_number(data["expected_units"], "expected_units")
        contribution = q * wcm
        operating_income = contribution - fixed
        rows += [["expected units", q], ["expected operating income", operating_income],
                 ["margin of safety", pct((q - q_acc) / q) if q else "n/a"],
                 ["degree of operating leverage",
                  contribution / operating_income if operating_income > 0 else "n/a (loss)"]]
        result["operating_income"] = operating_income
    section("Break-even results", md_table(["measure", "value"], rows))
    section("Break-even units by product (accounting basis)", md_table(
        ["product", "units", "sales"],
        [[p["name"], q_acc * p["mix"], q_acc * p["mix"] * p["price"]] for p in products]))
    write_json(args.json, result)


if __name__ == "__main__":
    run(main)
