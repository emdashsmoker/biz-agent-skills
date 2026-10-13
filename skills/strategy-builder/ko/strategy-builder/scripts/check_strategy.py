#!/usr/bin/env python3
"""Check a strategy-builder state file against the skill's step rules.

The state file is plain JSON that records every element of the strategy work
(facts, implications, issues, SWOT or gap data, vision, strategies, tasks,
KPIs) and the links between them. Checks are cumulative: --step N runs every
check that belongs to steps 1..N, so a later edit that breaks an earlier
rule is still caught.

Usage:
    python check_strategy.py --schema --lang ko
    python check_strategy.py --template > strategy_state.json
    python check_strategy.py strategy_state.json --step 6 --lang ko
    python check_strategy.py strategy_state.json --step 10 --chart

Exit codes: 0 no violation, 1 violation found, 2 unreadable input.
Requires only the Python standard library (3.8+).
"""
import argparse
import json
import re
import sys

# ---------------------------------------------------------------------------
# Allowed values. Kept in one place so the SKILL.md tables and the checks
# cannot drift apart.
# ---------------------------------------------------------------------------
ANALYSIS_TOOLS = ("swot", "gap")
GAP_MODES = ("split", "integrated")
SWOT_MODES = ("fixed", "flexible", "issue_linked")
FLEXIBLE_OPTIONS = ("as_is", "representative", "cross")
GOAL_PATTERNS = ("integrated", "dual", "qualitative", "quantitative")
KPI_SCOPES = ("all", "lower", "strategy", "none")
KPI_TRACKS = ("BSC", "GOV", "RND", "AUTO", "QUAL")
KPI_TYPES = ("Input", "Activity", "Output", "Outcome", "Impact")
FACT_SOURCES = ("macro", "micro", "internal", "benchmark")
IMPLICATION_SOURCES = FACT_SOURCES + ("asis",)
FACTOR_TYPES = ("S", "W", "O", "T")
QUADRANT_TYPES = {"SO": ("S", "O"), "ST": ("S", "T"),
                  "WO": ("W", "O"), "WT": ("W", "T")}
# SWOT factor type -> implication sources it may draw on.
# Internal findings describe the organisation (S, W); environment findings
# describe the outside (O, T); benchmark findings may inform any type.
FACTOR_ALLOWED_SOURCES = {
    "S": ("internal", "benchmark"),
    "W": ("internal", "benchmark"),
    "O": ("macro", "micro", "benchmark"),
    "T": ("macro", "micro", "benchmark"),
}
# Goal pattern -> (qualitative goal required, quantitative goal required)
GOAL_RULES = {
    "integrated": (False, False),
    "dual": (True, True),
    "qualitative": (True, False),
    "quantitative": (False, True),
}
# KPI scope -> element levels that carry KPIs
SCOPE_LEVELS = {
    "all": ("strategy", "task", "impl"),
    "strategy": ("strategy",),
    "lower": ("impl",),
    "none": (),
}
LAST_STEP = 10
MIN_GAP_ISSUES_RECOMMENDED = 3

STRATEGY_ID = re.compile(r"^[1-9][0-9]*$")
TASK_ID = re.compile(r"^([1-9][0-9]*)-[1-9][0-9]*$")
IMPL_ID = re.compile(r"^([1-9][0-9]*-[1-9][0-9]*)-[1-9][0-9]*$")
KPI_ID = re.compile(r"^([1-9][0-9]*(?:-[1-9][0-9]*){0,2})-KPI-[1-9][0-9]*$")

# Setting -> step that owns it (reported once, under that step).
SETTING_STEP = {"analysis_tool": 5, "gap_mode": 5, "swot_mode": 6,
                "fixed_followup": 6, "flexible_option": 6, "goal_pattern": 8,
                "kpi_scope": 10, "kpi_track": 10}

# Collection key -> step that owns it (structure checks run from that step).
COLLECTION_STEP = {
    "upper_alignments": 1, "beneficiaries": 1, "issues": 1,
    "facts": 5, "implications": 5,
    "swot_factors": 6, "swot_candidates": 6, "gaps": 6, "strategies": 6,
    "core_values": 7,
    "strategic_tasks": 8,
    "implementation_tasks": 9,
    "kpis": 10,
}

TEMPLATE = {
    "settings": {
        "analysis_tool": None, "gap_mode": None, "swot_mode": None,
        "fixed_followup": None, "flexible_option": None,
        "goal_pattern": None, "implementation_tasks": None,
        "kpi_scope": None, "kpi_track": None, "rnd_include_impact": False,
    },
    "hypothesis": {"subject": "", "space": "", "time": ""},
    "no_upper_alignment": False,
    "upper_alignments": [],
    "beneficiaries": [],
    "issues": [],
    "facts": [],
    "implications": [],
    "swot_factors": [],
    "swot_candidates": [],
    "gaps": [],
    "strategies": [],
    "vision": {"text": "", "upper_alignments": []},
    "mission": {"text": "", "beneficiaries": []},
    "core_values": [],
    "strategic_tasks": [],
    "implementation_tasks": [],
    "kpis": [],
}

