"""Full-lifecycle tests for scripts/check_strategy.py.

Each path gets a complete valid state that must pass all 10 steps.
Each edge case mutates one valid state and asserts the exact set of
violation codes, so the checker is tested for misses and for noise.
"""
import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT_DIR = os.path.join(HERE, "..", "scripts")
sys.path.insert(0, SCRIPT_DIR)
import check_strategy as cs  # noqa: E402

SCRIPT = os.path.join(SCRIPT_DIR, "check_strategy.py")


# ---------------------------------------------------------------------------
# Fixture builders
# ---------------------------------------------------------------------------
def base_front():
    """Steps 1-5 shared by SWOT and split-gap paths."""
    return {
        "settings": {"implementation_tasks": True, "kpi_scope": "all",
                     "kpi_track": "BSC", "goal_pattern": "dual"},
        "hypothesis": {"subject": "중견 제조기업 A사", "space": "국내 사업장",
                       "time": "2026-2030"},
        "no_upper_alignment": False,
        "upper_alignments": [{"id": "U1", "text": "모회사 중기 경영계획"}],
        "beneficiaries": [{"id": "B1", "text": "B2B 고객사", "needs": "납기 단축"}],
        "facts": [
            {"id": "F1", "source": "macro", "text": "탄소 규제 강화"},
            {"id": "F2", "source": "micro", "text": "경쟁사 가격 인하"},
            {"id": "F3", "source": "internal", "text": "숙련 인력 보유"},
            {"id": "F4", "source": "internal", "text": "설비 노후"},
            {"id": "F5", "source": "benchmark", "text": "선도사 공정 자동화"},
        ],
        "implications": [
            {"id": "I1", "source": "macro", "text": "저탄소 공정 수요 확대", "facts": ["F1"]},
            {"id": "I2", "source": "micro", "text": "가격 경쟁 심화", "facts": ["F2"]},
            {"id": "I3", "source": "internal", "text": "품질 관리 역량 우위", "facts": ["F3"]},
            {"id": "I4", "source": "internal", "text": "생산성 정체", "facts": ["F4"]},
            {"id": "I5", "source": "benchmark", "text": "자동화 전환 효과 확인", "facts": ["F5"]},
        ],
        "issues": [
            {"id": "P1", "text": "저탄소 전환 대응 지연", "implications": ["I1", "I3"]},
            {"id": "P2", "text": "원가 경쟁력 약화", "implications": ["I2"]},
            {"id": "P3", "text": "설비 생산성 저하", "implications": ["I4"]},
            {"id": "P4", "text": "자동화 도입 경로 부재", "implications": ["I5"]},
        ],
        "vision": {"text": "고객이 먼저 찾는 저탄소 정밀부품 기업", "upper_alignments": ["U1"]},
        "mission": {"text": "B2B 고객에게 안정 품질과 짧은 납기 제공", "beneficiaries": ["B1"]},
    }


def swot_factors():
    return [
        {"id": "S1", "type": "S", "text": "숙련 인력 기반 품질 관리", "implications": ["I3"]},
        {"id": "S2", "type": "S", "text": "자동화 선행 사례 학습 경험", "implications": ["I5"]},
        {"id": "W1", "type": "W", "text": "노후 설비", "implications": ["I4"]},
        {"id": "O1", "type": "O", "text": "저탄소 공정 수요", "implications": ["I1"]},
        {"id": "O2", "type": "O", "text": "자동화 확산", "implications": ["I5"]},
        {"id": "T1", "type": "T", "text": "가격 경쟁", "implications": ["I2"]},
    ]


FLEX_CANDIDATES = [
    {"id": "SO1", "quadrant": "SO", "text": "품질 우위 저탄소 라인", "factors": ["S1", "O1"]},
    {"id": "SO2", "quadrant": "SO", "text": "자동화 확장", "factors": ["S2", "O2"]},
    {"id": "ST1", "quadrant": "ST", "text": "품질 차별화", "factors": ["S1", "S2", "T1"]},
    {"id": "WO1", "quadrant": "WO", "text": "설비 교체", "factors": ["W1", "O1", "O2"]},
    {"id": "WT1", "quadrant": "WT", "text": "원가 방어", "factors": ["W1", "T1"]},
]


def add_execution(state, tasks, impls=None, precedes=None):
    """tasks: {strategy_id: n_tasks}; impls: {task_id: n_impl}."""
    state["core_values"] = [{"id": "CV" + s["id"], "text": "가치" + s["id"], "strategy": s["id"]}
                            for s in state["strategies"]]
    state["strategic_tasks"] = []
    for s_id, count in tasks.items():
        for m in range(1, count + 1):
            state["strategic_tasks"].append({"id": "{0}-{1}".format(s_id, m),
                                             "text": "전략과제 {0}-{1}".format(s_id, m)})
    state["implementation_tasks"] = []
    if impls is None:
        impls = {t["id"]: 1 for t in state["strategic_tasks"]}
    for t_id, count in impls.items():
        for n in range(1, count + 1):
            state["implementation_tasks"].append(
                {"id": "{0}-{1}".format(t_id, n), "text": "이행과제 {0}-{1}".format(t_id, n),
                 "precedes": []})
    for before, after in (precedes or []):
        for impl in state["implementation_tasks"]:
            if impl["id"] == before:
                impl["precedes"].append(after)
    return state


def add_kpis(state, scope, kpi_type_by_level=None):
    types = kpi_type_by_level or {"strategy": "Outcome", "task": "Output", "impl": "Activity"}
    kpis = []
    levels = cs.SCOPE_LEVELS[scope]
    if "strategy" in levels:
        for s in state["strategies"]:
            kpis.append({"id": s["id"] + "-KPI-1", "text": "지표 " + s["id"],
                         "type": types["strategy"], "contributes_to": None})
    if "task" in levels:
        for t in state["strategic_tasks"]:
            parent = t["id"].split("-")[0]
            kpis.append({"id": t["id"] + "-KPI-1", "text": "지표 " + t["id"],
                         "type": types["task"],
                         "contributes_to": parent + "-KPI-1" if scope == "all" else None})
    if "impl" in levels:
        for i in state["implementation_tasks"]:
            parent = i["id"].rsplit("-", 1)[0]
            kpis.append({"id": i["id"] + "-KPI-1", "text": "지표 " + i["id"],
                         "type": types["impl"],
                         "contributes_to": parent + "-KPI-1" if scope == "all" else None})
    state["kpis"] = kpis
    state["settings"]["kpi_scope"] = scope
    return state


