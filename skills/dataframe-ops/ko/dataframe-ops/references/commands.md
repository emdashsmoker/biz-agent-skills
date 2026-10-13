# 명령어 모음

`/?` 또는 "명령어 목록"을 받으면 이 파일의 표를 보여준다. 표 안의 `열`, `값`, `경로`는 자리 표시어이며 실행할 때 사용자 데이터의 실제 이름으로 바꾼다.

## 불러오기와 저장

| 자연어 | pandas | 예시 |
|---|---|---|
| CSV 불러오기 | `pd.read_csv(경로)` | "sales.csv 불러오기" |
| 엑셀 불러오기 | `pd.read_excel(경로)` | "report.xlsx 읽기" |
| JSON 불러오기 | `pd.read_json(경로)` | "data.json 로드" |
| CSV 저장 | `df.to_csv(경로, index=False)` | "result.csv로 저장" |
| 엑셀 저장 | `df.to_excel(경로, index=False)` | "엑셀로 내보내기" |

## 탐색

| 자연어 | pandas | 예시 |
|---|---|---|
| 전체 보기 | `df` | "테이블 전체 출력" |
| 상위 N개 | `df.head(N)` | "처음 10개" |
| 하위 N개 | `df.tail(N)` | "마지막 5개" |
| 크기 확인 | `df.shape` | "행렬 크기" |
| 열 목록 | `df.columns.tolist()` | "컬럼명 확인" |
| 데이터 타입 | `df.dtypes` | "타입 확인" |
| 기초 통계 | `df.describe()` | "통계 요약" |
| 결측치 개수 | `df.isna().sum()` | "빈 값 개수" |
| 고유값 | `df[열].unique()` | "부서 고유값" |
| 값 빈도 | `df[열].value_counts()` | "부서별 빈도수" |

## 선택과 필터

| 자연어 | pandas | 예시 |
|---|---|---|
| 열 선택 | `df[열]`, `df[[열1, 열2]]` | "이름 열만" |
| 행 선택 | `df.iloc[위치]` | "3번째 행" |
| 조건 필터 | `df[df[열] > 값]` | "나이 30 초과" |
| 여러 조건 | `df[(조건1) & (조건2)]` | "나이 30 이상이고 성별 남자" |
| 값 기준 상위 N개 | `df.nlargest(N, 열)` | "매출 상위 5개" |
| 값 기준 하위 N개 | `df.nsmallest(N, 열)` | "점수 하위 3개" |
| 무작위 추출 | `df.sample(N)` | "무작위 10개" |

## 수정

| 자연어 | pandas | 예시 |
|---|---|---|
| 열 추가 | `df[새 열] = 값` | "총합 열 추가" |
| 열 삭제 | `df = df.drop(columns=[열])` | "주소 열 제거" |
| 행 삭제 | `df = df.drop(df.index[위치])` | "1번 행 삭제" |
| 열 이름 변경 | `df = df.rename(columns={옛 이름: 새 이름})` | "name을 이름으로" |
| 값 바꾸기 | `df = df.replace(옛 값, 새 값)` | "M을 남자로 변경" |
| 결측치 채우기 | `df = df.fillna(값)` | "빈 값 0으로" |
| 결측 행 제거 | `df = df.dropna()` | "결측 행 제거" |
| 중복 행 제거 | `df = df.drop_duplicates()` | "중복 행 삭제" |
| 타입 변환 | `df[열] = df[열].astype(타입)` | "나이를 정수로" |

## 정렬과 집계

| 자연어 | pandas | 예시 |
|---|---|---|
| 오름차순 정렬 | `df.sort_values(열)` | "이름순 정렬" |
| 내림차순 정렬 | `df.sort_values(열, ascending=False)` | "매출 높은 순" |
| 그룹별 집계 | `df.groupby(열)[값 열].agg(함수)` | "부서별 평균 급여" |
| 피벗 테이블 | `df.pivot_table(index=열, columns=열, values=열, aggfunc=함수)` | "연도별 월별 매출 피벗" |
| 합계 | `df[열].sum()` | "매출 합계" |
| 평균 | `df[열].mean()` | "나이 평균" |
| 최댓값, 최솟값 | `df[열].max()`, `df[열].min()` | "최고 점수" |
| 개수 | `df[열].count()` | "유효 데이터 수" |

그룹 집계에서는 집계할 열을 먼저 고른다. pandas 2.0부터 `df.groupby(열).mean()`처럼 열을 고르지 않으면 글자 열이 섞였을 때 오류가 난다. 모든 숫자 열을 집계하려면 `df.groupby(열).mean(numeric_only=True)`를 쓴다.

## 결합

