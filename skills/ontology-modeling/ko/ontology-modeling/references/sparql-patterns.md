# SPARQL 질의 패턴

## 경로 판단

- 예 또는 아니오로 답하는 질문은 check 함수 경로를 쓴다
- 목록이나 수치로 답하는 질문은 SPARQL 경로를 쓴다
- check 함수가 다루지 않는 질문은 Python 코드를 새로 짜기 전에 SPARQL을 먼저 작성한다

SPARQL과 check 함수는 입력된 사실만 읽는다. FILTER NOT EXISTS로 찾은 미연결 개체는 미입력 후보로 보고하고, 그 연결이 실제로 없다고 단정하지 않는다.

## 내장 쿼리 (SPARQL_CHECKS)

onto_engine.py에는 파라미터를 받는 SPARQL 쿼리 12종이 들어 있다. run_sparql_check(world, "쿼리명", onto=onto, **params)로 실행한다. check 함수가 내부에서 호출하므로 직접 부르지 않아도 된다.

| 쿼리명 | 패턴 | 파라미터 |
|---|---|---|
| mece_overlap | 두 클래스에 동시에 속한 개체 | class_a, class_b |
| unsupported | 속성 값이 없는 개체 (FILTER NOT EXISTS) | target_class, link_property |
| coverage | 어떤 참조 개체도 가리키지 않는 개체 | source_class, ref_class, link_property |
| edges | 특정 속성의 모든 연결 | property |
| cardinality_count | 개체별 연결 수 (GROUP BY, COUNT) | parent_class, property_name |
| refs_for_class | 클래스별 참조 대상 집합 | subject_class, link_property |
| value_below | 하한 미달 값 (FILTER) | target_class, value_property, min_val |
| value_above | 상한 초과 값 (FILTER) | target_class, value_property, max_val |
| downstream | 속성 경로로 도달하는 뒤쪽 개체 (property path) | start, order_property |
| conflict_dual_ref | 두 속성이 같은 대상을 가리키는 개체 | prop_a, prop_b |
| mandatory_missing | 필수 산출물 클래스가 없는 단계 (중첩 FILTER NOT EXISTS) | stage_class, output_property, required_class |
| stage_unlinked | 다음 단계와 연결되지 않은 개체 | stage_class, link_property |

반환값은 {"check": 쿼리명, "sparql": 실행한 쿼리, "results": 결과, "count": 건수, "pass": 결과가 0건이면 True}이다.

## 자유 질의 패턴

owlready2의 SPARQL 엔진이 지원하는 범위에서 쓸 수 있는 패턴이다.

| 질의 유형 | SPARQL 패턴 | 자연어 질문 예시 |
|---|---|---|
| 조건 필터 | SELECT ?x WHERE { ?x a :Class . ?x :prop ?v . FILTER(?v > N) } | 예산이 10억 이상인 사업은? |
| 집계 | SELECT ?x (COUNT(?y) AS ?cnt) WHERE { ... } GROUP BY ?x | 전략마다 참조하는 요인은 몇 개인가? |
| 미연결 탐지 | SELECT ?x WHERE { ?x a :Class . FILTER NOT EXISTS { ?x :prop ?y } } | 목표와 연결되지 않은 활동은? |
| 경로 탐색 | SELECT ?x ?y WHERE { ?x :precedes+ ?y } | 활동 A에서 도달하는 모든 뒤 활동은? |
| 패턴 비교 | SELECT ?x WHERE { ?x :propA ?a . ?x :propB ?b . FILTER(?a = ?b) } | 명시한 대상과 실제 수혜자가 같은 사업은? |
| 선택적 조회 | SELECT ?x ?y WHERE { ?x a :Class . OPTIONAL { ?x :prop ?y } } | 모든 사업의 담당자를 조회하되 담당자가 없는 사업도 포함 |
| 합집합 | SELECT ?x WHERE { { ?x a :TypeA } UNION { ?x a :TypeB } } | 단기 과제이거나 긴급 과제인 것은? |