def dual_goals(strategies):
    for s in strategies:
        s["qualitative_goal"] = "정성 목표 " + s["id"]
        s["quantitative_goal"] = "정량 목표 " + s["id"]
    return strategies


def swot_fixed():
    state = base_front()
    state["settings"].update({"analysis_tool": "swot", "swot_mode": "fixed",
                              "fixed_followup": "Y"})
    state["swot_factors"] = swot_factors()
    state["swot_candidates"] = [
        {"id": "SO", "quadrant": "SO", "text": "저탄소 품질 성장", "factors": ["S1", "S2", "O1", "O2"]},
        {"id": "ST", "quadrant": "ST", "text": "품질 차별화", "factors": ["S1", "S2", "T1"]},
        {"id": "WO", "quadrant": "WO", "text": "설비 혁신", "factors": ["W1", "O1", "O2"]},
        {"id": "WT", "quadrant": "WT", "text": "원가 리스크 관리", "factors": ["W1", "T1"]},
    ]
    state["strategies"] = dual_goals([
        {"id": "1", "text": "저탄소 품질 성장", "candidates": ["SO"], "issues": ["P1"]},
        {"id": "2", "text": "품질 기반 차별화", "candidates": ["ST"], "issues": ["P2"]},
        {"id": "3", "text": "설비 혁신", "candidates": ["WO"], "issues": ["P3"]},
        {"id": "4", "text": "원가 리스크 관리", "candidates": ["WT"], "issues": ["P4"]},
    ])
    add_execution(state, {"1": 2, "2": 1, "3": 1, "4": 1},
                  precedes=[("1-1-1", "1-2-1"), ("1-2-1", "3-1-1")])
    return add_kpis(state, "all")


def swot_fixed_n():
    state = swot_fixed()
    state["settings"]["fixed_followup"] = "N"
    state["facts"] += [{"id": "F6", "source": "macro", "text": "금리 상승"},
                       {"id": "F7", "source": "micro", "text": "고객사 공급망 재편"}]
    state["implications"] += [
        {"id": "I6", "source": "macro", "text": "투자 비용 부담", "facts": ["F6"]},
        {"id": "I7", "source": "micro", "text": "공급사 재평가 확대", "facts": ["F7"]}]
    state["issues"] += [{"id": "P5", "text": "투자 재원 부족", "implications": ["I6"]},
                        {"id": "P6", "text": "공급사 지위 불안", "implications": ["I7"]}]
    state["strategies"][0]["issues"] = ["P1", "P5"]
    state["strategies"][1]["issues"] = ["P2", "P6"]
    return state


def swot_flexible(option):
    state = base_front()
    state["settings"].update({"analysis_tool": "swot", "swot_mode": "flexible",
                              "flexible_option": option})
    state["swot_factors"] = swot_factors()
    state["swot_candidates"] = copy.deepcopy(FLEX_CANDIDATES)
    if option == "as_is":
        state["strategies"] = dual_goals([
            {"id": "1", "text": "저탄소 라인", "candidates": ["SO1"], "issues": ["P1"]},
            {"id": "2", "text": "자동화 확장", "candidates": ["SO2"], "issues": ["P4"]},
            {"id": "3", "text": "품질 차별화", "candidates": ["ST1"], "issues": ["P2"]},
            {"id": "4", "text": "설비 교체", "candidates": ["WO1"], "issues": ["P3"]},
            {"id": "5", "text": "원가 방어", "candidates": ["WT1"], "issues": ["P2"]},
        ])
        add_execution(state, {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1})
    elif option == "representative":
        state["strategies"] = dual_goals([
            {"id": "1", "text": "성장", "candidates": ["SO1", "SO2"], "issues": ["P1", "P4"]},
            {"id": "2", "text": "경쟁우위 유지", "candidates": ["ST1"], "issues": ["P2"]},
            {"id": "3", "text": "혁신", "candidates": ["WO1"], "issues": ["P3"]},
            {"id": "4", "text": "리스크 관리", "candidates": ["WT1"], "issues": ["P2"]},
        ])
        add_execution(state, {"1": 2, "2": 1, "3": 1, "4": 1})
        cand_for = {"1-1": "SO1", "1-2": "SO2", "2-1": "ST1", "3-1": "WO1", "4-1": "WT1"}
        for task in state["strategic_tasks"]:
            task["candidate"] = cand_for[task["id"]]
    elif option == "cross":
        state["strategies"] = dual_goals([
            {"id": "1", "text": "저탄소 설비 전환", "candidates": ["SO1", "WO1"], "issues": ["P1", "P3"]},
            {"id": "2", "text": "자동화 기반 품질 차별화", "candidates": ["SO2", "ST1"], "issues": ["P4", "P2"]},
            {"id": "3", "text": "원가 방어", "candidates": ["WT1"], "issues": ["P2"]},
        ])
        add_execution(state, {"1": 1, "2": 1, "3": 1})
    return add_kpis(state, "all")


def swot_issue_linked():
    state = base_front()
    state["settings"].update({"analysis_tool": "swot", "swot_mode": "issue_linked"})
    state["swot_factors"] = swot_factors()
    state["swot_candidates"] = copy.deepcopy(FLEX_CANDIDATES)
    state["strategies"] = dual_goals([
        {"id": "1", "text": "저탄소 전환", "candidates": ["SO1", "WO1"], "issues": ["P1"]},
        {"id": "2", "text": "원가 경쟁력", "candidates": ["WT1"], "issues": ["P2"]},
        {"id": "3", "text": "설비 생산성", "candidates": ["WO1"], "issues": ["P3"]},
        {"id": "4", "text": "자동화 경로", "candidates": ["SO2"], "issues": ["P4"]},
    ])
    add_execution(state, {"1": 1, "2": 1, "3": 1, "4": 1})
    return add_kpis(state, "all")


