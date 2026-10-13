"""
nx_toolkit: social network analysis helpers built on NetworkX.

Every number reported by the skill is computed here so results can be
reproduced by anyone who runs the same code on the same data.

Quick start:
    from nx_toolkit import *
    setup_font()
    G = load_from_matrix([[0, 1, 1], [1, 0, 0], [1, 0, 0]], labels=["A", "B", "C"])
    cent = compute_centralities(G)
    result = draw_matrix_and_network(G, title="Sample", save_path="outputs/sample.png")
    print(build_response_block(G, "Sample", result, cent))

Output language of table columns, captions and chart text is set by LANG.

This English edition was translated from the Korean edition. Labels and
messages may not carry the original intent exactly.
"""

import math
import os
import subprocess
import warnings

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import pdist, squareform


# =============================================================================
# Configuration
# =============================================================================

LANG = "en"  # "ko" or "en": language of labels in tables and charts

MATRIX_INLINE_MAX_NODES = 30      # above this, matrices are excerpted
HEATMAP_VALUE_MAX_NODES = 20      # above this, heatmap cells show no numbers
STRATEGY_FULL_MAX = 30            # recommend_strategy size thresholds
STRATEGY_FILTERED_MAX = 100
STRATEGY_AGGREGATED_MAX = 500
LAYOUT_SEED = 42                  # fixed seed keeps layouts reproducible
COMMUNITY_SEED = 42
SAVE_DPI = 150
FONT_INSTALL_TIMEOUT_SEC = 120

PALETTE = {
    "primary": "#8FB8D4",        # node fill
    "primary_light": "#B8D1E2",
    "primary_pale": "#E0EBF3",
    "primary_deep": "#6B9BBD",
    "primary_edge": "#5783A8",   # node border
    "accent": "#E5A785",         # highlight and block borders
    "neutral": "#7A95A8",        # edges
    "muted": "#8FA3B3",          # heatmap grid
}

BLOCK_COLORS = [
    "#8FB8D4", "#A5CDB5", "#EDC491", "#CFB0CF", "#B8B8B8",
    "#9FC7CF", "#E5B5B5", "#C0CBA5", "#D6C7A5", "#B8ADC8",
]

HEATMAP_COLORS = ["#FFFFFF", "#E0EBF3", "#C5DEF0", "#9FC5DF", "#7DAECC"]

CENTRALITY_BAR_COLORS = ("#4A90B8", "#6DB39A", "#E0A75C")

TEXT = {
    "ko": {
        # generic
        "nodes": "노드_수", "edges": "엣지_수", "density": "밀도",
        "mean_degree": "평균_연결정도", "directed": "방향_그래프",
        "components": "컴퍼넌트_수", "weak_components": "약한_컴퍼넌트_수",
        "strong_components": "강한_컴퍼넌트_수", "diameter": "직경",
        "largest_component": "최대_컴퍼넌트_크기",
        "largest_component_share": "최대_컴퍼넌트_비율",
        "degree_mean": "연결정도_평균", "degree_median": "연결정도_중앙값",
        "degree_std": "연결정도_표준편차", "degree_max": "연결정도_최대",
        "degree_min": "연결정도_최소",
        # strategy
        "viz_full": "매트릭스와 그래프 병행 시각화",
        "viz_filtered": "상위 K개 노드 추출 후 시각화",
        "viz_aggregated": "블록 단위 축소 그래프로 시각화",
        "viz_summary": "통계 테이블과 분포 차트만 제시",
        "alg_full": "모든 알고리즘 사용 가능",
        "alg_filtered": "REGE와 계층 군집은 계산 시간 증가에 유의",
        "alg_aggregated": "CONCOR 대신 Louvain 커뮤니티 탐색 권장",
        "alg_summary": "Louvain 또는 Label Propagation만 권장",
        "warn_heatmap": "매트릭스 히트맵 가독성 저하",
        "warn_labels": "노드 라벨 중첩 우려",
        "warn_matrix_useless": "매트릭스 시각화 실용성 낮음",
        "warn_rege_slow": "REGE 계산에 수 분 이상 소요 가능",
        "warn_cluster_memory": "계층 군집 메모리 부담",
        "warn_no_full_viz": "네트워크 전체 시각화 불가",
        "warn_node_level": "개별 노드 단위 해석의 실익 낮음",
        "warn_subnetwork": "하위 네트워크 추출 후 분석 권장",
        # node classes
        "degree": "연결정도", "indegree": "인디그리", "outdegree": "아웃디그리",
        "class": "분류", "node": "노드",
        "isolate": "고립(isolated)", "connected": "연결",
        "transmitter": "전달자(transmitter)", "receiver": "수신자(receiver)",
        "carrier": "매개자(carrier)",
        # degree stats
        "lines": "라인_수", "variance": "분산", "std": "표준편차",
        "max": "최대", "min": "최소",
        "in_mean": "인디그리_평균", "in_var": "인디그리_분산", "in_std": "인디그리_표준편차",
        "out_mean": "아웃디그리_평균", "out_var": "아웃디그리_분산", "out_std": "아웃디그리_표준편차",
        # density
        "isolates": "고립점_수", "inclusiveness": "포괄성_비율",
        # centrality
        "c_degree": "연결정도_중심성", "c_closeness": "근접_중심성",
        "c_betweenness": "매개_중심성", "c_in": "내향_중심성", "c_out": "외향_중심성",
        "z_degree": "연결정도_집중도", "z_in": "내향_연결정도_집중도",
        "z_out": "외향_연결정도_집중도", "z_closeness": "근접_집중도",
        "z_betweenness": "매개_집중도",
        "openness": "공개성",
        # subgroups
        "component_list": "컴퍼넌트", "weak_list": "약한_컴퍼넌트",
        "strong_list": "강한_컴퍼넌트", "isolate_list": "고립점",
        "cut_points": "연계점", "bridges": "브릿지", "max_k": "최대_k",
        "k": "k", "core_members": "핵심구성원_수", "residuals": "잔류점_수",
        "residual_share": "잔류점_비율", "residual_list": "잔류점_목록",
        "cycle_components": "사이클_컴퍼넌트", "removed_bridges": "제거된_브릿지",
        "clique_count": "참여_파당_수", "clique_ids": "파당_번호",
        "block_name": "블록{b}",
        # markdown
        "matrix_label": "인접 매트릭스",
        "matrix_excerpt": "(전체 {total}노드 중 {by} 상위 {k}개 발췌, 전체 매트릭스는 CSV 파일로 제공)",
        "matrix_reordered": "(블록 재정렬)",
        "block_prefix": "블록 {b}",
        "block_summary_label": "블록 간 밀도 요약",
        "block_header": "블록{b}({n}명)",
        "block_summary_caption": "(원본 {n}노드를 {k}블록으로 축소)",
        "section_matrix": "입력 데이터 매트릭스",
        "section_result": "분석 결과",
        "section_visual": "시각화",
        "result_suffix": "결과",
        "visual_note": "매트릭스 이미지와 네트워크 그래프 이미지는 파일로 별도 전달",
        "matrix_file": "매트릭스 파일",
        "network_file": "네트워크 파일",
        # charts
        "title_network": "네트워크 구조", "title_centrality": "중심성 분석",
        "title_groups": "하위집단 구조", "title_comparison": "중심성 비교",
        "title_kcore": "k-core 네스팅 구조",
        "title_uzzi": "배태성과 경제적 성과의 역U자 관계 (개념도)",
        "title_bipartite": "이분 네트워크 (사람과 활동)",
        "title_analysis": "네트워크 분석",
        "suffix_matrix": "인접 매트릭스", "suffix_network": "네트워크 그래프",
        "group": "그룹 {g}", "people": "사람", "activity": "활동",
        "bar_degree": "연결정도", "bar_closeness": "근접", "bar_betweenness": "매개",
        "axis_centrality": "중심성 값",
        "uzzi_threshold": "임계점",
        "uzzi_left": "긍정 효과 우세\n신뢰와 정보 공유\n공동 문제 해결",
        "uzzi_right": "부정 효과 우세\n외부 충격에 취약\n외부 정보 차단",
        "uzzi_current": "현재 위치\n({v:.2f})",
        "uzzi_x": "배태성 수준", "uzzi_y": "경제적 성과",
    },
    "en": {
        "nodes": "nodes", "edges": "edges", "density": "density",
        "mean_degree": "mean_degree", "directed": "directed",
        "components": "components", "weak_components": "weak_components",
        "strong_components": "strong_components", "diameter": "diameter",
        "largest_component": "largest_component_size",
        "largest_component_share": "largest_component_share",
        "degree_mean": "degree_mean", "degree_median": "degree_median",
        "degree_std": "degree_std", "degree_max": "degree_max",
        "degree_min": "degree_min",
        "viz_full": "Show matrix and graph side by side",
        "viz_filtered": "Extract top K nodes, then visualize",
        "viz_aggregated": "Visualize a block-level reduced graph",
        "viz_summary": "Show summary tables and distribution charts only",
        "alg_full": "All algorithms are usable",
        "alg_filtered": "REGE and hierarchical clustering take longer",
        "alg_aggregated": "Use Louvain community detection instead of CONCOR",
        "alg_summary": "Use Louvain or Label Propagation only",
        "warn_heatmap": "Matrix heatmap becomes hard to read",
        "warn_labels": "Node labels may overlap",
        "warn_matrix_useless": "Matrix visualization has little practical value",
        "warn_rege_slow": "REGE may take several minutes",
        "warn_cluster_memory": "Hierarchical clustering needs a lot of memory",
        "warn_no_full_viz": "The whole network cannot be drawn legibly",
        "warn_node_level": "Node-by-node interpretation adds little",
        "warn_subnetwork": "Extract a subnetwork before detailed analysis",
        "degree": "degree", "indegree": "indegree", "outdegree": "outdegree",
        "class": "class", "node": "node",
        "isolate": "isolate", "connected": "connected",
        "transmitter": "transmitter", "receiver": "receiver",
        "carrier": "carrier",
        "lines": "lines", "variance": "variance", "std": "std",
        "max": "max", "min": "min",
        "in_mean": "indegree_mean", "in_var": "indegree_variance", "in_std": "indegree_std",
        "out_mean": "outdegree_mean", "out_var": "outdegree_variance", "out_std": "outdegree_std",
        "isolates": "isolates", "inclusiveness": "inclusiveness",
        "c_degree": "degree_centrality", "c_closeness": "closeness_centrality",
        "c_betweenness": "betweenness_centrality", "c_in": "in_centrality",
        "c_out": "out_centrality",
        "z_degree": "degree_centralization", "z_in": "in_degree_centralization",
        "z_out": "out_degree_centralization", "z_closeness": "closeness_centralization",
        "z_betweenness": "betweenness_centralization",
        "openness": "openness",
        "component_list": "components", "weak_list": "weak_components",
        "strong_list": "strong_components", "isolate_list": "isolates",
        "cut_points": "cut_points", "bridges": "bridges", "max_k": "max_k",
        "k": "k", "core_members": "core_members", "residuals": "residuals",
        "residual_share": "residual_share", "residual_list": "residual_list",
        "cycle_components": "cycle_components", "removed_bridges": "removed_bridges",
        "clique_count": "clique_count", "clique_ids": "clique_ids",
        "block_name": "Block{b}",
        "matrix_label": "Adjacency matrix",
        "matrix_excerpt": "(top {k} of {total} nodes by {by}, with the full matrix provided as a CSV file)",
        "matrix_reordered": "(reordered by block)",
        "block_prefix": "Block {b}",
        "block_summary_label": "Density between blocks",
        "block_header": "Block{b}(n={n})",
        "block_summary_caption": "({n} nodes reduced to {k} blocks)",
        "section_matrix": "Input matrix",
        "section_result": "Results",
        "section_visual": "Visualization",
        "result_suffix": "results",
        "visual_note": "Matrix and network graph images are delivered as separate files",
        "matrix_file": "Matrix file",
        "network_file": "Network file",
        "title_network": "Network structure", "title_centrality": "Centrality",
        "title_groups": "Subgroups", "title_comparison": "Centrality comparison",
        "title_kcore": "k-core nesting",
        "title_uzzi": "Inverted U between embeddedness and performance (schematic)",
        "title_bipartite": "Two-mode network (people and activities)",
        "title_analysis": "Network analysis",
        "suffix_matrix": "adjacency matrix", "suffix_network": "network graph",
        "group": "Group {g}", "people": "People", "activity": "Activity",
        "bar_degree": "Degree", "bar_closeness": "Closeness", "bar_betweenness": "Betweenness",
        "axis_centrality": "Centrality",
        "uzzi_threshold": "Threshold",
        "uzzi_left": "Benefits dominate\ntrust and information sharing\njoint problem-solving",
        "uzzi_right": "Costs dominate\nvulnerable to shocks\ninsulated from outside",
        "uzzi_current": "Current\n({v:.2f})",
        "uzzi_x": "Embeddedness", "uzzi_y": "Economic performance",
    },
}


