# 데이터 입출력과 규모 대응

파일에서 네트워크를 불러오는 방법, 규모에 따른 분석 전략, 다른 분석 도구와 파일을 주고받는 방법을 정리한다.

## 입력 형식

| 형식 | 함수 | 파일 모양 |
|---|---|---|
| CSV 엣지 리스트 | `load_from_csv(path, format="edges")` | `source,target,weight` |
| CSV 인접 매트릭스 | `load_from_csv(path, format="matrix")` | 첫 열에 노드 이름이 있는 정방 행렬 |
| CSV 사건 매트릭스 | `load_from_csv(path, format="incidence")` | 행은 사람, 열은 활동 |
| 엑셀 | `load_from_excel(path, sheet_name=0, format=...)` | 위 형식 중 하나 |
| 형식 자동 감지 | `load_from_csv(path)` | 아래 규칙 적용 |

형식을 지정하지 않으면 다음 순서로 판단한다.

- 열이 3개 이하이면 엣지 리스트로 본다.
- 행 수와 열 수가 같거나, 첫 열이 이름이고 나머지가 정방 행렬이면 인접 매트릭스로 본다.
- 그 밖에는 사건 매트릭스로 본다.

노드가 3개 이하인 매트릭스는 열 수 때문에 엣지 리스트로 오인될 수 있으므로 `format`을 직접 지정한다.

그 밖의 옵션은 다음과 같다.

- (방향) `directed=True`로 방향 그래프를 만든다.
- (가중치) `weighted=True`이면 엣지 리스트의 세 번째 열이나 매트릭스 칸의 값을 `weight` 속성으로 저장한다. 지정하지 않으면 0 이외의 값을 모두 관계 1로 본다.
- (사건 매트릭스) 반환값은 사전(dict)이다. `"bipartite"`, `"people_projection"`, `"activity_projection"` 키로 세 그래프를 꺼낸다.

### 엣지 리스트 예시

```
source,target,weight
김부장,이과장,3
김부장,박대리,2
이과장,박대리,4
```

```python
G = load_from_csv("network.csv", format="edges", weighted=True)
```

### 인접 매트릭스 예시

```
,A,B,C,D
A,0,1,1,0
B,1,0,0,1
C,1,0,0,1
D,0,1,1,0
```

```python
G = load_from_csv("matrix.csv", format="matrix")
```

### 한글 인코딩

- 기본 인코딩은 utf-8이다.
- 한글이 깨지면 `encoding="utf-8-sig"` 또는 `encoding="cp949"`를 지정한다.
- 내보낼 때는 `export_to_csv(G, path)`를 쓴다. 기본 인코딩 utf-8-sig는 엑셀에서 한글이 깨지지 않는다.

## 규모별 전략

`recommend_strategy(G)`는 노드 수에 따라 분석과 시각화 방식을 추천한다. 반환값의 `strategy`, `visualization`, `algorithms`, `warnings` 키를 확인한다.

| 노드 수 | strategy | 시각화 | 알고리즘 |
|---|---|---|---|
| 1에서 30 | full | 매트릭스와 그래프를 함께 | 모든 알고리즘 사용 가능 |
| 31에서 100 | filtered | 상위 K개 노드를 뽑아서 그림 | REGE와 계층 군집은 계산 시간 증가 |
| 101에서 500 | aggregated | 블록 단위 축소 그래프 | CONCOR 대신 Louvain 권장 |
| 501 이상 | summary_only | 통계 표와 분포 차트만 | Louvain 또는 Label Propagation |

응답 본문에 포함하는 표의 범위는 SKILL.md의 시각화 표(30노드, 50노드 기준)를 따른다.

## 대규모 네트워크 함수

```python
G_top = sample_top_k_nodes(G, k=30, by="betweenness")   # degree, closeness, pagerank도 가능
G_dense = extract_core_subgraph(G, min_degree=3)         # 연결정도 3 미만 점 제거(한 번만 적용)
communities = louvain_communities(G)                     # 점별 커뮤니티 번호
G_reduced = aggregate_to_blocks(G, communities)          # 점은 블록, 가중치는 블록 사이 라인 수
stats = summary_statistics_only(G)                       # 노드 수, 밀도, 컴퍼넌트, 연결정도 분포
print(blocks_summary_markdown(G, communities))           # 블록 간 밀도 표
export_to_csv(G, "outputs/full_matrix.csv", format="matrix")  # 원본 공유용
```

