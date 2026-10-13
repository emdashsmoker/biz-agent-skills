---
name: network-analysis
description: 소셜 네트워크 분석(SNA)을 NetworkX 코드로 계산하고 시각화하는 스킬. 인접 매트릭스, 엣지 리스트, 사건 매트릭스, CSV와 엑셀 파일, UCINET, Pajek, Gephi 파일, 관계를 설명한 문장을 받아 밀도, 중심성과 집중도, 구조적 틈새, 컴퍼넌트, 파당과 n-clique, k-core, 구조적 등위성, 블록모델링(CONCOR, REGE), 경로와 거리, 이분 네트워크를 분석한다. 사용자가 네트워크 분석, SNA, 연결망, 중심성, 매개 중심성, 밀도, 구조적 틈새, 사회적 자본, 블록모델링, 파당, k-core, 인접 매트릭스, 엣지 리스트, 에고 네트워크, 조직 네트워크, 중개자, 배태성, NetworkX, UCINET, Pajek, Gephi를 언급하거나 사람, 부서, 기업, 국가 사이의 관계 데이터를 주고 분석이나 시각화를 요청하면 이 스킬을 사용한다. 계산은 scripts/nx_toolkit.py로 수행한다. 요청에 맞춰 references/data_io.md(파일 입출력과 대규모 처리), references/graph_theory.md(경로, 거리, 연결정도), references/cohesion_subgroups.md(밀도, 구조적 틈새, 하위집단), references/centrality.md(중심성과 집중도), references/equivalence.md(등위성과 블록모델링), references/concepts_theory.md(개념과 이론), references/visualization.md(시각화 규칙)를 읽고 응답 구조는 assets/report_template.md를 따른다.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# 소셜 네트워크 분석

관계 데이터를 그래프로 바꾸고 지표를 계산한 뒤 매트릭스, 그림, 해석을 함께 제시한다. 모든 수치는 `scripts/nx_toolkit.py`를 실행해 얻는다. 수치를 암산이나 추정으로 적으면 같은 데이터로 같은 결과를 재현할 수 없기 때문이다.

## 준비

분석을 시작하기 전에 실행 환경을 한 번 점검한다.

- Python 3과 `networkx`(3.x), `pandas`, `numpy`, `scipy`, `matplotlib`이 필요하다. 엑셀 파일을 읽을 때는 `openpyxl`이 추가로 필요하다.
- 스크립트는 스킬 폴더의 `scripts` 경로를 `sys.path`에 추가한 뒤 `from nx_toolkit import *`로 불러온다.
- 표의 열 이름, 캡션, 차트 문구의 언어는 `LANG` 값이 정한다. 기본값은 `"ko"`이다.
- 한글을 그림에 표시하려면 NanumGothic 폰트가 필요하다. 코드 첫머리에서 `setup_font()`를 호출한다. 폰트가 없고 시스템 패키지 설치가 허용된 격리 환경이라면 `setup_font(install_if_missing=True)`로 설치한다. 그 외 환경에서는 사용자에게 `fonts-nanum` 설치를 안내한다.

```python
import sys
sys.path.insert(0, "<스킬 폴더>/scripts")
from nx_toolkit import *
setup_font()
```

## 작업 순서

모든 요청은 불러오기, 해석, 참고 문서 선택, 계산, 시각화, 보고 순서로 처리한다.

### 1. 데이터 불러오기

사용자가 파일을 준 경우 형식에 맞는 함수로 읽는다. 사용자에게 데이터를 파이썬 리스트로 다시 옮겨 적게 하지 않는다.

| 입력 | 함수 |
|---|---|
| CSV 엣지 리스트 | `load_from_csv(path, format="edges")` |
| CSV 인접 매트릭스 | `load_from_csv(path, format="matrix")` |
| CSV 사건 매트릭스 | `load_from_csv(path, format="incidence")` |
| 엑셀 | `load_from_excel(path, sheet_name=0)` |
| UCINET DL | `import_from_ucinet_dl(path)` |
| Pajek NET | `import_from_pajek(path)` |
| Gephi GEXF | `import_from_gephi(path)` |
| 대화창에 적힌 매트릭스 | `load_from_matrix(matrix, labels=[...])` |
| 대화창에 적힌 관계 목록 | `load_from_edges(edges)` |