def _t(key, **kwargs):
    """Return the label for key in the configured language."""
    text = TEXT.get(LANG, TEXT["en"]).get(key, key)
    return text.format(**kwargs) if kwargs else text


def _as_series(assignment):
    """Accept a dict or Series of node assignments and return a Series."""
    if isinstance(assignment, pd.Series):
        return assignment
    return pd.Series(assignment)


def _undirected_simple(G):
    """Undirected copy without self-loops, used by cohesion measures."""
    H = G.to_undirected() if G.is_directed() else G.copy()
    H.remove_edges_from(list(nx.selfloop_edges(H)))
    return H


def _is_weighted(G):
    return any("weight" in data for _, _, data in G.edges(data=True))


# =============================================================================
# Font
# =============================================================================

def _find_nanum_fonts():
    regular, bold = None, None
    for path in fm.findSystemFonts():
        name = os.path.basename(path)
        if name == "NanumGothic.ttf":
            regular = path
        elif name == "NanumGothicBold.ttf":
            bold = path
    return regular, bold


_FONT_READY = False


def _ensure_font():
    """Run setup_font() once before the first chart if the caller has not."""
    if not _FONT_READY:
        setup_font()


def setup_font(install_if_missing=False):
    """
    Register NanumGothic so Korean labels render. Latin text also renders.

    install_if_missing=True runs `apt-get install fonts-nanum`. Use it only in a
    disposable sandbox where installing system packages is allowed.
    Returns True when NanumGothic is active, False when DejaVu Sans is used.
    """
    global _FONT_READY
    _FONT_READY = True
    regular, bold = _find_nanum_fonts()
    if regular is None and install_if_missing:
        try:
            subprocess.run(["apt-get", "install", "-y", "fonts-nanum"],
                           check=False, capture_output=True,
                           timeout=FONT_INSTALL_TIMEOUT_SEC)
            subprocess.run(["fc-cache", "-f"], check=False, capture_output=True,
                           timeout=FONT_INSTALL_TIMEOUT_SEC)
            regular, bold = _find_nanum_fonts()
        except (OSError, subprocess.SubprocessError):
            regular = None

    if regular:
        fm.fontManager.addfont(regular)
        if bold:
            fm.fontManager.addfont(bold)
        name = fm.FontProperties(fname=regular).get_name()
        plt.rcParams["font.family"] = [name, "DejaVu Sans"]
        plt.rcParams["font.sans-serif"] = [name, "DejaVu Sans"]
    else:
        plt.rcParams["font.family"] = "DejaVu Sans"
        warnings.warn("NanumGothic not found. Korean characters may not render; "
                      "install the fonts-nanum package or call "
                      "setup_font(install_if_missing=True) in a sandbox.")
    plt.rcParams["axes.unicode_minus"] = False
    return regular is not None


# =============================================================================
# Loading data
# =============================================================================

def load_from_matrix(matrix, labels=None, directed=False, weighted=False):
    """
    Build a graph from an adjacency matrix. Nonzero off-diagonal cells become
    ties. weighted=True stores cell values as the 'weight' attribute.
    """
    arr = np.asarray(matrix, dtype=float)
    if arr.ndim != 2 or arr.shape[0] != arr.shape[1]:
        raise ValueError("Adjacency matrix must be square.")
    n = arr.shape[0]
    labels = list(range(n)) if labels is None else list(labels)
    if len(labels) != n:
        raise ValueError("Number of labels must equal matrix size.")

    G = nx.DiGraph() if directed else nx.Graph()
    G.add_nodes_from(labels)
    for i in range(n):
        for j in range(n):
            if i == j or arr[i, j] == 0:
                continue
            if weighted:
                G.add_edge(labels[i], labels[j], weight=float(arr[i, j]))
            else:
                G.add_edge(labels[i], labels[j])
    return G


def load_from_edges(edges, directed=False, weighted=False):
    """Build a graph from (u, v) pairs, or (u, v, weight) when weighted."""
    G = nx.DiGraph() if directed else nx.Graph()
    if weighted:
        G.add_weighted_edges_from(edges)
    else:
        G.add_edges_from((e[0], e[1]) for e in edges)
    return G


def auto_detect_format(df):
    """
    Guess the table layout: 3 or fewer columns -> 'edges', square table
    (optionally with a label column) -> 'matrix', otherwise 'incidence'.
    """
    n_rows, n_cols = df.shape
    if n_cols <= 3:
        return "edges"
    if n_rows == n_cols or n_rows == n_cols - 1:
        return "matrix"
    return "incidence"


def _graph_from_dataframe(df, format, directed, weighted):
    if format is None:
        format = auto_detect_format(df)

    if format == "edges":
        cols = df.columns.tolist()
        if weighted and len(cols) >= 3:
            edges = list(df[cols[:3]].itertuples(index=False, name=None))
        else:
            edges = list(df[cols[:2]].itertuples(index=False, name=None))
        return load_from_edges(edges, directed=directed, weighted=weighted)

    if format == "matrix":
        if df.shape[0] == df.shape[1] - 1:
            df = df.set_index(df.columns[0])
        return load_from_matrix(df.values, labels=df.columns.tolist(),
                                directed=directed, weighted=weighted)

    if format == "incidence":
        if not pd.api.types.is_numeric_dtype(df[df.columns[0]]):
            df = df.set_index(df.columns[0])
        return load_from_incidence(df)

    raise ValueError(f"Unknown format: {format}")


def load_from_csv(path, format=None, directed=False, weighted=False,
                  encoding="utf-8", sep=","):
    """
    Load a network from CSV. format: 'edges', 'matrix', 'incidence' or None
    (auto). Use encoding='utf-8-sig' or 'cp949' when Korean text breaks.
    Incidence input returns the dict produced by load_from_incidence.
    """
    df = pd.read_csv(path, encoding=encoding, sep=sep)
    return _graph_from_dataframe(df, format, directed, weighted)


def load_from_excel(path, sheet_name=0, format=None, directed=False,
                    weighted=False):
    """Load a network from an Excel sheet (needs openpyxl for .xlsx)."""
    df = pd.read_excel(path, sheet_name=sheet_name)
    return _graph_from_dataframe(df, format, directed, weighted)


