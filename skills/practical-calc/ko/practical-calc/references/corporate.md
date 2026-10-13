# 기업 재무 지표

손익계산서, 현금흐름표, 재무상태표 숫자로 수익성, 투자 규모, 손익분기점을 계산한다. 계정 이름은 한국채택국제회계기준(K-IFRS)의 기능별 손익계산서 표시를 따른다.

## 손익 요약

기간별 손익 항목을 받아 매출총이익, 영업이익, EBITDA, OPEX와 이익률을 구하고 두 기간을 비교한다.

### 용어와 산식

| 지표 | 산식 |
|---|---|
| 매출총이익 | 매출액 - 매출원가 |
| 영업이익 | 매출총이익 - 판매비와관리비 (입력값이 있으면 입력값 사용) |
| EBITDA(영업이익 기준) | 영업이익 + 감가상각비 + 무형자산상각비 |
| EBITDA(당기순이익 기준) | 당기순이익 + 법인세비용 + 이자비용 + 감가상각비 + 무형자산상각비 |
| OPEX | 매출원가 + 판매비와관리비 - 감가상각비 - 무형자산상각비 |
| 이익률 | 각 이익 / 매출액 |
| 매출액 대비 OPEX | OPEX / 매출액 |

- EBITDA는 회계기준이 정한 지표가 아니어서 회사마다 계산법이 다르다. 이 도구는 영업이익 기준을 기본으로 쓴다. 2027년부터 적용되는 IFRS 18은 "감가상각, 상각, IAS 36 범위 손상 전 영업이익"을 경영진이 정의한 성과 측정치(MPM)로 보지 않는다. 이 도구의 영업이익 기준 EBITDA에 손상차손을 더하면 그 지표와 같아진다.
- 당기순이익 기준 EBITDA는 이자수익, 기타수익, 기타비용 같은 영업외 손익을 포함한다. 두 기준의 차이는 이자비용을 제외한 영업외 손익의 합계와 같다.
- 손상차손을 더한 변형 EBITDA를 쓰려면 보고서에 가산 항목을 밝힌다.
- OPEX는 이 도구에서 감가상각비와 무형자산상각비를 제외한 영업비용으로 정의하며 매출액 - EBITDA와 같다. 감가상각비는 과거 CAPEX를 기간에 나눈 금액이므로 OPEX에서 제외해야 CAPEX와 겹치지 않는다. 판매비와관리비만 OPEX로 부르는 관행도 있으므로 보고서에는 정의를 함께 적는다.
- 입력한 영업이익과 계산한 영업이익(매출총이익 - 판매비와관리비)이 매출액의 0.5%보다 크게 다르면 스크립트가 알린다. 기타영업수익이나 기타영업비용을 영업이익에 포함하는 회사에서 주로 생긴다.

### 비교와 점검 표시

`--compare` 기간 대비 `--current` 기간의 증감액과 증감률을 구한다. 두 옵션을 생략하면 마지막 열을 바로 앞 열과 비교한다. 증감률 절댓값이 `--threshold-pct`(기본값 10) 이상이거나 증감액 절댓값이 `--threshold-amount` 이상이면 점검 열에 O를 표시한다. 점검 표시는 변동의 크기만 나타내므로 비용 항목의 증가와 이익 항목의 증가는 해석 방향이 반대다. 조직에 정해진 중요성 기준이 있으면 그 값을 입력한다. 이익률 변동은 %p로 표시한다.

### 입력 수집 순서

1. 기간별 손익 항목(매출액, 매출원가, 판매비와관리비, 감가상각비, 무형자산상각비는 EBITDA와 OPEX 계산에 필요)
2. 분석 기간과 비교 기간
3. 점검 기준(증감률, 증감액)

### 입력 형식

