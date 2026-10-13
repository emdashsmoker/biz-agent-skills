"""Market concentration: HHI, concentration ratios (CRk), and merger change in HHI.

Shares s_i are in percent of the whole market (sum = 100).
HHI = sum(s_i ** 2), range 0-10,000. Equivalent number of equal-size firms = 10,000 / HHI.
Merger of firms a and b: delta HHI = 2 * s_a * s_b.
When the remainder of the market is one lump ("other"), HHI is reported as a range:
lower bound treats "other" as infinitely many tiny firms (adds 0),
upper bound treats "other" as one firm (adds s_other ** 2).
"""

from _common import (InputError, build_parser, load_input, md_table, require,
                     run, section, to_number, write_json)

FULL_MARKET = 100.0
SHARE_SUM_TOLERANCE = 0.5          # percentage points allowed for rounding in reported shares
CR_LEVELS = (1, 3, 4)
KFTC_SAFE_HARBOR = [              # KFTC merger review guideline, horizontal mergers
    (0, 1200, None, "HHI below 1,200"),
    (1200, 2500, 250, "HHI 1,200-2,500 and delta below 250"),
    (2500, 10001, 150, "HHI 2,500 or more and delta below 150"),
]
US_2023_HIGH = 1800                # US 2023 Merger Guidelines: highly concentrated
US_2023_DELTA = 100
US_2023_SHARE = 30.0

EXAMPLE = {
    "market": "Example product market, domestic sales, 2024",
    "basis": "sales",
    "firms": {"Firm A": 420, "Firm B": 260, "Firm C": 150, "Firm D": 90},
    "other": 80,
    "merger": ["Firm B", "Firm C"],
}


def to_shares(firms, other, basis):
    """Convert sales (or shares) to percent shares of the whole market."""
    values = {name: to_number(v, name) for name, v in firms.items()}
    other_value = to_number(other or 0, "other")
    if any(v < 0 for v in values.values()) or other_value < 0:
        raise InputError("firm values must be non-negative")
    total = sum(values.values()) + other_value
    if total <= 0:
        raise InputError("market total must be positive")
    if basis == "share":
        if abs(total - FULL_MARKET) <= SHARE_SUM_TOLERANCE:
            scale = 1.0
            print("Shares read as percent values (sum 100).")
        elif abs(total - 1.0) <= SHARE_SUM_TOLERANCE / FULL_MARKET:
            scale = FULL_MARKET
            print("Shares read as decimal values (sum 1) and multiplied by 100.")
        else:
            raise InputError(f"shares sum to {total:.4f}; expected 100 (percent) or 1 (decimal). "
                             "Add 'other' or fix inputs")
    else:
        scale = FULL_MARKET / total
    return {n: v * scale for n, v in values.items()}, other_value * scale


def kftc_zone(hhi, delta):
    for low, high, max_delta, label in KFTC_SAFE_HARBOR:
        if low <= hhi < high:
            inside = max_delta is None or delta < max_delta
            return f"{'inside' if inside else 'outside'} safe harbor ({label})"
    return "n/a"


def main():
    args = build_parser(__doc__, EXAMPLE).parse_args()
    data = load_input(args)
    basis = data.get("basis", "sales")
    shares, other = to_shares(require(data, "firms"), data.get("other"), basis)
    ranked = sorted(shares.items(), key=lambda kv: kv[1], reverse=True)
    hhi_low = sum(s ** 2 for s in shares.values())
    hhi_high = hhi_low + other ** 2

    print(f"# Market concentration ({data.get('market', 'market not stated')})\n")
    rows = [[name, share] for name, share in ranked]
    if other:
        rows.append(["other (unlisted)", other])
    section("Shares (%)", md_table(["firm", "share %"], rows))
    cr = {k: sum(s for _, s in ranked[:k]) for k in CR_LEVELS if k <= len(ranked)}
    hhi_text = f"{hhi_low:,.0f}" if not other else f"{hhi_low:,.0f} - {hhi_high:,.0f}"
    section("Concentration", md_table(
        ["measure", "value"],
        [["HHI", hhi_text],
         ["equivalent equal-size firms (10,000 / HHI)",
          f"{10000 / hhi_low:.2f}" if not other
          else f"{10000 / hhi_high:.2f} - {10000 / hhi_low:.2f}"]]
        + [[f"CR{k}", f"{v:.2f}%"] for k, v in cr.items()]))

    result = {"shares": dict(ranked), "other": other, "hhi_low": hhi_low,
              "hhi_high": hhi_high, "cr": cr}
    merger = data.get("merger")
    if merger:
        if len(merger) != 2 or any(m not in shares for m in merger):
            raise InputError("merger must list two firm names from 'firms'")
        a, b = merger
        delta = 2 * shares[a] * shares[b]
        post_low, post_high = hhi_low + delta, hhi_high + delta
        combined = shares[a] + shares[b]
        def us_presumed(post):
            return (post > US_2023_HIGH or combined > US_2023_SHARE) and delta > US_2023_DELTA
        us_text = ("yes" if us_presumed(post_low) else
                   "only if 'other' is one firm" if us_presumed(post_high) else "no")
        section(f"Merger {a} + {b}", md_table(
            ["measure", "value"],
            [["combined share", f"{combined:.2f}%"], ["delta HHI", f"{delta:,.0f}"],
             ["post-merger HHI", f"{post_low:,.0f}" if not other
              else f"{post_low:,.0f} - {post_high:,.0f}"],
             ["KFTC screen (lower bound HHI)", kftc_zone(post_low, delta)],
             ["KFTC screen (upper bound HHI)", kftc_zone(post_high, delta)],
             ["US 2023 guideline presumption", us_text]]))
        result.update({"delta_hhi": delta, "post_hhi_low": post_low, "post_hhi_high": post_high})
    write_json(args.json, result)


if __name__ == "__main__":
    run(main)