# ---------------------------------------------------------------------------
# Messages
# ---------------------------------------------------------------------------
MESSAGES = {
    "not_list": ("{key} 항목은 목록이어야 함",
                 "{key} must be a list"),
    "not_object": ("{key} 항목은 객체여야 함",
                   "{key} must be an object"),
    "bad_entry": ("{key}의 {pos}번째 항목에 id가 없거나 객체가 아님",
                  "{key} entry #{pos} has no id or is not an object"),
    "duplicate_id": ("{key}에 중복 id {id}",
                     "duplicate id {id} in {key}"),
    "empty_text": ("{key} {id}의 {field} 미입력",
                   "{key} {id} has empty {field}"),
    "bad_field": ("{key} {id}의 {field}는 목록이어야 함",
                  "{field} of {key} {id} must be a list"),
    "bad_ref": ("{key} {id}가 존재하지 않는 {target} {ref}를 참조",
                "{key} {id} refers to unknown {target} {ref}"),
    "bad_value": ("{key} {id}의 {field} 값 {value}는 허용되지 않음 (허용: {allowed})",
                  "{key} {id}: {field} value {value} is not allowed (allowed: {allowed})"),
    "bad_setting": ("settings.{field} 값 {value}는 허용되지 않음 (허용: {allowed})",
                    "settings.{field} value {value} is not allowed (allowed: {allowed})"),
    "missing_setting": ("settings.{field} 미설정 (허용: {allowed})",
                        "settings.{field} is not set (allowed: {allowed})"),
    "hypothesis_missing": ("가설의 {field} 미입력",
                           "hypothesis.{field} is empty"),
    "no_beneficiary": ("수요자(beneficiaries) 0건",
                       "no beneficiary recorded"),
    "upper_alignment_missing": ("상위 정렬 미입력: 목록을 채우거나 no_upper_alignment를 true로 기록",
                                "upper alignment missing: fill the list or set no_upper_alignment to true"),
    "upper_alignment_conflict": ("no_upper_alignment가 true인데 상위 정렬 목록이 존재",
                                 "no_upper_alignment is true but upper_alignments is not empty"),
    "no_issue": ("문제이슈 0건",
                 "no problem issue recorded"),
    "fact_skipped_step": ("통합 모드는 2-3단계를 생략하므로 팩트 출처는 benchmark만 허용: {id}({source})",
                          "integrated mode skips steps 2-3, so facts may only come from benchmark: {id} ({source})"),
    "asis_not_allowed": ("asis 출처 시사점은 갭분석 통합 모드에서만 허용: {id}",
                         "asis implications are allowed only in integrated gap mode: {id}"),
    "implication_skipped_step": ("통합 모드 시사점 출처는 asis 또는 benchmark만 허용: {id}({source})",
                                 "in integrated mode implications may only be asis or benchmark: {id} ({source})"),
    "implication_no_fact": ("팩트 연결 없는 시사점: {id}",
                            "implication without any fact: {id}"),
    "mixed_source": ("시사점 {id}({source})가 출처가 다른 팩트 {fact}({fact_source})를 참조",
                     "implication {id} ({source}) cites fact {fact} from another source ({fact_source})"),
    "no_implication": ("시사점 0건",
                       "no implication recorded"),
    "fact_unused": ("시사점에 반영되지 않은 팩트: {id}",
                    "fact not used by any implication: {id}"),
    "issue_no_implication": ("시사점 귀납 없는 문제이슈: {id}",
                             "problem issue without supporting implication: {id}"),
    "implication_no_issue": ("문제이슈에 귀납되지 않은 시사점: {id}",
                             "implication not grouped into any problem issue: {id}"),
    "no_strategy": ("전략 0건",
                    "no strategy recorded"),
    "bad_strategy_id": ("전략 id {id}는 1 이상의 정수여야 함",
                        "strategy id {id} must be a positive integer"),
    "factor_type_missing": ("{type} 요인 0건",
                            "no {type} factor recorded"),
    "factor_no_implication": ("시사점 근거 없는 SWOT 요인: {id}",
                              "SWOT factor without implication: {id}"),
    "factor_source": ("요인 {id}({type})는 {source} 출처 시사점 {impl} 사용 불가",
                      "factor {id} ({type}) may not use {source} implication {impl}"),
    "candidate_wrong_factor": ("후보 {id}({quadrant})가 허용되지 않는 요인 {factor}({type}) 사용",
                               "candidate {id} ({quadrant}) uses factor {factor} of type {type}"),
    "candidate_missing_type": ("후보 {id}({quadrant})에 {type} 요인 없음",
                               "candidate {id} ({quadrant}) has no {type} factor"),
    "quadrant_factor_unused": ("{quadrant} 후보 전체에서 미사용 요인: {factor}",
                               "factor not used by any {quadrant} candidate: {factor}"),
    "fixed_candidate_count": ("고정형은 {quadrant} 후보가 1개여야 함 (현재 {count}개)",
                              "fixed mode needs exactly one {quadrant} candidate (found {count})"),
    "strategy_no_candidate": ("SWOT 후보 연결 없는 전략: {id}",
                              "strategy without SWOT candidate: {id}"),
    "fixed_strategy_count": ("고정형은 전략이 4개여야 함 (현재 {count}개)",
                             "fixed mode needs exactly 4 strategies (found {count})"),
    "one_candidate_required": ("전략 {id}는 후보 1개만 연결해야 함 (현재 {count}개)",
                               "strategy {id} must link exactly one candidate (found {count})"),
    "quadrant_mapping": ("전략 4개가 SO, ST, WO, WT를 하나씩 담당해야 함",
                         "the 4 strategies must cover SO, ST, WO, WT one each"),
    "as_is_mapping": ("후보 {id}가 전략 {count}개에 연결됨 (후보 그대로 방식은 1개)",
                      "candidate {id} is linked to {count} strategies (as_is needs exactly 1)"),
    "representative_count": ("구분별 대표 방식은 전략이 4개여야 함 (현재 {count}개)",
                             "representative option needs exactly 4 strategies (found {count})"),
    "representative_mixed": ("전략 {id}의 후보가 여러 구분에 걸쳐 있음",
                             "strategy {id} mixes candidates from different quadrants"),
    "representative_incomplete": ("전략 {id}가 {quadrant} 후보 {missing}를 포함하지 않음",
                                  "strategy {id} misses {quadrant} candidate {missing}"),
    "cross_factor_unused": ("최종 전략 집합에 반영되지 않은 요인: {factor}",
                            "factor not reflected in the final strategy set: {factor}"),
    "issue_linked_count": ("문제이슈연결형은 전략 수({strategies})와 문제이슈 수({issues})가 같아야 함",
                           "issue-linked mode needs as many strategies ({strategies}) as issues ({issues})"),
    "issue_linked_one_issue": ("전략 {id}는 문제이슈 1개만 해결해야 함 (현재 {count}개)",
                               "strategy {id} must resolve exactly one issue (found {count})"),
    "issue_linked_one_strategy": ("문제이슈 {id}는 전략 1개와만 연결되어야 함 (현재 {count}개)",
                                  "issue {id} must be resolved by exactly one strategy (found {count})"),
    "gap_missing_state": ("갭 {id}의 {field} 미입력",
                          "gap {id} has empty {field}"),
    "issue_no_gap": ("갭 없는 문제이슈: {id}",
                     "problem issue without gap: {id}"),
    "strategy_no_gap": ("갭 연결 없는 전략: {id}",
                        "strategy without gap: {id}"),
    "gap_no_strategy": ("전략 연결 없는 갭: {id}",
                        "gap not resolved by any strategy: {id}"),
    "note_gap_issue_count": ("(권고) 갭분석 문제이슈 {count}건, 3건 이상 권고",
                             "(recommendation) gap analysis has {count} issue(s); 3 or more recommended"),
    "no_vision": ("비전 문장 미입력",
                  "vision text is empty"),
    "no_mission": ("미션 문장 미입력",
                   "mission text is empty"),
    "vision_no_upper": ("비전에 상위 정렬 연결 없음",
                        "vision is not linked to any upper alignment"),
    "mission_no_beneficiary": ("미션에 수요자 연결 없음",
                               "mission is not linked to any beneficiary"),
    "cv_no_strategy": ("핵심가치 {id}에 전략 미연결",
                       "core value {id} has no strategy"),
    "strategy_no_cv": ("핵심가치 없는 전략: {id}",
                       "strategy without core value: {id}"),
    "strategy_multi_cv": ("전략 {id}에 핵심가치 {count}개 연결 (1개만 허용)",
                          "strategy {id} has {count} core values (exactly 1 allowed)"),
    "strategy_no_issue": ("해결 문제이슈 없는 전략: {id}",
                          "strategy resolves no issue: {id}"),
    "issue_no_strategy": ("전략 대응 없는 문제이슈: {id}",
                          "problem issue not resolved by any strategy: {id}"),
    "gap_issue_mismatch": ("전략 {id}가 갭 {gap}을 해결하지만 그 문제이슈 {issue}가 해결 목록에 없음",
                           "strategy {id} resolves gap {gap} but not its issue {issue}"),
    "goal_required": ("{pattern} 패턴: 전략 {id}의 {field} 필요",
                      "{pattern} pattern: strategy {id} needs {field}"),
    "goal_forbidden": ("{pattern} 패턴: 전략 {id}의 {field}는 비워야 함",
                       "{pattern} pattern: strategy {id} must leave {field} empty"),
    "quant_goal_single": ("전략 {id}의 정량 전략목표는 1개(문자열)만 허용",
                          "strategy {id}: quantitative goal must be a single string"),
    "bad_task_id": ("전략과제 id {id}는 N-M 형식이어야 함",
                    "strategic task id {id} must look like N-M"),
    "task_no_parent": ("전략과제 {id}의 상위 전략 {parent} 없음",
                       "strategic task {id}: parent strategy {parent} does not exist"),
    "strategy_no_task": ("전략과제 없는 전략: {id}",
                         "strategy without strategic task: {id}"),
    "representative_task_mapping": ("후보 {candidate}가 전략 {id}의 전략과제 {count}개에 배치됨 (1개 필요)",
                                    "candidate {candidate} is placed in {count} tasks of strategy {id} (exactly 1 needed)"),
    "task_candidate_mismatch": ("전략과제 {id}의 후보 {candidate}가 상위 전략의 후보 목록에 없음",
                                "strategic task {id}: candidate {candidate} is not listed on its parent strategy"),
    "impl_disabled": ("이행과제 생략 설정인데 이행과제 {count}건 존재",
                      "implementation tasks are switched off but {count} exist"),
    "bad_impl_id": ("이행과제 id {id}는 N-M-L 형식이어야 함",
                    "implementation task id {id} must look like N-M-L"),
    "impl_no_parent": ("이행과제 {id}의 상위 전략과제 {parent} 없음",
                       "implementation task {id}: parent task {parent} does not exist"),
    "task_no_impl": ("이행과제 없는 전략과제: {id}",
                     "strategic task without implementation task: {id}"),
    "self_precedes": ("이행과제 {id}가 자기 자신을 선행",
                      "implementation task {id} precedes itself"),
    "precedes_cycle": ("이행과제 선후관계 순환: {cycle}",
                       "precedence cycle among implementation tasks: {cycle}"),
    "kpi_disabled": ("성과지표 생략 설정인데 지표 {count}건 존재",
                     "KPI step is switched off but {count} KPI(s) exist"),
    "scope_needs_impl": ("{scope} 적용 계층은 이행과제 단계가 필요함",
                         "KPI scope {scope} needs the implementation task step"),
    "gov_needs_dual": ("정부업무평가 트랙(GOV)은 전략목표 패턴 dual(이중형)이 필요함",
                       "GOV track needs goal pattern dual"),
    "bad_kpi_id": ("지표 id {id}는 N-KPI-X, N-M-KPI-X, N-M-L-KPI-X 형식이어야 함",
                   "KPI id {id} must look like N-KPI-X, N-M-KPI-X or N-M-L-KPI-X"),
    "kpi_no_target": ("지표 {id}의 측정 대상 {target} 없음",
                      "KPI {id}: measured element {target} does not exist"),
    "kpi_level_scope": ("지표 {id}의 계층({level})은 적용 계층 {scope}에 포함되지 않음",
                        "KPI {id}: level {level} is outside scope {scope}"),
    "rnd_impact": ("R&D 트랙 기본값은 Impact 지표 제외: {id} (포함하려면 rnd_include_impact를 true로 기록)",
                   "RND track excludes Impact KPIs by default: {id} (set rnd_include_impact to true to include)"),
    "element_no_kpi": ("지표 없는 {level}: {id}",
                       "{level} without KPI: {id}"),
    "strategy_kpi_contrib": ("전략 지표 {id}는 상위 기여 지표가 없어야 함",
                             "strategy KPI {id} must not contribute to another KPI"),
    "kpi_contrib_missing": ("지표 {id}의 상위 기여 지표(contributes_to) 미입력",
                            "KPI {id} has no contributes_to"),
    "kpi_contrib_wrong_parent": ("지표 {id}의 기여 대상 {contrib}는 상위 요소 {parent}의 지표가 아님",
                                 "KPI {id} contributes to {contrib}, which is not a KPI of parent {parent}"),
    "step_label": ("[{step}단계] ", "[step {step}] "),
    "result_pass": ("결과: 통과 (1-{step}단계 점검)",
                    "Result: PASS (checks for steps 1-{step})"),
    "result_fail": ("결과: 위반 {count}건 (1-{step}단계 점검)",
                    "Result: FAIL, {count} violation(s) (checks for steps 1-{step})"),
    "input_error": ("입력 오류: {error}",
                    "Input error: {error}"),
}
LEVEL_NAMES = {
    "strategy": ("전략", "strategy"),
    "task": ("전략과제", "strategic task"),
    "impl": ("이행과제", "implementation task"),
}


