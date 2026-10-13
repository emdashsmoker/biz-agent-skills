# 중심성과 집중도

한 점이 네트워크에서 차지하는 위치를 수치로 나타내는 중심성과, 네트워크 전체가 한 점에 쏠린 정도를 나타내는 집중도를 정리한다.

## 중심성을 보는 이유

중심 위치의 행위자는 다른 사람과 많이 교류하고, 눈에 잘 띄며, 서로 떨어진 사람들을 이어 준다. 여러 실증 연구가 중심 위치와 성과의 관계를 보고했다.

| 연구 | 보고된 관계 |
|---|---|
| Brass(1984) | 조직 안 구조적 위치와 개인의 영향력 |
| Ibarra(1993) | 네트워크 중심성과 권력, 혁신 활동 참여 |
| Baldwin, Bedell, Johnson(1997) | 팀 기반 MBA 과정 학생의 네트워크 위치와 만족도, 성과 |
| Burt(1992) | 구조적 틈새가 많은 관리자의 조기 승진 |

> Brass, D. J.(1984), Being in the Right Place: A Structural Analysis of Individual Influence in an Organization, Administrative Science Quarterly 29(4)

> Ibarra, H.(1993), Network Centrality, Power, and Innovation Involvement, Academy of Management Journal 36

> Baldwin, T. T., Bedell, M. D., Johnson, J. L.(1997), The Social Fabric of a Team-Based MBA Program, Academy of Management Journal 40

> Burt, R. S.(1992), Structural Holes: The Social Structure of Competition, Harvard University Press

## 중심성의 분류

- (방향 기준) 들어오는 관계로 재는 내향 중심성은 명성(prestige)을, 나가는 관계로 재는 외향 중심성은 관계를 넓히는 정도를 나타낸다.
- (대상 기준) 한 점의 값은 점 중심성, 그래프 전체의 쏠림은 그래프 중심성(집중도)이다.
- (범위 기준) 직접 이웃만 보는 지표는 로컬 중심성, 전체 점과의 거리를 보는 지표는 글로벌 중심성이다.

| 중심성 | 보는 대상 | 질문 |
|---|---|---|
| 연결정도 | 직접 연결된 점의 수 | 몇 명과 바로 이어져 있는가 |
| 근접 | 다른 점까지의 거리 | 다른 점에 얼마나 가까운가 |
| 매개 | 다른 점 사이 최단 경로 위의 위치 | 다른 점들을 얼마나 이어 주는가 |

## 연결정도 중심성

$$
C_D(i) = d_i, \quad C'_D(i) = \frac{d_i}{g - 1}
$$

d_i는 점 i의 연결정도, g는 점의 수이다. g-1로 나눈 상대값은 크기가 다른 네트워크를 비교할 때 쓴다. 직접 연결만 보므로 네트워크 전체에서의 위치는 반영하지 못한다.

## 근접 중심성

$$
C_C(i) = \frac{1}{\sum_{j} d_{ij}}, \quad C'_C(i) = \frac{g - 1}{\sum_{j} d_{ij}}
$$

d_ij는 점 i와 j 사이의 거리이다. 상대값은 0에서 1 사이이며 클수록 다른 점에 가깝다.

## 매개 중심성

$$
C_B(i) = \sum_{j<k} \frac{g_{jk}(i)}{g_{jk}}, \quad C'_B(i) = \frac{C_B(i)}{(g-1)(g-2)/2}
$$

g_jk는 j와 k 사이 최단 경로의 수, g_jk(i)는 그중 i를 지나는 경로의 수이다. 값이 큰 점은 다른 점들 사이의 정보 흐름을 중개하거나 막을 수 있다.

| 그래프 모양 | 매개 중심성 |
|---|---|
| 스타형 | 중심 점만 상대값 1, 나머지 0 |
| 원형 | 모든 점이 같은 값 |
| 선형 | 가운데 점이 가장 큰 값 |

## NetworkX 계산 규칙

`compute_centralities(G)`는 NetworkX 함수를 그대로 쓰므로 다음 규칙이 결과에 반영된다.

