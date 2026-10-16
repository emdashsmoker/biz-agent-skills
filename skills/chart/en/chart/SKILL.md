---
name: chart
description: Builds static charts for reports and presentation slides with matplotlib. Settles the message first, picks the chart form that fits the comparison type (horizontal bar, vertical bar, line, scatter, bubble, heatmap, pie, stacked bar), gets approval on an ASCII chart plan, then renders. Runs every calculation in code and saves chart settings to a JSON file so the same chart can be rebuilt. Use this skill whenever the user says "/chart", "make a chart", "draw a graph", "bar chart", "pie chart", "line chart", "trend chart", "scatter plot", "bubble chart", "heatmap", "chart for a report", "chart for slides", "chart from Excel data", or hands over a table, CSV, Excel, or JSON data and asks for a visualization.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Chart Builder

> This English version is translated from the Korean original. It may not behave exactly as the original intends.

Build static charts for reports and presentation slides with matplotlib. The user picks data by cell range, as in a spreadsheet, and checks an ASCII chart plan before anything renders. Finished charts are edited by element ID and reloaded from a settings file.

## Working principles

- (Reproducibility) The same input produces the same chart. State colors as HEX codes, and save and load every setting through a JSON file.
- (Transparency) Show the code that built the chart and the reason for the chosen chart form.
- (Consistency) Use the same question order and the same response format in every session.
- (Convenience) Select data by cell range (A1:B10) and edit the chart by element ID.

## Numbers and data

Run Python code for every calculation, including totals, shares, averages, sorting, and ranks. A language model can get arithmetic wrong, so values the model computes by itself never go into the plan, the labels, or the chart.

- Use only the data the user provides. Do not make up data.
- Render only after the user approves the chart plan. Skip approval only when the user asks for one-shot mode.
- If the environment cannot run code, give the user the full code to run themselves.

## Environment setup

At the start of a session, prepare the environment in this order. Finish installing dependencies before any other work.

1. Check whether code can run, which matplotlib version is installed, and which fonts are installed. matplotlib 3.4 or later is required, since that release added bar_label.
2. If web search is available, search "matplotlib {version} changelog" and give the user a short note on new features, deprecations, and caveats. If web search is not available, report the installed version only and watch for MatplotlibDeprecationWarning during rendering.
3. Install adjustText if it is missing. Install pandas and openpyxl as well if they are missing, since they read CSV and Excel input.
4. If NanumGothic is missing, download the font files and register them with matplotlib. Registration applies only to the running process, so put the registration code at the top of every rendering script.

```bash
pip install adjustText pandas openpyxl
curl -L -O https://raw.githubusercontent.com/google/fonts/main/ofl/nanumgothic/NanumGothic-Regular.ttf
curl -L -O https://raw.githubusercontent.com/google/fonts/main/ofl/nanumgothic/NanumGothic-Bold.ttf
```

```python
from matplotlib import font_manager, rcParams

for path in ["NanumGothic-Regular.ttf", "NanumGothic-Bold.ttf"]:
    font_manager.fontManager.addfont(path)
rcParams.update({
    "font.family": "NanumGothic",
    "font.size": 16,
    "font.weight": "bold",
    "axes.labelweight": "bold",
    "axes.titleweight": "bold",
    "axes.unicode_minus": False,  # NanumGothic has no Unicode minus glyph, so negative signs break
})
```

## Workflow

There are two modes.

- (Step-by-step mode) The default. Go through data input, chart form, data cleanup, plan approval, rendering, and saving settings, in that order. Use it for fine adjustments.
- (One-shot mode) Use it when the request contains "skip plan" or "generate now". Pick the chart form, apply the data cleanup proposals, and render without a plan check. Show the code, the reason for the chart form, and the cleanup you applied along with the chart.

### 1. Data input

Read text, CSV, Excel, or JSON input, show it as a table with column letters and row numbers, and ask which range to use.

```
|   | A           | B       |
|---|-------------|---------|
| 1 | Company     | Revenue |
| 2 | Alpha Co.   | 150     |
| 3 | Beta Co.    | 120     |

Range: A2:B3 or all
```

Once the range is set, classify each column as time series, categorical, or numeric. From the request, find out whether the user named a chart type, which item to highlight, and any color preference.

### 2. Chart form

Settle the one message the chart must deliver, decide which comparison type that message needs, then pick the chart form. If the user did not name a chart type, ask: "Would you like to choose the chart type yourself, or should I recommend one?" If the user wants a recommendation, compute the data in Python, identify the comparison type with the table below, and propose a chart with the reason.

| Comparison type | Words in the request | Recommended chart |
|---|---|---|
| Component | share, proportion, % | Pie, stacked bar |
| Item | bigger, rank | Horizontal bar |
| Time series | change, trend | Vertical bar, line |
| Correlation | correlation, relationship | Scatter |
| Matrix | map, matrix, correlation matrix | Bubble, heatmap |

### 3. Data cleanup