def gap_split():
    state = base_front()
    state["settings"].update({"analysis_tool": "gap", "gap_mode": "split",
                              "implementation_tasks": False, "kpi_track": "GOV"})
    state["issues"] = state["issues"][:3]
    state["issues"][2]["implications"] = ["I4", "I5"]
    state["gaps"] = [
        {"id": "G1", "issue": "P1", "asis": "재래식 공정", "tobe": "저탄소 공정", "text": "공정 전환 격차"},
        {"id": "G2", "issue": "P2", "asis": "원가 열위", "tobe": "원가 동등", "text": "원가 격차"},
        {"id": "G3", "issue": "P3", "asis": "노후 설비", "tobe": "자동화 설비", "text": "설비 격차"},
    ]
    state["strategies"] = dual_goals([
        {"id": "1", "text": "저탄소 공정 전환", "gaps": ["G1"], "issues": ["P1"]},
        {"id": "2", "text": "생산 원가 혁신", "gaps": ["G2", "G3"], "issues": ["P2", "P3"]},
    ])
    add_execution(state, {"1": 1, "2": 2}, impls={})
    return add_kpis(state, "strategy")


def gap_integrated(with_benchmark=True):
    state = base_front()
    state["settings"].update({"analysis_tool": "gap", "gap_mode": "integrated",
                              "kpi_track": "RND", "goal_pattern": "integrated"})
    state["facts"] = [{"id": "F5", "source": "benchmark", "text": "선도사 공정 자동화"}] \
        if with_benchmark else []
    state["implications"] = [
        {"id": "A1", "source": "asis", "text": "수작업 검사 비중 높음"},
        {"id": "A2", "source": "asis", "text": "납기 지연 반복"},
        {"id": "A3", "source": "asis", "text": "데이터 미수집"},
    ]
    if with_benchmark:
        state["implications"].append(
            {"id": "I5", "source": "benchmark", "text": "자동화 전환 효과 확인", "facts": ["F5"]})
    state["issues"] = [
        {"id": "P1", "text": "검사 효율 저하", "implications": ["A1"] + (["I5"] if with_benchmark else [])},
        {"id": "P2", "text": "납기 신뢰 저하", "implications": ["A2"]},
        {"id": "P3", "text": "공정 가시성 부족", "implications": ["A3"]},
    ]
    state["gaps"] = [
        {"id": "G1", "issue": "P1", "asis": "수작업 검사", "tobe": "자동 검사", "text": "검사 자동화 격차"},
        {"id": "G2", "issue": "P2", "asis": "지연 반복", "tobe": "납기 준수", "text": "납기 격차"},
        {"id": "G3", "issue": "P3", "asis": "데이터 없음", "tobe": "실시간 수집", "text": "데이터 격차"},
    ]
    state["strategies"] = [
        {"id": "1", "text": "검사 자동화", "gaps": ["G1"], "issues": ["P1"]},
        {"id": "2", "text": "공정 데이터 기반 납기 관리", "gaps": ["G2", "G3"], "issues": ["P2", "P3"]},
    ]
    add_execution(state, {"1": 1, "2": 1})
    return add_kpis(state, "lower", {"strategy": "Outcome", "task": "Output", "impl": "Output"})


ALL_VALID = {
    "swot_fixed_y": swot_fixed,
    "swot_fixed_n": swot_fixed_n,
    "swot_flexible_as_is": lambda: swot_flexible("as_is"),
    "swot_flexible_representative": lambda: swot_flexible("representative"),
    "swot_flexible_cross": lambda: swot_flexible("cross"),
    "swot_issue_linked": swot_issue_linked,
    "gap_split": gap_split,
    "gap_integrated_benchmark": lambda: gap_integrated(True),
    "gap_integrated_no_benchmark": lambda: gap_integrated(False),
}


def codes(state, step=10):
    return set(cs.run_checks(state, step).codes())


# ---------------------------------------------------------------------------
# Valid paths
# ---------------------------------------------------------------------------
class ValidPaths(unittest.TestCase):
    def test_every_path_passes_every_step(self):
        for name, build in ALL_VALID.items():
            for step in range(1, 11):
                with self.subTest(path=name, step=step):
                    report = cs.run_checks(build(), step)
                    self.assertEqual(report.codes(), [], report.render(step))

    def test_no_upper_alignment_declared(self):
        state = swot_fixed()
        state["upper_alignments"] = []
        state["no_upper_alignment"] = True
        state["vision"]["upper_alignments"] = []
        self.assertEqual(codes(state), set())

    def test_goal_patterns(self):
        for pattern, qual, quant in (("integrated", False, False), ("dual", True, True),
                                     ("qualitative", True, False), ("quantitative", False, True)):
            state = swot_fixed()
            state["settings"]["goal_pattern"] = pattern
            for s in state["strategies"]:
                s["qualitative_goal"] = "정성" if qual else ""
                s["quantitative_goal"] = "정량" if quant else None
            with self.subTest(pattern=pattern):
                self.assertEqual(codes(state), set())

    def test_tracks(self):
        for track in ("BSC", "RND", "AUTO", "QUAL"):
            state = swot_fixed()
            state["settings"]["kpi_track"] = track
            with self.subTest(track=track):
                self.assertEqual(codes(state), set())

    def test_rnd_impact_allowed_when_opted_in(self):
        state = swot_fixed()
        state["settings"].update({"kpi_track": "RND", "rnd_include_impact": True})
        state["kpis"][0]["type"] = "Impact"
        self.assertEqual(codes(state), set())

    def test_integer_ids_accepted(self):
        state = swot_fixed()
        for s in state["strategies"]:
            s["id"] = int(s["id"])
        for cv in state["core_values"]:
            cv["strategy"] = int(cv["strategy"])
        self.assertEqual(codes(state), set())

    def test_kpi_none_scope(self):
        state = swot_fixed()
        state["settings"]["kpi_scope"] = "none"
        state["kpis"] = []
        self.assertEqual(codes(state), set())

    def test_gap_note_under_three_issues(self):
        state = gap_split()
        state["issues"] = state["issues"][:2]
        state["issues"][1]["implications"] = ["I2", "I4", "I5"]
        state["gaps"] = state["gaps"][:2]
        state["strategies"][1]["gaps"] = ["G2"]
        state["strategies"][1]["issues"] = ["P2"]
        report = cs.run_checks(state, 10)
        self.assertEqual(report.codes(), [])
        self.assertEqual([c for _, c, _ in report.notes], ["note_gap_issue_count"])


