---
name: network-analysis
description: "Social network analysis (SNA) with NetworkX code and charts. Computes density, centrality, centralization, structural holes, components, cliques, k-cores, structural equivalence, blockmodeling (CONCOR, REGE), paths and two-mode networks from matrices, edge lists, CSV, Excel, UCINET, Pajek or Gephi files. Use it whenever the user mentions network analysis, SNA, centrality, betweenness, structural holes, blockmodeling, cliques, adjacency matrix, edge list, ego network, brokers, embeddedness, NetworkX, UCINET or Gephi, or shares relationship data and asks for analysis or a chart. Compute every number with scripts/nx_toolkit.py. Read as needed: references/data_io.md (files, scale), references/graph_theory.md (paths, degree), references/cohesion_subgroups.md (density, subgroups), references/centrality.md, references/equivalence.md (blockmodeling), references/concepts_theory.md (theory), references/visualization.md (charts). Structure answers with assets/report_template.md."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Social Network Analysis

> This English edition was translated from the Korean edition of this skill. Some wording may not carry the original intent exactly, and the skill may behave differently from the Korean edition.

Turn relationship data into a graph, compute the measures, and present the matrix, the charts and the interpretation together. Every number comes from running `scripts/nx_toolkit.py`. Numbers written from mental arithmetic or estimation cannot be reproduced from the same data.

## Setup

Check the environment once before the first analysis.

- Python 3 with `networkx` (3.x), `pandas`, `numpy`, `scipy` and `matplotlib`. Reading Excel files also needs `openpyxl`.
- Add the skill's `scripts` folder to `sys.path` and import with `from nx_toolkit import *`.
- `LANG` sets the language of table columns, captions and chart text. This edition sets it to `"en"`.
- Labels in Latin script render with the default font. Korean node names need the NanumGothic font. Call `setup_font()` at the top of the code. In a disposable sandbox that allows system package installs, `setup_font(install_if_missing=True)` installs the font. Elsewhere, ask the user to install the `fonts-nanum` package.

```python
import sys
sys.path.insert(0, "<skill folder>/scripts")
from nx_toolkit import *
setup_font()
```

## Workflow

Handle every request in this order: load, interpret, choose references, compute, visualize, report.

### 1. Load the data

When the user provides a file, read it with the matching function. Do not ask the user to retype the data as a Python list.

| Input | Function |
|---|---|
| CSV edge list | `load_from_csv(path, format="edges")` |
| CSV adjacency matrix | `load_from_csv(path, format="matrix")` |
| CSV incidence matrix | `load_from_csv(path, format="incidence")` |
| Excel | `load_from_excel(path, sheet_name=0)` |
| UCINET DL | `import_from_ucinet_dl(path)` |
| Pajek NET | `import_from_pajek(path)` |
| Gephi GEXF | `import_from_gephi(path)` |
| Matrix typed in the chat | `load_from_matrix(matrix, labels=[...])` |
| List of relations typed in the chat | `load_from_edges(edges)` |

Format auto-detection rules and encoding options are in `references/data_io.md`. Right after loading, call `recommend_strategy(G)` to see the size-based strategy.

### 2. Interpret the request

Identify the following in the request.

- (Data) Was a matrix, a list of relations or a description of relations given?
- (Question) Which measure or technique does the user want?
- (Purpose) Concept learning, an exercise, or a practical diagnosis?

When the user asks about a concept without data, build a virtual network of 5 to 10 nodes for the demonstration and say that the data is virtual.

### 3. Choose references

Read only the documents the question needs. A request about one technique needs one document. A request that combines techniques needs two or three.

| Question keywords | Document |
|---|---|
| file loading, CSV, Excel, large data, UCINET, Pajek, Gephi | `references/data_io.md` |
| walk, path, cycle, distance, diameter, degree, indegree, outdegree, matrix | `references/graph_theory.md` |
| density, structural holes, social capital, components, cliques, k-core, n-clique | `references/cohesion_subgroups.md` |
| centrality, centralization, PageRank | `references/centrality.md` |
| structural equivalence, blockmodeling, CONCOR, REGE, image matrix | `references/equivalence.md` |
| relation types, strong and weak ties, organizational roles, embeddedness, Uzzi paradox | `references/concepts_theory.md` |
| charts, matrix heatmap, layout, colors | `references/visualization.md` |

