# 구조적 등위성과 블록모델링

관계 패턴이 비슷한 행위자를 같은 위치로 묶는 방법과, 묶은 결과를 블록 단위로 요약하는 방법을 정리한다.

## 구조적 등위성

두 행위자가 서로 직접 알지 못해도 제3자들과 맺는 관계가 같으면 같은 위치(position)에 있다고 본다. 같은 위치의 행위자는 네트워크 안에서 서로를 대체할 수 있다. 예를 들어 서로 모르는 두 지점장이 같은 본사 부서와 같은 유형의 고객을 상대한다면 조직 안에서 같은 위치이다.

| 개념 | 정의 |
|---|---|
| 지위(position) | 관계 패턴이 비슷한 행위자들이 차지하는 자리 |
| 역할(role) | 한 지위가 다른 지위와 맺는 관계의 패턴 |

## 등위성 측정

### 유클리디안 거리

두 행위자 i와 j가 나머지 행위자 k와 맺는 관계를 행(보내는 관계)과 열(받는 관계) 양쪽에서 비교한다. i와 j 자신을 가리키는 칸은 제외한다.

$$
d_{ij} = \sqrt{\sum_{k \ne i,j}\left[(x_{ik} - x_{jk})^2 + (x_{ki} - x_{kj})^2\right]}
$$

- 0이면 두 행위자의 관계가 완전히 같다.
- 관계 하나를 0과 1로 기록한 경우 최댓값은 √(2(g-2))이다. 관계 R개를 함께 쓰면 √(2R(g-2))이다.
- 관계의 개수 차이도 거리에 반영되므로 패턴이 같아도 관계 수가 다르면 값이 커진다.

### 상관계수

같은 두 관계 목록(i와 j 자신을 가리키는 칸 제외)의 피어슨 상관계수이다.

- +1이면 관계 패턴이 완전히 같은 방향으로 움직인다.
- 관계 수의 차이보다 패턴의 유사성을 본다.
- 관계 목록의 값이 모두 같은 행위자(예를 들어 고립점)는 상관계수를 정의할 수 없으므로 0으로 둔다.

| 방법 | 비교 대상 | 완전히 같은 두 행위자의 값 |
|---|---|---|
| 유클리디안 거리 | 관계가 같은지 | 0 |
| 상관계수 | 관계 패턴이 비슷한지 | +1 |

두 방법은 같은 데이터에서 다른 결과를 낼 수 있다(Faust and Wasserman 1992). 관계의 수까지 같아야 같은 위치로 볼 때는 유클리디안 거리를, 관계 패턴이 비슷하면 같은 위치로 볼 때는 상관계수를 쓴다.

## 블록모델링

등위성 값으로 비슷한 행위자를 블록으로 묶고, 행위자 단위 매트릭스를 블록 단위 매트릭스로 줄인다. 복잡한 네트워크의 전체 구조를 몇 개 블록 사이의 관계로 요약할 수 있다. 단계별 산출물은 다음과 같다.

| 단계 | 산출물 | 함수 |
|---|---|---|
| 1 | 원자료 매트릭스 | `matrix_to_markdown(G)` |
| 2 | 블록 순서로 재정렬한 매트릭스 | `reorder_matrix(G, reorder_by=blocks.to_dict())` |
| 3 | 블록 사이 관계를 0과 1로 줄인 이미지 매트릭스 | `image_matrix(G, blocks)` |
| 4 | 이미지 매트릭스를 그린 축소 그래프 | `aggregate_to_blocks(G, blocks)` |

블록 간 밀도는 `block_density_matrix(G, blocks)`로 확인한다. 같은 블록 안의 칸은 자기 자신과의 관계를 제외하고 계산한다.

## 블록 나누기 방법

`blockmodel(G, n_blocks, method)`는 다음 방법을 제공한다.

| method | 방법 | 기준 |
|---|---|---|
| `hierarchical` | 유클리디안 거리에 Ward 계층 군집 적용 | 관계의 동일성 |
| `concor` | CONCOR 반복 분할 | 관계 패턴의 상관 |
| `structure` | 최단 거리 목록 사이의 유클리디안 거리에 평균 연결 군집 적용 | 간접 연결을 포함한 거리 |
| `rege` | 일반 등위성 유사도에 평균 연결 군집 적용 | 비슷한 상대와의 관계 |

### CONCOR

CONCOR(CONvergence of iterated CORrelations)는 상관계수 매트릭스의 상관계수를 반복해서 구하면 모든 값이 +1 또는 -1로 수렴하는 성질을 쓴다(Breiger, Boorman, Arabie 1975). +1로 묶인 행위자와 -1로 묶인 행위자가 두 블록이 된다. 더 나누려면 각 블록에 같은 절차를 다시 적용한다.

- 한 단계에서 모든 블록을 둘로 나누므로 블록 수는 2, 4, 8처럼 2의 거듭제곱이다. `blockmodel(G, n_blocks=4, method="concor")`는 두 단계를 수행한다. 2의 거듭제곱 외의 값을 주면 오류를 낸다.
- 이미 관계 패턴이 같은 행위자만 남은 블록은 더 나뉘지 않으므로 실제 블록 수가 요청보다 적을 수 있다.
- 관계가 하나도 없는 고립점은 상관계수를 정의할 수 없어 분할에서 제외하고 블록 번호 0을 준다.
- 몇 단계까지 나눌지는 분석자가 정한다. 결과를 트리로 해석하면 단계별 분할 과정을 추적할 수 있다.

