# Data Input, Output and Scale

> Translated from the Korean edition. Wording may differ from the original intent.

Covers how to load networks from files, how to plan the analysis by network size, and how to exchange files with other analysis tools.

## Input formats

| Format | Function | File layout |
|---|---|---|
| CSV edge list | `load_from_csv(path, format="edges")` | `source,target,weight` |
| CSV adjacency matrix | `load_from_csv(path, format="matrix")` | Square matrix with node names in the first column |
| CSV incidence matrix | `load_from_csv(path, format="incidence")` | Rows are people, columns are activities |
| Excel | `load_from_excel(path, sheet_name=0, format=...)` | One of the layouts above |
| Auto-detection | `load_from_csv(path)` | Rules below |

Without `format`, the layout is guessed in this order:

- 3 or fewer columns means an edge list.
- Equal numbers of rows and columns, or a name column followed by a square matrix, means an adjacency matrix.
- Anything else is read as an incidence matrix.

A matrix with 3 or fewer nodes can be mistaken for an edge list because of its column count, so pass `format` explicitly.

Other options:

- (Direction) `directed=True` builds a directed graph.
- (Weights) With `weighted=True`, the third column of an edge list or the matrix cell values are stored in the `weight` attribute. Without it, every value other than 0 counts as a tie of 1.
- (Incidence matrix) The return value is a dict. Take the three graphs out with the keys `"bipartite"`, `"people_projection"` and `"activity_projection"`.

### Edge list example

```
source,target,weight
Alice,Bob,3
Alice,Carol,2
Bob,Carol,4
```

```python
G = load_from_csv("network.csv", format="edges", weighted=True)
```

### Adjacency matrix example

```
,A,B,C,D
A,0,1,1,0
B,1,0,0,1
C,1,0,0,1
D,0,1,1,0
```

```python
G = load_from_csv("matrix.csv", format="matrix")
```

### Text encoding

- The default encoding is utf-8.
- When non-ASCII text breaks, pass `encoding="utf-8-sig"` or, for Korean text, `encoding="cp949"`.
- Export with `export_to_csv(G, path)`. Its default utf-8-sig encoding opens cleanly in Excel.

## Strategy by size

`recommend_strategy(G)` recommends an analysis and visualization approach by node count. Read the `strategy`, `visualization`, `algorithms` and `warnings` keys of the result.

| Nodes | strategy | Visualization | Algorithms |
|---|---|---|---|
| 1 to 30 | full | Matrix and graph together | All algorithms usable |
| 31 to 100 | filtered | Draw the top K nodes | REGE and hierarchical clustering take longer |
| 101 to 500 | aggregated | Block-level reduced graph | Louvain instead of CONCOR |
| 501 or more | summary_only | Summary tables and distribution charts only | Louvain or Label Propagation |

How much of a table to put in the answer body follows the visualization table in SKILL.md (thresholds at 30 and 50 nodes).

## Functions for large networks

```python
G_top = sample_top_k_nodes(G, k=30, by="betweenness")   # degree, closeness, pagerank also work
G_dense = extract_core_subgraph(G, min_degree=3)         # drop points with degree below 3 (one pass)
communities = louvain_communities(G)                     # community number per point
G_reduced = aggregate_to_blocks(G, communities)          # points are blocks, weight = lines between blocks
stats = summary_statistics_only(G)                       # node count, density, components, degree distribution
print(blocks_summary_markdown(G, communities))           # density table between blocks
export_to_csv(G, "outputs/full_matrix.csv", format="matrix")  # full data for sharing
```

`extract_core_subgraph` filters once on the original degrees. When the remaining points must meet the threshold among themselves, use `find_k_cores`.

### CONCOR and Louvain

| Aspect | CONCOR | Louvain |
|---|---|---|
| Principle | Split in two by repeated correlation | Merge communities to raise modularity |
| What it finds | Positions with the same relation pattern (structural equivalence) | Groups dense on the inside |
| Cost | Repeats calculations on a matrix of size nodes squared | Fast on large graphs |
| Reproducibility | Same input, same result | Uses random order, so fix the seed for the same result (default seed 42) |

The two methods look for different things. If size forced a switch to Louvain, say in the interpretation that the result shows groups that are dense on the inside and may differ from positions based on structural equivalence.

## Exchanging files with other tools

| Tool | Extension | Export | Import |
|---|---|---|---|
| Pajek | .net | `export_to_pajek(G, path)` | `import_from_pajek(path)` |
| Gephi | .gexf | `export_to_gephi(G, path)` | `import_from_gephi(path)` |
| yEd and other GraphML tools | .graphml | `export_to_graphml(G, path)` | `import_from_graphml(path)` |
| UCINET | .dl | `export_to_ucinet_dl(G, path, format=...)` | `import_from_ucinet_dl(path)` |
| Spreadsheets | .csv | `export_to_csv(G, path)` | `load_from_csv(path)` |

### UCINET DL format

Export supports two layouts with labels inside the data (LABELS EMBEDDED). Labels that contain spaces raise an error.

```python
export_to_ucinet_dl(G, "output.dl", format="fullmatrix")
export_to_ucinet_dl(G, "output.dl", format="edgelist1")
```

FULLMATRIX output

```
DL N=4
FORMAT = FULLMATRIX
LABELS EMBEDDED
DATA:
 A B C D
A 0 1 1 0
B 1 0 0 1
C 1 0 0 1
D 0 1 1 0
```

EDGELIST1 output

```
DL N=3
FORMAT = EDGELIST1
LABELS EMBEDDED
DATA:
A B 1
B C 2.5
```

Import follows these rules:

- FULLMATRIX is read as undirected when the matrix is symmetric and as directed when it is not.
- EDGELIST layouts are read as undirected. For directed data, call `import_from_ucinet_dl(path, directed=True)`.
- Values other than 0 and 1 are kept as weights.

> UCINET 6 for Windows User's Guide(https://pages.uoregon.edu/vburris/hc431/Ucinet_Guide.pdf)

### What each format holds

- (Pajek NET) Simple structure that stores direction and weights.
- (Gephi GEXF) Stores visual attributes and networks that change over time.
- (GraphML) XML-based, read by many tools, stores node and line attributes freely.
- (UCINET DL) Use it to reload existing research data analyzed in UCINET.

## Practical cases

### Survey results in Excel

```python
G = load_from_excel("survey_result.xlsx", format="edges", weighted=True)
cent = compute_centralities(G)
```

### Collaboration across departments of a large organization

```python
G = load_from_csv("dept_collab.csv")
plan = recommend_strategy(G)                 # "aggregated" for 500 departments
communities = louvain_communities(G)
G_reduced = aggregate_to_blocks(G, communities)
draw_grouped_network(G_reduced, {n: n for n in G_reduced.nodes()},
                     save_path="outputs/dept_blocks.png")
```

### Reanalyzing existing UCINET data

```python
G = import_from_ucinet_dl("published_study.dl")
rege = regular_equivalence(G)
holes = compute_structural_holes(G)
export_to_gephi(G, "outputs/for_gephi.gexf")
```
