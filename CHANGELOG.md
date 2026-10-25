# Changelog

Dates are in UTC.

날짜는 UTC 기준으로 표기

<!--
Changelog rules
- (Timing) Record each pull request right after it is merged into main.
- (Scope) Check all main history since the last commit that changed CHANGELOG.md and record every merge that is still missing.
- (History command) TZ=UTC git log --first-parent --date=format-local:%Y-%m-%d origin/main
- (Date) Use the UTC date of the merge commit in YYYY-MM-DD format.
- (Date order) Keep the newest date at the top.
- (Entry unit) Write one entry for each change that users can notice.
- (Grouping) Combine same-day pull requests on the same topic into one entry and list every pull request number.
- (Splitting) Split a pull request that contains unrelated changes into separate entries.
- (Skill header) Group the entries of each date under ### headers named after the folders under skills/. Use ### Common for repository-wide changes and changes that apply to every skill. Repeat a change that applies to several skills under each of their headers.
- (Entry order) Put the Common header first and sort the other headers by skill folder name. List the entries under each header in pull request order.
- (English entries) List the English entries first under each header with the "-" bullet.
- (Korean entries) Leave one blank line after the English entries and list the same changes in the same order with the "*" bullet so that they render as a separate list.
- (English format) - Description that starts with the change type verb (#PR number)
- (Korean format) * Korean noun-ending description that ends with the change type word (#PR number)
- (Korean style) Write each Korean entry in formal note style as a simple sentence (단문) with a noun ending. Keep one subject-predicate relation per entry, turn other clauses into noun phrases, and split an entry that carries two messages. Avoid colloquial expressions and placeholder nouns such as 것, 곳, 거, 셈 and 부분.
- (Change types) Added (추가), Changed (변경), Fixed (수정), Removed (삭제), Action needed (필요)
- (Include) Changes to skill outputs, usage steps, or installation.
- (Exclude) Typo and wording fixes, demo image replacements, README changes unrelated to installation, internal refactoring without behavior changes, and commits that only change CHANGELOG.md.
- (Push) Commit on top of the latest main and push directly to main.
-->

## 2026-10-25

### biz-code-style
- Changed the scope for code to its classification structure (#37)
- Added an exception that applies the domain specification's category count and depth to code (#37)

* 코드의 적용 범위를 분류 구조로 변경 (#37)
* 코드의 항목 수와 계층 깊이에 도메인 명세 기준을 적용하는 예외 추가 (#37)

### logical-write
- Changed the scope for code to its classification structure (#37)
- Added an exception that applies the domain specification's item count and depth to code (#37)

* 코드의 적용 범위를 분류 구조로 변경 (#37)
* 코드의 항목 수와 계층 깊이에 도메인 명세 기준을 적용하는 예외 추가 (#37)

### onto-mece
- Changed the scope for code to its classification structure (#37)
- Added an exception that applies the domain specification's category count and depth to code (#37)

* 코드의 적용 범위를 분류 구조로 변경 (#37)
* 코드의 범주 수와 계층 깊이에 도메인 명세 기준을 적용하는 예외 추가 (#37)

### ontology-modeling
- Changed the scope for code to its classification structure (#37)

* 코드의 적용 범위를 분류 구조로 변경 (#37)

### skill-forge
- Added the SKILL.md frontmatter format to the build mode template (#38)
- Changed build mode to split work by output and assign each step to model judgment, a script, an external tool or a user checkpoint (#39)
- Added a final check and packaging in the .skill or zip format approved in the design as the last stages of build mode (#39)
- Changed the reference file rule to state in the body when each file is read (#39)
- Changed build mode to ask the user whether to run tests and whether to run them in a subagent or a separate session (#39)
- Removed framework selection, prompt output formats, documentation tables and the table of contents rule from build mode (#39)
- Removed the planning and consulting scope from the description and Combine mode (#39)
- Added a build mode rule to include instructions that call another skill or agent only when the user wants them, with a fallback for a missing target (#40)
- Changed the package format used when none is set from .skill to the recommended output format in the environment check table (#40)
- Added a step to confirm the target environment's skill registration steps when the chat window has no skill save feature (#40)
- Changed Combine mode to pick the simplest fitting pattern among single skill, chain, routing, split, dynamic split, review loop and autonomous run (#41)
- Changed the fixed default stage table of Combine mode to stages split by output with pass criteria for each stage (#41)
- Added a stop with options when a Combine mode stage fails its pass criteria, hits an error or reaches a limit (#41)
- Changed Combine mode to use subagents or separate sessions only when the user chooses them at plan approval (#41)
- Added an autonomous run option that asks the user for checkpoints, a stage limit and stop conditions (#41)

* 제작 모드 템플릿에 SKILL.md 프론트매터 양식 추가 (#38)
* 제작 모드의 설계 방식을 산출물 단위 업무 분해와 단계별 수행 주체 배정으로 변경 (#39)
* 제작 모드 마지막 단계에 최종 검사와 설계안에서 승인한 형식(.skill 또는 zip)의 패키징 추가 (#39)
* 참조 파일 규칙을 본문에 파일별 읽기 시점을 적는 방식으로 변경 (#39)
* 제작 모드 시험의 수행 여부와 서브 에이전트 실행 여부를 사용자에게 질의하는 방식으로 변경 (#39)
* 제작 모드의 프레임워크 선택, 프롬프트 출력 형식, 문서화 표, 참조 파일 목차 규칙 삭제 (#39)
* description과 조합 모드의 기획과 컨설팅 업무 한정 표현 삭제 (#39)
* 제작 모드에 다른 스킬이나 에이전트를 호출하는 지시는 사용자가 원할 때만 넣고 대체 동작을 함께 적는 규칙 추가 (#40)
* 형식 미지정 시 패키지 기본값을 .skill에서 실행 환경 판별 표의 권장 산출 형식으로 변경 (#40)
* 대화창에 스킬 저장 기능이 없는 환경에서 스킬 등록 절차를 사용자에게 확인하는 단계 추가 (#40)
* 조합 모드의 계획 방식을 단일 스킬, 순차 연결, 분기, 분할, 동적 분할, 평가 반복, 자율 진행 중 가장 단순한 유형의 선택으로 변경 (#41)
* 조합 모드의 고정 기본 단계 표를 산출물 단위 단계 분해와 단계별 통과 기준으로 변경 (#41)
* 조합 모드 단계의 통과 기준 미충족, 오류, 상한 도달 시 진행 중단과 선택지 제시 절차 추가 (#41)
* 조합 모드의 서브 에이전트와 별도 세션 사용 조건을 계획 승인 시 사용자 선택으로 변경 (#41)
* 자율 진행 선택 시 사용자 확인 지점, 단계 상한, 중단 조건의 질의 절차 추가 (#41)

### think-review
- Changed the scope for code to its classification structure (#37)
- Added an exception that applies the domain specification's category count and depth to code (#37)

* 코드의 적용 범위를 분류 구조로 변경 (#37)
* 코드의 항목 수와 계층 깊이에 도메인 명세 기준을 적용하는 예외 추가 (#37)

## 2026-10-24

### offline-deps-builder
- Changed the timing of the font redistribution check to the pre-sharing check (#36)
- Added a user confirmation step before connecting a substitute font (#36)

* 폰트 재배포 조건의 확인 시점을 공유 전 점검 단계로 변경 (#36)
* 대체 폰트 연결 전 사용자 확인 단계 추가 (#36)

## 2026-10-18

### biz-code-style
- Added a step that attaches GitHub repositories before accessing GitHub (#27, #28)

* GitHub 접근 전 GitHub 저장소 연결 단계 추가 (#27, #28)

### biz-code-style-lite
- Added a step that attaches GitHub repositories before accessing GitHub (#27, #28)

* GitHub 접근 전 GitHub 저장소 연결 단계 추가 (#27, #28)

### chart
- Added a step that attaches GitHub repositories before accessing GitHub (#26)

* GitHub 접근 전 GitHub 저장소 연결 단계 추가 (#26)

### offline-deps-builder
- Added a step that attaches GitHub repositories before accessing GitHub (#26)

* GitHub 접근 전 GitHub 저장소 연결 단계 추가 (#26)

### pref-architect
- Added a step that attaches GitHub repositories before accessing GitHub (#27)

* GitHub 접근 전 GitHub 저장소 연결 단계 추가 (#27)

## 2026-10-17

### Common
- Added SHA256SUMS.txt files with the checksums of the install packages to each skill folder (#24)
- Added a README note on building a dependency skill with offline-deps-builder where network access is blocked (#25)

* 스킬 폴더별 설치용 패키지의 체크섬을 담은 SHA256SUMS.txt 파일 추가 (#24)
* 네트워크 차단 환경에서 offline-deps-builder로 의존성 스킬을 생성하는 README 안내 추가 (#25)

### biz-code-style
- Added a rule that applies the commit message standard to PR messages (#22)
- Added a rule that keeps personal and company security information out of intermediate records (#22)

* 커밋 메시지 기준을 PR 메시지에도 적용하는 규칙 추가 (#22)
* 중간 기록에서 개인정보 및 사내 보안 정보를 제외하는 규칙 추가 (#22)

### biz-code-style-lite
- Added a rule that applies the commit message standard to PR messages (#22)
- Added a rule that keeps personal and company security information out of intermediate records (#22)

* 커밋 메시지 기준을 PR 메시지에도 적용하는 규칙 추가 (#22)
* 중간 기록에서 개인정보 및 사내 보안 정보를 제외하는 규칙 추가 (#22)

### pref-architect
- Added a rule that applies the commit message standard to PR messages (#22)
- Added a rule that keeps personal and company security information out of intermediate records (#22)

* 커밋 메시지 기준을 PR 메시지에도 적용하는 규칙 추가 (#22)
* 중간 기록에서 개인정보 및 사내 보안 정보를 제외하는 규칙 추가 (#22)

### slop-proof
- Changed the skill name from anti-slop to slop-proof (#23)

* 스킬 이름을 anti-slop에서 slop-proof로 변경 (#23)

## 2026-10-16

### chart
- Added a visual check loop that inspects the rendered image and renders again until no defects remain (#12)

* 결함 해소 시점까지 렌더링 이미지 검수와 재렌더링을 반복하는 시각 점검 단계 추가 (#12)

## 2026-10-13

### Common
- Added the first public release with the Korean and English editions of the skills

* 한국어판 및 영어판 스킬을 담은 최초 공개 버전 추가
