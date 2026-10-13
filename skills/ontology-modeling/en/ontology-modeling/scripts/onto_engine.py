"""
Ontology modeling engine built on owlready2.

Builds OWL ontologies (TBox and ABox), runs rule checks through SPARQL and
Python, runs an OWL reasoner (HermiT or Pellet), and exports reports and
Mermaid diagrams.

User-facing messages and report headings follow LANG ("ko" or "en").
"""
import os
import json
import sys
from typing import Optional

from owlready2 import (
    World, Thing, ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty,
    ObjectPropertyClass, DataPropertyClass
)

# ============================================================
# 0. Configuration
# ============================================================

LANG = "en"                       # language of messages and report headings
DEFAULT_IRI = "http://ontology.local/onto.owl"
DEFAULT_OUTPUT_DIR = "outputs"    # relative to the working directory
REASONER_TIMEOUT_SEC = 30         # enforced only where SIGALRM is available
VIZ_FULL_MAX = 50                 # individuals shown one by one up to this count
VIZ_AGGREGATED_MAX = 200          # class-level graph up to this count
SUMMARY_TOP_CLASSES = 30          # rows in the class distribution table
SUGGEST_CLASS_LIMIT = 5           # suggest_sparql_queries: class listing queries
SUGGEST_UNLINKED_LIMIT = 5        # suggest_sparql_queries: unlinked checks
SUGGEST_COUNT_LIMIT = 3           # suggest_sparql_queries: count queries
SUGGEST_VALUE_LIMIT = 3           # suggest_sparql_queries: value sort queries
MAX_CHAIN_DEPTH = 10              # depth guard for chain traversal
MAX_CHAIN_PATHS = 200             # path count guard for chain enumeration

ORDER_KEYWORDS = {"precedes", "follows", "leads_to", "next_stage",
                  "before", "after"}
EVIDENCE_KEYWORDS = {"supported_by", "evidence", "based_on",
                     "justified_by", "grounded_in"}
CAUSAL_KEYWORDS = {"causes", "caused_by", "results_in", "leads_to_effect"}
SYMMETRIC_KEYWORDS = {"cooperates", "collaborates", "partners",
                      "related", "similar", "connected"}
GOAL_KEYWORDS = ("goal", "objective")
RISK_KEYWORDS = ("risk", "constraint")
OUTPUT_KEYWORDS = ("output", "produces")
MANDATORY_KEYWORDS = ("mandatory", "required", "output", "deliverable")
ASSUMPTION_KEYWORDS = ("assumption", "premise")
RESERVED_DATA_PROPERTIES = ("description", "provenance_note")

MESSAGES = {
    "ko": {
        "world_loaded": "[INFO] OWL 파일 로드 완료: {path}",
        "world_created": "[INFO] 신규 온톨로지 생성: {iri}",
        "import_ok": "[INFO] 외부 온톨로지 import 완료: {src}",
        "import_fail": "[WARN] 외부 온톨로지 import 실패: {err}",
        "saved": "[INFO] 온톨로지 저장 완료: {path}",
        "outputs_saved": "[INFO] 산출물 저장 완료: {prefix}_*",
        "diff_no_before": "이전 OWL 파일 없음 (신규 구축)",
        "diff_load_fail": "이전 OWL 로드 실패: {err}",
        "diff_none": "변경 없음",
        "diff_classes": "클래스 +{a}/-{r}",
        "diff_individuals": "개체 +{a}/-{r}",
        "diff_properties": "속성 +{a}/-{r}",
        "class_not_found": "클래스 '{name}'를 온톨로지에서 찾을 수 없음",
        "class_missing": "클래스 '{name}' 없음",
        "classes_missing": "클래스 없음: {a} 또는 {b}",
        "individual_missing": "개체 '{name}' 없음",
        "reasoner_inconsistent_classes": "{r} 추론 결과 충족 불가 클래스 {n}건",
        "reasoner_ok": "{r} 추론 완료, 모순 없음",
        "reasoner_inconsistent_onto": "{r} 추론 결과 온톨로지 전체 모순 (상호 배타 위반 등)",
        "reasoner_timeout": "{r} {t}초 초과, Python 분석으로 대체 필요",
        "reasoner_error": "{r} 실행 불가({etype}), Python 분석으로 대체",
        "rdflib_fail": "[WARN] rdflib 변환 실패: {err}",
        "sparql_warn": "[WARN] SPARQL 오류: {err}",
        "sq_list_label": "{c} 개체 목록",
        "sq_list_desc": "{c} 클래스에 속한 개체를 조회",
        "sq_unlinked_label": "{d}의 {p} 미연결 개체",
        "sq_unlinked_desc": "{d} 개체 중 {p} 속성이 입력되지 않은 개체를 조회",
        "sq_count_label": "{d}별 {p} 연결 수",
        "sq_count_desc": "{d} 개체마다 {p} 속성으로 연결한 대상 수를 집계",
        "sq_value_label": "{d}의 {p} 값 정렬",
        "sq_value_desc": "{d} 개체를 {p} 값 기준으로 정렬하여 조회",
        "sq_path_label": "{d} 간 {p} 경로",
        "sq_path_desc": "{p} 속성을 따라 도달 가능한 개체 쌍을 추출",
        "ax_disjoint_union": "{c}의 하위 클래스 {n}개가 서로 겹치지 않고 합쳐서 {c} 전체를 이룬다고 선언",
        "ax_min_card": "모든 {d}가 {p} 속성으로 {r}를 1개 이상 가져야 한다고 선언 (요건 기록용, 빠진 연결 탐지는 SPARQL 점검 사용)",
        "ax_irreflexive": "'{p}' 속성이 자기 자신을 가리키지 못하게 선언",
        "ax_inverse": "'{a}'와 '{b}'를 서로 역방향 속성으로 선언하여 한쪽 입력 시 반대쪽 자동 완성",
        "ax_chain": "'{a}'를 거쳐 '{b}'에 이르는 간접 관계를 자동 도출",
        "ax_symmetric": "'{p}' 속성을 대칭으로 선언하여 한 방향 입력만으로 양방향 성립",
        "ax_datatype": "{d}의 {p} 값 범위로 자동 분류 가능 (THRESHOLD는 도메인 기준으로 설정)",
        "ax_swrl": "'{p}' 속성을 이용한 IF-THEN 규칙으로 새 사실 도출 가능",
        "tbox_title": "# TBox 정의서",
        "tbox_classes": "## 클래스 계층",
        "tbox_class_header": "| 클래스 | 상위 클래스 | 하위 클래스 | 설명 |",
        "tbox_props": "## 속성 정의",
        "tbox_prop_header": "| 속성 | 유형 | 정의역(domain) | 치역(range) |",
        "unspecified": "미지정",
        "abox_title": "# ABox 현황",
        "abox_header": "| 개체 | 속성 | 값 |",
        "summary_title": "# 온톨로지 요약 통계",
        "summary_classes": "- 클래스 수 {n}개",
        "summary_individuals": "- 개체 수 {n}개",
        "summary_isolated": "- 관계가 하나도 없는 개체 {n}개",
        "summary_class_dist": "## 클래스별 개체 분포",
        "summary_class_header": "| 클래스 | 개체 수 |",
        "summary_more": "| 외 {n}개 클래스 | |",
        "summary_prop_dist": "## 속성별 관계 분포",
        "summary_prop_header": "| 속성 | 관계 수 |",
        "route_order": "순서 속성 '{p}' 발견",
        "route_evidence": "근거 속성 '{p}' 발견",
        "route_causal": "인과 속성 '{p}' 발견",
        "route_assumption": "가정 클래스 '{c}' 발견",
        "route_assumption_order": "가정 클래스와 순서 속성이 함께 존재",
        "route_bidirectional": "{d}에서 {r}로 향하는 속성 {n}종 발견",
        "route_cardinality": "객체 속성 '{p}' 존재 (연결 수 기준 점검 가능)",
        "route_shared": "'{r}' 클래스를 {n}개 속성이 참조",
        "route_mandatory": "산출물 클래스 '{c}'와 순서 속성이 함께 존재",
        "route_provenance_note": "provenance_note 속성 발견 (판정 근거 기록 확인)",
        "route_mece": "하위 클래스가 2개 이상인 클래스 {k}건 발견 (외부 데이터 적재 시 분류 점검 권장)",
        "selftest_ok": "[OK] 엔진 정상 작동",
    },
    "en": {
        "world_loaded": "[INFO] Loaded OWL file: {path}",
        "world_created": "[INFO] Created new ontology: {iri}",
        "import_ok": "[INFO] Imported external ontology: {src}",
        "import_fail": "[WARN] Failed to import external ontology: {err}",
        "saved": "[INFO] Saved ontology: {path}",
        "outputs_saved": "[INFO] Saved outputs: {prefix}_*",
        "diff_no_before": "No previous OWL file (new build)",
        "diff_load_fail": "Failed to load previous OWL: {err}",
        "diff_none": "No changes",
        "diff_classes": "classes +{a}/-{r}",
        "diff_individuals": "individuals +{a}/-{r}",
        "diff_properties": "properties +{a}/-{r}",
        "class_not_found": "Class '{name}' not found in the ontology",
        "class_missing": "Class '{name}' does not exist",
        "classes_missing": "Class does not exist: {a} or {b}",
        "individual_missing": "Individual '{name}' does not exist",
        "reasoner_inconsistent_classes": "{r} found {n} unsatisfiable classes",
        "reasoner_ok": "{r} finished, no contradiction found",
        "reasoner_inconsistent_onto": "{r} found the whole ontology inconsistent (for example a disjointness violation)",
        "reasoner_timeout": "{r} exceeded {t} seconds, fall back to Python checks",
        "reasoner_error": "{r} could not run ({etype}), fall back to Python checks",
        "rdflib_fail": "[WARN] rdflib conversion failed: {err}",
        "sparql_warn": "[WARN] SPARQL error: {err}",
        "sq_list_label": "Individuals of {c}",
        "sq_list_desc": "List the individuals that belong to class {c}",
        "sq_unlinked_label": "{d} without {p}",
        "sq_unlinked_desc": "List {d} individuals that have no value for {p}",
        "sq_count_label": "{p} count per {d}",
        "sq_count_desc": "Count the targets each {d} individual links to through {p}",
        "sq_value_label": "{d} sorted by {p}",
        "sq_value_desc": "List {d} individuals sorted by the value of {p}",
        "sq_path_label": "{p} paths between {d}",
        "sq_path_desc": "Extract pairs of individuals reachable by following {p}",
        "ax_disjoint_union": "Declare that the {n} subclasses of {c} do not overlap and together make up all of {c}",
        "ax_min_card": "Declare that every {d} has at least one {r} through {p} (records the requirement; use a SPARQL check to find missing links)",
        "ax_irreflexive": "Declare that '{p}' never points to the individual itself",
        "ax_inverse": "Declare '{a}' and '{b}' as inverse properties so that entering one side fills in the other",
        "ax_chain": "Derive the indirect relation that goes through '{a}' and then '{b}'",
        "ax_symmetric": "Declare '{p}' symmetric so that one direction implies the other",
        "ax_datatype": "Classify {d} by the value range of {p} (set THRESHOLD from the domain)",
        "ax_swrl": "An IF-THEN rule using '{p}' can derive new facts",
        "tbox_title": "# TBox definitions",
        "tbox_classes": "## Class hierarchy",
        "tbox_class_header": "| Class | Parent classes | Subclasses | Description |",
        "tbox_props": "## Properties",
        "tbox_prop_header": "| Property | Type | Domain | Range |",
        "unspecified": "unspecified",
        "abox_title": "# ABox contents",
        "abox_header": "| Individual | Property | Value |",
        "summary_title": "# Ontology summary",
        "summary_classes": "- Classes: {n}",
        "summary_individuals": "- Individuals: {n}",
        "summary_isolated": "- Individuals without any relation: {n}",
        "summary_class_dist": "## Individuals per class",
        "summary_class_header": "| Class | Individuals |",
        "summary_more": "| {n} more classes | |",
        "summary_prop_dist": "## Relations per property",
        "summary_prop_header": "| Property | Relations |",
        "route_order": "Order property '{p}' found",
        "route_evidence": "Evidence property '{p}' found",
        "route_causal": "Causal property '{p}' found",
        "route_assumption": "Assumption class '{c}' found",
        "route_assumption_order": "Assumption class and order property both exist",
        "route_bidirectional": "{n} properties from {d} to {r} found",
        "route_cardinality": "Object property '{p}' exists (link counts can be checked)",
        "route_shared": "Class '{r}' is referenced by {n} properties",
        "route_mandatory": "Output class '{c}' and an order property both exist",
        "route_provenance_note": "provenance_note property found (check judgment records)",
        "route_mece": "{k} classes with two or more subclasses found (check classification when loading external data)",
        "selftest_ok": "[OK] Engine works",
    },
}


