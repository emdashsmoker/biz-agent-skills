# Structural Equivalence and Blockmodeling

> Translated from the Korean edition. Wording may differ from the original intent.

Covers how to group actors with similar relation patterns into positions and how to summarize those groups as blocks.

## Structural equivalence

Two actors hold the same position when they have the same ties to third parties, even if they do not know each other. Actors in the same position can substitute for each other in the network. For example, two branch managers who never met but deal with the same head-office departments and the same kinds of customers hold the same position in the organization.

| Concept | Definition |
|---|---|
| Position | The place occupied by actors with similar relation patterns |
| Role | The pattern of relations one position has with other positions |

## Measuring equivalence

### Euclidean distance

Compare the ties that actors i and j have with every other actor k, both as rows (ties sent) and as columns (ties received). Cells that refer to i or j themselves are excluded.

$$
d_{ij} = \sqrt{\sum_{k \ne i,j}\left[(x_{ik} - x_{jk})^2 + (x_{ki} - x_{kj})^2\right]}
$$

- 0 means the two actors have exactly the same ties.
- For one relation recorded as 0 or 1, the maximum is √(2(g-2)). With R relations combined it is √(2R(g-2)).
- Differences in the number of ties also add to the distance, so two actors with the same pattern but different numbers of ties get a larger value.

### Correlation

The Pearson correlation between the same two profiles (cells that refer to i or j excluded).

- +1 means the relation patterns move together perfectly.
- It looks at the similarity of patterns more than at differences in the number of ties.
- An actor whose profile has no variation, such as an isolate, has no defined correlation, so the value is set to 0.

| Method | Compares | Value for two identical actors |
|---|---|---|
| Euclidean distance | Whether the ties are the same | 0 |
| Correlation | Whether the patterns are similar | +1 |

The two methods can give different results on the same data (Faust and Wasserman 1992). Use Euclidean distance when the number of ties must also match for two actors to share a position. Use correlation when similar patterns are enough.

## Blockmodeling

Group similar actors into blocks using equivalence values, then reduce the actor-level matrix to a block-level matrix. This summarizes a complex network as relations among a few blocks. The outputs of each step:

| Step | Output | Function |
|---|---|---|
| 1 | Raw matrix | `matrix_to_markdown(G)` |
| 2 | Matrix reordered by block | `reorder_matrix(G, reorder_by=blocks.to_dict())` |
| 3 | Image matrix with 0 or 1 between blocks | `image_matrix(G, blocks)` |
| 4 | Reduced graph drawn from the image matrix | `aggregate_to_blocks(G, blocks)` |

Check the density between blocks with `block_density_matrix(G, blocks)`. Cells inside a block exclude ties of an actor with itself.

## Ways to form blocks

`blockmodel(G, n_blocks, method)` offers these methods.

| method | Procedure | Criterion |
|---|---|---|
| `hierarchical` | Ward hierarchical clustering on Euclidean distance | Identical ties |
| `concor` | Repeated CONCOR splits | Correlation of relation patterns |
| `structure` | Average-linkage clustering on the Euclidean distance between shortest-distance profiles | Distance including indirect ties |
| `rege` | Average-linkage clustering on regular-equivalence similarity | Ties to similar others |

### CONCOR

CONCOR (CONvergence of iterated CORrelations) uses the fact that repeatedly correlating a correlation matrix drives every entry to +1 or -1 (Breiger, Boorman, Arabie 1975). Actors tied together at +1 and those at -1 form two blocks. To split further, apply the same procedure to each block.

- Each step splits every block in two, so the number of blocks is a power of two: 2, 4, 8. `blockmodel(G, n_blocks=4, method="concor")` runs two steps. Any other value raises an error.
- A block whose members already share the same pattern cannot split, so the actual number of blocks can be smaller than requested.
- Isolates have no defined correlation. They are left out of the splitting and receive block number 0.
- The analyst decides how many steps to run. Reading the result as a tree lets you trace each split.

> Breiger, R. L., Boorman, S. A., Arabie, P. (1975), An Algorithm for Clustering Relational Data with Applications to Social Network Analysis and Comparison with Multidimensional Scaling, Journal of Mathematical Psychology

### Path distance method

Looking only at direct ties misses differences among actors that are far apart. The `structure` method lists the shortest distance from each actor to every other actor and groups actors with similar lists. Unreachable pairs get a distance of the number of points plus 1. It simplifies path-distance equivalence, which also reflects indirect ties.

### Regular equivalence and REGE

Regular equivalence treats two actors as holding the same role when they are tied to others of similar standing, even if those others are different people (White and Reitz 1983). Affiliates in different business groups, or nurses in different hospitals, fall into the same role this way.

`regular_equivalence(G)` works as follows.

- Start with similarity 1 for every pair.
- Match the neighbors of two actors to each other, add the similarity of each best match, and divide by the total number of neighbors of both actors.
- In a directed graph, match outgoing neighbors and incoming neighbors separately.
- Repeat until the change in similarity falls below the tolerance.

On undirected binary data, most actors other than isolates come out similar (Hanneman and Riddle 2005). Use regular equivalence on directed or valued graphs.

> White, D. R., Reitz, K. P. (1983), Graph and Semigroup Homomorphisms on Networks of Relations, Social Networks 5

> Hanneman, R. A., Riddle, M. (2005), Introduction to Social Network Methods, Chapter 15(https://faculty.ucr.edu/%7Ehanneman/nettext/C15_Regular_Equivalence.html)

## Image matrix criteria

These criteria decide whether a tie exists between two blocks (Faust and Wasserman 1992). Block density is the number of actual ties between the blocks divided by the number of possible ties.

| criterion | Name | Coded 1 when | Use |
|---|---|---|---|
| `alpha` | α density | Block density is α or more | Common default, with α set to overall density unless given |
| `zero` | Zeroblock | At least one tie exists | Sparse networks |
| `one` | Oneblock | Every possible tie exists | Dense networks |
| `perfect` | Perfect fit | 1 when complete, 0 when empty | Checks whether the blockmodel fits structural equivalence exactly |

Under `perfect`, a block with only some ties is marked NaN. A NaN means perfect fit fails for that pair of blocks. The oneblock criterion on a sparse network turns almost every cell into 0, and the zeroblock criterion on a dense network turns almost every cell into 1, so neither reveals structure in those cases.

> Faust, K., Wasserman, S. (1992), Blockmodels: Interpretation and Evaluation, Social Networks 14

## Code

```python
dist = euclidean_equivalence(G)           # closer to 0 means more equivalent
corr = correlation_equivalence(G)         # closer to +1 means more equivalent
rege = regular_equivalence(G_directed)    # closer to 1 means the same role

blocks = blockmodel(G, n_blocks=2, method="concor")
img = image_matrix(G, blocks, criterion="alpha")
dens = block_density_matrix(G, blocks)
reduced = aggregate_to_blocks(G, blocks)
```

## Reading the results

- (Structural equivalence) Actors with the same pattern of ties hold the same position even without a direct tie. Use it to review redeployment or substitutability.
- (Blockmodel) Reduce collaboration among dozens of departments to relations among a few blocks to see the whole structure. The direction of ties between blocks separates core blocks from peripheral ones.
- (Regular equivalence) Finds roles in data where many sub-organizations repeat a similar role structure, such as industries or business groups.
