---
name: network-analysis-lite
description: "Social network analysis (SNA) with NetworkX. Reads adjacency matrices, edge lists, person by activity data, CSV, Excel, UCINET DL, Pajek, GEXF, GraphML or plain descriptions of relationships, and reports an input matrix table, a results table, a matrix figure and a network figure. Covers density, degree, closeness, betweenness, eigenvector, PageRank and Katz centrality, centralization, structural holes, components, cut-points, bridges, k-cores, cliques, n-cliques, n-clans, n-clubs, structural equivalence, CONCOR, REGE, blockmodels, Louvain communities, bipartite networks, paths and cycles, and explains weak ties, embeddedness and social capital. Use this skill whenever the user mentions network analysis, SNA, centrality, structural holes, blockmodeling, cliques, adjacency matrix, edge list, organizational or collaboration networks, stakeholder maps, NetworkX, UCINET, Pajek or Gephi, or gives relationship data between people, teams, organizations or countries. Functions live in scripts/sna_toolkit.py."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Social Network Analysis

> This English version was translated from the Korean original. It may behave differently from what the original intends.

Compute relationship data between people, teams, organizations, companies or countries with NetworkX and report the input matrix, the results table and the figures as one package. The computing and drawing functions live in `scripts/sna_toolkit.py`.

## Ground rules

- Take every reported number from `sna_toolkit.py` or a NetworkX run. Centrality, equivalence and centralization are easy to get wrong by hand, and only code lets a third party reproduce the result.
- Deliver the input matrix table, the results table and the figure files together. A figure alone gives the reader nothing to check the numbers against.
- Save figures as PNG files and hand them over with the environment's file-sharing feature. A local path written as `![](path.png)` shows up as a broken image in most chat interfaces.
- The figure functions check that the file was written and raise an error otherwise. If one fails, remove every mention of that figure from the answer.
- When the user provides a file, read the file directly. Do not ask the user to retype the data as a Python list.
- When the user asks about a concept without data, demonstrate it on a made-up network of 5-10 nodes and say in the results that the data is made up.

## Setup

Required packages are networkx, numpy, pandas, scipy and matplotlib. Excel input also needs openpyxl, and label overlap adjustment uses adjustText. Tested versions: NetworkX 3.6, pandas 3.0, numpy 2.4, scipy 1.17, matplotlib 3.10.

```bash
pip install networkx numpy pandas scipy matplotlib openpyxl adjustText
```

Where the system Python is protected, use a virtual environment or add `--break-system-packages`.

Korean, Chinese or Japanese labels need an installed CJK font such as NanumGothic or Noto Sans CJK. The script only looks for installed fonts and never installs one, because font installation needs administrator rights. Without a matching font it warns and falls back to the default font, and CJK characters may then appear as boxes.

```python
import sys
sys.path.insert(0, "<skill folder>/scripts")
from sna_toolkit import *
```

## Workflow

Handle each request in this order.

1. Read the input and build the graph
2. Decide direction and weights
3. Choose the handling for the network size
4. Compute with the functions that match the question
5. Draw the matrix figure and the network figure
6. Answer in the report format

### Reading input

| Input | Function | Note |
|---|---|---|
| Python matrix | `from_matrix(matrix, labels, directed, weighted)` | Diagonal (self-ties) ignored |
| Edge list | `from_edges(edges, directed, weighted)` | `(u, v)` or `(u, v, weight)` |
| Person by activity membership | `from_incidence(df or dict)` | Returns the bipartite graph and both projections |
| CSV, TSV, Excel | `load_table(path, fmt, directed, weighted)` | `fmt` detected automatically when omitted |
| UCINET DL | `read_ucinet_dl(path)`, `write_ucinet_dl(G, path)` | FULLMATRIX, EDGELIST1 |
| Pajek, GEXF, GraphML | `nx.read_pajek`, `nx.read_gexf`, `nx.read_graphml` | Save with `nx.write_*` |
| Save as table | `export_table(G, path, fmt)` | Edge list or matrix CSV |

- Automatic detection treats 3 or fewer columns as an edge list, a square table (optionally with a label column) as an adjacency matrix, and anything else as an incidence matrix.
- If a CSV saved from Excel shows garbled characters, set `encoding="utf-8-sig"` or the file's legacy encoding (for Korean, `encoding="cp949"`). `export_table` writes utf-8-sig so Excel displays non-Latin text correctly.
- Saving to Pajek, GEXF or GraphML lets the user continue in tools such as Gephi.

