# 차트

메시지를 먼저 정하고, 메시지가 말하는 비교 유형을 찾고, 그 비교에 맞는 형태를 고른다. 색, 글꼴, 제목 위치, 피할 패턴, 시각 검증은 visual.md를 따른다.

## 형태 고르기

- 순서는 메시지 결정, 비교 유형 파악, 차트 형태 선택이다.
- 사용자가 형태를 지정하지 않으면 데이터를 코드로 살펴 비교 유형을 판단하고 근거와 함께 형태를 제안한다.
- 사용자가 기획안 없이 바로 만들어 달라고 하면 비교 유형에 따라 형태를 자동으로 골라 바로 만든다.

| 비교 유형 | 요청에 나오는 단서 | 형태 |
|-----------|-------------------|------|
| 구성비 | 비율, 점유율, 구성 | 원 차트(6조각 이하), 누적 막대 |
| 항목 비교 | 크다, 작다, 순위, 격차 | 수평 막대 |
| 시계열 | 변화, 추이, 성장 | 수직 막대, 꺾은선 |
| 도수분포 | 구간, 빈도, 분포 | 히스토그램 |
| 상관 | 상관, 관계, 함께 움직임 | 산점도 |
| 매트릭스 | 맵, 행렬, 교차표 | 버블, 히트맵 |

- 시계열은 시점이 적으면 수직 막대, 많으면 꺾은선을 쓴다. 수직 막대의 시점은 12개 이하로 유지한다.

## 데이터 다듬기

- 범주가 5개를 넘으면 상위 4-5개를 남기고 나머지를 "기타"로 합친다. 원 차트는 6조각을 넘지 않는다.
- 시계열이 12개 시점을 넘으면 최근 12개로 자르거나 메시지에 필요한 구간만 남기기를 제안한다.
- 시계열이 아닌 범주는 값의 내림차순으로 정렬한다. "기타"는 순위와 무관하게 맨 끝에 둔다.
- 합계, 비율, 순위, 정렬은 모두 코드로 계산한다.

## 공통 규격

- 배경은 흰색이나 투명으로 두고 차트 바깥 테두리는 쓰지 않는다.
- 데이터는 #6B8EC2로 칠하고 메시지 대상 1곳만 #C0392B로 칠한다. 비교 대상 계열은 명도 단계로 낮춘다.
- 모든 글자는 NanumGothic Bold로 쓰고 기본 16pt, 최소 12pt로 한다.
- 범주 이름은 축에, 수치는 데이터 라벨에 표시한다.
- 축선은 수평 막대는 왼쪽, 수직 막대는 아래쪽, 꺾은선과 산점도는 왼쪽과 아래쪽만 남긴다. 버블과 히트맵은 칸의 경계를 보여야 하므로 네 면을 남긴다.
- 축 이외의 격자는 지운다. 가독성에 꼭 필요하면 최소한의 보조선만 선택해 쓴다.
- 범례는 최소화하고 직접 라벨로 대체한다. 범례만으로 데이터를 구분하게 하지 않는다.
- 축 라벨에는 단위를 적는다(예: 매출(억 원)).
- 막대 길이는 값에 비례해야 하므로 막대 차트의 값 축은 0에서 시작한다.
- 구성 요소를 최소화해 데이터를 표현하는 잉크의 비율을 높인다.
- 범주 구분은 겹침 없이 전체를 덮게 나누고 범주와 색을 1:1로 대응시킨다.

## 데이터 라벨

- 값 축을 지운 차트(막대, 원, 버블, 히트맵)는 모든 데이터 도형에 값을 직접 표시해 독자가 축을 보지 않아도 읽게 한다.
- 꺾은선은 값 축을 유지하고 끝점과 강조 지점처럼 메시지와 관련된 지점에 라벨을 붙인다.
- 산점도는 항목명이 있는 점마다 "항목명\n(x, y)" 형식으로 라벨을 붙인다.
- 라벨 형식은 수치("850"), 비율("26%"), 수치와 비율("850(26%)"), 수치와 순위("850(1위)") 중에서 고른다.
- 소수점은 기본 0자리로 하고 사용자가 지정하면 1-2자리로 한다.
- 라벨이 겹치면 자동 배치(matplotlib에서는 adjustText 패키지), 막대 라벨 위치 조정(`bar_label`), 여백 자동 조정(`tight_layout`), 라벨 회전, 수동 배치 순서로 해결한다.
- 사용자가 표본 수 표시를 요청하면 오른쪽 위에 "(n=2,220)" 형식으로 12pt 크기로 적는다. 산점도에는 적지 않는다. 다른 요소와 겹치면 위치를 조정한다.

## 차트별 규격

