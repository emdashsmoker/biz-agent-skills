# 응집성과 하위집단

밀도, 구조적 틈새, 사회적 자본, 컴퍼넌트, k-core, 파당과 그 완화 개념을 정리한다.

## 밀도

밀도는 가능한 라인 수 대비 실제 라인 수이다. 0이면 연결이 전혀 없고 1이면 모든 점이 서로 연결되어 있다. k는 실제 라인 수, g는 점의 수이다.

$$
\text{비방향 밀도} = \frac{k}{g(g-1)/2}, \quad \text{방향 밀도} = \frac{k}{g(g-1)}
$$

방향 그래프는 A에서 B로, B에서 A로 가는 라인을 따로 세므로 가능한 라인 수가 두 배이다.

계량 그래프의 밀도는 아래 방식 중 하나를 골라 쓰고 어떤 방식을 썼는지 밝힌다.

- 관계 값을 무시하고 있음과 없음만으로 계산한다.
- 관계 값의 합을 가능한 라인 수로 나눈 평균 강도를 계산한다.
- 관계 값의 합을 실제 라인 수와 관계 값 최댓값의 곱으로 나눈다. 관계의 다중성(multiplicity)을 반영하는 방식이다.

`nx.density`와 `compute_density`는 첫 번째 방식이다.

포괄성(inclusiveness)은 고립되지 않은 점의 비율이다. 고립점이 많으면 밀도가 낮게 나오므로 밀도와 함께 본다. `compute_density(G)`가 밀도, 고립점 수, 포괄성 비율을 함께 반환한다.

## 구조적 틈새

구조적 틈새는 서로 연결되지 않은 두 사람 사이의 빈자리이다(Burt 1992). 이 빈자리를 잇는 사람은 양쪽의 정보를 먼저 얻고 흐름을 조정할 수 있다. 반대로 한 사람의 연결 상대들끼리 이미 서로 연결되어 있으면 그 관계들은 같은 정보를 반복해서 전하므로 중복(redundancy)이 된다.

비방향, 비가중 그래프에서 에고의 지표는 다음과 같이 계산한다(Borgatti 1997). n은 에고와 연결된 상대의 수, t는 상대들끼리의 라인 수이다.

$$
\text{중복} = \frac{2t}{n}, \quad \text{유효 규모} = n - \frac{2t}{n}, \quad \text{효율성} = \frac{\text{유효 규모}}{n}
$$

중복은 상대 한 명이 에고의 다른 상대와 평균 몇 명이나 연결되어 있는지를 뜻한다. 가중 그래프와 방향 그래프는 Burt의 일반식을 쓰며 `nx.effective_size`가 이를 계산한다.

제약(constraint)은 에고의 관계가 몇몇 상대에게 얼마나 묶여 있는지를 나타낸다. p_ij는 i의 전체 관계 중 j에게 들인 비중이다.

$$
c_{ij} = \left(p_{ij} + \sum_{q \ne i,j} p_{iq}\,p_{qj}\right)^2, \quad C_i = \sum_{j} c_{ij}
$$

상대가 적을수록, 상대들끼리 촘촘히 연결되어 있을수록, 관계가 한 상대에게 몰려 있을수록 제약이 커진다. 제약이 작을수록 구조적 틈새를 잇는 위치이다.

`compute_structural_holes(G)`는 유효 규모, 제약, 상대 수, 효율성을 반환하고 제약이 작은 순서로 정렬한다. 효율성의 분모는 중복을 제거한 상대의 수이다. 방향 그래프에서 서로를 가리키는 두 라인은 상대 한 명으로 센다.

> Burt, R. S.(1992), Structural Holes: The Social Structure of Competition, Harvard University Press

> Borgatti, S. P.(1997), Structural Holes: Unpacking Burt's Redundancy Measures, Connections 20(1)

## 밀도와 구조적 틈새

모든 구성원이 서로 연결된 파당에서는 누구를 거치지 않아도 서로 닿을 수 있으므로 구조적 틈새가 없다. 따라서 에고 네트워크의 밀도가 높아질수록 구조적 틈새는 줄어든다.

## 사회적 자본

사회적 자본은 한 행위자가 관계를 통해 쓸 수 있는 자원이다. 측정 관점은 다음과 같다.

- (결속 관점) 촘촘하게 연결된 관계가 신뢰와 협력을 만든다. 밀도와 연결정도로 잰다.
- (중개 관점) 서로 연결되지 않은 집단을 잇는 위치가 새로운 정보를 가져온다. 유효 규모와 제약으로 잰다.

## 컴퍼넌트

컴퍼넌트는 서로 경로로 이어진 점들의 최대 집합이고, 어느 점과도 연결되지 않은 점은 고립점이다. 방향 그래프에서는 컴퍼넌트를 다음과 같이 나눈다.

| 구분 | 조건 | 쓰임 |
|---|---|---|
| 강한 컴퍼넌트 | 구성원 누구에게서 출발해도 방향을 따라 다른 구성원에게 도달 | 자원이 순환하는 집단 |
| 약한 컴퍼넌트 | 방향을 무시하면 서로 이어짐 | 느슨하게 이어진 집단 |

## 사이클, 브릿지, 연계점, 노트