def msg(lang, code, **kw):
    """Render one message in the chosen language."""
    ko, en = MESSAGES[code]
    return (ko if lang == "ko" else en).format(**kw)


class Report:
    """Collects violations (fail the check) and notes (advice only)."""

    def __init__(self, lang):
        self.lang = lang
        self.violations = []
        self.notes = []
        self._seen = set()

    def add(self, step, code, **kw):
        key = (code, tuple(sorted((k, str(v)) for k, v in kw.items())))
        if key in self._seen:
            return
        self._seen.add(key)
        self.violations.append((step, code, kw))

    def note(self, step, code, **kw):
        self.notes.append((step, code, kw))

    def codes(self):
        return [code for _, code, _ in self.violations]

    def render(self, step):
        lines = []
        for s, code, kw in self.violations:
            lines.append(msg(self.lang, "step_label", step=s) + msg(self.lang, code, **kw))
        for s, code, kw in self.notes:
            lines.append(msg(self.lang, "step_label", step=s) + msg(self.lang, code, **kw))
        if self.violations:
            lines.append(msg(self.lang, "result_fail", count=len(self.violations), step=step))
        else:
            lines.append(msg(self.lang, "result_pass", step=step))
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Loading helpers
# ---------------------------------------------------------------------------
def _blank(value):
    return not isinstance(value, str) or not value.strip()


def load_collection(state, key, report):
    """Return (entries, index) for a list of {id, text, ...} objects.

    Structural problems are reported once, tagged with the owning step.
    """
    step = COLLECTION_STEP[key]
    raw = state.get(key, [])
    if raw is None:
        raw = []
    if not isinstance(raw, list):
        report.add(step, "not_list", key=key)
        return [], {}
    entries, index = [], {}
    for pos, entry in enumerate(raw, 1):
        entry_id = as_id(entry.get("id")) if isinstance(entry, dict) else None
        if entry_id is None:
            report.add(step, "bad_entry", key=key, pos=pos)
            continue
        entry = dict(entry, id=entry_id)
        if entry_id in index:
            report.add(step, "duplicate_id", key=key, id=entry_id)
            continue
        if _blank(entry.get("text")):
            report.add(step, "empty_text", key=key, id=entry_id, field="text")
        index[entry_id] = entry
        entries.append(entry)
    return entries, index


def ref_list(entry, field, key, report, step):
    """Read a list-of-id field; a missing field counts as an empty list."""
    value = entry.get(field, [])
    if value is None:
        return []
    if not isinstance(value, list):
        report.add(step, "bad_field", key=key, id=entry["id"], field=field)
        return []
    return [ref for ref in (as_id(v) for v in value) if ref is not None]


def check_refs(refs, index, key, entry_id, target, report, step):
    """Keep only existing references; report the unknown ones."""
    known = []
    for ref in refs:
        if ref in index:
            known.append(ref)
        else:
            report.add(step, "bad_ref", key=key, id=entry_id, target=target, ref=ref)
    return known


def as_id(value):
    """Accept str or int ids (not bool); return a stripped string or None."""
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def pick(value, allowed):
    """Return value when it is one of the allowed strings, else None.

    Guards every enum field so that lists or objects typed into a field are
    reported instead of crashing dictionary or set lookups.
    """
    return value if isinstance(value, str) and value in allowed else None


def flag(state, field):
    settings = state.get("settings") or {}
    return isinstance(settings, dict) and settings.get(field) is True


class State:
    """Loaded collections plus the settings every step needs."""

    def __init__(self, raw, report, upto):
        self.raw = raw
        self.report = report
        self.upto = upto
        self.col = {}
        self.idx = {}
        self._settings = {}
        for key, owner in COLLECTION_STEP.items():
            if owner <= upto:
                self.col[key], self.idx[key] = load_collection(raw, key, report)
            else:
                self.col[key], self.idx[key] = [], {}

    def setting(self, field, allowed, required=True):
        """Validated setting value or None; each problem is reported once."""
        if field in self._settings:
            return self._settings[field]
        settings = self.raw.get("settings") or {}
        value = settings.get(field) if isinstance(settings, dict) else None
        step = SETTING_STEP[field]
        result = None
        if value is None or value == "":
            if required:
                self.report.add(step, "missing_setting", field=field, allowed=", ".join(allowed))
        elif pick(value, allowed) is None:
            self.report.add(step, "bad_setting", field=field, value=value,
                            allowed=", ".join(allowed))
        else:
            result = value
        self._settings[field] = result
        return result

    def items(self, key):
        return self.col[key]

    def index(self, key):
        return self.idx[key]


