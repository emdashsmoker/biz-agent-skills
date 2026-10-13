# check 함수와 프리셋

## 기본 실행 패턴

```python
import sys
sys.path.insert(0, "path/to/ontology-modeling/scripts")  # 스킬 폴더의 scripts 경로
from onto_engine import *

world, onto = create_world()
# TBox와 ABox 구축

result = run_full_analysis(world, onto)                   # Python 점검
result = run_full_analysis(world, onto, use_hermit=True)  # Python 점검 뒤 추론기
paths = save_all_outputs(world, onto, base_name="analysis")  # OWL, Mermaid 2종, 보고서
```

save_all_outputs는 기본으로 작업 폴더 아래 outputs 폴더에 저장한다. output_dir 인자로 위치를 바꿀 수 있다.

## 이름에 기대는 함수

아래 함수는 클래스명이나 속성명을 고정해서 찾는다. 온톨로지의 이름이 다르면 결과가 비어 나오므로, 이름을 맞추거나 인자를 받는 다른 함수(check_provenance, check_coverage 등)를 쓴다.

| 함수 | 찾는 이름 |
|---|---|
| check_unsupported_assumptions | Assumption 클래스, supported_by 속성 |
| check_process_completeness | precedes 속성 |
| check_causal_chain | causes 속성 |
| check_constraint_conflicts | 이름에 goal 또는 objective가 든 속성과 risk 또는 constraint가 든 속성의 쌍 |
| check_assumption_impact | 기본값 attached_to, precedes 속성 (인자로 변경 가능), 이름에 output 또는 produces가 든 산출물 속성 |
| auto_route_advanced_checks | 아래 자동 라우팅 표의 키워드 |

## SPARQL 기반 점검 (15개)

모든 check 함수의 첫 인자는 world, 둘째 인자는 onto다. 내부에서 run_sparql_check로 내장 쿼리를 실행한다.

| 함수 | 내장 쿼리 | 하는 일 |
|---|---|---|
| check_mece(world, onto, parent) | mece_overlap | 하위 클래스 쌍마다 겹치는 개체와 어느 하위 클래스에도 속하지 않는 개체를 찾는다 |
| check_causal_chain(world, onto) | edges | causes 연결을 따라 원인이 없는 개체에서 시작하는 모든 경로를 뽑는다. 분기는 별도 경로로 나온다 |
| check_constraint_conflicts(world, onto) | conflict_dual_ref | 목표 계열 속성과 위험 계열 속성이 같은 대상을 가리키는 개체를 찾는다 |
| check_unsupported_assumptions(world, onto) | unsupported | 근거가 연결되지 않은 가정을 찾는다 |
| check_process_completeness(world, onto) | edges | precedes 연결의 시작 단계, 끝 단계, 시작에서 도달하지 못하는 단계를 찾는다 |
| check_coverage(world, onto, source, referencing, prop) | coverage | 참조 클래스의 어떤 개체도 가리키지 않는 개체를 찾는다 |
| check_cardinality(world, onto, cls, prop, expected) | cardinality_count | 연결 수가 기대값과 다른 개체를 찾는다. 연결이 없으면 0으로 센다 |
| check_provenance(world, onto, classes, prop) | unsupported | 지정 속성 값이 없는 개체를 찾는다 |
| check_shared_reference(world, onto, classes, prop) | refs_for_class | 여러 클래스가 같은 속성으로 참조하는 대상 집합을 비교한다 |
| check_value_range(world, onto, cls, prop, min_val, max_val, range_rules) | value_below, value_above | 값이 범위를 벗어난 개체를 찾는다. range_rules로 클래스마다 범위를 다르게 준다 |
| check_bidirectional_coverage(world, onto, a, b, a_to_b, b_to_a) | unsupported, coverage | A 쪽에서 연결이 없는 개체와 B 쪽에서 참조받지 못한 개체를 함께 찾는다 |
| check_reverse_chain(world, onto, effect, cause_prop, max_depth) | 개체 순회 | 결과에서 원인을 거슬러 올라가며 모든 분기를 추적한다. chains, roots, has_cycle을 돌려준다 |
| check_mandatory_outputs(world, onto, stage_cls, output_prop, required) | mandatory_missing | 필수 산출물 클래스가 없는 단계를 찾는다 |
| check_assumption_impact(world, onto, assumption, attached, order) | downstream | 가정이 붙은 단계에서 뒤쪽 단계와 산출물로 영향 범위를 산출한다 |
| check_pipeline_trace(world, onto, stage_chain) | stage_unlinked | 단계 클래스마다 다음 단계와 연결되지 않은 개체를 찾는다 |

## Python 전용 점검 (3개)

허용 조합 규칙이나 단계별 규칙은 SPARQL 한 줄로 표현하기 어려워 Python으로 점검한다.

