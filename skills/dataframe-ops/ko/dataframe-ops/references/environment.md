# 실행 환경

## 감지 순서

세션 시작 때 아래 순서로 코드를 실행할 곳을 찾는다. 앞 단계에서 찾으면 뒤 단계는 확인하지 않는다.

1. 내장 코드 실행기에서 `import pandas`가 되는지 시험한다. 되면 `dfo.env_report()`로 Python 버전, pandas 버전, 가상환경 여부, 추가 패키지 설치 여부를 읽는다.
2. 연결된 도구 목록에서 Python 또는 Anaconda 실행 도구(MCP 서버 등)를 찾는다. 있으면 그 도구로 1번과 같은 확인을 한다.
3. 등록된 외부 코드 실행 API가 있으면 같은 확인을 한다.
4. 모두 없으면 시뮬레이션 모드로 전환한다.

`/env`의 응답은 내장 실행기, Python 실행 도구, 외부 API 각각의 감지 여부와 현재 쓰는 환경의 종류, Python 버전, pandas 버전, 실행 가능 여부를 보여준다.

## 가상환경

사용자 컴퓨터에서 실행할 때만 적용한다. 채팅 서비스의 일회용 실행기는 세션이 끝나면 사라지므로 이 절차를 건너뛴다.

### 원칙

- 시스템 Python이나 conda의 base 환경에 패키지를 직접 설치하지 않는다. 다른 프로그램이 쓰는 패키지 버전이 바뀔 수 있기 때문이다.
- 작업은 이 스킬 전용 가상환경에서 한다.
- 전용 환경이 이미 있으면 새로 만들지 않고 다시 쓴다.

### 찾기와 선택

`dfo.env_report()`로 지금 가상환경 안에 있는지 확인한다. `isolated`가 True면 그 환경에서 바로 작업하고 아래 안내 4를 보여준다. 아니면 `dfo.find_environments()`로 기존 환경을 찾는다. 찾는 위치는 아래와 같다.

- venv 폴더: `~/.dataframe_ops_env`, `~/dataframe_ops_env`, `./.dataframe_ops_env`, `./dataframe_ops_env`, `./.venv`, `./venv`
- conda 환경: 이름에 `dataframe_ops` 또는 `dataframe-ops`가 들어간 환경
- 마지막 사용 시각은 환경 폴더의 수정 시각으로 대신한다.

찾은 환경 수에 따라 안내 1, 2, 3 가운데 하나를 보여준다. 추천 환경은 `dfo.recommend_environment()`가 고른다. pandas 버전이 가장 높은 환경을 고르고, 버전이 같으면 가장 최근에 쓴 환경을 고른다.

안내 1, 환경이 여러 개일 때

> 가상환경을 찾았습니다.
>
> | 번호 | 종류 | 이름 또는 경로 | Python | pandas | 최근 사용 |
> |---|---|---|---|---|---|
> | 1 | venv | ~/.dataframe_ops_env | 3.11.9 | 2.3.3 | 2026-05-02 |
> | 2 | conda | dataframe_ops | 3.12.4 | 3.0.6 | 2026-09-20 |
>
> 사용할 번호를 입력하세요. "새로 만들기"는 새 환경을 만들고, "건너뛰기"는 시스템 Python을 씁니다(권장하지 않음).
> 추천: 2번 (pandas 버전이 가장 높음)

안내 2, 환경이 하나일 때

> 기존 가상환경을 찾았습니다. (venv, ~/.dataframe_ops_env, Python 3.11.9, pandas 2.3.3, 최근 사용 2026-05-02)
> 이 환경을 쓸까요? "예"는 이 환경 사용, "새로 만들기"는 새 환경 생성, "건너뛰기"는 시스템 Python 사용(권장하지 않음)입니다.

안내 3, 환경이 없을 때

> 이 스킬 전용 가상환경이 없습니다. 패키지 충돌을 막기 위해 전용 환경을 만들기를 권합니다.
> "예"는 `~/.dataframe_ops_env`에 venv 생성, "conda"는 conda 환경 `dataframe_ops` 생성, "건너뛰기"는 시스템 Python 사용(주의 필요)입니다.
> 새 환경에는 pandas와 openpyxl만 설치하고 나머지 패키지는 필요할 때 묻고 설치합니다.

안내 4, 이미 가상환경 안일 때