# ---------------------------------------------------------------------------
# Step checks
# ---------------------------------------------------------------------------
def check_step1(st, rep):
    hyp = st.raw.get("hypothesis")
    if not isinstance(hyp, dict):
        rep.add(1, "not_object", key="hypothesis")
        hyp = {}
    for field in ("subject", "space", "time"):
        if _blank(hyp.get(field)):
            rep.add(1, "hypothesis_missing", field=field)
    if not st.items("beneficiaries"):
        rep.add(1, "no_beneficiary")
    declared_none = st.raw.get("no_upper_alignment") is True
    if not st.items("upper_alignments") and not declared_none:
        rep.add(1, "upper_alignment_missing")
    if st.items("upper_alignments") and declared_none:
        rep.add(1, "upper_alignment_conflict")
    if not st.items("issues"):
        rep.add(1, "no_issue")


def analysis_path(st, rep, step):
    """Return (tool, gap_mode); gap_mode is None on the SWOT path."""
    tool = st.setting("analysis_tool", ANALYSIS_TOOLS)
    gap_mode = None
    if tool == "gap":
        gap_mode = st.setting("gap_mode", GAP_MODES)
    return tool, gap_mode


def check_step5(st, rep):
    tool, gap_mode = analysis_path(st, rep, 5)
    integrated = tool == "gap" and gap_mode == "integrated"
    facts = st.index("facts")
    for fact in st.items("facts"):
        source = fact.get("source")
        if pick(source, FACT_SOURCES) is None:
            rep.add(5, "bad_value", key="facts", id=fact["id"], field="source",
                    value=source, allowed=", ".join(FACT_SOURCES))
        elif integrated and source != "benchmark":
            rep.add(5, "fact_skipped_step", id=fact["id"], source=source)
    used_facts = set()
    for impl in st.items("implications"):
        source = impl.get("source")
        if pick(source, IMPLICATION_SOURCES) is None:
            rep.add(5, "bad_value", key="implications", id=impl["id"], field="source",
                    value=source, allowed=", ".join(IMPLICATION_SOURCES))
            source = None
        elif source == "asis" and not integrated:
            rep.add(5, "asis_not_allowed", id=impl["id"])
        elif integrated and source not in ("asis", "benchmark"):
            rep.add(5, "implication_skipped_step", id=impl["id"], source=source)
        refs = ref_list(impl, "facts", "implications", rep, 5)
        refs = check_refs(refs, facts, "implications", impl["id"], "fact", rep, 5)
        used_facts.update(refs)
        if not refs and not integrated:
            rep.add(5, "implication_no_fact", id=impl["id"])
        for ref in refs:
            fact_source = pick(facts[ref].get("source"), FACT_SOURCES)
            if source and fact_source and fact_source != source:
                rep.add(5, "mixed_source", id=impl["id"], source=source,
                        fact=ref, fact_source=fact_source)
    if not st.items("implications"):
        rep.add(5, "no_implication")
    for fact in st.items("facts"):
        if fact["id"] not in used_facts:
            rep.add(5, "fact_unused", id=fact["id"])


def check_issue_induction(st, rep):
    impls = st.index("implications")
    covered = set()
    for issue in st.items("issues"):
        refs = ref_list(issue, "implications", "issues", rep, 6)
        refs = check_refs(refs, impls, "issues", issue["id"], "implication", rep, 6)
        if not refs:
            rep.add(6, "issue_no_implication", id=issue["id"])
        covered.update(refs)
    for impl in st.items("implications"):
        if impl["id"] not in covered:
            rep.add(6, "implication_no_issue", id=impl["id"])


def check_strategy_ids(st, rep):
    if not st.items("strategies"):
        rep.add(6, "no_strategy")
    for strategy in st.items("strategies"):
        if not STRATEGY_ID.match(strategy["id"]):
            rep.add(6, "bad_strategy_id", id=strategy["id"])


def check_swot_factors(st, rep):
    impls = st.index("implications")
    by_type = {t: [] for t in FACTOR_TYPES}
    for factor in st.items("swot_factors"):
        ftype = factor.get("type")
        if pick(ftype, FACTOR_TYPES) is None:
            rep.add(6, "bad_value", key="swot_factors", id=factor["id"], field="type",
                    value=ftype, allowed=", ".join(FACTOR_TYPES))
            continue
        by_type[ftype].append(factor["id"])
        refs = ref_list(factor, "implications", "swot_factors", rep, 6)
        refs = check_refs(refs, impls, "swot_factors", factor["id"], "implication", rep, 6)
        if not refs:
            rep.add(6, "factor_no_implication", id=factor["id"])
        for ref in refs:
            source = pick(impls[ref].get("source"), IMPLICATION_SOURCES)
            if source and source not in FACTOR_ALLOWED_SOURCES[ftype]:
                rep.add(6, "factor_source", id=factor["id"], type=ftype, source=source, impl=ref)
    for ftype in FACTOR_TYPES:
        if not by_type[ftype]:
            rep.add(6, "factor_type_missing", type=ftype)
    return by_type


def check_swot_candidates(st, rep, by_type, mode):
    factors = st.index("swot_factors")
    per_quadrant = {q: [] for q in QUADRANT_TYPES}
    cand_factors = {}
    for cand in st.items("swot_candidates"):
        quadrant = cand.get("quadrant")
        if pick(quadrant, tuple(QUADRANT_TYPES)) is None:
            rep.add(6, "bad_value", key="swot_candidates", id=cand["id"], field="quadrant",
                    value=quadrant, allowed=", ".join(QUADRANT_TYPES))
            continue
        per_quadrant[quadrant].append(cand["id"])
        refs = ref_list(cand, "factors", "swot_candidates", rep, 6)
        refs = check_refs(refs, factors, "swot_candidates", cand["id"], "SWOT factor", rep, 6)
        cand_factors[cand["id"]] = refs
        allowed = QUADRANT_TYPES[quadrant]
        present = set()
        for ref in refs:
            ftype = pick(factors[ref].get("type"), FACTOR_TYPES)
            if ftype is None:
                continue
            if ftype not in allowed:
                rep.add(6, "candidate_wrong_factor", id=cand["id"], quadrant=quadrant,
                        factor=ref, type=ftype)
            present.add(ftype)
        for ftype in allowed:
            if ftype not in present:
                rep.add(6, "candidate_missing_type", id=cand["id"], quadrant=quadrant, type=ftype)
    for quadrant, types in QUADRANT_TYPES.items():
        used = set()
        for cand_id in per_quadrant[quadrant]:
            used.update(cand_factors.get(cand_id, []))
        for ftype in types:
            for factor_id in by_type.get(ftype, []):
                if factor_id not in used:
                    rep.add(6, "quadrant_factor_unused", quadrant=quadrant, factor=factor_id)
        if mode == "fixed" and len(per_quadrant[quadrant]) != 1:
            rep.add(6, "fixed_candidate_count", quadrant=quadrant,
                    count=len(per_quadrant[quadrant]))
    return per_quadrant, cand_factors


def strategy_candidates(st, rep):
    """strategy id -> list of existing candidate ids."""
    cands = st.index("swot_candidates")
    result = {}
    for strategy in st.items("strategies"):
        refs = ref_list(strategy, "candidates", "strategies", rep, 6)
        refs = check_refs(refs, cands, "strategies", strategy["id"], "SWOT candidate", rep, 6)
        result[strategy["id"]] = refs
        if not refs:
            rep.add(6, "strategy_no_candidate", id=strategy["id"])
    return result