형식 자동 감지 규칙과 한글 인코딩 처리는 `references/data_io.md`에 있다. 불러온 직후 `recommend_strategy(G)`로 규모별 전략을 확인한다.

### 2. 요청 해석

요청에서 다음 항목을 파악한다.

- (데이터) 매트릭스, 관계 목록, 관계 서술 중 무엇이 주어졌는가
- (질문) 어떤 지표나 기법을 원하는가
- (용도) 개념 학습, 연습 문제 풀이, 실무 진단 중 무엇인가

데이터 없이 개념만 물으면 노드 5개에서 10개 규모의 가상 네트워크를 만들어 시연한다. 가상 데이터라는 사실은 결과에 밝힌다.

### 3. 참고 문서 선택

질문에 해당하는 문서만 읽는다. 기법 하나를 묻는 요청은 문서 1개, 여러 기법을 묻는 요청은 2개에서 3개를 읽는다.

| 질문 키워드 | 문서 |
|---|---|
| 파일 로딩, CSV, 엑셀, 대량 데이터, UCINET, Pajek, Gephi 연동 | `references/data_io.md` |
| 궤적, 경로, 사이클, 거리, 직경, 연결정도, 인디그리, 아웃디그리, 매트릭스 | `references/graph_theory.md` |
| 밀도, 구조적 틈새, 사회적 자본, 컴퍼넌트, 파당, k-core, n-clique | `references/cohesion_subgroups.md` |
| 중심성, 집중도, PageRank | `references/centrality.md` |
| 구조적 등위성, 블록모델링, CONCOR, REGE, 이미지 매트릭스 | `references/equivalence.md` |
| 관계 유형, 강한 연결과 약한 연결, 조직 내 역할, 배태성, Uzzi 역설 | `references/concepts_theory.md` |
| 그림, 매트릭스 히트맵, 레이아웃, 색상 | `references/visualization.md` |

### 4. 계산

수식을 보고 결과를 짐작하지 않고 코드를 실행해 값을 얻는다. 자주 쓰는 함수는 아래와 같다.

- (기본 정보) `describe_graph`, `compute_density`, `compute_degree_stats`, `compute_distances`
- (중심성) `compute_centralities`, `compute_centralization`, `compute_extended_centralities`
- (하위집단) `find_components`, `find_cut_points`, `find_k_cores`, `find_cliques`, `find_n_cliques`, `find_n_clans`, `find_n_clubs`
- (구조적 틈새) `compute_structural_holes`
- (등위성) `euclidean_equivalence`, `correlation_equivalence`, `regular_equivalence`, `blockmodel`, `image_matrix`

결과는 pandas DataFrame이나 Series로 돌아온다. 표로 옮길 때는 `dataframe_to_markdown`을 쓴다.

### 5. 시각화

그림과 마크다운 표를 함께 제시한다. 노드 수에 따라 방식을 고른다.

| 노드 수 | 매트릭스 표 | 결과 표 | 그림 |
|---|---|---|---|
| 30 이하 | 전체 매트릭스 | 전체 결과 | `draw_matrix_and_network`로 매트릭스와 그래프를 함께 |
| 31에서 50 | 블록 순서로 재정렬한 매트릭스 또는 상위 30개 노드 발췌 | 상위 10개, 전체는 CSV | 그래프 단독 |
| 51 이상 | 블록 간 밀도 요약(`blocks_summary_markdown`), 원본은 CSV | 상위 10개, 전체는 CSV | 블록 축소 그래프 |

노드가 30개 이하이면 `draw_matrix_and_network`만 쓴다. 매트릭스는 분석의 원자료이고 그래프는 그 해석이므로 둘을 나란히 보여야 독자가 결과를 검산할 수 있다. `draw_basic_network`, `draw_centrality_network`, `draw_grouped_network`처럼 그래프만 그리는 함수는 다음 세 경우에만 쓴다.