# ---------------------------------------------------------------------------
# Edge cases: one mutation -> exact expected codes
# ---------------------------------------------------------------------------
class Step1Cases(unittest.TestCase):
    def check(self, mutate, expected, build=swot_fixed, step=1):
        state = build()
        mutate(state)
        self.assertEqual(codes(state, step), expected)

    def test_missing_hypothesis_field(self):
        self.check(lambda s: s["hypothesis"].update(time=" "), {"hypothesis_missing"})

    def test_hypothesis_not_object(self):
        self.check(lambda s: s.update(hypothesis="A사"), {"not_object", "hypothesis_missing"})

    def test_no_beneficiary(self):
        self.check(lambda s: s.update(beneficiaries=[]), {"no_beneficiary"})

    def test_upper_alignment_missing(self):
        self.check(lambda s: s.update(upper_alignments=[]), {"upper_alignment_missing"})

    def test_upper_alignment_conflict(self):
        self.check(lambda s: s.update(no_upper_alignment=True), {"upper_alignment_conflict"})

    def test_no_issue(self):
        self.check(lambda s: s.update(issues=[]), {"no_issue"})

    def test_structure_errors(self):
        def mutate(s):
            s["beneficiaries"] = {"id": "B1"}
            s["issues"].append({"text": "id 없음"})
            s["issues"].append({"id": "P1", "text": "중복"})
            s["issues"].append({"id": "P9", "text": " "})
        self.check(mutate, {"not_list", "no_beneficiary", "bad_entry", "duplicate_id", "empty_text"})

    def test_step1_ignores_later_rules(self):
        state = swot_fixed()
        state["facts"].append({"id": "F9", "source": "macro", "text": "미사용 팩트"})
        self.assertEqual(codes(state, 1), set())
        self.assertEqual(codes(state, 5), {"fact_unused"})


class Step5Cases(unittest.TestCase):
    def check(self, mutate, expected, build=swot_fixed):
        state = build()
        mutate(state)
        self.assertEqual(codes(state, 5), expected)

    def test_missing_tool(self):
        self.check(lambda s: s["settings"].pop("analysis_tool"), {"missing_setting"})

    def test_bad_tool(self):
        self.check(lambda s: s["settings"].update(analysis_tool="pest"), {"bad_setting"})

    def test_gap_needs_mode(self):
        self.check(lambda s: s["settings"].pop("gap_mode"), {"missing_setting"}, build=gap_split)

    def test_bad_fact_source(self):
        self.check(lambda s: s["facts"][0].update(source="policy"), {"bad_value"})

    def test_cross_linked_sources(self):
        def mutate(s):
            s["implications"][0]["facts"] = ["F1", "F2"]
            s["implications"][1]["facts"] = ["F1"]
        self.check(mutate, {"mixed_source"})

    def test_fact_really_unused(self):
        self.check(lambda s: s["facts"].append({"id": "F9", "source": "macro", "text": "x"}),
                   {"fact_unused"})

    def test_implication_without_fact(self):
        self.check(lambda s: s["implications"][0].update(facts=[]),
                   {"implication_no_fact", "fact_unused"})

    def test_unknown_fact(self):
        self.check(lambda s: s["implications"][0].update(facts=["F1", "F99"]), {"bad_ref"})

    def test_mixed_source(self):
        self.check(lambda s: s["implications"][2].update(facts=["F3", "F5"]), {"mixed_source"})

    def test_asis_outside_integrated(self):
        self.check(lambda s: s["implications"].append(
            {"id": "A9", "source": "asis", "text": "x", "facts": []}),
            {"asis_not_allowed", "implication_no_fact"})

    def test_integrated_rejects_environment_fact(self):
        self.check(lambda s: s["facts"].append({"id": "F1", "source": "macro", "text": "x"}),
                   {"fact_skipped_step", "fact_unused"}, build=gap_integrated)

    def test_integrated_rejects_internal_implication(self):
        self.check(lambda s: s["implications"].append(
            {"id": "X1", "source": "internal", "text": "x"}),
            {"implication_skipped_step"}, build=gap_integrated)

    def test_no_implication(self):
        self.check(lambda s: s.update(implications=[]), {"no_implication", "fact_unused"})

    def test_facts_field_not_list(self):
        self.check(lambda s: s["implications"][0].update(facts="F1"),
                   {"bad_field", "implication_no_fact", "fact_unused"})


