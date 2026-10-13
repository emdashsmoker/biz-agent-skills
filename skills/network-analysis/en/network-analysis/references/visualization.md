# Visualization Rules

> Translated from the Korean edition. Wording may differ from the original intent.

Covers colors, fonts, function choice, layout and file saving for charts. Color and size values live in the constants at the top of `scripts/nx_toolkit.py`.

## Principles

- (Color) Use pastel blue by default and pastel orange only for elements that need emphasis.
- (Font) Use NanumGothic so Korean text renders, and set labels in bold.
- (Minimal decoration) Hide the axes on graph drawings and remove the top and right borders on bar charts. Do not use shadows, 3D effects or decorative gradients.
- (Labels) Name every node and print values on bars.
- (Category colors) Group colors follow a 10-color palette in order. Colors become hard to tell apart beyond 5 groups, so consider a block-level reduced graph.

## Palette

| Name | Value | Use |
|---|---|---|
| primary | #8FB8D4 | Default node fill |
| primary_edge | #5783A8 | Node border |
| primary_deep | #6B9BBD | Curves and emphasis lines |
| primary_light | #B8D1E2 | Area fill |
| accent | #E5A785 | Highlighted nodes, block borders, thresholds |
| neutral | #7A95A8 | Lines |
| muted | #8FA3B3 | Heatmap grid |

- (Group colors) #8FB8D4, #A5CDB5, #EDC491, #CFB0CF, #B8B8B8, #9FC7CF, #E5B5B5, #C0CBA5, #D6C7A5, #B8ADC8
- (Heatmap and centrality gradient) Five steps of pastel blue from white to #7DAECC
- (Centrality comparison bars) Degree #4A90B8, closeness #6DB39A, betweenness #E0A75C

## Font setup

`setup_font()` registers NanumGothic Regular and Bold. Drawing functions run it once on their own if it has not been called. Without the font, it falls back to DejaVu Sans and warns. Korean text then shows as boxes, so install the `fonts-nanum` package and draw again. In a disposable sandbox that allows installs, `setup_font(install_if_missing=True)` also installs the font.

## Choosing a function

For 30 nodes or fewer, use `draw_matrix_and_network` by default. It draws the matrix heatmap and the network graph and also returns the matrix as a Markdown table.

| Argument | Use |
|---|---|
| `centrality_dict` | Scales node size and color depth with centrality |
| `group_dict` | Colors nodes by group, reorders the matrix by group and draws orange lines at group borders |
| `split_files` | True (default) saves the matrix and the graph as two files. False saves one side-by-side file |
| `save_path` | Output path. With split_files=True it creates `name_matrix.png`, `name_network.png` and `name_matrix.md` |

The two-file default lets narrow screens such as phones show each image large.

Graph-only functions are for networks above 30 nodes, for requests that ask for the graph alone, or for an extra view added after the default chart. Calling them on 30 nodes or fewer prints a warning.

| Function | Chart |
|---|---|
| `draw_basic_network` | Plain graph |
| `draw_centrality_network` | Graph with size and color by centrality |
| `draw_grouped_network` | Graph colored by group |
| `draw_centrality_comparison` | Bars of the three centralities for the top nodes by betweenness |
| `draw_k_core_nesting` | Nodes grow larger and darker with core number |
| `draw_matrix_heatmap` | Matrix heatmap alone |
| `draw_bipartite_network` | Two-mode graph of people (circles) and activities (squares) |
| `draw_uzzi_paradox` | Schematic inverted U between embeddedness and performance |

## Default chart by analysis

- (Centrality) `draw_matrix_and_network(G, centrality_dict=...)` draws central nodes larger and darker.
- (Blockmodeling) `draw_matrix_and_network(G, group_dict=blocks.to_dict())` draws the matrix reordered by block and a graph colored by block.
- (Subgroups) Pass clique, k-core or component membership as `group_dict`. When a node belongs to several cliques, pass one representative membership and show the rest in the `clique_membership` table.
- (Directed graphs) Show arrows.

## Tables by size

- For 30 nodes or fewer, `matrix_to_markdown(G)` turns the whole matrix into a table.
- For 31 to 50 nodes, raise `max_size` to show the whole block-ordered matrix, for example `matrix_to_markdown(G, reorder_by=blocks.to_dict(), max_size=50)`. With the default, it excerpts the top 30 nodes by degree and says so in the caption.
- Above 50 nodes, show the density table between blocks with `blocks_summary_markdown(G, blocks)` and create the full data file with `export_to_csv`.
- The matrix heatmap prints numbers in cells only up to 20 nodes. Weighted graphs show one decimal place.

## Layout

| Layout | Suited to | Function |
|---|---|---|
| spring | General networks, default | `nx.spring_layout` |
| circular | Ring structures, symmetry | `nx.circular_layout` |
| kamada_kawai | When drawn distance should follow path distance | `nx.kamada_kawai_layout` |
| shell | Concentric layers | `nx.shell_layout` |
| bipartite | Two-mode networks | `draw_bipartite_network` places the sets left and right |

The spring layout fixes the seed at 42, so the same data gives the same placement.

## Saving files

- Save files with descriptive names in an output folder your environment can deliver to the user, for example `outputs/`. Missing folders are created.
- Resolution is 150 DPI. For print, change `SAVE_DPI` to 300.
- Backgrounds are saved white.
- Default sizes are 10x8 inches for graphs, 10x6 inches for bar charts and 15x7 inches for side-by-side images. In split mode, the matrix is a square of 6 to 10 inches by node count and the graph is 8 to 12 inches wide.
- After saving, confirm the file exists and deliver it with the file delivery feature. Keep image Markdown syntax out of the answer body.

## Overlapping labels

When many nodes make labels overlap, the `adjustText` package can move them. Skip this step if the package is not installed.

```python
try:
    from adjustText import adjust_text

    def draw_adjusted_labels(G, pos, ax):
        texts = [ax.text(x, y, str(n), fontsize=10, fontweight="bold")
                 for n, (x, y) in pos.items()]
        adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle="-", color="gray", lw=0.5))
except ImportError:
    draw_adjusted_labels = None
```

Call this function in place of `nx.draw_networkx_labels`.

## Checking the charts

Open each image before delivering it and check:

- No text is cut off or shown as boxes.
- Labels, nodes and legends do not overlap.
- Matrix values and graph lines match the input data.
- Group colors and legend entries match one to one.