| 자연어 | pandas | 예시 |
|---|---|---|
| 세로로 이어 붙이기 | `pd.concat([df1, df2], ignore_index=True)` | "두 테이블 합치기" |
| 키로 합치기 | `pd.merge(df1, df2, on=키)` | "ID 기준으로 조인" |
| 왼쪽 기준 합치기 | `pd.merge(df1, df2, on=키, how='left')` | "왼쪽 기준 병합" |

## 시각화

matplotlib가 필요하다. 설치되어 있지 않으면 설치 여부를 먼저 묻는다.

| 자연어 | 코드 | 예시 |
|---|---|---|
| 선 그래프 | `df.plot()` | "추이 그래프" |
| 막대 그래프 | `df.plot.bar()` | "막대 차트" |
| 히스토그램 | `df[열].hist()` | "분포도" |
| 산점도 | `df.plot.scatter(x=열, y=열)` | "X와 Y 산점도" |
| 상관관계 | `df.corr(numeric_only=True)`를 히트맵으로 | "상관 히트맵" |

## 의도 키워드

자연어 요청의 의도를 아래 키워드로 판단한다. 키워드가 여러 의도에 걸치면 수정 의도가 있는지 먼저 본다. 수정 의도가 있으면 `df`를 바꾸고, 없으면 결과를 `result`에 담는다.

| 의도 | 키워드 |
|---|---|
| 불러오기 | 불러오기, 읽기, 로드, 열기, 가져오기, import, read, load |
| 저장 | 저장, 내보내기, export, save, write |
| 보기 | 보기, 보여줘, 출력, 확인, show, display, print |
| 필터 | 필터, 조건, 만, 이상, 이하, 초과, 미만, 같은, where, filter |
| 정렬 | 정렬, 순서, 순, order, sort |
| 그룹 집계 | 그룹, 별, 집계, group, aggregate |
| 수정 | 수정, 변경, 추가, 삭제, 바꾸기, update, add, delete, remove |
| 통계 | 통계, 평균, 합계, 최대, 최소, 개수, mean, sum, count |
| 시각화 | 그래프, 차트, 시각화, plot, chart, graph |
| 도움말 | 도움, 명령어, 방법, 어떻게, help, ? |

| 입력 | 해석 | 코드 |
|---|---|---|
| "나이 30 이상만" | 필터 | `result = df[df['나이'] >= 30]` |
| "부서별 급여 평균" | 그룹 집계 | `result = df.groupby('부서')['급여'].mean()` |
| "이름순으로 정렬" | 정렬 | `result = df.sort_values('이름')` |
| "매출 높은 순으로 5개" | 정렬과 상위 N | `result = df.nlargest(5, '매출')` |
| "성별 열 삭제" | 수정 | `df = df.drop(columns=['성별'])` |

## 좌표 명령

행 번호는 첫 데이터 행이 1이고 열 문자는 A부터 시작한다. 코드는 `dfo.ref_to_code()`로 만든다.

| 입력 | 뜻 | pandas |
|---|---|---|
| "A1 값" | 한 셀 | `df.iloc[0, 0]` |
| "B3을 100으로" | 한 셀 수정 | `df.iloc[2, 1] = 100` |
| "C5 비우기" | 한 셀 비우기 | `df.iloc[4, 2] = None` |
| "A1:C3" | 셀 범위 | `df.iloc[0:3, 0:3]` |
| "A열 전체", `A:A` | 한 열 | `df.iloc[:, 0]` |
| "3행 전체", `3:3` | 한 행 | `df.iloc[2, :]` |
| "B부터 D열", `B:D` | 여러 열 | `df.iloc[:, 1:4]` |
| "2행부터 5행", `2:5` | 여러 행 | `df.iloc[1:5, :]` |
| "A, C, E열만" | 떨어진 열 | `df.iloc[:, [0, 2, 4]]` |
| "B열 삭제" | 열 삭제 | `df = df.drop(columns=df.columns[1])` |
| "3행 삭제" | 행 삭제 | `df = df.drop(df.index[2])` |
| "D열 자리에 새 열" | 위치를 정해 열 추가 | `df.insert(3, '새 열', 값)` |
| "A열 다음에 추가" | 위치를 정해 열 추가 | `df.insert(1, '새 열', 값)` |

`df.insert`는 `df`를 그 자리에서 바꾸는 메서드이므로 다시 대입하지 않는다.

## 행 범위와 페이지

모든 행 번호는 1부터 세고 양 끝을 포함한다.