def check_one_candidate_per_quadrant(st, rep, s_cands, expected_count, count_code):
    """Shared rule for fixed mode: four strategies, one quadrant each."""
    strategies = st.items("strategies")
    if len(strategies) != expected_count:
        rep.add(6, count_code, count=len(strategies))
    quadrants = []
    for strategy in strategies:
        refs = s_cands[strategy["id"]]
        if len(refs) != 1:
            rep.add(6, "one_candidate_required", id=strategy["id"], count=len(refs))
        for ref in refs:
            quadrant = pick(st.index("swot_candidates")[ref].get("quadrant"),
                            tuple(QUADRANT_TYPES))
            if quadrant:
                quadrants.append(quadrant)
    if sorted(quadrants) != sorted(QUADRANT_TYPES):
        rep.add(6, "quadrant_mapping")


def check_swot_strategy_mapping(st, rep, mode, option, per_quadrant, cand_factors):
    s_cands = strategy_candidates(st, rep)
    cands = st.index("swot_candidates")
    strategies = st.items("strategies")
    if mode == "fixed":
        check_one_candidate_per_quadrant(st, rep, s_cands, 4, "fixed_strategy_count")
    elif mode == "flexible" and option == "as_is":
        usage = {cand_id: 0 for cand_id in cands}
        for strategy in strategies:
            refs = s_cands[strategy["id"]]
            if len(refs) != 1:
                rep.add(6, "one_candidate_required", id=strategy["id"], count=len(refs))
            for ref in refs:
                usage[ref] += 1
        for cand_id, count in usage.items():
            if count != 1:
                rep.add(6, "as_is_mapping", id=cand_id, count=count)
    elif mode == "flexible" and option == "representative":
        if len(strategies) != 4:
            rep.add(6, "representative_count", count=len(strategies))
        seen_quadrants = []
        for strategy in strategies:
            quads = {pick(cands[ref].get("quadrant"), tuple(QUADRANT_TYPES))
                     for ref in s_cands[strategy["id"]]}
            quads.discard(None)
            if len(quads) > 1:
                rep.add(6, "representative_mixed", id=strategy["id"])
                continue
            if not quads:
                continue
            quadrant = quads.pop()
            seen_quadrants.append(quadrant)
            for cand_id in per_quadrant.get(quadrant, []):
                if cand_id not in s_cands[strategy["id"]]:
                    rep.add(6, "representative_incomplete", id=strategy["id"],
                            quadrant=quadrant, missing=cand_id)
        if sorted(seen_quadrants) != sorted(QUADRANT_TYPES):
            rep.add(6, "quadrant_mapping")
    elif mode == "flexible" and option == "cross":
        reflected = set()
        for strategy in strategies:
            for ref in s_cands[strategy["id"]]:
                reflected.update(cand_factors.get(ref, []))
        for factor in st.items("swot_factors"):
            if factor["id"] not in reflected:
                rep.add(6, "cross_factor_unused", factor=factor["id"])
    elif mode == "issue_linked":
        issues = st.index("issues")
        if len(strategies) != len(st.items("issues")):
            rep.add(6, "issue_linked_count", strategies=len(strategies),
                    issues=len(st.items("issues")))
        issue_use = {issue_id: 0 for issue_id in issues}
        for strategy in strategies:
            refs = ref_list(strategy, "issues", "strategies", rep, 6)
            refs = [r for r in refs if r in issues]
            if len(refs) != 1:
                rep.add(6, "issue_linked_one_issue", id=strategy["id"], count=len(refs))
            for ref in refs:
                issue_use[ref] += 1
        for issue_id, count in issue_use.items():
            if count != 1:
                rep.add(6, "issue_linked_one_strategy", id=issue_id, count=count)


def check_gap_path(st, rep):
    issues = st.index("issues")
    gaps = st.index("gaps")
    issues_with_gap = set()
    for gap in st.items("gaps"):
        issue_ref = as_id(gap.get("issue"))
        if issue_ref is None:
            rep.add(6, "empty_text", key="gaps", id=gap["id"], field="issue")
        elif issue_ref not in issues:
            rep.add(6, "bad_ref", key="gaps", id=gap["id"], target="issue", ref=issue_ref)
        else:
            issues_with_gap.add(issue_ref)
        for field in ("asis", "tobe"):
            if _blank(gap.get(field)):
                rep.add(6, "gap_missing_state", id=gap["id"], field=field)
    for issue in st.items("issues"):
        if issue["id"] not in issues_with_gap:
            rep.add(6, "issue_no_gap", id=issue["id"])
    resolved = set()
    for strategy in st.items("strategies"):
        refs = ref_list(strategy, "gaps", "strategies", rep, 6)
        refs = check_refs(refs, gaps, "strategies", strategy["id"], "gap", rep, 6)
        if not refs:
            rep.add(6, "strategy_no_gap", id=strategy["id"])
        resolved.update(refs)
    for gap in st.items("gaps"):
        if gap["id"] not in resolved:
            rep.add(6, "gap_no_strategy", id=gap["id"])
    if len(st.items("issues")) < MIN_GAP_ISSUES_RECOMMENDED:
        rep.note(6, "note_gap_issue_count", count=len(st.items("issues")))


def check_step6(st, rep):
    check_issue_induction(st, rep)
    check_strategy_ids(st, rep)
    tool, _ = analysis_path(st, rep, 6)
    if tool == "swot":
        mode = st.setting("swot_mode", SWOT_MODES)
        option = None
        if mode == "fixed":
            st.setting("fixed_followup", ("Y", "N"), required=False)
        if mode == "flexible":
            option = st.setting("flexible_option", FLEXIBLE_OPTIONS)
        by_type = check_swot_factors(st, rep)
        per_quadrant, cand_factors = check_swot_candidates(st, rep, by_type, mode)
        if mode and (mode != "flexible" or option):
            check_swot_strategy_mapping(st, rep, mode, option, per_quadrant, cand_factors)
    elif tool == "gap":
        check_gap_path(st, rep)


def check_step7(st, rep):
    vision = st.raw.get("vision")
    mission = st.raw.get("mission")
    if not isinstance(vision, dict):
        rep.add(7, "not_object", key="vision")
        vision = {}
    if not isinstance(mission, dict):
        rep.add(7, "not_object", key="mission")
        mission = {}
    if _blank(vision.get("text")):
        rep.add(7, "no_vision")
    if _blank(mission.get("text")):
        rep.add(7, "no_mission")
    vision = dict(vision, id="vision")
    mission = dict(mission, id="mission")
    ua_refs = ref_list(vision, "upper_alignments", "vision", rep, 7)
    ua_refs = check_refs(ua_refs, st.index("upper_alignments"), "vision", "vision",
                         "upper alignment", rep, 7)
    if st.items("upper_alignments") and not ua_refs:
        rep.add(7, "vision_no_upper")
    ben_refs = ref_list(mission, "beneficiaries", "mission", rep, 7)
    ben_refs = check_refs(ben_refs, st.index("beneficiaries"), "mission", "mission",
                          "beneficiary", rep, 7)
    if not ben_refs:
        rep.add(7, "mission_no_beneficiary")
    strategies = st.index("strategies")
    cv_count = {s_id: 0 for s_id in strategies}
    for cv in st.items("core_values"):
        target = as_id(cv.get("strategy"))
        if target is None:
            rep.add(7, "cv_no_strategy", id=cv["id"])
        elif target not in strategies:
            rep.add(7, "bad_ref", key="core_values", id=cv["id"], target="strategy", ref=target)
        else:
            cv_count[target] += 1
    for s_id, count in cv_count.items():
        if count == 0:
            rep.add(7, "strategy_no_cv", id=s_id)
        elif count > 1:
            rep.add(7, "strategy_multi_cv", id=s_id, count=count)


