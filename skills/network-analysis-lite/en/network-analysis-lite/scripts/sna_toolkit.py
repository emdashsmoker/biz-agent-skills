"""Social network analysis toolkit built on NetworkX.

Import this module and call the functions directly. Every number reported to
the user should come from these functions (or NetworkX), never from mental
arithmetic, so that results can be reproduced.

    import sys; sys.path.insert(0, "<skill-folder>/scripts")
    from sna_toolkit import *
"""

import os
import warnings

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import pdist, squareform

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SEED = 42                      # fixed seed so layouts and Louvain are repeatable
MATRIX_INLINE_MAX_NODES = 30   # above this, matrices are summarized
MATRIX_CELL_VALUE_MAX_NODES = 20
FILTER_MAX_NODES = 100
AGGREGATE_MAX_NODES = 500
MIN_CLIQUE_SIZE = 3            # Wasserman & Faust: cliques have 3+ nodes
FIG_DPI = 150
SPRING_K = 1.5                 # node spacing for spring layout
AUTO_REFINE_STEPS = 30         # spring steps applied after Kamada-Kawai

# Noto Sans CJK collections often register under the JP name; they still
# contain Hangul glyphs.
FONT_CANDIDATES = ["NanumGothic", "Noto Sans CJK KR", "Noto Sans KR",
                   "Malgun Gothic", "AppleGothic", "Noto Sans CJK JP"]

PALETTE = {
    "node": "#8FB8D4",
    "node_edge": "#5783A8",
    "accent": "#E5A785",
    "edge": "#7A95A8",
    "grid": "#8FA3B3",
    "frame": "#5B7890",
}
GROUP_COLORS = ["#8FB8D4", "#A5CDB5", "#EDC491", "#CFB0CF", "#B8B8B8",
                "#9FC7CF", "#E5B5B5", "#C0CBA5", "#D6C7A5", "#B8ADC8"]
HEAT_COLORS = ["#FFFFFF", "#E0EBF3", "#C5DEF0", "#9FC5DF", "#7DAECC"]


def _heat_cmap():
    return LinearSegmentedColormap.from_list("pastel_blue", HEAT_COLORS)


_FONT_IN_USE = None


def setup_font():
    """Use the first installed CJK-capable font; never installs anything."""
    global _FONT_IN_USE
    if _FONT_IN_USE is None:
        installed = {f.name for f in fm.fontManager.ttflist}
        found = [name for name in FONT_CANDIDATES if name in installed]
        if not found:
            warnings.warn("No CJK font found; non-Latin labels may not render.")
        _FONT_IN_USE = found[0] if found else "DejaVu Sans"
        plt.rcParams["font.family"] = [_FONT_IN_USE, "DejaVu Sans"]
        plt.rcParams["font.sans-serif"] = [_FONT_IN_USE, "DejaVu Sans"]
        plt.rcParams["axes.unicode_minus"] = False
    return _FONT_IN_USE


def _as_undirected(G):
    H = G.to_undirected() if G.is_directed() else G.copy()
    H.remove_edges_from(nx.selfloop_edges(H))
    return H


def _is_weighted(G):
    return any("weight" in d for _, _, d in G.edges(data=True))


# ---------------------------------------------------------------------------
# Loading and export
# ---------------------------------------------------------------------------

def from_matrix(matrix, labels=None, directed=False, weighted=False):
    """Adjacency matrix -> graph. Diagonal (self-ties) is ignored."""
    arr = np.asarray(matrix, dtype=float)
    labels = list(range(len(arr))) if labels is None else list(labels)
    G = nx.DiGraph() if directed else nx.Graph()
    G.add_nodes_from(labels)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i, j] != 0:
                if weighted:
                    G.add_edge(labels[i], labels[j], weight=float(arr[i, j]))
                else:
                    G.add_edge(labels[i], labels[j])
    return G


def from_edges(edges, directed=False, weighted=False):
    """Edge tuples (u, v) or (u, v, weight) -> graph."""
    G = nx.DiGraph() if directed else nx.Graph()
    if weighted:
        G.add_weighted_edges_from(edges)
    else:
        G.add_edges_from((e[0], e[1]) for e in edges)
    return G


def from_incidence(affiliations):
    """Person x activity data -> bipartite graph and both one-mode projections.

    affiliations: DataFrame (rows=people, columns=activities, >0 = member)
                  or dict {person: [activities]}.
    Projection edge weight = number of shared activities (or shared people).
    """
    B = nx.Graph()
    if isinstance(affiliations, dict):
        pairs = [(p, a) for p, acts in affiliations.items() for a in acts]
        people = list(affiliations)
        activities = sorted({a for _, a in pairs}, key=str)
    elif isinstance(affiliations, pd.DataFrame):
        people, activities = list(affiliations.index), list(affiliations.columns)
        pairs = [(p, a) for p in people for a in activities
                 if affiliations.loc[p, a] > 0]
    else:
        raise ValueError("affiliations must be a dict or a DataFrame")
    B.add_nodes_from(people, bipartite=0)
    B.add_nodes_from(activities, bipartite=1)
    B.add_edges_from(pairs)
    proj = nx.bipartite.weighted_projected_graph
    return {"bipartite": B, "people": people, "activities": activities,
            "people_projection": proj(B, people),
            "activity_projection": proj(B, activities)}


def detect_table_format(df):
    """'edges' (<=3 columns), 'matrix' (square, optional label column),
    otherwise 'incidence'."""
    n_rows, n_cols = df.shape
    if n_cols <= 3:
        return "edges"
    if n_rows in (n_cols, n_cols - 1):
        return "matrix"
    return "incidence"