def export_to_csv(G, path, format="edges", encoding="utf-8-sig"):
    """Save as an edge list or an adjacency matrix. utf-8-sig opens cleanly in Excel."""
    if format == "edges":
        rows = []
        for u, v, data in G.edges(data=True):
            row = {"source": u, "target": v}
            if "weight" in data:
                row["weight"] = data["weight"]
            rows.append(row)
        pd.DataFrame(rows).to_csv(path, index=False, encoding=encoding)
    elif format == "matrix":
        nodes = list(G.nodes())
        A = nx.to_numpy_array(G, nodelist=nodes)
        pd.DataFrame(A, index=nodes, columns=nodes).to_csv(path, encoding=encoding)
    else:
        raise ValueError(f"Unknown format: {format}")


def load_from_incidence(affiliations, people_label="people",
                        activity_label="activity"):
    """
    Build a two-mode (people x activity) graph and its two one-mode
    projections. Projection edge weight = number of shared partners.

    affiliations: DataFrame (index people, columns activities, values > 0 mean
    membership) or dict {person: [activities]}.
    """
    B = nx.Graph()
    if isinstance(affiliations, dict):
        for person, acts in affiliations.items():
            B.add_node(person, bipartite=0, kind=people_label)
            for act in acts:
                B.add_node(act, bipartite=1, kind=activity_label)
                B.add_edge(person, act)
    elif isinstance(affiliations, pd.DataFrame):
        B.add_nodes_from(affiliations.index, bipartite=0, kind=people_label)
        B.add_nodes_from(affiliations.columns, bipartite=1, kind=activity_label)
        for person in affiliations.index:
            for act in affiliations.columns:
                if affiliations.loc[person, act] > 0:
                    B.add_edge(person, act)
    else:
        raise ValueError("affiliations must be a dict or a DataFrame")

    people = {n for n, d in B.nodes(data=True) if d.get("kind") == people_label}
    activities = {n for n, d in B.nodes(data=True) if d.get("kind") == activity_label}
    return {
        "bipartite": B,
        "people_projection": nx.bipartite.weighted_projected_graph(B, people),
        "activity_projection": nx.bipartite.weighted_projected_graph(B, activities),
    }


# =============================================================================
# Interoperability with Pajek, Gephi, GraphML and UCINET
# =============================================================================

def export_to_pajek(G, path):
    nx.write_pajek(G, path)


def import_from_pajek(path):
    return nx.read_pajek(path)


def export_to_graphml(G, path):
    nx.write_graphml(G, path)


def import_from_graphml(path):
    return nx.read_graphml(path)


def export_to_gephi(G, path):
    nx.write_gexf(G, path)


def import_from_gephi(path):
    return nx.read_gexf(path)


def _format_value(value):
    value = float(value)
    return str(int(value)) if value.is_integer() else repr(value)


