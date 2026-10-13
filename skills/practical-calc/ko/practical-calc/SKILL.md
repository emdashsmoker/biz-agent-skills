---
name: practical-calc
description: 기획자와 컨설턴트가 자주 쓰는 계산을 Python 스크립트로 재현 가능하게 수행하는 도구 모음. CAGR과 실질가격 환산(references/growth.md), B/C 비율, NPV, IRR, 회수기간, 민감도 분석(references/appraisal.md), AHP 가중치와 일관성 비율(references/ahp.md), 손익 요약, EBITDA, OPEX, CAPEX, 감가상각, 손익분기점(references/corporate.md), 가격, 구성, 물량 차이 분해와 예측 정확도(references/variance.md), 산업연관 경제적 파급효과와 입지계수(references/industry.md), HHI, CRk, TAM, SAM, SOM 시장규모 추정(references/market.md), 제출 자료를 입력 형식으로 바꾸는 전처리 규칙(references/data-prep.md), 차트 작성 규칙(references/charts.md)을 담고 계산표를 CSV나 XLSX로 내보낸다. 연평균 성장률, 비용편익분석, 예비타당성조사 방식의 경제성 분석, 투자 회수기간, 평가 기준 가중치, 영업이익률, 손익분기 판매량, 예산 대비 실적 차이, 생산유발효과, 고용유발효과, 지역 산업 특화도, 시장 점유율 집중도, 시장규모 계산을 요청받으면 도구 이름이 언급되지 않아도 이 스킬을 사용한다.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# 실무 계산 도구

기획과 컨설팅 업무에서 자주 쓰는 계산을 Python 스크립트로 수행하는 도구 모음이다. 산식, 용어 정의, 판단 기준은 `references` 폴더의 문서에 있고 모든 숫자 계산은 `scripts` 폴더의 스크립트가 수행한다. 같은 입력 파일과 같은 명령을 쓰면 누구나 같은 결과를 얻는다.

## 도구 목록

| 분석 대상 | 도구 | 스크립트 | 참조 문서 |
|---|---|---|---|
| 시계열 값 | CAGR | `cagr.py` | `references/growth.md` |
| 시계열 값 | 실질가격 환산 | `deflate.py` | `references/growth.md` |
| 사업과 대안 | B/C 비율, NPV, IRR, 회수기간, 민감도 분석 | `appraisal.py` | `references/appraisal.md` |
| 사업과 대안 | AHP 가중치, 일관성 비율 | `ahp.py` | `references/ahp.md` |
| 기업 재무 | 손익 요약, EBITDA, OPEX | `pl_summary.py` | `references/corporate.md` |
| 기업 재무 | CAPEX, 잉여현금흐름, 감가상각 | `capex.py` | `references/corporate.md` |
| 기업 재무 | 손익분기점(BEP) | `bep.py` | `references/corporate.md` |
| 기업 재무 | 가격, 구성, 물량 차이 분해와 예측 정확도 | `variance.py` | `references/variance.md` |
| 산업과 시장 | 경제적 파급효과(산업연관분석) | `io_impact.py` | `references/industry.md` |
| 산업과 시장 | 입지계수(LQ) | `lq.py` | `references/industry.md` |
| 산업과 시장 | 시장집중도(HHI, CRk) | `hhi.py` | `references/market.md` |
| 산업과 시장 | 시장규모(TAM, SAM, SOM) | `market_size.py` | `references/market.md` |

제출 자료를 입력 형식으로 바꾸는 규칙은 `references/data-prep.md`에, 차트 규칙은 `references/charts.md`에 있다. 참조 문서에 나오는 예시 입력 파일은 `examples` 폴더에 있다. 요청 하나가 여러 도구에 걸치면 도구마다 아래 절차를 따로 밟는다.

## 계산 원칙

언어모델이 직접 계산한 숫자는 틀려도 겉으로 드러나지 않으므로 합계, 비율, 반올림을 포함한 모든 숫자는 스크립트가 계산한다. 보고서에는 스크립트 출력값을 그대로 옮긴다.