class Step6Cases(unittest.TestCase):
    def check(self, mutate, expected, build=swot_fixed):
        state = build()
        mutate(state)
        self.assertEqual(codes(state, 6), expected)

    # issue induction
    def test_issue_without_implication(self):
        self.check(lambda s: s["issues"][3].update(implications=[]),
                   {"issue_no_implication", "implication_no_issue"})

    def test_implication_without_issue(self):
        self.check(lambda s: s["issues"][0].update(implications=["I1"]), {"implication_no_issue"})

    # SWOT factor sources
    def test_strength_from_environment(self):
        self.check(lambda s: s["swot_factors"][0].update(implications=["I1"]), {"factor_source"})

    def test_opportunity_from_internal(self):
        self.check(lambda s: s["swot_factors"][3].update(implications=["I3"]), {"factor_source"})

    def test_benchmark_allowed_everywhere(self):
        self.check(lambda s: [f.update(implications=f["implications"] + ["I5"])
                              for f in s["swot_factors"]], set())

    def test_factor_without_implication(self):
        self.check(lambda s: s["swot_factors"][0].update(implications=[]),
                   {"factor_no_implication"})

    def test_missing_factor_type(self):
        def mutate(s):
            s["swot_factors"] = [f for f in s["swot_factors"] if f["type"] != "T"]
            for c in s["swot_candidates"]:
                c["factors"] = [x for x in c["factors"] if x != "T1"]
        self.check(mutate, {"factor_type_missing", "candidate_missing_type"})

    def test_bad_factor_type(self):
        self.check(lambda s: s["swot_factors"].append(
            {"id": "X1", "type": "Q", "text": "x", "implications": ["I1"]}), {"bad_value"})

    # SWOT candidate composition and quadrant coverage
    def test_so_uses_weakness(self):
        self.check(lambda s: s["swot_candidates"][0]["factors"].append("W1"),
                   {"candidate_wrong_factor"})

    def test_so_without_opportunity(self):
        self.check(lambda s: s["swot_candidates"][0].update(factors=["S1", "S2"]),
                   {"candidate_missing_type", "quadrant_factor_unused"})

    def test_quadrant_factor_unused(self):
        self.check(lambda s: s["swot_candidates"][1].update(factors=["S1", "T1"]),
                   {"quadrant_factor_unused"})

    def test_bad_quadrant(self):
        def mutate(s):
            s["swot_candidates"][0]["quadrant"] = "SX"
        self.check(mutate, {"bad_value", "quadrant_factor_unused", "fixed_candidate_count",
                            "quadrant_mapping"})

    # fixed mode
    def test_fixed_two_so(self):
        def mutate(s):
            s["swot_candidates"].append({"id": "SO_B", "quadrant": "SO", "text": "x",
                                         "factors": ["S1", "O1"]})
        self.check(mutate, {"fixed_candidate_count"})

    def test_fixed_three_strategies(self):
        def mutate(s):
            s["strategies"] = s["strategies"][:3]
        self.check(mutate, {"fixed_strategy_count", "quadrant_mapping"})

    def test_fixed_two_candidates_on_one_strategy(self):
        def mutate(s):
            s["strategies"][0]["candidates"] = ["SO", "ST"]
        self.check(mutate, {"one_candidate_required", "quadrant_mapping"})

    def test_fixed_duplicate_quadrant(self):
        self.check(lambda s: s["strategies"][3].update(candidates=["WO"]), {"quadrant_mapping"})

    def test_strategy_without_candidate(self):
        self.check(lambda s: s["strategies"][3].update(candidates=[]),
                   {"strategy_no_candidate", "one_candidate_required", "quadrant_mapping"})

    def test_bad_strategy_id(self):
        def mutate(s):
            s["strategies"][3]["id"] = "04"
        self.check(mutate, {"bad_strategy_id"})

    def test_no_strategy(self):
        self.check(lambda s: s.update(strategies=[]),
                   {"no_strategy", "fixed_strategy_count", "quadrant_mapping"})

    def test_bad_followup(self):
        self.check(lambda s: s["settings"].update(fixed_followup="maybe"), {"bad_setting"})

    # flexible options
    def test_as_is_unused_candidate(self):
        self.check(lambda s: s["strategies"].pop(), {"as_is_mapping"},
                   build=lambda: swot_flexible("as_is"))

    def test_as_is_double_use(self):
        self.check(lambda s: s["strategies"][4].update(candidates=["SO1"]), {"as_is_mapping"},
                   build=lambda: swot_flexible("as_is"))

    def test_representative_mixed(self):
        self.check(lambda s: s["strategies"][0]["candidates"].append("ST1"),
                   {"representative_mixed", "quadrant_mapping"},
                   build=lambda: swot_flexible("representative"))

    def test_representative_incomplete(self):
        self.check(lambda s: s["strategies"][0].update(candidates=["SO1"]),
                   {"representative_incomplete"}, build=lambda: swot_flexible("representative"))

    def test_representative_count(self):
        self.check(lambda s: s["strategies"].pop(), {"representative_count", "quadrant_mapping"},
                   build=lambda: swot_flexible("representative"))

    def test_cross_factor_unused(self):
        # strategy 2 is the only one carrying S2 (through SO2 and ST1)
        self.check(lambda s: s["strategies"].pop(1), {"cross_factor_unused"},
                   build=lambda: swot_flexible("cross"))

    def test_cross_redundant_strategy_removed(self):
        # W1 and T1 stay covered by strategies 1 and 2, so dropping 3 is valid
        self.check(lambda s: s["strategies"].pop(), set(), build=lambda: swot_flexible("cross"))

    def test_flexible_needs_option(self):
        self.check(lambda s: s["settings"].pop("flexible_option"), {"missing_setting"},
                   build=lambda: swot_flexible("cross"))

    # issue-linked mode
    def test_issue_linked_count(self):
        self.check(lambda s: s["strategies"].pop(),
                   {"issue_linked_count", "issue_linked_one_strategy"}, build=swot_issue_linked)

    def test_issue_linked_two_issues(self):
        self.check(lambda s: s["strategies"][0].update(issues=["P1", "P2"]),
                   {"issue_linked_one_issue", "issue_linked_one_strategy"},
                   build=swot_issue_linked)

    # gap path
    def test_gap_bad_issue(self):
        self.check(lambda s: s["gaps"][0].update(issue="P9"), {"bad_ref", "issue_no_gap"},
                   build=gap_split)

    def test_gap_missing_issue_field(self):
        self.check(lambda s: s["gaps"][0].pop("issue"), {"empty_text", "issue_no_gap"},
                   build=gap_split)

    def test_gap_missing_tobe(self):
        self.check(lambda s: s["gaps"][0].update(tobe=""), {"gap_missing_state"}, build=gap_split)

    def test_issue_without_gap(self):
        self.check(lambda s: s["gaps"].pop(), {"issue_no_gap", "bad_ref"}, build=gap_split)

    def test_gap_without_strategy(self):
        self.check(lambda s: s["strategies"][1].update(gaps=["G2"]), {"gap_no_strategy"},
                   build=gap_split)

    def test_strategy_without_gap(self):
        self.check(lambda s: s["strategies"][0].update(gaps=[]),
                   {"strategy_no_gap", "gap_no_strategy"}, build=gap_split)