### Direction and weights

- If the user does not state direction, read a symmetric matrix as undirected and an asymmetric one as directed.
- If cells hold only 0 and 1, read the graph as binary. Any other value makes it weighted.
- Pass the decision through the `directed` and `weighted` arguments of the reading function and state it in one line of the analysis overview.

### Handling by size

`recommend_strategy(G)` returns the handling in the table below based on node count. The 30-node limit is a default set by how many matrix cells stay readable.

| Nodes | Strategy | Matrix in the answer | Results table | Figures |
|---|---|---|---|---|
| 30 or fewer | full | Full matrix | All nodes | Matrix figure, network figure |
| 31-100 | filtered | Top 30 nodes by degree | Top 10, full table as CSV | Network figure |
| 101-500 | aggregated | Block density table | Top 10, full table as CSV | Block-reduced graph |
| 501 or more | summary_only | Block density table | Summary statistics | Degree distribution |

- In the 31-100 range, if a blockmodel was run, the excerpted matrix can be reordered by block.
- From 101 nodes, split the network into blocks with `louvain` or `blockmodel` first, then build the block density table with `block_density` and the reduced graph with `reduce_to_blocks`.
- From 501 nodes, report with the `describe` and `degree_stats` summary tables and the `plot_degree_histogram` figure. At this size nodes and lines overlap and individual nodes cannot be read.
- REGE and hierarchical clustering grow at least with the square of the node count, so above 100 nodes tell the user about the expected run time first.

### Choosing functions

| Question | Functions |
|---|---|
| Size, density, isolates, diameter | `describe`, `valued_density`, `degree_stats` |
| Walks, paths, cycles, distances | `walks`, `paths`, `cycles`, `distances` |
| Node types in directed graphs | `directed_node_types` |
| Ego networks | `ego_network` |
| Centrality | `centralities`, `extended_centralities` |
| Centralization | `centralization` |
| Structural holes, brokerage | `structural_holes`, `openness` |
| Components, cut-points, bridges | `components`, `cutpoints`, `cycle_components` |
| Cohesive subgroups | `k_cores`, `m_slices`, `cliques`, `clique_membership`, `n_cliques`, `n_clans`, `n_clubs` |
| Equivalence, blockmodeling | `se_distance`, `se_correlation`, `rege_similarity`, `concor`, `blockmodel`, `block_density`, `image_matrix` |
| Large networks | `recommend_strategy`, `top_k_subgraph`, `core_subgraph`, `louvain`, `reduce_to_blocks` |
| Bipartite networks | `from_incidence`, `plot_bipartite` |
| Report output | `matrix_and_network`, `matrix_markdown`, `df_markdown`, `plot_centrality_bars`, `plot_degree_histogram`, `plot_uzzi_concept` |

## Measure definitions

In the formulas below, $g$ is the number of nodes, $L$ the number of lines, $d_i$ the degree of node $i$ and $d_{ij}$ the shortest distance between two nodes.

### Graph basics

| Concept | Definition |
|---|---|
| Walk | A sequence of moves that may repeat nodes and lines |
| Path | A sequence of moves that visits each node once |
| Cycle | A path that returns to its start, with 3 or more nodes in undirected graphs |
| Distance | Number of lines on the shortest path between two nodes |
| Diameter | Largest distance in the graph, between 1 and $g-1$ |
| Eccentricity | Distance from a node to the node farthest from it |
| Radius | Smallest eccentricity among all nodes |
| Dyad | A pair of nodes; there are $g(g-1)/2$ possible pairs |

- `cycles` uses a default length limit of 4. Longer limits make the number of cycles grow fast and the result hard to interpret.
- Report diameter and radius of a disconnected graph as infinite, and compute the mean distance over reachable pairs only.
- In undirected graphs the mean degree is $2L/g$ and the variance is $\sum_i (d_i - \bar d)^2 / g$. In directed graphs in-degree and out-degree both have mean $L/g$, and their variances are computed separately.
- In directed graphs in-degree counts received ties and reflects popularity; out-degree counts sent ties and reflects range. Row sums of the matrix give out-degree and column sums give in-degree.
- `directed_node_types` labels a node isolate when in-degree and out-degree are both 0, transmitter when only in-degree is 0, receiver when only out-degree is 0, and carrier when both are positive.
- Reordering the matrix rows and columns by block (permutation) exposes hidden patterns; pass `groups` to the figure and table functions for this. For the reversed-direction view (transpose), use `G.reverse()`.

