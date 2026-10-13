"""Cost-benefit analysis: PV, NPV, B/C, IRR, payback, sensitivity, switching values.

Discounting: PV_t = X_t * DF_t, DF_t = product over years y in (base_year, t] of 1/(1+r_y).
With one rate this is X_t / (1+r)^(t - base_year). The base date is the end of base_year.
Benefit streams start in project_end_year + gestation_years + 1 and last benefit_years.
"""

from collections import defaultdict

from _common import (InputError, build_parser, load_input, md_table, pct, register_sheet,
                     require, run, section, to_number, write_json)

VAT_RATE_DEFAULT = 0.10          # Korean VAT rate; override with "vat_rate"
IRR_SEARCH_LOW = -0.99           # IRR search range (per year)
IRR_SEARCH_HIGH = 10.0
IRR_GRID_STEPS = 4000
IRR_TOLERANCE = 1e-10
SENSITIVITY_DEFAULT = {"discount_rate_pp": [-0.01, 0.01],
                       "cost_change": [-0.10, 0.10],
                       "benefit_change": [-0.10, 0.10]}

EXAMPLE = {
    "unit": "KRW 100 million, base-year constant prices",
    "base_year": 2025,
    "discount_rate": 0.045,
    "costs": [
        {"year": 2026, "item": "R&D", "amount": 120},
        {"year": 2027, "item": "R&D", "amount": 150},
        {"year": 2028, "item": "Facility", "amount": 55, "vat_included": True},
    ],
    "recurring_costs": [
        {"item": "Post-project O&M", "amount": 4, "from_year": 2032, "to_year": 2041}
    ],
    "benefit_streams": [
        {"item": "Technology A", "project_end_year": 2028, "gestation_years": 3,
         "benefit_years": 10,
         "market_size": [2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700],
         "factors": {"project_contribution": 0.30, "rnd_contribution": 0.35,
                     "commercialization_rate": 0.45, "value_added_ratio": 0.40}}
    ],
    "benefits": [],
    "residual_values": [{"year": 2041, "item": "Equipment", "amount": 5}],
    "sensitivity": SENSITIVITY_DEFAULT,
}


def rate_for_year(year, schedule):
    """Return the discount rate for a year from [{'to_year': Y, 'rate': r}, {'rate': r2}]."""
    for step in schedule:
        if "to_year" not in step or year <= int(step["to_year"]):
            return step["rate"]
    return schedule[-1]["rate"]


def discount_factor(year, base_year, schedule):
    """Compound yearly rates between the base date and the flow year."""
    factor = 1.0
    if year > base_year:
        for y in range(base_year + 1, year + 1):
            factor /= 1 + rate_for_year(y, schedule)
    elif year < base_year:
        for y in range(year + 1, base_year + 1):
            factor *= 1 + rate_for_year(y, schedule)
    return factor


def build_schedule(data):
    """Return {'rate': [...]} schedule from discount_rate or rate_schedule."""
    if "rate_schedule" in data and data["rate_schedule"]:
        steps = []
        for i, step in enumerate(data["rate_schedule"]):
            entry = {"rate": to_number(require(step, "rate", f"rate_schedule[{i}]"), "rate")}
            if "to_year" in step:
                entry["to_year"] = int(step["to_year"])
            steps.append(entry)
        return steps
    return [{"rate": to_number(require(data, "discount_rate"), "discount_rate")}]


def stream_amounts(stream, i):
    """Yearly amounts for one benefit stream (explicit list, constant, or market x factors)."""
    years = int(require(stream, "benefit_years", f"benefit_streams[{i}]"))
    if "market_size" in stream:
        market = [to_number(v, "market_size") for v in stream["market_size"]]
        factors = require(stream, "factors", f"benefit_streams[{i}]")
        multiplier = 1.0
        for key in ("project_contribution", "rnd_contribution",
                    "commercialization_rate", "value_added_ratio"):
            multiplier *= to_number(require(factors, key, "factors"), key)
        amounts = [m * multiplier for m in market]
    elif "amounts" in stream:
        amounts = [to_number(v, "amounts") for v in stream["amounts"]]
    else:
        base = to_number(require(stream, "amount", f"benefit_streams[{i}]"), "amount")
        growth = to_number(stream.get("growth_rate", 0), "growth_rate")
        amounts = [base * (1 + growth) ** k for k in range(years)]
    if len(amounts) != years:
        raise InputError(f"benefit_streams[{i}] has {len(amounts)} amounts "
                         f"but benefit_years = {years}")
    return amounts


