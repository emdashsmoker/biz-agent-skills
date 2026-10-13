# Graph Theory and Data Representation

> Translated from the Korean edition. Wording may differ from the original intent.

Covers the parts of a graph, walks and paths, degree statistics, relational data collection and matrix representation.

## Parts of a graph

A graph represents relations with points and lines. Points are actors such as people, organizations, firms or countries. Lines are exchanges, transactions or other interactions between actors.

| Part | Mathematical term | Social science term |
|---|---|---|
| Point | node, point, vertex | actor |
| Line | line, edge, arc | tie, link |

Graphs are classified by how they record direction and strength.

- (Undirected graph) Records the relation between A and B without direction.
- (Directed graph) Separates the relation from A to B from the relation from B to A.
- (Valued graph) Records the strength of each relation as a number. It can be directed or undirected.

## Walks, paths and cycles

| Concept | Definition | Repetition |
|---|---|---|
| Walk | A sequence of lines from one point to another | Points and lines may repeat |
| Path | A walk in which every point appears once | No repetition |
| Cycle | A closed walk that returns to its start and contains at least 3 distinct points | Only the start point repeats |

The distance between two points is the length of the shortest path, so paths underlie distance, centrality and subgroup analysis. In a directed graph, two points that point at each other form a closed walk with only 2 points, which does not count as a cycle.

## Components, cut-points and bridges

- (Component) A maximal set of points connected to each other by paths.
- (Cut-point) A point whose removal increases the number of components.
- (Bridge) A line whose removal increases the number of components.

## Distance and diameter

- (Distance) The number of lines on the shortest path between two points (geodesic distance). It is infinite when no path exists.
- (Diameter) The largest distance in the graph. In a connected graph it lies between 1 and g-1, where g is the number of points.
- (Eccentricity and radius) The distance from a point to the point farthest from it is its eccentricity. The smallest eccentricity is the radius.

`compute_distances(G)` returns the distance matrix, the mean distance over reachable pairs, the diameter, the radius and the eccentricities. For a disconnected graph (or a directed graph that is not strongly connected) it returns infinite diameter and radius.

## Neighbors and degree

- (Adjacency) Two points joined directly by one line.
- (Degree) The number of points adjacent to a point. In an undirected graph the sum of degrees is twice the number of lines.

A directed graph counts each direction separately.

- (Indegree) Lines coming in from other points. It reflects popularity.
- (Outdegree) Lines going out to other points. It reflects how widely a point reaches out.

`classify_nodes(G)` classifies points by indegree and outdegree.

| Indegree | Outdegree | Class |
|---|---|---|
| 0 | 0 | Isolate |
| 0 | 1 or more | Transmitter |
| 1 or more | 0 | Receiver |
| 1 or more | 1 or more | Carrier |

## Mean and variance of degree

L is the number of lines and g the number of points. The variance is the population variance (divided by g).

Undirected graph

$$
m_d = \frac{2L}{g}, \quad s_d^2 = \frac{\sum_{i=1}^{g}(d_i - m_d)^2}{g}
$$

Directed graph

$$
m_{d^{in}} = m_{d^{out}} = \frac{L}{g}, \quad s_{d^{in}}^2 = \frac{\sum_{i=1}^{g}(d_i^{in} - m_{d^{in}})^2}{g}
$$

The outdegree variance follows the same formula. `compute_degree_stats(G)` returns the mean, variance and standard deviation.

## Collecting relational data

| Method | Description |
|---|---|
| Survey | Respondents list the people they have ties with |
| Observation | The researcher observes and records relations |
| Experiment | Interactions are recorded under designed conditions |
| Existing records | Records that already exist, such as email logs, transactions or co-author lists |

Set the scope of the analysis (the network boundary) in one of these ways.

- (Positional) Limit the population to people who hold certain positions or memberships.
- (Reputational) Ask informants to name the important actors.
- (Snowball) Start from a few people and add the people they name.

## Measurement types

Relations can be recorded as present or absent (binary) or as strength (valued), with or without direction, which defines the measurement types below.

| Type | Values | Direction |
|---|---|---|
| 1 | Binary (0 or 1) | None |
| 2 | Binary (0 or 1) | Yes |
| 3 | Valued | None |
| 4 | Valued | Yes |

## Matrix representation

- (Adjacency matrix) Rows and columns are actors and each cell holds the value of the relation. In a directed graph the row sum is the outdegree and the column sum is the indegree.
- (Incidence matrix) Rows are people, columns are activities or affiliations, and cells record participation. `load_from_incidence` builds a two-mode graph of people and activities, a people-to-people projection and an activity-to-activity projection from it. Projection line weights count shared partners.

Basic operations on a matrix:

- (Reordering) Permute rows and columns in the same order to reveal hidden groups. Use `reorder_matrix(G, reorder_by=blocks)`.
- (Transpose) Swap rows and columns to reverse the direction of relations. Use `transpose_matrix(G)`.

## Functions

```python
dyadic_pairs(10)                        # possible pairs N(N-1)/2 = 45
find_walks(G, "A", "C", max_length=4)   # walks, repetition allowed
find_paths(G, "A", "H", max_length=5)   # paths, shortest first
find_cycles(G, max_length=4)            # cycles with 3 or more points
classify_nodes(G_directed)              # isolate, transmitter, receiver, carrier
compute_degree_stats(G)                 # degree mean, variance, standard deviation
extract_ego_network(G, ego="Dana", radius=1)    # ego and neighbors within radius
transpose_matrix(G_directed)            # reverse direction
reorder_matrix(G, reorder_by=blocks.to_dict())  # reorder by block
```

The number of walks grows fast with length, so keep `max_length` small in `find_walks`. `extract_ego_network` follows both incoming and outgoing relations in a directed graph.