- 노드가 30개를 넘어 매트릭스를 읽기 어려운 경우
- 사용자가 그래프만 보여 달라고 요청한 경우
- `draw_matrix_and_network` 결과를 보여 준 뒤 다른 관점의 그림을 덧붙이는 경우

30노드 이하의 표준 코드는 다음과 같다.

```python
cent = compute_centralities(G)
result = draw_matrix_and_network(
    G, title="영업본부 협업",
    centrality_dict=cent["매개_중심성"].to_dict(),
    save_path="outputs/sales_network.png",
)
print(build_response_block(G, "영업본부 협업", result, cent))
```

`build_response_block`은 매트릭스 표, 결과 표, 그림 파일 목록을 한 번에 조립한다. 출력된 블록을 응답 본문에 그대로 옮긴다. 그림 파일은 사용 환경의 파일 전달 기능으로 따로 보낸다. 색상과 레이아웃 규칙은 `references/visualization.md`에 있다.

### 6. 보고

`assets/report_template.md`의 틀을 따른다. 데이터를 준 분석 요청, 개념 설명 요청, 연습 문제 풀이 요청에 각각 맞는 틀이 있다. 분석 요청의 응답에는 다음 요소가 들어간다.

- 질문 해석과 적용한 기법
- 처리 과정을 보여 주는 Mermaid 흐름도
- 각 기법의 정의, LaTeX 수식, 파이썬 코드
- 입력 매트릭스 표와 결과 표
- 그림 파일(별도 전달)
- 결론과 실무 시사점

## 응답 전 확인

응답을 보내기 전에 다음 항목을 확인한다. 하나라도 빠졌다면 보완한 뒤 보낸다.

- 입력 매트릭스 마크다운 표(`result["markdown"]` 또는 `build_response_block` 출력)가 본문에 있는가
- 분석 결과 표(`dataframe_to_markdown` 출력)가 본문에 있는가
- 그림 파일이 실제로 생성되었고 파일 전달 기능으로 보냈는가
- 본문에 `![설명](파일.png)` 형태의 이미지 구문을 쓰지 않았는가

마지막 항목을 두는 이유는 채팅 화면이 로컬 파일 경로의 이미지를 대부분 표시하지 못해 깨진 링크만 남기 때문이다. 본문에는 "그림 파일 별도 전달" 정도의 문장만 적는다. 생성에 실패한 파일은 언급하지 않는다.

## 계산 규칙

결과 수치를 바꾸는 규칙이므로 해석할 때 함께 밝힌다.

- 방향 그래프의 연결정도 중심성은 인디그리와 아웃디그리의 합을 쓰므로 0에서 2 사이 값을 가진다. 방향을 나눠 보려면 내향 중심성과 외향 중심성 열을 본다.
- 방향 그래프의 근접 중심성은 다른 점에서 들어오는 거리로 계산한다. 나가는 거리를 보려면 `transpose_matrix(G)`로 방향을 뒤집어 계산한다.
- 연결되지 않은 그래프의 근접 중심성은 도달 가능한 점의 비율로 보정한 값이다.
- CONCOR는 한 번 나눌 때마다 모든 블록을 둘로 쪼개므로 블록 수를 2, 4, 8처럼 2의 거듭제곱으로 정한다.
- `find_n_clubs`는 근사 탐색이다. 결과에 없는 n-club이 존재할 수 있다.
- `draw_uzzi_paradox`의 곡선과 임계점 위치는 개념을 보여 주기 위해 정한 값이다.

## 다른 분석 도구 질문

UCINET, Pajek, Gephi의 메뉴 조작을 묻는 질문에는 같은 분석을 NetworkX로 수행하는 방법을 제시한다. 결과를 해당 도구로 옮겨야 하면 `export_to_ucinet_dl`, `export_to_pajek`, `export_to_gephi`로 파일을 만든다.