첫 열 `item`에 계정 이름, 나머지 열에 기간별 금액을 둔다. 인식하는 계정 이름은 매출액, 매출원가, 판매비와관리비, 영업이익, 감가상각비, 무형자산상각비, 이자비용, 법인세비용, 당기순이익과 각각의 영문 이름(revenue, cogs, sga, operating_income, depreciation, amortization, interest_expense, income_tax, net_income)이다. 무형자산상각비 행이 없으면 0으로 보고 알린다. 인식하지 못한 계정은 계산에서 제외하고 목록을 알린다.

```
item,2024,2025
매출액,1000,1150
매출원가,620,700
판매비와관리비,250,270
감가상각비,40,45
무형자산상각비,10,12
```

### 실행 예시

```
python scripts/pl_summary.py --input examples/pl.csv --unit 억원 --chart operating_profit_bridge.png
```

차트는 비교 기간 영업이익에서 매출액, 매출원가, 판매비와관리비 변동을 거쳐 당기 영업이익에 이르는 폭포 차트다.

## CAPEX

CAPEX(자본적 지출)는 유형자산과 무형자산을 새로 취득하거나 성능을 높이는 데 쓴 지출이다. 비용으로 바로 처리하지 않고 자산으로 올린 뒤 감가상각으로 나누어 비용화한다.

### 산식

| 지표 | 산식 |
|---|---|
| CAPEX(현금흐름표 기준) | 유형자산의 취득 + 무형자산의 취득 |
| CAPEX(재무상태표 증감 추정) | 기말 순유형자산 - 기초 순유형자산 + 감가상각비 + 처분 자산 장부가액 + 손상차손 |
| 매출액 대비 CAPEX | CAPEX / 매출액 |
| 잉여현금흐름(FCF) | 영업활동현금흐름 - CAPEX |

- 현금흐름표 투자활동의 취득 금액이 있으면 그 값을 쓴다. 없을 때만 재무상태표 증감으로 추정한다.
- 증감 추정은 재평가, 환율 변동, 사업결합으로 늘어난 자산을 구분하지 못한다. 스크립트는 추정값을 쓴 기간을 알린다.
- 무형자산의 기초, 기말 잔액과 무형자산상각비를 함께 주면 무형자산분도 같은 방식으로 더한다.

### 감가상각 일정

계획한 CAPEX가 연도별 비용으로 어떻게 나뉘는지 계산한다.

| 방법 | 연간 감가상각비 |
|---|---|
| 정액법(`straight`) | (취득원가 - 잔존가치) / 내용연수 |
| 정률법(`declining`) | 기초 장부가액 x 상각률, 상각률 = 1 - (잔존가치 / 취득원가)^(1 / 내용연수) |

정률법은 이 상각률을 쓰면 마지막 해 말 장부가액이 잔존가치와 같아진다. 잔존가치가 0이면 상각률이 100%가 되므로 정률법에는 0보다 큰 잔존가치가 필요하다.

### 입력 수집 순서

1. 기간별 유형자산, 무형자산 취득 금액 또는 기초, 기말 잔액과 감가상각비
2. 기간별 매출액과 영업활동현금흐름(매출액 대비 CAPEX와 FCF에 필요)
3. 감가상각 일정이 필요한 자산의 취득원가, 잔존가치, 내용연수, 시작 연도, 상각 방법

### 입력 형식

```json
{
  "unit": "억원",
  "periods": [
    {"period": "2024", "ppe_purchase": 90, "intangible_purchase": 8, "revenue": 1000, "operating_cash_flow": 150},
    {"period": "2025", "net_ppe_begin": 400, "net_ppe_end": 440, "depreciation": 45, "ppe_disposals_nbv": 5, "revenue": 1150, "operating_cash_flow": 175}
  ],
  "assets": [
    {"name": "생산 설비", "cost": 100, "residual": 10, "life": 5, "start_year": 2026, "method": "straight"}
  ]
}
```

무형자산 증감 추정에는 `net_intangible_begin`, `net_intangible_end`, `amortization`, `intangible_disposals_nbv`, `intangible_impairment`를 쓰고 유형자산 손상차손은 `ppe_impairment`로 입력한다.