def _msg(key, **kwargs):
    """Return the localized message for key."""
    table = MESSAGES.get(LANG, MESSAGES["en"])
    return table[key].format(**kwargs)


def _as_list(value):
    """Normalize a property value to a list."""
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _first_text(value):
    """Return the first element of a property value as text, or ''."""
    values = _as_list(value)
    return str(values[0]) if values else ""


def _type_name(value):
    """Readable name of a class, datatype, or literal type."""
    if hasattr(value, "name"):
        return value.name
    if hasattr(value, "__name__"):
        return value.__name__
    return str(value)


# ============================================================
# 1. Reasoner
# ============================================================

def run_hermit_reasoner(world, onto, timeout_sec: int = REASONER_TIMEOUT_SEC,
                        reasoner: str = "hermit",
                        infer_property_values: bool = False,
                        infer_data_property_values: bool = False) -> dict:
    """
    Run an OWL reasoner. HermiT is the default; Pellet is optional.

    Args:
        world: owlready2 World
        onto: owlready2 ontology
        timeout_sec: timeout in seconds (POSIX main thread only)
        reasoner: "hermit" or "pellet"
        infer_property_values: infer object property values
        infer_data_property_values: infer data property values (Pellet only)

    Returns:
        {"success": bool, "mode": str, "message": str,
         "inconsistent_classes": list}
    """
    import signal
    import threading
    import owlready2
    from owlready2 import OwlReadyInconsistentOntologyError

    class _ReasonerTimeout(Exception):
        pass

    def _handler(signum, frame):
        raise _ReasonerTimeout()

    # SIGALRM does not exist on Windows and only works in the main thread.
    use_alarm = (hasattr(signal, "SIGALRM")
                 and threading.current_thread() is threading.main_thread())
    old_handler = None
    try:
        if use_alarm:
            old_handler = signal.signal(signal.SIGALRM, _handler)
            signal.alarm(timeout_sec)
        with onto:
            if reasoner == "pellet":
                owlready2.sync_reasoner_pellet(
                    world,
                    infer_property_values=infer_property_values,
                    infer_data_property_values=infer_data_property_values)
            else:
                owlready2.sync_reasoner(
                    world, infer_property_values=infer_property_values)
    except OwlReadyInconsistentOntologyError:
        return {"success": True, "mode": f"{reasoner}_inconsistent",
                "message": _msg("reasoner_inconsistent_onto", r=reasoner),
                "inconsistent_classes": ["ONTOLOGY_LEVEL_INCONSISTENCY"]}
    except _ReasonerTimeout:
        return {"success": False, "mode": "fallback",
                "message": _msg("reasoner_timeout", r=reasoner, t=timeout_sec),
                "inconsistent_classes": []}
    except Exception as e:
        return {"success": False, "mode": "fallback",
                "message": _msg("reasoner_error", r=reasoner,
                                etype=type(e).__name__),
                "inconsistent_classes": []}
    finally:
        if use_alarm:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)

    # owl:Nothing is always unsatisfiable, so it is not a finding.
    incon = [c.name for c in onto.inconsistent_classes()
             if hasattr(c, "name") and c.name != "Nothing"]
    if incon:
        return {"success": True, "mode": f"{reasoner}_inconsistent",
                "message": _msg("reasoner_inconsistent_classes",
                                r=reasoner, n=len(incon)),
                "inconsistent_classes": incon}
    return {"success": True, "mode": reasoner,
            "message": _msg("reasoner_ok", r=reasoner),
            "inconsistent_classes": []}


# ============================================================
# 2. World, files, versions
# ============================================================

def create_world(owl_path: Optional[str] = None,
                 label: str = None, version: str = None,
                 comment: str = None,
                 iri: str = None) -> tuple:
    """
    Create a new World or load an existing OWL file.
    label, version and comment are standard metadata (rdfs:label,
    owl:versionInfo, rdfs:comment) that tools such as Protege display.

    Returns: (world, onto)
    """
    world = World()
    if owl_path and os.path.exists(owl_path):
        onto = world.get_ontology(f"file://{os.path.abspath(owl_path)}").load()
        print(_msg("world_loaded", path=owl_path))
    else:
        base_iri = iri if iri else DEFAULT_IRI
        onto = world.get_ontology(base_iri)
        print(_msg("world_created", iri=base_iri))
    if label:
        onto.metadata.label.append(label)
    if version:
        onto.metadata.versionInfo.append(version)
    if comment:
        onto.metadata.comment.append(comment)
    return world, onto


def import_ontology(world, onto, iri_or_path: str):
    """
    Import an external ontology from a local path or IRI.

    Returns:
        the imported ontology, or None on failure
    """
    if os.path.exists(iri_or_path):
        ext_iri = f"file://{os.path.abspath(iri_or_path)}"
    else:
        ext_iri = iri_or_path
    try:
        ext_onto = world.get_ontology(ext_iri).load()
        onto.imported_ontologies.append(ext_onto)
        print(_msg("import_ok", src=iri_or_path))
        return ext_onto
    except Exception as e:
        print(_msg("import_fail", err=e), file=sys.stderr)
        return None


def save_ontology(onto, output_path: str, fmt: str = "rdfxml") -> str:
    """Save the ontology to an OWL file."""
    folder = os.path.dirname(os.path.abspath(output_path))
    os.makedirs(folder, exist_ok=True)
    onto.save(file=output_path, format=fmt)
    print(_msg("saved", path=output_path))
    return output_path


def diff_ontology(before_owl_path: str, onto_after) -> dict:
    """
    Compare a previous OWL file with the current ontology.

    Returns:
        {"added_classes": [], "removed_classes": [],
         "added_individuals": [], "removed_individuals": [],
         "added_properties": [], "removed_properties": [],
         "summary": str}
    """
    result = {
        "added_classes": [], "removed_classes": [],
        "added_individuals": [], "removed_individuals": [],
        "added_properties": [], "removed_properties": [],
        "summary": ""
    }
    if not os.path.exists(before_owl_path):
        result["summary"] = _msg("diff_no_before")
        return result

    before_world = World()
    try:
        before_onto = before_world.get_ontology(
            f"file://{os.path.abspath(before_owl_path)}").load()
    except Exception as e:
        result["summary"] = _msg("diff_load_fail", err=type(e).__name__)
        return result

    before_classes = {c.name for c in before_onto.classes() if hasattr(c, "name")}
    after_classes = {c.name for c in onto_after.classes() if hasattr(c, "name")}
    result["added_classes"] = sorted(after_classes - before_classes)
    result["removed_classes"] = sorted(before_classes - after_classes)

    before_inds = {i.name for i in before_onto.individuals() if hasattr(i, "name")}
    after_inds = {i.name for i in onto_after.individuals() if hasattr(i, "name")}
    result["added_individuals"] = sorted(after_inds - before_inds)
    result["removed_individuals"] = sorted(before_inds - after_inds)

    before_props = {p.python_name for p in before_onto.properties()}
    after_props = {p.python_name for p in onto_after.properties()}
    result["added_properties"] = sorted(after_props - before_props)
    result["removed_properties"] = sorted(before_props - after_props)

    parts = []
    pairs = [("diff_classes", "added_classes", "removed_classes"),
             ("diff_individuals", "added_individuals", "removed_individuals"),
             ("diff_properties", "added_properties", "removed_properties")]
    for key, added, removed in pairs:
        a, r = len(result[added]), len(result[removed])
        if a or r:
            parts.append(_msg(key, a=a, r=r))
    result["summary"] = ", ".join(parts) if parts else _msg("diff_none")
    return result


def save_all_outputs(world, onto, output_dir: str = DEFAULT_OUTPUT_DIR,
                     base_name: str = "analysis",
                     force_viz_mode: str = None) -> dict:
    """
    Save the OWL file, two Mermaid diagrams and a Markdown report.

    Files:
        {base_name}.owl, {base_name}_class.mermaid,
        {base_name}_instance.mermaid, {base_name}_report.md

    Returns:
        {"owl": path, "class_mermaid": path, "instance_mermaid": path,
         "report": path}
    """
    os.makedirs(output_dir, exist_ok=True)
    paths = {}

    owl_path = os.path.join(output_dir, f"{base_name}.owl")
    save_ontology(onto, owl_path)
    paths["owl"] = owl_path

    viz = export_smart_visualization(onto, force_mode=force_viz_mode)

    cls_path = os.path.join(output_dir, f"{base_name}_class.mermaid")
    with open(cls_path, "w", encoding="utf-8") as f:
        f.write(viz["class_diagram"])
    paths["class_mermaid"] = cls_path

    inst_path = os.path.join(output_dir, f"{base_name}_instance.mermaid")
    with open(inst_path, "w", encoding="utf-8") as f:
        f.write(viz["instance_view"])
    paths["instance_mermaid"] = inst_path

    report_path = os.path.join(output_dir, f"{base_name}_report.md")
    report_parts = [export_tbox_markdown(onto), export_abox_markdown(onto)]
    if viz.get("summary"):
        report_parts.append(viz["summary"])
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(report_parts))
    paths["report"] = report_path

    print(_msg("outputs_saved", prefix=os.path.join(output_dir, base_name)))
    return paths


# ============================================================
# 3. TBox helpers
# ============================================================

def _resolve_cls(onto, name_or_cls):
    """Resolve a class name to a class object. 'Thing' maps to owl:Thing."""
    if name_or_cls is None:
        return None
    if isinstance(name_or_cls, str):
        if name_or_cls == "Thing":
            return Thing
        resolved = onto[name_or_cls]
        if resolved is None:
            raise ValueError(_msg("class_not_found", name=name_or_cls))
        return resolved
    return name_or_cls


