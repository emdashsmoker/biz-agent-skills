---
name: no-standard
description: "write-standard와 code-standard를 불러오지 않고 답하게 하는 스킬. 사용자가 \"/no-standard\"로 호출하거나 write-standard와 code-standard 없이 답해 달라고 요청한 경우에 사용한다. 사용자의 요청이 없으면 불러오지 않는다."
metadata:
  generator: pref-architect
  generator-version: "1.3"
---

# no-standard

이 스킬을 호출한 대화에서는 설정 절의 대상 모듈을 불러오지 않는다. 이 호출은 상시 지침의 모듈 로드 규칙에서 사용자가 모듈을 쓰지 말라고 명시한 경우에 해당한다.

## 설정

- (대상 모듈) write-standard, code-standard

## 적용 범위

- 호출한 응답부터 그 대화가 끝날 때까지 적용한다.
- 대화에서 이미 불러온 대상 모듈의 규칙도 호출 이후에는 적용하지 않는다.
- 사용자가 대상 모듈을 다시 요청하면 그 요청부터 대상 모듈을 불러온다.
- 대상에 들지 않은 모듈과 상시 지침의 공통 작업 규칙은 그대로 적용한다.

## 호출 조건

사용자의 요청이 있을 때만 이 스킬을 불러온다. 모델이 스스로 불러오면 사용자가 알지 못한 채 대상 모듈의 기준이 적용되지 않는다.