### 실행 예시

```
python scripts/capex.py --input examples/capex.json --chart capex.png
```

## 손익분기점

손익분기점(BEP)은 매출로 고정비와 변동비를 모두 회수하여 영업이익이 0이 되는 판매량 또는 매출액이다.

### 산식

| 지표 | 산식 |
|---|---|
| 단위 공헌이익 | 단가 - 단위 변동비 |
| 공헌이익률 | 단위 공헌이익 / 단가 |
| 손익분기 판매량 | 고정비 / 단위 공헌이익 |
| 손익분기 매출액 | 고정비 / 공헌이익률 |
| 목표이익 달성 판매량 | (고정비 + 목표 세전이익) / 단위 공헌이익 |
| 목표 세전이익 | 목표 세후이익 / (1 - 법인세율) |
| 안전한계 매출액 | 현재 매출액 - 손익분기 매출액 |
| 안전한계율 | 안전한계 매출액 / 현재 매출액 |
| 영업레버리지도(DOL) | 공헌이익 / 영업이익 |

- 제품이 여럿이면 판매량 구성비(`mix`)로 가중평균한 단가와 단위 공헌이익을 쓴다. 손익분기 판매량을 구성비대로 나누면 제품별 손익분기 판매량이 된다. 구성비 합이 1이 아니면 비율로 환산하고 알린다.
- `tax_rate`를 주면 `target_profit`을 세후이익으로 보고 세전이익으로 바꾼다. `tax_rate`가 없으면 `target_profit`을 세전이익으로 본다.
- `current_units`는 구성비를 유지한 전체 판매량이다.
- DOL은 매출이 1% 변할 때 영업이익이 몇 % 변하는지 나타내며 영업이익이 0 이하이면 산출하지 않는다.
- 이 계산은 단가, 단위 변동비, 고정비, 구성비가 판매량 범위 안에서 일정하다는 가정을 둔다.

### 입력 수집 순서

1. 고정비
2. 제품별 단가, 단위 변동비, 판매량 구성비
3. 목표이익과 법인세율(목표 판매량이 필요할 때)
4. 현재 판매량(안전한계와 DOL이 필요할 때)

### 입력 형식

```json
{
  "unit": "원",
  "fixed_cost": 120000000,
  "products": [
    {"name": "기본형", "price": 30000, "variable_cost": 18000, "mix": 0.7},
    {"name": "고급형", "price": 50000, "variable_cost": 27000, "mix": 0.3}
  ],
  "target_profit": 40000000,
  "tax_rate": 0.2,
  "current_units": 12000
}
```

### 실행 예시

```
python scripts/bep.py --input examples/bep.json --chart bep.png
```

차트는 판매량에 따른 매출액선과 총비용선, 두 선이 만나는 손익분기점을 보여 준다.

## 출처

> IFRS Foundation(2024), IFRS 18 Presentation and Disclosure in Financial Statements: Effects Analysis(https://www.ifrs.org/content/dam/ifrs/publications/amendments/english/2024/effect-analysis-ifrs18-april2024.pdf)

> OpenStax(2022), Principles of Finance 5.6 Operating Cash Flow and Free Cash Flow to the Firm(https://openstax.org/books/principles-finance/pages/5-6-operating-cash-flow-and-free-cash-flow-to-the-firm-fcff)

> OpenStax(2019), Principles of Accounting Volume 2 3.2 Calculate a Break-Even Point in Units and Dollars(https://openstax.org/books/principles-managerial-accounting/pages/3-2-calculate-a-break-even-point-in-units-and-dollars)

> OpenStax(2019), Principles of Accounting Volume 2 3.5 Calculate and Interpret a Company's Margin of Safety and Operating Leverage(https://openstax.org/books/principles-managerial-accounting/pages/3-5-calculate-and-interpret-a-companys-margin-of-safety-and-operating-leverage)
