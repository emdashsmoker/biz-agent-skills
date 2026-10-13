# 시각화 규칙

그림의 색상, 글꼴, 함수 선택, 레이아웃, 파일 저장 규칙을 정리한다. 색상과 크기 값은 `scripts/nx_toolkit.py` 상단의 상수에 모여 있다.

## 원칙

- (색상) 파스텔 블루를 기본으로 쓰고 강조할 요소에만 파스텔 오렌지를 쓴다.
- (글꼴) 한글을 표시하기 위해 NanumGothic을 쓰고 라벨은 굵게 표시한다.
- (장식 최소화) 그래프 그림에서는 축을 숨기고 막대 차트에서는 위쪽과 오른쪽 테두리를 없앤다. 그림자, 입체 효과, 그라데이션 장식은 쓰지 않는다.
- (라벨) 모든 노드에 이름을 표시하고 막대에는 값을 적는다.
- (범주 색상) 그룹 색상은 10가지 팔레트를 순서대로 쓴다. 그룹이 5개를 넘으면 색 구분이 어려우므로 블록 축소 그래프를 검토한다.

## 팔레트

| 이름 | 값 | 쓰임 |
|---|---|---|
| primary | #8FB8D4 | 노드 기본색 |
| primary_edge | #5783A8 | 노드 테두리 |
| primary_deep | #6B9BBD | 곡선과 강조선 |
| primary_light | #B8D1E2 | 면 채우기 |
| accent | #E5A785 | 강조 노드, 블록 경계선, 임계점 |
| neutral | #7A95A8 | 라인 |
| muted | #8FA3B3 | 히트맵 격자 |

- (그룹 색상) #8FB8D4, #A5CDB5, #EDC491, #CFB0CF, #B8B8B8, #9FC7CF, #E5B5B5, #C0CBA5, #D6C7A5, #B8ADC8
- (히트맵과 중심성 그라데이션) 흰색에서 #7DAECC까지 5단계 파스텔 블루
- (중심성 비교 막대) 연결정도 #4A90B8, 근접 #6DB39A, 매개 #E0A75C

## 글꼴 설정

`setup_font()`가 NanumGothic Regular와 Bold를 등록한다. 그리기 함수는 호출 전에 설정이 없으면 자동으로 한 번 실행한다. 폰트가 없으면 DejaVu Sans로 대체하고 경고를 낸다. 이때 한글이 네모로 표시되므로 `fonts-nanum` 패키지를 설치한 뒤 다시 그린다. 설치가 허용된 격리 환경에서는 `setup_font(install_if_missing=True)`가 설치까지 수행한다.

## 함수 선택

노드가 30개 이하이면 `draw_matrix_and_network`를 기본으로 쓴다. 매트릭스 히트맵과 네트워크 그래프를 만들고 매트릭스의 마크다운 표도 함께 돌려준다.

| 인자 | 쓰임 |
|---|---|
| `centrality_dict` | 노드 크기와 색 농도를 중심성 값에 비례시킨다 |
| `group_dict` | 노드를 그룹별 색으로 칠하고 매트릭스를 그룹 순서로 재정렬하며 그룹 경계에 오렌지 선을 긋는다 |
| `split_files` | True(기본)이면 매트릭스와 그래프를 두 파일로, False이면 좌우로 붙인 한 파일로 저장한다 |
| `save_path` | 저장 경로. split_files=True이면 `이름_matrix.png`, `이름_network.png`, `이름_matrix.md`가 생긴다 |

두 파일로 나누는 기본값은 휴대폰처럼 좁은 화면에서 두 그림을 각각 크게 보기 위한 설정이다.

그래프만 그리는 함수는 노드가 30개를 넘거나, 사용자가 그래프만 요청했거나, 기본 그림에 다른 관점을 덧붙일 때 쓴다. 30개 이하에서 호출하면 경고를 낸다.

| 함수 | 그림 |
|---|---|
| `draw_basic_network` | 기본 그래프 |
| `draw_centrality_network` | 중심성에 따라 크기와 색이 달라지는 그래프 |
| `draw_grouped_network` | 그룹별 색 그래프 |
| `draw_centrality_comparison` | 매개 중심성 상위 노드의 세 중심성 막대 비교 |
| `draw_k_core_nesting` | core 번호가 클수록 크고 진한 노드 |
| `draw_matrix_heatmap` | 매트릭스 히트맵 단독 |
| `draw_bipartite_network` | 사람(원)과 활동(사각형)의 이분 그래프 |
| `draw_uzzi_paradox` | 배태성과 성과의 역U자 개념도 |