def export_to_ucinet_dl(G, path, format="fullmatrix"):
    """
    Save as a UCINET DL file with embedded labels. format: 'fullmatrix' or
    'edgelist1'. Node labels must not contain spaces.
    """
    fmt = "edgelist1" if format in ("edgelist", "edgelist1") else format
    if fmt not in ("fullmatrix", "edgelist1"):
        raise ValueError(f"Unknown UCINET format: {format}")
    nodes = list(G.nodes())
    if any(" " in str(n) for n in nodes):
        raise ValueError("UCINET DL labels cannot contain spaces.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"DL N={len(nodes)}\n")
        f.write(f"FORMAT = {fmt.upper()}\n")
        f.write("LABELS EMBEDDED\n")
        f.write("DATA:\n")
        if fmt == "fullmatrix":
            f.write(" " + " ".join(str(n) for n in nodes) + "\n")
            A = nx.to_numpy_array(G, nodelist=nodes)
            for i, node in enumerate(nodes):
                f.write(f"{node} " + " ".join(_format_value(v) for v in A[i]) + "\n")
        else:
            for u, v, data in G.edges(data=True):
                f.write(f"{u} {v} {_format_value(data.get('weight', 1))}\n")


def import_from_ucinet_dl(path, directed=None):
    """
    Read a UCINET DL file (FULLMATRIX or EDGELIST1).

    directed=None: a full matrix is read as directed when it is asymmetric;
    an edge list is read as undirected. Pass True or False to override.
    Non-binary values are kept as weights.
    """
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    data_start = next((i + 1 for i, line in enumerate(lines)
                       if "DATA" in line.upper() and ":" in line), None)
    if data_start is None:
        raise ValueError("DATA: section not found")
    header = " ".join(lines[:data_start]).upper()
    fmt = "edgelist" if "EDGELIST" in header else "fullmatrix"
    embedded = "EMBEDDED" in header
    rows = [line.split() for line in lines[data_start:] if line.strip()]

    if fmt == "fullmatrix":
        if embedded:
            labels = [r[0] for r in rows[1:]]
            values = np.array([[float(v) for v in r[1:]] for r in rows[1:]])
        else:
            labels = None
            values = np.array([[float(v) for v in r] for r in rows])
        is_directed = (not np.allclose(values, values.T)) if directed is None else directed
        is_weighted = bool(np.any((values != 0) & (values != 1)))
        return load_from_matrix(values, labels=labels, directed=is_directed,
                                weighted=is_weighted)

    edges = []
    for r in rows:
        if len(r) >= 3:
            edges.append((r[0], r[1], float(r[2])))
        elif len(r) == 2:
            edges.append((r[0], r[1], 1.0))
    is_weighted = any(w != 1.0 for _, _, w in edges)
    return load_from_edges(edges if is_weighted else [(u, v) for u, v, _ in edges],
                           directed=bool(directed), weighted=is_weighted)


# =============================================================================
# Scale handling
# =============================================================================

def recommend_strategy(G):
    """Recommend an analysis and visualization strategy by node count."""
    n = G.number_of_nodes()
    result = {"size": n, "edges": G.number_of_edges(),
              "density": nx.density(G) if n > 1 else 0.0}
    if n <= STRATEGY_FULL_MAX:
        result.update(strategy="full", visualization=_t("viz_full"),
                      algorithms=_t("alg_full"), warnings=[])
    elif n <= STRATEGY_FILTERED_MAX:
        result.update(strategy="filtered", visualization=_t("viz_filtered"),
                      algorithms=_t("alg_filtered"),
                      warnings=[_t("warn_heatmap"), _t("warn_labels")])
    elif n <= STRATEGY_AGGREGATED_MAX:
        result.update(strategy="aggregated", visualization=_t("viz_aggregated"),
                      algorithms=_t("alg_aggregated"),
                      warnings=[_t("warn_matrix_useless"), _t("warn_rege_slow"),
                                _t("warn_cluster_memory")])
    else:
        result.update(strategy="summary_only", visualization=_t("viz_summary"),
                      algorithms=_t("alg_summary"),
                      warnings=[_t("warn_no_full_viz"), _t("warn_node_level"),
                                _t("warn_subnetwork")])
    return result


def sample_top_k_nodes(G, k=30, by="betweenness"):
    """Subgraph of the k nodes ranked highest by betweenness, degree, closeness or pagerank."""
    scorers = {
        "betweenness": nx.betweenness_centrality,
        "degree": lambda g: dict(g.degree()),
        "closeness": nx.closeness_centrality,
        "pagerank": nx.pagerank,
    }
    if by not in scorers:
        raise ValueError(f"Unknown metric: {by}")
    scores = scorers[by](G)
    top = [n for n, _ in sorted(scores.items(), key=lambda x: -x[1])[:k]]
    return G.subgraph(top).copy()


def extract_core_subgraph(G, min_degree=3):
    """Keep nodes whose degree is at least min_degree (one pass, not a k-core)."""
    return G.subgraph([n for n in G.nodes() if G.degree(n) >= min_degree]).copy()


def aggregate_to_blocks(G, blocks):
    """Reduced graph: one node per block, edge weight = number of ties between blocks."""
    blocks = _as_series(blocks)
    reduced = nx.DiGraph() if G.is_directed() else nx.Graph()
    names = {b: _t("block_name", b=b) for b in sorted(set(blocks.values))}
    reduced.add_nodes_from(names.values())
    for u, v in G.edges():
        b1, b2 = names[blocks[u]], names[blocks[v]]
        if b1 == b2:
            continue
        if reduced.has_edge(b1, b2):
            reduced[b1][b2]["weight"] += 1
        else:
            reduced.add_edge(b1, b2, weight=1)
    return reduced


def summary_statistics_only(G):
    """Whole-network statistics for networks too large to draw."""
    n, m = G.number_of_nodes(), G.number_of_edges()
    stats = {
        _t("nodes"): n, _t("edges"): m, _t("density"): nx.density(G),
        _t("mean_degree"): 2 * m / n if n else 0,
        _t("directed"): G.is_directed(),
    }
    if G.is_directed():
        stats[_t("strong_components")] = nx.number_strongly_connected_components(G)
        stats[_t("weak_components")] = nx.number_weakly_connected_components(G)
    elif n:
        largest = max(nx.connected_components(G), key=len)
        stats[_t("components")] = nx.number_connected_components(G)
        stats[_t("largest_component")] = len(largest)
        stats[_t("largest_component_share")] = len(largest) / n
    degrees = [d for _, d in G.degree()]
    if degrees:
        stats[_t("degree_mean")] = float(np.mean(degrees))
        stats[_t("degree_median")] = float(np.median(degrees))
        stats[_t("degree_std")] = float(np.std(degrees))
        stats[_t("degree_max")] = max(degrees)
        stats[_t("degree_min")] = min(degrees)
    return pd.Series(stats)


def louvain_communities(G, seed=COMMUNITY_SEED):
    """Louvain modularity communities. The same seed gives the same result."""
    communities = nx.community.louvain_communities(G, seed=seed)
    assignment = {node: i for i, c in enumerate(communities, 1) for node in c}
    return pd.Series(assignment, name="community")


# =============================================================================
# Graph basics, paths and distances
# =============================================================================

def describe_graph(G):
    """Basic facts about the graph."""
    n = G.number_of_nodes()
    info = {
        _t("nodes"): n, _t("edges"): G.number_of_edges(),
        _t("directed"): G.is_directed(), _t("density"): nx.density(G),
        _t("mean_degree"): sum(d for _, d in G.degree()) / n if n else 0,
    }
    if G.is_directed():
        info[_t("weak_components")] = nx.number_weakly_connected_components(G)
        info[_t("strong_components")] = nx.number_strongly_connected_components(G)
    elif n:
        info[_t("components")] = nx.number_connected_components(G)
        if nx.is_connected(G):
            info[_t("diameter")] = nx.diameter(G)
    return pd.Series(info)


def dyadic_pairs(n_or_graph):
    """Number of unordered pairs N(N-1)/2."""
    n = n_or_graph.number_of_nodes() if hasattr(n_or_graph, "number_of_nodes") else int(n_or_graph)
    return n * (n - 1) // 2


def find_walks(G, source, target, max_length=4):
    """All walks (nodes and lines may repeat) from source to target up to max_length lines."""
    walks = []

    def extend(current, path):
        if current == target and len(path) > 1:
            walks.append(list(path))
        if len(path) - 1 == max_length:
            return
        for nxt in G.neighbors(current):
            path.append(nxt)
            extend(nxt, path)
            path.pop()

    extend(source, [source])
    return walks


def find_paths(G, source, target, max_length=None):
    """All paths (no repeated node) from source to target, shortest first."""
    try:
        paths = list(nx.all_simple_paths(G, source, target, cutoff=max_length))
    except nx.NodeNotFound:
        return []
    return sorted(paths, key=len)


def find_cycles(G, max_length=4):
    """Simple cycles with 3 to max_length nodes (reciprocal pairs are not cycles)."""
    try:
        cycles = list(nx.simple_cycles(G, length_bound=max_length))
    except (TypeError, nx.NetworkXNotImplemented):
        cycles = [c for c in (nx.simple_cycles(G) if G.is_directed() else nx.cycle_basis(G))
                  if len(c) <= max_length]
    return sorted((c for c in cycles if len(c) >= 3), key=lambda c: (len(c), [str(x) for x in c]))


def classify_nodes(G):
    """
    Directed graphs: isolate (in=0, out=0), transmitter (in=0, out>0),
    receiver (in>0, out=0), carrier (in>0, out>0).
    Undirected graphs: isolate or connected.
    """
    if not G.is_directed():
        return pd.DataFrame({
            _t("degree"): dict(G.degree()),
            _t("class"): {n: _t("isolate") if G.degree(n) == 0 else _t("connected")
                          for n in G.nodes()},
        })

    def label(i, o):
        if i == 0 and o == 0:
            return _t("isolate")
        if i == 0:
            return _t("transmitter")
        if o == 0:
            return _t("receiver")
        return _t("carrier")

    rows = [{_t("node"): n, _t("indegree"): G.in_degree(n), _t("outdegree"): G.out_degree(n),
             _t("class"): label(G.in_degree(n), G.out_degree(n))} for n in G.nodes()]
    return pd.DataFrame(rows).set_index(_t("node"))


def compute_degree_stats(G):
    """
    Mean and population variance of degree.
    Undirected: mean = 2L/g. Directed: mean indegree = mean outdegree = L/g.
    """
    g = G.number_of_nodes()
    if g == 0:
        return pd.Series(dtype=float)
    L = G.number_of_edges()
    if G.is_directed():
        ins = np.array([d for _, d in G.in_degree()], dtype=float)
        outs = np.array([d for _, d in G.out_degree()], dtype=float)
        mean = L / g
        var_in = float(((ins - mean) ** 2).mean())
        var_out = float(((outs - mean) ** 2).mean())
        return pd.Series({
            _t("nodes"): g, _t("lines"): L,
            _t("in_mean"): mean, _t("in_var"): var_in, _t("in_std"): var_in ** 0.5,
            _t("out_mean"): mean, _t("out_var"): var_out, _t("out_std"): var_out ** 0.5,
        })
    degs = np.array([d for _, d in G.degree()], dtype=float)
    mean = 2 * L / g
    var = float(((degs - mean) ** 2).mean())
    return pd.Series({
        _t("nodes"): g, _t("lines"): L, _t("mean_degree"): mean,
        _t("variance"): var, _t("std"): var ** 0.5,
        _t("max"): int(degs.max()), _t("min"): int(degs.min()),
    })


def compute_distances(G):
    """
    Geodesic distance matrix (inf when unreachable), mean distance over
    reachable pairs, and diameter, radius and eccentricity when connected.
    """
    nodes = list(G.nodes())
    index = {n: i for i, n in enumerate(nodes)}
    dist = np.full((len(nodes), len(nodes)), np.inf)
    for u in nodes:
        for v, d in nx.single_source_shortest_path_length(G, u).items():
            dist[index[u], index[v]] = d
    finite = dist[np.isfinite(dist) & (dist > 0)]
    result = {
        "distance_matrix": pd.DataFrame(dist, index=nodes, columns=nodes),
        "avg_distance": float(finite.mean()) if finite.size else np.inf,
        "diameter": np.inf, "radius": np.inf, "eccentricity": None,
    }
    connected = (nx.is_strongly_connected(G) if G.is_directed() else nx.is_connected(G)) \
        if nodes else False
    if connected:
        result["diameter"] = nx.diameter(G)
        result["radius"] = nx.radius(G)
        result["eccentricity"] = pd.Series(nx.eccentricity(G))
    return result


def extract_ego_network(G, ego, radius=1):
    """Ego plus every node within radius steps (both directions for digraphs)."""
    if ego not in G:
        raise ValueError(f"Node {ego} is not in the graph")
    H = G.to_undirected(as_view=True) if G.is_directed() else G
    reach = nx.single_source_shortest_path_length(H, ego, cutoff=radius)
    return G.subgraph(reach.keys()).copy()


def transpose_matrix(G):
    """Reverse tie direction (transpose). Undirected graphs are returned as a copy."""
    return G.reverse(copy=True) if G.is_directed() else G.copy()


def reorder_matrix(G, order=None, reorder_by=None):
    """Adjacency matrix with rows and columns permuted by an explicit order or by group."""
    if order is not None:
        nodes = [n for n in order if n in G]
    elif reorder_by is not None:
        nodes = sorted(G.nodes(), key=lambda n: (reorder_by.get(n, 0), str(n)))
    else:
        nodes = list(G.nodes())
    return pd.DataFrame(nx.to_numpy_array(G, nodelist=nodes), index=nodes, columns=nodes)


# =============================================================================
# Density, structural holes and openness
# =============================================================================

def compute_density(G):
    """Density plus inclusiveness (share of nodes that are not isolates)."""
    n = G.number_of_nodes()
    isolates = list(nx.isolates(G))
    return pd.Series({
        _t("density"): nx.density(G), _t("nodes"): n, _t("edges"): G.number_of_edges(),
        _t("isolates"): len(isolates),
        _t("inclusiveness"): (n - len(isolates)) / n if n else 0.0,
    })


def _alter_count(G, node):
    if G.is_directed():
        alters = set(G.predecessors(node)) | set(G.successors(node))
    else:
        alters = set(G.neighbors(node))
    alters.discard(node)
    return len(alters)


def compute_structural_holes(G):
    """
    Burt's effective size, efficiency (= effective size / number of alters)
    and aggregate constraint. Sorted by constraint, lowest first.
    """
    nodes = list(G.nodes())
    df = pd.DataFrame(index=nodes)
    df["effective_size"] = pd.Series(nx.effective_size(G))
    df["constraint"] = pd.Series(nx.constraint(G))
    df["alters"] = pd.Series({n: _alter_count(G, n) for n in nodes})
    df["efficiency"] = (df["effective_size"] / df["alters"].replace(0, np.nan))
    return df.sort_values("constraint", ascending=True, na_position="last")


def compute_network_openness(G, groups):
    """
    Openness of each group = share of its members' tie ends that point to
    nodes outside the group (0 closed, 1 fully open). An internal tie is
    counted from both of its ends. Digraphs count outgoing ties only.
    """
    groups = _as_series(groups)
    openness = {}
    for group in sorted(set(groups.values)):
        members = set(groups[groups == group].index)
        internal = external = 0
        for node in members:
            for nb in G.neighbors(node):
                if nb in members:
                    internal += 1
                else:
                    external += 1
        total = internal + external
        openness[group] = external / total if total else 0.0
    return pd.Series(openness, name=_t("openness"))


# =============================================================================
# Centrality and centralization
# =============================================================================

def compute_centralities(G):
    """
    Relative degree, closeness and betweenness centrality, sorted by
    betweenness. Digraphs add in and out centrality.
    NetworkX conventions: digraph degree centrality uses in+out degree (0 to 2);
    digraph closeness uses incoming distance; disconnected graphs use the
    Wasserman-Faust correction (share of reachable nodes / mean distance).
    """
    df = pd.DataFrame({
        _t("c_degree"): nx.degree_centrality(G),
        _t("c_closeness"): nx.closeness_centrality(G),
        _t("c_betweenness"): nx.betweenness_centrality(G),
    })
    if G.is_directed():
        df[_t("c_in")] = pd.Series(nx.in_degree_centrality(G))
        df[_t("c_out")] = pd.Series(nx.out_degree_centrality(G))
    return df.sort_values(_t("c_betweenness"), ascending=False)


def compute_extended_centralities(G):
    """Eigenvector, PageRank and Katz centrality. NaN when a measure does not converge."""
    measures = {
        "eigenvector": lambda g: nx.eigenvector_centrality(g, max_iter=1000),
        "pagerank": nx.pagerank,
        "katz": nx.katz_centrality_numpy,
    }
    result = {}
    for name, func in measures.items():
        try:
            result[name] = func(G)
        except (nx.NetworkXException, np.linalg.LinAlgError, ZeroDivisionError):
            result[name] = {n: np.nan for n in G.nodes()}
    return pd.DataFrame(result)


def _centralization(values, denominator):
    values = list(values)
    if denominator <= 0 or not values:
        return 0.0
    top = max(values)
    return sum(top - v for v in values) / denominator


def compute_centralization(G):
    """
    Freeman centralization: sum of (max score - each score) divided by the
    largest possible sum, which a star graph attains (range 0 to 1).
    Undirected: degree (g-1)(g-2), betweenness (g-1)^2(g-2)/2 on raw scores,
    closeness (g-1)(g-2)/(2g-3) on relative scores, connected graphs only.
    Directed: in and out degree (g-1)^2, betweenness (g-1)^2(g-2);
    closeness centralization is not reported for digraphs.
    """
    g = G.number_of_nodes()
    if g < 3:
        keys = ("z_in", "z_out") if G.is_directed() else ("z_degree",)
        return pd.Series({**{_t(k): 0.0 for k in keys},
                          _t("z_closeness"): np.nan, _t("z_betweenness"): 0.0})
    raw_betweenness = nx.betweenness_centrality(G, normalized=False).values()

    if G.is_directed():
        return pd.Series({
            _t("z_in"): _centralization((d for _, d in G.in_degree()), (g - 1) ** 2),
            _t("z_out"): _centralization((d for _, d in G.out_degree()), (g - 1) ** 2),
            _t("z_closeness"): np.nan,
            _t("z_betweenness"): _centralization(raw_betweenness, (g - 1) ** 2 * (g - 2)),
        })

    closeness = np.nan
    if nx.is_connected(G):
        closeness = _centralization(nx.closeness_centrality(G).values(),
                                    (g - 1) * (g - 2) / (2 * g - 3))
    return pd.Series({
        _t("z_degree"): _centralization((d for _, d in G.degree()), (g - 1) * (g - 2)),
        _t("z_closeness"): closeness,
        _t("z_betweenness"): _centralization(raw_betweenness, (g - 1) ** 2 * (g - 2) / 2),
    })


# =============================================================================
# Components and cohesive subgroups
# =============================================================================

def find_components(G):
    """Components (weak and strong for digraphs) and isolates."""
    result = {}
    if G.is_directed():
        weak = [sorted(c, key=str) for c in nx.weakly_connected_components(G)]
        strong = [sorted(c, key=str) for c in nx.strongly_connected_components(G)]
        result.update({_t("weak_list"): weak, _t("strong_list"): strong,
                       _t("weak_components"): len(weak), _t("strong_components"): len(strong)})
    else:
        comps = [sorted(c, key=str) for c in nx.connected_components(G)]
        result.update({_t("component_list"): comps, _t("components"): len(comps)})
    result[_t("isolate_list")] = list(nx.isolates(G))
    return result


def find_cut_points(G):
    """Cut-points (removal splits a component) and bridges (lines whose removal does)."""
    H = _undirected_simple(G)
    return {_t("cut_points"): list(nx.articulation_points(H)),
            _t("bridges"): list(nx.bridges(H))}


def find_k_cores(G, k_range=None):
    """Members of each k-core (every member has at least k ties inside the core)."""
    H = _undirected_simple(G)
    core = nx.core_number(H)
    max_k = max(core.values()) if core else 0
    result = {f"{k}-core": [n for n, c in core.items() if c >= k]
              for k in (k_range or range(1, max_k + 1))}
    result["core_numbers"] = core
    result[_t("max_k")] = max_k
    return result


def k_core_residuals(G):
    """For each k, how many nodes fall outside the k-core (residuals) and their share."""
    H = _undirected_simple(G)
    core = nx.core_number(H)
    max_k = max(core.values()) if core else 0
    total = G.number_of_nodes()
    rows = []
    for k in range(1, max_k + 2):
        inside = [n for n, c in core.items() if c >= k]
        outside = sorted((n for n, c in core.items() if c < k), key=str)
        rows.append({_t("k"): k, _t("core_members"): len(inside),
                     _t("residuals"): len(outside),
                     _t("residual_share"): len(outside) / total if total else 0.0,
                     _t("residual_list"): str(outside[:10])})
    return pd.DataFrame(rows)


def compute_m_core(G, m=2):
    """
    Keep only strong ties. Weighted graph: ties with weight >= m.
    Unweighted graph (substitute rule): ties whose two ends share >= m neighbors.
    """
    H0 = _undirected_simple(G)
    H = nx.Graph()
    H.add_nodes_from(H0.nodes())
    if _is_weighted(H0):
        H.add_weighted_edges_from((u, v, d.get("weight", 1)) for u, v, d in H0.edges(data=True)
                                  if d.get("weight", 1) >= m)
    else:
        H.add_edges_from((u, v) for u, v in H0.edges()
                         if len(set(H0[u]) & set(H0[v])) >= m)
    return H


def find_cliques(G, min_size=3):
    """Maximal cliques with at least min_size members, largest first."""
    H = _undirected_simple(G)
    cliques = [sorted(c, key=str) for c in nx.find_cliques(H) if len(c) >= min_size]
    return sorted(cliques, key=lambda c: (-len(c), [str(x) for x in c]))


def clique_membership(G, min_size=3):
    """Number of cliques each node belongs to and their ids (1-based, as in find_cliques)."""
    cliques = find_cliques(G, min_size=min_size)
    rows = []
    for node in G.nodes():
        ids = [i + 1 for i, c in enumerate(cliques) if node in c]
        rows.append({_t("node"): node, _t("clique_count"): len(ids),
                     _t("clique_ids"): str(ids) if ids else "-"})
    return pd.DataFrame(rows).set_index(_t("node")).sort_values(_t("clique_count"),
                                                                 ascending=False)


def find_n_cliques(G, n=2, min_size=3):
    """
    n-cliques: maximal sets whose members are all within distance n in the
    whole graph (paths may pass through outsiders).
    """
    H = _undirected_simple(G)
    power = nx.Graph()
    power.add_nodes_from(H.nodes())
    for u in H.nodes():
        for v, d in nx.single_source_shortest_path_length(H, u, cutoff=n).items():
            if u != v:
                power.add_edge(u, v)
    cliques = [sorted(c, key=str) for c in nx.find_cliques(power) if len(c) >= min_size]
    return sorted(cliques, key=lambda c: (-len(c), [str(x) for x in c]))


def _diameter_within(H, members):
    sub = H.subgraph(members)
    if len(members) == 1:
        return 0
    return nx.diameter(sub) if nx.is_connected(sub) else math.inf


def find_n_clans(G, n=2, min_size=3):
    """n-clans: n-cliques whose own subgraph has diameter <= n."""
    H = _undirected_simple(G)
    return [c for c in find_n_cliques(G, n=n, min_size=min_size)
            if _diameter_within(H, c) <= n]


def find_n_clubs(G, n=2, min_size=3):
    """
    n-clubs: subgraphs with diameter <= n (approximate search).

    For every node, start from all nodes within distance n and repeatedly drop
    the member (other than the starting node) that reaches the fewest members
    within distance n inside the current set, until the diameter is <= n.
    Sets contained in another found set are discarded. Finding every maximal
    n-club is computationally hard, so the result can miss some clubs.
    """
    H = _undirected_simple(G)
    found = set()
    for center in H.nodes():
        members = set(nx.single_source_shortest_path_length(H, center, cutoff=n))
        while len(members) >= min_size and _diameter_within(H, members) > n:
            sub = H.subgraph(members)
            reach = {v: len(nx.single_source_shortest_path_length(sub, v, cutoff=n))
                     for v in members if v != center}
            drop = min(reach, key=lambda v: (reach[v], str(v)))
            members.discard(drop)
        if len(members) >= min_size:
            found.add(frozenset(members))
    maximal = [s for s in found if not any(s < other for other in found)]
    return sorted((sorted(s, key=str) for s in maximal),
                  key=lambda c: (-len(c), [str(x) for x in c]))


def find_cycle_components(G):
    """Remove bridges; the remaining components with 3 or more nodes are cycle components."""
    H = _undirected_simple(G)
    bridges = list(nx.bridges(H))
    H.remove_edges_from(bridges)
    comps = [sorted(c, key=str) for c in nx.connected_components(H) if len(c) >= 3]
    return {_t("cycle_components"): sorted(comps, key=lambda c: -len(c)),
            _t("removed_bridges"): bridges}


# =============================================================================
# Structural equivalence and blockmodeling
# =============================================================================

def _profile_pair(A, i, j):
    """Row and column values of i and j, excluding the cells that refer to i or j."""
    keep = np.ones(A.shape[0], dtype=bool)
    keep[[i, j]] = False
    vi = np.concatenate([A[i, keep], A[keep, i]])
    vj = np.concatenate([A[j, keep], A[keep, j]])
    return vi, vj


def euclidean_equivalence(G):
    """
    Euclidean distance between the tie profiles of i and j:
    sqrt(sum over k != i, j of (x_ik - x_jk)^2 + (x_ki - x_kj)^2).
    0 means identical ties to every third party.
    """
    nodes = list(G.nodes())
    A = nx.to_numpy_array(G, nodelist=nodes)
    n = len(nodes)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            vi, vj = _profile_pair(A, i, j)
            D[i, j] = D[j, i] = float(np.sqrt(((vi - vj) ** 2).sum()))
    return pd.DataFrame(D, index=nodes, columns=nodes)


def _pearson(vi, vj):
    if vi.size == 0 or vi.std() == 0 or vj.std() == 0:
        return 0.0
    return float(np.corrcoef(vi, vj)[0, 1])


def _correlation_matrix(A, members):
    k = len(members)
    R = np.eye(k)
    for a in range(k):
        for b in range(a + 1, k):
            R[a, b] = R[b, a] = _pearson(*_profile_pair(A, members[a], members[b]))
    return R


def correlation_equivalence(G):
    """
    Pearson correlation between the tie profiles of i and j (cells that refer
    to i or j excluded). +1 means perfectly similar patterns. A node with no
    variation in its profile (for example an isolate) gets 0 with everyone.
    """
    nodes = list(G.nodes())
    A = nx.to_numpy_array(G, nodelist=nodes)
    R = _correlation_matrix(A, list(range(len(nodes))))
    return pd.DataFrame(R, index=nodes, columns=nodes)


def _concor_split(A, members, max_iter, tol):
    """Split members in two by iterating correlations until entries reach +1 or -1."""
    M = _correlation_matrix(A, members)
    for _ in range(max_iter):
        with np.errstate(invalid="ignore", divide="ignore"):
            M_next = np.nan_to_num(np.corrcoef(M))
        converged = np.allclose(np.abs(M_next), 1.0, atol=tol)
        M = M_next
        if converged:
            break
    first = [members[i] for i in range(len(members)) if M[i, 0] > 0]
    second = [members[i] for i in range(len(members)) if M[i, 0] <= 0]
    return first, second


def concor(G, n_splits=1, max_iter=50, tol=1e-6):
    """
    CONCOR: iterate correlations of the correlation matrix until every entry is
    +1 or -1, which splits a set in two. Each split step halves every block, so
    n_splits steps give up to 2**n_splits blocks. Nodes without variation in
    their tie profile (isolates) are kept out of the splitting and labeled 0.
    """
    nodes = list(G.nodes())
    A = nx.to_numpy_array(G, nodelist=nodes)
    profiles = [np.concatenate([A[i], A[:, i]]) for i in range(len(nodes))]
    active = [i for i, p in enumerate(profiles) if p.std() > 0]
    blocks = [active] if active else []
    for _ in range(n_splits):
        next_blocks = []
        for block in blocks:
            if len(block) < 2:
                next_blocks.append(block)
                continue
            first, second = _concor_split(A, block, max_iter, tol)
            next_blocks.extend(b for b in (first, second) if b)
        blocks = next_blocks
    labels = {nodes[i]: 0 for i in range(len(nodes))}
    for number, block in enumerate(blocks, 1):
        for i in block:
            labels[nodes[i]] = number
    return pd.Series(labels)


def regular_equivalence(G, max_iter=20, tol=1e-4):
    """
    Iterative regular-equivalence similarity in the spirit of REGE (0 to 1).
    Two nodes are similar when each neighbor of one can be matched with a
    similar neighbor of the other. Digraphs match out-neighbors and
    in-neighbors separately. Starting similarity is 1 for every pair.
    On undirected binary data most non-isolated nodes end up similar.
    """
    nodes = list(G.nodes())
    n = len(nodes)
    A = nx.to_numpy_array(G, nodelist=nodes) > 0
    directions = [A, A.T] if G.is_directed() else [A]
    neighbor_sets = [[np.flatnonzero(M[i]) for i in range(n)] for M in directions]

    S = np.ones((n, n))
    for _ in range(max_iter):
        S_new = np.eye(n)
        for i in range(n):
            for j in range(i + 1, n):
                matched, total = 0.0, 0
                for nbrs in neighbor_sets:
                    Ni, Nj = nbrs[i], nbrs[j]
                    total += len(Ni) + len(Nj)
                    if len(Ni) and len(Nj):
                        block = S[np.ix_(Ni, Nj)]
                        matched += block.max(axis=1).sum() + block.max(axis=0).sum()
                S_new[i, j] = S_new[j, i] = matched / total if total else 1.0
        change = np.max(np.abs(S_new - S))
        S = S_new
        if change < tol:
            break
    return pd.DataFrame(S, index=nodes, columns=nodes)


def _cluster(condensed, n_blocks, method):
    labels = fcluster(linkage(condensed, method=method), n_blocks, criterion="maxclust")
    return labels


def blockmodel(G, n_blocks=3, method="hierarchical"):
    """
    Assign nodes to blocks.
    'hierarchical': Ward clustering of Euclidean structural-equivalence distance.
    'concor': CONCOR splits; n_blocks must be a power of two (2, 4, 8, ...).
    'structure': average-linkage clustering of Euclidean distance between
                 geodesic-distance profiles (approximation of Burt's path-distance idea).
    'rege': average-linkage clustering of 1 - regular-equivalence similarity.
    """
    nodes = list(G.nodes())
    if len(nodes) < 2:
        return pd.Series([1] * len(nodes), index=nodes)

    if method == "concor":
        splits = math.log2(n_blocks) if n_blocks > 0 else -1
        if splits < 1 or not float(splits).is_integer():
            raise ValueError("CONCOR produces 2, 4, 8, ... blocks; set n_blocks to a power of two.")
        return concor(G, n_splits=int(splits))

    if method == "hierarchical":
        D = euclidean_equivalence(G).values
        return pd.Series(_cluster(squareform(D, checks=False), n_blocks, "ward"), index=nodes)

    if method == "structure":
        index = {v: i for i, v in enumerate(nodes)}
        P = np.full((len(nodes), len(nodes)), float(len(nodes) + 1))
        for u in nodes:
            for v, d in nx.single_source_shortest_path_length(G, u).items():
                P[index[u], index[v]] = d
        return pd.Series(_cluster(pdist(P), n_blocks, "average"), index=nodes)

    if method == "rege":
        S = regular_equivalence(G).values
        D = 1 - (S + S.T) / 2
        np.fill_diagonal(D, 0)
        return pd.Series(_cluster(squareform(D, checks=False), n_blocks, "average"), index=nodes)

    raise ValueError(f"Unknown method: {method}. Use 'hierarchical', 'concor', 'structure' or 'rege'.")


def _block_cells(G, blocks):
    """Yield (row block, column block, submatrix, possible ties, actual ties)."""
    blocks = _as_series(blocks)
    nodes = list(G.nodes())
    A = nx.to_numpy_array(G, nodelist=nodes)
    order = sorted(set(blocks.values))
    members = {b: [i for i, n in enumerate(nodes) if blocks[n] == b] for b in order}
    for b1 in order:
        for b2 in order:
            sub = A[np.ix_(members[b1], members[b2])]
            if b1 == b2:
                size = len(members[b1])
                possible = size * (size - 1)
                actual = sub.sum() - np.trace(sub)
            else:
                possible = sub.size
                actual = sub.sum()
            yield b1, b2, sub, possible, actual


def image_matrix(G, blocks, alpha=None, criterion="alpha"):
    """
    Reduce a blocked matrix to 0/1 ties between blocks.
    'alpha': 1 when block density >= alpha (default alpha = overall density).
    'zero' : 0 only when the block has no ties at all (lean fit).
    'one'  : 1 only when every possible tie is present.
    'perfect': 1 for complete blocks, 0 for empty blocks, NaN for mixed blocks,
               which mark where a perfect structural-equivalence fit fails.
    """
    if criterion not in ("alpha", "zero", "one", "perfect"):
        raise ValueError(f"Unknown criterion: {criterion}")
    alpha = nx.density(G) if alpha is None else alpha
    order = sorted(set(_as_series(blocks).values))
    img = pd.DataFrame(0.0, index=order, columns=order)
    for b1, b2, _, possible, actual in _block_cells(G, blocks):
        density = actual / possible if possible else 0.0
        if criterion == "alpha":
            value = 1.0 if possible and density >= alpha else 0.0
        elif criterion == "zero":
            value = 1.0 if actual > 0 else 0.0
        elif criterion == "one":
            value = 1.0 if possible and density >= 1.0 else 0.0
        else:
            value = 1.0 if possible and density >= 1.0 else (0.0 if actual == 0 else np.nan)
        img.loc[b1, b2] = value
    return img


def block_density_matrix(G, blocks):
    """Density of ties inside and between blocks (diagonal cells exclude self-ties)."""
    order = sorted(set(_as_series(blocks).values))
    dens = pd.DataFrame(0.0, index=order, columns=order)
    for b1, b2, _, possible, actual in _block_cells(G, blocks):
        dens.loc[b1, b2] = actual / possible if possible else 0.0
    return dens


# =============================================================================
# Markdown output
# =============================================================================

def matrix_to_markdown(G, reorder_by=None, label=None, max_size=MATRIX_INLINE_MAX_NODES,
                       top_k_by="degree"):
    """
    Adjacency matrix as a copyable Markdown table. Above max_size nodes, the
    top nodes by degree or betweenness are excerpted and the caption says so.
    """
    label = label or _t("matrix_label")
    total = G.number_of_nodes()
    truncated = total > max_size
    if truncated:
        scores = nx.betweenness_centrality(G) if top_k_by == "betweenness" else dict(G.degree())
        keep = [n for n, _ in sorted(scores.items(), key=lambda x: -x[1])[:max_size]]
        G = G.subgraph(keep).copy()

    if reorder_by is not None:
        nodes = sorted(G.nodes(), key=lambda n: (reorder_by.get(n, 0), str(n)))
    else:
        nodes = list(G.nodes())
    A = nx.to_numpy_array(G, nodelist=nodes)
    weighted = _is_weighted(G)

    lines = ["| | " + " | ".join(str(n) for n in nodes) + " |",
             "|---|" + "---|" * len(nodes)]
    for i, row_label in enumerate(nodes):
        cells = [(f"{v:.1f}" if v else "0") if weighted else str(int(v)) for v in A[i]]
        lines.append(f"| **{row_label}** | " + " | ".join(cells) + " |")

    if truncated:
        caption = f"> **{label}** " + _t("matrix_excerpt", total=total, by=top_k_by, k=max_size)
    elif reorder_by is not None:
        groups = {}
        for n in nodes:
            groups.setdefault(reorder_by.get(n), []).append(str(n))
        detail = " ".join(f"({_t('block_prefix', b=b)}) {', '.join(ms)}" for b, ms in groups.items())
        caption = f"> **{label}** {_t('matrix_reordered')} {detail}"
    else:
        caption = f"> **{label}**"
    return "\n" + caption + "\n\n" + "\n".join(lines) + "\n"


def blocks_summary_markdown(G, blocks, label=None):
    """Block-by-block density table for networks too large to show node by node."""
    blocks = _as_series(blocks)
    label = label or _t("block_summary_label")
    dens = block_density_matrix(G, blocks)
    sizes = blocks.value_counts().to_dict()
    names = [_t("block_header", b=b, n=sizes[b]) for b in dens.index]
    lines = ["| | " + " | ".join(names) + " |", "|---|" + "---|" * len(names)]
    for b, name in zip(dens.index, names):
        lines.append(f"| **{name}** | " + " | ".join(f"{v:.3f}" for v in dens.loc[b]) + " |")
    caption = f"> **{label}** " + _t("block_summary_caption", n=G.number_of_nodes(), k=len(names))
    return "\n" + caption + "\n\n" + "\n".join(lines) + "\n"


def dataframe_to_markdown(df, label=None, float_format="{:.3f}"):
    """DataFrame (or Series) as a Markdown table with fixed decimal places."""
    if isinstance(df, pd.Series):
        df = df.to_frame()
    shown = df.copy()
    for col in shown.columns:
        if pd.api.types.is_float_dtype(shown[col]):
            shown[col] = shown[col].map(lambda x: float_format.format(x) if pd.notnull(x) else "")
    header = [""] + [str(c) for c in shown.columns]
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for idx, row in shown.iterrows():
        lines.append("| " + " | ".join([str(idx)] + [str(v) for v in row.values]) + " |")
    caption = f"\n> **{label}**\n\n" if label else ""
    return caption + "\n".join(lines) + "\n"


def build_response_block(G, title, result_dict=None, centrality_df=None,
                         analysis_name=None):
    """
    Assemble the Markdown body of an analysis answer: input matrix, result
    table and the list of image files to deliver separately.
    """
    parts = [f"## {_t('section_matrix')}\n"]
    parts.append(result_dict["markdown"] if result_dict and "markdown" in result_dict
                 else matrix_to_markdown(G, label=title))
    if centrality_df is not None:
        name = analysis_name or title
        parts.append(f"\n## {_t('section_result')}\n")
        parts.append(dataframe_to_markdown(centrality_df, label=f"{name} {_t('result_suffix')}"))
    if result_dict:
        parts.append(f"\n## {_t('section_visual')}\n")
        parts.append(f"- {_t('visual_note')}")
        for key, name in (("matrix_path", "matrix_file"), ("network_path", "network_file")):
            if key in result_dict:
                parts.append(f"- {_t(name)} `{os.path.basename(result_dict[key])}`")
    return "\n".join(parts) + "\n"


# =============================================================================
# Visualization
# =============================================================================

def _pastel_cmap():
    return LinearSegmentedColormap.from_list("pastel_blue", HEATMAP_COLORS)


def _get_layout(G, layout="spring", seed=LAYOUT_SEED):
    layouts = {
        "spring": lambda: nx.spring_layout(G, seed=seed, k=1.5),
        "circular": lambda: nx.circular_layout(G),
        "kamada_kawai": lambda: nx.kamada_kawai_layout(G),
        "shell": lambda: nx.shell_layout(G),
    }
    return layouts.get(layout, layouts["spring"])()


def _save(fig, path):
    if path:
        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        fig.savefig(path, dpi=SAVE_DPI, bbox_inches="tight", facecolor="white")


def _warn_small(G, name):
    if G.number_of_nodes() <= MATRIX_INLINE_MAX_NODES:
        warnings.warn(f"{name} draws the graph alone. For networks of "
                      f"{MATRIX_INLINE_MAX_NODES} nodes or fewer use draw_matrix_and_network().",
                      UserWarning, stacklevel=3)


def _node_style(G, centrality_dict=None, group_dict=None, size_range=(300, 1300)):
    """Node colors and sizes from centrality values or group membership."""
    nodes = list(G.nodes())
    colors, sizes, legend = PALETTE["primary"], 700, None
    if group_dict is not None:
        groups = sorted(set(group_dict.values()), key=str)
        cmap = {g: BLOCK_COLORS[i % len(BLOCK_COLORS)] for i, g in enumerate(groups)}
        colors = [cmap[group_dict[n]] for n in nodes]
        legend = [Patch(facecolor=cmap[g], label=_t("group", g=g)) for g in groups]
    if centrality_dict is not None:
        vals = [centrality_dict[n] for n in nodes]
        low, span = min(vals), (max(vals) - min(vals)) or 1
        scaled = [(v - low) / span for v in vals]
        sizes = [size_range[0] + (size_range[1] - size_range[0]) * s for s in scaled]
        if group_dict is None:
            cm = _pastel_cmap()
            colors = [cm(0.25 + 0.45 * s) for s in scaled]
    return colors, sizes, legend


def _draw_graph(ax, G, pos, colors, sizes, legend=None, font_size=11):
    arrow_args = {"arrows": True, "arrowsize": 15} if G.is_directed() else {"arrows": False}
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color=PALETTE["neutral"], alpha=0.75,
                           width=1.2, **arrow_args)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=colors, node_size=sizes,
                           edgecolors=PALETTE["primary_edge"], linewidths=1.5)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=font_size, font_weight="bold",
                            font_color="black")
    if legend:
        ax.legend(handles=legend, loc="upper right", frameon=False, fontsize=10)
    ax.set_axis_off()


