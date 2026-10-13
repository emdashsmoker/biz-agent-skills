"""Project appraisal: B/C ratio, NPV, IRR, payback period, sensitivity.

Economic mode treats inflows as benefits and outflows as costs (B/C ratio).
Financial mode uses the same arithmetic on cash inflows and outflows and
labels the ratio as the profitability index (PI).
"""
import argparse

import chart
from common import (InputError, Report, add_common_args, fmt_num, fmt_pct, load_json, num, pct,
                    run_main, to_float)
from labels import T

IRR_GRID = [-0.9 + i * 0.001 for i in range(1901)] + [1.0 + i * 0.01 for i in range(1, 901)]
BISECTION_STEPS = 200
DEFAULT_DISCOUNT_RATE = 0.045  # Korean preliminary feasibility study social discount rate (2026 guideline, Art. 50)
DEFAULT_SENSITIVITY = {"rate_delta": 0.01, "cost_changes": [-0.1, 0.1], "benefit_changes": [-0.1, 0.1]}


# ---------- cash flow construction ----------

def expand_rule(rule, kind):
    """Turn one generation rule into {year: amount}. See references/appraisal.md."""
    item = rule.get("item", kind)
    if "total" in rule:
        total = to_float(rule["total"], f"{item}.total")
        start = int(rule["start_year"])
        years = int(rule["years"])
        if years <= 0:
            raise InputError(T("rule_years_positive", item=item))
        return {start + k: total / years for k in range(years)}
    if "annual" not in rule:
        raise InputError(T("rule_needs_amount", item=item))
    annual = to_float(rule["annual"], f"{item}.annual")
    if "start_year" in rule:
        start = int(rule["start_year"])
    elif "project_end_year" in rule:
        start = int(rule["project_end_year"]) + int(rule.get("gestation", 0)) + 1
    else:
        raise InputError(T("rule_needs_start", item=item))
    if "end_year" in rule:
        end = int(rule["end_year"])
    elif "duration" in rule:
        end = start + int(rule["duration"]) - 1
    else:
        raise InputError(T("rule_needs_end", item=item))
    if end < start:
        raise InputError(T("rule_end_before_start", item=item))
    growth = to_float(rule.get("growth", 0), f"{item}.growth")
    return {start + k: annual * (1 + growth) ** k for k in range(end - start + 1)}


def build_flows(config):
    """Return {year: {"cost": {item: amount}, "benefit": {item: amount}}}."""
    flows = {}

    def add(kind, item, year, amount):
        flows.setdefault(year, {"cost": {}, "benefit": {}})
        bucket = flows[year][kind]
        bucket[item] = bucket.get(item, 0.0) + amount

    for kind, rows_key, rules_key in (("cost", "costs", "cost_rules"),
                                      ("benefit", "benefits", "benefit_rules")):
        for row in config.get(rows_key, []):
            add(kind, row.get("item", kind), int(row["year"]),
                to_float(row["amount"], f"{rows_key}.amount"))
        for rule in config.get(rules_key, []):
            for year, amount in expand_rule(rule, kind).items():
                add(kind, rule.get("item", kind), year, amount)
    if not flows:
        raise InputError(T("no_flows"))
    end = config.get("analysis_end_year")
    if end is not None:
        flows = {y: v for y, v in flows.items() if y <= int(end)}
    first, last = min(flows), max(flows)
    if end is not None:
        last = max(last, int(end))
    for year in range(first, last + 1):
        flows.setdefault(year, {"cost": {}, "benefit": {}})
    return dict(sorted(flows.items()))


# ---------- discounting ----------

def discount_factor(year, base_year, rate, switch=None):
    """Piecewise compounding: the second rate applies only to years after the switch year."""
    t = year - base_year
    if not switch or year <= switch["after_year"]:
        return (1 + rate) ** -t
    t1 = switch["after_year"] - base_year
    return (1 + rate) ** -t1 * (1 + switch["rate"]) ** -(year - switch["after_year"])


def evaluate(flows, base_year, rate, switch, cost_factor=1.0, benefit_factor=1.0):
    table, pv_cost, pv_benefit = [], 0.0, 0.0
    for year, bucket in flows.items():
        cost = sum(bucket["cost"].values()) * cost_factor
        benefit = sum(bucket["benefit"].values()) * benefit_factor
        df = discount_factor(year, base_year, rate, switch)
        pv_cost += cost * df
        pv_benefit += benefit * df
        table.append({"year": year, "t": year - base_year, "df": df, "cost": cost,
                      "cost_pv": cost * df, "benefit": benefit, "benefit_pv": benefit * df,
                      "net_pv": (benefit - cost) * df})
    ratio = pv_benefit / pv_cost if pv_cost > 0 else float("nan")
    return {"table": table, "pv_cost": pv_cost, "pv_benefit": pv_benefit,
            "ratio": ratio, "npv": pv_benefit - pv_cost}