def build_class(onto, name: str, parent=None, description: str = None):
    """Create a class. parent accepts a class, a name, or a list (multiple inheritance)."""
    if parent is None:
        parents = (Thing,)
    elif isinstance(parent, list):
        resolved = [_resolve_cls(onto, p) for p in parent]
        parents = tuple(resolved) if resolved else (Thing,)
    else:
        parents = (_resolve_cls(onto, parent),)
    with onto:
        cls = type(name, parents, {"namespace": onto})
        if description:
            # A 'description' data property lets individuals carry readable text too.
            if not onto["description"]:
                desc_prop = type("description", (DataProperty,), {"namespace": onto})
                desc_prop.range = [str]
            cls.comment = [description]
    return cls


def build_object_property(onto, name: str, domain=None, range_cls=None,
                          is_transitive: bool = False,
                          is_functional: bool = False,
                          is_symmetric: bool = False,
                          is_asymmetric: bool = False,
                          is_reflexive: bool = False,
                          is_irreflexive: bool = False,
                          is_inverse_functional: bool = False):
    """Create an ObjectProperty. domain and range_cls accept names."""
    from owlready2 import (SymmetricProperty, AsymmetricProperty,
                           ReflexiveProperty, IrreflexiveProperty,
                           InverseFunctionalProperty)
    domain = _resolve_cls(onto, domain)
    if domain is Thing:
        domain = None  # owl:Thing is the default domain
    range_cls = _resolve_cls(onto, range_cls)
    if range_cls is Thing:
        range_cls = None
    bases = [ObjectProperty]
    flags = [(is_transitive, TransitiveProperty),
             (is_functional, FunctionalProperty),
             (is_symmetric, SymmetricProperty),
             (is_asymmetric, AsymmetricProperty),
             (is_reflexive, ReflexiveProperty),
             (is_irreflexive, IrreflexiveProperty),
             (is_inverse_functional, InverseFunctionalProperty)]
    bases.extend(base for enabled, base in flags if enabled)
    with onto:
        prop = type(name, tuple(bases), {"namespace": onto})
        if domain:
            prop.domain = [domain]
        if range_cls:
            prop.range = [range_cls]
    return prop


def build_data_property(onto, name: str, domain=None, range_type=str,
                        is_functional: bool = False):
    """Create a DataProperty. domain accepts a name."""
    domain = _resolve_cls(onto, domain)
    if domain is Thing:
        domain = None
    bases = [DataProperty]
    if is_functional:
        bases.append(FunctionalProperty)
    with onto:
        prop = type(name, tuple(bases), {"namespace": onto})
        if domain:
            prop.domain = [domain]
        prop.range = [range_type]
    return prop


def build_annotation_property(onto, name: str):
    """
    Create an AnnotationProperty for documentation only.
    Reasoners ignore annotation properties.
    """
    from owlready2 import AnnotationProperty
    with onto:
        prop = type(name, (AnnotationProperty,), {"namespace": onto})
    return prop


def build_sub_property(onto, child_property_name: str,
                       parent_property_name: str):
    """Declare SubPropertyOf between two properties. Returns the child property."""
    child = onto[child_property_name]
    parent = onto[parent_property_name]
    if child is None or parent is None:
        return None
    with onto:
        if parent not in child.is_a:
            child.is_a.append(parent)
    return child


def build_equivalent_properties(onto, property_name_a: str,
                                property_name_b: str):
    """Declare two properties equivalent (used when merging vocabularies)."""
    a = onto[property_name_a]
    b = onto[property_name_b]
    if a is None or b is None:
        return None
    with onto:
        if b not in a.equivalent_to:
            a.equivalent_to.append(b)
    return a


# ============================================================
# 4. ABox helpers
# ============================================================

def create_individual(onto, cls, name: str, **props):
    """Create an individual and assign properties. cls accepts a name."""
    cls = _resolve_cls(onto, cls)
    if cls is None:
        cls = Thing
    with onto:
        ind = cls(name)
        for key, value in props.items():
            setattr(ind, key, value)
    return ind


def add_to_class(onto, individual_name: str, class_name: str):
    """Add an existing individual to one more class."""
    ind = onto[individual_name]
    cls = onto[class_name]
    if ind is None or cls is None:
        return None
    with onto:
        if cls not in ind.is_a:
            ind.is_a.append(cls)
    return ind


def destroy_individual(onto, individual_name: str):
    """Delete an individual and every triple that mentions it."""
    from owlready2 import destroy_entity
    ind = onto[individual_name]
    if ind is None:
        return False
    destroy_entity(ind)
    return True


def build_same_as(onto, individual_name_a: str, individual_name_b: str):
    """Declare owl:sameAs between two individuals."""
    a = onto[individual_name_a]
    b = onto[individual_name_b]
    if a is None or b is None:
        return None
    with onto:
        if b not in a.equivalent_to:
            a.equivalent_to.append(b)
    return a


def update_property(onto, individual_name: str, property_name: str,
                    new_values):
    """Replace all values of a property on an individual."""
    ind = onto[individual_name]
    prop = onto[property_name]
    if ind is None or prop is None:
        return None
    with onto:
        if FunctionalProperty in prop.is_a:
            setattr(ind, property_name,
                    new_values[0] if isinstance(new_values, list) else new_values)
        else:
            setattr(ind, property_name, _as_list(new_values))
    return ind


def remove_property_value(onto, individual_name: str, property_name: str,
                          value):
    """Remove one value of a property. Returns True when a value was removed."""
    ind = onto[individual_name]
    prop = onto[property_name]
    if ind is None or prop is None:
        return False
    with onto:
        if FunctionalProperty in prop.is_a:
            if getattr(ind, property_name, None) == value:
                setattr(ind, property_name, None)
                return True
            return False
        values = getattr(ind, property_name, [])
        if value in values:
            values.remove(value)
            return True
        return False


def clear_property(onto, individual_name: str, property_name: str):
    """Remove all values of a property on an individual."""
    ind = onto[individual_name]
    prop = onto[property_name]
    if ind is None or prop is None:
        return False
    with onto:
        if FunctionalProperty in prop.is_a:
            setattr(ind, property_name, None)
        else:
            setattr(ind, property_name, [])
    return True


def _ensure_provenance_property(onto):
    """Declare provenance_note as a data property so it is saved and queryable."""
    if onto["provenance_note"] is None:
        with onto:
            prop = type("provenance_note", (DataProperty,), {"namespace": onto})
            prop.range = [str]


def set_with_provenance(individual, property_name: str, value, provenance: str):
    """
    Assign a judgment property and record why in provenance_note.

    Args:
        individual: owlready2 individual
        property_name: property to assign
        value: value or list of values, matching the property type
        provenance: the reason or source for the judgment
    """
    onto = individual.namespace.ontology
    _ensure_provenance_property(onto)
    with onto:
        setattr(individual, property_name, value)
        notes = list(_as_list(getattr(individual, "provenance_note", [])))
        notes.append(f"[{property_name}] {provenance}")
        individual.provenance_note = notes


# ============================================================
# 5. OWL axiom helpers
# ============================================================

def build_equivalent_class(onto, class_name: str, restriction_expr):
    """
    Set an EquivalentClass axiom (necessary and sufficient conditions) so a
    reasoner can classify individuals.

    Args:
        class_name: target class name
        restriction_expr: owlready2 expression, e.g. Parent & prop.some(Target)

    Returns:
        the class, or None
    """
    cls = onto[class_name]
    if cls is None:
        return None
    with onto:
        cls.equivalent_to = [restriction_expr]
    return cls


def build_disjoint_group(onto, class_names: list):
    """
    Declare the listed classes mutually disjoint (DisjointClasses).

    Returns:
        AllDisjoint object, or None when fewer than two classes exist
    """
    from owlready2 import AllDisjoint
    classes = [onto[n] for n in class_names if onto[n] is not None]
    if len(classes) < 2:
        return None
    with onto:
        return AllDisjoint(classes)


def _add_cardinality(onto, class_name, property_name, count, target_class_name,
                     kind):
    cls = onto[class_name]
    prop = onto[property_name]
    if cls is None or prop is None:
        return None
    restriction = getattr(prop, kind)
    with onto:
        if target_class_name and onto[target_class_name]:
            cls.is_a.append(restriction(count, onto[target_class_name]))
        else:
            cls.is_a.append(restriction(count))
    return cls


def build_min_cardinality(onto, class_name: str, property_name: str,
                          min_count: int, target_class_name: str = None):
    """
    Add a minCardinality restriction ("every X has at least N Y").
    Under the open world assumption a missing link is not a contradiction,
    so use a SPARQL check or close_world_scope to find missing links.
    """
    return _add_cardinality(onto, class_name, property_name, min_count,
                            target_class_name, "min")


def build_max_cardinality(onto, class_name: str, property_name: str,
                          max_count: int, target_class_name: str = None):
    """
    Add a maxCardinality restriction ("every X has at most N Y").
    OWL does not assume that different names mean different individuals,
    so declare build_all_different on the targets to detect an excess.
    """
    return _add_cardinality(onto, class_name, property_name, max_count,
                            target_class_name, "max")


def build_exact_cardinality(onto, class_name: str, property_name: str,
                            exact_count: int,
                            target_class_name: str = None):
    """Add an exactCardinality restriction ("every X has exactly N Y")."""
    return _add_cardinality(onto, class_name, property_name, exact_count,
                            target_class_name, "exactly")


def build_all_values_from(onto, class_name: str, property_name: str,
                          target_class_name: str):
    """Restrict every value of a property to one class (AllValuesFrom)."""
    cls = onto[class_name]
    prop = onto[property_name]
    target = onto[target_class_name]
    if cls is None or prop is None or target is None:
        return None
    with onto:
        cls.is_a.append(prop.only(target))
    return cls


def build_has_value(onto, class_name: str, property_name: str,
                    individual_name: str):
    """Require a link to one named individual (HasValue)."""
    cls = onto[class_name]
    prop = onto[property_name]
    ind = onto[individual_name]
    if cls is None or prop is None or ind is None:
        return None
    with onto:
        cls.is_a.append(prop.value(ind))
    return cls


def build_disjoint_union(onto, parent_class_name: str,
                         child_class_names: list):
    """
    Declare DisjointUnion: the children do not overlap and their union
    equals the parent (the axiom form of a mutually exclusive and
    collectively exhaustive split).

    Returns:
        the parent class, or None
    """
    parent = onto[parent_class_name]
    if parent is None:
        return None
    children = [onto[n] for n in child_class_names if onto[n] is not None]
    if len(children) < 2:
        return None
    with onto:
        parent.disjoint_unions.append(children)
    return parent


def build_one_of(onto, class_name: str, individual_names: list):
    """Define a class by enumerating its members (OneOf)."""
    from owlready2 import OneOf
    cls = onto[class_name]
    if cls is None:
        return None
    inds = [onto[n] for n in individual_names if onto[n] is not None]
    if not inds:
        return None
    with onto:
        cls.equivalent_to.append(OneOf(inds))
    return cls


def build_all_different(onto, individual_names: list):
    """Declare that the listed individuals are all different (AllDifferent)."""
    from owlready2 import AllDifferent
    inds = [onto[n] for n in individual_names if onto[n] is not None]
    if len(inds) < 2:
        return None
    with onto:
        return AllDifferent(inds)


