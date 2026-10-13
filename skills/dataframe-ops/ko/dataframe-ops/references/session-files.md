# 세션 파일

체크포인트는 `df`와 작업 기록을 파일로 남기는 기능이다. 대화가 길어져 앞부분이 요약되거나 실행기가 다시 시작되어도 작업을 이어갈 수 있다. 파일은 작업 폴더 아래 `dataframe_ops_checkpoints/`에 저장한다.

## 저장 시점

| 시점 | 저장 내용 | 파일 이름 |
|---|---|---|
| 명령 5회마다(`session.record()`가 True를 돌려줄 때) | 현재 상태 | `checkpoint_날짜_시각.pkl` |
| 데이터를 불러온 직후 | 원본 스냅샷 | `original_파일이름.pkl` |
| 확인이 필요한 삭제에서 "백업 후 실행"을 고른 직후 | 실행 전 상태 | `before_작업명.pkl` |
| 사용자가 `/save 이름`을 요청할 때 | 현재 상태 | `save_이름.pkl` |
| 세션 종료 때 사용자가 "예"를 고를 때 | 상태, 재현 코드 | `session_날짜.zip` |

- 날짜와 시각은 `dfo.timestamp()`가 돌려주는 `YYYYMMDD_HHMMSS` 형식이다.
- 작업명은 `dropna`, `drop_duplicates`처럼 실행할 pandas 메서드 이름을 쓴다.
- 불러온 원본은 `df_original`에도 복사해 두고 체크포인트마다 함께 저장한다.
- 민감 정보 열을 마스킹하거나 삭제하기 전이면 첫 저장 전에 사용자에게 묻는다(SKILL.md의 민감 정보 절).

## 체크포인트 내용

`session.save_checkpoint({'df': df, 'df_original': df_original, 'result': result}, 파일이름)`은 아래 항목을 pickle 파일 하나에 담는다.

| 항목 | 내용 |
|---|---|
| timestamp | 저장 시각 |
| environment | Python 버전, pandas 버전, 가상환경 이름 |
| dataframes | `df`, `df_original`, `result` |
| column_map | 좌표와 열 이름 대응 |
| history | 세션의 모든 실행 코드와 시각 |
| macros | 저장한 매크로 |
| command_count | 실행한 명령 수 |
| change_count | `df`를 바꾼 명령 수 |
| full_code | 재현 코드 전체 |

기록은 전부 저장한다. 복원한 뒤에도 처음부터의 재현 코드를 만들 수 있어야 하기 때문이다.

## 저장과 복원 명령

| 명령 | 동작 |
|---|---|
| `/save` | 현재 상태를 `save_날짜_시각.pkl`로 저장 |
| `/save 이름` | 현재 상태를 `save_이름.pkl`로 저장 |
| `/save code` | 재현 코드를 `dataframe_ops_session.py`로 내보내기(`session.export_code()`) |
| `/save all` | 체크포인트와 재현 코드를 zip 하나로 저장(`session.save_all()`) |
| `/load`, `/checkpoints` | 저장된 파일 목록을 최근 순으로 보여주기(`session.list_checkpoints()`) |
| `/load 파일이름` | 해당 시점의 `df`, `df_original`, `result`, 기록, 매크로 복원 |

`session.load_checkpoint()`는 체크포인트 폴더 안의 .pkl 파일만 연다. pickle 파일은 여는 순간 안에 든 코드가 실행될 수 있어서 출처를 모르는 파일은 열지 않는다.

저장을 마치면 아래처럼 알린다. 파일을 사용자에게 전달할 수 있는 환경이면 내려받을 수 있게 전달한다.

> 체크포인트를 저장했습니다.
> - 파일: checkpoint_20260930_143522.pkl
> - 위치: ./dataframe_ops_checkpoints/
> - 내용: DataFrame 150행 × 5열, 명령 기록 15개, 열 매핑 A=이름, B=나이, C=부서, D=급여, E=입사일
> - 복원은 `/load checkpoint_20260930_143522.pkl`, 코드 내보내기는 `/save code`

## 컨텍스트 압축 뒤 복원

아래 가운데 하나에 해당하면 이전 작업이 유실되었다고 보고 복원 안내를 보여준다.

- Python 실행기에 `df`나 `session`이 없다. 실행기가 다시 시작된 경우다.
- 대화 앞부분이 요약문으로 바뀌어 이전 실행 코드나 결과를 볼 수 없다.

실행기가 다시 시작되었으면 `dfo.Session()`을 새로 만든 뒤 `list_checkpoints()`로 디스크의 파일을 읽는다.

> 이전 작업 내용 일부가 요약되어 보이지 않습니다.
> 복원 방법은 세 가지입니다. `/checkpoints`로 저장된 파일 확인, `/load 파일이름`으로 원하는 시점 복원, `/save code`로 지금까지의 코드 내보내기.
> 최근 체크포인트
> - checkpoint_20260930_143522.pkl (5분 전)
> - checkpoint_20260930_142815.pkl (12분 전)
>
> 어느 시점으로 복원할까요?

## 세션 종료

사용자가 "끝", "종료", "그만", "마무리", "오늘은 여기까지"처럼 작업을 마치겠다고 하면 저장 여부를 묻는다.

> 작업 내용을 저장할까요?
> 1. "예": `df`, 재현 코드, 기록 전체 저장(`session_날짜.zip`)
> 2. "코드만": 재현 코드만 저장
> 3. "아니오": 저장하지 않고 종료
>
> 자동 저장된 체크포인트는 [개수]개이며 최신 파일은 [파일 이름]입니다.

## 재현 코드

사용자가 "코드 전체", "재현 코드", `/save code`를 요청하면 `session.full_code()`로 세션 전체 코드를 만든다. 첫 줄에는 생성 시각과 Python, pandas 버전을 주석으로 적고, 그 뒤로 실행한 코드를 순서대로 번호와 시각을 붙여 적는다.

시뮬레이션 모드이거나 작업 하나의 재현 코드를 요청받으면 아래 틀을 쓴다. 파일을 읽을 때 쓴 인코딩이나 시트 이름은 그대로 옮긴다.

```python
# dataframe-ops 재현 코드
# 생성 시각: [YYYY-MM-DD HH:MM:SS]
# 환경: Python [x.y] / pandas [x.y.z]

import pandas as pd

# 1. 데이터 불러오기 (실제 파일 경로로 바꾸세요)
df = pd.read_csv('data.csv')

# 2. 불러온 데이터 확인
print(f"원본 데이터: {df.shape[0]}행 × {df.shape[1]}열")
print(f"열 목록: {df.columns.tolist()}")

# 3. 작업: 나이 30 이상, 영업부만
result = df[(df['나이'] >= 30) & (df['부서'] == '영업')]

# 4. 결과 확인
print(f"결과 데이터: {result.shape[0]}행 × {result.shape[1]}열")
print(result)

# 5. 저장 (필요하면 주석 해제)
# result.to_csv('result.csv', index=False)
```