def check_issue_strategy_links(st, rep, tool):
    issues = st.index("issues")
    gaps = st.index("gaps")
    resolved = set()
    for strategy in st.items("strategies"):
        refs = ref_list(strategy, "issues", "strategies", rep, 8)
        refs = check_refs(refs, issues, "strategies", strategy["id"], "issue", rep, 8)
        if not refs:
            rep.add(8, "strategy_no_issue", id=strategy["id"])
        resolved.update(refs)
        if tool == "gap":
            for gap_id in ref_list(strategy, "gaps", "strategies", rep, 8):
                gap = gaps.get(gap_id)
                gap_issue = as_id(gap.get("issue")) if gap else None
                if gap_issue in issues and gap_issue not in refs:
                    rep.add(8, "gap_issue_mismatch", id=strategy["id"], gap=gap_id,
                            issue=gap_issue)
    for issue in st.items("issues"):
        if issue["id"] not in resolved:
            rep.add(8, "issue_no_strategy", id=issue["id"])


def check_goals(st, rep):
    pattern = st.setting("goal_pattern", GOAL_PATTERNS)
    for strategy in st.items("strategies"):
        quant = strategy.get("quantitative_goal")
        if quant is not None and not isinstance(quant, str):
            rep.add(8, "quant_goal_single", id=strategy["id"])
        if pattern is None:
            continue
        need_qual, need_quant = GOAL_RULES[pattern]
        for field, needed in (("qualitative_goal", need_qual), ("quantitative_goal", need_quant)):
            value = strategy.get(field)
            present = isinstance(value, str) and bool(value.strip())
            if needed and not present:
                rep.add(8, "goal_required", pattern=pattern, id=strategy["id"], field=field)
            if not needed and present:
                rep.add(8, "goal_forbidden", pattern=pattern, id=strategy["id"], field=field)


def check_strategic_tasks(st, rep):
    strategies = st.index("strategies")
    has_task = set()
    for task in st.items("strategic_tasks"):
        match = TASK_ID.match(task["id"])
        if not match:
            rep.add(8, "bad_task_id", id=task["id"])
            continue
        parent = match.group(1)
        if parent not in strategies:
            rep.add(8, "task_no_parent", id=task["id"], parent=parent)
            continue
        has_task.add(parent)
    for s_id in strategies:
        if s_id not in has_task:
            rep.add(8, "strategy_no_task", id=s_id)


def check_representative_tasks(st, rep):
    """In the representative option each candidate becomes one strategic task."""
    strategies = st.index("strategies")
    known = st.index("swot_candidates")
    placed = {}
    for task in st.items("strategic_tasks"):
        match = TASK_ID.match(task["id"])
        cand = as_id(task.get("candidate"))
        if not match or match.group(1) not in strategies or cand is None:
            continue
        parent = match.group(1)
        s_cands = ref_list(strategies[parent], "candidates", "strategies", rep, 8)
        if cand not in s_cands:
            rep.add(8, "task_candidate_mismatch", id=task["id"], candidate=cand)
            continue
        key = (parent, cand)
        placed[key] = placed.get(key, 0) + 1
    for s_id, strategy in strategies.items():
        for cand in ref_list(strategy, "candidates", "strategies", rep, 8):
            if cand not in known:
                continue
            count = placed.get((s_id, cand), 0)
            if count != 1:
                rep.add(8, "representative_task_mapping", candidate=cand, id=s_id, count=count)


def check_step8(st, rep):
    tool, _ = analysis_path(st, rep, 8)
    check_issue_strategy_links(st, rep, tool)
    check_goals(st, rep)
    check_strategic_tasks(st, rep)
    if tool == "swot":
        mode = st.setting("swot_mode", SWOT_MODES)
        if mode == "flexible":
            option = st.setting("flexible_option", FLEXIBLE_OPTIONS)
            if option == "representative":
                check_representative_tasks(st, rep)


def find_cycle(graph):
    """Return one cycle as a list of node ids, or None. Iterative DFS."""
    white, grey, black = 0, 1, 2
    color = {node: white for node in graph}
    for start in sorted(graph):
        if color[start] != white:
            continue
        stack = [(start, iter(sorted(graph[start])))]
        path = [start]
        color[start] = grey
        while stack:
            node, children = stack[-1]
            advanced = False
            for child in children:
                if color.get(child, white) == grey:
                    return path[path.index(child):] + [child]
                if color.get(child, white) == white and child in graph:
                    color[child] = grey
                    stack.append((child, iter(sorted(graph[child]))))
                    path.append(child)
                    advanced = True
                    break
            if not advanced:
                color[node] = black
                stack.pop()
                path.pop()
    return None


def check_step9(st, rep):
    enabled = flag(st.raw, "implementation_tasks")
    impls = st.items("implementation_tasks")
    if not enabled:
        if impls:
            rep.add(9, "impl_disabled", count=len(impls))
        return
    tasks = st.index("strategic_tasks")
    impl_index = st.index("implementation_tasks")
    has_impl = set()
    graph = {}
    for impl in impls:
        match = IMPL_ID.match(impl["id"])
        if not match:
            rep.add(9, "bad_impl_id", id=impl["id"])
        elif match.group(1) not in tasks:
            rep.add(9, "impl_no_parent", id=impl["id"], parent=match.group(1))
        else:
            has_impl.add(match.group(1))
        refs = ref_list(impl, "precedes", "implementation_tasks", rep, 9)
        refs = check_refs(refs, impl_index, "implementation_tasks", impl["id"],
                          "implementation task", rep, 9)
        if impl["id"] in refs:
            rep.add(9, "self_precedes", id=impl["id"])
        graph[impl["id"]] = [r for r in refs if r != impl["id"]]
    for task_id in tasks:
        if task_id not in has_impl:
            rep.add(9, "task_no_impl", id=task_id)
    cycle = find_cycle(graph)
    if cycle:
        rep.add(9, "precedes_cycle", cycle=" -> ".join(cycle))


def kpi_level(target):
    return ("strategy", "task", "impl")[target.count("-")]


def check_step10(st, rep):
    scope = st.setting("kpi_scope", KPI_SCOPES)
    kpis = st.items("kpis")
    if scope is None:
        return
    if scope == "none":
        if kpis:
            rep.add(10, "kpi_disabled", count=len(kpis))
        return
    track = st.setting("kpi_track", KPI_TRACKS)
    impl_enabled = flag(st.raw, "implementation_tasks")
    if scope in ("all", "lower") and not impl_enabled:
        rep.add(10, "scope_needs_impl", scope=scope)
    if track == "GOV":
        if st.setting("goal_pattern", GOAL_PATTERNS) != "dual":
            rep.add(10, "gov_needs_dual")
    targets = {
        "strategy": st.index("strategies"),
        "task": st.index("strategic_tasks"),
        "impl": st.index("implementation_tasks"),
    }
    kpi_index = st.index("kpis")
    kpi_target = {}
    measured = set()
    for kpi in kpis:
        match = KPI_ID.match(kpi["id"])
        if not match:
            rep.add(10, "bad_kpi_id", id=kpi["id"])
            continue
        target = match.group(1)
        level = kpi_level(target)
        kpi_target[kpi["id"]] = (target, level)
        if target not in targets[level]:
            rep.add(10, "kpi_no_target", id=kpi["id"], target=target)
        if level not in SCOPE_LEVELS[scope]:
            rep.add(10, "kpi_level_scope", id=kpi["id"], level=level, scope=scope)
        measured.add(target)
        kpi_type = kpi.get("type")
        if pick(kpi_type, KPI_TYPES) is None:
            rep.add(10, "bad_value", key="kpis", id=kpi["id"], field="type",
                    value=kpi_type, allowed=", ".join(KPI_TYPES))
        elif kpi_type == "Impact" and track == "RND" and not flag(st.raw, "rnd_include_impact"):
            rep.add(10, "rnd_impact", id=kpi["id"])
    lang_index = 0 if rep.lang == "ko" else 1
    for level in SCOPE_LEVELS[scope]:
        for element_id in targets[level]:
            if element_id not in measured:
                rep.add(10, "element_no_kpi", level=LEVEL_NAMES[level][lang_index], id=element_id)
    for kpi in kpis:
        if kpi["id"] not in kpi_target:
            continue
        target, level = kpi_target[kpi["id"]]
        contrib = as_id(kpi.get("contributes_to"))
        if contrib and contrib not in kpi_index:
            rep.add(10, "bad_ref", key="kpis", id=kpi["id"], target="KPI", ref=contrib)
            continue
        if scope != "all":
            continue
        if level == "strategy":
            if contrib:
                rep.add(10, "strategy_kpi_contrib", id=kpi["id"])
            continue
        if not contrib:
            rep.add(10, "kpi_contrib_missing", id=kpi["id"])
            continue
        parent = target.rsplit("-", 1)[0]
        contrib_target = kpi_target.get(contrib, (None, None))[0]
        if contrib_target != parent:
            rep.add(10, "kpi_contrib_wrong_parent", id=kpi["id"], contrib=contrib, parent=parent)