def close_world_scope(onto, class_names: list = None,
                      individual_names: list = None) -> dict:
    """
    Declare that the entered facts of the given individuals are complete
    (closed world). After this, a reasoner can conclude that a missing link
    does not exist. Use it only for a scope whose enumeration is complete.

    Args:
        class_names: close every individual of these classes
        individual_names: close these individuals

    Returns:
        {"closed": [individual names], "count": int}
    """
    from owlready2 import close_world
    targets = []
    for cls_name in class_names or []:
        cls = onto[cls_name]
        if cls is not None:
            targets.extend(cls.instances())
    for ind_name in individual_names or []:
        ind = onto[ind_name]
        if ind is not None:
            targets.append(ind)
    closed = []
    with onto:
        for ind in targets:
            if ind.name in closed:
                continue
            close_world(ind)
            closed.append(ind.name)
    return {"closed": closed, "count": len(closed)}


def build_swrl_rule(onto, rule_str: str, name: str = None):
    """
    Add a SWRL rule. HermiT runs DL-safe rules without built-ins.
    Rules with built-ins such as greaterThan need Pellet.

    Args:
        rule_str: e.g. "Person(?p), manages(?p, ?x) -> responsible_for(?p, ?x)"
        name: optional label

    Returns:
        Imp object
    """
    from owlready2 import Imp
    with onto:
        imp = Imp()
        imp.set_as_rule(rule_str)
        if name:
            imp.label = [name]
    return imp


def list_swrl_rules(onto):
    """
    List SWRL rules.

    Returns:
        [{"rule": Imp, "label": str or None, "body": [str], "head": [str]}]
    """
    results = []
    for imp in onto.rules():
        results.append({
            "rule": imp,
            "label": imp.label[0] if imp.label else None,
            "body": [str(a) for a in imp.body] if imp.body else [],
            "head": [str(a) for a in imp.head] if imp.head else [],
        })
    return results


def delete_swrl_rule(onto, rule_or_label):
    """Delete a SWRL rule by Imp object or label. Returns True when deleted."""
    from owlready2 import destroy_entity, Imp
    if isinstance(rule_or_label, Imp):
        destroy_entity(rule_or_label)
        return True
    for imp in onto.rules():
        if imp.label and rule_or_label in imp.label:
            destroy_entity(imp)
            return True
    return False


# ============================================================
# 6. Lookup and SPARQL
# ============================================================

def as_rdflib_graph(onto):
    """
    Return an rdflib-compatible graph of the ontology's World (all loaded
    ontologies), or None when rdflib is missing.
    """
    try:
        return onto.world.as_rdflib_graph()
    except Exception as e:
        print(_msg("rdflib_fail", err=e), file=sys.stderr)
        return None


def query_sparql(world, sparql_str: str, silent: bool = False) -> list:
    """Run a full SPARQL query and return raw rows."""
    try:
        return list(world.sparql(sparql_str))
    except Exception as e:
        if not silent:
            print(_msg("sparql_warn", err=e), file=sys.stderr)
        return []


def get_class_hierarchy(onto) -> dict:
    """Return {class: {"parents", "children", "ancestors"}}."""
    hierarchy = {}
    for cls in onto.classes():
        hierarchy[cls.name] = {
            "parents": [p.name for p in cls.is_a
                        if hasattr(p, "name") and p != Thing],
            "children": [c.name for c in cls.subclasses()],
            "ancestors": [a.name for a in cls.ancestors()
                          if a != Thing and a != cls],
        }
    return hierarchy


def get_all_individuals(onto) -> list:
    """Return [{"name", "classes", "properties"}] for every individual."""
    result = []
    for ind in onto.individuals():
        props = {}
        for prop in ind.get_properties():
            vals = getattr(ind, prop.python_name, None)
            if vals is None:
                continue
            if isinstance(vals, list):
                props[prop.python_name] = [_type_name(v) if hasattr(v, "name")
                                           else str(v) for v in vals]
            else:
                props[prop.python_name] = (vals.name if hasattr(vals, "name")
                                           else str(vals))
        result.append({
            "name": ind.name,
            "classes": [c.name for c in ind.is_a if hasattr(c, "name")],
            "properties": props,
        })
    return result


SPARQL_CHECKS = {
    "mece_overlap": {
        "description": "individuals that belong to both classes",
        "query": "SELECT ?ind WHERE {{ ?ind a :{class_a} . ?ind a :{class_b} }}",
        "params": ["class_a", "class_b"],
    },
    "unsupported": {
        "description": "individuals without any value for a property",
        "query": """SELECT ?ind WHERE {{
            ?ind a :{target_class} .
            FILTER NOT EXISTS {{ ?ind :{link_property} ?ref }}
        }}""",
        "params": ["target_class", "link_property"],
    },
    "coverage": {
        "description": "individuals that no individual of ref_class points to",
        "query": """SELECT ?orphan WHERE {{
            ?orphan a :{source_class} .
            FILTER NOT EXISTS {{
                ?ref a :{ref_class} .
                ?ref :{link_property} ?orphan
            }}
        }}""",
        "params": ["source_class", "ref_class", "link_property"],
    },
    "edges": {
        "description": "all edges of a property",
        "query": "SELECT ?src ?tgt WHERE {{ ?src :{property} ?tgt }}",
        "params": ["property"],
    },
    "cardinality_count": {
        "description": "number of links per individual",
        "query": """SELECT ?ind (COUNT(?t) AS ?cnt) WHERE {{
            ?ind a :{parent_class} . ?ind :{property_name} ?t
        }} GROUP BY ?ind""",
        "params": ["parent_class", "property_name"],
    },
    "refs_for_class": {
        "description": "targets referenced by individuals of a class",
        "query": """SELECT ?target WHERE {{
            ?ind a :{subject_class} . ?ind :{link_property} ?target
        }}""",
        "params": ["subject_class", "link_property"],
    },
    "value_below": {
        "description": "individuals whose value is below a minimum",
        "query": """SELECT ?ind ?val WHERE {{
            ?ind a :{target_class} . ?ind :{value_property} ?val .
            FILTER(?val < {min_val})
        }}""",
        "params": ["target_class", "value_property", "min_val"],
    },
    "value_above": {
        "description": "individuals whose value is above a maximum",
        "query": """SELECT ?ind ?val WHERE {{
            ?ind a :{target_class} . ?ind :{value_property} ?val .
            FILTER(?val > {max_val})
        }}""",
        "params": ["target_class", "value_property", "max_val"],
    },
    "downstream": {
        "description": "individuals reachable along a property path",
        "query": "SELECT ?d WHERE {{ :{start} :{order_property}+ ?d }}",
        "params": ["start", "order_property"],
    },
    "conflict_dual_ref": {
        "description": "individuals that point to the same target through two properties",
        "query": """SELECT ?ind ?target WHERE {{
            ?ind :{prop_a} ?target . ?ind :{prop_b} ?target
        }}""",
        "params": ["prop_a", "prop_b"],
    },
    "mandatory_missing": {
        "description": "stages without a required output class",
        "query": """SELECT ?stage WHERE {{
            ?stage a :{stage_class} .
            FILTER NOT EXISTS {{
                ?stage :{output_property} ?out .
                ?out a :{required_class}
            }}
        }}""",
        "params": ["stage_class", "output_property", "required_class"],
    },
    "stage_unlinked": {
        "description": "stage individuals without a link to the next stage",
        "query": """SELECT ?ind WHERE {{
            ?ind a :{stage_class} .
            FILTER NOT EXISTS {{ ?ind :{link_property} ?next }}
        }}""",
        "params": ["stage_class", "link_property"],
    },
}


def run_sparql_check(world, check_name, onto=None, **params):
    """
    Run a SPARQL check.

    Template mode: check_name is a key of SPARQL_CHECKS.
    Ad hoc mode: check_name is "_adhoc" and params has sparql_body
    (and optionally label).

    Returns:
        {"check": str, "sparql": str, "results": list, "count": int,
         "pass": bool (True when no rows)}
    """
    if check_name == "_adhoc":
        body = params.pop("sparql_body")
        label = params.pop("label", "adhoc")
    else:
        body = SPARQL_CHECKS[check_name]["query"].format(**params)
        label = check_name

    sparql = f"PREFIX : <{onto.base_iri}>\n{body}" if onto is not None else body
    results = []
    for row in query_sparql(world, sparql):
        converted = tuple(r.name if hasattr(r, "name") else r for r in row)
        results.append(converted[0] if len(converted) == 1 else converted)
    return {"check": label, "sparql": sparql, "results": results,
            "count": len(results), "pass": len(results) == 0}


def query_onto(world, onto, sparql_body):
    """
    Run a free SPARQL query with prefixes set automatically.
    ':' points to the current ontology; imported ontologies get their own prefix.

    Returns:
        raw rows (list of tuples)
    """
    prefixes = [f"PREFIX : <{onto.base_iri}>"]
    for i, imp in enumerate(onto.imported_ontologies):
        if hasattr(imp, "base_iri"):
            name = imp.name if getattr(imp, "name", None) else f"ext{i}"
            prefixes.append(f"PREFIX {name}: <{imp.base_iri}>")
    return query_sparql(world, "\n".join(prefixes) + "\n" + sparql_body)


def _property_summaries(onto):
    """Split properties into object and data property summaries."""
    obj_props, data_props = [], []
    for prop in onto.properties():
        domain = [d.name for d in (prop.domain or []) if hasattr(d, "name")]
        if isinstance(prop, ObjectPropertyClass):
            obj_props.append({
                "name": prop.python_name,
                "domain": domain,
                "range": [r.name for r in (prop.range or []) if hasattr(r, "name")],
                "is_transitive": TransitiveProperty in prop.is_a,
            })
        elif isinstance(prop, DataPropertyClass):
            data_props.append({"name": prop.python_name, "domain": domain})
    return obj_props, data_props


def suggest_sparql_queries(onto):
    """
    Suggest exploratory SPARQL queries from the current TBox.

    Returns:
        [{"label": str, "sparql": str, "description": str}]
    """
    suggestions = []
    classes = [c.name for c in onto.classes() if hasattr(c, "name")]
    obj_props, data_props = _property_summaries(onto)

    for c in classes[:SUGGEST_CLASS_LIMIT]:
        suggestions.append({
            "label": _msg("sq_list_label", c=c),
            "sparql": f"SELECT ?x WHERE {{ ?x a :{c} }}",
            "description": _msg("sq_list_desc", c=c)})

    for op in obj_props[:SUGGEST_UNLINKED_LIMIT]:
        if op["domain"]:
            d, p = op["domain"][0], op["name"]
            suggestions.append({
                "label": _msg("sq_unlinked_label", d=d, p=p),
                "sparql": (f"SELECT ?x WHERE {{ ?x a :{d} . "
                           f"FILTER NOT EXISTS {{ ?x :{p} ?y }} }}"),
                "description": _msg("sq_unlinked_desc", d=d, p=p)})

    for op in obj_props[:SUGGEST_COUNT_LIMIT]:
        if op["domain"]:
            d, p = op["domain"][0], op["name"]
            suggestions.append({
                "label": _msg("sq_count_label", d=d, p=p),
                "sparql": (f"SELECT ?x (COUNT(?y) AS ?cnt) WHERE {{ "
                           f"?x a :{d} . ?x :{p} ?y }} "
                           f"GROUP BY ?x ORDER BY DESC(?cnt)"),
                "description": _msg("sq_count_desc", d=d, p=p)})

    for dp in data_props[:SUGGEST_VALUE_LIMIT]:
        if dp["domain"] and dp["name"] not in RESERVED_DATA_PROPERTIES:
            d, p = dp["domain"][0], dp["name"]
            suggestions.append({
                "label": _msg("sq_value_label", d=d, p=p),
                "sparql": (f"SELECT ?x ?val WHERE {{ ?x a :{d} . "
                           f"?x :{p} ?val }} ORDER BY DESC(?val)"),
                "description": _msg("sq_value_desc", d=d, p=p)})

    for op in obj_props:
        if op["is_transitive"] and op["domain"]:
            d, p = op["domain"][0], op["name"]
            suggestions.append({
                "label": _msg("sq_path_label", d=d, p=p),
                "sparql": (f"SELECT ?start ?end WHERE {{ ?start a :{d} . "
                           f"?start :{p}+ ?end }}"),
                "description": _msg("sq_path_desc", p=p)})
            break

    return suggestions