### check_cross_mapping(onto, subject_classes, property_name, target_class_set)

유형마다 참조할 수 있는 대상 유형이 정해진 규칙을 점검한다. subject_classes는 {"유형명": {"allowed": {"허용 대상1", "허용 대상2"}}} 형태다.

```python
violations = check_cross_mapping(onto,
    {"Strategy": {"allowed": {"Strength", "Opportunity"}}},
    "uses_factor",
    {"Strength", "Weakness", "Opportunity"})
```

### check_mapping_chain(world, onto, chain_rules)

A에서 B, B에서 C로 이어지는 대응을 단계마다 점검하고 처음 어긋난 단계를 알려 준다. allowed와 target_types가 있는 단계는 허용 조합을, 없는 단계는 연결 존재 여부를 점검한다.

```python
result = check_mapping_chain(world, onto, [
    {"from_class": "Category", "to_class": "Field",
     "link_property": "maps_to",
     "allowed": {"Category": {"allowed": {"Field"}}},
     "target_types": {"Field"}},
    {"from_class": "Field", "to_class": "Item",
     "link_property": "selects_item"},
])
```

### check_conditional_branch(onto, condition_class, condition_property, branch_rules, stage_property)

조건값마다 반드시 있어야 하는 단계와 없어야 하는 단계를 규칙으로 정하고 실제 단계 구성과 비교한다.

```python
violations = check_conditional_branch(onto,
    "Project", "project_type",
    {"type_a": {"required": ["Step"], "excluded": ["Activity"]}},
    "has_step")
```

## 프리셋 (7개)

구조 패턴을 알아보면 프리셋으로 관련 점검을 한 번에 실행한다. 모든 프리셋의 첫 두 인자는 world, onto다.

| 프리셋 | 포함 점검 | 맞는 구조 |
|---|---|---|
| run_preset_cross_factor | check_cross_mapping, check_provenance, check_cardinality | 유형마다 참조할 수 있는 요인이 정해진 구조 |
| run_preset_multi_axis | check_coverage, check_shared_reference | 여러 평가 기준의 결과가 종합 판정으로 모이는 구조 |
| run_preset_regulated_procedure | check_pipeline_trace, check_mandatory_outputs | 순서와 필수 산출물이 정해진 절차 |
| run_preset_causal | check_causal_chain, check_unsupported_assumptions, check_reverse_chain | 원인과 결과의 연쇄 |
| run_preset_logic_model | check_pipeline_trace, check_bidirectional_coverage, check_unsupported_assumptions, check_provenance | 투입, 활동, 산출, 성과로 이어지는 구조 |
| run_preset_mapping_chain | check_mapping_chain, check_bidirectional_coverage | 다단계 분류 대응 |
| run_preset_decision_tree | check_conditional_branch, check_provenance | 조건에 따라 갈리는 절차 |

```python
# 인과 분석
result = run_preset_causal(world, onto,
    effect_name="funding_gap", cause_property="caused_by")

# 유형별 허용 요인
result = run_preset_cross_factor(world, onto,
    rules={"Strategy": {"allowed": {"Strength", "Opportunity"}}},
    factor_property="uses_factor",
    factor_types={"Strength", "Weakness", "Opportunity"},
    source_property="achieves",
    source_classes=["Strategy"],
    cardinality_property="uses_factor",
    expected_count=2)

# 순서가 정해진 절차
result = run_preset_regulated_procedure(world, onto,
    stage_chain=[{"class": "Step", "link_to_next": "precedes"},
                 {"class": "Step"}],
    output_property="produces",
    mandatory_map={"Step": ["MandatoryOutput"]})

# 다단계 분류 대응
result = run_preset_mapping_chain(world, onto,
    chain_rules=[
        {"from_class": "Category", "to_class": "Field",
         "link_property": "maps_to",
         "allowed": {"Category": {"allowed": {"Field"}}},
         "target_types": {"Field"}},
        {"from_class": "Field", "to_class": "Item",
         "link_property": "selects_item"},
    ],
    bidirectional_pairs=[("Category", "Field", "maps_to")])

# 조건 분기
result = run_preset_decision_tree(world, onto,
    condition_class="Project",
    condition_property="project_type",
    branch_rules={
        "type_a": {"required": ["StepX", "StepY"], "excluded": ["StepZ"]},
        "type_b": {"required": ["StepZ"], "excluded": ["StepX"]},
    },
    stage_property="has_step",
    prerequisite_property="requires_prerequisite")

# 논리모형
result = run_preset_logic_model(world, onto,
    stage_chain=[{"class": "Activity", "link_to_next": "precedes"}],
    objective_class="Goal", activity_class="Strategy",
    obj_to_act_property="achieves",
    indicator_property="has_indicator", indicator_classes=["Objective"])

# 다축 평가
result = run_preset_multi_axis(world, onto,
    axis_classes=["AxisA", "AxisB"],
    result_property="produces",
    comprehensive_class="FinalEvaluation",
    intake_property="uses_result",
    shared_ref_property="references")
```

