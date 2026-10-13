"""CAGR, year-over-year growth, nominal-to-real conversion, and projection.

CAGR = (V_end / V_start) ** (1 / n) - 1, where n = end_year - start_year
(the number of yearly steps, not the number of data points).
Real value_t = nominal_t * index_base / index_t (index = deflator or CPI).
"""

from _common import (InputError, build_parser, load_input, md_table, pct,
                     require, run, section, to_number, write_json)

EXAMPLE = {
    "series": {"2020": 1000, "2021": 1150, "2022": 1210},
    "unit": "KRW 100 million",
    "deflator": {"2020": 100.0, "2021": 102.0, "2022": 105.0},
    "base_year": 2020,
    "project_to": [2025, 2030],
    "projection_rate": None,
}


def parse_series(raw, name):
    """Turn {"2020": 1.0, ...} into a year-sorted list of (int year, float value)."""
    if not isinstance(raw, dict) or len(raw) < 2:
        raise InputError(f"'{name}' needs at least two year:value pairs")
    pairs = []
    for year, value in raw.items():
        try:
            year_int = int(year)
        except ValueError as exc:
            raise InputError(f"'{name}' has a non-integer year: {year!r}") from exc
        pairs.append((year_int, to_number(value, f"{name}[{year}]")))
    return sorted(pairs)


def cagr(start_value, end_value, periods):
    """Return (rate, note). rate is None when CAGR is undefined."""
    if periods <= 0:
        return None, "end year must be later than start year"
    if start_value <= 0:
        return None, "undefined: start value must be positive"
    if end_value < 0:
        return None, "undefined: end value is negative"
    return (end_value / start_value) ** (1 / periods) - 1, "ok"


def to_real(series, index, base_year):
    """Convert nominal values to base-year prices with a price index."""
    index_map = dict(index)
    if base_year not in index_map:
        raise InputError(f"price index has no value for base_year {base_year}")
    real = []
    for year, value in series:
        if year not in index_map:
            raise InputError(f"price index has no value for year {year}")
        if index_map[year] <= 0:
            raise InputError(f"price index must be positive (year {year})")
        real.append((year, value * index_map[base_year] / index_map[year]))
    return real


def yoy_rows(series):
    """Growth between consecutive observations, annualized when years are skipped."""
    rows = []
    for (y0, v0), (y1, v1) in zip(series, series[1:]):
        rate, note = cagr(v0, v1, y1 - y0)
        rows.append((y0, y1, rate, note))
    return rows


def main():
    args = build_parser(__doc__, EXAMPLE).parse_args()
    data = load_input(args)
    series = parse_series(require(data, "series"), "series")
    unit = data.get("unit", "")
    (first_year, first_value), (last_year, last_value) = series[0], series[-1]
    periods = last_year - first_year

    rate, note = cagr(first_value, last_value, periods)
    results = {"nominal_cagr": rate, "periods": periods, "note": note}
    print("# Growth report\n")
    section("CAGR (nominal)", md_table(
        ["start year", "start value", "end year", "end value", "n (years)", "CAGR", "status"],
        [[str(first_year), first_value, str(last_year), last_value, periods,
          pct(rate) if rate is not None else "n/a", note]]))
    print(f"Formula: ({last_value:,.6g} / {first_value:,.6g}) ^ (1 / {periods}) - 1"
          + (f"   Unit: {unit}\n" if unit else "\n"))

    section("Year-over-year growth", md_table(
        ["from", "to", "annualized growth", "status"],
        [[str(y0), str(y1), pct(r) if r is not None else "n/a", n] for y0, y1, r, n in yoy_rows(series)]))

    deflator = data.get("deflator")
    if deflator:
        base_year = int(require(data, "base_year"))
        index = parse_series(deflator, "deflator")
        real = to_real(series, index, base_year)
        real_rate, real_note = cagr(real[0][1], real[-1][1], periods)
        results.update({"real_values": dict(real), "real_cagr": real_rate})
        section(f"Real values (base year {base_year} prices)", md_table(
            ["year", "nominal", "index", "real"],
            [[str(y), v, dict(index)[y], r] for (y, v), (_, r) in zip(series, real)]))
        print(f"Real CAGR: {pct(real_rate) if real_rate is not None else 'n/a'} ({real_note})\n")

    targets = data.get("project_to") or []
    if targets:
        growth = data.get("projection_rate")
        growth = rate if growth is None else to_number(growth, "projection_rate")
        if growth is None:
            raise InputError("cannot project: CAGR is undefined and no projection_rate given")
        rows = []
        for target in targets:
            steps = int(target) - last_year
            rows.append([str(int(target)), steps, last_value * (1 + growth) ** steps])
        results["projection"] = {r[0]: r[2] for r in rows}
        section(f"Projection from {last_year} at {pct(growth)} per year",
                md_table(["year", "years ahead", "projected value"], rows))

    write_json(args.json, results)


if __name__ == "__main__":
    run(main)