def suggest_axioms(onto):
    """
    Suggest axioms from the current TBox structure. Call it only after the
    TBox is agreed, never while designing the TBox.

    Returns:
        [{"axiom": str, "target": str, "code": str, "description": str,
          "priority": "required" or "recommended"}]
    """
    suggestions = []
    classes = {c.name: c for c in onto.classes() if hasattr(c, "name")}
    obj_props, data_props = _property_summaries(onto)

    # 1. DisjointUnion for classes with two or more subclasses
    for cls_name, cls in classes.items():
        subs = [s.name for s in cls.subclasses() if hasattr(s, "name")]
        if len(subs) >= 2 and not cls.disjoint_unions:
            suggestions.append({
                "axiom": "DisjointUnion", "target": cls_name,
                "code": f'build_disjoint_union(onto, "{cls_name}", {subs})',
                "description": _msg("ax_disjoint_union", c=cls_name, n=len(subs)),
                "priority": "recommended"})

    # 2. MinCardinality for object properties with domain and range
    for op in obj_props:
        if op["domain"] and op["range"]:
            d, r, p = op["domain"][0], op["range"][0], op["name"]
            suggestions.append({
                "axiom": "MinCardinality", "target": f"{d}.{p}",
                "code": f'build_min_cardinality(onto, "{d}", "{p}", 1, "{r}")',
                "description": _msg("ax_min_card", d=d, p=p, r=r),
                "priority": "recommended"})

    # 3. Irreflexive for order properties
    for op in obj_props:
        if op["name"].lower() in ORDER_KEYWORDS:
            suggestions.append({
                "axiom": "IrreflexiveProperty", "target": op["name"],
                "code": "# recreate with build_object_property(..., is_irreflexive=True)",
                "description": _msg("ax_irreflexive", p=op["name"]),
                "priority": "recommended"})

    # 4. InverseProperty for property pairs with swapped domain and range
    for i, op1 in enumerate(obj_props):
        for op2 in obj_props[i + 1:]:
            if op1["domain"] == op2["range"] and op1["range"] == op2["domain"]:
                suggestions.append({
                    "axiom": "InverseProperty",
                    "target": f"{op1['name']} / {op2['name']}",
                    "code": (f'with onto:\n    onto["{op2["name"]}"].'
                             f'inverse_property = onto["{op1["name"]}"]'),
                    "description": _msg("ax_inverse", a=op1["name"], b=op2["name"]),
                    "priority": "recommended"})

    # 5. PropertyChain for A -> B -> C patterns
    range_to_props = {}
    for op in obj_props:
        for r in op["range"]:
            range_to_props.setdefault(r, []).append(op)
    for op in obj_props:
        for d in op["domain"]:
            for upstream in range_to_props.get(d, []):
                if upstream["name"] == op["name"] or not op["range"]:
                    continue
                new_name = f"indirect_{upstream['name']}_{op['name']}"
                suggestions.append({
                    "axiom": "PropertyChain",
                    "target": f"{upstream['name']} + {op['name']}",
                    "code": (
                        "from owlready2 import PropertyChain\n"
                        "with onto:\n"
                        f'    new_prop = build_object_property(onto, "{new_name}", '
                        f'"{upstream["domain"][0]}", "{op["range"][0]}")\n'
                        "    new_prop.property_chain.append(PropertyChain("
                        f'[onto["{upstream["name"]}"], onto["{op["name"]}"]]))'),
                    "description": _msg("ax_chain", a=upstream["name"], b=op["name"]),
                    "priority": "recommended"})

    # 6. Symmetric for same-class properties with symmetric wording
    for op in obj_props:
        if (op["domain"] and op["domain"] == op["range"]
                and not op["is_transitive"]
                and any(kw in op["name"].lower() for kw in SYMMETRIC_KEYWORDS)):
            suggestions.append({
                "axiom": "SymmetricProperty", "target": op["name"],
                "code": "# recreate with build_object_property(..., is_symmetric=True)",
                "description": _msg("ax_symmetric", p=op["name"]),
                "priority": "recommended"})

    # 7. ConstrainedDatatype for numeric data properties
    for dp in data_props:
        if not dp["domain"] or dp["name"] in RESERVED_DATA_PROPERTIES:
            continue
        prop_obj = onto[dp["name"]]
        numeric = [r for r in (prop_obj.range or [])
                   if _type_name(r) in ("int", "float")]
        if numeric:
            d, p, t = dp["domain"][0], dp["name"], _type_name(numeric[0])
            suggestions.append({
                "axiom": "ConstrainedDatatype", "target": f"{d}.{p}",
                "code": (f'build_equivalent_class(onto, "High{d}",\n'
                         f'    onto["{d}"] & onto["{p}"].some('
                         f'ConstrainedDatatype({t}, min_inclusive=THRESHOLD)))'),
                "description": _msg("ax_datatype", d=d, p=p),
                "priority": "recommended"})

    # 8. SWRL candidate when a transitive property exists
    transitive_props = [op for op in obj_props if op["is_transitive"]]
    if transitive_props and len(obj_props) >= 2:
        tp = transitive_props[0]
        head_class = tp["domain"][0] if tp["domain"] else "Thing"
        suggestions.append({
            "axiom": "SWRL", "target": tp["name"],
            "code": (f'build_swrl_rule(onto,\n    "{head_class}(?x), '
                     f'{tp["name"]}(?x, ?y) -> ...",\n    name="custom_rule")'),
            "description": _msg("ax_swrl", p=tp["name"]),
            "priority": "recommended"})

    return suggestions


# ============================================================
# 7. SPARQL-based checks (15)
# ============================================================

def check_mece(world, onto, parent_cls_name):
    """
    Check the subclasses of a parent class: overlap between subclasses
    and parent individuals that fit no subclass.

    Returns:
        {"parent", "subclasses", "mutually_exclusive", "overlaps",
         "collectively_exhaustive", "unclassified", "pass"}
    """
    cls = onto[parent_cls_name]
    if cls is None:
        return {"error": _msg("class_missing", name=parent_cls_name)}

    subs = list(cls.subclasses())
    overlaps = []
    for i, s1 in enumerate(subs):
        for s2 in subs[i + 1:]:
            r = run_sparql_check(world, "mece_overlap", onto=onto,
                                 class_a=s1.name, class_b=s2.name)
            if r["results"]:
                overlaps.append({"class_a": s1.name, "class_b": s2.name,
                                 "shared_individuals": list(r["results"])})

    parent_inds = {ind.name for ind in cls.instances()}
    classified = set()
    for s in subs:
        classified |= {ind.name for ind in s.instances()}
    unclassified = sorted(parent_inds - classified)

    return {"parent": parent_cls_name,
            "subclasses": [s.name for s in subs],
            "mutually_exclusive": not overlaps,
            "overlaps": overlaps,
            "collectively_exhaustive": not unclassified,
            "unclassified": unclassified,
            "pass": not overlaps and not unclassified}


def _enumerate_paths(graph, start, max_depth=MAX_CHAIN_DEPTH):
    """All simple paths from start until a node has no unvisited successor."""
    paths = []
    stack = [[start]]
    while stack and len(paths) < MAX_CHAIN_PATHS:
        path = stack.pop()
        nexts = [n for n in graph.get(path[-1], []) if n not in path]
        if not nexts or len(path) > max_depth:
            paths.append(path)
            continue
        for n in reversed(nexts):
            stack.append(path + [n])
    return paths


def check_causal_chain(world, onto):
    """
    Extract every causal path along the 'causes' property, starting from
    individuals that nothing causes. Branches are listed as separate paths.

    Returns:
        [[individual, ...], ...]
    """
    if onto["causes"] is None:
        return []
    r = run_sparql_check(world, "edges", onto=onto, property="causes")
    if not r["results"]:
        return []

    graph, targets = {}, set()
    for src, tgt in r["results"]:
        graph.setdefault(src, []).append(tgt)
        targets.add(tgt)

    chains = []
    for root in sorted(set(graph) - targets):
        chains.extend(_enumerate_paths(graph, root))
    return chains


def check_constraint_conflicts(world, onto):
    """
    Find individuals that point to the same target through a goal-like
    property and a risk-like property (matched by property name keywords).

    Returns:
        [{"individual": str, "conflicting_terms": [str]}]
    """
    names = [p.python_name for p in onto.properties()]
    goal_props = [n for n in names if any(k in n.lower() for k in GOAL_KEYWORDS)]
    risk_props = [n for n in names if any(k in n.lower() for k in RISK_KEYWORDS)]
    conflicts, seen = [], set()
    for gp in goal_props:
        for rp in risk_props:
            r = run_sparql_check(world, "conflict_dual_ref", onto=onto,
                                 prop_a=gp, prop_b=rp)
            for item in r["results"]:
                ind_name, target = item if isinstance(item, tuple) else (item, "unknown")
                key = (ind_name, str(target))
                if key not in seen:
                    seen.add(key)
                    conflicts.append({"individual": ind_name,
                                      "conflicting_terms": [str(target)]})
    return conflicts


def check_unsupported_assumptions(world, onto):
    """
    List Assumption individuals without supported_by (entered data only).

    Returns:
        [{"assumption": str, "description": str}]
    """
    if onto["Assumption"] is None:
        return []
    r = run_sparql_check(world, "unsupported", onto=onto,
                         target_class="Assumption", link_property="supported_by")
    unsupported = []
    for name in r["results"]:
        ind = onto[name]
        desc = _first_text(getattr(ind, "description", None)) if ind else ""
        unsupported.append({"assumption": name, "description": desc})
    return unsupported


def check_process_completeness(world, onto):
    """
    Check reachability along 'precedes' from start steps.

    Returns:
        {"total_steps", "start_steps", "end_steps", "unreachable_steps",
         "complete"} or {"status": "no_process_found", "edges": []}
    """
    if onto["precedes"] is None:
        return {"status": "no_process_found", "edges": []}
    r = run_sparql_check(world, "edges", onto=onto, property="precedes")
    if not r["results"]:
        return {"status": "no_process_found", "edges": []}

    graph, all_nodes, targets = {}, set(), set()
    for src, tgt in r["results"]:
        graph.setdefault(src, []).append(tgt)
        all_nodes.update((src, tgt))
        targets.add(tgt)

    starts = all_nodes - targets
    ends = all_nodes - set(graph)
    reachable, queue = set(), list(starts)
    while queue:
        node = queue.pop(0)
        if node in reachable:
            continue
        reachable.add(node)
        queue.extend(graph.get(node, []))
    unreachable = all_nodes - reachable

    return {"total_steps": len(all_nodes),
            "start_steps": sorted(starts),
            "end_steps": sorted(ends),
            "unreachable_steps": sorted(unreachable),
            "complete": not unreachable and bool(starts) and bool(ends)}