class Step7Cases(unittest.TestCase):
    def check(self, mutate, expected, build=swot_fixed):
        state = build()
        mutate(state)
        self.assertEqual(codes(state, 7), expected)

    def test_no_vision_text(self):
        self.check(lambda s: s["vision"].update(text=""), {"no_vision"})

    def test_mission_not_object(self):
        self.check(lambda s: s.update(mission="미션"),
                   {"not_object", "no_mission", "mission_no_beneficiary"})

    def test_vision_without_upper(self):
        self.check(lambda s: s["vision"].update(upper_alignments=[]), {"vision_no_upper"})

    def test_vision_unknown_upper(self):
        self.check(lambda s: s["vision"].update(upper_alignments=["U9"]),
                   {"bad_ref", "vision_no_upper"})

    def test_mission_without_beneficiary(self):
        self.check(lambda s: s["mission"].update(beneficiaries=[]), {"mission_no_beneficiary"})

    def test_strategy_without_core_value(self):
        self.check(lambda s: s["core_values"].pop(), {"strategy_no_cv"})

    def test_strategy_with_two_core_values(self):
        self.check(lambda s: s["core_values"].append({"id": "CVX", "text": "x", "strategy": "1"}),
                   {"strategy_multi_cv"})

    def test_core_value_unknown_strategy(self):
        self.check(lambda s: s["core_values"][0].update(strategy="9"),
                   {"bad_ref", "strategy_no_cv"})

    def test_core_value_without_strategy(self):
        self.check(lambda s: s["core_values"][0].pop("strategy"),
                   {"cv_no_strategy", "strategy_no_cv"})


class Step8Cases(unittest.TestCase):
    def check(self, mutate, expected, build=swot_fixed):
        state = build()
        mutate(state)
        self.assertEqual(codes(state, 8), expected)

    def test_strategy_without_issue(self):
        self.check(lambda s: s["strategies"][3].update(issues=[]),
                   {"strategy_no_issue", "issue_no_strategy"})

    def test_issue_without_strategy(self):
        self.check(lambda s: s["strategies"][3].update(issues=["P1"]), {"issue_no_strategy"})

    def test_unknown_issue(self):
        self.check(lambda s: s["strategies"][3]["issues"].append("P9"), {"bad_ref"})

    def test_gap_shared_by_two_strategies(self):
        def mutate(s):
            s["strategies"][1]["issues"] = ["P2", "P3", "P1"]
            s["strategies"][1]["gaps"] = ["G1", "G2", "G3"]
        self.check(mutate, set(), build=gap_split)

    def test_gap_issue_mismatch(self):
        self.check(lambda s: s["strategies"][1].update(issues=["P2"]),
                   {"gap_issue_mismatch", "issue_no_strategy"}, build=gap_split)

    def test_goal_dual_missing_quant(self):
        self.check(lambda s: s["strategies"][0].update(quantitative_goal=""), {"goal_required"})

    def test_goal_qualitative_forbids_quant(self):
        self.check(lambda s: s["settings"].update(goal_pattern="qualitative"), {"goal_forbidden"})

    def test_goal_integrated_forbids_both(self):
        self.check(lambda s: s["settings"].update(goal_pattern="integrated"), {"goal_forbidden"})

    def test_goal_quantitative_needs_quant(self):
        def mutate(s):
            s["settings"]["goal_pattern"] = "quantitative"
            for st in s["strategies"]:
                st["qualitative_goal"] = ""
            s["strategies"][0]["quantitative_goal"] = None
        self.check(mutate, {"goal_required"})

    def test_quant_goal_list(self):
        self.check(lambda s: s["strategies"][0].update(quantitative_goal=["90%", "80%"]),
                   {"quant_goal_single", "goal_required"})

    def test_missing_goal_pattern(self):
        self.check(lambda s: s["settings"].pop("goal_pattern"), {"missing_setting"})

    def test_bad_task_ids(self):
        for bad in ("1", "1-0", "01-1", "1-1-1", "1.1"):
            with self.subTest(bad=bad):
                self.check(lambda s: s["strategic_tasks"].append({"id": bad, "text": "x"}),
                           {"bad_task_id"})

    def test_task_without_parent(self):
        self.check(lambda s: s["strategic_tasks"].append({"id": "9-1", "text": "x"}),
                   {"task_no_parent"})

    def test_strategy_without_task(self):
        self.check(lambda s: s.update(strategic_tasks=[t for t in s["strategic_tasks"]
                                                       if not t["id"].startswith("4-")]),
                   {"strategy_no_task"})

    def test_representative_task_missing(self):
        self.check(lambda s: s["strategic_tasks"][1].pop("candidate"),
                   {"representative_task_mapping"}, build=lambda: swot_flexible("representative"))

    def test_representative_task_duplicate(self):
        self.check(lambda s: s["strategic_tasks"][1].update(candidate="SO1"),
                   {"representative_task_mapping"}, build=lambda: swot_flexible("representative"))

    def test_representative_task_foreign_candidate(self):
        self.check(lambda s: s["strategic_tasks"][1].update(candidate="WT1"),
                   {"task_candidate_mismatch", "representative_task_mapping"},
                   build=lambda: swot_flexible("representative"))