### 4. Compute

Run the code to get every value. Do not infer results from formulas. The most used functions are:

- (Basics) `describe_graph`, `compute_density`, `compute_degree_stats`, `compute_distances`
- (Centrality) `compute_centralities`, `compute_centralization`, `compute_extended_centralities`
- (Subgroups) `find_components`, `find_cut_points`, `find_k_cores`, `find_cliques`, `find_n_cliques`, `find_n_clans`, `find_n_clubs`
- (Structural holes) `compute_structural_holes`
- (Equivalence) `euclidean_equivalence`, `correlation_equivalence`, `regular_equivalence`, `blockmodel`, `image_matrix`

Results come back as pandas DataFrames or Series. Use `dataframe_to_markdown` to turn them into tables.

### 5. Visualize

Show charts and Markdown tables together. Pick the format by node count.

| Nodes | Matrix table | Results table | Chart |
|---|---|---|---|
| 30 or fewer | Full matrix | Full results | `draw_matrix_and_network`, matrix and graph together |
| 31 to 50 | Matrix reordered by block, or an excerpt of the top 30 nodes | Top 10, full table as CSV | Graph only |
| 51 or more | Density between blocks (`blocks_summary_markdown`), original as CSV | Top 10, full table as CSV | Block-level reduced graph |

For 30 nodes or fewer, use `draw_matrix_and_network` only. The matrix is the raw data and the graph is its reading. Showing both lets the reader check the result. Use graph-only functions such as `draw_basic_network`, `draw_centrality_network` and `draw_grouped_network` only in these cases:

- The network has more than 30 nodes and the matrix becomes unreadable.
- The user asks for the graph alone.
- You add another view after showing the `draw_matrix_and_network` output.

Standard code for 30 nodes or fewer:

```python
cent = compute_centralities(G)
result = draw_matrix_and_network(
    G, title="Sales division collaboration",
    centrality_dict=cent["betweenness_centrality"].to_dict(),
    save_path="outputs/sales_network.png",
)
print(build_response_block(G, "Sales division collaboration", result, cent))
```

`build_response_block` assembles the matrix table, the results table and the list of image files in one call. Copy the printed block into the answer. Send the image files separately with the file delivery feature of your environment. Color and layout rules are in `references/visualization.md`.

### 6. Report

Follow `assets/report_template.md`. It has templates for data analysis requests, concept questions and exercises. An analysis answer contains:

- The reading of the question and the techniques applied
- A Mermaid flowchart of the process
- Each technique's definition, LaTeX formula and Python code
- The input matrix table and the results table
- Image files (delivered separately)
- Conclusions and practical implications

## Checks before answering

Confirm the following before sending the answer. If an item is missing, fix it first.

- The input matrix Markdown table (`result["markdown"]` or the `build_response_block` output) is in the answer body.
- The results table (`dataframe_to_markdown` output) is in the answer body.
- The image files exist on disk and were sent with the file delivery feature.
- The answer body contains no `![alt](file.png)` image syntax.

The last check exists because most chat interfaces cannot display images from local file paths and leave a broken link. Write a short line such as "image files sent separately" instead. Do not mention files that failed to save.

## Calculation conventions

These conventions change the numbers, so state them when interpreting results.

- Degree centrality on a directed graph uses indegree plus outdegree and ranges from 0 to 2. Use the in-centrality and out-centrality columns to see each direction.
- Closeness centrality on a directed graph uses incoming distance. For outgoing distance, reverse the graph with `transpose_matrix(G)` and compute again.
- Closeness on a disconnected graph is scaled by the share of reachable nodes.
- CONCOR splits every block in two at each step, so set the number of blocks to a power of two: 2, 4, 8.
- `find_n_clubs` is an approximate search. Some n-clubs may be missing from its result.
- The curve and threshold in `draw_uzzi_paradox` are set for illustration.

## Questions about other tools

When the user asks how to use UCINET, Pajek or Gephi menus, show how to run the same analysis in NetworkX. If the results must move to one of those tools, write files with `export_to_ucinet_dl`, `export_to_pajek` or `export_to_gephi`.
