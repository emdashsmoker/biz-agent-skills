"""Market sizing: TAM, SAM, SOM (top-down) cross-checked with a bottom-up build.

Top-down:  TAM (given, or users x adoption x spend per user)
           SAM = TAM x product of filter shares (region, segment, channel ...)
           SOM = SAM x obtainable share
Bottom-up: revenue = sum(customers x adoption x units per customer x price x purchases per year)
Projection: value_T = value_0 x (1 + CAGR) ** (T - base year)
Every factor should carry a source; the report lists missing sources.
"""

from _common import (InputError, build_parser, load_input, md_table, pct,
                     require, run, section, to_number, write_json)

EXAMPLE = {
    "unit": "KRW 100 million",
    "year": 2025,
    "top_down": {
        "tam": 12000, "tam_source": "industry statistics (name, year)",
        "sam_filters": [
            {"name": "domestic share of global market", "share": 0.04, "source": "..."},
            {"name": "target customer segment", "share": 0.35, "source": "..."},
        ],
        "som_share": 0.08, "som_source": "comparable entrant share (state basis)",
    },
    "bottom_up": {
        "segments": [
            {"name": "Public agencies", "customers": 250, "adoption_rate": 0.10,
             "units_per_customer": 1, "price": 0.30, "purchases_per_year": 1, "source": "..."},
            {"name": "Mid-size firms", "customers": 1800, "adoption_rate": 0.02,
             "units_per_customer": 1, "price": 0.15, "purchases_per_year": 1, "source": "..."},
        ]
    },
    "projection": {"cagr": 0.08, "cagr_source": "...", "to_years": [2028, 2030]},
}


def top_down(spec, missing):
    if "tam" in spec:
        tam = to_number(spec["tam"], "tam")
        build = None
    else:
        b = require(spec, "tam_build", "top_down")
        factors = [to_number(require(b, k, "tam_build"), k)
                   for k in ("users", "adoption_rate", "spend_per_user")]
        tam = factors[0] * factors[1] * factors[2]
        build = factors
    if not spec.get("tam_source"):
        missing.append("tam_source")
    rows, value = [["TAM", "", tam]], tam
    for i, f in enumerate(spec.get("sam_filters", [])):
        share = to_number(require(f, "share", f"sam_filters[{i}]"), "share")
        if not 0 <= share <= 1:
            raise InputError(f"sam_filters[{i}].share must be between 0 and 1")
        if not f.get("source"):
            missing.append(f"sam_filters[{i}].source")
        value *= share
        rows.append([f"x {f.get('name', f'filter {i + 1}')}", pct(share), value])
    sam = value
    rows.append(["SAM", "", sam])
    som_share = to_number(require(spec, "som_share", "top_down"), "som_share")
    if not spec.get("som_source"):
        missing.append("som_source")
    som = sam * som_share
    rows.append(["SOM (x obtainable share)", pct(som_share), som])
    return {"tam": tam, "sam": sam, "som": som, "tam_build": build}, rows


def bottom_up(spec, missing):
    rows, total = [], 0.0
    for i, s in enumerate(require(spec, "segments", "bottom_up")):
        where = f"segments[{i}]"
        values = [to_number(require(s, k, where), k) for k in
                  ("customers", "adoption_rate", "units_per_customer", "price")]
        freq = to_number(s.get("purchases_per_year", 1), "purchases_per_year")
        revenue = values[0] * values[1] * values[2] * values[3] * freq
        if not s.get("source"):
            missing.append(f"{where}.source")
        total += revenue
        rows.append([s.get("name", where)] + values + [freq, revenue])
    return total, rows


def main():
    args = build_parser(__doc__, EXAMPLE).parse_args()
    data = load_input(args)
    unit, year = data.get("unit", "unit not stated"), int(require(data, "year"))
    missing, result = [], {}
    print(f"# Market size ({unit}, base year {year})\n")

    if "top_down" in data:
        td, rows = top_down(data["top_down"], missing)
        result.update(td)
        section("Top-down chain", md_table(["step", "factor", "value"], rows))
    if "bottom_up" in data:
        bu, rows = bottom_up(data["bottom_up"], missing)
        result["bottom_up"] = bu
        section("Bottom-up build", md_table(
            ["segment", "customers", "adoption", "units/customer", "price", "purchases/yr",
             "revenue"], rows, decimals=4))
        if "som" in result and result["som"] > 0:
            print(f"Bottom-up / top-down SOM = {bu / result['som']:.2f} "
                  "(explain the gap before using either figure)\n")

    projection = data.get("projection")
    if projection:
        g = to_number(require(projection, "cagr", "projection"), "cagr")
        tiers = [k for k in ("tam", "sam", "som", "bottom_up") if k in result]
        rows = []
        for target in projection.get("to_years", []):
            rows.append([str(target)] + [result[k] * (1 + g) ** (int(target) - year) for k in tiers])
        section(f"Projection at CAGR {pct(g)}", md_table(["year"] + tiers, rows))
        if not projection.get("cagr_source"):
            missing.append("projection.cagr_source")
    if missing:
        print("MISSING SOURCES: " + ", ".join(missing) + "\n")
    result["missing_sources"] = missing
    write_json(args.json, result)


if __name__ == "__main__":
    run(main)