class Step9Cases(unittest.TestCase):
    def check(self, mutate, expected, build=swot_fixed):
        state = build()
        mutate(state)
        self.assertEqual(codes(state, 9), expected)

    def test_disabled_but_present(self):
        self.check(lambda s: s["settings"].update(implementation_tasks=False), {"impl_disabled"})

    def test_bad_impl_id(self):
        self.check(lambda s: s["implementation_tasks"].append({"id": "1-1", "text": "x"}),
                   {"bad_impl_id"})

    def test_impl_without_parent(self):
        self.check(lambda s: s["implementation_tasks"].append({"id": "1-9-1", "text": "x"}),
                   {"impl_no_parent"})

    def test_task_without_impl(self):
        self.check(lambda s: s.update(implementation_tasks=[i for i in s["implementation_tasks"]
                                                            if not i["id"].startswith("4-1-")]),
                   {"task_no_impl"})

    def test_self_precedes(self):
        self.check(lambda s: s["implementation_tasks"][0]["precedes"].append("1-1-1"),
                   {"self_precedes"})

    def test_two_node_cycle(self):
        self.check(lambda s: s["implementation_tasks"][1]["precedes"].append("1-1-1"),
                   {"precedes_cycle"})

    def test_three_node_cycle(self):
        def mutate(s):
            by_id = {i["id"]: i for i in s["implementation_tasks"]}
            by_id["3-1-1"]["precedes"].append("1-1-1")
        self.check(mutate, {"precedes_cycle"})

    def test_cycle_in_second_component(self):
        def mutate(s):
            by_id = {i["id"]: i for i in s["implementation_tasks"]}
            by_id["2-1-1"]["precedes"].append("4-1-1")
            by_id["4-1-1"]["precedes"].append("2-1-1")
        self.check(mutate, {"precedes_cycle"})

    def test_unknown_precedes(self):
        self.check(lambda s: s["implementation_tasks"][0]["precedes"].append("9-9-9"), {"bad_ref"})


class Step10Cases(unittest.TestCase):
    def check(self, mutate, expected, build=swot_fixed):
        state = build()
        mutate(state)
        self.assertEqual(codes(state, 10), expected)

    def test_disabled_but_present(self):
        self.check(lambda s: s["settings"].update(kpi_scope="none"), {"kpi_disabled"})

    def test_all_scope_without_impl(self):
        def mutate(s):
            s["settings"]["implementation_tasks"] = False
            s["implementation_tasks"] = []
            s["kpis"] = [k for k in s["kpis"] if k["id"].count("-") < 4]
        self.check(mutate, {"scope_needs_impl"})

    def test_lower_scope_without_impl(self):
        self.check(lambda s: s["settings"].update(implementation_tasks=False),
                   {"scope_needs_impl", "impl_disabled"},
                   build=lambda: gap_integrated(True))

    def test_gov_needs_dual(self):
        self.check(lambda s: s["settings"].update(goal_pattern="qualitative") or
                   [st.update(quantitative_goal="") for st in s["strategies"]],
                   {"gov_needs_dual"}, build=gap_split)

    def test_bad_kpi_ids(self):
        for bad in ("KPI-1", "1-KPI-0", "1-1-1-1-KPI-1", "1-kpi-1", "S1-KPI-1"):
            with self.subTest(bad=bad):
                self.check(lambda s: s["kpis"].append({"id": bad, "text": "x", "type": "Output"}),
                           {"bad_kpi_id"})

    def test_kpi_target_missing(self):
        self.check(lambda s: s["kpis"].append({"id": "9-KPI-1", "text": "x", "type": "Outcome"}),
                   {"kpi_no_target"})

    def test_kpi_outside_scope(self):
        self.check(lambda s: s["kpis"].append({"id": "1-1-KPI-1", "text": "x", "type": "Output"}),
                   {"kpi_level_scope"}, build=gap_split)

    def test_bad_kpi_type(self):
        self.check(lambda s: s["kpis"][0].update(type="Result"), {"bad_value"})

    def test_rnd_impact_default(self):
        def mutate(s):
            s["settings"]["kpi_track"] = "RND"
            s["kpis"][0]["type"] = "Impact"
        self.check(mutate, {"rnd_impact"})

    def test_missing_track(self):
        self.check(lambda s: s["settings"].pop("kpi_track"), {"missing_setting"})

    def test_missing_scope(self):
        self.check(lambda s: s["settings"].pop("kpi_scope"), {"missing_setting"})

    def test_element_without_kpi(self):
        for level, prefix in (("strategy", "4-KPI"), ("task", "4-1-KPI"), ("impl", "4-1-1-KPI")):
            with self.subTest(level=level):
                def mutate(s, prefix=prefix):
                    s["kpis"] = [k for k in s["kpis"] if not k["id"].startswith(prefix)]
                expected = {"element_no_kpi"}
                if level != "impl":
                    # the child KPI now points at a deleted KPI
                    expected.add("bad_ref")
                self.check(mutate, expected)

    def test_strategy_kpi_contributes(self):
        self.check(lambda s: s["kpis"][0].update(contributes_to="2-KPI-1"),
                   {"strategy_kpi_contrib"})

    def test_task_kpi_without_contrib(self):
        def mutate(s):
            for k in s["kpis"]:
                if k["id"] == "1-1-KPI-1":
                    k["contributes_to"] = None
        self.check(mutate, {"kpi_contrib_missing"})

    def test_task_kpi_wrong_parent(self):
        def mutate(s):
            for k in s["kpis"]:
                if k["id"] == "1-1-KPI-1":
                    k["contributes_to"] = "2-KPI-1"
        self.check(mutate, {"kpi_contrib_wrong_parent"})

    def test_impl_kpi_skipping_level(self):
        def mutate(s):
            for k in s["kpis"]:
                if k["id"] == "1-1-1-KPI-1":
                    k["contributes_to"] = "1-KPI-1"
        self.check(mutate, {"kpi_contrib_wrong_parent"})

    def test_unknown_contrib(self):
        def mutate(s):
            for k in s["kpis"]:
                if k["id"] == "1-1-KPI-1":
                    k["contributes_to"] = "1-KPI-9"
        self.check(mutate, {"bad_ref"})


