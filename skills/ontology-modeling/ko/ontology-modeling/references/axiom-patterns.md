# 공리와 추론기 패턴

OWL 공리를 구축하고 추론기(HermiT, Pellet)를 실행하는 방법이다. 공리는 TBox가 확정된 뒤 사용자가 고른 것만 적용한다.

## 추론기가 하는 일

점검에 쓰는 패턴은 다음과 같다.

- (자동 분류) 유형의 필요충분조건을 정의하면 추론기가 속성값으로 개체의 유형을 판별한다. 사용자가 선언한 유형과 추론기가 판별한 유형이 다르면 오분류를 찾은 것이다
- (상호 배타) 동시에 속할 수 없는 유형에 함께 속한 개체를 모순으로 찾는다
- (수량 제약) 연결 수의 상한이나 정확한 수를 선언하면 서로 다르다고 선언한 대상이 제약을 넘을 때 모순으로 찾는다
- (모순 검사) 여러 공리의 조합이 모순인지 충족 가능성 검사로 판정한다

새 사실을 끌어내는 패턴은 다음과 같다.

- (속성 연쇄) 두 단계 이상의 관계를 이어 간접 관계를 도출한다
- (역속성) 한쪽 방향만 입력하면 반대 방향을 채운다
- (복합 조건 분류) 속성값 범위와 관계 존재 여부를 조합해 분류한다
- (SWRL 규칙) IF-THEN 규칙으로 새 사실을 도출한다

## 개방 세계에서 추론기가 판정하는 범위

OWL 추론기는 입력되지 않은 사실을 미지로 본다. 또 이름이 다르다고 다른 개체라고 가정하지 않는다. 그래서 같은 공리라도 판정할 수 있는 것과 없는 것이 나뉜다. 아래 동작은 owlready2 0.51과 HermiT로 실행해 확인했다.

| 공리 | 입력만으로 판정하는 것 | 입력만으로 판정하지 못하는 것 | 보완 방법 |
|---|---|---|---|
| DisjointClasses | 두 클래스에 동시에 속한 개체 (온톨로지 모순) | 없음 | 없음 |
| MinCardinality | 없음 | 연결이 빠진 개체 | SPARQL의 unsupported 쿼리나 check_provenance로 미입력 후보를 찾고, 입력이 완전하다고 확인되면 close_world_scope 뒤 추론 |
| MaxCardinality | 서로 다르다고 선언한 대상이 상한을 넘는 경우 | build_all_different 선언이 없는 초과 | 대상 개체에 build_all_different 선언 |
| EquivalentClass (some 조건) | 조건을 채운 개체의 자동 분류 | 없음 | 없음 |
| EquivalentClass (Not 조건) | 없음 | 연결이 없다는 이유의 분류 | 입력이 완전하다고 확인된 범위에 close_world_scope 뒤 추론 |
| 전이 속성 (domain과 range가 다름) | 연쇄 중간의 개체가 두 클래스에 동시에 속한다는 추론 | 해당 없음 | 전이 속성은 domain과 range가 같은 클래스일 때만 선언 |

close_world_scope는 "이 범위의 입력은 완전하다"는 선언이다. 사용자가 해당 범위의 조사가 끝났다고 확인한 경우에만 실행하고, 선언한 범위와 근거를 보고서에 적는다.

```python
# 사용자가 Assumption 목록과 근거 연결이 완전하다고 확인한 뒤
close_world_scope(onto, class_names=["Assumption"])
result = run_full_analysis(world, onto, use_hermit=True)
```

## 공리 구축 헬퍼

### 클래스 공리

| 공리 | 헬퍼 | 용도 |
|---|---|---|
| EquivalentClass | build_equivalent_class | 필요충분조건으로 자동 분류 |
| DisjointClasses | build_disjoint_group | 상호 배타 선언 |
| DisjointUnion | build_disjoint_union | 하위 클래스가 겹치지 않고 합쳐서 상위 클래스 전체를 이룬다는 선언 |
| OneOf | build_one_of | 특정 개체 목록만으로 클래스 정의 |
| AllDifferent | build_all_different | 목록의 개체가 모두 서로 다르다는 선언 |
| SWRL | build_swrl_rule | IF-THEN 규칙으로 새 사실 도출 |

### 수량과 값 제약

