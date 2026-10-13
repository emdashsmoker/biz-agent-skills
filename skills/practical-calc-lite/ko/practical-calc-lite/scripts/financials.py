"""Financial statement analysis: integrity checks, EBITDA, CAPEX, OPEX, FCF, ratios, changes.

Definitions (each output row names the inputs it used):
  EBITDA          = operating income + depreciation + amortization
  CAPEX           = purchases of PP&E + purchases of intangibles   (cash flow statement)
  net CAPEX       = CAPEX - proceeds from disposals
  OPEX (SG&A)     = selling, general and administrative expenses
  operating costs = cost of sales + SG&A
  FCF             = operating cash flow - CAPEX
Return and turnover ratios use the average of opening and closing balances when the
previous period is supplied, otherwise closing balances (the basis column says which).
"""

from _common import (InputError, build_parser, load_input, md_table, pct,
                     require, run, section, to_number, write_json)

MATERIALITY_PCT_DEFAULT = 0.10     # screening default when the user gives no threshold
BALANCE_TOLERANCE = 0.005          # relative tolerance for assets = liabilities + equity
INCOME_KEYS = ["revenue", "cogs", "sga", "operating_income", "depreciation", "amortization",
               "interest_expense", "pretax_income", "income_tax", "net_income"]
BALANCE_KEYS = ["total_assets", "current_assets", "receivables", "inventory", "cash",
                "total_liabilities", "current_liabilities", "borrowings", "equity"]
CASH_KEYS = ["cfo", "cfi", "cff", "fx_effect", "cash_begin", "cash_end",
             "capex_ppe", "capex_intangible", "disposal_proceeds"]

EXAMPLE = {
    "unit": "KRW million",
    "statement_basis": "K-IFRS consolidated (state which)",
    "periods": {
        "2024": {"revenue": 52000, "cogs": 36400, "sga": 9800, "operating_income": 5800,
                 "depreciation": 2100, "amortization": 300, "interest_expense": 700,
                 "pretax_income": 5300, "income_tax": 1100, "net_income": 4200,
                 "total_assets": 61000, "current_assets": 24000, "receivables": 8200,
                 "inventory": 6100, "cash": 5200, "total_liabilities": 33000,
                 "current_liabilities": 15000, "borrowings": 18000, "equity": 28000,
                 "cfo": 7400, "cfi": -4600, "cff": -1500, "fx_effect": 0,
                 "cash_begin": 3900, "cash_end": 5200,
                 "capex_ppe": 4200, "capex_intangible": 500, "disposal_proceeds": 200},
        "2025": {"revenue": 58500, "cogs": 41200, "sga": 10500, "operating_income": 6800,
                 "depreciation": 2300, "amortization": 350, "interest_expense": 760,
                 "pretax_income": 6150, "income_tax": 1300, "net_income": 4850,
                 "total_assets": 66500, "current_assets": 26500, "receivables": 9400,
                 "inventory": 6900, "cash": 5600, "total_liabilities": 34500,
                 "current_liabilities": 16200, "borrowings": 18500, "equity": 32000,
                 "cfo": 8300, "cfi": -5900, "cff": -2000, "fx_effect": 0,
                 "cash_begin": 5200, "cash_end": 5600,
                 "capex_ppe": 5400, "capex_intangible": 600, "disposal_proceeds": 100},
    },
    "materiality": {"pct": 0.10, "amount": 500},
}


def get(period, key):
    value = period.get(key)
    return None if value is None else to_number(value, key)


def ratio(num, den, scale=1.0):
    if num is None or den in (None, 0):
        return None
    return num / den * scale


def average(current, previous, key):
    """Average balance when the previous period exists, else the closing balance."""
    now = get(current, key)
    before = get(previous, key) if previous else None
    if now is None:
        return None, "-"
    if before is None:
        return now, "closing"
    return (now + before) / 2, "average"