def collect_flows(data):
    """Aggregate every cost and benefit into {year: amount} and keep an item log."""
    vat_rate = to_number(data.get("vat_rate", VAT_RATE_DEFAULT), "vat_rate")
    costs, benefits, log = defaultdict(float), defaultdict(float), []

    for i, row in enumerate(data.get("costs", [])):
        year = int(require(row, "year", f"costs[{i}]"))
        amount = to_number(require(row, "amount", f"costs[{i}]"), "amount")
        if row.get("vat_included"):
            amount /= 1 + vat_rate
        costs[year] += amount
        log.append(("cost", row.get("item", ""), year, year, amount))

    for i, row in enumerate(data.get("recurring_costs", [])):
        start = int(require(row, "from_year", f"recurring_costs[{i}]"))
        end = int(require(row, "to_year", f"recurring_costs[{i}]"))
        amount = to_number(require(row, "amount", f"recurring_costs[{i}]"), "amount")
        for year in range(start, end + 1):
            costs[year] += amount
        log.append(("cost (recurring)", row.get("item", ""), start, end, amount))

    for i, row in enumerate(data.get("residual_values", [])):
        year = int(require(row, "year", f"residual_values[{i}]"))
        amount = to_number(require(row, "amount", f"residual_values[{i}]"), "amount")
        costs[year] -= amount
        log.append(("residual value (cost deduction)", row.get("item", ""), year, year, -amount))

    for i, row in enumerate(data.get("benefits", [])):
        year = int(require(row, "year", f"benefits[{i}]"))
        amount = to_number(require(row, "amount", f"benefits[{i}]"), "amount")
        benefits[year] += amount
        log.append(("benefit", row.get("item", ""), year, year, amount))

    for i, stream in enumerate(data.get("benefit_streams", [])):
        end = int(require(stream, "project_end_year", f"benefit_streams[{i}]"))
        gestation = int(require(stream, "gestation_years", f"benefit_streams[{i}]"))
        first = end + gestation + 1
        amounts = stream_amounts(stream, i)
        for k, amount in enumerate(amounts):
            benefits[first + k] += amount
        log.append(("benefit stream", stream.get("item", ""), first,
                    first + len(amounts) - 1, sum(amounts)))

    if not costs:
        raise InputError("no costs given")
    if not benefits:
        raise InputError("no benefits given")
    return costs, benefits, log


def evaluate(costs, benefits, base_year, schedule, cost_scale=1.0, benefit_scale=1.0):
    """Return yearly table rows and summary indicators for one scenario."""
    years = range(min(costs.keys() | benefits.keys()), max(costs.keys() | benefits.keys()) + 1)
    rows, pv_cost, pv_benefit = [], 0.0, 0.0
    for year in years:
        cost = costs.get(year, 0.0) * cost_scale
        benefit = benefits.get(year, 0.0) * benefit_scale
        factor = discount_factor(year, base_year, schedule)
        pv_cost += cost * factor
        pv_benefit += benefit * factor
        rows.append([year, cost, cost * factor, benefit, benefit * factor,
                     benefit - cost, (benefit - cost) * factor])
    npv = pv_benefit - pv_cost
    bc = pv_benefit / pv_cost if pv_cost > 0 else None
    return rows, {"pv_cost": pv_cost, "pv_benefit": pv_benefit, "npv": npv, "bc_ratio": bc}


def npv_at(rate, net_by_year, base_year):
    return sum(v / (1 + rate) ** (y - base_year) for y, v in net_by_year)


def find_irrs(net_by_year, base_year):
    """Scan the rate grid for sign changes and refine each root by bisection."""
    step = (IRR_SEARCH_HIGH - IRR_SEARCH_LOW) / IRR_GRID_STEPS
    grid = [IRR_SEARCH_LOW + k * step for k in range(IRR_GRID_STEPS + 1)]
    roots, prev_rate, prev_val = [], grid[0], npv_at(grid[0], net_by_year, base_year)
    for rate in grid[1:]:
        val = npv_at(rate, net_by_year, base_year)
        if prev_val == 0:
            roots.append(prev_rate)
        elif prev_val * val < 0:
            lo, hi = prev_rate, rate
            while hi - lo > IRR_TOLERANCE:
                mid = (lo + hi) / 2
                if npv_at(lo, net_by_year, base_year) * npv_at(mid, net_by_year, base_year) <= 0:
                    hi = mid
                else:
                    lo = mid
            roots.append((lo + hi) / 2)
        prev_rate, prev_val = rate, val
    return roots


