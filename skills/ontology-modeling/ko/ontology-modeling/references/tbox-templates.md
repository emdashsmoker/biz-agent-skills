# 도메인 TBox 템플릿

아래 템플릿은 TBox 구축의 출발점이다. 특정 방법론을 강제하지 않으며 사용자가 정의한 구조가 우선한다. 클래스명, 속성명, 계층은 사용자의 용어와 방법론에 맞게 바꾼다.

각 템플릿의 axioms 항목은 추론기를 쓸 때 구축할 수 있는 기본 공리 세트다. 골라서 적용하거나 지우고 바꿀 수 있다. 공리를 적용하지 않아도 check 함수와 SPARQL 점검은 그대로 동작한다.

## 템플릿 공통 사항

- 템플릿의 dict는 설계안을 적는 표기다. 실제 구축은 build_class, build_object_property, build_data_property로 한다
- "transitive": True는 build_object_property의 is_transitive=True, "functional": True는 is_functional=True에 대응한다
- 전이 속성(transitive)은 domain과 range가 같은 클래스일 때만 쓴다. 둘이 다르면 연쇄 중간의 개체가 두 클래스에 동시에 속한다고 추론되고, 두 클래스가 상호 배타이면 온톨로지 전체가 모순이 된다
- owl_pattern은 사람이 읽는 표기다. 코드로는 `&`, `Not(...)`, `prop.some(Class)`, `Inverse(prop)`로 옮긴다
- owl_pattern에 NOT이 들어간 자동 분류는 개방 세계 가정 때문에 입력만으로는 판정되지 않는다. 먼저 SPARQL 점검으로 해당 개체를 미입력 후보로 찾고, 사용자가 해당 범위의 입력이 완전하다고 확인하면 close_world_scope를 실행한 뒤 추론기로 판정한다
- min_cardinality 공리도 빠진 연결을 위반으로 잡지 못한다. 빠진 연결은 check_provenance나 SPARQL의 unsupported 쿼리로 찾는다

```python
from owlready2 import Not, Inverse
# "Assumption & NOT(supported_by.some(Evidence))"
build_equivalent_class(onto, "UnsupportedAssumption",
    onto["Assumption"] & Not(onto["supported_by"].some(onto["Evidence"])))
# "Objective & NOT(INVERSE(achieves).some(Strategy))"
build_equivalent_class(onto, "OrphanObjective",
    onto["Objective"] & Not(Inverse(onto["achieves"]).some(onto["Strategy"])))
```

## 1. 정책 분석 (policy_analysis)

```python
classes = {
    "Policy": None,
    "EconomicPolicy": "Policy",
    "SocialPolicy": "Policy",
    "RegulatoryPolicy": "Policy",
    "Stakeholder": None,
    "Goal": None,
    "Risk": None,
    "Constraint": None,
}

object_properties = {
    "affects":         {"domain": "Policy", "range": "Stakeholder"},
    "implemented_by":  {"domain": "Policy", "range": "Stakeholder", "functional": True},
    "has_goal":        {"domain": "Policy", "range": "Goal"},
    "has_risk":        {"domain": "Policy", "range": "Risk"},
    "conflicts_with":  {"domain": "Policy", "range": "Policy"},
    "constrained_by":  {"domain": "Policy", "range": "Constraint"},
    "mitigates":       {"domain": "Policy", "range": "Risk"},
}

data_properties = {
    "priority_level":  {"domain": "Policy", "range": "int", "functional": True},
    "rationale":       {"domain": "Policy", "range": "str"},
}
```

점검 규칙:

- (겹침과 빠짐) Policy의 하위 분류
- (목표와 위험의 충돌) has_goal과 has_risk가 같은 대상을 가리키는지 확인한다. check_constraint_conflicts가 속성명의 goal, risk 키워드로 이 쌍을 찾는다
- (이해관계자 영향) affects 관계를 SPARQL로 조회한다

