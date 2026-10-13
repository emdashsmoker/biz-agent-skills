# Cohesion and Subgroups

> Translated from the Korean edition. Wording may differ from the original intent.

Covers density, structural holes, social capital, components, k-cores, cliques and their relaxations.

## Density

Density is the number of actual lines divided by the number of possible lines. 0 means no ties at all and 1 means every point is tied to every other point. k is the number of lines and g the number of points.

$$
\text{Undirected density} = \frac{k}{g(g-1)/2}, \quad \text{Directed density} = \frac{k}{g(g-1)}
$$

A directed graph counts A to B and B to A separately, so it has twice as many possible lines.

For a valued graph, pick one of the methods below and state which one you used.

- Ignore the values and count only presence or absence.
- Divide the sum of values by the number of possible lines, which gives the average strength.
- Divide the sum of values by the number of actual lines times the largest value. This reflects the multiplicity of relations.

`nx.density` and `compute_density` use the first method.

Inclusiveness is the share of points that are not isolates. Many isolates pull density down, so read the two together. `compute_density(G)` returns density, the number of isolates and the inclusiveness ratio.

## Structural holes

A structural hole is the gap between two people who are not tied to each other (Burt 1992). The person who bridges the gap hears from both sides first and can steer the flow between them. When an ego's contacts are already tied to one another, those relations repeat the same information and are redundant.

For undirected, unweighted graphs, the ego measures are as follows (Borgatti 1997). n is the number of ego's contacts and t the number of lines among those contacts.

$$
\text{Redundancy} = \frac{2t}{n}, \quad \text{Effective size} = n - \frac{2t}{n}, \quad \text{Efficiency} = \frac{\text{Effective size}}{n}
$$

Redundancy is the average number of ego's other contacts that each contact is tied to. Weighted and directed graphs use Burt's general formula, which `nx.effective_size` computes.

Constraint shows how much an ego's ties depend on a few contacts. p_ij is the share of i's relations invested in j.

$$
c_{ij} = \left(p_{ij} + \sum_{q \ne i,j} p_{iq}\,p_{qj}\right)^2, \quad C_i = \sum_{j} c_{ij}
$$

Constraint grows when there are fewer contacts, when contacts are densely tied to each other, and when relations concentrate on one contact. Low constraint marks a position that bridges structural holes.

`compute_structural_holes(G)` returns effective size, constraint, number of contacts and efficiency, sorted by constraint from low to high. The efficiency denominator counts each contact once. In a directed graph, two lines pointing at each other count as one contact.

> Burt, R. S. (1992), Structural Holes: The Social Structure of Competition, Harvard University Press

> Borgatti, S. P. (1997), Structural Holes: Unpacking Burt's Redundancy Measures, Connections 20(1)

## Density and structural holes

In a clique where every member is tied to every other, members reach each other without going through anyone, so there are no structural holes. As the density of an ego network rises, its structural holes shrink.

## Social capital

Social capital is the set of resources an actor can use through relations. It is measured from these views.

- (Closure view) Dense ties build trust and cooperation. Measure it with density and degree.
- (Brokerage view) A position that links unconnected groups brings in new information. Measure it with effective size and constraint.

## Components

A component is a maximal set of points joined by paths. A point tied to nobody is an isolate. Directed graphs divide components as follows.

| Kind | Condition | Use |
|---|---|---|
| Strong component | Every member reaches every other member along the direction of ties | Groups in which resources circulate |
| Weak component | Members are connected once direction is ignored | Loosely linked groups |

## Cycles, bridges, cut-points and knots

- (Cycle component) After removing all bridges, each remaining connected piece with 3 or more points. `find_cycle_components` finds them.
- (Bridge) A line whose removal splits a component in two.
- (Cut-point) A point whose removal splits a component into two or more.
- (Knot) A piece separated by cut-points. NetworkX finds these pieces with `nx.biconnected_components`.

## k-cores and m-cores

- (k-core) The maximal subgraph in which every member has at least k lines inside the core (Seidman 1983). Raising k leaves only denser central groups.
- (Residuals) Points that drop out of the k-core as k rises. `k_core_residuals` shows the number and share of residuals for each k.
- (m-core) A subgraph that keeps only strong ties. In a weighted graph it keeps lines with weight m or more. Without weights it uses a substitute rule and keeps lines whose two end points share m or more neighbors.

> Seidman, S. B. (1983), Network Structure and Minimum Degree, Social Networks 5

## Cliques and their relaxations

A clique is a maximal set of 3 or more points that are all directly tied to one another. The condition is strict, so real data tends to produce many small, overlapping cliques. Relaxed definitions extend the distance condition.

| Technique | Definition | Where distance is measured |
|---|---|---|
| Clique | Maximal set whose members are all directly tied | Distance 1 |
| n-clique | Maximal set whose members are all within distance n | Paths may pass through outsiders |
| n-clan | An n-clique whose own subgraph also has diameter n or less | Paths among members only |
| n-club | Maximal subgraph with diameter n or less | Paths among members only |

Every n-clan is both an n-clique and an n-club. An n-clique and an n-club need not contain one another (Mokken 1979). With n of 3 or more, members sit far apart and the set is hard to read as one group.

`find_n_clubs` is an approximate search. From each point it collects all points within distance n, then repeatedly drops the member that reaches the fewest other members within distance n until the diameter is n or less. Sets contained in another result are discarded. Finding every maximal n-club becomes computationally impractical as networks grow, which is why this approach is used.

> Mokken, R. J. (1979), Cliques, Clubs and Clans, Quality and Quantity

## Network openness

Openness is the share of a group's tie ends that point outside the group. 0 means a fully closed group and 1 means all ties point outside. A line inside the group is counted once from each end, so it counts twice. A directed graph counts outgoing ties only. Use `compute_network_openness(G, groups)`.

## NetworkX functions

| Technique | Function |
|---|---|
| Density | `nx.density` |
| Effective size, constraint | `nx.effective_size`, `nx.constraint` |
| Components | `nx.connected_components`, `nx.strongly_connected_components`, `nx.weakly_connected_components` |
| Knots (biconnected pieces) | `nx.biconnected_components` |
| k-core | `nx.k_core`, `nx.core_number` |
| Clique | `nx.find_cliques` |

## Script functions

```python
compute_density(G)                     # density, isolates, inclusiveness
compute_structural_holes(G)            # effective size, constraint, efficiency
find_components(G)                     # components and isolates
find_cut_points(G)                     # cut-points and bridges
find_cycle_components(G)               # cyclic pieces after removing bridges
find_k_cores(G)                        # core members for each k
k_core_residuals(G)                    # residuals for each k
compute_m_core(G_weighted, m=2)        # graph with strong ties only
find_cliques(G, min_size=3)            # maximal cliques, largest first
clique_membership(G)                   # number of cliques per point
find_n_cliques(G, n=2)
find_n_clans(G, n=2)
find_n_clubs(G, n=2)
compute_network_openness(G, blocks)    # openness per group
```

With a directed graph as input, k-cores, cliques, the n-clique family, cut-points and bridges ignore direction.

## Reading the results

- (Dense group) Members interact often, which eases trust and cooperation, while outside information enters with difficulty.
- (Sparse group) Cooperation and information sharing rarely arise on their own. The group needs mechanisms that create ties.
- (Low constraint) The point links contacts who are not tied to each other and hears new information first.
- (Core with large k) A tightly knit central group.
- (Point in several cliques) A person who links small groups.
