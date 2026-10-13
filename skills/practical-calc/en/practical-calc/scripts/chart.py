"""Chart helpers shared by all tools.

Style rules: one message per chart, no in-chart title, no grid or legend,
direct data labels, bold text, minimal spines, flat colors.
"""
from labels import T

PALETTE = {
    "primary": "#6B8EC2",    # pastel navy, default data color
    "highlight": "#F5A962",  # emphasis and negative steps
    "dark": "#4F6F9E",       # totals in waterfalls
    "light": "#BCC9E2",      # de-emphasized data
    "text": "#1A1A1A",
    "subtext": "#595959",
}
SERIES_COLORS = ["#4F6F9E", "#6B8EC2", "#93AAD3", "#BCC9E2"]
PREFERRED_FONT = "NanumGothic"  # covers Hangul and Latin glyphs
FONT_SIZE = 14
FIG_SIZE = (10, 6)
DPI = 200


def apply_style():
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib import font_manager
    except ImportError:
        raise SystemExit(T("chart_needs_matplotlib"))
    names = {font.name for font in font_manager.fontManager.ttflist}
    if PREFERRED_FONT not in names:
        # matplotlib caches its font list, so fonts installed later must be registered by file
        for path in font_manager.findSystemFonts():
            file_name = path.replace("\\", "/").rsplit("/", 1)[-1]
            if file_name.startswith(PREFERRED_FONT) and "Coding" not in file_name:
                font_manager.fontManager.addfont(path)
        names = {font.name for font in font_manager.fontManager.ttflist}
    if PREFERRED_FONT in names:
        plt.rcParams["font.family"] = PREFERRED_FONT
    else:
        print(T("font_missing", font=PREFERRED_FONT))
    plt.rcParams.update({
        "font.size": FONT_SIZE,
        "font.weight": "bold",
        "axes.labelweight": "bold",
        "axes.unicode_minus": False,
        "text.color": PALETTE["text"],
        "axes.labelcolor": PALETTE["text"],
        "xtick.color": PALETTE["text"],
        "ytick.color": PALETTE["text"],
    })
    return plt


def _finish(fig, ax, path, keep_spines):
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(side in keep_spines)
    ax.grid(False)
    fig.patch.set_facecolor("white")
    fig.tight_layout()
    fig.savefig(path, dpi=DPI, facecolor="white", bbox_inches="tight", pad_inches=0.4)
    print(f"{T('saved_chart')}: {path}")


MAX_LABELED_BARS = 15  # beyond this, only key bars get labels to avoid overlap


def key_indices(values):
    """First, last, minimum, maximum and first non-negative after a negative run."""
    keys = {0, len(values) - 1, values.index(min(values)), values.index(max(values))}
    for i in range(1, len(values)):
        if values[i - 1] < 0 <= values[i]:
            keys.add(i)
            break
    return keys