`extract_core_subgraph`는 원래 그래프의 연결정도로 한 번만 거른다. 남은 점끼리 다시 기준을 만족해야 하면 `find_k_cores`를 쓴다.

### CONCOR와 Louvain

| 기준 | CONCOR | Louvain |
|---|---|---|
| 원리 | 상관계수 반복 계산으로 이분할 | 모듈성(modularity)이 커지도록 커뮤니티를 합침 |
| 찾는 대상 | 관계 패턴이 같은 위치(구조적 등위성) | 안쪽 연결이 촘촘한 집단 |
| 계산량 | 노드 수 제곱 크기의 매트릭스를 반복 계산 | 대규모 그래프에서도 빠름 |
| 재현성 | 같은 입력이면 같은 결과 | 무작위 순서를 쓰므로 seed를 고정해야 같은 결과(기본 seed 42) |

두 방법이 찾는 대상은 서로 다르다. 규모 때문에 Louvain으로 바꿨다면 결과는 안쪽 연결이 촘촘한 집단이며 구조적 등위성으로 묶은 위치와 다를 수 있다는 점을 해석에 밝힌다.

## 다른 분석 도구와 파일 주고받기

| 도구 | 확장자 | 내보내기 | 불러오기 |
|---|---|---|---|
| Pajek | .net | `export_to_pajek(G, path)` | `import_from_pajek(path)` |
| Gephi | .gexf | `export_to_gephi(G, path)` | `import_from_gephi(path)` |
| yEd 등 GraphML 도구 | .graphml | `export_to_graphml(G, path)` | `import_from_graphml(path)` |
| UCINET | .dl | `export_to_ucinet_dl(G, path, format=...)` | `import_from_ucinet_dl(path)` |
| 스프레드시트 | .csv | `export_to_csv(G, path)` | `load_from_csv(path)` |

### UCINET DL 형식

내보내기는 라벨을 데이터 안에 포함하는(LABELS EMBEDDED) 두 형식을 지원한다. 라벨에 공백이 있으면 오류를 낸다.

```python
export_to_ucinet_dl(G, "output.dl", format="fullmatrix")
export_to_ucinet_dl(G, "output.dl", format="edgelist1")
```

FULLMATRIX 결과 예시

```
DL N=4
FORMAT = FULLMATRIX
LABELS EMBEDDED
DATA:
 A B C D
A 0 1 1 0
B 1 0 0 1
C 1 0 0 1
D 0 1 1 0
```

EDGELIST1 결과 예시

```
DL N=3
FORMAT = EDGELIST1
LABELS EMBEDDED
DATA:
A B 1
B C 2.5
```

불러오기는 다음 규칙을 따른다.

- FULLMATRIX는 매트릭스가 대칭이면 비방향, 비대칭이면 방향 그래프로 읽는다.
- EDGELIST 계열은 비방향 그래프로 읽는다. 방향 데이터라면 `import_from_ucinet_dl(path, directed=True)`를 쓴다.
- 0과 1 외의 값이 있으면 가중치로 보존한다.

> UCINET 6 for Windows User's Guide(https://pages.uoregon.edu/vburris/hc431/Ucinet_Guide.pdf)

### 형식별 특징

- (Pajek NET) 구조가 단순하고 방향과 가중치를 저장한다.
- (Gephi GEXF) 시각화 속성과 시간에 따라 변하는 네트워크를 저장한다.
- (GraphML) XML 기반이라 여러 도구가 읽으며 노드와 라인의 속성을 자유롭게 저장한다.
- (UCINET DL) UCINET으로 분석한 기존 연구 데이터를 그대로 불러와 재분석할 때 쓴다.

## 실무 사례

### 설문 결과 엑셀 분석

```python
G = load_from_excel("survey_result.xlsx", format="edges", weighted=True)
cent = compute_centralities(G)
```

### 대규모 조직의 부서 간 협업 분석

```python
G = load_from_csv("dept_collab.csv")
plan = recommend_strategy(G)                 # 500개 부서라면 "aggregated"
communities = louvain_communities(G)
G_reduced = aggregate_to_blocks(G, communities)
draw_grouped_network(G_reduced, {n: n for n in G_reduced.nodes()},
                     save_path="outputs/dept_blocks.png")
```

### 기존 UCINET 데이터 재분석

```python
G = import_from_ucinet_dl("published_study.dl")
rege = regular_equivalence(G)
holes = compute_structural_holes(G)
export_to_gephi(G, "outputs/for_gephi.gexf")
```