- (사이클 컴퍼넌트) 브릿지를 모두 제거한 뒤 남는 연결 덩어리 중 점이 3개 이상인 덩어리이다. `find_cycle_components`가 찾는다.
- (브릿지) 제거하면 컴퍼넌트가 둘로 나뉘는 라인이다.
- (연계점) 제거하면 컴퍼넌트가 둘 이상으로 나뉘는 점이다.
- (노트, knot) 연계점을 경계로 나뉘는 조각이다. NetworkX의 `nx.biconnected_components`가 이 조각을 찾는다.

## k-core와 m-core

- (k-core) 모든 구성원이 core 안에서 k개 이상의 라인을 가지는 최대 부분 그래프이다(Seidman 1983). k를 키울수록 더 촘촘한 중심 집단만 남는다.
- (잔류점) k를 올릴 때 k-core 밖으로 빠지는 점이다. `k_core_residuals`가 k별 잔류점 수와 비율을 보여 준다.
- (m-core) 강한 관계만 남긴 부분 그래프이다. 가중 그래프는 가중치가 m 이상인 라인을 남긴다. 가중치가 없으면 두 끝점이 공통 이웃을 m명 이상 가진 라인을 남기는 대체 규칙을 쓴다.

> Seidman, S. B.(1983), Network Structure and Minimum Degree, Social Networks 5

## 파당과 완화 개념

파당(clique)은 점 3개 이상이 모두 서로 직접 연결된 최대 집합이다. 조건이 엄격해서 실제 데이터에서는 작은 파당이 여러 개 겹쳐 나오기 쉽다. 그래서 거리 조건을 늘린 개념을 함께 쓴다.

| 기법 | 정의 | 거리를 재는 범위 |
|---|---|---|
| 파당 | 구성원 모두가 서로 직접 연결된 최대 집합 | 거리 1 |
| n-clique | 구성원 모두가 서로 거리 n 이내인 최대 집합 | 집합 밖의 점을 거쳐도 됨 |
| n-clan | 구성원만으로 만든 부분 그래프의 직경도 n 이하인 n-clique | 구성원 사이의 경로만 |
| n-club | 직경이 n 이하인 최대 부분 그래프 | 구성원 사이의 경로만 |

모든 n-clan은 n-clique이면서 n-club이다. n-clique와 n-club은 서로 포함 관계가 성립하지 않을 수 있다(Mokken 1979). n이 3 이상이면 구성원 사이가 멀어져 하나의 집단으로 해석하기 어렵다.

`find_n_clubs`는 근사 탐색이다. 각 점에서 거리 n 이내의 점을 모두 모은 뒤, 직경이 n 이하가 될 때까지 거리 n 안에 닿는 구성원이 가장 적은 점을 하나씩 뺀다. 다른 결과에 포함되는 집합은 버린다. 모든 극대 n-club을 찾는 계산은 규모가 커지면 현실적으로 끝나지 않으므로 이 방식을 쓴다.

> Mokken, R. J.(1979), Cliques, Clubs and Clans, Quality and Quantity

## 네트워크 공개성

공개성은 한 집단 구성원이 가진 관계의 끝점 중 집단 밖을 향하는 비율이다. 0이면 완전히 닫힌 집단, 1이면 관계가 모두 밖으로 향하는 집단이다. 집단 안의 라인은 양 끝에서 한 번씩 세므로 두 번 세어진다. 방향 그래프는 나가는 관계만 센다. `compute_network_openness(G, groups)`를 쓴다.

## NetworkX 함수 대응표

| 기법 | 함수 |
|---|---|
| 밀도 | `nx.density` |
| 유효 규모, 제약 | `nx.effective_size`, `nx.constraint` |
| 컴퍼넌트 | `nx.connected_components`, `nx.strongly_connected_components`, `nx.weakly_connected_components` |
| 노트(양방향 연결 조각) | `nx.biconnected_components` |
| k-core | `nx.k_core`, `nx.core_number` |
| 파당 | `nx.find_cliques` |

## 스크립트 함수

```python
compute_density(G)                     # 밀도, 고립점 수, 포괄성
compute_structural_holes(G)            # 유효 규모, 제약, 효율성
find_components(G)                     # 컴퍼넌트와 고립점
find_cut_points(G)                     # 연계점과 브릿지
find_cycle_components(G)               # 브릿지 제거 후 사이클 덩어리
find_k_cores(G)                        # k별 core 구성원
k_core_residuals(G)                    # k별 잔류점
compute_m_core(G_weighted, m=2)        # 강한 관계만 남긴 그래프
find_cliques(G, min_size=3)            # 극대 파당, 큰 순서
clique_membership(G)                   # 점별 소속 파당 수
find_n_cliques(G, n=2)
find_n_clans(G, n=2)
find_n_clubs(G, n=2)
compute_network_openness(G, blocks)    # 집단별 공개성
```

방향 그래프를 입력하면 k-core, 파당, n-clique 계열, 연계점, 브릿지는 방향을 무시하고 계산한다.

## 결과 해석

- (밀도가 높은 집단) 구성원이 서로 자주 교류해 신뢰와 협력이 쉽지만 외부 정보가 들어오기 어렵다.
- (밀도가 낮은 집단) 협력과 정보 공유가 저절로 일어나기 어렵다. 연결을 만드는 장치가 필요하다.
- (제약이 낮은 점) 서로 연결되지 않은 상대들을 이어 주는 자리로 새로운 정보를 먼저 얻는다.
- (k가 큰 core) 촘촘하게 얽힌 중심 집단이다.
- (여러 파당에 동시에 속한 점) 소집단 사이를 잇는 사람이다.