STEP_CHECKS = {1: check_step1, 5: check_step5, 6: check_step6, 7: check_step7,
               8: check_step8, 9: check_step9, 10: check_step10}


def run_checks(raw, upto, lang="en"):
    """Run every check for steps 1..upto and return the Report."""
    report = Report(lang)
    if not isinstance(raw, dict):
        report.add(1, "not_object", key="state")
        return report
    state = State(raw, report, upto)
    for step in sorted(STEP_CHECKS):
        if step <= upto:
            STEP_CHECKS[step](state, report)
    return report


# ---------------------------------------------------------------------------
# Field guide printed by --schema. Enumerations come from the constants above
# so the guide and the checks cannot disagree.
# ---------------------------------------------------------------------------
SCHEMA_FIELDS = [
    ("settings", "선택한 옵션(아래 옵션 값)", "chosen options (see option values below)"),
    ("hypothesis", "{subject: 주체, space: 공간 범위, time: 시간 범위}",
     "{subject, space (spatial scope), time (time scope)}"),
    ("upper_alignments", "[{id, text}]. 상위 정렬이 없으면 []와 \"no_upper_alignment\": true",
     "[{id, text}]. With no upper alignment use [] and \"no_upper_alignment\": true"),
    ("beneficiaries", "[{id, text, needs}]", "[{id, text, needs}]"),
    ("issues", "[{id, text, implications: [시사점 id]}]", "[{id, text, implications: [implication ids]}]"),
    ("facts", "[{id, source, text}]", "[{id, source, text}]"),
    ("implications", "[{id, source, text, facts: [팩트 id]}]", "[{id, source, text, facts: [fact ids]}]"),
    ("swot_factors", "[{id, type, text, implications: [시사점 id]}]",
     "[{id, type, text, implications: [implication ids]}]"),
    ("swot_candidates", "[{id, quadrant, text, factors: [요인 id]}]",
     "[{id, quadrant, text, factors: [factor ids]}]"),
    ("gaps", "[{id, issue: 문제이슈 id, asis, tobe, text}]", "[{id, issue: issue id, asis, tobe, text}]"),
    ("strategies", "[{id: \"1\", text, issues, candidates(SWOT) 또는 gaps(갭분석), "
                   "qualitative_goal, quantitative_goal}]",
     "[{id: \"1\", text, issues, candidates (SWOT) or gaps (gap), qualitative_goal, quantitative_goal}]"),
    ("vision", "{text, upper_alignments: [상위 정렬 id]}", "{text, upper_alignments: [ids]}"),
    ("mission", "{text, beneficiaries: [수요자 id]}", "{text, beneficiaries: [ids]}"),
    ("core_values", "[{id, text, strategy: 전략 id}]", "[{id, text, strategy: strategy id}]"),
    ("strategic_tasks", "[{id: \"N-M\", text, candidate(구분별 대표 방식에서 후보 id)}]",
     "[{id: \"N-M\", text, candidate (representative option: candidate id)}]"),
    ("implementation_tasks", "[{id: \"N-M-L\", text, precedes: [이행과제 id]}]",
     "[{id: \"N-M-L\", text, precedes: [implementation task ids]}]"),
    ("kpis", "[{id: \"N-KPI-X\" | \"N-M-KPI-X\" | \"N-M-L-KPI-X\", text, type, contributes_to, "
             "method, target, deadline}]",
     "[{id: \"N-KPI-X\" | \"N-M-KPI-X\" | \"N-M-L-KPI-X\", text, type, contributes_to, "
     "method, target, deadline}]"),
]
SCHEMA_OPTIONS = [
    ("analysis_tool", ANALYSIS_TOOLS, "분석도구", "analysis tool"),
    ("gap_mode", GAP_MODES, "갭분석 모드: split 분리, integrated 통합", "gap mode"),
    ("swot_mode", SWOT_MODES, "SWOT 모드: fixed 고정형, flexible 유연형, issue_linked 문제이슈연결형",
     "SWOT mode"),
    ("fixed_followup", ("Y", "N"), "고정형 후속", "fixed-mode follow-up"),
    ("flexible_option", FLEXIBLE_OPTIONS,
     "유연형 후속: as_is 후보 그대로, representative 구분별 대표, cross 구분 교차 결합",
     "flexible-mode option"),
    ("goal_pattern", GOAL_PATTERNS,
     "전략목표: integrated 통합형, dual 이중형, qualitative 정성형, quantitative 정량형", "goal pattern"),
    ("implementation_tasks", ("true", "false"), "이행과제 단계 수행", "implementation task step on"),
    ("kpi_scope", KPI_SCOPES, "성과지표 적용 계층: all 전계층형, lower 하위형, strategy 전략형, none 생략",
     "KPI scope"),
    ("kpi_track", KPI_TRACKS, "성과지표 트랙: GOV 정부업무평가, RND R&D, AUTO 모델 자율, QUAL 질적 지표",
     "KPI track"),
    ("rnd_include_impact", ("true", "false"), "R&D 트랙의 Impact 지표 포함", "include Impact KPIs on RND"),
]
SCHEMA_TEXT = {
    "ko": {
        "keys": "[상태 파일 키]",
        "rules": [
            "[규칙]",
            "목록 항목은 모두 id와 text를 가지며 id는 같은 목록 안에서 중복되지 않음",
            "연결 필드에는 연결 대상의 id 목록을 적음",
            "전략과제, 이행과제, 지표의 상위 요소는 id 번호로 정해짐 (1-2-3은 전략과제 1-2 소속, "
            "1-2-KPI-1은 전략과제 1-2 측정)",
            "source: macro 거시환경, micro 미시환경, internal 내부현황, benchmark 벤치마킹, "
            "asis 갭분석 통합 모드의 As-is 시사점",
            "type(요인): S 강점, W 약점, O 기회, T 위협 / quadrant: SO, ST, WO, WT",
            "type(지표): " + ", ".join(KPI_TYPES),
        ],
        "options": "[settings 옵션 값]",
    },
    "en": {
        "keys": "[state file keys]",
        "rules": [
            "[rules]",
            "every list entry has id and text; ids are unique within a list",
            "link fields hold lists of target ids",
            "the parent of a task, implementation task or KPI is read from its id "
            "(1-2-3 belongs to task 1-2, 1-2-KPI-1 measures task 1-2)",
            "source: macro, micro, internal, benchmark, asis (as-is implication in integrated gap mode)",
            "type (factor): S, W, O, T / quadrant: SO, ST, WO, WT",
            "type (KPI): " + ", ".join(KPI_TYPES),
        ],
        "options": "[settings option values]",
    },
}


