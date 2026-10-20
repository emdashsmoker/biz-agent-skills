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
- (Korean style) Write each Korean entry as one short formal sentence in note style with a noun ending. Avoid colloquial expressions.
- (Change types) Added (추가), Changed (변경), Fixed (수정), Removed (삭제), Action needed (필요)
- (Include) Changes to skill outputs, usage steps, or installation.
- (Exclude) Typo and wording fixes, demo image replacements, README changes unrelated to installation, internal refactoring without behavior changes, and commits that only change CHANGELOG.md.
- (Push) Commit on top of the latest main and push directly to main.
-->

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
* 네트워크 접근이 차단된 환경에서 offline-deps-builder로 의존성 스킬을 생성하는 README 안내 추가 (#25)

### biz-code-style
- Added a rule that applies the commit message standard to PR messages and keeps personal and company security information out of them (#22)

* 커밋 메시지 기준을 PR 메시지에 적용하여 개인정보 및 사내 보안 정보를 제외하는 규칙 추가 (#22)

### biz-code-style-lite
- Added a rule that applies the commit message standard to PR messages and keeps personal and company security information out of them (#22)

* 커밋 메시지 기준을 PR 메시지에 적용하여 개인정보 및 사내 보안 정보를 제외하는 규칙 추가 (#22)

### pref-architect
- Added a rule that applies the commit message standard to PR messages and keeps personal and company security information out of them (#22)

* 커밋 메시지 기준을 PR 메시지에 적용하여 개인정보 및 사내 보안 정보를 제외하는 규칙 추가 (#22)

### slop-proof
- Changed the skill name from anti-slop to slop-proof (#23)

* 스킬 이름을 anti-slop에서 slop-proof로 변경 (#23)

## 2026-10-16

### chart
- Added a visual check loop that inspects the rendered image and renders again until no defects remain (#12)

* 렌더링한 이미지를 검수하여 결함이 없을 때까지 다시 렌더링하는 시각 검수 단계 추가 (#12)

## 2026-10-13

### Common
- Added the first public release with the Korean and English editions of the skills

* 한국어판 및 영어판 스킬을 담은 최초 공개 버전 추가