| 공리 | 헬퍼 | 용도 |
|---|---|---|
| MinCardinality | build_min_cardinality | 최소 N개 연결 요건 |
| MaxCardinality | build_max_cardinality | 최대 N개 연결 제한 |
| ExactCardinality | build_exact_cardinality | 정확히 N개 연결 요건 |
| AllValuesFrom | build_all_values_from | 참조 대상을 특정 클래스로 제한 |
| HasValue | build_has_value | 특정 개체와 반드시 연결 |

### 속성 특성

| 특성 | 지정 방법 | 뜻 |
|---|---|---|
| Transitive | is_transitive=True | A가 B에, B가 C에 앞서면 A가 C에 앞선다 |
| Functional | is_functional=True | 값을 최대 하나만 가진다 |
| Symmetric | is_symmetric=True | A가 B와 협력하면 B도 A와 협력한다 |
| Asymmetric | is_asymmetric=True | A가 B에게 보고하면 B는 A에게 보고할 수 없다 |
| Reflexive | is_reflexive=True | 모든 개체가 자기 자신과 관계를 가진다 |
| Irreflexive | is_irreflexive=True | 어떤 개체도 자기 자신과 관계를 가질 수 없다 |
| InverseFunctional | is_inverse_functional=True | 속성값으로 개체를 하나로 식별한다 |
| Inverse | onto["B"].inverse_property = onto["A"] | A의 역방향이 B다 |
| PropertyChain | prop.property_chain.append(PropertyChain([p1, p2])) | p1을 거쳐 p2이면 prop이 성립한다 |

Transitive부터 InverseFunctional까지는 build_object_property의 인자로 지정한다.

### restriction_expr 조합

build_equivalent_class의 restriction_expr 인자에 아래 표현을 조합한다.

| 표현 | 뜻 | 종류 |
|---|---|---|
| prop.some(Target) | Target과 최소 1개 연결 | 존재 제약 |
| prop.only(Target) | Target만 참조 | 전칭 제약 |
| prop.value(individual) | 특정 개체와 연결 | 개체 제약 |
| prop.min(N, Target) | 최소 N개 연결 | 최소 수량 |
| prop.max(N, Target) | 최대 N개 연결 | 최대 수량 |
| prop.exactly(N, Target) | 정확히 N개 연결 | 정확 수량 |
| prop.has_self() | 자기 자신을 참조 | 자기 참조 |
| ConstrainedDatatype(int, min_inclusive=N) | 수치 하한 | 데이터 범위 |
| Class & expr1 & expr2 | 모든 조건을 동시에 충족 | 교집합 |
| Class1 \| Class2 | 둘 중 하나 | 합집합 |
| Not(expr) | 조건의 부정 | 부정 (개방 세계 동작은 위 표 참고) |
| Inverse(prop) | 이름 없는 역방향 속성 | 역방향 |

## 코드 예시

### 기본 공리

```python
# 자동 분류
build_equivalent_class(onto, "ShortTerm",
    onto["Project"] & onto["has_tag"].some(onto["ShortTag"]))

# 상호 배타
build_disjoint_group(onto, ["TypeA", "TypeB", "TypeC"])

# 겹치지 않고 합쳐서 전체를 이룸
build_disjoint_union(onto, "Factor",
    ["Strength", "Weakness", "Opportunity", "Threat"])

# 수량 제약
build_min_cardinality(onto, "Objective", "has_indicator", 1, "Indicator")
build_max_cardinality(onto, "Strategy", "uses_factor", 3, "Factor")
build_exact_cardinality(onto, "Step", "performed_by", 1, "Actor")

# 참조 제한
build_all_values_from(onto, "InternalProject", "performed_by", "InternalActor")
build_has_value(onto, "RegulatedProject", "governed_by", "gov_agency_1")
```

### 도출 공리

```python
from owlready2 import PropertyChain

# 속성 연쇄: manages를 거쳐 contains이면 responsible_for
with onto:
    onto["responsible_for"].property_chain.append(
        PropertyChain([onto["manages"], onto["contains"]]))

# 역속성
with onto:
    onto["managed_by"].inverse_property = onto["manages"]

# SWRL 규칙 (내장 함수 없음, HermiT에서 실행)
build_swrl_rule(onto,
    "Person(?p), manages(?p, ?proj) -> responsible_for(?p, ?proj)",
    name="manager_responsibility")

# SWRL 내장 함수 (Pellet에서만 실행)
build_swrl_rule(onto,
    "Project(?p), budget(?p, ?b), lessThan(?b, 1000000) -> SmallProject(?p)",
    name="small_project")

# 규칙 목록 조회와 삭제
for r in list_swrl_rules(onto):
    print(f"[{r['label']}] IF {r['body']} THEN {r['head']}")
delete_swrl_rule(onto, "small_project")
```