- 연결정도, 근접, 매개 중심성 모두 상대값을 반환한다.
- 방향 그래프의 연결정도 중심성은 인디그리와 아웃디그리의 합을 g-1로 나눈 값이라 0에서 2 사이이다. 방향별 값은 내향 중심성과 외향 중심성 열을 본다.
- 방향 그래프의 근접 중심성은 다른 점에서 들어오는 거리로 계산한다. 나가는 거리 기준 값은 `compute_centralities(transpose_matrix(G))`로 얻는다.
- 연결되지 않은 그래프의 근접 중심성은 Wasserman과 Faust의 보정식(도달 가능한 점의 비율을 평균 거리로 나눈 값)을 쓴다. 연결된 그래프에서는 위 공식과 같은 값이다.

| 지표 | NetworkX 함수 |
|---|---|
| 연결정도 중심성 | `nx.degree_centrality` |
| 내향, 외향 중심성 | `nx.in_degree_centrality`, `nx.out_degree_centrality` |
| 근접 중심성 | `nx.closeness_centrality` |
| 매개 중심성 | `nx.betweenness_centrality` |

## 집중도

집중도는 가장 큰 중심성 값과 각 점 값의 차이를 모두 더한 뒤, 같은 크기의 그래프에서 나올 수 있는 최댓값으로 나눈 값이다(Freeman 1979). 최댓값은 스타형 그래프에서 나오므로 스타형은 1, 모든 점이 같은 값을 가지는 원형은 0이다. 중심성이 한 점의 위치라면 집중도는 네트워크 전체의 구조이다. 밀도가 평균적인 연결 수준을 보여 준다면 집중도는 연결이 고르게 퍼졌는지를 보여 준다.

비방향 그래프에서 `compute_centralization(G)`가 쓰는 분모는 다음과 같다.

| 집중도 | 사용하는 점수 | 분모(최댓값) |
|---|---|---|
| 연결정도 | 연결정도 원값 | (g-1)(g-2) |
| 근접 | 근접 중심성 상대값 | (g-1)(g-2)/(2g-3) |
| 매개 | 매개 중심성 원값 | (g-1)²(g-2)/2 |

$$
C_D = \frac{\sum_{i}[\max_j d_j - d_i]}{(g-1)(g-2)}
$$

근접 집중도는 연결된 그래프에서만 계산하고, 연결되지 않으면 NaN을 반환한다.

방향 그래프에서는 다음을 반환한다.

- (내향, 외향 연결정도 집중도) 인디그리 또는 아웃디그리 원값을 쓰고 분모는 (g-1)²이다. 모든 점이 한 점만 가리키는 그래프에서 내향 집중도가 1이다.
- (매개 집중도) 방향 경로로 센 매개 중심성 원값을 쓰고 분모는 (g-1)²(g-2)이다. 중심 점과 나머지 점이 서로를 가리키는 스타형에서 1이다.
- (근접 집중도) 방향 그래프에서는 계산하지 않고 NaN을 반환한다.

> Freeman, L. C.(1979), Centrality in Social Networks: Conceptual Clarification, Social Networks 1

## 확장 중심성

`compute_extended_centralities(G)`는 아이겐벡터, PageRank, Katz 중심성을 계산한다. 수렴하지 않는 지표는 NaN으로 채운다.

| 중심성 | 함수 | 의미 |
|---|---|---|
| 아이겐벡터 | `nx.eigenvector_centrality` | 중요한 점과 연결될수록 커진다 |
| PageRank | `nx.pagerank` | 들어오는 연결을 연결한 쪽의 점수로 가중한다 |
| Katz | `nx.katz_centrality_numpy` | 멀리 떨어진 연결까지 감쇠 가중치로 더한다 |
| HITS | `nx.hits` | 방향 그래프에서 허브 점수와 권위 점수를 따로 낸다 |

## 결과 해석

- (연결정도 중심성이 높은 점) 직접 교류가 많아 주변 정보가 모이는 자리이다.
- (근접 중심성이 높은 점) 네트워크 전체로 정보를 빠르게 퍼뜨리거나 받을 수 있는 자리이다.
- (매개 중심성이 높은 점) 집단 사이를 잇는 자리이다. 이 점이 빠지면 집단 사이의 흐름이 끊기거나 느려진다.
- (집중도가 1에 가까운 네트워크) 한 점에 연결이 몰려 있어 그 점이 빠지면 네트워크가 흩어질 수 있다.
- (집중도가 0에 가까운 네트워크) 연결이 고르게 퍼져 있다.