### Density

| Case | Formula | Function |
|---|---|---|
| Undirected binary | $L / \{g(g-1)/2\}$ | `nx.density` |
| Directed binary | $L / \{g(g-1)\}$ | `nx.density` |
| Values ignored | Same as binary density | `nx.density` |
| Mean value | Sum of line values / possible ties | `valued_density(G)` |
| Multiplex relations | Sum of line values / (number of relation types × possible ties) | `valued_density(G, max_value=number of relation types)` |

- Inclusiveness is the number of non-isolated nodes divided by all nodes, and `describe` computes it. Two networks with the same inclusiveness can have different numbers of ties, so read it together with density.
- A dense network shares information quickly and binds members tightly, but it has fewer routes for outside information. In a sparse network cooperation and information sharing rarely start on their own.

### Centrality

| Measure | Relative formula | Meaning |
|---|---|---|
| Degree | $d_i / (g-1)$ | Number of direct contacts, local influence |
| Closeness | $(g-1) / \sum_j d_{ij}$ | How quickly a node reaches all others, network-wide |
| Betweenness | $\sum_{j<k} \frac{g_{jk}(i)}{g_{jk}} \Big/ \frac{(g-1)(g-2)}{2}$ | How much a node brokers shortest paths between others |
| In, out | In-degree, out-degree $/(g-1)$ | Received and sent ties in directed graphs |
| Eigenvector | Leading eigenvector of the adjacency matrix | Higher when connected to important nodes |
| PageRank | Stationary probability of a random walk with teleportation | Influence ranking in directed graphs |
| Katz | Sum of all walks, discounted by length | Combines direct and indirect ties |
| HITS | `nx.hits(G)` | Hub and authority scores in directed graphs |

- $g_{jk}$ is the number of shortest paths between $j$ and $k$, and $g_{jk}(i)$ is the number of them passing through $i$.
- `centralities` returns relative values sorted by betweenness. `extended_centralities` leaves measures that fail to converge blank and issues a warning.
- Closeness follows the NetworkX default: it uses reachable nodes only and multiplies by the share of reachable nodes.
- In a star, the center has relative betweenness 1 and all others 0. In a circle every node is equal, and in a line the middle node scores highest.
- Degree reads direct exchange, closeness reads speed of reach, and betweenness reads control over information flow. Removing a node with high betweenness can cut communication between groups.

### Centralization

Centralization measures how much a whole network leans on a single node. It uses Freeman's (1979) formula $\sum_i (C^* - C_i) / \max\sum$, where $C^*$ is the highest score and the denominator is the largest possible sum of differences, reached by a star. 0 means all nodes are equal and 1 means a star.

| Graph | Measure | Based on | Denominator |
|---|---|---|---|
| Undirected | Degree | Raw degree | $(g-1)(g-2)$ |
| Undirected | Betweenness | Raw betweenness (unordered pairs) | $(g-1)^2(g-2)/2$ |
| Undirected | Closeness | Relative closeness | $(g-1)(g-2)/(2g-3)$ |
| Directed | In-degree, out-degree | Raw degree | $(g-1)^2$ |
| Directed | Betweenness | Raw betweenness (ordered pairs) | $(g-1)^2(g-2)$ |

- Closeness centralization is computed for connected undirected graphs only and left blank otherwise, because Freeman derived that denominator under those conditions.
- Density shows how many ties there are on average; centralization shows how unevenly they are spread. When centralization is close to 1, losing the central node risks breaking the network apart.

### Structural holes

A structural hole exists when one node connects neighbors who are not connected to each other (Burt 1992). That node gets non-redundant information first and can steer its flow.

| Measure | Formula | Reading |
|---|---|---|
| Redundancy | $2t/n$ | How much the neighbors are tied to each other |
| Effective size | $n - 2t/n$ | Number of neighbors after removing redundancy |
| Efficiency | Effective size $/ n$ | Share of non-redundant neighbors |
| Constraint | $\sum_j (p_{ij} + \sum_{q \ne i,j} p_{iq} p_{qj})^2$ | Lower means a position spanning holes |