def derived(p):
    """Compute derived amounts for one period."""
    g = lambda k: get(p, k)  # noqa: E731
    d = {}
    if g("revenue") is not None and g("cogs") is not None:
        d["gross_profit"] = g("revenue") - g("cogs")
    if g("operating_income") is not None:
        dep, amo = g("depreciation"), g("amortization")
        if dep is not None or amo is not None:
            d["ebitda"] = g("operating_income") + (dep or 0) + (amo or 0)
    if g("capex_ppe") is not None or g("capex_intangible") is not None:
        d["capex"] = (g("capex_ppe") or 0) + (g("capex_intangible") or 0)
        d["net_capex"] = d["capex"] - (g("disposal_proceeds") or 0)
    if g("sga") is not None:
        d["opex_sga"] = g("sga")
        if g("cogs") is not None:
            d["operating_costs"] = g("cogs") + g("sga")
    if g("cfo") is not None and "capex" in d:
        d["fcf"] = g("cfo") - d["capex"]
    return d


def checks(name, p):
    """Arithmetic integrity checks between statements of one period."""
    rows = []
    ta, tl, eq = get(p, "total_assets"), get(p, "total_liabilities"), get(p, "equity")
    if None not in (ta, tl, eq):
        gap = ta - (tl + eq)
        ok = abs(gap) <= BALANCE_TOLERANCE * abs(ta)
        rows.append([name, "assets = liabilities + equity", gap, ok])
    parts = [get(p, k) for k in ("cash_begin", "cfo", "cfi", "cff")]
    if None not in parts and get(p, "cash_end") is not None:
        gap = get(p, "cash_end") - (sum(parts) + (get(p, "fx_effect") or 0))
        rows.append([name, "cash end = begin + CFO + CFI + CFF + FX", gap, abs(gap) < 1e-6 or
                     abs(gap) <= BALANCE_TOLERANCE * abs(get(p, "cash_end") or 1)])
    rev, cogs, sga, oi = (get(p, k) for k in ("revenue", "cogs", "sga", "operating_income"))
    if None not in (rev, cogs, sga, oi):
        gap = oi - (rev - cogs - sga)
        rows.append([name, "operating income - (revenue - COGS - SG&A)", gap,
                     "other operating items" if abs(gap) > 1e-6 else True])
    return rows


def ratio_rows(current, previous, d):
    """Ratios for one period with their basis."""
    g = lambda k: get(current, k)  # noqa: E731
    avg_ta, b_ta = average(current, previous, "total_assets")
    avg_eq, b_eq = average(current, previous, "equity")
    avg_ar, b_ar = average(current, previous, "receivables")
    avg_inv, b_inv = average(current, previous, "inventory")
    inv_num, inv_label = (g("cogs"), "COGS") if g("cogs") is not None else (g("revenue"), "revenue")
    rows = [
        ["profitability", "gross margin %", ratio(d.get("gross_profit"), g("revenue"), 100), "period"],
        ["profitability", "operating margin %", ratio(g("operating_income"), g("revenue"), 100), "period"],
        ["profitability", "EBITDA margin %", ratio(d.get("ebitda"), g("revenue"), 100), "period"],
        ["profitability", "net margin %", ratio(g("net_income"), g("revenue"), 100), "period"],
        ["profitability", "ROA % (net income / assets)", ratio(g("net_income"), avg_ta, 100), b_ta],
        ["profitability", "ROE % (net income / equity)", ratio(g("net_income"), avg_eq, 100), b_eq],
        ["stability", "debt ratio % (liabilities / equity)",
         ratio(g("total_liabilities"), g("equity"), 100), "closing"],
        ["stability", "current ratio %", ratio(g("current_assets"), g("current_liabilities"), 100), "closing"],
        ["stability", "equity ratio % (equity / assets)", ratio(g("equity"), g("total_assets"), 100), "closing"],
        ["stability", "borrowings dependence % (borrowings / assets)",
         ratio(g("borrowings"), g("total_assets"), 100), "closing"],
        ["stability", "interest coverage % (operating income / interest)",
         ratio(g("operating_income"), g("interest_expense"), 100), "period"],
        ["activity", "total asset turnover (times)", ratio(g("revenue"), avg_ta), b_ta],
        ["activity", "receivables turnover (times)", ratio(g("revenue"), avg_ar), b_ar],
        ["activity", f"inventory turnover (times, {inv_label})", ratio(inv_num, avg_inv), b_inv],
    ]
    if previous:
        rows += [
            ["growth", "revenue growth %", ratio(g("revenue") - get(previous, "revenue"),
                                                 get(previous, "revenue"), 100)
             if None not in (g("revenue"), get(previous, "revenue")) else None, "vs previous"],
            ["growth", "total asset growth %", ratio(g("total_assets") - get(previous, "total_assets"),
                                                     get(previous, "total_assets"), 100)
             if None not in (g("total_assets"), get(previous, "total_assets")) else None, "vs previous"],
        ]
    return rows