def check_coverage(world, onto, source_class_name, referencing_class_name,
                   link_property, referencing_scope="any"):
    """
    List source individuals that no referencing individual points to.

    Returns:
        [{"individual", "class", "not_referenced_by"}]
    """
    if onto[source_class_name] is None or onto[referencing_class_name] is None:
        return []
    r = run_sparql_check(world, "coverage", onto=onto,
                         source_class=source_class_name,
                         ref_class=referencing_class_name,
                         link_property=link_property)
    return [{"individual": name, "class": source_class_name,
             "not_referenced_by": referencing_class_name}
            for name in r["results"]]


def check_cardinality(world, onto, parent_class_name, property_name, expected):
    """
    Compare link counts with an expected number. Individuals with no link
    count as 0.

    Returns:
        [{"individual", "class", "property", "actual", "expected"}]
    """
    cls = onto[parent_class_name]
    if cls is None:
        return []
    r = run_sparql_check(world, "cardinality_count", onto=onto,
                         parent_class=parent_class_name,
                         property_name=property_name)
    violations, counted = [], {}
    for item in r["results"]:
        if not isinstance(item, tuple):
            continue
        ind_name, cnt = item
        counted[ind_name] = int(cnt)
        if int(cnt) != expected:
            violations.append({"individual": ind_name, "class": parent_class_name,
                               "property": property_name,
                               "actual": int(cnt), "expected": expected})
    for ind in cls.instances():
        if ind.name not in counted and expected != 0:
            violations.append({"individual": ind.name, "class": parent_class_name,
                               "property": property_name,
                               "actual": 0, "expected": expected})
    return violations


def check_provenance(world, onto, target_class_names, link_property):
    """
    List individuals of the given classes without any value for link_property.

    Returns:
        [{"individual", "class", "missing_property"}]
    """
    disconnected = []
    for cls_name in target_class_names:
        if onto[cls_name] is None:
            continue
        r = run_sparql_check(world, "unsupported", onto=onto,
                             target_class=cls_name, link_property=link_property)
        disconnected.extend({"individual": name, "class": cls_name,
                             "missing_property": link_property}
                            for name in r["results"])
    return disconnected


def check_shared_reference(world, onto, subject_class_names, link_property):
    """
    Compare the targets that several classes reference through one property.

    Returns:
        {"class_references", "shared", "discrepancies", "consistent"}
    """
    class_refs = {}
    for cls_name in subject_class_names:
        if onto[cls_name] is None:
            class_refs[cls_name] = set()
            continue
        r = run_sparql_check(world, "refs_for_class", onto=onto,
                             subject_class=cls_name, link_property=link_property)
        class_refs[cls_name] = set(r["results"])

    non_empty = [s for s in class_refs.values() if s]
    shared = set.intersection(*non_empty) if non_empty else set()
    discrepancies = []
    names = list(class_refs)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            only_a = class_refs[a] - class_refs[b]
            only_b = class_refs[b] - class_refs[a]
            if only_a or only_b:
                discrepancies.append({"class_a": a, "class_b": b,
                                      "only_in_a": sorted(only_a),
                                      "only_in_b": sorted(only_b)})
    return {"class_references": {k: sorted(v) for k, v in class_refs.items()},
            "shared": sorted(shared),
            "discrepancies": discrepancies,
            "consistent": not discrepancies}


def _range_violations(world, onto, cls_name, value_property, low, high):
    violations = []
    checks = [("value_below", "min_val", low, "below_minimum"),
              ("value_above", "max_val", high, "above_maximum")]
    for check, param, bound, vtype in checks:
        if bound is None:
            continue
        r = run_sparql_check(world, check, onto=onto, target_class=cls_name,
                             value_property=value_property, **{param: bound})
        for item in r["results"]:
            name, val = item if isinstance(item, tuple) else (item, None)
            violations.append({"individual": name, "value": val,
                               "min": low, "max": high, "violation_type": vtype})
    return violations


def check_value_range(world, onto, target_class_name, value_property,
                      min_val=None, max_val=None, range_rules=None):
    """
    Find values outside a range. range_rules sets a range per class:
    {"ClassName": {"min": x, "max": y}}.

    Returns:
        [{"individual", "value", "min", "max", "violation_type"}]
    """
    if onto[target_class_name] is None:
        return [{"error": _msg("class_missing", name=target_class_name)}]
    if range_rules:
        violations = []
        for rule_cls, bounds in range_rules.items():
            violations.extend(_range_violations(
                world, onto, rule_cls, value_property,
                bounds.get("min"), bounds.get("max")))
        return violations
    return _range_violations(world, onto, target_class_name, value_property,
                             min_val, max_val)


def check_bidirectional_coverage(world, onto, class_a, class_b,
                                 a_to_b_property, b_to_a_property=None):
    """
    Check links in both directions between two classes.
    Without b_to_a_property, B individuals that no A points to are listed.

    Returns:
        {"a_without_b": [str], "b_without_a": [str], "complete": bool}
    """
    if onto[class_a] is None or onto[class_b] is None:
        return {"error": _msg("classes_missing", a=class_a, b=class_b)}
    r_a = run_sparql_check(world, "unsupported", onto=onto,
                           target_class=class_a, link_property=a_to_b_property)
    if b_to_a_property:
        r_b = run_sparql_check(world, "unsupported", onto=onto,
                               target_class=class_b, link_property=b_to_a_property)
    else:
        r_b = run_sparql_check(world, "coverage", onto=onto,
                               source_class=class_b, ref_class=class_a,
                               link_property=a_to_b_property)
    a_without_b, b_without_a = list(r_a["results"]), list(r_b["results"])
    return {"a_without_b": a_without_b, "b_without_a": b_without_a,
            "complete": not a_without_b and not b_without_a}


def check_reverse_chain(world, onto, effect_individual_name,
                        cause_property, max_depth=MAX_CHAIN_DEPTH):
    """
    Trace causes backward from an effect. Every branch is followed.

    Returns:
        {"chain": first path, "chains": all paths, "depth": longest depth,
         "has_cycle": bool, "dead_end": effect name when it has no cause,
         "root": end of the first path or None, "roots": [str]}
    """
    start = onto[effect_individual_name]
    if start is None:
        return {"error": _msg("individual_missing", name=effect_individual_name)}

    chains, has_cycle = [], False
    stack = [(start, [effect_individual_name])]
    while stack and len(chains) < MAX_CHAIN_PATHS:
        node, path = stack.pop()
        causes = [c for c in _as_list(getattr(node, cause_property, []))
                  if hasattr(c, "name")]
        if not causes or len(path) > max_depth:
            chains.append(path)
            continue
        for cause in reversed(causes):
            if cause.name in path:
                has_cycle = True
                chains.append(path + [f"{cause.name} [cycle]"])
            else:
                stack.append((cause, path + [cause.name]))

    first = chains[0] if chains else [effect_individual_name]
    roots = sorted({p[-1] for p in chains
                    if len(p) > 1 and not p[-1].endswith("[cycle]")})
    return {"chain": first,
            "chains": chains,
            "depth": max((len(p) - 1 for p in chains), default=0),
            "has_cycle": has_cycle,
            "dead_end": effect_individual_name if len(first) == 1 else None,
            "root": None if first[-1].endswith("[cycle]") else first[-1],
            "roots": roots}


def check_mandatory_outputs(world, onto, stage_class_name, output_property,
                            required_output_classes):
    """
    List stages that lack a required output class.

    Returns:
        [{"stage": str, "missing_outputs": [str]}]
    """
    if onto[stage_class_name] is None:
        return [{"error": _msg("class_missing", name=stage_class_name)}]
    by_stage = {}
    for req_cls in required_output_classes:
        if onto[req_cls] is None:
            continue
        r = run_sparql_check(world, "mandatory_missing", onto=onto,
                             stage_class=stage_class_name,
                             output_property=output_property,
                             required_class=req_cls)
        for name in r["results"]:
            by_stage.setdefault(name, []).append(req_cls)
    return [{"stage": s, "missing_outputs": m} for s, m in by_stage.items()]


def check_assumption_impact(world, onto, assumption_name,
                            attached_property="attached_to",
                            stage_order_property="precedes"):
    """
    Estimate which later stages and outputs depend on an assumption.

    Returns:
        {"assumption", "attached_stages", "affected_downstream",
         "affected_outputs", "impact_depth"}
    """
    assumption = onto[assumption_name]
    if assumption is None:
        return {"error": _msg("individual_missing", name=assumption_name)}

    attached = [s for s in _as_list(getattr(assumption, attached_property, []))
                if hasattr(s, "name")]
    attached_names = [s.name for s in attached]
    if not attached_names:
        return {"assumption": assumption_name, "attached_stages": [],
                "affected_downstream": [], "affected_outputs": [],
                "impact_depth": 0}

    downstream = set()
    for stage_name in attached_names:
        r = run_sparql_check(world, "downstream", onto=onto, start=stage_name,
                             order_property=stage_order_property)
        downstream |= set(r["results"])

    affected_outputs = []
    for stage in attached + [onto[n] for n in sorted(downstream) if onto[n]]:
        for prop in stage.get_properties():
            if any(k in prop.python_name.lower() for k in OUTPUT_KEYWORDS):
                affected_outputs.extend(
                    v.name for v in _as_list(getattr(stage, prop.python_name, []))
                    if hasattr(v, "name"))

    return {"assumption": assumption_name,
            "attached_stages": attached_names,
            "affected_downstream": sorted(downstream),
            "affected_outputs": affected_outputs,
            "impact_depth": len(downstream)}


def check_pipeline_trace(world, onto, stage_chain):
    """
    Check that each stage class links to the next one.
    stage_chain: [{"class": "A", "link_to_next": "prop"}, {"class": "B"}]

    Returns:
        {"stages": [...], "breaks": [...], "complete": bool}
    """
    stages_info, breaks = [], []
    for i, stage in enumerate(stage_chain):
        cls = onto[stage["class"]]
        if cls is None:
            stages_info.append({"class": stage["class"], "count": 0,
                                "status": "class_not_found"})
            breaks.append({"stage": i, "class": stage["class"],
                           "reason": "class_not_found"})
            continue
        stages_info.append({"class": stage["class"],
                            "count": len(list(cls.instances()))})
        if "link_to_next" in stage and i < len(stage_chain) - 1:
            prop_name = stage["link_to_next"]
            r = run_sparql_check(world, "stage_unlinked", onto=onto,
                                 stage_class=stage["class"],
                                 link_property=prop_name)
            if r["results"]:
                breaks.append({"stage": i, "class": stage["class"],
                               "property": prop_name,
                               "target": stage_chain[i + 1]["class"],
                               "unlinked_individuals": list(r["results"])})
    return {"stages": stages_info, "breaks": breaks, "complete": not breaks}


# ============================================================
# 8. Python-only checks (3)
# ============================================================

def check_cross_mapping(onto, subject_classes: dict, property_name: str,
                        target_class_set: set) -> list:
    """
    Check that each subject type references only allowed target types.

    Args:
        subject_classes: {"SubjectClass": {"allowed": {"TargetClass", ...}}}
        property_name: object property to check
        target_class_set: target class names that the rule covers

    Returns:
        [{"subject", "subject_type", "target", "target_type", "allowed"}]
    """
    violations = []
    for ind in onto.individuals():
        subject_types = [c.name for c in ind.is_a
                         if hasattr(c, "name") and c.name in subject_classes]
        if not subject_types:
            continue
        targets = _as_list(getattr(ind, property_name, []))
        for st in subject_types:
            allowed = subject_classes[st]["allowed"]
            for t in targets:
                for tc in [c.name for c in getattr(t, "is_a", [])
                           if hasattr(c, "name") and c.name in target_class_set]:
                    if tc not in allowed:
                        violations.append({"subject": ind.name, "subject_type": st,
                                           "target": t.name, "target_type": tc,
                                           "allowed": sorted(allowed)})
    return violations


