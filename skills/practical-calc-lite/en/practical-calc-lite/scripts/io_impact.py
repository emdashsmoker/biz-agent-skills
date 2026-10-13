"""Economic ripple effects from input-output (IO) inducement coefficients.

For each sector i with final-demand spending b_i:
  production induced      = sum(b_i * p_i)       (p = production inducement coefficient)
  value added induced     = sum(b_i * v_i)       (v = value-added inducement coefficient)
  employment induced      = sum(b_i * unit_krw / labor_basis_krw * e_i)
The labor coefficients are persons per labor_basis_krw of final demand
(Bank of Korea tables: persons per KRW 1 billion).
"""

from _common import (InputError, build_parser, load_input, md_table, require,
                     run, section, to_number, write_json)

AMOUNT_UNIT_KRW_DEFAULT = 1e8    # amounts entered in KRW 100 million (eok)
LABOR_BASIS_KRW_DEFAULT = 1e9    # labor coefficients per KRW 1 billion
COEFFICIENT_KEYS = ("production", "value_added", "employment_total", "employment_wage")

EXAMPLE = {
    "unit": "KRW 100 million",
    "amount_unit_krw": AMOUNT_UNIT_KRW_DEFAULT,
    "labor_basis_krw": LABOR_BASIS_KRW_DEFAULT,
    "coefficient_source": "Bank of Korea IO table (year, domestic-goods basis) - state it",
    "total_budget": 300,
    "excluded": [
        {"item": "Land purchase", "amount": 40, "reason": "transfer of an existing asset"},
        {"item": "VAT", "amount": 20, "reason": "tax transfer"},
    ],
    "allocations": [
        {"sector": "Non-residential building construction", "amount": 180},
        {"sector": "Special-purpose machinery", "amount": 60},
    ],
    "coefficients": {
        "Non-residential building construction": {
            "production": 2.0, "value_added": 0.8,
            "employment_total": 10.0, "employment_wage": 8.0},
        "Special-purpose machinery": {
            "production": 1.9, "value_added": 0.7,
            "employment_total": 6.0, "employment_wage": 5.0},
    },
}


def main():
    args = build_parser(__doc__, EXAMPLE).parse_args()
    data = load_input(args)
    unit_krw = to_number(data.get("amount_unit_krw", AMOUNT_UNIT_KRW_DEFAULT), "amount_unit_krw")
    labor_basis = to_number(data.get("labor_basis_krw", LABOR_BASIS_KRW_DEFAULT), "labor_basis_krw")
    labor_scale = unit_krw / labor_basis
    coefficients = require(data, "coefficients")
    allocations = require(data, "allocations")

    rows, totals = [], dict.fromkeys(("amount",) + COEFFICIENT_KEYS, 0.0)
    present = set()
    for i, alloc in enumerate(allocations):
        sector = require(alloc, "sector", f"allocations[{i}]")
        amount = to_number(require(alloc, "amount", f"allocations[{i}]"), "amount")
        if sector not in coefficients:
            raise InputError(f"no coefficients for sector '{sector}'")
        coef = coefficients[sector]
        row = [sector, amount]
        totals["amount"] += amount
        for key in COEFFICIENT_KEYS:
            if key not in coef or coef[key] is None:
                row.append(None)
                continue
            present.add(key)
            value = to_number(coef[key], f"{sector}.{key}")
            effect = amount * value * (labor_scale if key.startswith("employment") else 1.0)
            totals[key] += effect
            row.append(effect)
        rows.append(row)

    unit = data.get("unit", "unit not stated")
    headers = ["sector", f"spend ({unit})", f"production induced ({unit})",
               f"value added induced ({unit})", "employment, all workers (persons)",
               "employment, wage workers (persons)"]
    total_row = ["Total", totals["amount"]] + [totals[k] if k in present else None
                                                for k in COEFFICIENT_KEYS]
    print("# Economic ripple effect report\n")
    print(f"Coefficient source: {data.get('coefficient_source', 'NOT STATED - ask the user')}\n")
    section("Coefficients used", md_table(
        ["sector"] + list(COEFFICIENT_KEYS),
        [[s] + [coefficients[s].get(k) for k in COEFFICIENT_KEYS] for s in coefficients],
        decimals=4))
    section("Induced effects", md_table(headers, rows + [total_row]))
    print(f"Labor conversion: persons = spend x {unit_krw:,.0f} / {labor_basis:,.0f} x coefficient "
          f"(scale {labor_scale:g}).")
    print("Production induced already contains the initial spending; do not add production "
          "and value added together.\n")

    excluded = data.get("excluded", [])
    if "total_budget" in data:
        budget = to_number(data["total_budget"], "total_budget")
        excluded_sum = sum(to_number(e.get("amount", 0), "excluded.amount") for e in excluded)
        gap = budget - excluded_sum - totals["amount"]
        section("Budget reconciliation", md_table(
            ["total budget", "excluded", "allocated", "unexplained gap"],
            [[budget, excluded_sum, totals["amount"], gap]]))
        if abs(gap) > 1e-9:
            print("WARNING: allocations plus exclusions do not match the total budget.\n")
    if excluded:
        section("Excluded items", md_table(["item", "amount", "reason"],
                                           [[e.get("item"), e.get("amount"), e.get("reason")]
                                            for e in excluded]))
    write_json(args.json, {"totals": totals, "labor_scale": labor_scale})


if __name__ == "__main__":
    run(main)
