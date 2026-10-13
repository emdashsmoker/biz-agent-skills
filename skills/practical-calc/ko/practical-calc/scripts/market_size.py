"""Market sizing: TAM, SAM, SOM by chained factors.

Each approach is an ordered list of steps. The first step is a base quantity,
each later step multiplies the running value. The running value after the
last step of a stage is that stage's market size.
"""
import argparse

import chart
from common import (InputError, Report, add_common_args, chart_formatter, fmt_pct, gen, load_json, num,
                    pct, run_main, to_float)
from labels import T

STAGES = ("TAM", "SAM", "SOM")


def run_chain(name, steps):
    if not steps:
        raise InputError(T("market_empty", name=name))
    running, rows, sizes = None, [], {}
    last_stage_index = -1
    for pos, step in enumerate(steps):
        stage = str(step.get("stage", "")).upper()
        if stage not in STAGES:
            raise InputError(T("market_stage_invalid", name=name, stage=stage))
        index = STAGES.index(stage)
        if index < last_stage_index:
            raise InputError(T("market_stage_order", name=name))
        value = to_float(step["value"], f"{name}.{step.get('name', pos)}")
        running = value if running is None else running * value
        rows.append({"stage": stage, "name": step.get("name", ""), "value": value,
                     "running": running, "source": step.get("source", "")})
        sizes[stage] = running
        last_stage_index = index
    missing = [s for s in STAGES if s not in sizes]
    if missing:
        raise InputError(T("market_stage_missing", name=name, stages=", ".join(missing)))
    return rows, sizes


def main():
    parser = argparse.ArgumentParser(description="TAM, SAM, SOM market sizing")
    parser.add_argument("--input", required=True, help="JSON file, see references/market.md")
    add_common_args(parser)
    args = parser.parse_args()
    d = args.decimals
    cfg = load_json(args.input)
    unit = cfg.get("unit", "")
    approaches = cfg.get("approaches", {})
    if not approaches:
        raise InputError(T("market_no_approach"))
    warnings, output = [], {"unit": unit, "approaches": {}}
    report = Report(d)

    for name, steps in approaches.items():
        rows, sizes = run_chain(name, steps)
        output["approaches"][name] = {"steps": rows, "sizes": sizes}
        report.table(f"{T('steps')}: {name}",
                     [T("stage"), T("step"), T("value"), T("running_value"), T("source")],
                     [[r["stage"], r["name"], gen(r["value"]), num(r["running"]), r["source"] or "-"]
                      for r in rows])
        report.table(f"{T('result')}: {name}",
                     [T("stage"), f"{T('market_size')} ({unit})" if unit else T("market_size"),
                      T("ratio_to_upper")],
                     [["TAM", num(sizes["TAM"]), None],
                      ["SAM", num(sizes["SAM"]), pct(sizes["SAM"] / sizes["TAM"])],
                      ["SOM", num(sizes["SOM"]), pct(sizes["SOM"] / sizes["SAM"])]])
        if sizes["SAM"] > sizes["TAM"] or sizes["SOM"] > sizes["SAM"]:
            warnings.append(T("market_nesting", name=name))

    names = list(output["approaches"])
    if len(names) == 2:
        a, b = (output["approaches"][n]["sizes"] for n in names)
        report.table(T("market_cross_check"), [T("stage"), names[0], names[1], T("gap_pct")],
                     [[s, num(a[s]), num(b[s]), pct(b[s] / a[s] - 1)] for s in STAGES])

    projection = cfg.get("projection")
    if projection:
        g = to_float(projection["growth_rate"], "projection.growth_rate")
        y0, y1 = int(projection["start_year"]), int(projection["end_year"])
        rows = []
        for name in names:
            sizes = output["approaches"][name]["sizes"]
            rows += [[name, s, num(sizes[s]), num(sizes[s] * (1 + g) ** (y1 - y0))] for s in STAGES]
        report.table(T("market_projection", g=fmt_pct(g, d), y0=y0, y1=y1),
                     [T("approach"), T("stage"), str(y0), str(y1)], rows)
        output["projection"] = projection
    report.warnings(warnings)
    report.finish(args, output)
    if args.chart:
        sizes = output["approaches"][names[0]]["sizes"]
        values = [sizes[s] for s in STAGES]
        chart.barh(list(STAGES), values, args.chart, chart_formatter(values, d))


if __name__ == "__main__":
    run_main(main)