- $n$ is the number of the ego's neighbors and $t$ the number of ties among them, excluding ties to the ego. This effective size formula is Burt's general formula reduced for undirected binary graphs (Borgatti 1997). For weighted or directed graphs, `structural_holes(G, weight="weight")` uses the general formula through NetworkX.
- $p_{ij}$ is the share of $i$'s ties invested in $j$. Constraint rises when the network is small, when it is dense, and when ties concentrate on one neighbor.
- Nodes without neighbors cannot be scored and are left blank.
- The denser the network, the less room there is for holes; a clique where everyone is connected has none.
- `openness(G, groups)` is the share of a group's ties that leave the group. 0 means closed, 1 means open. Directed graphs count outgoing ties.

### Subgroups

| Concept | Definition | Function |
|---|---|---|
| Component | A set of nodes linked without breaks; directed graphs split into weak components (direction ignored) and strong components (nodes reach each other along directions) | `components` |
| Isolate | A node with no ties | `components` |
| Cut-point | A node whose removal increases the number of components | `cutpoints` |
| Bridge | A line whose removal increases the number of components | `cutpoints` |
| Knot | A piece separated at cut-points (bicomponent) | `cutpoints` |
| Cycle component | A connected set of 3 or more nodes left after removing every bridge | `cycle_components` |
| k-core | A maximal set in which every member has at least $k$ ties inside the set (Seidman 1983) | `k_cores` |
| m-slice | A connected set left after keeping only ties with multiplicity $m$ or more | `m_slices` |
| Clique | A maximal set of 3 or more nodes all directly tied to each other | `cliques` |
| n-clique | A maximal set whose members are within distance $n$ in the whole graph | `n_cliques` |
| n-clan | An n-clique whose diameter, using paths inside the set only, is $n$ or less | `n_clans` |
| n-club | A maximal set whose inside diameter is $n$ or less | `n_clubs` |

- Components find connected regions; the clique family finds tightly tied groups of nodes.
- `k_cores` returns each node's core number and, for each $k$, the members, remainders and remainder ratio. Remainders are the nodes dropped when $k$ goes up, and the remainder ratio is their count divided by all nodes. Higher-$k$ cores are more cohesive central groups. Coloring nodes by core number shows the nested layers of cohesion.
- `m_slices` uses line weights as multiplicity in weighted graphs. In binary graphs it uses the number of neighbors shared by the two end nodes as multiplicity.
- An n-clique can reach its distance through nodes outside the set. The n-clan rules this out; every n-clan is both an n-clique and an n-club (Wasserman and Faust 1994).
- Use $n = 2$ by default. With 3 or more the sets grow too large to read as cohesive groups.
- `n_clubs` takes n-clans and radius-$n$ neighborhoods as candidates and checks their diameter. The cost of finding every n-club rises steeply with node count, so the function returns only the maximal sets among its candidates.
- In `clique_membership`, a node that belongs to several cliques reads as a connector between cliques.

### Structural equivalence and blockmodeling

Two nodes that never meet can still hold the same position if they have the same pattern of ties to third parties; this is structural equivalence. Actors in the same position can substitute for each other in the network. A position is a set of actors with similar tie patterns, and a role is the pattern of ties attached to that position.

| Function | Computation | Reading |
|---|---|---|
| `se_distance` | $\sqrt{\sum_{k \ne i,j} [(x_{ik}-x_{jk})^2 + (x_{ki}-x_{kj})^2]}$ | Closer to 0 means more equivalent; the maximum for one binary relation is $\sqrt{2(g-2)}$ |
| `se_correlation` | Pearson correlation of the same row and column profiles | Closer to +1 means more equivalent |
| `rege_similarity` | Regular equivalence similarity from repeatedly matching neighbors | Closer to 1 means the same role |

- Correlation reaches +1 when two profiles have the same shape, while distance reaches 0 only when their level and spread match too. The two methods can therefore group the same data differently; use distance to test identical ties and correlation to test similar patterns.
- Correlation is undefined for profiles with zero variance, such as isolates, and is set to 0.
- Regular equivalence treats actors as playing the same role when they tie to the same kinds of others, even if not to the same individuals (White and Reitz 1983). Two managers with different subordinates are regularly equivalent.
- `rege_similarity` starts every pair at 1. Each round it matches the two nodes' outgoing neighbors and incoming neighbors separately, averages the scores of the best matches, and lowers the score in a direction where only one of the two has neighbors. It stops when the change falls below 1e-4 or after 20 rounds. In undirected binary graphs every non-isolated pair converges to 1, so use it on directed data.