## 분석별 기본 그림

- (중심성) `draw_matrix_and_network(G, centrality_dict=...)`로 중심성이 큰 노드를 크고 진하게 그린다.
- (블록모델링) `draw_matrix_and_network(G, group_dict=blocks.to_dict())`로 블록 순서로 재정렬한 매트릭스와 블록별 색 그래프를 그린다.
- (하위집단) 파당, k-core, 컴퍼넌트 소속을 `group_dict`로 넘긴다. 한 노드가 여러 파당에 속하면 대표 소속 하나를 골라 넘기고, 나머지 소속은 `clique_membership` 표로 보여 준다.
- (방향 그래프) 화살표를 표시한다.

## 규모에 따른 표 출력

- 노드 30개 이하에서는 `matrix_to_markdown(G)`가 전체 매트릭스를 표로 만든다.
- 노드 31개에서 50개 사이에서 블록 순서 매트릭스를 모두 보여 주려면 `matrix_to_markdown(G, reorder_by=blocks.to_dict(), max_size=50)`처럼 `max_size`를 올린다. 기본값을 쓰면 연결정도 상위 30개만 발췌하고 캡션에 발췌 사실을 적는다.
- 노드가 50개를 넘으면 `blocks_summary_markdown(G, blocks)`로 블록 간 밀도 표를 보여 주고 원본은 `export_to_csv`로 파일을 만든다.
- 매트릭스 히트맵은 노드 20개 이하에서만 칸에 숫자를 적는다. 가중 그래프는 소수 첫째 자리까지 적는다.

## 레이아웃

| 레이아웃 | 맞는 경우 | 함수 |
|---|---|---|
| spring | 일반 네트워크, 기본값 | `nx.spring_layout` |
| circular | 원형 구조, 대칭 강조 | `nx.circular_layout` |
| kamada_kawai | 그림 위 거리가 경로 거리와 비슷해야 할 때 | `nx.kamada_kawai_layout` |
| shell | 동심원 계층 | `nx.shell_layout` |
| bipartite | 이분 네트워크 | `draw_bipartite_network`가 좌우 배치 |

spring 레이아웃은 seed를 42로 고정해 같은 데이터에서 같은 배치를 만든다.

## 파일 저장

- 파일은 사용 환경이 사용자에게 전달할 수 있는 산출 폴더(예를 들어 `outputs/`)에 설명적인 이름으로 저장한다. 폴더가 없으면 자동으로 만든다.
- 해상도는 150 DPI이다. 인쇄용이 필요하면 `SAVE_DPI`를 300으로 바꾼다.
- 배경은 흰색으로 저장한다.
- 기본 크기는 그래프 10x8인치, 막대 차트 10x6인치, 좌우 병합 그림 15x7인치이다. 분리 저장 시 매트릭스는 노드 수에 따라 6에서 10인치 정사각형, 그래프는 8에서 12인치 폭이다.
- 저장한 뒤 파일이 실제로 생겼는지 확인하고, 파일 전달 기능으로 보낸다. 응답 본문에 이미지 마크다운 구문을 포함하지 않는다.

## 라벨 겹침

노드가 많아 라벨이 겹치면 `adjustText` 패키지로 위치를 조정할 수 있다. 설치되어 있지 않으면 이 단계를 건너뛴다.

```python
try:
    from adjustText import adjust_text

    def draw_adjusted_labels(G, pos, ax):
        texts = [ax.text(x, y, str(n), fontsize=10, fontweight="bold")
                 for n, (x, y) in pos.items()]
        adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle="-", color="gray", lw=0.5))
except ImportError:
    draw_adjusted_labels = None
```

이 함수를 쓸 때는 `nx.draw_networkx_labels` 대신 호출한다.

## 그림 점검

그림을 전달하기 전에 이미지를 직접 열어 다음을 확인한다.

- 글자가 잘리거나 네모로 깨지지 않았는가
- 라벨과 노드, 범례가 서로 겹치지 않았는가
- 매트릭스 값과 그래프의 라인이 입력 데이터와 일치하는가
- 그룹 색과 범례가 1대1로 대응하는가