## 자동 라우팅 규칙

auto_route_advanced_checks는 이름을 보고 적용할 점검을 고른다. 이름에 기대므로 결과를 실행 전에 검토한다.

| 조건 | 권고 점검 | 구분 |
|---|---|---|
| 속성명이 precedes, follows, leads_to, next_stage, before, after이거나 전이 속성이 있다 | pipeline_trace | 필수 |
| 속성명에 supported_by, evidence, based_on, justified_by, grounded_in이 들어 있다 | provenance | 필수 |
| 속성명에 causes, caused_by, results_in, leads_to_effect가 들어 있다 | causal_chain, reverse_chain | 필수 |
| 클래스명에 assumption이나 premise가 들어 있다 | unsupported_assumptions | 필수 |
| 가정 클래스와 순서 속성이 함께 있다 | assumption_impact | 권장 |
| 같은 domain과 range를 가진 객체 속성이 둘 이상이다 | bidirectional_coverage | 필수 |
| domain이 있는 객체 속성이 있다 | cardinality | 권장 |
| 한 클래스를 둘 이상의 속성이 range로 참조한다 | shared_reference | 권장 |
| 클래스명에 mandatory, required, output, deliverable이 들어 있고 순서 속성이 있다 | mandatory_outputs | 권장 |
| provenance_note 속성이 있다 | provenance | 필수 |
| 하위 클래스가 2개 이상인 클래스가 있다 | mece | 권장 |

## 구조 패턴

공리를 설계하거나 자동 라우팅 결과를 해석할 때 참고하는 범용 구조 패턴이다.

| 패턴 | 구조 | 관련 공리 | 알아보는 단서 |
|---|---|---|---|
| 상호 배타 분류 | 하위 유형에 동시에 속할 수 없다 | DisjointClasses | 같은 상위 클래스 아래 하위 클래스가 2개 이상 |
| 순차 의존 연쇄 | 앞 단계 산출물이 뒤 단계 입력이 된다 | MinCardinality (뒤 단계 연결 요건 기록), 단절은 check_pipeline_trace로 점검 | precedes, follows 같은 순서 속성 |
| 허용 조합 제약 | 유형마다 참조할 수 있는 대상이 정해져 있다 | EquivalentClass (허용 조합) | 유형별 허용 대상이 명시적으로 나열됨 |
| 필수 연결 | 모든 X가 Y와 1개 이상 연결되어야 한다 | MinCardinality (요건 기록), SPARQL 점검 | 도메인 논리상 반드시 필요한 관계 |
| 미연결 상태가 곧 문제 | 연결이 없으면 문제 상태다 | EquivalentClass의 Not 조건 (close_world_scope 뒤 판정) | 연결 부재를 문제로 인식하는 도메인 |
| 명시 대상과 실제 대상의 비교 | 명시한 수혜 대상과 실제 수혜 대상이 다를 수 있다 | 두 속성 값의 비교. OWL 클래스 공리로는 같은 개체의 두 속성 값을 직접 비교할 수 없으므로 SPARQL 패턴 비교나 DL-safe SWRL 규칙을 쓴다 | 수혜자 관련 속성이 2종 이상 |

## 다른 분석 결과를 온톨로지로 옮기기

분류표, 절차, 규칙 목록 같은 다른 분석 결과를 입력으로 받으면 아래 대응으로 TBox를 설계한다.

| 분석 결과의 요소 | 온톨로지 요소 | 구조 패턴 |
|---|---|---|
| 서로 겹치지 않는 유형 분류 | 하위 클래스와 DisjointClasses | 상호 배타 분류 |
| 순서가 있는 단계 | 개체와 precedes 속성 | 순차 의존 연쇄 |
| 유형별 허용 조합 규칙 | 참조 속성, check_cross_mapping 규칙, EquivalentClass | 허용 조합 제약 |
| 반드시 있어야 하는 관계 | MinCardinality와 SPARQL 점검 | 필수 연결 |
| 연결이 없으면 문제인 상태 | Not 조건 EquivalentClass | 미연결 상태가 곧 문제 |
| 명시 대상과 실제 대상 | 두 속성과 비교 질의 | 명시 대상과 실제 대상의 비교 |

옮기는 순서는 다음과 같다.

- 분석 결과의 구조를 파악해 위 대응에 따라 TBox 설계안을 만들고 사용자와 합의한다
- 분석 결과의 항목을 ABox 개체로 입력한다
- 해석이 들어간 속성은 set_with_provenance로 근거를 함께 기록한다
- auto_route_advanced_checks로 적용할 점검을 확인한 뒤 실행한다