def draw_basic_network(G, title=None, figsize=(10, 8), layout="spring", save_path=None):
    """Plain graph. For 30 nodes or fewer prefer draw_matrix_and_network()."""
    _ensure_font()
    _warn_small(G, "draw_basic_network")
    fig, ax = plt.subplots(figsize=figsize)
    _draw_graph(ax, G, _get_layout(G, layout), PALETTE["primary"], 800)
    ax.set_title(title or _t("title_network"), fontsize=14, fontweight="bold", pad=15)
    fig.tight_layout()
    _save(fig, save_path)
    return fig, ax


def draw_centrality_network(G, centrality_dict, title=None, figsize=(10, 8),
                            layout="spring", save_path=None):
    """Graph with node size and color scaled by centrality."""
    _ensure_font()
    _warn_small(G, "draw_centrality_network")
    fig, ax = plt.subplots(figsize=figsize)
    colors, sizes, _ = _node_style(G, centrality_dict=centrality_dict, size_range=(300, 1500))
    _draw_graph(ax, G, _get_layout(G, layout), colors, sizes, font_size=10)
    ax.set_title(title or _t("title_centrality"), fontsize=14, fontweight="bold", pad=15)
    fig.tight_layout()
    _save(fig, save_path)
    return fig, ax


def draw_grouped_network(G, group_dict, title=None, figsize=(10, 8), layout="spring",
                         save_path=None):
    """Graph colored by group (block, clique, community)."""
    _ensure_font()
    _warn_small(G, "draw_grouped_network")
    fig, ax = plt.subplots(figsize=figsize)
    colors, sizes, legend = _node_style(G, group_dict=group_dict)
    _draw_graph(ax, G, _get_layout(G, layout), colors, sizes, legend, font_size=10)
    ax.set_title(title or _t("title_groups"), fontsize=14, fontweight="bold", pad=15)
    fig.tight_layout()
    _save(fig, save_path)
    return fig, ax