```python
axioms = {
    "disjoint_groups": [
        ["EconomicPolicy", "SocialPolicy", "RegulatoryPolicy"]  # 정책 유형은 서로 겹치지 않음
    ],
    "min_cardinality": [
        {"class": "Policy", "property": "has_goal", "min": 1, "range_class": "Goal"},
        {"class": "Policy", "property": "affects", "min": 1, "range_class": "Stakeholder"},
    ],
    "equivalent_classes": [
        {"name": "UnmitigatedRiskPolicy", "base_class": "Policy",
         "condition": "위험(Risk)이 있으나 완화 수단(mitigates)이 연결되지 않은 정책",
         "owl_pattern": "Policy & has_risk.some(Risk) & NOT(mitigates.some(Risk))"},
    ],
}
```

## 2. 기획 논리 점검 (plan_logic)

기획안의 목표, 수단, 가정, 근거 사이의 논리적 연결을 분석한다. 기획 방법론과 무관하게 쓰며 사용자의 방법론에 맞게 클래스 구조를 바꾼다.

```python
classes = {
    "Plan": None,
    "Objective": None,
    "Strategy": None,
    "Action": None,
    "Assumption": None,
    "Evidence": None,
    "Gap": None,
}

object_properties = {
    "achieves":        {"domain": "Strategy", "range": "Objective"},
    "consists_of":     {"domain": "Strategy", "range": "Action"},
    "depends_on":      {"domain": "Action", "range": "Assumption"},
    "supported_by":    {"domain": "Assumption", "range": "Evidence"},
    "causes":          {"domain": "Action", "range": "Objective"},
    "has_gap":         {"domain": "Plan", "range": "Gap"},
}

data_properties = {
    "feasibility":     {"domain": "Action", "range": "str", "functional": True},
}
```

점검 규칙:

- (겹침과 빠짐) 사용자가 정의한 분류 체계의 하위 분류
- (원인과 결과의 연쇄) causes 경로가 행동에서 목표까지 이어지는지 확인한다
- (근거) Assumption이 Evidence와 연결되었는지 확인한다
- (실행 가능성) Action의 feasibility 값이 빠졌는지 확인한다

```python
axioms = {
    "disjoint_groups": [],
    "min_cardinality": [
        {"class": "Strategy", "property": "achieves", "min": 1, "range_class": "Objective"},
        {"class": "Strategy", "property": "consists_of", "min": 1, "range_class": "Action"},
        {"class": "Assumption", "property": "supported_by", "min": 1, "range_class": "Evidence"},
    ],
    "equivalent_classes": [
        {"name": "UnsupportedAssumption", "base_class": "Assumption",
         "condition": "근거(Evidence)가 연결되지 않은 가정",
         "owl_pattern": "Assumption & NOT(supported_by.some(Evidence))"},
        {"name": "OrphanObjective", "base_class": "Objective",
         "condition": "어떤 전략도 달성 대상으로 가리키지 않는 목표",
         "owl_pattern": "Objective & NOT(INVERSE(achieves).some(Strategy))"},
    ],
}
```

## 3. 절차 준수 점검 (process_compliance)

```python
classes = {
    "Process": None,
    "Step": None,
    "Input": None,
    "Output": None,
    "Rule": None,
    "Violation": None,
    "Actor": None,
}

object_properties = {
    "precedes":        {"domain": "Step", "range": "Step", "transitive": True},
    "requires_input":  {"domain": "Step", "range": "Input"},
    "produces_output": {"domain": "Step", "range": "Output"},
    "performed_by":    {"domain": "Step", "range": "Actor"},
    "governed_by":     {"domain": "Step", "range": "Rule"},
    "violates":        {"domain": "Step", "range": "Rule"},
    "part_of":         {"domain": "Step", "range": "Process"},
}

data_properties = {
    "step_order":      {"domain": "Step", "range": "int", "functional": True},
    "is_mandatory":    {"domain": "Step", "range": "bool", "functional": True},
}
```