### 고급 공리

```python
from owlready2 import ConstrainedDatatype, Inverse

# 열거 클래스
build_one_of(onto, "PriorityRole", ["role_pm", "role_lead"])

# 개체 고유성 (두 개만 넘기면 개별 쌍 선언)
build_all_different(onto, ["alice", "bob", "charlie"])

# 데이터 범위로 자동 분류
build_equivalent_class(onto, "LargeProject",
    onto["Project"]
    & onto["budget"].some(ConstrainedDatatype(int, min_inclusive=1000000000))
    & onto["duration_years"].some(ConstrainedDatatype(int, min_inclusive=3)))

# 자기 참조
build_equivalent_class(onto, "SelfReviewedDocument",
    onto["Document"] & onto["reviewed_by_self"].has_self())

# 복합 조건 (Not과 max 0은 close_world_scope 뒤에 판정된다)
build_equivalent_class(onto, "RiskyProject",
    onto["Project"]
    & onto["budget"].some(ConstrainedDatatype(int, min_inclusive=5000000000))
    & onto["mitigates"].max(0, onto["Risk"]))

# 속성 특성 조합
build_object_property(onto, "reports_to", "Person", "Person",
    is_asymmetric=True, is_irreflexive=True)
build_object_property(onto, "cooperates_with", "Partner", "Partner",
    is_symmetric=True)
build_object_property(onto, "has_id", "Person", "IDNumber",
    is_inverse_functional=True)

# 이름 없는 역속성을 제약 안에서 사용
build_equivalent_class(onto, "UnmanagedDepartment",
    onto["Department"] & Inverse(onto["manages"]).max(0, onto["Person"]))
```

## 속성값 수정

```python
update_property(onto, "proj1", "budget", 3000000000)            # 값 전체 교체
remove_property_value(onto, "proj1", "achieves", onto["goal_old"])  # 값 하나 제거
clear_property(onto, "proj1", "achieves")                        # 값 전체 삭제
```

## rdflib 연결

as_rdflib_graph는 World 전체를 rdflib 호환 그래프로 돌려준다. rdflib의 SPARQL 1.1 기능과 RDF 직렬화를 쓸 수 있다.

```python
graph = as_rdflib_graph(onto)
if graph is not None:
    rows = list(graph.query("SELECT ?s WHERE { ?s ?p ?o } LIMIT 5"))
```

## 추론기 실행

```python
# HermiT (기본값: 클래스 분류만 수행)
result = run_full_analysis(world, onto, use_hermit=True)

# HermiT와 객체 속성 값 추론
result = run_full_analysis(world, onto, use_hermit=True,
                           infer_property_values=True)

# Pellet (SWRL 내장 함수가 필요할 때)
result = run_full_analysis(world, onto, use_hermit=True, reasoner="pellet")

# Pellet과 객체, 데이터 속성 값 추론
result = run_full_analysis(world, onto, use_hermit=True, reasoner="pellet",
                           infer_property_values=True,
                           infer_data_property_values=True)

# 추론기만 실행하고 재분류 확인
ha = run_hermit_analysis(world, onto)
for rc in ha["reclassifications"]:
    print(f"{rc['individual']}: {rc['before']} -> {rc['after']}")
```

- 추론 결과의 mode가 fallback이면 추론기가 실행되지 않은 것이다. message를 사용자에게 알리고 check 함수와 SPARQL로 대신한다
- 추론기 시간 제한(기본 30초)은 SIGALRM을 지원하는 운영체제의 메인 스레드에서만 동작한다. Windows와 다른 스레드에서는 시간 제한 없이 실행된다
- owlready2 0.50과 0.51에 포함된 Pellet 라이브러리는 Java 25 이상에서 실행된다. 더 낮은 Java에서는 Pellet 호출이 실패해 fallback으로 돌아간다

| 인자 | HermiT | Pellet | 용도 |
|---|---|---|---|
| infer_property_values | 지원 | 지원 | 객체 속성 값 추론 |
| infer_data_property_values | 미지원 | 지원 | 데이터 속성 값 추론 |
| reasoner | "hermit" | "pellet" | 추론기 선택 |