| 명령 | 자연어 예시 | 동작 | 함수 |
|---|---|---|---|
| `/h N` | "처음 30개" | 상위 N행, N이 없으면 5행 | `df.head(N)` |
| `/t N` | "마지막 20개" | 하위 N행, N이 없으면 5행 | `df.tail(N)` |
| `/all` | "전체 보여줘" | 전체, 100행 초과 시 먼저 질문 | |
| `/range 10 30` | "10행부터 30행까지", "10-30행" | 10-30행 | `dfo.rows_between(n, 10, 30)` |
| `/mid 20` | "중간 부분 보여줘" | 가운데 20행 | `dfo.rows_mid(n, 20)` |
| | "50행 근처" | 40-60행 | `dfo.rows_near(n, 50)` |
| `/next`, `n` | "다음" | 다음 페이지 | `dfo.page_rows(n, 쪽)` |
| `/prev`, `p` | "이전" | 이전 페이지 | |
| `/page 5` | "5페이지" | 5페이지 | |
| `/page first`, `/page last` | "첫 페이지", "마지막 페이지" | 처음, 마지막 페이지 | |
| `/pagesize N` | | 페이지 크기 변경 | |

페이지 방식으로 보여줄 때는 표 위에 "페이지 1/62, 행 1-20 표시"를 적고 표 아래에 이동 방법을 한 줄로 안내한다.

## 출력 설정

| 명령 | 동작 |
|---|---|
| `/rows` | 현재 출력 설정 표 보기 |
| `/rows N` | 기본 출력 행 수를 N으로 변경, 100 초과는 100으로 |
| `/rows all` | 기본 출력 행 수를 100으로 |
| `/rows reset` | 기본값 10행으로 복원 |

`/rows`는 기본 출력 행 수, 최대 출력 행 수, 페이지 크기, 현재 페이지, 셀당 글자 수, 행 번호 표시 여부를 표로 보여준다.

## 단축 명령어

| 명령 | 기능 |
|---|---|
| `/?` | 전체 명령어 |
| `/env` | 실행 환경 확인과 재탐지 |
| `/venv` | 가상환경 상태와 관리 |
| `/render` | 출력 모드 확인과 변경 |
| `/rows` | 출력 행 수 설정 |
| `/map` | 좌표와 열 이름 대응표 |
| `/h`, `/t` | 상위, 하위 행 |
| `/i` | 데이터 정보, `df.info()` |
| `/d` | 기초 통계, `df.describe()` |
| `/c` | 열 목록 |
| `/s` | 저장 형식 선택 메뉴 |
| `/u` | 실행취소 |
| `/history` | 작업 기록 |
| `/run 이름` | 매크로 실행 |
| `/save`, `/load`, `/checkpoints` | 체크포인트 저장, 복원, 목록 |
| `/reset` | 세션 초기화, `df`와 기록을 비우기 전에 확인 |

## 파일 형식

| 형식 | 확장자 | 읽는 방법 | 추가 패키지 |
|---|---|---|---|
| 스프레드시트 | .csv | `pd.read_csv(경로, encoding=인코딩)` | 없음 |
| | .xlsx, .xlsm | `pd.read_excel(경로, sheet_name=시트)` | openpyxl |
| | .xls | `pd.read_excel(경로)` | xlrd |
| | .ods | `pd.read_excel(경로)` | odfpy |
| 텍스트 | .tsv | `pd.read_csv(경로, sep='\t')` | 없음 |
| | .txt | `pd.read_csv(경로, sep=None, engine='python')` 구분자 자동 판별 | 없음 |
| JSON | .json | `pd.read_json(경로)` | 없음 |
| Parquet | .parquet | `pd.read_parquet(경로)` | pyarrow |
| 이미지 | .png, .jpg | 모델이 표를 읽어 옮기고 사용자 확인 후 `pd.DataFrame` | 없음 |
| PDF | .pdf | `dfo.pdf_tables(경로)`, Java가 있으면 tabula-py도 가능 | pdfplumber |
| Word | .docx | `dfo.docx_tables(경로)` | python-docx |

추가 패키지는 그 형식을 처음 다룰 때 설치 여부를 묻고 설치한다.

## 저장 형식

| 자연어 | pandas | 형식 |
|---|---|---|
| "CSV로 저장" | `df.to_csv('output.csv', index=False)` | .csv |
| "엑셀로 저장" | `df.to_excel('output.xlsx', index=False)` | .xlsx |
| "JSON으로 저장" | `df.to_json('output.json', orient='records')` | .json |
| "마크다운으로 저장" | `df.to_markdown('output.md')`, tabulate 필요 | .md |
| "클립보드 복사" | `df.to_clipboard()` | 화면이 있는 데스크톱 전용, 리눅스는 xclip 또는 xsel 필요 |

저장을 마치면 파일 이름, 위치, 행과 열 수를 알린다. 파일을 사용자에게 전달할 수 있는 환경이면 내려받을 수 있게 전달한다. 끝에 "CSV로도 저장"처럼 다른 형식으로 저장하는 문장을 한 줄 제안한다.