> 가상환경에서 작업합니다. (conda, dataframe_ops, Python 3.12.4, pandas 3.0.6)

### 만들기

- venv는 `dfo.create_venv()`로 만든다. 현재 Python으로 환경을 만들고 pip을 업그레이드한 뒤 pandas와 openpyxl을 PyPI에서 설치한다.
- conda 환경은 `dfo.create_conda_env()`로 만든다. 채널은 conda-forge만 쓴다. Anaconda 기본 채널은 규모가 큰 조직에 유료 약관이 적용될 수 있기 때문이다.
- pandas 3.x는 Python 3.11 이상이 필요하다. 시스템 Python이 3.10 이하면 conda 환경을 권하거나 pandas 2.x 설치를 제안한다.
- 만들기 전에 위치와 설치할 패키지를 보여주고 동의를 받는다.

### 가상환경 명령

| 명령 | 동작 |
|---|---|
| `/venv` | 현재 환경 정보 |
| `/venv list` | 찾은 환경 목록 |
| `/venv create` | 새 환경 생성, venv와 conda 가운데 선택 |
| `/venv activate 이름` | 다른 환경으로 전환 |
| `/venv install 패키지` | 현재 환경에 패키지 설치 |
| `/venv delete 이름` | 환경 삭제, 경로를 보여주고 확인을 받은 뒤 실행 |

### 패키지 설치 확인

사용자가 "seaborn 설치해줘"처럼 설치를 요청하면 현재 환경을 먼저 본다.

- 가상환경 안이면 설치 명령(`pip install seaborn`)을 보여주고 바로 설치한다.
- 시스템 Python이면 경고하고 세 가지 가운데 고르게 한다. "환경 생성 후 설치"(권장), "그래도 설치", "취소"다.
- 스킬이 기능을 쓰려고 추가 패키지가 필요할 때(예를 들어 .xls 파일을 열 때 xlrd)는 어떤 기능에 필요한지 알리고 설치 여부를 묻는다.

## 버전 확인

환경이 정해지면 설치된 pandas 버전을 기준으로 안내한다.

- 웹 검색이나 웹 페이지 읽기 도구가 있으면 공식 자료를 확인한다. 설치 버전의 릴리스 노트는 `https://pandas.pydata.org/docs/whatsnew/v버전.html`(예를 들어 v3.0.6.html)이다. 최신 안정 버전은 `https://pandas.pydata.org/docs/whatsnew/index.html` 목록 맨 위나 `https://pypi.org/pypi/pandas/json`의 `info.version`으로 확인한다.
- 릴리스 노트에서 새 기능, 사용 중단 예고, 삭제된 기능, 알려진 문제를 찾아 두세 줄로 요약한다.
- 설치 버전과 최신 버전이 같은 부 버전(3.0.x처럼 앞 두 자리가 같음)이고 끝자리만 낮으면 업그레이드를 권한다. 끝자리 업데이트는 버그 수정 위주이기 때문이다.
- 앞 두 자리가 다르면 기존 코드가 달라질 수 있다. 두 버전의 차이를 알리고 업그레이드 여부는 사용자가 정하게 한다.
- 웹 도구가 없으면 설치 버전과 위 공식 주소만 알린다. 시뮬레이션 모드에서 최신 버전을 확인할 수 없으면 참조 버전을 "확인 불가"로 적는다.

## 호환성 확인

코드를 실행하기 전에 아래 표에 걸리는 코드가 있는지 본다. 걸리면 경고와 대안 코드를 보여주고 대안으로 실행할지 묻는다.

| 대상 | 버전별 변화 | 대안 |
|---|---|---|
| `DataFrame.append`, `Series.append` | 2.0.0에서 삭제 | `pd.concat([df, df2], ignore_index=True)` |
| 열을 고르지 않은 그룹 집계 `df.groupby(열).mean()` | 2.0.0부터 글자 열이 섞이면 오류 | 집계할 열을 먼저 고르거나 `numeric_only=True` |
| `DataFrame.applymap` | 2.1.0에서 사용 중단 예고, 3.0.0에서 삭제 | `DataFrame.map` |
| `Series.case_when` | 2.2.0에서 추가 | 2.2.0 미만은 `numpy.select` |
| 연쇄 대입 `df['열'][0] = 값` | 3.0.0부터 값이 바뀌지 않음 | `df.loc[0, '열'] = 값` |
| 문자열 열의 dtype | 3.0.0부터 기본값이 `str`, 이전은 `object` | dtype 비교는 `pd.api.types.is_string_dtype(df[열])` |
| `pd.options.mode.copy_on_write` | 3.0.0부터 효과 없음, 4.0에서 삭제 예정 | 3.x에서는 설정하지 않음 |
| `inplace=True` | PDEP-8에 따라 `drop`, `dropna`, `rename`, `sort_values` 등에서 폐지 예정 | `df = df.drop(...)`처럼 다시 대입 |

