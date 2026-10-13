# plan.json 형식과 파일 내보내기

plan.json 1개가 오버뷰, CSV, XLSX의 원본이다. 파일마다 따로 고치면 날짜와 수치가 어긋나므로 항상 plan.json을 고친 뒤 다시 내보낸다. 전체 예시는 `assets/plan_example.json`에 있다.

## project

| 필드 | 필수 | 뜻 |
|---|---|---|
| name | 예 | 프로젝트명 |
| start, end | 예 | 계약 시작일과 종료일, YYYY-MM-DD |
| buffer_ratio | 아니오 | 일정 여유 기준 비율. 기본 0.15 |
| max_task_days | 아니오 | 작업 행 1개의 최대 일수. 기본 28 |
| baseline_last_end | 아니오 | 최초 계획의 마지막 작업 종료일. 여유 소진율 계산에 쓴다 |

## options

| 필드 | 기본 | 뜻 |
|---|---|---|
| mm | true | 투입인력 표와 M/M 검산 |
| raci | false | 작업 행의 RACI 열과 검산 |

## people

| 필드 | 뜻 |
|---|---|
| id | 작업 행의 owner와 raci에서 쓰는 식별자 (예: P1) |
| name, role | 표에 보이는 이름과 역할 |
| rate | 참여율 (0.5는 50%) |
| months | 참여 개월 수 |
| contract_mm | 계약 서류의 M/M. 없으면 rate × months로 계산한다 |
| mm | 월별 M/M, 예: {"2026-03": 0.5, "2026-04": 0.4} |

## tasks

| 필드 | 필수 | 뜻 |
|---|---|---|
| stage | 예 | 단계명 |
| name | 예 | 작업명 |
| type | 예 | work(작업), wait(대기), check(점검), buffer(여유) |
| start, end | 예 | YYYY-MM-DD. 날짜를 모르면 가정 날짜를 넣고 note에 `[확인 필요: 날짜]`를 적는다 |
| owner | 작업과 점검은 예 | people의 id 또는 기관명 같은 글자 |
| output | 작업과 점검은 예 | 산출물(완료 기준) |
| status | 아니오 | planned(예정), doing(진행), done(완료). 기본은 planned |
| note | 아니오 | 비고. 결과 불확실, 특정 인력 의존, 납기 직결 같은 표준 문구와 대응을 적는다 |
| event | 아니오 | kickoff, interim_report, final_report, advisory, hearing, other. 행사 간격 검사에 쓴다 |
| allow_long | 아니오 | true면 기간 초과 경고를 끈다. 매월 반복하는 관리 업무에 쓴다 |
| raci | 아니오 | {"P1": "A", "P2": "R"} |

- 표의 행 순서는 tasks의 순서를 그대로 따른다. 같은 단계의 행은 이어서 적는다.
- 단계 이름이 같은 행은 한 단계로 묶인다.

## overview

| 필드 | 형식 | 오버뷰 위치 |
|---|---|---|
| summary | [["발주처", "OO기관"], ["계약 형태", "용역"]] | 기본개요의 추가 줄 |
| beneficiary | 문장 목록 | Why의 수혜자 |
| needs | 문장 목록 | Why의 니즈 및 문제 |
| goals | 문장 목록 | 프로젝트 목표 |
| hypotheses | [{"statement": "가설", "solutions": ["솔루션"]}] | 가설 & 솔루션 |
| success | 문장 목록, 3개 이내 | 성공판단기준 |
| notes | 문장 목록 | 특기사항 |

## 검산 항목

`plan.py check`는 오류와 경고를 나눠 출력한다. 오류가 있으면 파일을 만들지 않는다.

| 종류 | 항목 |
|---|---|
| 오류 | 필수 필드 누락, 날짜 형식, 종료일이 시작일보다 빠름, type과 status와 event의 허용 값 |
| 경고 | 계약 기간 밖의 일정, 담당이나 완료 기준 누락, 긴 작업 행, 일정 여유 기준 미달, 여유 행 없음, 여유 소진율이 진척률 초과, 자문회의와 공청회 간격, 성공판단기준 4줄 이상, M/M 합계 불일치, 월 M/M 1.0 초과, RACI의 A가 1명이 아님 |

## 파일 형식

| 파일 | 명령 | 구성 |
|---|---|---|
| 오버뷰 MD | `plan.py md plan.json -o overview.md` | 오버뷰 전체 섹션, WBS 상세 표, 투입인력 표 |
| CSV | `plan.py csv plan.json -o wbs.csv` | WBS 표 1개. M/M을 켜면 wbs_mm.csv를 추가한다. BOM이 붙은 UTF-8 |
| XLSX | `plan.py xlsx plan.json -o wbs.xlsx` | WBS 시트와 투입인력 시트(M/M을 켠 경우) |
| PDF | `md2pdf.py overview.md -o overview.pdf` | 본문은 세로 쪽, 열이 9개 이상인 표가 있는 섹션은 가로 쪽 |

XLSX 서식

- 글자색은 검정, 테두리는 얇은 실선이고 머리글에만 회색 바탕(D9D9D9)을 쓴다. 간트 머리글 위 줄은 흰 바탕의 병합 칸이다. 다른 색과 조건부 서식은 쓰지 않는다.
- 간트 칸은 수식으로 표시한다. 시작일이나 종료일을 고치면 표시도 따라 바뀐다.
- 간트 기호는 ■ 작업, ○ 대기, ● 점검, □ 여유다.
- 기간이 약 7개월(30주) 이하면 주 단위 열을 쓴다. 머리글 위 줄은 월마다 칸을 병합해 "2026년 3월"처럼 적고, 머리글에는 각 주 월요일의 날짜를 숫자로 적는다.
- 기간이 더 길면 월 단위 열을 쓴다. 머리글 위 줄은 연도마다 칸을 병합해 "2026년"처럼 적고, 머리글에는 "3월"처럼 월을 적는다.
- 투입인력 시트의 합계와 차이 열은 수식이다. 차이가 0이 아니면 계약 M/M과 배분이 어긋난 상태다.

## 영어 라벨

스크립트는 `--lang en`을 주면 영어 라벨을 쓴다. 기본 언어는 `scripts/plan.py` 상단의 DEFAULT_LANG으로 정한다.