def sign_changes(values):
    signs = [v > 0 for v in values if v != 0]
    return sum(1 for a, b in zip(signs, signs[1:]) if a != b)


def payback(rows, column):
    """Years from the first flow year until the cumulative net turns non-negative."""
    start, cumulative = rows[0][0], 0.0
    for index, row in enumerate(rows):
        previous = cumulative
        cumulative += row[column]
        if index == 0 and cumulative >= 0:
            return row[0], 0.0
        if cumulative >= 0 > previous:
            fraction = -previous / row[column] if row[column] else 0.0
            return row[0], (row[0] - start) + fraction
    return None, None


def write_formula_sheet(workbook, costs, benefits, base_year, schedule, unit):
    """Cash-flow sheet whose discount factors, PVs, B/C, NPV and IRR are Excel formulas.

    Rows run over every year from min(first flow year, base_year + 1) to the last flow year.
    Discount factors chain from the base date: DF(base+1) = 1/(1+r), DF(t) = DF(t-1)/(1+r_t),
    and backwards for years up to the base year: DF(t) = DF(t+1) * (1+r_(t+1)).
    Editing the rate column recalculates every result.
    """
    from openpyxl.styles import Font

    sheet = workbook.create_sheet("CF formulas", 0)
    first = min(min(costs), min(benefits), base_year + 1)
    last = max(max(costs), max(benefits), base_year + 1)
    years = list(range(first, last + 1))
    head_row, top = 3, 4
    sheet["A1"] = f"Cash flow with live formulas ({unit}). Base date: end of {base_year}."
    sheet["A1"].font = Font(bold=True)
    sheet["A2"] = ("DF(base+1) = 1/(1+r); DF(t) = DF(t-1)/(1+r_t). Edit column D to test "
                   "other discount rates.")
    headers = ["year", "cost", "benefit", "discount rate", "discount factor", "cost PV",
               "benefit PV", "net flow", "net PV"]
    for col, text in enumerate(headers, 1):
        sheet.cell(head_row, col, text).font = Font(bold=True)
    anchor = top + years.index(base_year + 1)
    for i, year in enumerate(years):
        r = top + i
        sheet.cell(r, 1, year)
        sheet.cell(r, 2, costs.get(year, 0.0))
        sheet.cell(r, 3, benefits.get(year, 0.0))
        sheet.cell(r, 4, rate_for_year(year, schedule)).number_format = "0.00%"
        if r == anchor:
            sheet.cell(r, 5, f"=1/(1+D{r})")
        elif r > anchor:
            sheet.cell(r, 5, f"=E{r - 1}/(1+D{r})")
        sheet.cell(r, 6, f"=B{r}*E{r}")
        sheet.cell(r, 7, f"=C{r}*E{r}")
        sheet.cell(r, 8, f"=C{r}-B{r}")
        sheet.cell(r, 9, f"=H{r}*E{r}")
    for r in range(anchor - 1, top - 1, -1):          # years at or before the base year
        sheet.cell(r, 5, f"=E{r + 1}*(1+D{r + 1})")
    bottom = top + len(years) - 1
    total = bottom + 1
    sheet.cell(total, 1, "Total").font = Font(bold=True)
    for col in "BCFGHI":
        sheet[f"{col}{total}"] = f"=SUM({col}{top}:{col}{bottom})"
    summary = [("PV cost", f"=F{total}", "#,##0.00"), ("PV benefit", f"=G{total}", "#,##0.00"),
               ("NPV", f"=G{total}-F{total}", "#,##0.00"), ("B/C", f"=G{total}/F{total}", "0.0000"),
               ("IRR", f"=IRR(H{top}:H{bottom})", "0.00%")]
    for i, (label, formula, number_format) in enumerate(summary):
        r = total + 2 + i
        sheet.cell(r, 1, label).font = Font(bold=True)
        sheet.cell(r, 2, formula).number_format = number_format
    sheet.cell(total + 2 + len(summary), 1,
               "IRR shows one root only; when net flows change sign more than once, "
               "use NPV and B/C (see the script report).")
    for r in range(top, total + 1):
        for col in (2, 3, 6, 7, 8, 9):
            sheet.cell(r, col).number_format = "#,##0.00"
        sheet.cell(r, 5).number_format = "0.000000"
    sheet.freeze_panes = f"A{top}"
    for col, width in zip("ABCDEFGHI", (12, 14, 14, 13, 15, 14, 14, 14, 14)):
        sheet.column_dimensions[col].width = width