점검 규칙:

- (절차 완결) precedes 관계에 시작 단계와 끝 단계가 있는지 확인한다
- (순서 일치) step_order 순서와 precedes 관계가 일치하는지 확인한다
- (필수 단계 누락) is_mandatory가 True인 Step이 실행되었는지 확인한다
- (입출력 연결) 앞 단계의 Output이 뒤 단계의 Input과 이어지는지 확인한다

```python
axioms = {
    "disjoint_groups": [
        ["Input", "Output"]  # 입력과 출력은 서로 겹치지 않음
    ],
    "min_cardinality": [
        {"class": "Step", "property": "produces_output", "min": 1, "range_class": "Output"},
        {"class": "Step", "property": "part_of", "min": 1, "range_class": "Process"},
    ],
    "equivalent_classes": [
        {"name": "DisconnectedStep", "base_class": "Step",
         "condition": "앞 단계도 뒤 단계도 없는 고립 단계",
         "owl_pattern": "Step & NOT(precedes.some(Step)) & NOT(INVERSE(precedes).some(Step))"},
    ],
}
```

## 4. 문제 분해 (problem_decomposition)

```python
classes = {
    "Problem": None,
    "SubProblem": "Problem",
    "RootCause": None,
    "Symptom": None,
    "Solution": None,
    "Criterion": None,
    "Resource": None,
}

object_properties = {
    "has_subproblem":  {"domain": "Problem", "range": "SubProblem"},
    "caused_by":       {"domain": "Problem", "range": "RootCause"},
    "manifests_as":    {"domain": "RootCause", "range": "Symptom"},
    "resolved_by":     {"domain": "Problem", "range": "Solution"},
    "evaluated_by":    {"domain": "Solution", "range": "Criterion"},
    "requires":        {"domain": "Solution", "range": "Resource"},
    "causes":          {"domain": "RootCause", "range": "Problem"},
}

data_properties = {
    "severity":        {"domain": "Problem", "range": "str", "functional": True},
}
```

점검 규칙:

- (겹침과 빠짐) Problem의 하위 분해(SubProblem)
- (원인과 결과의 연쇄) caused_by와 causes 경로에 순환이 있는지 확인한다
- (해결책 포괄) 모든 SubProblem에 resolved_by 연결이 있는지 확인한다
- (자원 충돌) 여러 Solution이 같은 Resource를 requires하는지 확인한다

```python
axioms = {
    "disjoint_groups": [
        ["RootCause", "Symptom"]  # 원인과 증상은 서로 겹치지 않음
    ],
    "min_cardinality": [
        {"class": "Problem", "property": "caused_by", "min": 1, "range_class": "RootCause"},
        {"class": "Problem", "property": "resolved_by", "min": 1, "range_class": "Solution"},
    ],
    "equivalent_classes": [
        {"name": "UnresolvedProblem", "base_class": "Problem",
         "condition": "해결책이 연결되지 않은 문제",
         "owl_pattern": "Problem & NOT(resolved_by.some(Solution))"},
    ],
}
```

## 5. 다축 평가 (multi_axis_evaluation)

여러 평가 기준이 각자 분석한 뒤 종합 판정에 합산되는 구조다. 각 기준이 같은 대상을 참조하는지와 모든 기준의 결과가 종합 판정에 빠짐없이 들어가는지 분석한다. 평가 기준의 명칭과 수는 사용자가 정한다.

```python
classes = {
    "EvaluationAxis": None,
    "Criterion": None,
    "SharedEntity": None,
    "AxisResult": None,
    "ComprehensiveResult": None,
}

object_properties = {
    "has_criterion":     {"domain": "EvaluationAxis", "range": "Criterion"},
    "references_entity": {"domain": "EvaluationAxis", "range": "SharedEntity"},
    "produces_result":   {"domain": "EvaluationAxis", "range": "AxisResult"},
    "feeds_into":        {"domain": "AxisResult", "range": "ComprehensiveResult"},
}

data_properties = {
    "weight":      {"domain": "EvaluationAxis", "range": "float", "functional": True},
    "score":       {"domain": "AxisResult", "range": "str", "functional": True},
}
```

