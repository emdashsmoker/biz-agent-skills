"""Regional industry analysis: location quotient (LQ), regional share, shift-share.

LQ_ij        = (x_ij / x_j) / (X_i / X)      x: region j, X: nation, i: industry
Regional share = x_ij / X_i                   (share of the national industry total)
Shift-share (Dunn 1960 classic form), for region j and industry i between t0 and t1:
  national growth  NS = e0 * G                G  = E1 / E0 - 1   (all industries, nation)
  industry mix     IM = e0 * (G_i - G)        G_i = E1_i / E0_i - 1
  regional shift   RS = e0 * (g_i - G_i)      g_i = e1 / e0 - 1
  NS + IM + RS = e1 - e0
Input data must be tidy: one row per (region, industry) with numeric values.
"""

import pandas as pd

from _common import (InputError, build_parser, load_input, md_table, require,
                     run, section, to_number, write_json)

KOREAN_FONTS = ["NanumGothic", "Malgun Gothic", "AppleGothic", "Noto Sans CJK KR", "Noto Sans KR"]
BAR_COLOR = "#6B8EC2"
REFERENCE_COLOR = "#333333"

EXAMPLE = {
    "mode": "lq",
    "data_file": "employees_2023.csv",
    "columns": {"region": "region", "industry": "industry", "value": "employees"},
    "national_label": "Nation",
    "total_label": "All industries",
    "target": {"industry": "Manufacturing"},
    "threshold": 1.0,
    "chart": None,
    "_shift_share_variant": {
        "mode": "shift_share",
        "columns": {"region": "region", "industry": "industry",
                    "value_t0": "employees_2018", "value_t1": "employees_2023"},
        "target": {"region": "Region A"},
    },
}


def read_table(path):
    """Read CSV or XLSX into a DataFrame (UTF-8 with BOM tolerated)."""
    if str(path).lower().endswith((".xlsx", ".xls")):
        return pd.read_excel(path)
    return pd.read_csv(path, encoding="utf-8-sig")


def numeric(series, name):
    """Parse spreadsheet number notations cell by cell; reject blanks and negatives."""
    def convert(value):
        if pd.isna(value) or str(value).strip() == "":
            raise InputError(f"column '{name}' has empty cells; resolve them during preparation")
        return to_number(value, f"column {name}")
    values = series.map(convert).astype(float)
    if (values < 0).any():
        raise InputError(f"column '{name}' has negative values")
    return values


def tidy(df, columns, value_keys):
    """Rename to canonical columns and check uniqueness of (region, industry)."""
    rename = {columns["region"]: "region", columns["industry"]: "industry"}
    for key in value_keys:
        rename[columns[key]] = key
    missing = [c for c in rename if c not in df.columns]
    if missing:
        raise InputError(f"columns not found in data file: {missing}")
    out = df[list(rename)].rename(columns=rename)
    out["region"] = out["region"].astype(str).str.strip()
    out["industry"] = out["industry"].astype(str).str.strip()
    for key in value_keys:
        out[key] = numeric(out[key], columns[key])
    duplicated = out.duplicated(["region", "industry"])
    if duplicated.any():
        sample = out.loc[duplicated, ["region", "industry"]].head(3).values.tolist()
        raise InputError(f"duplicate (region, industry) rows, e.g. {sample}; "
                         "filter sub-categories (such as establishment type) first")
    return out


def split_levels(df, national_label, total_label, key):
    """Return (regional rows, national by industry, regional totals, national total)."""
    notes = []
    if national_label:
        nation = df[df["region"] == national_label]
        regions = df[df["region"] != national_label]
        if nation.empty:
            raise InputError(f"national_label '{national_label}' not found in region column")
    else:
        regions = df
        nation = df.groupby("industry", as_index=False)[key].sum()
        nation["region"] = "(sum of regions)"
        notes.append("National values = sum of listed regions (all regions must be present).")

    if total_label:
        reg_total = regions[regions["industry"] == total_label].set_index("region")[key]
        nat_total_rows = nation[nation["industry"] == total_label][key]
        if reg_total.empty or nat_total_rows.empty:
            raise InputError(f"total_label '{total_label}' not found for regions and nation")
        nat_total = float(nat_total_rows.iloc[0])
        regions = regions[regions["industry"] != total_label]
        nation = nation[nation["industry"] != total_label]
    else:
        reg_total = regions.groupby("region")[key].sum()
        nat_total = float(nation[key].sum())
        notes.append("Totals = sum of listed industries (list must be complete and one level only).")

    if national_label:
        check = regions.groupby("industry")[key].sum()
        nat = nation.set_index("industry")[key]
        gap = ((check - nat).abs() / nat.replace(0, pd.NA)).dropna()
        if not gap.empty and gap.max() > 0.001:
            notes.append(f"Sum of regions differs from national value by up to {gap.max():.2%} "
                         "(suppressed cells or missing regions).")
    return regions, nation.set_index("industry")[key], reg_total, nat_total, notes


def location_quotients(df, national_label, total_label):
    regions, nation, reg_total, nat_total, notes = split_levels(
        df, national_label, total_label, "value")
    out = regions.copy()
    out["region_total"] = out["region"].map(reg_total)
    out["national_industry"] = out["industry"].map(nation)
    out["regional_share"] = out["value"] / out["national_industry"]
    out["lq"] = (out["value"] / out["region_total"]) / (out["national_industry"] / nat_total)
    return out, notes