def load_table(path, fmt=None, directed=False, weighted=False,
               sheet_name=0, encoding="utf-8", sep=","):
    """Load .csv/.tsv/.txt/.xlsx/.xls as edges, matrix or incidence data.
    Korean CSV exported from Excel may need encoding='utf-8-sig' or 'cp949'."""
    if str(path).lower().endswith((".xlsx", ".xls")):
        df = pd.read_excel(path, sheet_name=sheet_name)   # needs openpyxl
    else:
        df = pd.read_csv(path, encoding=encoding, sep=sep)
    fmt = fmt or detect_table_format(df)
    if fmt == "edges":
        cols = list(df.columns)
        use_w = weighted and len(cols) >= 3
        rows = df[cols[:3] if use_w else cols[:2]].itertuples(index=False)
        return from_edges(list(rows), directed=directed, weighted=use_w)
    if fmt == "matrix":
        if df.shape[0] == df.shape[1] - 1:
            df = df.set_index(df.columns[0])
        return from_matrix(df.values, labels=list(df.columns),
                           directed=directed, weighted=weighted)
    if fmt == "incidence":
        return from_incidence(df.set_index(df.columns[0]))
    raise ValueError(f"Unknown format: {fmt}")


def export_table(G, path, fmt="edges", encoding="utf-8-sig"):
    """Save as edge list or matrix CSV. utf-8-sig keeps Korean readable in Excel."""
    if fmt == "edges":
        rows = [{"source": u, "target": v, **d} for u, v, d in G.edges(data=True)]
        pd.DataFrame(rows).to_csv(path, index=False, encoding=encoding)
    elif fmt == "matrix":
        nodes = list(G.nodes())
        A = nx.to_numpy_array(G, nodelist=nodes)
        pd.DataFrame(A, index=nodes, columns=nodes).to_csv(path, encoding=encoding)
    else:
        raise ValueError(f"Unknown format: {fmt}")