점검 규칙:

- (같은 대상 참조) check_shared_reference로 여러 기준이 같은 SharedEntity를 참조하는지 확인한다
- (종합 판정 포괄) check_coverage로 모든 AxisResult가 ComprehensiveResult에 들어가는지 확인한다
- (프리셋) run_preset_multi_axis로 한 번에 실행할 수 있다

```python
axioms = {
    "disjoint_groups": [],
    "min_cardinality": [
        {"class": "EvaluationAxis", "property": "produces_result", "min": 1, "range_class": "AxisResult"},
        {"class": "AxisResult", "property": "feeds_into", "min": 1, "range_class": "ComprehensiveResult"},
    ],
    "equivalent_classes": [
        {"name": "OrphanAxisResult", "base_class": "AxisResult",
         "condition": "종합 판정(ComprehensiveResult)에 들어가지 않은 기준 결과",
         "owl_pattern": "AxisResult & NOT(feeds_into.some(ComprehensiveResult))"},
    ],
}
```

## 6. 법정 절차 준수 (regulated_procedure)

법령이나 지침으로 절차 순서와 단계별 필수 산출물이 정해진 구조다. 절차명과 단계 수는 사용자가 정하며 템플릿은 기본 클래스와 속성만 제공한다.

```python
classes = {
    "Procedure": None,
    "Stage": None,
    "MandatoryOutput": None,
    "OptionalOutput": None,
    "Actor": None,
    "LegalBasis": None,
}

object_properties = {
    "precedes":            {"domain": "Stage", "range": "Stage", "transitive": True},
    "produces":            {"domain": "Stage", "range": "MandatoryOutput"},
    "optionally_produces": {"domain": "Stage", "range": "OptionalOutput"},
    "performed_by":        {"domain": "Stage", "range": "Actor"},
    "governed_by":         {"domain": "Procedure", "range": "LegalBasis"},
    "part_of":             {"domain": "Stage", "range": "Procedure"},
}

data_properties = {
    "step_order":      {"domain": "Stage", "range": "int", "functional": True},
    "is_mandatory":    {"domain": "Stage", "range": "bool", "functional": True},
}
```

점검 규칙:

- (절차 순서) check_pipeline_trace로 precedes 연쇄가 시작에서 끝까지 끊기지 않는지 확인한다
- (필수 산출물) check_mandatory_outputs로 각 Stage가 MandatoryOutput을 가졌는지 전수 확인한다
- (프리셋) run_preset_regulated_procedure로 한 번에 실행할 수 있다

```python
axioms = {
    "disjoint_groups": [
        ["MandatoryOutput", "OptionalOutput"]  # 필수 산출물과 선택 산출물은 서로 겹치지 않음
    ],
    "min_cardinality": [
        {"class": "Stage", "property": "produces", "min": 1, "range_class": "MandatoryOutput"},
        {"class": "Stage", "property": "part_of", "min": 1, "range_class": "Procedure"},
    ],
    "equivalent_classes": [
        {"name": "IncompleteStage", "base_class": "Stage",
         "condition": "필수 산출물(MandatoryOutput)이 연결되지 않은 단계",
         "owl_pattern": "Stage & NOT(produces.some(MandatoryOutput))"},
    ],
}
```

## 7. 논리모형 (logic_model)

자원을 투입해 활동을 수행하고 산출과 성과를 만드는 구조를 분석한다. 사업 기획, 정책 설계, 프로그램 평가처럼 투입에서 활동, 산출, 성과, 영향으로 이어지는 분석에 쓴다. 단계 명칭과 수는 사용자가 정한다.