class Regression(unittest.TestCase):
    def test_later_step_catches_earlier_break(self):
        state = swot_fixed()
        state["swot_candidates"][0]["factors"].append("W1")
        self.assertIn("candidate_wrong_factor", codes(state, 10))

    def test_settings_reported_once(self):
        state = swot_fixed()
        state["settings"]["analysis_tool"] = None
        report = cs.run_checks(state, 10)
        self.assertEqual(report.codes().count("missing_setting"), 1)

    def test_state_not_object(self):
        self.assertEqual(cs.run_checks([], 10).codes(), ["not_object"])


class Cli(unittest.TestCase):
    def run_cli(self, *args, state=None):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "state.json")
            if state is not None:
                with open(path, "w", encoding="utf-8") as handle:
                    if isinstance(state, str):
                        handle.write(state)
                    else:
                        json.dump(state, handle, ensure_ascii=False)
            cmd = [sys.executable, SCRIPT] + ([path] if state is not None else []) + list(args)
            return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    def test_pass_exit_zero(self):
        result = self.run_cli("--step", "all", "--lang", "en", state=swot_fixed())
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("Result: PASS", result.stdout)

    def test_fail_exit_one_korean(self):
        state = swot_fixed()
        state["strategies"][0]["issues"] = []
        result = self.run_cli("--step", "8", "--lang", "ko", state=state)
        self.assertEqual(result.returncode, 1)
        self.assertIn("[8단계] 해결 문제이슈 없는 전략: 1", result.stdout)
        self.assertIn("결과: 위반", result.stdout)

    def test_bad_json_exit_two(self):
        result = self.run_cli(state="{not json")
        self.assertEqual(result.returncode, 2)

    def test_template_roundtrip(self):
        result = self.run_cli("--template")
        template = json.loads(result.stdout)
        self.assertEqual(set(template), set(cs.TEMPLATE))
        report = cs.run_checks(template, 10)
        self.assertNotIn("not_list", report.codes())
        self.assertNotIn("bad_entry", report.codes())

    def test_chart_output(self):
        result = self.run_cli("--chart", state=swot_fixed())
        out = result.stdout
        self.assertIn("%% trace", out)
        self.assertIn("%% vision house", out)
        self.assertIn('S_1["1. 저탄소 품질 성장"]', out)
        self.assertIn("P_P1 --> S_1", out)
        self.assertIn("S_1 --> T_1_2d_1", out)
        self.assertIn("T_1_2d_1 --> M_1_2d_1_2d_1", out)
        self.assertIn("CV_CV1 --> S_1", out)
        self.assertIn("U_U1 --> V_V", out)

    def test_chart_korean_ids_do_not_collide(self):
        a = cs._node_id("F", "강점1")
        b = cs._node_id("F", "약점1")
        self.assertNotEqual(a, b)
        self.assertTrue(a.isascii())
        self.assertNotEqual(cs._node_id("T", "1-1"), cs._node_id("T", "1_1"))

    def test_bad_step_value(self):
        result = self.run_cli("--step", "11", state=swot_fixed())
        self.assertEqual(result.returncode, 2)


def partial_state(full, step):
    """Keep only what exists right after `step` in a real session."""
    st = copy.deepcopy(full)
    settings = st["settings"]
    if step < 10:
        st["kpis"] = []
        for key in ("kpi_scope", "kpi_track", "rnd_include_impact"):
            settings.pop(key, None)
    if step < 9:
        st["implementation_tasks"] = []
        settings.pop("implementation_tasks", None)
    if step < 8:
        st["strategic_tasks"] = []
        settings.pop("goal_pattern", None)
        for strategy in st.get("strategies", []):
            strategy.pop("qualitative_goal", None)
            strategy.pop("quantitative_goal", None)
            if settings.get("swot_mode") == "fixed":
                strategy.pop("issues", None)   # fixed Y links issues by step 8
    if step < 7:
        st["vision"] = {"text": "", "upper_alignments": []}
        st["mission"] = {"text": "", "beneficiaries": []}
        st["core_values"] = []
    if step < 6:
        for key in ("swot_factors", "swot_candidates", "gaps", "strategies"):
            st[key] = []
        for key in ("swot_mode", "fixed_followup", "flexible_option"):
            settings.pop(key, None)
        for issue in st["issues"]:
            issue["implications"] = []        # still drafts
    if step < 5:
        st["facts"], st["implications"] = [], []
        settings.pop("analysis_tool", None)
        settings.pop("gap_mode", None)
    return st


class ProgressiveSession(unittest.TestCase):
    def test_each_step_passes_with_only_its_own_data(self):
        for name, build in ALL_VALID.items():
            full = build()
            for step in (1, 5, 6, 7, 8, 9, 10):
                if step == 9 and not full["settings"].get("implementation_tasks"):
                    continue
                with self.subTest(path=name, step=step):
                    report = cs.run_checks(partial_state(full, step), step)
                    self.assertEqual(report.codes(), [], report.render(step))


class SchemaConsistency(unittest.TestCase):
    def test_schema_covers_template(self):
        field_keys = {row[0] for row in cs.SCHEMA_FIELDS}
        template_keys = set(cs.TEMPLATE) - {"no_upper_alignment"}
        self.assertEqual(field_keys, template_keys)
        option_keys = {row[0] for row in cs.SCHEMA_OPTIONS}
        self.assertEqual(option_keys, set(cs.TEMPLATE["settings"]))

    def test_schema_prints_both_languages(self):
        for lang in ("ko", "en"):
            text = cs.schema_text(lang)
            for key in cs.TEMPLATE["settings"]:
                self.assertIn(key, text)

    def test_every_message_has_both_languages(self):
        for code, pair in cs.MESSAGES.items():
            self.assertEqual(len(pair), 2, code)
            self.assertTrue(all(pair), code)


if __name__ == "__main__":
    unittest.main(verbosity=1)