- 입력값은 사용자가 준 자료나 출처를 확인한 공개 통계에서 가져온다. 산업연관 계수, 물가지수, 시장점유율처럼 공식 통계가 필요한 값은 출처를 밝힌 자료로 채운다.
- 금액에는 단위를 붙인다. 입력 단위와 결과 단위가 다르면 환산 규칙을 결과와 함께 적는다.
- 입력은 파일로 저장한 뒤 스크립트에 넘긴다. 입력 파일과 실행 명령이 남아 있어야 제3자가 같은 결과를 재현한다.
- 판단 기준(예: B/C 비율 1.0 이상)은 참조 문서에 적힌 기준과 출처만 사용한다.

## 작업 절차

1. 요청에서 계산 목적을 파악하고 도구 목록에서 스크립트와 참조 문서를 고른다.
2. 참조 문서에서 용어 정의, 산식, 입력 형식, 입력 수집 순서를 읽는다.
3. 입력을 모은다. 필요한 값이 요청에 모두 있으면 질문 없이 바로 계산한다. 누락된 값이 있으면 참조 문서의 입력 수집 순서에 따라 누락된 값을 한 번에 묶어 묻는다.
4. 입력 파일(JSON 또는 CSV)을 작업 폴더에 저장한다. 제출 자료의 형태가 입력 형식과 다르면 `references/data-prep.md`에 따라 변환 코드를 작성하고 코드 파일도 함께 저장한다.
5. 스크립트를 실행한다.
6. 스크립트가 "확인 사항"을 출력하면 그 내용을 결과와 함께 전달한다. 입력 오류로 멈추면 오류 메시지를 사용자에게 보여 주고 입력을 고친다.
7. 결과를 아래 보고 형식으로 정리한다. 사용자가 차트를 미리 요청하지 않았으면 결과를 보인 뒤 차트가 필요한지 한 번 묻는다.

## 실행 방법

스크립트 경로는 스킬 폴더 기준이다. 모든 스크립트는 같은 공통 옵션을 쓴다.

```
python scripts/<스크립트 이름> --input <입력 파일> [--decimals 2] [--export tables.xlsx] [--out result.json] [--chart chart.png]
```

| 옵션 | 용도 |
|---|---|
| `--decimals` | 표에 표시할 소수 자릿수 (기본값 2) |
| `--export` | 출력한 계산표를 파일로 저장하며 `.xlsx`는 표마다 시트 하나, `.csv`는 표마다 파일 하나 |
| `--out` | 계산 결과 전체를 JSON 파일로 저장 |
| `--chart` | 차트를 PNG 파일로 저장 |

도구별 추가 옵션과 입력 형식은 참조 문서의 실행 예시를 따른다. `cagr.py`는 입력 파일 대신 값을 옵션으로 받을 수 있고 `variance.py`는 첫 인수로 `mix` 또는 `accuracy`를 받는다.

입력 오류가 있으면 스크립트는 종료 코드 2와 함께 원인을 출력한다. 코드를 실행할 수 없는 환경에서는 입력 파일 내용과 실행 명령을 사용자에게 전달하고 사용자가 직접 실행하도록 안내한다. 이때 결과 숫자는 추정해서 채우지 않는다.

## 결과 보고

- (입력 요약) 사용한 값, 단위, 자료 출처, 값이 달라진 전처리 내용
- (계산 과정) 스크립트가 출력한 중간 계산표
- (결과) 주요 지표 표와 참조 문서의 판단 기준에 근거한 한두 문장의 해석
- (확인 사항) 스크립트가 출력한 경고가 있을 때 포함
- (재현 정보) 입력 파일 내용, 전처리 코드, 실행 명령을 코드 블록으로 제시

사용자가 계산표를 파일로 원하거나 표가 길면 `--export`로 XLSX 또는 CSV 파일을 만들어 함께 전달한다. 내보낸 파일에는 반올림하지 않은 값이 들어간다. 비율은 백분율 숫자로 저장하고 해당 열 이름이나 항목 이름에 (%)를 붙인다.

## 실행 환경

- Python 3.9 이상과 numpy, pandas가 필요하다. 차트에는 matplotlib, XLSX 입력과 내보내기에는 openpyxl이 추가로 필요하다.
- 설치 명령은 `pip install numpy pandas matplotlib openpyxl`이다.
- 한글 차트에는 나눔고딕(NanumGothic) 글꼴이 필요하다. 글꼴이 없으면 스크립트가 알림을 출력하고 기본 글꼴로 그린다. 기본 글꼴에서는 한글이 깨질 수 있다.
- 작성 시점 검증에 사용한 버전은 Python 3.11, numpy 2.4, pandas 3.0, matplotlib 3.10이다.
