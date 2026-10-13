# Charts

Fix the message first, find the comparison type the message makes, and choose the form that fits that comparison. Colors, fonts, title placement, patterns to avoid, and visual verification follow visual.md.

## Choosing the form

- The order is: decide the message, identify the comparison type, choose the chart form.
- If the user does not specify a form, examine the data in code, judge the comparison type, and propose a form with the reason.
- If the user asks to build it right away without a plan, choose the form automatically from the comparison type and build it.

| Comparison type | Cues in the request | Form |
|-----------------|---------------------|------|
| Component | ratio, share, composition | Pie chart (6 slices or fewer), stacked bar |
| Item | larger, smaller, rank, gap | Horizontal bar |
| Time series | change, trend, growth | Vertical bar (column), line |
| Frequency distribution | range, frequency, distribution | Histogram |
| Correlation | correlation, relationship, moving together | Scatter plot |
| Matrix | map, matrix, cross table | Bubble, heatmap |

- For time series, use vertical bars when there are few time points and a line when there are many. Keep vertical bar charts to 12 time points or fewer.

## Preparing the data

- When there are more than 5 categories, keep the top 4-5 and combine the rest into "Other". A pie chart has no more than 6 slices.
- When a time series has more than 12 points, propose cutting it to the latest 12 or to the range the message needs.
- Sort non-time-series categories by value in descending order. Put "Other" last regardless of its rank.
- Calculate sums, ratios, ranks, and sorting in code.

## Common specifications

- Use a white or transparent background and no outer border around the chart.
- Paint data in #6B8EC2 and only the one message target in #C0392B. Tone down comparison series with lightness steps.
- Set all text in NanumGothic Bold at 16pt by default and at least 12pt.
- Show category names on the axis and values as data labels.
- Keep spines as follows: left only for horizontal bars, bottom only for vertical bars, left and bottom for lines and scatter plots. Bubble charts and heatmaps keep all four sides because they need to show cell boundaries.
- Remove grids other than the axes. If readability requires it, add a minimal guide line.
- Minimize legends and replace them with direct labels. Do not make readers identify data through the legend alone.
- Put units in axis labels (for example Revenue (KRW 100M)).
- Bar length must be proportional to the value, so the value axis of a bar chart starts at zero.
- Keep components to a minimum to raise the share of ink that shows data.
- Divide categories without overlap so they cover the whole, and map categories to colors one to one.

## Data labels

- In charts with the value axis removed (bars, pies, bubbles, heatmaps), show the value directly on every data shape so readers do not need the axis.
- Line charts keep the value axis and label the points tied to the message, such as end points and emphasized points.
- Label every named point in a scatter plot in the form "name\n(x, y)".
- Choose the label format from value ("850"), ratio ("26%"), value and ratio ("850(26%)"), and value and rank ("850(1st)").
- Use 0 decimal places by default, and 1-2 if the user specifies.
- When labels overlap, resolve them in this order: automatic placement (the adjustText package in matplotlib), bar label placement (`bar_label`), automatic margin adjustment (`tight_layout`), rotating labels, manual placement.
- If the user asks for the sample size, write "(n=2,220)" at the top right in 12pt. Do not add it to scatter plots. Move it if it overlaps other elements.

## Per-chart specifications

- (Horizontal bar) Use for item comparison. Categories on the Y axis, values as labels at the bar ends, left spine only.
- (Vertical bar) Recommended for time series. Categories on the X axis, values as labels above the bars, bottom spine only.
- (Line) Time points on the X axis and values on the Y axis, with the Y axis label shown. Keep the left and bottom spines.
- (Scatter) Keep the left and bottom spines. Point labels use "name\n(x, y)".
- (Bubble) Keep all four spines. Distinguish Y axis items with the category lightness steps in visual.md. Bubble area (matplotlib `s`) defaults to 10 times the value, adjusted to the data range. Write X axis labels as "category\n(column total)" and write the value inside each bubble. Mark cells with a value of 0 with ▽.
- (Heatmap) Keep all four spines. Show values as the density of a single navy family from #EDF1F8 to #2C466D. Choose the text color of cell values with the contrast rule in visual.md. Do not include a colorbar by default.
- (Pie) Use 6 slices or fewer, start at 12 o'clock, and place the largest values first going clockwise. Slice colors follow the category rule in visual.md, and slice boundaries are white lines (2px). Put labels inside slices as "name\n(00%)" and use no leader lines.

## When using matplotlib

- At the start of a session, check the installed matplotlib version and whether the font is installed, in code. If the user allowed web search, check the changes in the installed version (added and deprecated features).
- Install adjustText if missing, and NanumGothic if missing.
- Put settings at the top of the code so matplotlib's default colors and spines are not used as is.

```python
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager

FONT_PATH = Path("NanumGothic-Bold.ttf")  # location of the installed font file
COLOR_TEXT = "#1A1A1A"
COLOR_SUB = "#595959"
COLOR_DATA = "#6B8EC2"
COLOR_ACCENT = "#C0392B"
FONT_SIZE = 16

font_manager.fontManager.addfont(str(FONT_PATH))
plt.rcParams["font.family"] = font_manager.FontProperties(fname=str(FONT_PATH)).get_name()
plt.rcParams["font.weight"] = "bold"
plt.rcParams["font.size"] = FONT_SIZE
plt.rcParams["axes.unicode_minus"] = False  # keeps the minus sign from breaking with Korean fonts

labels = ["Sales Team 4", "Sales Team 3", "Sales Team 2", "Sales Team 1"]  # ascending input draws descending from the top
values = [410, 650, 720, 850]
colors = [COLOR_ACCENT if name == "Sales Team 1" else COLOR_DATA for name in labels]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(labels, values, color=colors)
ax.bar_label(bars, padding=6, color=COLOR_TEXT)
for side in ("top", "right", "bottom"):
    ax.spines[side].set_visible(False)
ax.spines["left"].set_color(COLOR_SUB)
ax.xaxis.set_visible(False)
ax.tick_params(axis="y", length=0)
fig.tight_layout()
fig.savefig("chart.png", dpi=200)
```

- For pie charts, `ax.pie(values, startangle=90, counterclock=False)` gives a clockwise layout from 12 o'clock. matplotlib pie charts run counterclockwise by default.

## Checklist

- Did you fix the message first and choose the form that fits the comparison type?
- Is the accent color on the one message target only?
- Are data labels shown directly according to the criteria?
- Are spines, grids, and legends set as specified?
- Do axis labels include units?
- Does the value axis of bar charts start at zero?
- Do the numbers in the chart match the source data?

## References

- Gene Zelazny, Say It With Charts (Korean edition titled "맥킨지, 차트의 기술"). Source of choosing charts in the order message, comparison type, chart form.
- Gene Zelazny, Say It With Presentations (Korean edition titled "맥킨지, 발표의 기술"). Source of the principle of one message per visual.
- Statistics Canada, Pie chart (https://www150.statcan.gc.ca/n1/edu/power-pouvoir/ch9/pie-secteurs/5214826-eng.htm). Basis for pie charts with 6 slices or fewer, starting at 12 o'clock, largest first clockwise.
- W3C, Understanding Success Criterion 1.4.11 Non-text Contrast (https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html). Basis for the 3:1 contrast of graphical objects.
