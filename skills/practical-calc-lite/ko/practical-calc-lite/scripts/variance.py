"""Budget (or prior period) versus actual variance analysis with price, mix, volume effects.

For items with quantity (Q) and unit price or unit cost (P); B = budget, A = actual:
  total  = sum(AQ*AP) - sum(BQ*BP)
  price  = sum((AP - BP) * AQ)
  mix    = sum((AQ_i - sum(AQ) * BM_i) * BP_i)      BM_i = BQ_i / sum(BQ)
  volume = (sum(AQ) - sum(BQ)) * sum(BQ*BP) / sum(BQ)
  price + mix + volume = total                      (checked in code)
With separate_mix = false (items measured in different units) the volume effect is
sum((AQ_i - BQ_i) * BP_i) and mix is zero.
Sign: revenue items are favorable when actual > budget; cost items when actual < budget.
"""

from _common import (InputError, build_parser, load_input, md_table, pct,
                     require, run, section, to_number, write_json)

MATERIALITY_PCT_DEFAULT = 0.10
CHECK_TOLERANCE = 1e-6

EXAMPLE = {
    "unit": "KRW million",
    "comparison": "Actual vs budget, FY2025",
    "kind": "revenue",
    "separate_mix": True,
    "items": [
        {"name": "Product A", "budget_qty": 10000, "budget_price": 0.050,
         "actual_qty": 11000, "actual_price": 0.048},
        {"name": "Product B", "budget_qty": 4000, "budget_price": 0.120,
         "actual_qty": 3500, "actual_price": 0.125},
    ],
    "materiality": {"pct": 0.10, "amount": 20},
}


def direction(value, kind):
    if value == 0:
        return "none"
    good = value > 0 if kind == "revenue" else value < 0
    return "favorable" if good else "unfavorable"


def decompose(items, separate_mix):
    bq_sum = sum(i["bq"] for i in items)
    aq_sum = sum(i["aq"] for i in items)
    budget_total = sum(i["bq"] * i["bp"] for i in items)
    if bq_sum <= 0:
        raise InputError("budget quantities must sum to a positive number")
    rows = []
    for i in items:
        price = (i["ap"] - i["bp"]) * i["aq"]
        if separate_mix:
            mix_share = i["bq"] / bq_sum
            mix = (i["aq"] - aq_sum * mix_share) * i["bp"]
            volume = (aq_sum * mix_share - i["bq"]) * i["bp"]
        else:
            mix, volume = 0.0, (i["aq"] - i["bq"]) * i["bp"]
        total = i["aq"] * i["ap"] - i["bq"] * i["bp"]
        if abs(price + mix + volume - total) > CHECK_TOLERANCE * max(1.0, abs(total)):
            raise InputError(f"decomposition does not reconcile for {i['name']}")
        rows.append({"name": i["name"], "budget": i["bq"] * i["bp"], "actual": i["aq"] * i["ap"],
                     "price": price, "mix": mix, "volume": volume, "total": total})
    return rows, budget_total


def main():
    args = build_parser(__doc__, EXAMPLE).parse_args()
    data = load_input(args)
    kind = data.get("kind", "revenue")
    if kind not in ("revenue", "cost"):
        raise InputError("kind must be 'revenue' or 'cost'")
    materiality = data.get("materiality") or {}
    pct_limit = to_number(materiality.get("pct", MATERIALITY_PCT_DEFAULT), "materiality.pct")
    amount_limit = materiality.get("amount")
    amount_limit = None if amount_limit is None else to_number(amount_limit, "materiality.amount")

    raw = require(data, "items")
    has_qty = all("budget_qty" in r for r in raw)
    items = []
    for n, r in enumerate(raw):
        where = f"items[{n}]"
        if has_qty:
            items.append({"name": r.get("name", where),
                          "bq": to_number(require(r, "budget_qty", where), "budget_qty"),
                          "bp": to_number(require(r, "budget_price", where), "budget_price"),
                          "aq": to_number(require(r, "actual_qty", where), "actual_qty"),
                          "ap": to_number(require(r, "actual_price", where), "actual_price")})
        else:
            budget = to_number(require(r, "budget", where), "budget")
            actual = to_number(require(r, "actual", where), "actual")
            items.append({"name": r.get("name", where), "budget": budget, "actual": actual,
                          "total": actual - budget, "price": None, "mix": None, "volume": None})

    unit = data.get("unit", "unit not stated")
    print(f"# Variance analysis ({data.get('comparison', 'comparison not stated')}, {unit}, {kind})\n")
    if has_qty:
        separate_mix = bool(data.get("separate_mix", len(items) > 1))
        rows, _ = decompose(items, separate_mix)
    else:
        rows = items

    table, flags = [], []
    for r in rows:
        rate = r["total"] / abs(r["budget"]) if r["budget"] else None
        flag = rate is not None and abs(rate) >= pct_limit and \
            (amount_limit is None or abs(r["total"]) >= amount_limit)
        flags.append(flag)
        table.append([r["name"], r["budget"], r["actual"], r["price"], r["mix"], r["volume"],
                      r["total"], pct(rate) if rate is not None else "n/a",
                      direction(r["total"], kind), flag])
    totals = {k: sum(r[k] for r in rows) if rows[0][k] is not None else None
              for k in ("budget", "actual", "price", "mix", "volume", "total")}
    table.append(["Total", totals["budget"], totals["actual"], totals["price"], totals["mix"],
                  totals["volume"], totals["total"],
                  pct(totals["total"] / abs(totals["budget"])) if totals["budget"] else "n/a",
                  direction(totals["total"], kind), ""])
    rule = f"|variance| >= {pct(pct_limit)}" + (
        f" and |amount| >= {amount_limit:,.2f}" if amount_limit is not None else "")
    if "pct" not in materiality:
        rule += " (screening default, not a materiality judgement)"
    section(f"Variance by item (flag rule: {rule})", md_table(
        ["item", "budget", "actual", "price effect", "mix effect", "volume effect",
         "total variance", "variance %", "direction", "flag"], table, decimals=4))

    bridge = [["Budget total", totals["budget"], totals["budget"]]]
    running = totals["budget"]
    drivers = [("price", totals["price"]), ("mix", totals["mix"]), ("volume", totals["volume"])] \
        if has_qty else [(r["name"], r["total"]) for r in rows]
    for label, value in drivers:
        if value is None:
            continue
        running += value
        bridge.append([f"{'+' if value >= 0 else '-'} {label}", value, running])
    bridge.append(["Actual total", totals["actual"], totals["actual"]])
    if abs(running - totals["actual"]) > CHECK_TOLERANCE * max(1.0, abs(totals["actual"])):
        raise InputError("bridge does not reconcile to the actual total")
    section("Bridge (budget to actual)", md_table(["step", "amount", "running total"], bridge,
                                                  decimals=4))
    write_json(args.json, {"items": rows, "totals": totals, "flags": flags})


if __name__ == "__main__":
    run(main)