불러오기(`read_csv`, `read_excel`, `read_json`), 기본 탐색(`head`, `tail`, `shape`, `columns`, `dtypes`, `info`, `describe`), 선택(`df[열]`, `loc`, `iloc`), 수정(`drop`, `rename`, `fillna`, `dropna`, `replace`), 정렬과 집계(`sort_values`, `groupby`, `agg`, `pivot_table`), 결합(`concat`, `merge`), 저장(`to_csv`, `to_excel`, `to_json`)은 pandas 1.0 이후 모든 버전에 같은 이름으로 있다. 세부 동작의 변화는 위 표를 따른다.

경고 문구 예시

> 버전 호환성 경고
> 현재 환경은 pandas 3.0.6입니다. `DataFrame.append()`는 pandas 2.0에서 삭제되었습니다.
> 대안 코드는 `result = pd.concat([df, df2], ignore_index=True)`입니다. 이 코드로 실행할까요? (y/n)

pandas 2.x 사용자가 3.0 동작을 미리 맞춰 보려면 아래 두 설정을 쓴다. 3.x에서는 둘 다 필요 없다.

```python
pd.options.mode.copy_on_write = True    # 2.0 이상
pd.options.future.infer_string = True   # 2.1 이상
```

## 초기화 안내

첫 응답은 아래 틀을 채워 보여준다. 대괄호는 실제 값으로 바꾸고 해당하지 않는 줄은 생략한다.

실행 환경이 있을 때

> **dataframe-ops 준비 완료**
>
> - 실행 환경: [내장 실행기, Python 실행 도구, 외부 API 가운데 하나], [가상환경 이름 또는 시스템 Python]
> - 버전: Python [x.y.z], pandas [x.y.z], 코드 실행 가능
> - 이 버전의 참고 사항: [릴리스 노트 요약 한두 줄]
> - 최신 안정 버전: [버전], 업그레이드 권장 여부: [예 또는 아니오와 이유]
> - 출력 모드: [markdown 또는 ascii], 변경은 `/render markdown`, `/render ascii`
> - 좌표 규칙: A1은 첫 열의 첫 데이터 값(열 이름 줄은 행 번호에 포함하지 않음)
>
> 시작 방법
> 1. CSV, 엑셀, JSON 파일 올리기
> 2. 코드 직접 입력하기, 예를 들어 `df = pd.DataFrame({'A': [1, 2, 3]})`
> 3. "예시 데이터 생성" 입력하기
>
> 도움말은 `/?` 또는 "명령어 목록"

실행 환경이 없을 때(시뮬레이션 모드)

> **dataframe-ops 준비 완료 (시뮬레이션 모드)**
>
> - Python과 pandas를 실행할 환경을 찾지 못했습니다. 코드를 만들어 드리고 결과는 예시로만 보여드립니다.
> - 참조 버전: pandas [최신 안정 버전 또는 확인 불가], 권장 Python [버전]
> - 최신 버전의 주요 기능: [두세 줄]
> - 실제 실행하려면 사용 중인 AI 서비스의 코드 실행 기능을 켜거나 Python 실행 도구를 연결하세요.
>
> 시작 방법
> 1. 마크다운 표나 JSON으로 데이터 붙여넣기
> 2. "CSV 읽는 코드"처럼 코드 작성 요청하기
> 3. "예시 데이터로 시작" 입력하기
>
> 도움말은 `/?` 또는 "명령어 목록"

"예시 데이터 생성"을 받으면 이름, 나이, 부서, 급여 열이 있는 5-10행짜리 가상 데이터를 코드로 만든다. 이름은 홍길동, 김철수, 이영희처럼 널리 쓰는 예시 이름을 쓰고 실존 인물로 오해될 이름은 쓰지 않는다.