```python
classes = {
    "Problem": None,
    "Objective": None,
    "Beneficiary": None,
    "InputResource": None,
    "Activity": None,
    "Output": None,
    "Outcome": None,
    "Impact": None,
    "Assumption": None,
    "Evidence": None,
    "Indicator": None,
}

object_properties = {
    "addresses":      {"domain": "Activity", "range": "Problem"},
    "achieves":       {"domain": "Activity", "range": "Objective"},
    "targets":        {"domain": "Objective", "range": "Beneficiary"},
    "requires":       {"domain": "Activity", "range": "InputResource"},
    "produces":       {"domain": "Activity", "range": "Output"},
    "leads_to":       {"domain": "Output", "range": "Outcome"},
    "contributes_to": {"domain": "Outcome", "range": "Impact"},
    "precedes":       {"domain": "Activity", "range": "Activity", "transitive": True},
    "attached_to":    {"domain": "Assumption", "range": "Activity"},
    "supported_by":   {"domain": "Assumption", "range": "Evidence"},
    "measured_by":    {"domain": "Objective", "range": "Indicator"},
}

data_properties = {}
```

점검 규칙:

- (활동 연쇄) check_pipeline_trace로 Activity 연쇄가 끊긴 곳을 찾는다
- (양방향 포괄) check_bidirectional_coverage로 목표와 활동 사이에 연결되지 않은 개체를 찾는다
- (근거 없는 가정) check_unsupported_assumptions로 Evidence가 연결되지 않은 Assumption을 찾는다
- (가정 영향) check_assumption_impact로 가정이 틀렸을 때 다시 검토해야 하는 뒤 단계를 산출한다
- (지표) check_provenance로 Objective가 Indicator를 가졌는지 확인한다
- (프리셋) run_preset_logic_model로 한 번에 실행할 수 있다

```python
axioms = {
    "disjoint_groups": [
        ["InputResource", "Output", "Outcome", "Impact"]  # 투입, 산출, 성과, 영향은 서로 겹치지 않음
    ],
    "min_cardinality": [
        {"class": "Activity", "property": "produces", "min": 1, "range_class": "Output"},
        {"class": "Activity", "property": "achieves", "min": 1, "range_class": "Objective"},
        {"class": "Objective", "property": "measured_by", "min": 1, "range_class": "Indicator"},
        {"class": "Assumption", "property": "supported_by", "min": 1, "range_class": "Evidence"},
    ],
    "equivalent_classes": [
        {"name": "UnsupportedAssumption", "base_class": "Assumption",
         "condition": "근거(Evidence)가 연결되지 않은 가정",
         "owl_pattern": "Assumption & NOT(supported_by.some(Evidence))"},
        {"name": "UnmeasuredObjective", "base_class": "Objective",
         "condition": "지표(Indicator)가 연결되지 않은 목표",
         "owl_pattern": "Objective & NOT(measured_by.some(Indicator))"},
    ],
}
```

## 8. 의사결정 트리 (decision_tree)

조건에 따라 절차나 선택지가 갈리는 구조다. 도입 절차, 사업 유형별 절차 분기, 사전 점검표처럼 조건으로 결정하는 경우에 쓴다. 분기 조건과 선택지 명칭은 사용자가 정한다.

```python
classes = {
    "DecisionPoint": None,
    "Condition": None,
    "Option": None,
    "Prerequisite": None,
}

object_properties = {
    "has_condition":   {"domain": "DecisionPoint", "range": "Condition"},
    "leads_to":        {"domain": "Condition", "range": "Option"},
    "requires":        {"domain": "Option", "range": "Prerequisite"},
    "excludes":        {"domain": "Option", "range": "Option"},
    "precedes":        {"domain": "DecisionPoint", "range": "DecisionPoint", "transitive": True},
}

data_properties = {
    "condition_value": {"domain": "DecisionPoint", "range": "str", "functional": True},
}
```