def main():
    args = build_parser(__doc__, EXAMPLE).parse_args()
    data = load_input(args)
    base_year = int(require(data, "base_year"))
    schedule = build_schedule(data)
    costs, benefits, log = collect_flows(data)
    rows, summary = evaluate(costs, benefits, base_year, schedule)
    register_sheet(lambda wb: write_formula_sheet(wb, costs, benefits, base_year, schedule,
                                                  data.get("unit", "unit not stated")))
    net = [(r[0], r[5]) for r in rows]
    irrs = find_irrs(net, base_year)
    changes = sign_changes([v for _, v in net])
    reference_rate = schedule[0]["rate"]

    print(f"# Cost-benefit report ({data.get('unit', 'unit not stated')})\n")
    steps = [f"{pct(st['rate'])}" + (f" through {st['to_year']}" if "to_year" in st else "")
             for st in schedule]
    print(f"Base date: end of {base_year}. Discount rate: {', then '.join(steps)}\n")
    section("Input items", md_table(["type", "item", "from", "to", "amount (total)"],
                                    [[t, n, str(a), str(b), v] for t, n, a, b, v in log]))
    table = [[str(r[0])] + r[1:] for r in rows]
    totals = ["Total"] + [sum(r[k] for r in rows) for k in range(1, 7)]
    section("Yearly table", md_table(
        ["year", "cost", "cost PV", "benefit", "benefit PV", "net", "net PV"], table + [totals]))

    bc = summary["bc_ratio"]
    irr_text = ", ".join(pct(r) for r in irrs) if irrs else "not found in search range"
    decision = [
        ["B/C", f"{bc:.4f}" if bc is not None else "n/a", ">= 1.0", bool(bc is not None and bc >= 1)],
        ["NPV", summary["npv"], ">= 0", summary["npv"] >= 0],
        ["IRR", irr_text, f"> {pct(reference_rate)}",
         bool(len(irrs) == 1 and irrs[0] > reference_rate)],
    ]
    section("Indicators", md_table(["indicator", "value", "criterion", "meets"], decision))
    print(f"PV cost {summary['pv_cost']:,.2f} | PV benefit {summary['pv_benefit']:,.2f} | "
          f"net-flow sign changes {changes}")
    if len(irrs) != 1:
        print("IRR is not unique or absent: rely on NPV and B/C for the decision.")
    print()

    pay_year, pay_years = payback(rows, 5)
    dpay_year, dpay_years = payback(rows, 6)
    section("Payback (from first flow year, interpolated within the year)", md_table(
        ["measure", "turning year", "years"],
        [["simple", str(pay_year) if pay_year else "not reached", pay_years],
         ["discounted", str(dpay_year) if dpay_year else "not reached", dpay_years]]))

    sens = {**SENSITIVITY_DEFAULT, **(data.get("sensitivity") or {})}
    scenario_rows = []
    for pp in sens["discount_rate_pp"]:
        shifted = [{**s, "rate": s["rate"] + pp} for s in schedule]
        _, s = evaluate(costs, benefits, base_year, shifted)
        scenario_rows.append([f"discount rate {pp * 100:+.1f}%p", s["pv_cost"], s["pv_benefit"],
                              s["npv"], s["bc_ratio"]])
    for change in sens["cost_change"]:
        _, s = evaluate(costs, benefits, base_year, schedule, cost_scale=1 + change)
        scenario_rows.append([f"cost {change * 100:+.0f}%", s["pv_cost"], s["pv_benefit"],
                              s["npv"], s["bc_ratio"]])
    for change in sens["benefit_change"]:
        _, s = evaluate(costs, benefits, base_year, schedule, benefit_scale=1 + change)
        scenario_rows.append([f"benefit {change * 100:+.0f}%", s["pv_cost"], s["pv_benefit"],
                              s["npv"], s["bc_ratio"]])
    section("Sensitivity", md_table(["scenario", "PV cost", "PV benefit", "NPV", "B/C"],
                                    scenario_rows, decimals=4))
    if bc:
        print(f"Switching values: B/C reaches 1.0 with a benefit change of {pct(1 / bc - 1)} "
              f"or a cost change of {pct(bc - 1)} (signed, other side unchanged).\n")

    write_json(args.json, {"summary": summary, "irr": irrs, "payback_years": pay_years,
                           "discounted_payback_years": dpay_years,
                           "yearly": [dict(zip(["year", "cost", "cost_pv", "benefit",
                                                "benefit_pv", "net", "net_pv"], r)) for r in rows]})


if __name__ == "__main__":
    run(main)