def check_mapping_chain(world, onto, chain_rules: list) -> dict:
    """
    Check a multi-step mapping (A -> B -> C ...) step by step.
    A step with "allowed" and "target_types" checks allowed combinations;
    a step without them checks only that links exist.

    Returns:
        {"stages": [{"stage", "from_class", "to_class", "violations"}],
         "total_violations": int, "first_break_stage": int or None}
    """
    stages, total, first_break = [], 0, None
    for i, rule in enumerate(chain_rules):
        if "allowed" in rule and "target_types" in rule:
            violations = check_cross_mapping(onto, rule["allowed"],
                                             rule["link_property"],
                                             rule["target_types"])
        else:
            violations = check_provenance(world, onto, [rule["from_class"]],
                                          rule["link_property"])
        if violations and first_break is None:
            first_break = i
        total += len(violations)
        stages.append({"stage": i, "from_class": rule["from_class"],
                       "to_class": rule["to_class"], "violations": violations})
    return {"stages": stages, "total_violations": total,
            "first_break_stage": first_break}


def check_conditional_branch(onto, condition_class: str,
                             condition_property: str, branch_rules: dict,
                             stage_property: str = "has_stage") -> list:
    """
    Compare the stages each individual has with rules per condition value.
    branch_rules: {"value": {"required": [StageClass], "excluded": [StageClass]}}

    Returns:
        [{"individual", "condition", "violation_type", "stage"}]
    """
    cond_cls = onto[condition_class]
    if cond_cls is None:
        return [{"error": _msg("class_missing", name=condition_class)}]
    violations = []
    for ind in cond_cls.instances():
        values = _as_list(getattr(ind, condition_property, None))
        if not values:
            continue
        cond = str(values[0])
        if cond not in branch_rules:
            continue
        rules = branch_rules[cond]
        stage_classes = {c.name for s in _as_list(getattr(ind, stage_property, []))
                         for c in getattr(s, "is_a", []) if hasattr(c, "name")}
        for req in rules.get("required", []):
            if req not in stage_classes:
                violations.append({"individual": ind.name, "condition": cond,
                                   "violation_type": "missing_required",
                                   "stage": req})
        for exc in rules.get("excluded", []):
            if exc in stage_classes:
                violations.append({"individual": ind.name, "condition": cond,
                                   "violation_type": "included_excluded",
                                   "stage": exc})
    return violations


# ============================================================
# 9. Presets
# ============================================================

def run_preset_cross_factor(world, onto, rules, factor_property, factor_types,
                            source_property=None, source_classes=None,
                            cardinality_property=None, expected_count=None):
    """Allowed factor combinations + source links + link counts."""
    result = {"mapping": check_cross_mapping(onto, rules, factor_property,
                                             factor_types)}
    result["provenance"] = (check_provenance(world, onto, source_classes,
                                             source_property)
                            if source_property and source_classes else [])
    cardinality = []
    if cardinality_property and expected_count is not None:
        for cls_name in rules:
            cardinality.extend(check_cardinality(world, onto, cls_name,
                                                 cardinality_property,
                                                 expected_count))
    result["cardinality"] = cardinality
    return result


def run_preset_multi_axis(world, onto, axis_classes, result_property,
                          comprehensive_class, intake_property,
                          shared_ref_property=None):
    """Axis results reaching the overall result + shared references."""
    coverage = []
    for axis_cls in axis_classes:
        coverage.extend(check_coverage(world, onto, axis_cls,
                                       comprehensive_class, intake_property))
    shared = (check_shared_reference(world, onto, axis_classes,
                                     shared_ref_property)
              if shared_ref_property and len(axis_classes) >= 2 else None)
    return {"coverage": coverage, "shared_reference": shared}


def run_preset_regulated_procedure(world, onto, stage_chain,
                                   output_property=None, mandatory_map=None):
    """Stage order + mandatory outputs for a fixed procedure."""
    mandatory = []
    if output_property and mandatory_map:
        for stage_cls, required in mandatory_map.items():
            mandatory.extend(check_mandatory_outputs(world, onto, stage_cls,
                                                     output_property, required))
    return {"pipeline": check_pipeline_trace(world, onto, stage_chain),
            "mandatory_outputs": mandatory}


def run_preset_causal(world, onto, effect_name=None, cause_property="caused_by"):
    """Forward causal paths + backward trace + unsupported assumptions."""
    return {"forward_chains": check_causal_chain(world, onto),
            "unsupported_assumptions": check_unsupported_assumptions(world, onto),
            "reverse_chain": (check_reverse_chain(world, onto, effect_name,
                                                  cause_property)
                              if effect_name else None)}


def run_preset_logic_model(world, onto, stage_chain=None, objective_class=None,
                           activity_class=None, obj_to_act_property=None,
                           indicator_property=None, indicator_classes=None):
    """Stage links + activity and objective links + assumptions + indicators."""
    return {
        "pipeline": (check_pipeline_trace(world, onto, stage_chain)
                     if stage_chain else None),
        "bidirectional": (check_bidirectional_coverage(
            world, onto, activity_class, objective_class, obj_to_act_property)
            if objective_class and activity_class and obj_to_act_property
            else None),
        "assumptions": check_unsupported_assumptions(world, onto),
        "indicator_coverage": (check_provenance(world, onto, indicator_classes,
                                                indicator_property)
                               if indicator_property and indicator_classes
                               else None),
    }


def run_preset_mapping_chain(world, onto, chain_rules, bidirectional_pairs=None):
    """Multi-step mapping + links in both directions per class pair."""
    bidi = [{"pair": f"{a}-{b}",
             "result": check_bidirectional_coverage(world, onto, a, b, prop)}
            for a, b, prop in (bidirectional_pairs or [])]
    return {"chain": check_mapping_chain(world, onto, chain_rules),
            "bidirectional": bidi}


def run_preset_decision_tree(world, onto, condition_class, condition_property,
                             branch_rules, stage_property="has_stage",
                             prerequisite_property=None):
    """Conditional branches + prerequisites of required options."""
    result = {"branch_violations": check_conditional_branch(
        onto, condition_class, condition_property, branch_rules, stage_property)}
    if prerequisite_property:
        required = set()
        for rules in branch_rules.values():
            required.update(rules.get("required", []))
        result["prerequisite_gaps"] = check_provenance(
            world, onto, sorted(required), prerequisite_property)
    else:
        result["prerequisite_gaps"] = []
    return result


# ============================================================
# 10. Reasoner results
# ============================================================

def snapshot_classifications(onto) -> dict:
    """Return {individual: [named classes]} before reasoning."""
    return {ind.name: sorted(c.name for c in ind.is_a if hasattr(c, "name"))
            for ind in onto.individuals()}


def check_inferred_reclassification(onto, snapshot_before: dict) -> list:
    """
    Compare class membership after reasoning with a snapshot.

    Returns:
        [{"individual", "before", "after", "added", "removed"}]
    """
    changes = []
    for ind in onto.individuals():
        after = sorted(c.name for c in ind.is_a if hasattr(c, "name"))
        before = snapshot_before.get(ind.name, [])
        if before != after:
            changes.append({"individual": ind.name, "before": before,
                            "after": after,
                            "added": [c for c in after if c not in before],
                            "removed": [c for c in before if c not in after]})
    return changes


def run_hermit_analysis(world, onto, timeout_sec: int = REASONER_TIMEOUT_SEC,
                        reasoner: str = "hermit",
                        infer_property_values: bool = False,
                        infer_data_property_values: bool = False) -> dict:
    """
    Snapshot, run the reasoner, and report reclassified individuals.

    Returns:
        {"hermit_result": dict, "reclassifications": list,
         "reclassification_count": int}
    """
    before = snapshot_classifications(onto)
    hr = run_hermit_reasoner(world, onto, timeout_sec, reasoner=reasoner,
                             infer_property_values=infer_property_values,
                             infer_data_property_values=infer_data_property_values)
    reclass = check_inferred_reclassification(onto, before) if hr["success"] else []
    return {"hermit_result": hr, "reclassifications": reclass,
            "reclassification_count": len(reclass)}


# ============================================================
# 11. Markdown and Mermaid export
# ============================================================

def export_tbox_markdown(onto) -> str:
    """TBox (classes and properties) as Markdown tables."""
    none = _msg("unspecified")
    lines = [_msg("tbox_title"), "", _msg("tbox_classes"), "",
             _msg("tbox_class_header"), "|---|---|---|---|"]
    hierarchy = get_class_hierarchy(onto)
    for cls_name, info in sorted(hierarchy.items()):
        desc = _first_text(getattr(onto[cls_name], "comment", None))
        lines.append(f"| {cls_name} | {', '.join(info['parents']) or 'Thing'} "
                     f"| {', '.join(info['children']) or '-'} | {desc or '-'} |")
    lines += ["", _msg("tbox_props"), "", _msg("tbox_prop_header"),
              "|---|---|---|---|"]
    for prop in onto.properties():
        if isinstance(prop, ObjectPropertyClass):
            ptype = "ObjectProperty"
        elif isinstance(prop, DataPropertyClass):
            ptype = "DataProperty"
        else:
            ptype = "AnnotationProperty"
        domain = ", ".join(_type_name(d) for d in (prop.domain or [])) or none
        rng = ", ".join(_type_name(r) for r in (prop.range or [])) or none
        lines.append(f"| {prop.python_name} | {ptype} | {domain} | {rng} |")
    return "\n".join(lines) + "\n"


def export_abox_markdown(onto) -> str:
    """ABox (individuals and their values) as one Markdown table per class."""
    lines = [_msg("abox_title"), ""]
    by_class = {}
    for ind in get_all_individuals(onto):
        for cls_name in ind["classes"]:
            by_class.setdefault(cls_name, []).append(ind)
    for cls_name, inds in sorted(by_class.items()):
        lines += [f"## {cls_name}", "", _msg("abox_header"), "|---|---|---|"]
        for ind in inds:
            if not ind["properties"]:
                lines.append(f"| {ind['name']} | - | - |")
            for key, val in ind["properties"].items():
                text = ", ".join(val) if isinstance(val, list) else val
                lines.append(f"| {ind['name']} | {key} | {text} |")
        lines.append("")
    return "\n".join(lines)


def _mermaid_id(name):
    return name.replace("-", "_").replace(" ", "_")


def export_mermaid_class_diagram(onto) -> str:
    """Class hierarchy and properties as a Mermaid classDiagram (no code fence)."""
    lines = ["classDiagram"]
    for cls_name, info in get_class_hierarchy(onto).items():
        if info["parents"]:
            lines.extend(f"    {p} <|-- {cls_name}" for p in info["parents"])
        else:
            lines.append(f"    class {cls_name}")
    for prop in onto.properties():
        domains = [d for d in (prop.domain or []) if hasattr(d, "name")]
        if not domains:
            continue
        d = domains[0].name
        if isinstance(prop, ObjectPropertyClass):
            ranges = [r for r in (prop.range or []) if hasattr(r, "name")]
            if ranges:
                lines.append(f"    {d} --> {ranges[0].name} : {prop.python_name}")
        elif isinstance(prop, DataPropertyClass):
            rtype = _type_name(prop.range[0]) if prop.range else "Literal"
            lines.append(f"    {d} : +{rtype} {prop.python_name}")
    return "\n".join(lines)