점검 규칙:

- (조건 분기) check_conditional_branch로 조건값마다 필수 단계와 제외 단계를 지켰는지 확인한다
- (전제조건) check_provenance로 Option이 Prerequisite를 가졌는지 확인한다
- (동시 선택) excludes로 이어진 Option이 함께 선택되지 않았는지 확인한다
- (프리셋) run_preset_decision_tree로 한 번에 실행할 수 있다

```python
axioms = {
    "disjoint_groups": [],
    "min_cardinality": [
        {"class": "DecisionPoint", "property": "has_condition", "min": 1, "range_class": "Condition"},
        {"class": "Condition", "property": "leads_to", "min": 1, "range_class": "Option"},
    ],
    "equivalent_classes": [
        {"name": "DeadEndCondition", "base_class": "Condition",
         "condition": "선택지(Option)가 연결되지 않은 조건",
         "owl_pattern": "Condition & NOT(leads_to.some(Option))"},
    ],
}
```

## 9. 다단계 분류 대응 (classification_chain)

유형 분류에서 하위 분야를 거쳐 세부 항목으로 이어지는 다단계 허용 대응 구조다. 분류 체계에 따라 지표, 평가 기준, 자원 배분 항목을 고르는 작업에 쓴다. 단계 수와 분류 명칭은 사용자가 정한다.

```python
classes = {
    "Category": None,
    "Field": None,
    "Item": None,
    "MeasurementMethod": None,
}

object_properties = {
    "maps_to_field":   {"domain": "Category", "range": "Field"},
    "selects_item":    {"domain": "Field", "range": "Item"},
    "measured_by":     {"domain": "Item", "range": "MeasurementMethod"},
}

data_properties = {
    "item_name":       {"domain": "Item", "range": "str", "functional": True},
    "formula":         {"domain": "MeasurementMethod", "range": "str"},
}
```

점검 규칙:

- (단계별 허용 대응) check_mapping_chain으로 Category에서 Field를 거쳐 Item까지 단계마다 허용 규칙을 지켰는지 확인한다
- (양방향 포괄) check_bidirectional_coverage로 어느 Field에도 속하지 않는 Item을 찾는다
- (항목명과 측정 방법) check_shared_reference로 Item과 MeasurementMethod가 같은 대상을 참조하는지 확인한다
- (프리셋) run_preset_mapping_chain으로 한 번에 실행할 수 있다

```python
axioms = {
    "disjoint_groups": [],
    "min_cardinality": [
        {"class": "Category", "property": "maps_to_field", "min": 1, "range_class": "Field"},
        {"class": "Field", "property": "selects_item", "min": 1, "range_class": "Item"},
        {"class": "Item", "property": "measured_by", "min": 1, "range_class": "MeasurementMethod"},
    ],
    "equivalent_classes": [
        {"name": "UnmappedCategory", "base_class": "Category",
         "condition": "분야(Field)에 대응되지 않은 분류",
         "owl_pattern": "Category & NOT(maps_to_field.some(Field))"},
    ],
}
```

## 템플릿 병합과 변형

- 사용자가 고유한 분석 틀이나 방법론을 가졌으면 템플릿 없이 처음부터 TBox를 만든다
- 같은 이름의 클래스가 여러 템플릿에 있으면 상위 클래스 구조가 더 세분된 쪽을 쓴다
- 속성은 이름이 겹치지 않으면 모두 합친다
- 이름이 겹치면 도메인에 더 특화된 쪽을 쓰되 사용자 확인 뒤 진행한다
- 클래스명, 속성명, 계층 구조는 사용자의 용어 체계에 맞게 바꾼다
- axioms의 disjoint_groups, min_cardinality, equivalent_classes는 이름이 겹치지 않으면 모두 합친다. 같은 클래스에 서로 충돌하는 공리가 있으면 사용자 확인 뒤 진행한다