def schema_text(lang):
    text = SCHEMA_TEXT[lang]
    column = 1 if lang == "ko" else 2
    lines = [text["keys"]]
    for row in SCHEMA_FIELDS:
        lines.append("- {0}: {1}".format(row[0], row[column]))
    lines.append("")
    lines.append(text["rules"][0])
    lines.extend("- " + rule for rule in text["rules"][1:])
    lines.append("")
    lines.append(text["options"])
    for key, values, ko_label, en_label in SCHEMA_OPTIONS:
        label = ko_label if lang == "ko" else en_label
        lines.append("- {0} = {1} ({2})".format(key, " | ".join(values), label))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Mermaid trace charts
# ---------------------------------------------------------------------------
def _node_id(prefix, element_id):
    """ASCII-only, collision-free node id: other characters become _<hex>_."""
    body = "".join(ch if ch.isascii() and ch.isalnum() else "_{0:x}_".format(ord(ch))
                   for ch in element_id)
    return prefix + "_" + body


def _label(element_id, text):
    clean = str(text or "").replace('"', "'").replace("\n", " ").strip()
    return "{0}. {1}".format(element_id, clean) if clean else element_id


class Chart:
    def __init__(self, title):
        self.lines = ["%% " + title, "graph LR"]
        self.seen = set()

    def node(self, prefix, element_id, text):
        nid = _node_id(prefix, element_id)
        if nid not in self.seen:
            self.seen.add(nid)
            self.lines.append('    {0}["{1}"]'.format(nid, _label(element_id, text)))
        return nid

    def edge(self, a, b):
        self.lines.append("    {0} --> {1}".format(a, b))

    def render(self):
        return "\n".join(self.lines)


def _entries(raw, key):
    value = raw.get(key) or []
    if not isinstance(value, list):
        return []
    return [dict(e, id=as_id(e.get("id"))) for e in value
            if isinstance(e, dict) and as_id(e.get("id")) is not None]


def _refs(entry, field):
    value = entry.get(field) or []
    if not isinstance(value, list):
        return []
    return [ref for ref in (as_id(v) for v in value) if ref is not None]


def _add_execution_chain(chart, raw):
    """strategy -> strategic task -> implementation task, plus KPIs."""
    strategies = {e["id"]: e for e in _entries(raw, "strategies")}
    tasks = {e["id"]: e for e in _entries(raw, "strategic_tasks")}
    for task_id, task in tasks.items():
        match = TASK_ID.match(task_id)
        if match and match.group(1) in strategies:
            parent = strategies[match.group(1)]
            chart.edge(chart.node("S", parent["id"], parent.get("text")),
                       chart.node("T", task_id, task.get("text")))
    for impl in _entries(raw, "implementation_tasks"):
        match = IMPL_ID.match(impl["id"])
        if match and match.group(1) in tasks:
            parent = tasks[match.group(1)]
            chart.edge(chart.node("T", parent["id"], parent.get("text")),
                       chart.node("M", impl["id"], impl.get("text")))
    prefixes = {"strategy": ("S", strategies), "task": ("T", tasks),
                "impl": ("M", {e["id"]: e for e in _entries(raw, "implementation_tasks")})}
    for kpi in _entries(raw, "kpis"):
        match = KPI_ID.match(kpi["id"])
        if not match:
            continue
        prefix, pool = prefixes[kpi_level(match.group(1))]
        owner = pool.get(match.group(1))
        if owner:
            chart.edge(chart.node(prefix, owner["id"], owner.get("text")),
                       chart.node("K", kpi["id"], kpi.get("text")))


def trace_chart(raw):
    chart = Chart("trace")
    issues = {e["id"]: e for e in _entries(raw, "issues")}
    impls = {e["id"]: e for e in _entries(raw, "implications")}
    factors = {e["id"]: e for e in _entries(raw, "swot_factors")}
    cands = {e["id"]: e for e in _entries(raw, "swot_candidates")}
    gaps = {e["id"]: e for e in _entries(raw, "gaps")}
    for issue in issues.values():
        for ref in _refs(issue, "implications"):
            if ref in impls:
                chart.edge(chart.node("I", ref, impls[ref].get("text")),
                           chart.node("P", issue["id"], issue.get("text")))
    for cand in cands.values():
        for ref in _refs(cand, "factors"):
            if ref in factors:
                chart.edge(chart.node("F", ref, factors[ref].get("text")),
                           chart.node("C", cand["id"], cand.get("text")))
    for strategy in _entries(raw, "strategies"):
        s_node = chart.node("S", strategy["id"], strategy.get("text"))
        for ref in _refs(strategy, "candidates"):
            if ref in cands:
                chart.edge(chart.node("C", ref, cands[ref].get("text")), s_node)
        for ref in _refs(strategy, "gaps"):
            if ref in gaps:
                chart.edge(chart.node("G", ref, gaps[ref].get("text")), s_node)
        for ref in _refs(strategy, "issues"):
            if ref in issues:
                chart.edge(chart.node("P", ref, issues[ref].get("text")), s_node)
    _add_execution_chain(chart, raw)
    return chart.render()


def vision_chart(raw):
    chart = Chart("vision house")
    vision = raw.get("vision") if isinstance(raw.get("vision"), dict) else {}
    mission = raw.get("mission") if isinstance(raw.get("mission"), dict) else {}
    uas = {e["id"]: e for e in _entries(raw, "upper_alignments")}
    bens = {e["id"]: e for e in _entries(raw, "beneficiaries")}
    v_node = chart.node("V", "V", vision.get("text"))
    m_node = chart.node("MS", "M", mission.get("text"))
    for ref in _refs(vision, "upper_alignments"):
        if ref in uas:
            chart.edge(chart.node("U", ref, uas[ref].get("text")), v_node)
    for ref in _refs(mission, "beneficiaries"):
        if ref in bens:
            chart.edge(chart.node("B", ref, bens[ref].get("text")), m_node)
    strategies = {e["id"]: e for e in _entries(raw, "strategies")}
    for strategy in strategies.values():
        chart.edge(v_node, chart.node("S", strategy["id"], strategy.get("text")))
    for cv in _entries(raw, "core_values"):
        target = as_id(cv.get("strategy"))
        if target in strategies:
            chart.edge(chart.node("CV", cv["id"], cv.get("text")),
                       chart.node("S", target, strategies[target].get("text")))
    _add_execution_chain(chart, raw)
    return chart.render()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def parse_step(value):
    if value == "all":
        return LAST_STEP
    step = int(value)
    if not 1 <= step <= LAST_STEP:
        raise argparse.ArgumentTypeError("step must be 1-10 or all")
    return step


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a strategy-builder state file.")
    parser.add_argument("state", nargs="?", help="path to the JSON state file")
    parser.add_argument("--step", type=parse_step, default=LAST_STEP,
                        help="run checks for steps 1..N (1-10 or all, default all)")
    parser.add_argument("--lang", choices=("ko", "en"), default="en")
    parser.add_argument("--chart", action="store_true",
                        help="also print Mermaid trace and vision-house charts")
    parser.add_argument("--template", action="store_true",
                        help="print an empty state file and exit")
    parser.add_argument("--schema", action="store_true",
                        help="print the state file field guide and exit")
    args = parser.parse_args(argv)
    # Korean messages must survive Windows consoles and piped output.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if args.template:
        print(json.dumps(TEMPLATE, ensure_ascii=False, indent=2))
        return 0
    if args.schema:
        print(schema_text(args.lang))
        return 0
    if not args.state:
        parser.error("state file path is required unless --template is used")
    try:
        with open(args.state, encoding="utf-8") as handle:
            raw = json.load(handle)
    except (OSError, ValueError) as exc:
        print(msg(args.lang, "input_error", error=exc))
        return 2
    report = run_checks(raw, args.step, args.lang)
    print(report.render(args.step))
    if args.chart and isinstance(raw, dict):
        print()
        print(trace_chart(raw))
        print()
        print(vision_chart(raw))
    return 1 if report.violations else 0


if __name__ == "__main__":
    sys.exit(main())