def shift_share(df, national_label, total_label):
    reg0, nat0, _, tot0, notes0 = split_levels(df, national_label, total_label, "value_t0")
    reg1, nat1, _, tot1, _ = split_levels(df, national_label, total_label, "value_t1")
    out = reg0[["region", "industry", "value_t0"]].merge(
        reg1[["region", "industry", "value_t1"]], on=["region", "industry"])
    growth_all = tot1 / tot0 - 1
    out["G_nation"] = growth_all
    out["G_industry"] = out["industry"].map(nat1 / nat0 - 1)
    out["g_region"] = out["value_t1"] / out["value_t0"] - 1
    out["national_growth"] = out["value_t0"] * growth_all
    out["industry_mix"] = out["value_t0"] * (out["G_industry"] - growth_all)
    out["regional_shift"] = out["value_t0"] * (out["g_region"] - out["G_industry"])
    out["actual_change"] = out["value_t1"] - out["value_t0"]
    residual = (out[["national_growth", "industry_mix", "regional_shift"]].sum(axis=1)
                - out["actual_change"]).abs().max()
    if residual > 1e-6:
        raise InputError(f"shift-share components do not add up (residual {residual})")
    return out, notes0


def pick(df, target):
    """Filter to one industry (compare regions) or one region (compare industries)."""
    if not target:
        return df, "all"
    if "industry" in target:
        view = df[df["industry"] == target["industry"]]
        label = f"industry = {target['industry']}"
    elif "region" in target:
        view = df[df["region"] == target["region"]]
        label = f"region = {target['region']}"
    else:
        raise InputError("target must name 'industry' or 'region'")
    if view.empty:
        raise InputError(f"target not found: {target}")
    return view, label


def draw_chart(view, label_col, path, threshold):
    """Horizontal bar chart of LQ, largest at top, with the threshold line."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import font_manager

    installed = {f.name for f in font_manager.fontManager.ttflist}
    font = next((f for f in KOREAN_FONTS if f in installed), None)
    if font:
        plt.rcParams["font.family"] = font
    else:
        print("WARNING: no Korean font found; Hangul labels may not render.")
    plt.rcParams["axes.unicode_minus"] = False
    data = view.sort_values("lq")
    fig, ax = plt.subplots(figsize=(8, max(3, 0.45 * len(data) + 1)))
    bars = ax.barh(data[label_col], data["lq"], color=BAR_COLOR)
    ax.axvline(threshold, color=REFERENCE_COLOR, linestyle="--", linewidth=1)
    ax.text(threshold, len(data) - 0.4, f"LQ {threshold:g}", ha="center", va="bottom",
            fontsize=12, color=REFERENCE_COLOR)
    for bar, value in zip(bars, data["lq"]):
        ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f" {value:.2f}",
                va="center", fontsize=12, fontweight="bold")
    for side in ("top", "right", "bottom"):
        ax.spines[side].set_visible(False)
    ax.xaxis.set_visible(False)
    ax.tick_params(axis="y", labelsize=12)
    fig.tight_layout()
    fig.savefig(path, dpi=200, facecolor="white")
    print(f"(chart saved to {path})")


def main():
    args = build_parser(__doc__, EXAMPLE).parse_args()
    cfg = load_input(args)
    mode = cfg.get("mode", "lq")
    columns = require(cfg, "columns")
    raw = read_table(require(cfg, "data_file"))
    national, total = cfg.get("national_label"), cfg.get("total_label")
    target = cfg.get("target")

    if mode == "lq":
        df = tidy(raw, columns, ["value"])
        result, notes = location_quotients(df, national, total)
        view, label = pick(result, target)
        view = view.sort_values("lq", ascending=False)
        threshold = to_number(cfg.get("threshold", 1.0), "threshold")
        print(f"# Location quotient ({columns['value']}, {label})\n")
        section("LQ table (descending)", md_table(
            ["region", "industry", "value", "region total", "national industry",
             "regional share", "LQ", f"LQ >= {threshold:g}"],
            [[r.region, r.industry, r.value, r.region_total, r.national_industry,
              f"{r.regional_share:.2%}", f"{r.lq:.3f}", bool(r.lq >= threshold)]
             for r in view.itertuples()]))
        if cfg.get("chart"):
            label_col = "region" if target and "industry" in target else "industry"
            draw_chart(view, label_col, cfg["chart"], threshold)
        payload = view[["region", "industry", "value", "regional_share", "lq"]]
    elif mode == "shift_share":
        df = tidy(raw, columns, ["value_t0", "value_t1"])
        result, notes = shift_share(df, national, total)
        view, label = pick(result, target)
        print(f"# Shift-share ({columns['value_t0']} -> {columns['value_t1']}, {label})\n")
        rows = [[r.region, r.industry, r.value_t0, r.value_t1, r.national_growth,
                 r.industry_mix, r.regional_shift, r.actual_change] for r in view.itertuples()]
        sums = view[["value_t0", "value_t1", "national_growth", "industry_mix",
                     "regional_shift", "actual_change"]].sum()
        rows.append(["Total", ""] + [sums[c] for c in sums.index])
        section("Components", md_table(
            ["region", "industry", "t0", "t1", "national growth", "industry mix",
             "regional shift", "actual change"], rows))
        print(f"National growth rate of all industries G = {view['G_nation'].iloc[0]:.4%}\n")
        payload = view
    else:
        raise InputError("mode must be 'lq' or 'shift_share'")

    for note in notes:
        print(f"NOTE: {note}")
    write_json(args.json, payload.to_dict(orient="records"))


if __name__ == "__main__":
    run(main)