def write_ucinet_dl(G, path, fmt="fullmatrix"):
    """Write UCINET DL (FULLMATRIX or EDGELIST1, labels embedded)."""
    nodes = list(G.nodes())
    lines = [f"DL N={len(nodes)}"]
    if fmt == "fullmatrix":
        A = nx.to_numpy_array(G, nodelist=nodes)
        lines += ["FORMAT = FULLMATRIX", "LABELS EMBEDDED", "DATA:",
                  " " + " ".join(map(str, nodes))]
        lines += [f"{n} " + " ".join(f"{v:g}" for v in A[i])
                  for i, n in enumerate(nodes)]
    elif fmt == "edgelist":
        lines += ["FORMAT = EDGELIST1", "LABELS EMBEDDED", "DATA:"]
        lines += [f"{u} {v} {d.get('weight', 1):g}" for u, v, d in G.edges(data=True)]
    else:
        raise ValueError(f"Unknown DL format: {fmt}")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def read_ucinet_dl(path, directed=False):
    """Read UCINET DL files written as FULLMATRIX or EDGELIST1 with embedded labels."""
    with open(path, encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
    header = " ".join(lines).upper()
    start = next(i for i, l in enumerate(lines) if l.upper().startswith("DATA"))
    data = lines[start + 1:]
    if "EDGELIST" in header:
        edges = [(t[0], t[1], float(t[2])) if len(t) >= 3 else (t[0], t[1], 1.0)
                 for t in (l.split() for l in data)]
        return from_edges(edges, directed=directed, weighted=True)
    if "EMBEDDED" in header:
        labels = [l.split()[0] for l in data[1:]]
        matrix = [[float(v) for v in l.split()[1:]] for l in data[1:]]
    else:
        matrix = [[float(v) for v in l.split()] for l in data]
        labels = None
    return from_matrix(matrix, labels=labels, directed=directed,
                       weighted=np.any(np.asarray(matrix) > 1))


# ---------------------------------------------------------------------------
# Descriptive measures
# ---------------------------------------------------------------------------

def describe(G):
    """Size, density, inclusiveness, components and diameter in one table."""
    n = G.number_of_nodes()
    isolates = list(nx.isolates(G))
    info = {"nodes": n, "ties": G.number_of_edges(), "directed": G.is_directed(),
            "possible_dyads": n * (n - 1) // 2, "density": nx.density(G),
            "isolates": len(isolates),
            "inclusiveness": (n - len(isolates)) / n if n else 0.0}
    if G.is_directed():
        info["weak_components"] = nx.number_weakly_connected_components(G)
        info["strong_components"] = nx.number_strongly_connected_components(G)
        connected = n > 0 and nx.is_strongly_connected(G)
    else:
        info["components"] = nx.number_connected_components(G)
        connected = n > 0 and nx.is_connected(G)
    info["diameter"] = nx.diameter(G) if connected else np.inf
    return pd.Series(info)


def valued_density(G, weight="weight", max_value=None):
    """Sum of tie values / possible ties; divide by max_value for multiplex data."""
    n = G.number_of_nodes()
    possible = n * (n - 1) if G.is_directed() else n * (n - 1) / 2
    total = sum(d.get(weight, 1) for _, _, d in G.edges(data=True))
    value = total / possible if possible else 0.0
    return value / max_value if max_value else value


def degree_stats(G):
    """Mean and population variance of degree (undirected: m = 2L/g;
    directed: in and out means are both L/g)."""
    g = G.number_of_nodes()
    if G.is_directed():
        ins = np.array([d for _, d in G.in_degree()])
        outs = np.array([d for _, d in G.out_degree()])
        return pd.Series({"lines": G.number_of_edges(), "in_mean": ins.mean(),
                          "in_var": ins.var(), "out_mean": outs.mean(),
                          "out_var": outs.var()})
    deg = np.array([d for _, d in G.degree()])
    return pd.Series({"lines": G.number_of_edges(), "mean": 2 * G.number_of_edges() / g,
                      "var": deg.var(), "sd": deg.std(), "max": deg.max(),
                      "min": deg.min()})


def directed_node_types(G):
    """isolate (in=0,out=0), transmitter (in=0), receiver (out=0), carrier (both>0)."""
    rows = []
    for n in G.nodes():
        i, o = G.in_degree(n), G.out_degree(n)
        kind = ("isolate" if i == 0 and o == 0 else "transmitter" if i == 0
                else "receiver" if o == 0 else "carrier")
        rows.append({"node": n, "in_degree": i, "out_degree": o, "type": kind})
    return pd.DataFrame(rows).set_index("node")


def ego_network(G, ego, radius=1):
    """Ego plus alters within `radius` steps (direction ignored)."""
    return nx.ego_graph(G, ego, radius=radius, undirected=True)


# ---------------------------------------------------------------------------
# Walks, paths, cycles, distances
# ---------------------------------------------------------------------------

def walks(G, source, target, max_length=4):
    """All walks up to max_length lines (nodes and lines may repeat)."""
    found = []

    def step(node, seq):
        if node == target and len(seq) > 1:
            found.append(list(seq))
        if len(seq) - 1 < max_length:
            for nb in G.neighbors(node):
                step(nb, seq + [nb])

    step(source, [source])
    return found


def paths(G, source, target, max_length=None):
    """Simple paths (no repeated nodes), shortest first."""
    return sorted(nx.all_simple_paths(G, source, target, cutoff=max_length), key=len)


def cycles(G, max_length=4):
    """Simple cycles with 3..max_length nodes (directed cycles may have 2)."""
    return sorted((c for c in nx.simple_cycles(G, length_bound=max_length)
                   if G.is_directed() or len(c) >= 3), key=lambda c: (len(c), str(c)))


def distances(G):
    """Geodesic distance matrix, diameter, radius, eccentricity, mean distance."""
    nodes = list(G.nodes())
    idx = {n: i for i, n in enumerate(nodes)}
    D = np.full((len(nodes), len(nodes)), np.inf)
    for u, lengths in nx.all_pairs_shortest_path_length(G):
        for v, d in lengths.items():
            D[idx[u], idx[v]] = d
    finite = D[np.isfinite(D) & (D > 0)]
    connected = (nx.is_strongly_connected(G) if G.is_directed()
                 else nx.is_connected(G))
    return {"matrix": pd.DataFrame(D, index=nodes, columns=nodes),
            "mean_distance": float(finite.mean()) if finite.size else np.inf,
            "diameter": nx.diameter(G) if connected else np.inf,
            "radius": nx.radius(G) if connected else np.inf,
            "eccentricity": pd.Series(nx.eccentricity(G)) if connected else None}


# ---------------------------------------------------------------------------
# Centrality and centralization
# ---------------------------------------------------------------------------

def centralities(G):
    """Relative degree, closeness and betweenness (plus in/out for digraphs)."""
    df = pd.DataFrame({"degree": nx.degree_centrality(G),
                       "closeness": nx.closeness_centrality(G),
                       "betweenness": nx.betweenness_centrality(G)})
    if G.is_directed():
        df["in_degree"] = pd.Series(nx.in_degree_centrality(G))
        df["out_degree"] = pd.Series(nx.out_degree_centrality(G))
    return df.sort_values("betweenness", ascending=False)


def extended_centralities(G):
    """Eigenvector, PageRank and Katz. Unconverged measures are left blank."""
    out = {}
    for name, func in [("eigenvector", lambda: nx.eigenvector_centrality(G, max_iter=1000)),
                       ("pagerank", lambda: nx.pagerank(G)),
                       ("katz", lambda: nx.katz_centrality_numpy(G))]:
        try:
            out[name] = func()
        except (nx.NetworkXException, np.linalg.LinAlgError) as err:
            warnings.warn(f"{name} not computed: {err}")
            out[name] = {n: np.nan for n in G.nodes()}
    return pd.DataFrame(out)


def _freeman(values, denominator):
    values = list(values)
    return sum(max(values) - v for v in values) / denominator if denominator else 0.0


def centralization(G):
    """Freeman (1979) centralization, 0 = equal, 1 = star.

    Undirected: degree (n-1)(n-2); betweenness (n-1)^2(n-2)/2 on raw scores;
    closeness (n-1)(n-2)/(2n-3) on relative closeness, connected graphs only.
    Directed: in/out degree (n-1)^2; betweenness (n-1)^2(n-2) (ordered pairs).
    """
    n = G.number_of_nodes()
    if n < 3:
        return pd.Series(dtype=float)
    raw_bc = nx.betweenness_centrality(G, normalized=False).values()
    if G.is_directed():
        return pd.Series({
            "in_degree": _freeman(dict(G.in_degree()).values(), (n - 1) ** 2),
            "out_degree": _freeman(dict(G.out_degree()).values(), (n - 1) ** 2),
            "betweenness": _freeman(raw_bc, (n - 1) ** 2 * (n - 2)),
            "closeness": np.nan})
    closeness = (_freeman(nx.closeness_centrality(G).values(),
                          (n - 1) * (n - 2) / (2 * n - 3))
                 if nx.is_connected(G) else np.nan)
    return pd.Series({
        "degree": _freeman(dict(G.degree()).values(), (n - 1) * (n - 2)),
        "betweenness": _freeman(raw_bc, (n - 1) ** 2 * (n - 2) / 2),
        "closeness": closeness})


# ---------------------------------------------------------------------------
# Brokerage: structural holes and openness
# ---------------------------------------------------------------------------

def structural_holes(G, weight=None):
    """Burt measures. redundancy = alters - effective size (= 2t/n when binary
    and undirected); efficiency = effective size / alters."""
    alters = pd.Series({n: len(set(nx.all_neighbors(G, n))) for n in G.nodes()})
    df = pd.DataFrame({"alters": alters,
                       "effective_size": pd.Series(nx.effective_size(G, weight=weight)),
                       "constraint": pd.Series(nx.constraint(G, weight=weight))})
    df["redundancy"] = df["alters"] - df["effective_size"]
    df["efficiency"] = (df["effective_size"] / df["alters"]).where(df["alters"] > 0)
    return df.sort_values("constraint")


def openness(G, groups):
    """Share of each group's tie ends that leave the group (0 closed, 1 open).
    Digraphs count outgoing ties."""
    groups = pd.Series(groups)
    result = {}
    for g in sorted(groups.unique(), key=str):
        members = set(groups[groups == g].index)
        ends = [nb in members for n in members for nb in G.neighbors(n)]
        result[g] = (len(ends) - sum(ends)) / len(ends) if ends else 0.0
    return pd.Series(result, name="openness")


# ---------------------------------------------------------------------------
# Cohesive subgroups
# ---------------------------------------------------------------------------

def components(G):
    """Components (weak and strong for digraphs) and isolates."""
    if G.is_directed():
        return {"weak": [sorted(c, key=str) for c in nx.weakly_connected_components(G)],
                "strong": [sorted(c, key=str) for c in nx.strongly_connected_components(G)],
                "isolates": list(nx.isolates(G))}
    return {"components": [sorted(c, key=str) for c in nx.connected_components(G)],
            "isolates": list(nx.isolates(G))}


def cutpoints(G):
    """Cut-points, bridges and knots (bicomponents split by cut-points)."""
    H = _as_undirected(G)
    return {"cutpoints": list(nx.articulation_points(H)),
            "bridges": list(nx.bridges(H)),
            "knots": [sorted(c, key=str) for c in nx.biconnected_components(H)]}


def cycle_components(G):
    """Groups of 3+ nodes that stay connected after removing all bridges."""
    H = _as_undirected(G)
    bridges = list(nx.bridges(H))
    H.remove_edges_from(bridges)
    comps = [sorted(c, key=str) for c in nx.connected_components(H) if len(c) >= 3]
    return {"cycle_components": sorted(comps, key=len, reverse=True), "bridges": bridges}


def k_cores(G):
    """Core number per node and, for each k, members and remainders."""
    core = nx.core_number(_as_undirected(G))
    n = len(core)
    rows = []
    for k in range(1, max(core.values(), default=0) + 2):
        members = sorted((v for v, c in core.items() if c >= k), key=str)
        rest = sorted((v for v, c in core.items() if c < k), key=str)
        rows.append({"k": k, "members": len(members), "remainders": len(rest),
                     "remainder_ratio": len(rest) / n if n else 0.0,
                     "member_list": members})
    return {"core_number": pd.Series(core), "table": pd.DataFrame(rows)}


def m_slices(G, m=2):
    """Keep ties with multiplicity >= m, return the kept graph and its
    components of 2+ nodes. Weighted graphs use the tie weight as multiplicity;
    binary graphs use the number of shared neighbours of the two ends."""
    H0 = _as_undirected(G)
    weighted = _is_weighted(H0)
    H = nx.Graph()
    H.add_nodes_from(H0.nodes())
    for u, v, d in H0.edges(data=True):
        mult = d.get("weight", 1) if weighted else len(set(H0[u]) & set(H0[v]))
        if mult >= m:
            H.add_edge(u, v, multiplicity=mult)
    comps = [sorted(c, key=str) for c in nx.connected_components(H) if len(c) >= 2]
    return {"graph": H, "slices": comps}


def cliques(G, min_size=MIN_CLIQUE_SIZE):
    """Maximal complete subgraphs with at least min_size nodes, largest first."""
    found = [sorted(c, key=str) for c in nx.find_cliques(_as_undirected(G))
             if len(c) >= min_size]
    return sorted(found, key=len, reverse=True)


def clique_membership(G, min_size=MIN_CLIQUE_SIZE):
    """How many cliques each node belongs to (overlap marks connectors)."""
    found = cliques(G, min_size)
    rows = [{"node": n, "cliques": sum(n in c for c in found),
             "clique_ids": [i + 1 for i, c in enumerate(found) if n in c]}
            for n in G.nodes()]
    return pd.DataFrame(rows).set_index("node").sort_values("cliques", ascending=False)


def _distance_power(H, n):
    P = nx.Graph()
    P.add_nodes_from(H.nodes())
    for u, lengths in nx.all_pairs_shortest_path_length(H, cutoff=n):
        P.add_edges_from((u, v) for v in lengths if v != u)
    return P


def n_cliques(G, n=2, min_size=MIN_CLIQUE_SIZE):
    """Maximal sets whose members are within distance n in the whole graph."""
    P = _distance_power(_as_undirected(G), n)
    found = [sorted(c, key=str) for c in nx.find_cliques(P) if len(c) >= min_size]
    return sorted(found, key=len, reverse=True)


def _diameter_within(H, members):
    S = H.subgraph(members)
    return nx.diameter(S) if nx.is_connected(S) else np.inf


def n_clans(G, n=2, min_size=MIN_CLIQUE_SIZE):
    """n-cliques whose diameter, measured inside the set, is at most n."""
    H = _as_undirected(G)
    return [c for c in n_cliques(G, n, min_size) if _diameter_within(H, c) <= n]


def n_clubs(G, n=2, min_size=MIN_CLIQUE_SIZE):
    """Candidate n-clubs: n-clans plus radius-n neighbourhoods with inner
    diameter <= n, keeping sets not contained in another candidate. This is a
    candidate search; it does not guarantee every maximal n-club."""
    H = _as_undirected(G)
    cands = {frozenset(c) for c in n_clans(G, n, min_size)}
    for v in H.nodes():
        ball = frozenset(nx.single_source_shortest_path_length(H, v, cutoff=n))
        if len(ball) >= min_size and _diameter_within(H, ball) <= n:
            cands.add(ball)
    maximal = [c for c in cands if not any(c < o for o in cands)]
    return sorted((sorted(c, key=str) for c in maximal), key=len, reverse=True)


# ---------------------------------------------------------------------------
# Equivalence and blockmodeling
# ---------------------------------------------------------------------------

def _adjacency(G, weight="weight"):
    nodes = list(G.nodes())
    return nodes, nx.to_numpy_array(G, nodelist=nodes, weight=weight if _is_weighted(G) else None)


def _profile_distance(A):
    """Euclidean distance between the row+column profiles of every pair,
    leaving out the pair's own cells (k = i, j), as in Wasserman & Faust."""
    R = squareform(pdist(A, "sqeuclidean"))
    C = squareform(pdist(A.T, "sqeuclidean"))
    d = np.diag(A)
    corr = ((d[:, None] - A.T) ** 2 + (A - d[None, :]) ** 2
            + (d[:, None] - A) ** 2 + (A.T - d[None, :]) ** 2)
    D = np.sqrt(np.clip(R + C - corr, 0, None))
    np.fill_diagonal(D, 0)
    return D


def se_distance(G):
    """Structural equivalence as Euclidean distance over rows and columns,
    excluding the pair's own cells (k = i, j). 0 = perfectly equivalent."""
    nodes, A = _adjacency(G)
    return pd.DataFrame(_profile_distance(A), index=nodes, columns=nodes)


def se_correlation(G):
    """Structural equivalence as Pearson correlation of each pair's row and
    column profiles, excluding k = i, j. +1 = perfectly equivalent.
    Profiles with zero variance (for example isolates) get 0."""
    nodes, A = _adjacency(G)
    n = len(nodes)
    M = np.eye(n)
    for i in range(n):
        for j in range(i + 1, n):
            keep = [k for k in range(n) if k not in (i, j)]
            x = np.concatenate([A[i, keep], A[keep, i]])
            y = np.concatenate([A[j, keep], A[keep, j]])
            r = np.corrcoef(x, y)[0, 1] if x.std() > 0 and y.std() > 0 else 0.0
            M[i, j] = M[j, i] = r
    return pd.DataFrame(M, index=nodes, columns=nodes)


def rege_similarity(G, max_iter=20, tol=1e-4):
    """Regular equivalence similarity in the REGE style (White & Reitz 1983),
    binary ties. Start at 1; each round, a pair's score is the average best
    match of their neighbours' scores, matched separately for out- and
    in-neighbours. Pairs where only one side has neighbours in a direction
    lose score. Converges to 1 for all non-isolated pairs in undirected binary
    graphs, so use it on directed data."""
    nodes = list(G.nodes())
    idx = {v: i for i, v in enumerate(nodes)}
    if G.is_directed():
        sides = [[[idx[u] for u in G.successors(v)] for v in nodes],
                 [[idx[u] for u in G.predecessors(v)] for v in nodes]]
    else:
        sides = [[[idx[u] for u in G.neighbors(v)] for v in nodes]]
    n = len(nodes)
    S = np.ones((n, n))
    for _ in range(max_iter):
        new = np.eye(n)
        for i in range(n):
            for j in range(i + 1, n):
                total, count = 0.0, 0
                for nb in sides:
                    a, b = nb[i], nb[j]
                    count += len(a) + len(b)
                    if a and b:
                        sub = S[np.ix_(a, b)]
                        total += sub.max(axis=1).sum() + sub.max(axis=0).sum()
                new[i, j] = new[j, i] = total / count if count else 1.0
        change = np.abs(new - S).max()
        S = new
        if change < tol:
            break
    return pd.DataFrame(S, index=nodes, columns=nodes)


def _concor_split(M0, members, max_iter=50, tol=1e-6):
    """Iterate correlations on the members' submatrix until entries reach +/-1,
    then split by sign relative to a reference member."""
    M = M0[np.ix_(members, members)]
    for _ in range(max_iter):
        with np.errstate(invalid="ignore", divide="ignore"):
            M = np.nan_to_num(np.corrcoef(M))
        if np.all(np.abs(np.abs(M) - 1) < tol):
            break
    # reference = member with the strongest correlations, so isolates
    # (all-zero rows) never decide the split
    ref = int(np.abs(M).sum(axis=1).argmax())
    left = [m for k, m in enumerate(members) if M[ref, k] > 0]
    right = [m for m in members if m not in left]
    return (left, right) if left and right else None


def concor(G, n_blocks=2):
    """CONCOR (Breiger, Boorman & Arabie 1975). Starts from se_correlation and
    keeps splitting the largest splittable block in two until n_blocks."""
    nodes = list(G.nodes())
    M0 = se_correlation(G).values
    blocks, frozen = [list(range(len(nodes)))], []
    while len(blocks) + len(frozen) < n_blocks and blocks:
        blocks.sort(key=len, reverse=True)
        target = blocks.pop(0)
        split = _concor_split(M0, target) if len(target) > 1 else None
        if split:
            blocks.extend(split)
        else:
            frozen.append(target)
    labels = {}
    for b, members in enumerate(sorted(blocks + frozen, key=min), start=1):
        labels.update({nodes[m]: b for m in members})
    return pd.Series(labels).loc[nodes]


def _cluster(distance_matrix, n_blocks, nodes):
    D = np.array(distance_matrix, dtype=float)
    np.fill_diagonal(D, 0)
    Z = linkage(squareform((D + D.T) / 2, checks=False), method="average")
    return pd.Series(fcluster(Z, n_blocks, criterion="maxclust"), index=nodes)


def blockmodel(G, n_blocks=3, method="euclidean"):
    """Assign nodes to blocks.

    euclidean: average-linkage clustering of se_distance
    concor:    repeated CONCOR splits
    structure: same distance as euclidean, computed on geodesic distances
               instead of ties (Burt 1976 STRUCTURE idea); unreachable pairs
               get distance n+1
    rege:      average-linkage clustering of 1 - rege_similarity
    """
    nodes = list(G.nodes())
    if method == "euclidean":
        return _cluster(se_distance(G).values, n_blocks, nodes)
    if method == "concor":
        return concor(G, n_blocks)
    if method == "structure":
        geo = distances(G)["matrix"].values.copy()
        geo[np.isinf(geo)] = len(nodes) + 1
        return _cluster(_profile_distance(geo), n_blocks, nodes)
    if method == "rege":
        return _cluster(1 - rege_similarity(G).values, n_blocks, nodes)
    raise ValueError("method must be euclidean, concor, structure or rege")


def block_density(G, blocks):
    """Tie density inside and between blocks (self-ties excluded)."""
    blocks = pd.Series(blocks)
    nodes, A = _adjacency(G, weight=None)
    A = (A > 0).astype(float)
    labels = sorted(blocks.unique(), key=str)
    out = pd.DataFrame(index=labels, columns=labels, dtype=float)
    for b1 in labels:
        r = [k for k, v in enumerate(nodes) if blocks[v] == b1]
        for b2 in labels:
            c = [k for k, v in enumerate(nodes) if blocks[v] == b2]
            sub = A[np.ix_(r, c)]
            cells = len(r) * len(c) - (len(r) if b1 == b2 else 0)
            ties = sub.sum() - (np.trace(sub) if b1 == b2 else 0)
            out.loc[b1, b2] = ties / cells if cells else np.nan
    return out


def image_matrix(G, blocks, criterion="alpha", alpha=None):
    """Block-to-block image.
    alpha:   1 if block density >= alpha (default alpha = whole-network density)
    zero:    1 if the block has any tie (zeroblock criterion)
    one:     1 only if the block is complete (oneblock criterion)
    perfect: 1 complete, 0 empty, NaN mixed (NaN cells show imperfect fit)"""
    dens = block_density(G, blocks)
    if criterion == "alpha":
        cut = nx.density(G) if alpha is None else alpha
        return (dens >= cut).astype(int)
    if criterion == "zero":
        return (dens > 0).astype(int)
    if criterion == "one":
        return (dens >= 1).astype(int)
    if criterion == "perfect":
        return dens.map(lambda x: 1.0 if x >= 1 else 0.0 if x == 0 else np.nan)
    raise ValueError("criterion must be alpha, zero, one or perfect")


# ---------------------------------------------------------------------------
# Large networks
# ---------------------------------------------------------------------------

def recommend_strategy(G):
    """Default handling by node count (readability thresholds, not statistics)."""
    n = G.number_of_nodes()
    if n <= MATRIX_INLINE_MAX_NODES:
        plan = ("full", "full matrix and graph", "all methods")
    elif n <= FILTER_MAX_NODES:
        plan = ("filtered", "top-k subgraph", "all methods; REGE and clustering are slow")
    elif n <= AGGREGATE_MAX_NODES:
        plan = ("aggregated", "block-reduced graph", "Louvain for grouping")
    else:
        plan = ("summary_only", "statistics and distributions", "Louvain for grouping")
    return {"nodes": n, "ties": G.number_of_edges(), "strategy": plan[0],
            "visualization": plan[1], "algorithms": plan[2]}


def top_k_subgraph(G, k=MATRIX_INLINE_MAX_NODES, by="betweenness"):
    """Subgraph of the k highest-scoring nodes."""
    scorers = {"betweenness": nx.betweenness_centrality,
               "degree": lambda H: dict(H.degree()),
               "closeness": nx.closeness_centrality, "pagerank": nx.pagerank}
    scores = scorers[by](G)
    keep = sorted(scores, key=lambda v: -scores[v])[:k]
    return G.subgraph(keep).copy()


def core_subgraph(G, min_degree=3):
    """Drop nodes whose degree is below min_degree (single pass)."""
    return G.subgraph([v for v, d in G.degree() if d >= min_degree]).copy()


def louvain(G, seed=SEED):
    """Modularity communities. Louvain shuffles node order, so the seed is
    fixed for repeatable results."""
    comms = nx.community.louvain_communities(G, seed=seed)
    return pd.Series({v: i for i, c in enumerate(comms, start=1) for v in c},
                     name="community")


def reduce_to_blocks(G, blocks):
    """One node per block; tie weight = number of ties between blocks."""
    blocks = pd.Series(blocks)
    R = nx.DiGraph() if G.is_directed() else nx.Graph()
    R.add_nodes_from(f"B{b}" for b in sorted(blocks.unique(), key=str))
    for u, v in G.edges():
        a, b = f"B{blocks[u]}", f"B{blocks[v]}"
        if a != b:
            w = R[a][b]["weight"] + 1 if R.has_edge(a, b) else 1
            R.add_edge(a, b, weight=w)
    return R


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def df_markdown(df, digits=3):
    """DataFrame -> markdown table without extra dependencies."""
    def fmt(x):
        if isinstance(x, (float, np.floating)):
            return "" if np.isnan(x) else f"{x:.{digits}f}"
        return str(x)
    head = "| | " + " | ".join(map(str, df.columns)) + " |"
    sep = "|---|" + "---|" * len(df.columns)
    rows = ["| **" + str(i) + "** | " + " | ".join(fmt(v) for v in r) + " |"
            for i, r in zip(df.index, df.itertuples(index=False))]
    return "\n".join([head, sep] + rows)


def matrix_markdown(G, groups=None, max_nodes=MATRIX_INLINE_MAX_NODES, top_by="degree"):
    """Adjacency matrix as markdown. Larger graphs keep the top max_nodes
    nodes by `top_by`; `groups` reorders rows and columns by block."""
    note = ""
    if G.number_of_nodes() > max_nodes:
        note = f"(top {max_nodes} of {G.number_of_nodes()} nodes by {top_by})\n\n"
        G = top_k_subgraph(G, max_nodes, by=top_by)
    nodes = list(G.nodes())
    if groups is not None:
        nodes = sorted(nodes, key=lambda v: (str(groups[v]), str(v)))
    A = nx.to_numpy_array(G, nodelist=nodes, weight="weight" if _is_weighted(G) else None)
    df = pd.DataFrame(A, index=nodes, columns=nodes)
    return note + df_markdown(df if _is_weighted(G) else df.astype(int), digits=1)


# ---------------------------------------------------------------------------
# Figures
# ---------------------------------------------------------------------------

def _layout(G, layout="auto"):
    """auto: up to FILTER_MAX_NODES nodes, Kamada-Kawai positions refined by
    a short seeded spring run (even spacing, and structurally identical nodes
    no longer sit on the same spot); seeded spring layout above that."""
    G = G.to_undirected() if G.is_directed() else G   # direction does not change placement
    if layout == "auto":
        if G.number_of_nodes() > FILTER_MAX_NODES:
            return nx.spring_layout(G, seed=SEED, k=SPRING_K)
        start = nx.kamada_kawai_layout(G)
        return nx.spring_layout(G, pos=start, seed=SEED, iterations=AUTO_REFINE_STEPS)
    if layout == "circular":
        return nx.circular_layout(G)
    if layout == "kamada_kawai":
        return nx.kamada_kawai_layout(G)
    if layout == "shell":
        return nx.shell_layout(G)
    return nx.spring_layout(G, seed=SEED, k=SPRING_K)


def _save(fig, path):
    folder = os.path.dirname(os.path.abspath(path))
    os.makedirs(folder, exist_ok=True)
    fig.savefig(path, dpi=FIG_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    if not os.path.exists(path):
        raise RuntimeError(f"figure not written: {path}")
    return path


def plot_matrix(G, path, groups=None, title=None):
    """Adjacency heatmap; block boundaries drawn when groups are given."""
    setup_font()
    nodes = list(G.nodes())
    if groups is not None:
        nodes = sorted(nodes, key=lambda v: (str(groups[v]), str(v)))
    A = nx.to_numpy_array(G, nodelist=nodes, weight="weight" if _is_weighted(G) else None)
    n = len(nodes)
    size = max(6, min(10, n * 0.4))
    fig, ax = plt.subplots(figsize=(size, size))
    ax.imshow(A, cmap=_heat_cmap(), vmin=0, vmax=max(A.max(), 1))
    ax.set_xticks(range(n), [str(v) for v in nodes], rotation=45, ha="right",
                  fontsize=10, fontweight="bold")
    ax.set_yticks(range(n), [str(v) for v in nodes], fontsize=10, fontweight="bold")
    ax.set_xticks(np.arange(-0.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which="minor", color=PALETTE["grid"], linewidth=0.8, alpha=0.6)
    ax.tick_params(which="minor", length=0)
    if n <= MATRIX_CELL_VALUE_MAX_NODES:
        for i in range(n):
            for j in range(n):
                if A[i, j]:
                    ax.text(j, i, f"{A[i, j]:g}", ha="center", va="center",
                            fontsize=9, fontweight="bold")
    if groups is not None:
        edge = 0
        sizes = pd.Series([groups[v] for v in nodes]).value_counts(sort=False)
        for b in sorted(sizes.index, key=str)[:-1]:
            edge += sizes[b]
            ax.axhline(edge - 0.5, color=PALETTE["accent"], linewidth=2.5)
            ax.axvline(edge - 0.5, color=PALETTE["accent"], linewidth=2.5)
    for spine in ax.spines.values():
        spine.set_color(PALETTE["frame"])
    if title:
        ax.set_title(title, fontsize=13, fontweight="bold")
    return _save(fig, path)


def plot_network(G, path, values=None, groups=None, layout="auto", title=None):
    """Graph drawing. `values` (dict) scales node size and colour;
    `groups` (dict) colours nodes by group and adds a legend."""
    setup_font()
    values = None if values is None else dict(values)
    groups = None if groups is None else dict(groups)
    nodes = list(G.nodes())
    size = max(8, min(12, G.number_of_nodes() * 0.5))
    fig, ax = plt.subplots(figsize=(size, size * 0.85))
    pos = _layout(G, layout)
    color, sizes = PALETTE["node"], 700
    if groups is not None:
        labels = sorted(set(groups.values()), key=str)
        cmap = {g: GROUP_COLORS[i % len(GROUP_COLORS)] for i, g in enumerate(labels)}
        color = [cmap[groups[v]] for v in nodes]
        ax.legend(handles=[Patch(facecolor=cmap[g], label=str(g)) for g in labels],
                  loc="upper right", frameon=False, fontsize=10)
    elif values is not None:
        lo, hi = min(values.values()), max(values.values())
        span = (hi - lo) or 1
        scaled = [(values[v] - lo) / span for v in nodes]
        color = [_heat_cmap()(0.35 + 0.65 * s) for s in scaled]
        sizes = [300 + 1200 * s for s in scaled]
    arrow_opts = ({"arrows": True, "arrowsize": 15, "node_size": sizes}
                  if G.is_directed() else {})
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color=PALETTE["edge"], alpha=0.75,
                           width=1.2, **arrow_opts)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=color, node_size=sizes,
                           edgecolors=PALETTE["node_edge"], linewidths=1.5)
    texts = [ax.text(x, y, str(v), fontsize=11, fontweight="bold", ha="center",
                     va="center") for v, (x, y) in pos.items()]
    try:
        from adjustText import adjust_text
        if G.number_of_nodes() > MATRIX_INLINE_MAX_NODES:
            adjust_text(texts, ax=ax)
    except ImportError:
        pass
    ax.set_axis_off()
    if title:
        ax.set_title(title, fontsize=13, fontweight="bold")
    return _save(fig, path)


def matrix_and_network(G, out_prefix, title=None, values=None, groups=None, layout="auto"):
    """Standard output for one analysis: matrix markdown plus two PNG files
    (<prefix>_matrix.png, <prefix>_network.png). Graphs above the inline
    limit get the network figure only."""
    result = {"markdown": matrix_markdown(G, groups=groups)}
    if G.number_of_nodes() <= MATRIX_INLINE_MAX_NODES:
        result["matrix_png"] = plot_matrix(G, f"{out_prefix}_matrix.png", groups, title)
    result["network_png"] = plot_network(G, f"{out_prefix}_network.png", values,
                                         groups, layout, title)
    return result


def plot_bipartite(result, path, title=None):
    """People (circles, left) and activities (squares, right)."""
    setup_font()
    B, people, acts = result["bipartite"], result["people"], result["activities"]
    fig, ax = plt.subplots(figsize=(10, max(5, 0.6 * max(len(people), len(acts)))))
    pos = {p: (0, -i) for i, p in enumerate(people)}
    pos.update({a: (2, -i) for i, a in enumerate(acts)})
    nx.draw_networkx_edges(B, pos, ax=ax, edge_color=PALETTE["edge"], alpha=0.75)
    nx.draw_networkx_nodes(B, pos, nodelist=people, ax=ax, node_color=PALETTE["node"],
                           node_size=700, edgecolors=PALETTE["node_edge"])
    nx.draw_networkx_nodes(B, pos, nodelist=acts, ax=ax, node_color=PALETTE["accent"],
                           node_shape="s", node_size=700, edgecolors=PALETTE["node_edge"])
    nx.draw_networkx_labels(B, pos, ax=ax, font_size=10, font_weight="bold",
                            font_family=setup_font())
    ax.set_axis_off()
    if title:
        ax.set_title(title, fontsize=13, fontweight="bold")
    return _save(fig, path)


def plot_centrality_bars(df, path, columns=("degree", "closeness", "betweenness"),
                         top_n=10, title=None):
    """Grouped bars for the top_n nodes by the last column, values labelled."""
    setup_font()
    top = df.sort_values(columns[-1], ascending=False).head(top_n)
    width = 0.8 / len(columns)
    fig, ax = plt.subplots(figsize=(max(9, top_n * 1.1), 5.5))
    x = np.arange(len(top))
    for k, col in enumerate(columns):
        bars = ax.bar(x + (k - (len(columns) - 1) / 2) * width, top[col], width,
                      label=col, color=GROUP_COLORS[k])
        ax.bar_label(bars, fmt="%.2f", fontsize=9, fontweight="bold")
    ax.set_xticks(x, [str(v) for v in top.index], fontweight="bold",
                  rotation=30, ha="right")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.set_yticks([])
    ax.set_ylim(0, top[list(columns)].to_numpy().max() * 1.12)
    ax.legend(frameon=False, ncol=len(columns), loc="lower center",
              bbox_to_anchor=(0.5, 1.0))
    if title:
        ax.set_title(title, fontsize=13, fontweight="bold", pad=30)
    return _save(fig, path)


def plot_degree_histogram(G, path, title=None, xlabel="degree", ylabel="nodes"):
    """Degree distribution for networks too large to draw node by node."""
    setup_font()
    counts = pd.Series([d for _, d in G.degree()]).value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(counts.index, counts.values, color=GROUP_COLORS[0])
    if len(counts) <= MATRIX_INLINE_MAX_NODES:
        ax.bar_label(bars, fontsize=9, fontweight="bold")
    ax.set_xlabel(xlabel, fontweight="bold")
    ax.set_ylabel(ylabel, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    if title:
        ax.set_title(title, fontsize=13, fontweight="bold")
    return _save(fig, path)


def plot_uzzi_concept(path, position=None, labels=None):
    """Concept sketch of Uzzi (1997): benefits rise with embeddedness up to a
    threshold, then fall. The curve and threshold are illustrative only, so
    the axes carry no numbers. `position` (0-1) marks a relative location."""
    setup_font()
    labels = labels or {"x": "Embeddedness", "y": "Performance",
                        "threshold": "Threshold", "left": "Benefits dominate",
                        "right": "Closure costs dominate"}
    x = np.linspace(0, 1, 200)
    curve = lambda t: 1 - 4 * (t - 0.5) ** 2
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x, curve(x), color=PALETTE["node_edge"], linewidth=3)
    ax.axvline(0.5, color=PALETTE["accent"], linestyle="--", linewidth=2)
    ax.text(0.5, 1.05, labels["threshold"], ha="center", fontweight="bold",
            bbox={"facecolor": "white", "edgecolor": "none"})
    ax.text(0.2, 0.3, labels["left"], ha="center", fontweight="bold")
    ax.text(0.8, 0.3, labels["right"], ha="center", fontweight="bold")
    if position is not None:
        ax.scatter([position], [curve(position)], s=200, color=PALETTE["accent"], zorder=5)
    ax.set_xlabel(labels["x"], fontweight="bold")
    ax.set_ylabel(labels["y"], fontweight="bold")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0, 1.15)
    ax.spines[["top", "right"]].set_visible(False)
    return _save(fig, path)