def main():
    args = build_parser(__doc__, EXAMPLE).parse_args()
    data = load_input(args)
    periods = require(data, "periods")
    order = data.get("order") or sorted(periods)
    if any(p not in periods for p in order):
        raise InputError("'order' lists a period that is not in 'periods'")
    materiality = data.get("materiality") or {}
    pct_limit = to_number(materiality.get("pct", MATERIALITY_PCT_DEFAULT), "materiality.pct")
    amount_limit = materiality.get("amount")
    amount_limit = None if amount_limit is None else to_number(amount_limit, "materiality.amount")

    unit = data.get("unit", "unit not stated")
    print(f"# Financial statement analysis ({unit}, {data.get('statement_basis', 'basis not stated')})\n")
    derived_by = {name: derived(periods[name]) for name in order}
    keys = [k for k in INCOME_KEYS + BALANCE_KEYS + CASH_KEYS if any(k in periods[n] for n in order)]
    dkeys = ["gross_profit", "ebitda", "opex_sga", "operating_costs", "capex", "net_capex", "fcf"]
    dkeys = [k for k in dkeys if any(k in derived_by[n] for n in order)]
    section("Amounts", md_table(["item"] + order,
                                [[k] + [get(periods[n], k) for n in order] for k in keys]
                                + [[f"{k} (derived)"] + [derived_by[n].get(k) for n in order]
                                   for k in dkeys]))

    check_rows = [row for n in order for row in checks(n, periods[n])]
    if check_rows:
        section("Integrity checks", md_table(["period", "check", "gap", "pass"], check_rows))

    ratio_table = {}
    for i, name in enumerate(order):
        previous = periods[order[i - 1]] if i > 0 else None
        ratio_table[name] = ratio_rows(periods[name], previous, derived_by[name])
    labels = [(r[0], r[1]) for r in ratio_table[order[-1]]]
    rows = []
    for group, label in labels:
        values, bases = [], []
        for name in order:
            match = next((r for r in ratio_table[name] if r[1] == label), None)
            values.append(None if match is None else match[2])
            bases.append(None if match is None or match[2] is None else match[3])
        rows.append([group, label] + values + bases)
    section("Ratios", md_table(["group", "ratio"] + order + [f"basis {n}" for n in order], rows))

    if len(order) >= 2:
        prev, curr = order[-2], order[-1]
        change_rows = []
        for key in keys + dkeys:
            a = get(periods[prev], key) if key in keys else derived_by[prev].get(key)
            b = get(periods[curr], key) if key in keys else derived_by[curr].get(key)
            if a is None or b is None:
                continue
            delta = b - a
            rate = delta / abs(a) if a else None
            flag = rate is not None and abs(rate) >= pct_limit and \
                (amount_limit is None or abs(delta) >= amount_limit)
            change_rows.append([key, a, b, delta, pct(rate) if rate is not None else "n/a", flag])
        rule = f"|change| >= {pct(pct_limit)}" + (f" and |amount| >= {amount_limit:,.0f}"
                                                 if amount_limit is not None else "")
        if "pct" not in materiality:
            rule += " (screening default, not a materiality judgement)"
        section(f"Changes {prev} -> {curr} (flag rule: {rule})", md_table(
            ["item", prev, curr, "change", "change %", "flag"], change_rows))

    write_json(args.json, {"derived": derived_by,
                           "ratios": {n: [r[1:] for r in ratio_table[n]] for n in order}})


if __name__ == "__main__":
    run(main)
