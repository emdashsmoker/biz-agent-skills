# Chart Rules

One chart carries one message. Write the message as one sentence first, decide what kind of comparison it makes, and then pick the chart form. The `--chart` option of each script draws a default chart that follows these rules.

## Choosing a Chart

| Comparison | Example message | Chart form |
|---|---|---|
| Component | A accounts for 40% of the total | Pie or stacked bar |
| Item | Region 2 has the highest LQ | Horizontal bar |
| Time series | Revenue grew steadily over five years | Vertical bar or line |
| Correlation | Larger investment goes with larger revenue | Scatter |
| Matrix | Distribution differs by industry and region | Heatmap or bubble |
| Change breakdown | Volume growth explains most of the revenue increase | Waterfall |

## Default Chart per Tool

| Script | Chart | Message |
|---|---|---|
| `cagr.py`, `deflate.py` | Vertical bar | Change in yearly values |
| `appraisal.py` | Vertical bar | Year when cumulative net PV turns positive |
| `ahp.py` | Horizontal bar | Ranking of criterion weights |
| `pl_summary.py` | Waterfall | Drivers of the change in operating profit |
| `capex.py` | Vertical bar | CAPEX by period |
| `bep.py` | Line | Volume where the revenue line meets the total cost line |
| `variance.py` | Waterfall | Size of price, mix and quantity effects |
| `io_impact.py` | Horizontal bar | Ranking of induced output by product group |
| `lq.py` | Horizontal bar | Ranking of LQ by region with a reference line at 1.0 |
| `hhi.py` | Horizontal bar | Ranking of firm shares |
| `market_size.py` | Horizontal bar | Size of TAM, SAM and SOM |

## Style

- (Color) Base data uses pastel navy #6B8EC2, emphasis and decreases use #F5A962, total bars use #4F6F9E, and items below a threshold use #BCC9E2. Multiple series use #4F6F9E, #6B8EC2, #93AAD3 and #BCC9E2 in that order. Put data labels and signs next to the colors so readers can follow the meaning without relying on color.
- (Font) Use NanumGothic bold at 14pt and make all text bold. Text color is #1A1A1A.
- (Background) Use white, with no shadows, gradients or 3D effects.
- (Title) Leave titles out of the chart. The message sentence serves as the chart title in the report text.
- (Axes and lines) Use no gridlines, legend or chart border. Horizontal bars keep only the left axis line, vertical bars and waterfalls keep only the bottom axis line, and line and scatter charts keep the left and bottom axis lines.
- (Labels) Show values as direct data labels. With more than 15 bars, label only the first, last, minimum, maximum and the point where values turn from negative to positive, which prevents overlap.
- (Order) Sort item comparisons in descending order with the largest value on top, and keep time series in time order.
- (Categories) In component charts with six or more categories, keep the top four or five and group the rest as "Other".

## Review

After saving a chart, open the image, check the items below, and redraw when something is wrong.

- Is any text cut off or outside the plot area?
- Do labels overlap bars or each other?
- Does any text render as broken glyphs?
- Are margins and spacing between elements even?
- Do the numbers in the chart match the result table?
- Is any element left that does not serve the message?

## Chart Forms Outside the Defaults

For pie, scatter, heatmap and other forms the scripts do not draw, write new matplotlib code that uses `PALETTE`, `SERIES_COLORS` and `apply_style()` from `scripts/chart.py` to keep the same style. When labels overlap, show fewer labels or use the adjustText package to move them.