def export_mermaid_instance_graph(onto, max_nodes: int = 0) -> str:
    """Individuals and links as a Mermaid graph. max_nodes=0 shows all."""
    inds = list(onto.individuals())
    if max_nodes > 0:
        inds = inds[:max_nodes]
    lines, seen_edges = ["graph LR"], set()
    for ind in inds:
        ind_id = _mermaid_id(ind.name)
        cls_names = "/".join(c.name for c in ind.is_a if hasattr(c, "name"))
        lines.append(f'    {ind_id}["{ind.name}<br/>{cls_names}"]')
        for prop in ind.get_properties():
            for v in _as_list(getattr(ind, prop.python_name, [])):
                if hasattr(v, "name"):
                    edge = (ind_id, prop.python_name, _mermaid_id(v.name))
                    if edge not in seen_edges:
                        seen_edges.add(edge)
                        lines.append(f"    {edge[0]} -->|{edge[1]}| {edge[2]}")
    return "\n".join(lines)


def export_mermaid_aggregated_graph(onto) -> str:
    """Class-level graph with individual counts and link counts."""
    class_edges, class_counts = {}, {}
    for ind in onto.individuals():
        src_classes = [c.name for c in ind.is_a if hasattr(c, "name")]
        for c in src_classes:
            class_counts[c] = class_counts.get(c, 0) + 1
        if not src_classes:
            continue
        for prop in ind.get_properties():
            for v in _as_list(getattr(ind, prop.python_name, [])):
                tgt = [c.name for c in getattr(v, "is_a", []) if hasattr(c, "name")]
                if hasattr(v, "name") and tgt:
                    key = (src_classes[0], prop.python_name, tgt[0])
                    class_edges[key] = class_edges.get(key, 0) + 1
    lines = ["graph LR"]
    for cls_name, count in sorted(class_counts.items()):
        lines.append(f'    {_mermaid_id(cls_name)}["{cls_name}<br/>({count})"]')
    for (src, prop, tgt), count in sorted(class_edges.items()):
        lines.append(f"    {_mermaid_id(src)} -->|{prop} x{count}| {_mermaid_id(tgt)}")
    return "\n".join(lines)


def export_summary_statistics(onto) -> str:
    """Summary statistics in Markdown for large ontologies."""
    inds = list(onto.individuals())
    class_counts, prop_counts, connected = {}, {}, set()
    for ind in inds:
        for c in ind.is_a:
            if hasattr(c, "name"):
                class_counts[c.name] = class_counts.get(c.name, 0) + 1
        for prop in ind.get_properties():
            obj_vals = [v for v in _as_list(getattr(ind, prop.python_name, []))
                        if hasattr(v, "name")]
            if obj_vals:
                prop_counts[prop.python_name] = (prop_counts.get(prop.python_name, 0)
                                                 + len(obj_vals))
                connected.add(ind.name)

    lines = [_msg("summary_title"), "",
             _msg("summary_classes", n=len(list(onto.classes()))),
             _msg("summary_individuals", n=len(inds)),
             _msg("summary_isolated", n=len(inds) - len(connected)), "",
             _msg("summary_class_dist"), "", _msg("summary_class_header"),
             "|---|---|"]
    ranked = sorted(class_counts.items(), key=lambda x: -x[1])
    lines.extend(f"| {c} | {n} |" for c, n in ranked[:SUMMARY_TOP_CLASSES])
    if len(ranked) > SUMMARY_TOP_CLASSES:
        lines.append(_msg("summary_more", n=len(ranked) - SUMMARY_TOP_CLASSES))
    if prop_counts:
        lines += ["", _msg("summary_prop_dist"), "", _msg("summary_prop_header"),
                  "|---|---|"]
        lines.extend(f"| {p} | {n} |"
                     for p, n in sorted(prop_counts.items(), key=lambda x: -x[1]))
    return "\n".join(lines) + "\n"


def export_smart_visualization(onto, force_mode: str = None) -> dict:
    """
    Pick the instance view by size: full graph up to VIZ_FULL_MAX
    individuals, class-level graph up to VIZ_AGGREGATED_MAX, summary above.
    force_mode accepts "full", "aggregated" or "summary".

    Returns:
        {"mode", "individual_count", "class_diagram", "instance_view", "summary"}
    """
    count = len(list(onto.individuals()))
    if force_mode == "full" or (force_mode is None and count <= VIZ_FULL_MAX):
        mode, view, summary = "full", export_mermaid_instance_graph(onto), None
    elif force_mode == "aggregated" or (force_mode is None
                                        and count <= VIZ_AGGREGATED_MAX):
        mode = "aggregated"
        view, summary = export_mermaid_aggregated_graph(onto), export_summary_statistics(onto)
    else:
        mode = "summary"
        view, summary = export_mermaid_aggregated_graph(onto), export_summary_statistics(onto)
    return {"mode": mode, "individual_count": count,
            "class_diagram": export_mermaid_class_diagram(onto),
            "instance_view": view, "summary": summary}


# ============================================================
# 12. Routing and full run
# ============================================================

def auto_route_advanced_checks(onto):
    """
    Scan property and class names to list checks that apply.
    Matching uses name keywords, so review the list before running it.

    Returns:
        {"required": [{"func", "reason"}], "recommended": [{"func", "reason"}]}
    """
    required, recommended, seen = [], [], set()

    def add(bucket, func, reason):
        if func not in seen:
            bucket.append({"func": func, "reason": reason})
            seen.add(func)

    class_names = {c.name for c in onto.classes()}
    prop_names, prop_domains, prop_ranges = set(), {}, {}
    has_transitive = False
    for prop in onto.properties():
        name = prop.python_name
        prop_names.add(name)
        if isinstance(prop, ObjectPropertyClass):
            prop_domains[name] = [c.name for c in (prop.domain or []) if hasattr(c, "name")]
            prop_ranges[name] = [c.name for c in (prop.range or []) if hasattr(c, "name")]
        if TransitiveProperty in getattr(prop, "is_a", []):
            has_transitive = True

    has_order = False
    for name in sorted(prop_names):
        lower = name.lower()
        if lower in ORDER_KEYWORDS or has_transitive:
            add(required, "pipeline_trace", _msg("route_order", p=name))
            has_order = True
        if any(k in lower for k in EVIDENCE_KEYWORDS):
            add(required, "provenance", _msg("route_evidence", p=name))
        if any(k in lower for k in CAUSAL_KEYWORDS):
            add(required, "causal_chain", _msg("route_causal", p=name))
            add(required, "reverse_chain", _msg("route_causal", p=name))

    assumption_like = sorted(n for n in class_names
                             if any(k in n.lower() for k in ASSUMPTION_KEYWORDS))
    if assumption_like:
        add(required, "unsupported_assumptions",
            _msg("route_assumption", c=assumption_like[0]))
        if has_order:
            add(recommended, "assumption_impact", _msg("route_assumption_order"))

    pairs = {}
    for name, domains in prop_domains.items():
        for d in domains:
            for r in prop_ranges.get(name, []):
                pairs.setdefault((d, r), []).append(name)
    for (d, r), props in sorted(pairs.items()):
        if len(props) >= 2:
            add(required, "bidirectional_coverage",
                _msg("route_bidirectional", d=d, r=r, n=len(props)))

    for name in sorted(prop_domains):
        if prop_domains[name]:
            add(recommended, "cardinality", _msg("route_cardinality", p=name))
            break

    referrers = {}
    for name, ranges in prop_ranges.items():
        for r in ranges:
            referrers.setdefault(r, []).append(name)
    for r, props in sorted(referrers.items()):
        if len(props) >= 2:
            add(recommended, "shared_reference", _msg("route_shared", r=r, n=len(props)))
            break

    mandatory_like = sorted(n for n in class_names
                            if any(k in n.lower() for k in MANDATORY_KEYWORDS))
    if mandatory_like and has_order:
        add(recommended, "mandatory_outputs",
            _msg("route_mandatory", c=mandatory_like[0]))

    if "provenance_note" in prop_names:
        add(required, "provenance", _msg("route_provenance_note"))

    parents = [c.name for c in onto.classes() if len(list(c.subclasses())) >= 2]
    if parents:
        add(recommended, "mece", _msg("route_mece", k=len(parents)))

    return {"required": required, "recommended": recommended}


def run_full_analysis(world, onto, use_hermit=False, run_mece=False,
                      reasoner: str = "hermit",
                      infer_property_values: bool = False,
                      infer_data_property_values: bool = False):
    """
    Run the default analysis bundle.

    Args:
        use_hermit: run the OWL reasoner after the Python checks
        run_mece: run check_mece on every class that has subclasses

    Returns:
        {"class_hierarchy", "individuals", "tbox_md", "abox_md",
         "mermaid_class", "visualization", "mece_checks", "conflicts",
         "process_check", "causal_chains", "unsupported_assumptions",
         "provenance_check", "advanced_routing", "hermit_analysis"}
    """
    result = {
        "class_hierarchy": get_class_hierarchy(onto),
        "individuals": get_all_individuals(onto),
        "tbox_md": export_tbox_markdown(onto),
        "abox_md": export_abox_markdown(onto),
        "mermaid_class": export_mermaid_class_diagram(onto),
        "visualization": export_smart_visualization(onto),
    }
    result["mece_checks"] = ({c.name: check_mece(world, onto, c.name)
                              for c in onto.classes() if list(c.subclasses())}
                             if run_mece else None)
    result["conflicts"] = check_constraint_conflicts(world, onto)
    result["process_check"] = check_process_completeness(world, onto)
    result["causal_chains"] = check_causal_chain(world, onto)
    result["unsupported_assumptions"] = check_unsupported_assumptions(world, onto)

    # Judgment records: individuals in classes where some members carry a
    # provenance_note but they do not.
    if onto["provenance_note"] is not None:
        noted_classes = []
        for ind in onto.individuals():
            if _as_list(getattr(ind, "provenance_note", None)):
                noted_classes.extend(c.name for c in ind.is_a
                                     if hasattr(c, "name")
                                     and c.name not in noted_classes)
        result["provenance_check"] = (check_provenance(world, onto, noted_classes,
                                                       "provenance_note")
                                      if noted_classes else [])
    else:
        result["provenance_check"] = None

    result["advanced_routing"] = auto_route_advanced_checks(onto)
    result["hermit_analysis"] = (run_hermit_analysis(
        world, onto, reasoner=reasoner,
        infer_property_values=infer_property_values,
        infer_data_property_values=infer_data_property_values)
        if use_hermit else None)
    return result


if __name__ == "__main__":
    world, onto = create_world()
    build_class(onto, "Problem")
    build_class(onto, "Cause")
    build_object_property(onto, "caused_by", "Problem", "Cause")
    cause = create_individual(onto, "Cause", "cause_1")
    create_individual(onto, "Problem", "problem_1", caused_by=[cause])
    summary = run_full_analysis(world, onto)
    print(json.dumps({k: v for k, v in summary.items()
                      if k not in ("tbox_md", "abox_md", "mermaid_class",
                                   "visualization")},
                     ensure_ascii=False, indent=2, default=str))
    print(_msg("selftest_ok"))