def draw_centrality_comparison(centrality_df, title=None, figsize=(10, 6), top_n=10,
                               save_path=None):
    """Grouped bars of degree, closeness and betweenness for the top_n nodes by betweenness."""
    _ensure_font()
    cols = [_t("c_degree"), _t("c_closeness"), _t("c_betweenness")]
    names = [_t("bar_degree"), _t("bar_closeness"), _t("bar_betweenness")]
    df = centrality_df.sort_values(cols[2], ascending=False).head(top_n)
    fig, ax = plt.subplots(figsize=figsize)
    width = 0.25
    x = np.arange(len(df))
    for offset, col, name, color in zip((-width, 0, width), cols, names, CENTRALITY_BAR_COLORS):
        bars = ax.bar(x + offset, df[col], width, label=name, color=color)
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h + 0.01, f"{h:.2f}",
                    ha="center", fontsize=8, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([str(i) for i in df.index], fontweight="bold")
    ax.set_ylabel(_t("axis_centrality"), fontweight="bold")
    ax.set_title(title or _t("title_comparison"), fontsize=14, fontweight="bold", pad=15)
    ax.legend(frameon=False, loc="upper right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    _save(fig, save_path)
    return fig, ax


def draw_k_core_nesting(G, title=None, figsize=(10, 8), save_path=None):
    """Graph whose node color and size grow with core number."""
    _ensure_font()
    core = nx.core_number(_undirected_simple(G))
    top = max(core.values()) if core else 1
    cm = _pastel_cmap()
    colors = [cm(0.25 + 0.45 * core[n] / (top or 1)) for n in G.nodes()]
    sizes = [300 + 200 * core[n] for n in G.nodes()]
    fig, ax = plt.subplots(figsize=figsize)
    _draw_graph(ax, G, _get_layout(G), colors, sizes, font_size=10)
    ax.set_title(title or _t("title_kcore"), fontsize=14, fontweight="bold", pad=15)
    fig.tight_layout()
    _save(fig, save_path)
    return fig, ax


def draw_uzzi_paradox(current_embeddedness=None, title=None, figsize=(10, 6), save_path=None):
    """
    Schematic inverted U between embeddedness (0 to 1) and performance.
    The curve y = 1 - 4(x - 0.5)^2 and the threshold at 0.5 are illustrative,
    not estimated from data.
    """
    _ensure_font()
    fig, ax = plt.subplots(figsize=figsize)
    x = np.linspace(0, 1, 200)
    y = 1 - 4 * (x - 0.5) ** 2
    ax.plot(x, y, color=PALETTE["primary_deep"], linewidth=3, zorder=2)
    ax.fill_between(x, 0, y, color=PALETTE["primary_light"], alpha=0.3, zorder=1)
    ax.axvline(0.5, color=PALETTE["accent"], linestyle="--", linewidth=2, alpha=0.7, zorder=3)
    ax.annotate(_t("uzzi_threshold"), xy=(0.5, 1.0), xytext=(0.5, 1.1), ha="center",
                fontsize=11, fontweight="bold", color=PALETTE["accent"],
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none"))
    ax.text(0.25, 0.45, _t("uzzi_left"), ha="center", va="center", fontsize=10, fontweight="bold")
    ax.text(0.75, 0.45, _t("uzzi_right"), ha="center", va="center", fontsize=10, fontweight="bold")
    if current_embeddedness is not None:
        cy = 1 - 4 * (current_embeddedness - 0.5) ** 2
        ax.scatter([current_embeddedness], [cy], s=200, color=PALETTE["accent"], zorder=5,
                   edgecolors=PALETTE["primary_edge"], linewidths=1.5)
        ax.annotate(_t("uzzi_current", v=current_embeddedness), xy=(current_embeddedness, cy),
                    xytext=(current_embeddedness, cy - 0.25), ha="center", fontsize=10,
                    fontweight="bold", arrowprops=dict(arrowstyle="->", color=PALETTE["accent"]))
    ax.set_xlabel(_t("uzzi_x"), fontsize=12, fontweight="bold")
    ax.set_ylabel(_t("uzzi_y"), fontsize=12, fontweight="bold")
    ax.set_title(title or _t("title_uzzi"), fontsize=14, fontweight="bold", pad=15)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    _save(fig, save_path)
    return fig, ax


def draw_bipartite_network(bipartite_result, title=None, figsize=(12, 8), save_path=None,
                           people_label="people", activity_label="activity"):
    """Two-mode graph: people as circles on the left, activities as squares on the right."""
    _ensure_font()
    B = bipartite_result["bipartite"]
    people = sorted((n for n, d in B.nodes(data=True) if d.get("kind") == people_label), key=str)
    acts = sorted((n for n, d in B.nodes(data=True) if d.get("kind") == activity_label), key=str)
    pos = {p: (0, i - len(people) / 2) for i, p in enumerate(people)}
    pos.update({a: (2, i - len(acts) / 2) for i, a in enumerate(acts)})
    fig, ax = plt.subplots(figsize=figsize)
    nx.draw_networkx_edges(B, pos, ax=ax, edge_color=PALETTE["neutral"], alpha=0.75, width=1.2)
    nx.draw_networkx_nodes(B, pos, nodelist=people, ax=ax, node_color=PALETTE["primary"],
                           node_size=700, edgecolors=PALETTE["primary_edge"], linewidths=1.5)
    nx.draw_networkx_nodes(B, pos, nodelist=acts, ax=ax, node_color=PALETTE["accent"],
                           node_size=700, node_shape="s", edgecolors=PALETTE["primary_edge"],
                           linewidths=1.5)
    nx.draw_networkx_labels(B, pos, ax=ax, font_size=10, font_weight="bold", font_color="black")
    ax.legend(handles=[Patch(facecolor=PALETTE["primary"], label=_t("people")),
                       Patch(facecolor=PALETTE["accent"], label=_t("activity"))],
              loc="upper right", frameon=False, fontsize=10)
    ax.set_title(title or _t("title_bipartite"), fontsize=14, fontweight="bold", pad=15)
    ax.set_axis_off()
    fig.tight_layout()
    _save(fig, save_path)
    return fig, ax


def draw_matrix_heatmap(G, ax=None, title=None, reorder_by=None, show_values=True,
                        figsize=(8, 7), save_path=None):
    """Adjacency matrix heatmap. reorder_by groups rows and draws block borders."""
    _ensure_font()
    standalone = ax is None
    fig, ax = plt.subplots(figsize=figsize) if standalone else (ax.figure, ax)
    if reorder_by is not None:
        nodes = sorted(G.nodes(), key=lambda n: (reorder_by.get(n, 0), str(n)))
    else:
        nodes = list(G.nodes())
    A = nx.to_numpy_array(G, nodelist=nodes)
    n = len(nodes)
    ax.imshow(A, cmap=_pastel_cmap(), aspect="equal", vmin=0, vmax=max(A.max(), 1))
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(nodes, fontsize=9, fontweight="bold", rotation=45, ha="right")
    ax.set_yticklabels(nodes, fontsize=9, fontweight="bold")
    ax.set_xticks(np.arange(-0.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which="minor", color=PALETTE["muted"], linewidth=0.8, alpha=0.6)
    ax.tick_params(which="minor", length=0)

    if show_values and n <= HEATMAP_VALUE_MAX_NODES:
        weighted = _is_weighted(G)
        for i in range(n):
            for j in range(n):
                if A[i, j] > 0:
                    text = f"{A[i, j]:.1f}" if weighted else f"{int(A[i, j])}"
                    ax.text(j, i, text, ha="center", va="center", color="black",
                            fontsize=8, fontweight="bold")

    if reorder_by is not None:
        counts = {}
        for node in nodes:
            b = reorder_by.get(node, 0)
            counts[b] = counts.get(b, 0) + 1
        boundary = 0
        for b in sorted(counts, key=str)[:-1]:
            boundary += counts[b]
            ax.axhline(boundary - 0.5, color=PALETTE["accent"], linewidth=2.5, zorder=10)
            ax.axvline(boundary - 0.5, color=PALETTE["accent"], linewidth=2.5, zorder=10)

    ax.set_title(title or _t("matrix_label"), fontsize=13, fontweight="bold", pad=12)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("#5B7890")
        spine.set_linewidth(1.2)
    if standalone:
        fig.tight_layout()
        _save(fig, save_path)
    return fig, ax


def draw_matrix_and_network(G, title=None, node_colors=None, node_sizes=None,
                            group_dict=None, centrality_dict=None, layout="spring",
                            figsize=(15, 7), save_path=None, print_markdown=True,
                            split_files=True):
    """
    Default view for networks of 30 nodes or fewer: adjacency matrix heatmap
    plus network graph, and the matrix as Markdown.

    split_files=True saves <name>_matrix.png and <name>_network.png (easier to
    read on phones); False saves one side-by-side image at save_path.
    Returns a dict with 'markdown' (paste into the answer), image paths when
    save_path is given ('matrix_path', 'network_path' or 'path'),
    'markdown_path', and the matplotlib figures.
    """
    _ensure_font()
    title = title or _t("title_analysis")
    colors, sizes, legend = _node_style(G, centrality_dict, group_dict, size_range=(300, 1300))
    if node_colors is not None:
        colors, legend = node_colors, None
    if node_sizes is not None:
        sizes = node_sizes
    markdown = matrix_to_markdown(G, reorder_by=group_dict, label=title)
    result = {"markdown": markdown}
    pos = _get_layout(G, layout)
    base = os.path.splitext(save_path)[0] if save_path else None

    if split_files:
        side = max(6, min(10, G.number_of_nodes() * 0.4))
        fig_m, ax_m = plt.subplots(figsize=(side, side))
        draw_matrix_heatmap(G, ax=ax_m, title=f"{title} {_t('suffix_matrix')}",
                            reorder_by=group_dict)
        fig_m.tight_layout()
        width = max(8, min(12, G.number_of_nodes() * 0.5))
        fig_n, ax_n = plt.subplots(figsize=(width, width * 0.85))
        _draw_graph(ax_n, G, pos, colors, sizes, legend)
        ax_n.set_title(f"{title} {_t('suffix_network')}", fontsize=13, fontweight="bold", pad=12)
        fig_n.tight_layout()
        result.update(fig_matrix=fig_m, fig_network=fig_n)
        if base:
            ext = os.path.splitext(save_path)[1] or ".png"
            result["matrix_path"] = f"{base}_matrix{ext}"
            result["network_path"] = f"{base}_network{ext}"
            _save(fig_m, result["matrix_path"])
            _save(fig_n, result["network_path"])
    else:
        fig, (ax_m, ax_n) = plt.subplots(1, 2, figsize=figsize,
                                         gridspec_kw={"width_ratios": [1, 1.2]})
        draw_matrix_heatmap(G, ax=ax_m, title=_t("suffix_matrix"), reorder_by=group_dict)
        _draw_graph(ax_n, G, pos, colors, sizes, legend)
        ax_n.set_title(_t("suffix_network"), fontsize=13, fontweight="bold", pad=12)
        fig.suptitle(title, fontsize=15, fontweight="bold", y=0.98)
        fig.tight_layout()
        result.update(fig=fig, axes=(ax_m, ax_n))
        if base:
            result["path"] = save_path
            _save(fig, save_path)

    if base:
        result["markdown_path"] = f"{base}_matrix.md"
        with open(result["markdown_path"], "w", encoding="utf-8") as f:
            f.write(markdown)
    if print_markdown:
        print(markdown)
    return result