## 코드 예시

```python
# query_onto: 접두어를 자동으로 붙이는 자유 질의 (권장)
rows = query_onto(world, onto,
    "SELECT ?project ?b WHERE { "
    "?project a :Project . ?project :budget ?b . FILTER(?b >= 1000000000) }")

# 집계
rows = query_onto(world, onto,
    "SELECT ?strategy (COUNT(?factor) AS ?cnt) WHERE { "
    "?strategy a :Strategy . ?strategy :uses_factor ?factor "
    "} GROUP BY ?strategy ORDER BY DESC(?cnt)")

# 미연결 탐지
rows = query_onto(world, onto,
    "SELECT ?activity WHERE { ?activity a :Activity . "
    "FILTER NOT EXISTS { ?activity :achieves ?obj } }")

# 선택적 조회
rows = query_onto(world, onto,
    "SELECT ?project ?manager WHERE { ?project a :Project . "
    "OPTIONAL { ?project :managed_by ?manager } }")

# 내장 쿼리 실행
r = run_sparql_check(world, "coverage", onto=onto,
    source_class="Goal", ref_class="Strategy", link_property="achieves")
print(r["results"], r["pass"])

# 내장 쿼리에 없는 질의를 같은 반환 형식으로 실행
r = run_sparql_check(world, "_adhoc", onto=onto,
    sparql_body="SELECT ?x WHERE { ?x a :Strategy . "
                "FILTER NOT EXISTS { ?x :achieves ?g } }",
    label="strategy_without_goal")
print(r["results"], r["count"], r["pass"])
```

## 질의 제안

suggest_sparql_queries(onto)는 현재 TBox를 훑어 탐색에 쓸 질의를 제안한다. 점검 단계를 시작할 때 사용자에게 가능한 질의를 안내하는 용도로 쓰고, 제안된 질의는 query_onto로 바로 실행한다.

```python
for s in suggest_sparql_queries(onto):
    rows = query_onto(world, onto, s["sparql"])
    print(f"[{s['label']}] {s['description']}: {len(rows)}건")
```

## 역량 질문에 답하기

- 역량 질문을 SPARQL의 WHERE 절로 옮겨 query_onto로 실행하는 방식을 먼저 쓴다. Python 코드를 새로 짜지 않고도 답할 수 있다
- check 함수가 이미 다루는 질문은 그 결과를 그대로 쓴다
- 답할 수 있는 역량 질문은 실제 반환값(SPARQL 질의나 check 함수의 결과)을 함께 제시한다
- 답할 수 없는 역량 질문은 보충할 클래스, 속성, 개체를 알린다
- 후속 턴에서 더한 역량 질문도 같은 방식으로 보고한다

## 결과 보고 형식

SPARQL 결과는 질의부, 결과부, 해석으로 나눠 보고한다. 질의문과 반환값은 사용자가 확인할 산출물이므로 그대로 보여 준다.

```markdown
### Q1. 목표와 연결되지 않은 활동

| 구분 | 내용 |
|---|---|
| SPARQL | `SELECT ?a WHERE { ?a a :Activity . FILTER NOT EXISTS { ?a :achieves ?o } }` |
| 자연어 질문 | 목표와 연결되지 않은 활동은 무엇인가 |

| 구분 | 내용 |
|---|---|
| 반환값 | `['activity_3', 'activity_7']` |
| 자연어 답변 | 활동 2건이 어떤 목표와도 연결되어 있지 않다 |

| 반환값 | 해석 |
|---|---|
| activity_3 | 현장 교육 활동에 연결할 목표가 입력되지 않았다 |
| activity_7 | 홍보 활동에 연결할 목표가 입력되지 않았다 |

- 두 활동 모두 미입력 후보이며, 목표와 실제로 무관한지는 원자료로 확인해야 한다
```

결과에서 발견한 패턴은 온톨로지 비전문가도 이해할 수 있는 문장으로 불릿에 적는다.