## 외부 온톨로지와 IRI

```python
# 원하는 IRI로 온톨로지 생성
world, onto = create_world(iri="http://example.org/project.owl")
build_class(onto, "LocalClass")

# 로컬 파일이나 IRI의 외부 온톨로지 import
ext = import_ontology(world, onto, "external.owl")
if ext is not None:
    build_object_property(onto, "uses_ext", "LocalClass", ext["ExternalClass"])

# query_onto는 import한 온톨로지의 접두어를 자동으로 붙인다
rows = query_onto(world, onto, "SELECT ?x WHERE { ?x a :LocalClass }")
```

외부 온톨로지를 import하면 추론기를 실행할 때 import한 공리도 함께 적용된다.

## 공리 제안

TBox가 확정된 뒤 suggest_axioms로 적용할 수 있는 공리를 받아 사용자에게 보여 준다.

```python
for s in suggest_axioms(onto):
    print(f"[{s['axiom']}] {s['target']}: {s['description']}")
    print(s["code"])
```

제안에 없는 공리도 도메인 판단에 따라 위 표와 restriction_expr 조합으로 제안할 수 있다.

## 추가 헬퍼

| 함수 | 용도 |
|---|---|
| build_annotation_property(onto, name) | 문서화 전용 속성 생성 (추론기가 사용하지 않음) |
| add_to_class(onto, individual_name, class_name) | 개체를 다른 클래스에도 소속 |
| destroy_individual(onto, individual_name) | 개체와 관련 연결 삭제 |
| build_same_as(onto, name_a, name_b) | 두 개체가 같은 대상이라고 선언 |
| build_sub_property(onto, child, parent) | 속성의 상하 관계 선언 |
| build_equivalent_properties(onto, name_a, name_b) | 두 속성이 같다고 선언 (어휘를 합칠 때) |
| build_class(onto, name, parent=[A, B]) | 여러 상위 클래스 지정 |
| close_world_scope(onto, class_names, individual_names) | 입력이 완전하다고 확인된 범위를 폐쇄 세계로 선언 |
| list_swrl_rules(onto) | SWRL 규칙 목록 (label, body, head) |
| delete_swrl_rule(onto, rule_or_label) | SWRL 규칙 삭제 |

## SWRL 규칙

- SWRL은 2004년에 제출된 W3C 멤버 제출(Member Submission) 문서로 표준 권고안 단계에 오르지 않았다
- OWL DL에 SWRL을 결합하면 유한 시간 안에 추론이 끝난다는 보장이 사라지므로 보수적으로 쓴다
- SWRL 규칙을 제안하기 전에 이 위험을 알리고 적용 여부를 묻는다
- 같은 효과를 EquivalentClass나 제약 공리로 낼 수 있는지 먼저 검토한다
- HermiT는 규칙을 이름 있는 개체에만 적용(DL-safe)하며 내장 함수가 들어간 규칙은 실행하지 않는다
- 내장 함수가 필요하면 reasoner="pellet"으로 바꾼다. 이 경우 추론이 끝나지 않을 수 있음을 알린다

내장 함수는 Pellet에서 실행된다.

| 내장 함수 | 용도 | 예시 |
|---|---|---|
| greaterThan(?a, N) | 초과 | "age(?p, ?a), greaterThan(?a, 18)" |
| lessThan(?a, N) | 미만 | "budget(?p, ?b), lessThan(?b, 1000000)" |
| equal(?a, N) | 같음 | "priority(?p, ?v), equal(?v, 1)" |
| greaterThanOrEqual(?a, N) | 이상 | "score(?p, ?s), greaterThanOrEqual(?s, 80)" |
| lessThanOrEqual(?a, N) | 이하 | "score(?p, ?s), lessThanOrEqual(?s, 100)" |
| add(?r, ?a, ?b) | 덧셈 (?r = ?a + ?b) | "budget(?p, ?b), add(?total, ?b, 100000)" |
| subtract(?r, ?a, ?b) | 뺄셈 (?r = ?a - ?b) | "subtract(?profit, ?total, ?cost)" |
| multiply(?r, ?a, ?b) | 곱셈 (?r = ?a × ?b) | "multiply(?amount, ?rate, ?base)" |
| stringConcat(?r, ?a, ?b) | 문자열 결합 | "stringConcat(?s, ?name, '_suffix')" |
