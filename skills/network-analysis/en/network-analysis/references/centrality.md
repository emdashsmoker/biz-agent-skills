# Centrality and Centralization

> Translated from the Korean edition. Wording may differ from the original intent.

Centrality measures the position of one point in the network. Centralization measures how much the whole network leans on a single point.

## Why centrality matters

Actors in central positions interact with many others, are visible, and connect people who are otherwise apart. Several empirical studies report links between central positions and outcomes.

| Study | Reported relation |
|---|---|
| Brass (1984) | Structural position in an organization and individual influence |
| Ibarra (1993) | Network centrality, power and involvement in innovation |
| Baldwin, Bedell, Johnson (1997) | Network position of students in a team-based MBA program, satisfaction and performance |
| Burt (1992) | Early promotion of managers whose networks span structural holes |

> Brass, D. J. (1984), Being in the Right Place: A Structural Analysis of Individual Influence in an Organization, Administrative Science Quarterly 29(4)

> Ibarra, H. (1993), Network Centrality, Power, and Innovation Involvement, Academy of Management Journal 36

> Baldwin, T. T., Bedell, M. D., Johnson, J. L. (1997), The Social Fabric of a Team-Based MBA Program, Academy of Management Journal 40

> Burt, R. S. (1992), Structural Holes: The Social Structure of Competition, Harvard University Press

## Kinds of centrality

- (By direction) In-centrality, measured on incoming ties, reflects prestige. Out-centrality, measured on outgoing ties, reflects how widely an actor reaches out.
- (By target) A value for one point is point centrality. The concentration of the whole graph is graph centrality, or centralization.
- (By range) Measures that look only at direct neighbors are local. Measures based on distances to all points are global.

| Centrality | What it looks at | Question |
|---|---|---|
| Degree | Number of directly connected points | How many others is the actor tied to directly? |
| Closeness | Distance to other points | How close is the actor to everyone else? |
| Betweenness | Position on shortest paths between others | How much does the actor connect others? |

## Degree centrality

$$
C_D(i) = d_i, \quad C'_D(i) = \frac{d_i}{g - 1}
$$

d_i is the degree of point i and g is the number of points. The relative value, divided by g-1, compares networks of different sizes. Degree looks only at direct ties and does not reflect position in the wider network.

## Closeness centrality

$$
C_C(i) = \frac{1}{\sum_{j} d_{ij}}, \quad C'_C(i) = \frac{g - 1}{\sum_{j} d_{ij}}
$$

d_ij is the distance between points i and j. The relative value lies between 0 and 1. Larger values mean the point is closer to the others.

## Betweenness centrality

$$
C_B(i) = \sum_{j<k} \frac{g_{jk}(i)}{g_{jk}}, \quad C'_B(i) = \frac{C_B(i)}{(g-1)(g-2)/2}
$$

g_jk is the number of shortest paths between j and k, and g_jk(i) is the number of those paths that pass through i. A point with a high value can relay or block the flow of information between others.

| Graph shape | Betweenness |
|---|---|
| Star | Center has relative value 1, all others 0 |
| Circle | Every point has the same value |
| Line | The middle point has the largest value |

## NetworkX conventions

`compute_centralities(G)` calls NetworkX directly, so these conventions apply to the results.

- Degree, closeness and betweenness are returned as relative values.
- Degree centrality on a directed graph divides indegree plus outdegree by g-1, so it ranges from 0 to 2. Read the in-centrality and out-centrality columns for each direction.
- Closeness on a directed graph uses incoming distance. Get outgoing-distance values with `compute_centralities(transpose_matrix(G))`.
- Closeness on a disconnected graph uses the Wasserman and Faust correction: the share of reachable points divided by the mean distance. On a connected graph it equals the formula above.

| Measure | NetworkX function |
|---|---|
| Degree centrality | `nx.degree_centrality` |
| In and out centrality | `nx.in_degree_centrality`, `nx.out_degree_centrality` |
| Closeness centrality | `nx.closeness_centrality` |
| Betweenness centrality | `nx.betweenness_centrality` |

## Centralization

Centralization adds up the differences between the largest centrality score and every point's score, then divides by the largest sum possible in a graph of the same size (Freeman 1979). A star graph reaches that maximum, so a star scores 1 and a circle, where every point has the same score, scores 0. Centrality describes one point's position. Centralization describes the structure of the whole network. Density shows the average level of connection, while centralization shows whether connections are spread evenly.

For undirected graphs `compute_centralization(G)` uses these denominators.

| Centralization | Scores used | Denominator (maximum) |
|---|---|---|
| Degree | Raw degree | (g-1)(g-2) |
| Closeness | Relative closeness | (g-1)(g-2)/(2g-3) |
| Betweenness | Raw betweenness | (g-1)²(g-2)/2 |

$$
C_D = \frac{\sum_{i}[\max_j d_j - d_i]}{(g-1)(g-2)}
$$

Closeness centralization is computed for connected graphs only. A disconnected graph returns NaN.

For directed graphs it returns:

- (In and out degree centralization) Raw indegree or outdegree, divided by (g-1)². A graph in which every point points at one point has in-degree centralization 1.
- (Betweenness centralization) Raw betweenness counted along directed paths, divided by (g-1)²(g-2). A star whose center and leaves point at each other scores 1.
- (Closeness centralization) Not computed for directed graphs. Returns NaN.

> Freeman, L. C. (1979), Centrality in Social Networks: Conceptual Clarification, Social Networks 1

## Extended measures

`compute_extended_centralities(G)` computes eigenvector, PageRank and Katz centrality. A measure that fails to converge is filled with NaN.

| Centrality | Function | Meaning |
|---|---|---|
| Eigenvector | `nx.eigenvector_centrality` | Grows with ties to important points |
| PageRank | `nx.pagerank` | Weights incoming ties by the score of the sender |
| Katz | `nx.katz_centrality_numpy` | Adds distant ties with decaying weights |
| HITS | `nx.hits` | Gives separate hub and authority scores in a directed graph |

## Reading the results

- (High degree centrality) The point has many direct exchanges and gathers local information.
- (High closeness centrality) The point can spread or receive information across the whole network quickly.
- (High betweenness centrality) The point connects groups. If it leaves, flows between groups break or slow down.
- (Centralization near 1) Ties concentrate on one point, and the network may fall apart without it.
- (Centralization near 0) Ties are spread evenly.