# ---------- IRR and payback ----------

def npv_at(net_by_t, rate):
    return sum(v * (1 + rate) ** -t for t, v in net_by_t)


def find_irr(net_by_t):
    """Return all roots found on the scan grid (as ratios)."""
    roots = []
    prev_rate, prev_value = None, None
    for rate in IRR_GRID:
        value = npv_at(net_by_t, rate)
        if prev_value is not None and prev_value * value < 0:
            lo, hi = prev_rate, rate
            for _ in range(BISECTION_STEPS):
                mid = (lo + hi) / 2
                if npv_at(net_by_t, lo) * npv_at(net_by_t, mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            roots.append((lo + hi) / 2)
        elif value == 0:
            roots.append(rate)
        prev_rate, prev_value = rate, value
    return roots


def sign_changes(values):
    signs = [v > 0 for v in values if v != 0]
    return sum(1 for a, b in zip(signs, signs[1:]) if a != b)


def payback(table, key):
    """Years from the start of the first year until cumulative net turns non-negative."""
    first_year = table[0]["year"]
    cumulative = 0.0
    for row in table:
        net = row[key]
        before = cumulative
        cumulative += net
        if before < 0 <= cumulative:
            fraction = -before / net
            return {"year": row["year"], "years": row["year"] - first_year + fraction}
    return None


# ---------- main ----------

def main():
    parser = argparse.ArgumentParser(description="Project appraisal (B/C, NPV, IRR)")
    parser.add_argument("--input", required=True, help="JSON file, see references/appraisal.md")
    add_common_args(parser)
    args = parser.parse_args()
    d = args.decimals
    cfg = load_json(args.input)
    warnings = []

    mode = cfg.get("mode", "economic")
    if mode not in ("economic", "financial"):
        raise InputError(T("mode_invalid", mode=mode))
    ratio_label = T("bc_ratio") if mode == "economic" else T("pi_ratio")
    npv_label = T("npv") if mode == "economic" else T("fnpv")
    cost_label = T("cost") if mode == "economic" else T("cash_outflow")
    benefit_label = T("benefit") if mode == "economic" else T("cash_inflow")
    unit = cfg.get("unit", "")
    base_year = int(cfg["base_year"])
    if "discount_rate" in cfg:
        rate = to_float(cfg["discount_rate"], "discount_rate")
    else:
        rate = DEFAULT_DISCOUNT_RATE
        warnings.append(T("default_rate"))
    switch = cfg.get("rate_switch")
    if switch:
        switch = {"after_year": int(switch["after_year"]), "rate": to_float(switch["rate"], "rate_switch.rate")}

    flows = build_flows(cfg)
    if min(flows) <= base_year:
        warnings.append(T("flows_before_base", year=min(flows), base=base_year))
    negatives = [y for y, b in flows.items() if any(v < 0 for v in b["cost"].values())]
    if negatives:
        warnings.append(T("negative_cost_rows", years=", ".join(map(str, negatives))))
    base = evaluate(flows, base_year, rate, switch)
    if base["pv_cost"] <= 0:
        raise InputError(T("pv_cost_positive"))

    net_by_t = [(row["t"], row["benefit"] - row["cost"]) for row in base["table"]]
    roots = find_irr(net_by_t)
    changes = sign_changes([v for _, v in net_by_t])
    if changes != 1:
        warnings.append(T("irr_sign_changes", n=changes))
    irr = roots[0] if len(roots) == 1 else None
    if len(roots) > 1:
        warnings.append(T("irr_multiple", roots=", ".join(fmt_pct(r, d) for r in roots)))
    for row in base["table"]:
        row["net"] = row["benefit"] - row["cost"]
    pb_discounted = payback(base["table"], "net_pv")
    pb_simple = payback(base["table"], "net")

    report = Report(d)
    input_rows = [[T("mode"), T(f"mode_{mode}")], [T("unit"), unit or "-"],
                  [T("discount_base_year"), base_year], [T("discount_rate"), pct(rate)],
                  [T("analysis_period"), f"{min(flows)} - {max(flows)}"]]
    if switch:
        input_rows.append([T("rate_switch"), T("rate_switch_desc", year=switch["after_year"],
                                               rate=fmt_pct(switch["rate"], d))])
    report.table(T("inputs"), [T("item"), T("value")], input_rows)

    item_rows = []
    for kind, label in (("cost", cost_label), ("benefit", benefit_label)):
        totals = {}
        for bucket in flows.values():
            for item, amount in bucket[kind].items():
                totals[item] = totals.get(item, 0.0) + amount
        item_rows += [[label, item, num(amount)] for item, amount in totals.items()]
    report.table(T("items_nominal"), [T("kind"), T("item"), T("nominal_total")], item_rows)

    rows = [[r["year"], r["t"], num(r["df"], 6), num(r["cost"]), num(r["cost_pv"]),
             num(r["benefit"]), num(r["benefit_pv"]), num(r["net_pv"])] for r in base["table"]]
    totals = [sum(r[k] for r in base["table"]) for k in ("cost", "cost_pv", "benefit", "benefit_pv", "net_pv")]
    rows.append([T("total"), "", ""] + [num(v) for v in totals])
    report.table(T("annual_table"),
                 [T("year"), "t", T("discount_factor"), cost_label, f"{cost_label} PV",
                  benefit_label, f"{benefit_label} PV", T("net_pv")], rows, bold_last=True)

    def payback_rows(result, years_key, year_key):
        if result is None:
            return [[T(years_key), T("not_recovered")]]
        return [[T(years_key), num(result["years"])], [T(year_key), result["year"]]]

    report.table(T("result"), [T("indicator"), T("value")], [
        [f"{benefit_label} PV", num(base["pv_benefit"])],
        [f"{cost_label} PV", num(base["pv_cost"])],
        [ratio_label, num(base["ratio"], 4)],
        [npv_label, num(base["npv"])],
        ["IRR", pct(irr) if irr is not None else T("irr_na")]]
        + payback_rows(pb_discounted, "discounted_payback", "discounted_payback_year")
        + payback_rows(pb_simple, "simple_payback", "simple_payback_year"))

    sens_cfg = {**DEFAULT_SENSITIVITY, **cfg.get("sensitivity", {})}
    scenarios = [(T("scenario_base"), rate, 1.0, 1.0)]
    delta = sens_cfg["rate_delta"]
    for sign in (-1, 1):
        scenarios.append((T("scenario_rate", delta=("+" if sign > 0 else "-") + fmt_num(delta * 100, d) + "%p"),
                          rate + sign * delta, 1.0, 1.0))
    for change in sens_cfg["cost_changes"]:
        scenarios.append((T("scenario_cost", change=("+" if change > 0 else "") + fmt_pct(change, 0)),
                          rate, 1 + change, 1.0))
    for change in sens_cfg["benefit_changes"]:
        scenarios.append((T("scenario_benefit", change=("+" if change > 0 else "") + fmt_pct(change, 0)),
                          rate, 1.0, 1 + change))
    sens_rows, sens_out = [], []
    for name, r, cf, bf in scenarios:
        sw = None
        if switch:
            sw = {"after_year": switch["after_year"], "rate": switch["rate"] + (r - rate)}
        result = evaluate(flows, base_year, r, sw, cf, bf)
        sens_rows.append([name, pct(r), num(result["ratio"], 4), num(result["npv"])])
        sens_out.append({"scenario": name, "rate": r, "cost_factor": cf, "benefit_factor": bf,
                         "ratio": result["ratio"], "npv": result["npv"]})
    report.table(T("sensitivity"), [T("scenario"), T("discount_rate"), ratio_label, npv_label], sens_rows)
    report.warnings(warnings)

    report.finish(args, {"mode": mode, "unit": unit, "base_year": base_year, "discount_rate": rate,
                         "rate_switch": switch, "pv_benefit": base["pv_benefit"],
                         "pv_cost": base["pv_cost"], "ratio": base["ratio"], "npv": base["npv"],
                         "irr": irr, "irr_roots": roots, "discounted_payback": pb_discounted,
                         "simple_payback": pb_simple, "table": base["table"],
                         "sensitivity": sens_out, "warnings": warnings})
    if args.chart:
        cumulative, values = 0.0, []
        for row in base["table"]:
            cumulative += row["net_pv"]
            values.append(cumulative)
        colors = [chart.PALETTE["highlight"] if v < 0 else chart.PALETTE["primary"] for v in values]
        chart.bar([r["year"] for r in base["table"]], values, args.chart,
                  lambda v: fmt_num(v, 0), colors=colors)


if __name__ == "__main__":
    run_main(main)