> Breiger, R. L., Boorman, S. A., Arabie, P.(1975), An Algorithm for Clustering Relational Data with Applications to Social Network Analysis and Comparison with Multidimensional Scaling, Journal of Mathematical Psychology

### 경로 거리 방식

직접 연결만 보면 멀리 떨어진 행위자들의 관계 차이를 놓친다. `structure` 방식은 각 행위자에서 다른 모든 행위자까지의 최단 거리를 목록으로 만들고, 목록이 비슷한 행위자를 묶는다. 도달할 수 없는 쌍의 거리는 점의 수에 1을 더한 값으로 둔다. 간접 연결까지 반영하는 경로 거리 기반 등위성을 단순화한 방식이다.

### 일반 등위성과 REGE

일반 등위성(regular equivalence)은 같은 상대와 연결될 필요 없이 비슷한 지위의 상대와 연결되어 있으면 같은 역할로 본다(White and Reitz 1983). 서로 다른 기업 그룹에 속한 계열사끼리, 서로 다른 병원의 간호사끼리 같은 역할로 묶이는 경우가 여기에 해당한다.

`regular_equivalence(G)`의 계산 절차는 다음과 같다.

- 모든 쌍의 유사도를 1로 시작한다.
- 두 행위자의 이웃을 서로 짝지어 가장 비슷한 이웃과의 유사도를 더하고, 두 행위자의 이웃 수 합으로 나눈다.
- 방향 그래프는 나가는 이웃과 들어오는 이웃을 따로 짝짓는다.
- 유사도 변화가 허용 오차보다 작아질 때까지 반복한다.

방향이 없는 이분 데이터에서는 고립점을 제외한 행위자 대부분이 서로 비슷하게 나온다(Hanneman and Riddle 2005). 일반 등위성은 방향 그래프나 계량 그래프에 쓴다.

> White, D. R., Reitz, K. P.(1983), Graph and Semigroup Homomorphisms on Networks of Relations, Social Networks 5

> Hanneman, R. A., Riddle, M.(2005), Introduction to Social Network Methods, Chapter 15(https://faculty.ucr.edu/%7Ehanneman/nettext/C15_Regular_Equivalence.html)

## 이미지 매트릭스 판정 기준

블록 사이에 관계가 있다고 볼지 판정하는 기준은 다음과 같다(Faust and Wasserman 1992). 블록 밀도는 블록 사이의 실제 관계 수를 가능한 관계 수로 나눈 값이다.

| criterion | 기준 | 1로 판정하는 조건 | 쓰임 |
|---|---|---|---|
| `alpha` | α 밀도 | 블록 밀도가 α 이상 | 일반적인 기본값, α는 전체 밀도를 기본으로 씀 |
| `zero` | 영블록 | 관계가 하나라도 있음 | 밀도가 낮은 네트워크 |
| `one` | 1블록 | 가능한 관계가 모두 있음 | 밀도가 높은 네트워크 |
| `perfect` | 완전 적합 | 모두 있으면 1, 하나도 없으면 0 | 블록모델이 구조적 등위성에 완전히 맞는지 점검 |

`perfect` 기준에서 관계가 일부만 있는 칸은 NaN으로 표시한다. NaN이 있으면 그 블록 쌍에서 완전 적합이 성립하지 않는다는 뜻이다. 밀도가 낮은 네트워크에 1블록 기준을 쓰면 거의 모든 칸이 0이 되고, 밀도가 높은 네트워크에 영블록 기준을 쓰면 거의 모든 칸이 1이 되어 구조가 드러나지 않는다.

> Faust, K., Wasserman, S.(1992), Blockmodels: Interpretation and Evaluation, Social Networks 14

## 코드

```python
dist = euclidean_equivalence(G)           # 0에 가까울수록 등위
corr = correlation_equivalence(G)         # +1에 가까울수록 등위
rege = regular_equivalence(G_directed)    # 1에 가까울수록 같은 역할

blocks = blockmodel(G, n_blocks=2, method="concor")
img = image_matrix(G, blocks, criterion="alpha")
dens = block_density_matrix(G, blocks)
reduced = aggregate_to_blocks(G, blocks)
```

## 결과 해석

- (구조적 등위성) 직접 연결이 없어도 관계 패턴이 같은 행위자는 같은 위치이다. 인력 재배치나 대체 가능성을 검토할 때 쓴다.
- (블록모델) 수십 개 부서의 협업 관계를 몇 개 블록 사이의 관계로 줄여 전체 구조를 본다. 블록 사이 관계의 방향으로 중심 블록과 주변 블록을 구분한다.
- (일반 등위성) 산업이나 기업 그룹처럼 여러 하위 조직이 비슷한 역할 구조를 반복하는 데이터에서 역할을 찾을 때 쓴다.