def bar(labels, values, path, value_format, colors=None, y_label=""):
    """Vertical bars for time series. Keeps the bottom spine only."""
    plt = apply_style()
    width = max(FIG_SIZE[0], 0.45 * len(labels))
    fig, ax = plt.subplots(figsize=(width, FIG_SIZE[1]))
    bars = ax.bar([str(x) for x in labels], values,
                  color=colors or PALETTE["primary"])
    shown = range(len(values)) if len(values) <= MAX_LABELED_BARS else key_indices(list(values))
    ax.bar_label(bars, labels=[value_format(v) if i in shown else "" for i, v in enumerate(values)],
                 padding=4, fontsize=FONT_SIZE, fontweight="bold")
    if len(labels) > MAX_LABELED_BARS:
        step = -(-len(labels) // MAX_LABELED_BARS)  # ceiling division
        ax.set_xticks(range(0, len(labels), step))
        ax.set_xticklabels([str(labels[i]) for i in range(0, len(labels), step)])
    ax.axhline(0, color=PALETTE["subtext"], linewidth=1)
    ax.set_yticks([])
    ax.set_ylabel(y_label)
    ax.margins(y=0.15)
    _finish(fig, ax, path, keep_spines=("bottom",))
    plt.close(fig)


def barh(labels, values, path, value_format, colors=None, ref_line=None, x_label=""):
    """Horizontal bars for item comparison, largest value on top."""
    plt = apply_style()
    height = max(FIG_SIZE[1], 0.5 * len(labels) + 1)
    fig, ax = plt.subplots(figsize=(FIG_SIZE[0], height))
    order = list(range(len(labels)))[::-1]
    bars = ax.barh([str(labels[i]) for i in order], [values[i] for i in order],
                   color=[(colors or [PALETTE["primary"]] * len(labels))[i] for i in order])
    ax.bar_label(bars, labels=[value_format(values[i]) for i in order], padding=4,
                 fontsize=FONT_SIZE, fontweight="bold")
    if ref_line is not None:
        ax.axvline(ref_line, color=PALETTE["subtext"], linewidth=1.2, linestyle="--")
    ax.set_xticks([])
    ax.set_xlabel(x_label)
    ax.margins(x=0.15)
    _finish(fig, ax, path, keep_spines=("left",))
    plt.close(fig)


def waterfall(start, steps, end, path, value_format):
    """Bridge from a start total to an end total through signed steps.

    start, end: (label, value); steps: list of (label, signed value).
    """
    plt = apply_style()
    fig, ax = plt.subplots(figsize=(max(FIG_SIZE[0], 1.4 * (len(steps) + 2)), FIG_SIZE[1]))
    labels = [start[0]] + [s[0] for s in steps] + [end[0]]
    bottoms, heights, colors, texts = [0], [start[1]], [PALETTE["dark"]], [value_format(start[1])]
    running = start[1]
    for _, delta in steps:
        bottoms.append(running if delta >= 0 else running + delta)
        heights.append(abs(delta))
        colors.append(PALETTE["primary"] if delta >= 0 else PALETTE["highlight"])
        texts.append(("+" if delta >= 0 else "") + value_format(delta))
        running += delta
    bottoms.append(0)
    heights.append(end[1])
    colors.append(PALETTE["dark"])
    texts.append(value_format(end[1]))
    bars = ax.bar(labels, heights, bottom=bottoms, color=colors)
    ax.bar_label(bars, labels=texts, padding=4, fontsize=FONT_SIZE, fontweight="bold")
    ax.axhline(0, color=PALETTE["subtext"], linewidth=1)
    ax.set_yticks([])
    ax.margins(y=0.15)
    _finish(fig, ax, path, keep_spines=("bottom",))
    plt.close(fig)


def lines(x_values, series, path, x_label, y_label, marker=None):
    """Line chart with end-of-line labels instead of a legend.

    series: list of (name, y_values). marker: optional (x, y, text).
    """
    plt = apply_style()
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    for index, (name, y_values) in enumerate(series):
        color = SERIES_COLORS[index % len(SERIES_COLORS)]
        ax.plot(x_values, y_values, color=color, linewidth=2.5)
        ax.annotate(name, (x_values[-1], y_values[-1]), xytext=(6, 0),
                    textcoords="offset points", va="center", color=color,
                    fontweight="bold")
    if marker:
        ax.scatter([marker[0]], [marker[1]], color=PALETTE["highlight"], s=90, zorder=3)
        ax.annotate(marker[2], (marker[0], marker[1]), xytext=(10, -24),
                    textcoords="offset points", color=PALETTE["text"], fontweight="bold")
    from matplotlib.ticker import FuncFormatter
    thousands = FuncFormatter(lambda v, _: f"{v:,.0f}")
    ax.xaxis.set_major_formatter(thousands)
    ax.yaxis.set_major_formatter(thousands)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.margins(x=0.12)
    _finish(fig, ax, path, keep_spines=("left", "bottom"))
    plt.close(fig)