`blockmodel(G, n_blocks, method)` assigns nodes to blocks.

| method | Procedure |
|---|---|
| `euclidean` | Average-linkage hierarchical clustering of `se_distance` |
| `concor` | Repeated CONCOR splits |
| `structure` | The `se_distance` formula applied to the geodesic distance matrix, so indirect ties count (Burt 1976); unreachable pairs get distance $g+1$ |
| `rege` | Average-linkage hierarchical clustering of $1 -$ `rege_similarity` |

- CONCOR (Breiger, Boorman and Arabie 1975) correlates the `se_correlation` matrix again and again until every entry is +1 or -1, then splits by sign. It keeps splitting the largest block the same way until the requested number of blocks is reached. Since it only ever splits in two, the analyst sets the number of blocks.
- CONCOR groups by correlation of direct tie patterns; structure groups by distances that include indirect ties.
- If the user does not set the number of blocks, use the function defaults (3 for `blockmodel`, 2 for `concor`) and state the number used in the analysis overview.

Use `image_matrix(G, blocks, criterion)` to decide whether two blocks are tied. Block density is the number of actual ties between two blocks divided by the possible ties; inside a block, ties to oneself are excluded.

| criterion | Marked 1 when | Use |
|---|---|---|
| `alpha` | Block density is at least α; α defaults to whole-network density | General case |
| `zero` | The block has at least one tie | Sparse networks |
| `one` | Every possible tie in the block exists | Dense networks |
| `perfect` | 1 if complete, 0 if empty, blank if mixed | Checking blockmodel fit |

Present blockmodel results in this order: raw matrix, matrix reordered by block (`plot_matrix(G, path, groups=blocks)`), image matrix, reduced graph (`reduce_to_blocks` then `plot_network`).

### Large networks

- `top_k_subgraph(G, k, by)` keeps the top $k$ nodes by betweenness, degree, closeness or PageRank.
- `core_subgraph(G, min_degree=3)` removes nodes below the degree threshold in one pass to trim the periphery.
- `louvain(G)` finds communities by raising modularity. Louvain shuffles node order at random, so the seed is fixed at 42 to reproduce results.
- A community is a group of densely tied nodes; an equivalence block is a group of nodes with the same tie pattern. Use Louvain for questions about cohesion and blockmodeling for questions about position and role.
- From 501 nodes, `nx.community.label_propagation_communities` is also an option.

### Bipartite networks

- `from_incidence` builds a bipartite graph from person by activity membership data and returns the person projection and the activity projection with it.
- In the person projection, line weight is the number of shared activities; in the activity projection, it is the number of shared people.
- `plot_bipartite` draws people as circles on the left and activities as squares on the right.

## Theory concepts

When explaining a concept, use the definitions and sources below, link it to a measure where possible, and demonstrate it on a made-up network.

| Concept | Content | Related analysis | Source |
|---|---|---|---|
| Types of relations | Transaction, communication, boundary penetration, instrumental, sentiment, authority and power, kinship. Decide which relation counts as a line before analysis | Data definition | Knoke and Kuklinski (1982) |
| Scope of analysis | One actor and its neighbors (ego), a pair of actors (dyad), every actor inside a boundary (whole network) | `ego_network`, `describe` | Wasserman and Faust (1994) |
| Tie strength | A combination of time spent, emotional intensity, intimacy and reciprocal services. Weak ties bridge separate groups and carry new information; strong ties provide cohesion and support | Weights, bridges, betweenness | Granovetter (1973) |
| Structural holes | A position linking disconnected groups gains non-redundant information and brokerage opportunities | `structural_holes` | Burt (1992) |
| Social capital | The closure view holds that dense, closed ties build trust and norms; the brokerage view holds that positions spanning holes give an information advantage | Density, constraint | Coleman (1988), Burt (1992) |
| Embeddedness | Economic action takes place within ongoing social relations; criticizes both the undersocialized and the oversocialized views | Tie duration, repeated exchange | Granovetter (1985) |
| Paradox of embeddedness | Embedded ties raise performance through trust, fine-grained information transfer and joint problem solving, but past a threshold they expose firms to outside shocks and cut them off from outside information | `plot_uzzi_concept` | Uzzi (1997) |
| Network organization | Defines the network as a form of coordinating economic activity distinct from markets and hierarchies | Designing interorganizational ties | Powell (1990) |
| Effects of central positions | Links reported between central positions and influence, involvement in innovation, team performance and managerial promotion | Centrality, constraint | Brass (1984), Ibarra (1993), Baldwin, Bedell and Johnson (1997), Burt (1992) |