- Sort data other than time series in descending order of value.
- With more than 5 categories, propose keeping the top 5 and grouping the rest as "Other". With exactly 6 categories, keep the top 4 so that Other holds at least 2 items. Put Other last whatever its value.
- With more than 12 time periods, propose using the latest 12 only.
- In step-by-step mode, put these proposals in the chart plan for approval.

### 4. Chart plan

Draw the preview in ASCII characters only until the user approves. Changes before rendering cost less. When the user approves with "y", run matplotlib.

````
## Chart plan
Type: horizontal bar | Reason: item comparison | n=2,220 (sum of values, computed in Python)

[Preview]
(A) ████████████████████ Sales 1  850
(B) █████████████████░░░ Sales 2  720
(C) ███████████████░░░░░ Sales 3  650

[Code]
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(["Sales 1", "Sales 2", "Sales 3"], [850, 720, 650], color="#6B8EC2")
ax.invert_yaxis()
ax.bar_label(bars, padding=3)
# hide value axis, set spines, etc.
```

[Settings] Category: axis | Value: label | Spine: left | Title: OFF | n: OFF | Decimals: 0
Edit: "highlight A", "title XXX", "show n", etc. | Proceed: "y"
````

- Preview bar length: the largest value gets 20 cells and the rest scale in proportion, computed in Python.
- (A), (B), (C) are element IDs. Edit commands use them to point at elements.
- For charts other than bars, show element ID, item, and value as an ASCII table.

> (n) The number of respondents or samples behind the chart values

> (Spine) The border lines on the four sides of the plot area

### 5. Rendering

After approval, render according to the visual spec. Open the rendered image yourself and check the items below. If you find a defect, fix the code and render again. Deliver the chart only when no defect remains. If the environment cannot show you the image, tell the user the chart was not checked.

- (Clipping and overlap) Labels and axis text are not cut off at the figure edge and do not overlap.
- (Legibility) Data labels have enough font size and contrast against their background.
- (Accuracy) Label values match the values computed in Python.
- (Spec) Spines, grid, and colors match the per-chart spec.
- (Spacing) Gaps between elements are even and the figure edges have enough margin.

Also fix anything that would look odd to a practitioner putting this chart in a report, even if the list above does not cover it.

If labels overlap, apply these fixes in order.

1. Let adjustText move labels. For scatter and line charts, pass the point coordinates as well (adjust_text(texts, x=xs, y=ys, ax=ax)) so labels do not cover points.
2. Change the bar_label padding to adjust the gap between bar and label.
3. Recompute margins with tight_layout.
4. Rotate the labels.
5. Set label coordinates by hand.

### 6. Saving settings

After rendering, ask: "Saving the current settings lets you rebuild this chart later. Save now? (y/n)". If the user agrees, save as chart_config_YYYYMMDD_HHMMSS.json. The file layout follows the Settings file section.

## Edit commands

When the user types `/?`, show this table.

| Command | Action |
|---|---|
| /? | Show help |
| /new | Start a new chart |
| /save | Save current settings |
| /load | Load saved settings |
| y | Approve the chart plan |
| highlight A | Paint element A in the highlight color |
| B color red | Change the color of element B |
| A,B to Other | Group elements A and B into Other |
| title XXX | Set the title to XXX |
| show n | Turn on the n label |

On "show n", ask for a description to show with n (for example, all respondents). After a change that affects the whole chart, confirm it with an updated chart plan and offer to save settings.

Every element can be adjusted by element ID. Adjustable items:

- (On and off) title, data labels, axes, grid, legend, spines, n label, colorbar
- (Values) colors, font, figure size, axis range, title text, n description, bubble size ratio, decimals
- (Label format) value, percent, value+percent, value+rank
- (Orientation) switch between horizontal and vertical bars

> (Colorbar) A bar-shaped legend that maps heatmap color intensity to values

## Visual spec

### Colors and font

```python
COLORS = {
    "primary": "#6B8EC2",    # primary color
    "highlight": "#F5A962",  # highlight color
    "pastel": ["#A8C5E2", "#B8D4A8", "#F5D5A8", "#E8B8C2", "#C4C4C4", "#D4C4E8"],
}
DARK_TEXT = "#1A1A1A"
FONT = {"family": "NanumGothic", "size": 16, "weight": "bold"}
```

- Set all text in bold.
- Paint elements in the primary color. Use the highlight color only for elements the user asks to highlight.
- When each item needs its own color, as in pie, stacked bar, and bubble charts, use the pastel palette in order. Write text on pastel colors in DARK_TEXT so black text stays readable.

### Default layout

- (Shown) Categories on the axis and values as data labels, both in bold. The title is off by default.
- (Off by default) grid, legend, spines not listed in the chart spec, pie leader lines, colorbar
- (Figure size) figsize=(10, 6) by default.
- (n label) Off by default. When on, write "(n=2,220)" at 12pt in the top right of the figure. If there is a description, append it as in "(n=2,220, all respondents)". Move it if it overlaps other elements. n defaults to the sum of the values in the selected range. If the user gives a value, use that value.

> (Leader line) A line that connects a pie slice to a label placed outside it

### Chart spec

- (Horizontal bar) Keep only the left spine. Put categories on the Y axis and values as labels at the bar ends, and hide the value axis. Put the largest bar at the top (ax.invert_yaxis). Use it for item comparison.
- (Vertical bar) Keep only the bottom spine. Put categories on the X axis and values as labels above the bars, and hide the value axis. Recommended for time series.
- (Line) Keep the left and bottom spines. Put categories on the X axis. Show Y axis tick values and the Y axis title. Add a data label to every point.
- (Scatter) Keep the left and bottom spines. Label each point as "name\n(x, y)". Do not show the n label.
- (Bubble) Keep all four spines. Bubble size shows the value where an X category meets a Y item, and the value is written inside the bubble. Give each Y item the next pastel palette color. Write X axis labels as "category\n(column total)". Draw ▽ instead of a bubble where the value is 0.
- (Heatmap) Keep all four spines. Shade cells with a single color scale from white (#FFFFFF) to the primary color, and write the value in each cell. The colorbar is off by default.
- (Pie) Use 6 slices or fewer. Start at 12 o'clock and go clockwise (startangle=90, counterclock=False) with the pastel palette. Write labels as "name\n(00%)" inside the slices (labeldistance=0.6). Leader lines are off by default.
- (Stacked bar) Follow the spine and axis rules of the vertical or horizontal bar, depending on orientation. Color segments with the pastel palette in order and write a "name\n(value)" label at the center of each segment.

Bubble size and heatmap text color come from these calculations.

- (Bubble size) The smallest value above 0 gets a bubble area of 300pt². The largest value gets that area times the size ratio (default 10). Values in between get an area scaled linearly between the two.
- (Heatmap text color) Compute the contrast ratio of the cell color against DARK_TEXT and against white, and use whichever is higher. The contrast ratio is (L1 + 0.05) / (L2 + 0.05) with relative luminance from the WCAG 2 formula.

```python
size = s_min + (v - v_min) / (v_max - v_min) * (s_min * ratio - s_min)
```

### Label formats

| Format | Example |
|---|---|
| Value | 850 |
| Percent | 38% |
| Value+percent | 850(38%) |
| Value+rank | 850(#1) |

- The percent denominator is the sum of the values in the selected range.
- Decimals default to 0. The user can change them to 1 or 2 in the plan settings.

## Settings file

Within a session, keep the current dataset, the settings the user chose, and the history of charts made so far. Save settings that must outlive the session to the settings file, which holds every adjustable item.

```json
{
  "metadata": {"created": "2026-01-15T09:30:00+09:00", "matplotlib_version": "3.10.0"},
  "input": {"file_path": "data.xlsx", "sheet": "Sheet1", "range": "A1:B4"},
  "data": {
    "labels": ["Sales 1", "Sales 2", "Sales 3"],
    "values": [850, 720, 650],
    "element_ids": {"A": "Sales 1", "B": "Sales 2", "C": "Sales 3"}
  },
  "style": {
    "chart_type": "barh",
    "colors": {"A": "#F5A962", "B": "#6B8EC2", "C": "#6B8EC2"},
    "font": {"family": "NanumGothic", "size": 16, "weight": "bold"},
    "label_format": "value",
    "decimals": 0,
    "bubble": {"min_size": 300, "ratio": 10}
  },
  "visibility": {
    "title": false,
    "data_label": true,
    "axis": true,
    "grid": false,
    "legend": false,
    "spines": ["left"],
    "n_display": false,
    "colorbar": false
  },
  "n_display": {"value": 2220, "text": "all respondents", "fontsize": 12},
  "layout": {
    "figsize": [10, 6],
    "title_text": "",
    "axis_range": {"x": null, "y": null},
    "margin": {"left": null, "right": null, "top": null, "bottom": null}
  }
}
```

- (chart_type) One of barh, bar, line, scatter, bubble, heatmap, pie, stacked_bar, stacked_barh
- (label_format) One of value, percent, value+percent, value+rank, in the same order as the label format table
- (data) For multiple series or matrix data, store values as a 2D list and keep row and column names in labels
- (visibility.axis) true shows axes as the chart spec says, false hides all axes
- (visibility.spines) The spines to keep, chosen from left, right, top, bottom
- (layout.axis_range) null means automatic range, [min, max] means a fixed range
- (layout.margin) null means tight_layout, values between 0 and 1 go straight to subplots_adjust

When the user loads a settings file with `/load`, handle it in this order.

1. Show the creation time, the matplotlib version, and the main settings.
2. Check that the source file at input.file_path exists. If it does not, warn the user and use the data values stored in the settings file.
3. If the installed matplotlib version differs from metadata, warn the user and ask: "Regenerate the chart? (y/n)".

## Reference

The selection steps (message, then comparison type, then chart form) and the component, item, time series, and correlation comparison types follow Zelazny's book. The matrix type was added for cross-tabulated data.

> Gene Zelazny(2001), Say It With Charts: The Executive's Guide to Visual Communication, 4th ed., McGraw-Hill