- (수평 막대) 항목 비교에 쓴다. 범주는 Y축, 수치는 막대 끝 라벨로 표시하고 왼쪽 축선만 남긴다.
- (수직 막대) 시계열에 권장한다. 범주는 X축, 수치는 막대 위 라벨로 표시하고 아래쪽 축선만 남긴다.
- (꺾은선) X축은 시점, Y축은 수치로 두고 Y축 라벨을 표시한다. 왼쪽과 아래쪽 축선을 남긴다.
- (산점도) 왼쪽과 아래쪽 축선을 남기고 점 라벨은 "항목명\n(x, y)"로 쓴다.
- (버블) 네 면 축선을 남긴다. Y축 항목은 visual.md의 범주 명도 단계로 구분한다. 버블 면적(matplotlib `s`)은 값의 10배를 기본으로 하고 데이터 범위에 맞게 조정한다. X축 라벨은 "분류명\n(열 합계)"로 쓰고 버블 안에 수치를 적는다. 값이 0인 칸은 ▽로 표시한다.
- (히트맵) 네 면 축선을 남긴다. #EDF1F8부터 #2C466D까지 네이비 단일 계열의 농도로 값을 표현한다. 칸 안 수치의 글자색은 visual.md의 대비 규칙으로 고른다. 색 막대(colorbar)는 기본으로 두지 않는다.
- (원) 6조각 이하로 만들고 12시 방향에서 시작해 시계 방향으로 큰 값부터 배치한다. 조각 색은 visual.md의 범주 구분 규칙을 따르고 조각 경계는 흰 선(2px)으로 나눈다. 라벨은 조각 안에 "항목명\n(00%)"로 적고 지시선은 쓰지 않는다.

## matplotlib을 쓸 때

- 세션을 시작하면 설치된 matplotlib 버전과 글꼴 설치 여부를 코드로 확인한다. 사용자가 웹 검색을 허용했으면 설치 버전의 변경 사항(추가된 기능, 폐기된 기능)을 확인한다.
- adjustText가 없으면 설치하고 NanumGothic이 없으면 설치한다.
- matplotlib 기본 색과 기본 축선을 그대로 쓰지 않도록 설정을 코드 상단에 둔다.

```python
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager

FONT_PATH = Path("NanumGothic-Bold.ttf")  # 설치한 글꼴 파일 위치
COLOR_TEXT = "#1A1A1A"
COLOR_SUB = "#595959"
COLOR_DATA = "#6B8EC2"
COLOR_ACCENT = "#C0392B"
FONT_SIZE = 16

font_manager.fontManager.addfont(str(FONT_PATH))
plt.rcParams["font.family"] = font_manager.FontProperties(fname=str(FONT_PATH)).get_name()
plt.rcParams["font.weight"] = "bold"
plt.rcParams["font.size"] = FONT_SIZE
plt.rcParams["axes.unicode_minus"] = False  # 한글 글꼴에서 음수 기호가 깨지지 않게 함

labels = ["영업4팀", "영업3팀", "영업2팀", "영업1팀"]  # 오름차순 입력이 위에서부터 내림차순으로 그려짐
values = [410, 650, 720, 850]
colors = [COLOR_ACCENT if name == "영업1팀" else COLOR_DATA for name in labels]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(labels, values, color=colors)
ax.bar_label(bars, padding=6, color=COLOR_TEXT)
for side in ("top", "right", "bottom"):
    ax.spines[side].set_visible(False)
ax.spines["left"].set_color(COLOR_SUB)
ax.xaxis.set_visible(False)
ax.tick_params(axis="y", length=0)
fig.tight_layout()
fig.savefig("chart.png", dpi=200)
```

- 원 차트는 `ax.pie(values, startangle=90, counterclock=False)`로 12시 방향 시계 방향 배치를 만든다. matplotlib 원 차트의 기본 진행 방향은 반시계 방향이다.

## 점검

- 메시지를 먼저 정하고 비교 유형에 맞는 형태를 골랐는가
- 강조색이 메시지 대상 1곳에만 있는가
- 기준에 맞게 데이터 라벨을 직접 표시했는가
- 축선, 격자, 범례를 규격대로 정리했는가
- 축 라벨에 단위가 있는가
- 막대 차트 값 축이 0에서 시작하는가
- 차트의 수치가 원본 데이터와 일치하는가

## 참고 문헌

- Gene Zelazny, Say It With Charts(국내 번역서 "맥킨지, 차트의 기술"). 메시지, 비교 유형, 차트 형태 순서로 차트를 고르는 방식의 출처다.
- Gene Zelazny, Say It With Presentations(국내 번역서 "맥킨지, 발표의 기술"). 시각 자료 1개에 메시지 1개를 담는 원칙의 출처다.
- Statistics Canada, Pie chart(https://www150.statcan.gc.ca/n1/edu/power-pouvoir/ch9/pie-secteurs/5214826-eng.htm). 원 차트 6조각 이하, 12시 방향 시작, 큰 값부터 시계 방향 배치 기준이다.
- W3C, Understanding Success Criterion 1.4.11 Non-text Contrast(https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html). 그래픽 요소 대비 3:1 기준이다.