The curve shape and threshold in `plot_uzzi_concept` are illustrative values chosen for explanation. For that reason the axes carry no numbers and `position` marks only a relative location.

Bavelas (1950) and Leavitt (1951) controlled the communication channels among group members in experiments and compared task performance across network shapes. Results for simple tasks:

| Criterion | Star, Y | Chain | Circle |
|---|---|---|---|
| Speed of solution | Fast | Slow | Slow |
| Number of messages | Few | Medium | Many |
| Errors | Few | Few | Many |
| Member satisfaction | Low | Medium | High |
| Recognition of and agreement on a leader | High | Medium | Low |

Cross and Prusak (2002) described four roles in informal organizational networks. The measures below can be read from network data alone; expertise needs separate attribute data.

| Role | Content | Measure |
|---|---|---|
| Central connector | Linked to many colleagues in the group; gathers and spreads information | High degree |
| Boundary spanner | Maintains ties outside the group or with other departments | Number of ties leaving the member's group |
| Information broker | Links subgroups that are otherwise apart | High betweenness, low constraint |
| Peripheral specialist | Few ties, but provides expertise in a specific field | Low degree plus expertise attribute data |

## Report format

Pick the format that fits the request and drop sections that are not needed. Every analysis answer includes the input matrix table, the results table and the figure files.

For analysis requests, `matrix_and_network` produces the matrix markdown and both PNG paths in one call.

```python
cent = centralities(G)
out = matrix_and_network(G, "outputs/org", title="Team communication",
                         values=cent["betweenness"])
print(out["markdown"])      # input matrix table
print(df_markdown(cent))    # results table
# deliver out["matrix_png"] and out["network_png"] as files
```

To show block or clique membership, pass `groups=blocks`. The matrix is then reordered by block and block boundaries are drawn.

### Data analysis requests

```markdown
# [Subject] network analysis

## Overview
- (Question) What the user wants to know, in one or two sentences
- (Data) Nodes, lines, direction and weight decision, made-up data or not
- (Methods) Measures and functions used

## Process
(Mermaid flowchart of input, computation, figures, interpretation)

## Methods
- (Definition) What each measure means
- (Formula) LaTeX formula
- (Code) Python code that was run

## Input matrix
(Output of matrix_markdown or the markdown from matrix_and_network)

## Results
(df_markdown results table; figures delivered as separate files)

## Interpretation
- (Main finding) The structure the numbers show
- (Practical implication) What it means for the organization or policy
```

### Concept explanation requests

```markdown
# [Concept]: definition and use

## Definition
- (Definition) Meaning of the concept and original author

## How it works
- How it is measured, with formulas

## Demonstration
(Code for a made-up network, results table, figure files)

## Use
- (Application) Example analysis situations
- (Caveats) Conditions for applying it
```

### Worked problem requests

```markdown
# [Problem topic]: solution

## Problem
- (Given) Data and requirements
- (To find) Values to compute or items to identify

## Solution
- (Step 1) Approach and formula
- (Step 2) NetworkX verification code

## Answer
(Final answer with reasoning)

## Check
(Results table and figure files)
```

### Labeling rules

- The script's column names are in English. When reporting tables, rename columns into the user's language if it is not English.
- Show decimals to three places.
- Pass figure titles and labels in the user's language too: give `plot_centrality_bars` a table with renamed columns plus matching `columns`, give `plot_degree_histogram` its `xlabel` and `ylabel`, and give `plot_uzzi_concept` its `labels`.
- When the user asks how to do something in UCINET or Pajek, show the NetworkX code for the same analysis and save the result in that tool's file format.

## Pre-delivery check

- Did every number come from code that was run?
- Are the input matrix table and the results table in the answer?
- Were the figure files created and delivered with the file-sharing feature?
- Is the answer free of local-path image markdown?
- Were the size-handling rules followed?
- Does the overview state direction, weights and whether the data is made up?
- Are table columns and figure labels in the user's language?
