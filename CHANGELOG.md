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

## 2026-11-28

### biz-code-style
- Added a grammar check that restores a Korean noun-ending sentence to a declarative sentence with the omitted particles and the ending in place (rewriting of sentences that do not restore naturally or that change meaning) (#107)
- Added a step that reviews outward-facing text of automated work, such as commit messages, PR messages, posts, and emails, as a Markdown draft before publishing (check of reader needs, safe disclosure, and the skill rules, with questions to the user on ambiguous points) (#108)
- Added 판정, 짝, 통찰력 used as praise, 꽤 and 미친 듯이 to the non-preferred words (#109)
- Added usage conditions for 경로, 구조적, 실무적 and 감각 (경로 only for a physical or logical path whose existence is clearly confirmed) (#109)
- Added calques of English predicates such as -로 기능한다, 방어 가능하다, 회귀가 발생 and 버그를 닫다 to the translationese patterns (#109)
- Added "A라기보다 B" and recasting the other person's words before correcting them to contrast framing (#109)
- Added middle dots that are not part of official names to the symbol rules (#109)
- Added unfounded praise, post-hoc excuses and unfounded progress reports to the meta-commentary rules (#109)
- Added a rule that states results the writer ran and checked as settled (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 명사형 종결 문장을 생략된 조사와 종결 어미를 갖춘 평서문으로 복원하는 문법 점검 추가 (자연스럽게 복원되지 않거나 의미가 달라지는 문장의 재작성) (#107)
* 자동화 작업에서 커밋 메시지, PR 메시지, 게시글, 메일 등 외부에 게시하는 글을 마크다운 초안으로 먼저 검토하는 단계 추가 (외부 독자에게 필요한 내용, 공개해도 안전한 정보, 스킬 규칙 반영 여부의 점검과 모호한 지점의 사용자 질의) (#108)
* 비선호 어휘에 판정, 짝, 칭찬 용도의 통찰력, 꽤, 미친 듯이 추가 (#109)
* 경로, 구조적, 실무적, 감각의 사용 조건 추가 (경로는 실제로 존재함이 명백히 확인된 물리적, 논리적 길에 한정) (#109)
* 번역투 유형에 -로 기능한다, 방어 가능하다, 회귀가 발생, 버그를 닫다 등 영어 서술어 직역 추가 (#109)
* 대비 강조 유형에 A라기보다 B와 상대 발언을 단순화한 뒤 바로잡는 형태 추가 (#109)
* 기호 기준에 공식 명칭이 아닌 가운뎃점 추가 (#109)
* 메타 서술 기준에 근거 없는 칭찬, 사후 해명, 근거 없는 진행 보고 추가 (#109)
* 직접 실행하고 확인한 결과를 확정해서 쓰는 규칙 추가 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### biz-code-style-lite
- Added a grammar check that restores a Korean noun-ending sentence to a declarative sentence with the omitted particles and the ending in place (rewriting of sentences that do not restore naturally or that change meaning) (#107)
- Added a step that reviews outward-facing text of automated work, such as commit messages, PR messages, posts, and emails, as a Markdown draft before publishing (check of reader needs, safe disclosure, and the skill rules, with questions to the user on ambiguous points) (#108)
- Added 판정, 짝, 통찰력 used as praise, 꽤 and 미친 듯이 to the non-preferred words (#109)
- Added calques of English predicates such as -로 기능한다, 방어 가능하다, 회귀가 발생 and 버그를 닫다 to the translationese patterns (#109)
- Added a rule that states results the writer ran and checked as settled (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 명사형 종결 문장을 생략된 조사와 종결 어미를 갖춘 평서문으로 복원하는 문법 점검 추가 (자연스럽게 복원되지 않거나 의미가 달라지는 문장의 재작성) (#107)
* 자동화 작업에서 커밋 메시지, PR 메시지, 게시글, 메일 등 외부에 게시하는 글을 마크다운 초안으로 먼저 검토하는 단계 추가 (외부 독자에게 필요한 내용, 공개해도 안전한 정보, 스킬 규칙 반영 여부의 점검과 모호한 지점의 사용자 질의) (#108)
* 비선호 어휘에 판정, 짝, 칭찬 용도의 통찰력, 꽤, 미친 듯이 추가 (#109)
* 번역투 유형에 -로 기능한다, 방어 가능하다, 회귀가 발생, 버그를 닫다 등 영어 서술어 직역 추가 (#109)
* 직접 실행하고 확인한 결과를 확정해서 쓰는 규칙 추가 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### clear-comm
- Added 판정, 경로, 짝, 꽤 and 미친 듯이 to the expressions to avoid (#109)
- Added calques of English predicates to the translationese rules (#109)
- Added generic empathy lines and post-hoc excuses to the expressions to avoid (#109)
- Added a rule that keeps one speech level in a polite message (#109)
- Added middle dots that are not part of official names to the symbol rules (#109)

* 지양할 표현에 판정, 경로, 짝, 꽤, 미친 듯이 추가 (#109)
* 번역투 기준에 영어 서술어 직역 추가 (#109)
* 지양할 표현에 범용 공감 문구와 사후 해명 추가 (#109)
* 존댓말 글의 높임 등급을 하나로 유지하는 규칙 추가 (#109)
* 기호 기준에 공식 명칭이 아닌 가운뎃점 추가 (#109)

### digest
- Added a rule to write each Korean noun-ending sentence so that it restores to a natural declarative sentence with the same meaning when the omitted particles and the ending are added (#107)
- Added stock predicates such as serves as, and in Korean translations calques of English predicates and 판정, to the writing-style rules (#109)

* 명사형 종결 문장이 생략된 조사와 종결 어미를 갖추었을 때 의미가 같은 자연스러운 평서문으로 복원되도록 작성하는 규칙 추가 (#107)
* 작성 문체 기준에 영어 서술어 직역과 판정 추가 (번역본 포함) (#109)

### environment-analysis
- Added a grammar check that restores a Korean noun-ending sentence to a declarative sentence with the omitted particles and the ending in place (rewriting of sentences that do not restore naturally or that change meaning) (#107)
- Added calques of English predicates and unrequested caveats to the expressions to avoid (#109)
- Changed the internal capability wording to VRIO 진단 and the Five Forces wording to 5-Forces 분석 (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 명사형 종결 문장을 생략된 조사와 종결 어미를 갖춘 평서문으로 복원하는 문법 점검 추가 (자연스럽게 복원되지 않거나 의미가 달라지는 문장의 재작성) (#107)
* 지양할 표현에 영어 서술어 직역과 요청하지 않은 단서 추가 (#109)
* 내부역량 표기를 VRIO 진단으로, 경쟁강도 표기를 5-Forces 분석으로 변경 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### environment-analysis-lite
- Added a grammar check that restores a Korean noun-ending sentence to a declarative sentence with the omitted particles and the ending in place (rewriting of sentences that do not restore naturally or that change meaning) (#107)
- Added calques of English predicates and unrequested caveats to the expressions to avoid (#109)
- Changed the internal capability wording to VRIO 진단 and the Five Forces wording to 5-Forces 분석 (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 명사형 종결 문장을 생략된 조사와 종결 어미를 갖춘 평서문으로 복원하는 문법 점검 추가 (자연스럽게 복원되지 않거나 의미가 달라지는 문장의 재작성) (#107)
* 지양할 표현에 영어 서술어 직역과 요청하지 않은 단서 추가 (#109)
* 내부역량 표기를 VRIO 진단으로, 경쟁강도 표기를 5-Forces 분석으로 변경 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### five-forces
- Changed the Five Forces wording from 평가 to 분석 (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 경쟁강도 표기를 평가에서 분석으로 변경 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### grand-viz-style
- Added a rule to write each Korean noun-ending sentence of slide text so that it restores to a natural declarative sentence with the same meaning when the omitted particles and the ending are added (#107)

* 장표 문구의 명사형 종결 문장이 생략된 조사와 종결 어미를 갖추었을 때 의미가 같은 자연스러운 평서문으로 복원되도록 작성하는 규칙 추가 (#107)

### logical-write
- Added a grammar check that restores a Korean noun-ending sentence to a declarative sentence with the omitted particles and the ending in place (rewriting of sentences that do not restore naturally or that change meaning) (#107)
- Added 판정, 짝, 통찰력 used as praise, 꽤 and 미친 듯이 to the non-preferred words (#109)
- Added usage conditions for 경로, 구조적, 실무적 and 감각 (경로 only for a physical or logical path whose existence is clearly confirmed) (#109)
- Added calques of English predicates such as -로 기능한다, 방어 가능하다, 회귀가 발생 and 버그를 닫다 to the translationese patterns (#109)
- Added a rule that keeps the established Korean spelling of proper nouns (#109)
- Added "A라기보다 B" and recasting the other person's words before correcting them to contrast framing (#109)
- Added unfounded praise and rankings, generic empathy lines, post-hoc excuses, unfounded progress reports and unrequested caveats to the meta-commentary types (#109)
- Added conclusion reversal by a new criterion and hedging of verified results to conclusion avoidance (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 명사형 종결 문장을 생략된 조사와 종결 어미를 갖춘 평서문으로 복원하는 문법 점검 추가 (자연스럽게 복원되지 않거나 의미가 달라지는 문장의 재작성) (#107)
* 비선호 어휘에 판정, 짝, 칭찬 용도의 통찰력, 꽤, 미친 듯이 추가 (#109)
* 경로, 구조적, 실무적, 감각의 사용 조건 추가 (경로는 실제로 존재함이 명백히 확인된 물리적, 논리적 길에 한정) (#109)
* 번역투 유형에 -로 기능한다, 방어 가능하다, 회귀가 발생, 버그를 닫다 등 영어 서술어 직역 추가 (#109)
* 고유명사의 정착된 한글 표기를 유지하는 규칙 추가 (#109)
* 대비 강조 유형에 A라기보다 B와 상대 발언을 단순화한 뒤 바로잡는 형태 추가 (#109)
* 메타 서술 유형에 근거 없는 칭찬과 순위 평가, 범용 공감 문구, 사후 해명, 근거 없는 진행 보고, 요청하지 않은 단서 추가 (#109)
* 결론 회피 유형에 새 기준에 따른 결론 번복과 확인 사실 유보 추가 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### logical-write-lite
- Added a grammar check that restores a Korean noun-ending sentence to a declarative sentence with the omitted particles and the ending in place (rewriting of sentences that do not restore naturally or that change meaning) (#107)
- Added 판정, 짝, 통찰력 used as praise, 꽤 and 미친 듯이 to the non-preferred words (#109)
- Added usage conditions for 경로, 구조적, 실무적 and 감각 (경로 only for a physical or logical path whose existence is clearly confirmed) (#109)
- Added calques of English predicates such as -로 기능한다, 방어 가능하다, 회귀가 발생 and 버그를 닫다 to the translationese patterns (#109)
- Added "A라기보다 B" and recasting the other person's words before correcting them to contrast framing (#109)
- Added praise and excuses, and conclusion reversal, to the expression patterns (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 명사형 종결 문장을 생략된 조사와 종결 어미를 갖춘 평서문으로 복원하는 문법 점검 추가 (자연스럽게 복원되지 않거나 의미가 달라지는 문장의 재작성) (#107)
* 비선호 어휘에 판정, 짝, 칭찬 용도의 통찰력, 꽤, 미친 듯이 추가 (#109)
* 경로, 구조적, 실무적, 감각의 사용 조건 추가 (경로는 실제로 존재함이 명백히 확인된 물리적, 논리적 길에 한정) (#109)
* 번역투 유형에 -로 기능한다, 방어 가능하다, 회귀가 발생, 버그를 닫다 등 영어 서술어 직역 추가 (#109)
* 대비 강조 유형에 A라기보다 B와 상대 발언을 단순화한 뒤 바로잡는 형태 추가 (#109)
* 표현 패턴에 칭찬과 해명, 결론 번복 추가 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### long-task-ledger
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### network-analysis
- Added a rule to write each Korean noun-ending sentence of the report so that it restores to a natural declarative sentence with the same meaning when the omitted particles and the ending are added (#107)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 보고서의 명사형 종결 문장이 생략된 조사와 종결 어미를 갖추었을 때 의미가 같은 자연스러운 평서문으로 복원되도록 작성하는 규칙 추가 (#107)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### network-analysis-lite
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### no-meta-commentary
- Added unfounded praise and rankings, generic empathy lines, post-hoc excuses, unfounded progress reports and unrequested caveats to the meta-commentary types (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 메타 서술 유형에 근거 없는 칭찬과 순위 평가, 범용 공감 문구, 사후 해명, 근거 없는 진행 보고, 요청하지 않은 단서 추가 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### no-meta-commentary-lite
- Added unfounded praise and rankings, generic empathy lines, post-hoc excuses, unfounded progress reports and unrequested caveats to the meta-commentary types (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 메타 서술 유형에 근거 없는 칭찬과 순위 평가, 범용 공감 문구, 사후 해명, 근거 없는 진행 보고, 요청하지 않은 단서 추가 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### ontology-modeling
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### practical-calc
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### practical-stats
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### pref-architect
- Added a grammar check to the write-standard and code-standard modules that restores a Korean noun-ending sentence to a declarative sentence with the omitted particles and the ending in place (rewriting of sentences that do not restore naturally or that change meaning) (#107)
- Changed the metadata version of the skill and the generator-version of the bundled modules from 1.3 to 1.4 (#107)
- Added a step to the code-standard module that reviews outward-facing text of automated work, such as commit messages, PR messages, posts, and emails, as a Markdown draft before publishing (check of reader needs, safe disclosure, and the module rules, with questions to the user on ambiguous points) (#108)
- Changed the metadata version of the skill and the generator-version of the bundled modules from 1.4 to 1.5 (#108)
- Added the new slop rules to the write-standard module (words to avoid, calques of English predicates, proper nouns, praise and excuses, one conclusion under the user's criteria) (#109)
- Changed the metadata version of the skill and the generator-version of the write-standard, code-standard and staged-work modules from 1.5 to 1.6 (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* write-standard와 code-standard 모듈에 명사형 종결 문장을 생략된 조사와 종결 어미를 갖춘 평서문으로 복원하는 문법 점검 추가 (자연스럽게 복원되지 않거나 의미가 달라지는 문장의 재작성) (#107)
* 스킬의 metadata version과 동봉 모듈의 generator-version을 1.3에서 1.4로 변경 (#107)
* code-standard 모듈에 자동화 작업에서 커밋 메시지, PR 메시지, 게시글, 메일 등 외부에 게시하는 글을 마크다운 초안으로 먼저 검토하는 단계 추가 (외부 독자에게 필요한 내용, 공개해도 안전한 정보, 모듈 규칙 반영 여부의 점검과 모호한 지점의 사용자 질의) (#108)
* 스킬의 metadata version과 동봉 모듈의 generator-version을 1.4에서 1.5로 변경 (#108)
* write-standard 모듈에 신규 슬롭 규칙 추가 (피하는 말, 영어 서술어 직역, 고유명사 표기, 칭찬과 해명, 사용자 기준의 단일 결론) (#109)
* 스킬의 metadata version과 write-standard, code-standard, staged-work 모듈의 generator-version을 1.5에서 1.6으로 변경 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### project-plan
- Added a rule to write each Korean noun-ending sentence of the overview body so that it restores to a natural declarative sentence with the same meaning when the omitted particles and the ending are added (#107)
- Renamed 승계 분류 in the previous plan comparison table to 처리 방향 분류 (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 오버뷰 본문의 명사형 종결 문장이 생략된 조사와 종결 어미를 갖추었을 때 의미가 같은 자연스러운 평서문으로 복원되도록 작성하는 규칙 추가 (#107)
* 기존 계획 대조표의 승계 분류 명칭을 처리 방향 분류로 변경 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### rfp-strategy
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### skill-forge
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### slop-proof
- Added a grammar check that restores a Korean noun-ending sentence to a declarative sentence with the omitted particles and the ending in place (rewriting of sentences that do not restore naturally or that change meaning) (#107)
- Added 판정, 짝, 통찰력 used as praise, 꽤 and 미친 듯이 to the non-preferred words (#109)
- Added usage conditions for 경로, 구조적, 실무적 and 감각 (경로 only for a physical or logical path whose existence is clearly confirmed) (#109)
- Added calques of English predicates such as -로 기능한다, 방어 가능하다, 회귀가 발생 and 버그를 닫다 to the translationese patterns (#109)
- Added a rule that keeps the established Korean spelling of proper nouns (#109)
- Added "A라기보다 B" and recasting the other person's words before correcting them to contrast framing (#109)
- Added middle dots that are not part of official names to the symbol rules (#109)
- Added unfounded praise and rankings, generic empathy lines, post-hoc excuses, unfounded progress reports and unrequested caveats to the meta-commentary types (#109)
- Added conclusion reversal by a new criterion and hedging of verified results to conclusion avoidance (#109)

* 명사형 종결 문장을 생략된 조사와 종결 어미를 갖춘 평서문으로 복원하는 문법 점검 추가 (자연스럽게 복원되지 않거나 의미가 달라지는 문장의 재작성) (#107)
* 비선호 어휘에 판정, 짝, 칭찬 용도의 통찰력, 꽤, 미친 듯이 추가 (#109)
* 경로, 구조적, 실무적, 감각의 사용 조건 추가 (경로는 실제로 존재함이 명백히 확인된 물리적, 논리적 길에 한정) (#109)
* 번역투 유형에 -로 기능한다, 방어 가능하다, 회귀가 발생, 버그를 닫다 등 영어 서술어 직역 추가 (#109)
* 고유명사의 정착된 한글 표기를 유지하는 규칙 추가 (#109)
* 대비 강조 유형에 A라기보다 B와 상대 발언을 단순화한 뒤 바로잡는 형태 추가 (#109)
* 기호 기준에 공식 명칭이 아닌 가운뎃점 추가 (#109)
* 메타 서술 유형에 근거 없는 칭찬과 순위 평가, 범용 공감 문구, 사후 해명, 근거 없는 진행 보고, 요청하지 않은 단서 추가 (#109)
* 결론 회피 유형에 새 기준에 따른 결론 번복과 확인 사실 유보 추가 (#109)

### source-check
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### strategy-builder
- Added a rule to write each Korean noun-ending sentence so that it restores to a natural declarative sentence with the same meaning when the omitted particles and the ending are added (#107)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 명사형 종결 문장이 생략된 조사와 종결 어미를 갖추었을 때 의미가 같은 자연스러운 평서문으로 복원되도록 작성하는 규칙 추가 (#107)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### think-review
- Renamed the 등급 평가 step of the plan lens to 질문별 검토 (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 기획 관점의 등급 평가 단계 명칭을 질문별 검토로 변경 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

### think-review-lite
- Renamed the outcome section from 평가 to 검토 결과 and the 평가표 to 검토표 (#109)
- Changed the wording of the instructions to name the actual act instead of stock words such as 판정, 평가 and 짝, keeping 평가 for institutional and established concepts (#109)

* 점검 결과 절의 명칭을 평가에서 검토 결과로, 평가표를 검토표로 변경 (#109)
* 판정, 평가, 짝 등 상투 어휘 대신 실제 행위를 나타내는 어휘로 지침 문구 변경 (제도 용어와 확립된 개념의 평가는 유지) (#109)

## 2026-11-26

### biz-code-style
- Added a rule that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)

### biz-code-style-lite
- Added a rule that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)

### clear-comm
- Added a rule that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)

### digest
- Added a rule that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)

### environment-analysis
- Added a rule that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)

### environment-analysis-lite
- Added a rule that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)

### logical-write
- Added a rule that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)

### logical-write-lite
- Added a rule that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)

### network-analysis
- Added a rule that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)

### no-meta-commentary
- Added a step to the subject test that reads a sentence about the work, actions, procedures and guidelines of individuals, organizations and society again with "the AI model" as its subject or modifier, and treats a sentence that reads more naturally than the original as meta-commentary (#106)

* 주어 테스트에 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 서술한 문장의 주어나 수식어 자리에 'AI 모델'을 넣어 다시 읽는 절차 추가 (원래 문장보다 자연스럽게 읽히는 문장의 메타적 서술 판별) (#106)

### no-meta-commentary-lite
- Added a step to the subject test that reads a sentence about the work, actions, procedures and guidelines of individuals, organizations and society again with "the AI model" as its subject or modifier, and treats a sentence that reads more naturally than the original as meta-commentary (#106)

* 주어 테스트에 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 서술한 문장의 주어나 수식어 자리에 'AI 모델'을 넣어 다시 읽는 절차 추가 (원래 문장보다 자연스럽게 읽히는 문장의 메타적 서술 판별) (#106)

### pref-architect
- Added a rule to the write-standard module that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)
- Changed the metadata version of the skill and the generator-version of the bundled modules from 1.2 to 1.3 (#106)

* write-standard 모듈에 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)
* 스킬의 metadata version과 동봉 모듈의 generator-version을 1.2에서 1.3으로 변경 (#106)

### project-plan
- Added a rule that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)

### rfp-strategy
- Added a rule that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)

### slop-proof
- Added a formulaic rhetoric pattern for sentences that depict the work, actions, procedures and guidelines of individuals, organizations and society as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on), rewritten through the actor and the actual action (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 문장의 정형 수사 패턴 추가 (행위 주체와 실제 행위로 재작성) (#106)

### strategy-builder
- Added a rule that describes the work, actions, procedures and guidelines of individuals, organizations and society through the actor and the actual action, without depicting them as the workings of a computer, machine or software architecture (input, processing, output, pass, gate and so on) (#106)

* 개인, 조직, 사회의 업무, 행동, 절차, 지침 등을 행위 주체와 실제 행위로 서술하는 규칙 추가 (컴퓨터, 기계, 소프트웨어 구조의 작동 방식처럼 묘사한 서술의 방지) (#106)

## 2026-11-24

### biz-code-style
- Added a clarity check that asks "So what does it mean?" and "Why can you say that?" after a sentence, comment, prompt or similar text is written, and rewrites a sentence that cannot answer both questions right away (#100)
- Added a meta information check that puts "the writer", "to the writer", "the model that wrote the text", or "the AI provider" in front of a sentence, and rewrites a sentence that still reads naturally with its meaning unchanged (#100)

* 문장, 주석, 프롬프트 등을 쓴 뒤 "그래서 무엇을 뜻하는가"와 "왜 그렇게 말할 수 있는가"를 되묻는 명료성 점검 추가 (두 질문에 바로 답하지 못하는 문장의 재작성) (#100)
* 문장 앞에 '작성자가', '작성자에게', '글을 작성한 모델이', 'AI 제공자가'를 붙여 메타 정보를 판별하는 점검 추가 (원래 뜻 그대로 읽히는 문장의 재작성) (#100)

### biz-code-style-lite
- Added a clarity check that asks "So what does it mean?" and "Why can you say that?" after a sentence, comment, prompt or similar text is written, and rewrites a sentence that cannot answer both questions right away (#100)
- Added a meta information check that puts "the writer", "to the writer", "the model that wrote the text", or "the AI provider" in front of a sentence, and rewrites a sentence that still reads naturally with its meaning unchanged (#100)

* 문장, 주석, 프롬프트 등을 쓴 뒤 "그래서 무엇을 뜻하는가"와 "왜 그렇게 말할 수 있는가"를 되묻는 명료성 점검 추가 (두 질문에 바로 답하지 못하는 문장의 재작성) (#100)
* 문장 앞에 '작성자가', '작성자에게', '글을 작성한 모델이', 'AI 제공자가'를 붙여 메타 정보를 판별하는 점검 추가 (원래 뜻 그대로 읽히는 문장의 재작성) (#100)

### grand-viz-style
- Added a clarity check for slide copy that asks "So what does it mean?" and "Why can you say that?" after the copy is written, and rewrites copy that cannot answer both questions right away (#100)
- Added a check that puts "the maker", "to the maker", "the model that wrote the text", or "the AI provider" in front of slide copy, and rewrites copy that still reads naturally with its meaning unchanged as unneeded meta narration (#100)
- Changed the readability check for shapes that hold text to ask whether the text and copy are aligned to the vertical center (#101)
- Changed the verification from a single check to a loop that re-renders each fixed slide, rechecks every item from the start, and repeats until no defect remains (#102)
- Added a table rule that keeps a table's placement, alignment and spacing to neighboring shapes and text in harmony with the rest of the slide, because tables tend to look detached from their surroundings (#105)

* 장표 문구를 쓴 뒤 "그래서 무엇을 뜻하는가"와 "왜 그렇게 말할 수 있는가"를 되묻는 명료성 점검 추가 (두 질문에 바로 답하지 못하는 문구의 재작성) (#100)
* 문구 앞에 '작업자가', '작업자에게', '글을 작성한 모델이', 'AI 제공자가'를 붙여 메타적 서술을 판별하는 점검 추가 (원래 뜻 그대로 읽히는 문구의 청중 관점 재작성) (#100)
* 글자를 담은 도형의 가독성 점검 항목을 글자 및 문구의 세로 기준 가운데 정렬 확인으로 변경 (#101)
* 검증 절차를 1회 점검에서 결함 해소 시점까지의 반복 점검으로 변경 (수정한 장표의 재렌더링과 전체 항목 재확인) (#102)
* 표의 배치와 정렬, 이웃한 도형과 글자까지의 간격을 장표의 다른 요소와 조화시키는 표 규칙 추가 (주변 요소와 동떨어져 보이기 쉬운 표의 보완) (#105)

### logical-write
- Added a clarity check below the pre-output checklist that asks "So what does it mean?" and "Why can you say that?" after a sentence is written, and rewrites a sentence that cannot answer both questions right away (#100)
- Added a step to the subject test that restores an omitted subject by putting "the writer", "to the writer", "the model that wrote the text", or "the AI provider" in front of the sentence, and treats a sentence that still reads naturally with its meaning unchanged as meta commentary (#100)

* 산출 전 점검에 문장을 쓴 뒤 "그래서 무엇을 뜻하는가"와 "왜 그렇게 말할 수 있는가"를 되묻는 명료성 점검 추가 (두 질문에 바로 답하지 못하는 문장의 재작성) (#100)
* 주어 테스트에 문장 앞에 '작성자가', '작성자에게', '글을 작성한 모델이', 'AI 제공자가'를 붙이는 생략 주어 복원 절차 추가 (원래 뜻 그대로 읽히는 문장의 메타 서술 판정) (#100)

### logical-write-lite
- Added a clarity check below the pre-output checklist that asks "So what does it mean?" and "Why can you say that?" after a sentence is written, and rewrites a sentence that cannot answer both questions right away (#100)
- Added a step to the subject test that restores an omitted subject by putting "the writer", "to the writer", "the model that wrote the text", or "the AI provider" in front of the sentence, and treats a sentence that still reads naturally with its meaning unchanged as meta commentary (#100)

* 산출 전 점검에 문장을 쓴 뒤 "그래서 무엇을 뜻하는가"와 "왜 그렇게 말할 수 있는가"를 되묻는 명료성 점검 추가 (두 질문에 바로 답하지 못하는 문장의 재작성) (#100)
* 주어 테스트에 문장 앞에 '작성자가', '작성자에게', '글을 작성한 모델이', 'AI 제공자가'를 붙이는 생략 주어 복원 절차 추가 (원래 뜻 그대로 읽히는 문장의 메타 서술 판정) (#100)

### no-meta-commentary
- Added a step to the subject test that restores an omitted subject by putting "the writer", "to the writer", "the model that wrote the text", or "the AI provider" in front of the sentence, and treats a sentence that still reads naturally with its meaning unchanged as meta commentary (#100)

* 주어 테스트에 문장 앞에 '작성자가', '작성자에게', '글을 작성한 모델이', 'AI 제공자가'를 붙이는 생략 주어 복원 절차 추가 (원래 뜻 그대로 읽히는 문장의 메타 서술 판정) (#100)

### no-meta-commentary-lite
- Added a step to the subject test that restores an omitted subject by putting "the writer", "to the writer", "the model that wrote the text", or "the AI provider" in front of the sentence, and treats a sentence that still reads naturally with its meaning unchanged as meta commentary (#100)

* 주어 테스트에 문장 앞에 '작성자가', '작성자에게', '글을 작성한 모델이', 'AI 제공자가'를 붙이는 생략 주어 복원 절차 추가 (원래 뜻 그대로 읽히는 문장의 메타 서술 판정) (#100)

### ontology-modeling
- Added a step to the subject test that restores an omitted subject by putting "the writer", "to the writer", "the model that wrote the text", or "the AI provider" in front of the sentence, and treats a sentence that still reads naturally with its meaning unchanged as meta commentary (#100)

* 주어 테스트에 문장 앞에 '작성자가', '작성자에게', '글을 작성한 모델이', 'AI 제공자가'를 붙이는 생략 주어 복원 절차 추가 (원래 뜻 그대로 읽히는 문장의 메타 서술 판정) (#100)

### pref-architect
- Added a clarity check to the write-standard and code-standard modules that asks "So what does it mean?" and "Why can you say that?" after a sentence is written, and rewrites a sentence that cannot answer both questions right away (#100)
- Added a meta information check to the write-standard and code-standard modules that puts "the writer", "to the writer", "the model that wrote the text", or "the AI provider" in front of a sentence, and rewrites a sentence that still reads naturally with its meaning unchanged (#100)
- Changed the metadata version of the skill and the generator-version of the bundled modules from 1.1 to 1.2 (#100)

* write-standard와 code-standard 모듈에 문장을 쓴 뒤 "그래서 무엇을 뜻하는가"와 "왜 그렇게 말할 수 있는가"를 되묻는 명료성 점검 추가 (두 질문에 바로 답하지 못하는 문장의 재작성) (#100)
* write-standard와 code-standard 모듈에 문장 앞에 '작성자가', '작성자에게', '글을 작성한 모델이', 'AI 제공자가'를 붙여 메타 정보를 판별하는 점검 추가 (원래 뜻 그대로 읽히는 문장의 재작성) (#100)
* 스킬의 metadata version과 동봉 모듈의 generator-version을 1.1에서 1.2로 변경 (#100)

### skill-forge
- Added a clarity check for instruction sentences to the body writing rules, which asks "So what does it mean?" and "Why can you say that?" and rewrites an instruction that cannot answer both questions right away (#100)
- Added a meta information check for instruction sentences to the body writing rules, which puts "the writer", "to the writer", "the model that wrote the text", or "the AI provider" in front of a sentence and rewrites a sentence that still reads naturally from the skill user's point of view (#100)

* 본문 작성 규칙에 지시 문장을 쓴 뒤 "그래서 무엇을 뜻하는가"와 "왜 그렇게 말할 수 있는가"를 되묻는 명료성 점검 추가 (두 질문에 바로 답하지 못하는 지시의 재작성) (#100)
* 본문 작성 규칙에 문장 앞에 '작성자가', '작성자에게', '글을 작성한 모델이', 'AI 제공자가'를 붙여 메타 정보를 판별하는 점검 추가 (원래 뜻 그대로 읽히는 문장의 스킬 사용자 관점 재작성) (#100)

### slop-proof
- Added a step to the subject test that restores an omitted subject by putting "the writer", "to the writer", "the model that wrote the text", or "the AI provider" in front of the sentence, and treats a sentence that still reads naturally with its meaning unchanged as meta commentary (#100)

* 주어 테스트에 문장 앞에 '작성자가', '작성자에게', '글을 작성한 모델이', 'AI 제공자가'를 붙이는 생략 주어 복원 절차 추가 (원래 뜻 그대로 읽히는 문장의 메타 서술 판정) (#100)

## 2026-11-22

### biz-code-style
- Added a rule that writes prompts and instructions for LLMs and agents in the positive form, with the reason that a positive instruction states the target state directly (#86)
- Added a reason to the positive phrasing rule: a positive sentence states the target state directly, so it is clear and easy to revise and combine sentence by sentence (#86)

* LLM 및 에이전트에 전달하는 프롬프트와 지침의 긍정형 작성 규칙 추가 (목표 상태를 직접 나타내는 긍정형 지시의 명료성을 근거로 명시) (#86)
* 긍정 표현 우선 규칙에 근거 문장 추가 (목표 상태의 직접 제시에 따른 명료성 및 문장 단위의 수정과 결합 용이성) (#86)

### biz-code-style-lite
- Added a rule that writes prompts and instructions for LLMs and agents in the positive form, with the reason that a positive instruction states the target state directly (#86)
- Added a reason to the positive phrasing rule: a positive sentence states the target state directly, so it is clear and easy to revise and combine sentence by sentence (#86)

* LLM 및 에이전트에 전달하는 프롬프트와 지침의 긍정형 작성 규칙 추가 (목표 상태를 직접 나타내는 긍정형 지시의 명료성을 근거로 명시) (#86)
* 긍정 표현 우선 규칙에 근거 문장 추가 (목표 상태의 직접 제시에 따른 명료성 및 문장 단위의 수정과 결합 용이성) (#86)

### digest
- Fixed HWPX tables missing from the Markdown output with python-hwpx 7.0, which moved export_markdown to a separate package, by pinning python-hwpx to 6.12.0 in the install command and the missing-dependency hint (#99)

* python-hwpx 7.0의 export_markdown 이동에 따른 HWPX 표의 마크다운 변환 누락 오류 수정 (설치 명령과 미설치 안내의 python-hwpx 6.12.0 고정) (#99)

### environment-analysis
- Added a placement criterion that puts each fact in one category by the kind of thing it describes, with a table of facts that are easy to misplace (#87)
- Changed government programs with a set budget, period and implementing body to go to the investment category, with each program named in the measures column of its policy (#87)
- Changed the policy category to cover policy directions and to organize policy literature (#87)
- Added a separate regulation table that records the stage of each rule (#87)
- Changed technology trends to record where a technology stands on its development path through performance level, maturity, R&D level and R&D trends, with public literature used first (#87)
- Changed investment trends to divide by source of funds (public, private) and by use (R&D, other than R&D) (#87)
- Added budget classification, program type and program period columns to the public investment table (#87)
- Added a scope step that fixes where an industry or technology topic sits in a classification of its field (#87)
- Added scope questions on whether the policy category covers political conditions and which label it takes (#87)
- Changed the P label of PEST, STEEP and PESTEL to policy (#87)

* 사실이 서술하는 대상의 종류로 범주를 정하는 배치 기준 및 혼동하기 쉬운 사실의 배치 표 추가 (#87)
* 예산, 기간, 수행 주체가 정해진 정부 사업의 배치를 투자 범주로 변경 (정책 테이블에는 추진 방안 열의 사업명으로 기재) (#87)
* 정책 범주의 대상 및 정리 자료의 표기를 정책 방향 및 정책 문헌으로 변경 (#87)
* 규범의 진행 단계를 기재하는 제도와 규제 테이블 추가 (#87)
* 기술 동향의 기록 내용을 발전 경로상의 위치(성능 수준, 성숙도, 연구개발 수준, 연구개발 동향)로 변경 (공개 문헌 우선 활용) (#87)
* 투자 동향의 구분 기준을 재원(공공, 민간) 및 용도(연구개발, 연구개발 외)로 변경 (#87)
* 공공 투자 테이블에 재정 구분, 사업 유형, 사업 기간 열 추가 (#87)
* 산업 및 기술 주제의 분류상 위치를 정하는 범위 설정 절차 추가 (#87)
* 정치 상황의 포함 여부 및 정책 범주 명칭을 묻는 범위 설정 질문 추가 (#87)
* PEST, STEEP, PESTEL의 P 항목 표기를 정책으로 변경 (#87)

### environment-analysis-lite
- Added a placement criterion that puts each fact under one item by the kind of thing it describes (#87)
- Changed government programs with a set budget and period to go to investment trends (#87)
- Changed policy and regulation into separate items (#87)
- Changed investment trends to divide by source of funds (public, private) and by use (R&D, other than R&D) (#87)
- Added a rule that fixes where an industry or technology target sits in a classification of its field (#87)
- Added scope questions on whether the policy item covers political conditions and which label it takes (#87)
- Changed the P label of PEST and STEEP to policy (#87)

* 사실이 서술하는 대상의 종류로 항목을 정하는 배치 기준 추가 (#87)
* 예산 및 기간이 정해진 정부 사업의 배치를 투자 동향으로 변경 (#87)
* 정책 항목과 제도와 규제 항목의 구성을 별도 항목으로 변경 (#87)
* 투자 동향의 구분 기준을 재원(공공, 민간) 및 용도(연구개발, 연구개발 외)로 변경 (#87)
* 산업 및 기술 대상의 분류상 위치를 정하는 규칙 추가 (#87)
* 정치 상황의 포함 여부 및 정책 항목 명칭을 묻는 범위 설정 질문 추가 (#87)
* PEST, STEEP의 P 항목 표기를 정책으로 변경 (#87)

### grand-viz-style
- Changed the default accent from red to an orange-leaning vermilion that stays vivid at the lightness that passes 4.5:1 with white text (#83)
- Changed the color order to apply to each role so that only unspecified roles fall to the defaults (#83)
- Added a rule that asks the user how to assign the primary and accent colors when a warm primary meets the default accent (#83)
- Added a rule that uses a lightness step of a color field when neither white nor dark text reaches 4.5:1 for normal text on it (#83)
- Added a line that adjusts colors that look jarring or unnatural to the audience and practitioners during verification toward what is easy to read, pleasant and natural (#83)
- Changed the slide text rule to leave out meta information from the maker's point of view, including notes that drafting rules such as the same scale or a zero baseline were followed (#84)
- Added a use setting rule that follows a stated or clearly implied venue and distribution and otherwise proceeds without asking as screen showing at a large venue with no handouts (#88)
- Changed the information density rule so that carrying the situation, cause and direction on the slide applies to slides that double as printed handouts (#88)
- Changed the background lightness for requests that leave the lighting unknown, including requests under the large-venue default, to follow the slide's purpose and subject, with a light background when these do not settle the choice (#91)
- Removed large screens and screen-only showing from the conditions that favor a dark background (#91)
- Added a principle that a slide delivers one message, with content that belongs to another message moved to a separate slide (#92)
- Changed the photo caption rule from every photo to photos that need a caption (#94)
- Added a line that leaves images placed for decoration or metaphor without a caption, whether they are photos or generated images (#94)

* 기본 강조색을 적색 계열에서 흰 글자와 4.5:1 대비를 내는 명도에서도 선명한 주황 쪽 주홍 계열로 변경 (#83)
* 색 결정 순서를 지정되지 않은 역할만 기본값으로 채우는 역할별 적용 방식으로 변경 (#83)
* 따뜻한 주조색과 기본 강조색이 겹치는 경우의 주조색과 강조색 배정 질의 규칙 추가 (#83)
* 흰 글자와 짙은 글자 모두 4.5:1에 못 미치는 색면의 일반 글자용 명도 단계 규칙 추가 (#83)
* 청중과 실무자의 눈에 거슬리거나 부자연스러운 색의 검증 단계 조정 문장 추가 (#83)
* 같은 축척 적용, 0 기준선 등 작성 기준의 준수 사실을 포함한 작업자 관점 메타 정보를 장표에서 제외하도록 글자 규칙 변경 (#84)
* 용도 미기재 요청의 용도를 자료 배포 없는 대형 발표장의 화면 상영으로 정하는 용도 판단 규칙 추가 (명시하거나 요청에 드러난 용도는 그대로 적용) (#88)
* 현황, 원인, 방향을 장표 안에 모두 갖추는 정보 밀도 기준의 적용 대상을 인쇄 배포 겸용 장표로 변경 (#88)
* 조명을 알 수 없는 요청(대형 발표장 기본값 적용 요청 포함)의 배경 명도 판단 기준을 장표의 목적과 주제로 변경 (목적과 주제로 가려지지 않는 경우 밝은 배경 선택) (#91)
* 짙은 배경이 유리한 조건에서 대형 화면 및 화면 상영 전용 삭제 (#91)
* 장표 1장에 메시지 1개만 담는 원칙 추가 (다른 메시지에 해당하는 내용의 별도 장표 분리 포함) (#92)
* 사진 설명 규칙의 적용 대상을 모든 사진에서 설명이 필요한 사진으로 변경 (#94)
* 장식이나 비유를 위해 넣은 이미지를 설명 없이 두는 규칙 추가 (사진과 생성 이미지 모두 적용) (#94)

### lean-work
- Added a sentence rule that states the same content in the positive form, with the reason that a positive sentence states the target state directly (#86)
- Removed the summary mode that produced fixed-format summaries of web pages, files and pasted text, with its trigger phrases such as "summarize" and "brief me" (#89)
- Removed the sentence rules, the concise-answer example and the concision trigger phrases such as "be concise" and "just the key points" (#89)
- Added ECRS criteria that apply eliminate, combine, rearrange and simplify in this order to work steps and expression elements, with a criteria table for each mode (#89)
- Added a work design procedure, a revision procedure for work processes and an expression procedure for new output (#89)
- Added a chart example, the message overload definition and checklist items on mixed element kinds and header consistency (#89)
- Changed the default reader to a general adult reader without background in the field (#89)
- Changed the unit examples to open lists that name a subheading or paragraph of a text, the headline or a component of a slide and a data item (#89)
- Added output rules that keep internal work content, the terms of the skill and meta-commentary out of the output (#89)
- Changed the output rule on skill terms to cover only the terms and internal frameworks the skill defines, so plain words such as message, reader and scope stay usable in the output (#90)
- Fixed the slide example so that it moves the industry structure items, which its diagnosis calls an independent message, to a third slide (#90)

* 같은 내용의 긍정 표현 서술 규칙 추가 (목표 상태를 직접 나타내는 긍정 문장의 명료성을 근거로 명시) (#86)
* 웹 페이지, 파일, 붙여넣은 글을 고정 포맷으로 요약하던 요약 모드와 "요약해줘", "브리핑해줘" 등의 발동 문구 삭제 (#89)
* 문장 규칙, 간결 응답 예시, "간결하게", "핵심만" 등의 발동 문구 삭제 (#89)
* 작업 단계와 표현 요소에 제거, 결합, 재배열, 단순화를 순서대로 적용하는 ECRS 기준과 모드별 기준 표 추가 (#89)
* 작업 설계 절차, 작업 절차의 교정 절차, 신규 작성용 표현 절차 추가 (#89)
* 차트 예시, 메시지 과적 정의, 성격이 다른 요소의 혼재 및 헤더 일치 점검 항목 추가 (#89)
* 독자 기본값을 해당 분야의 배경지식이 없는 일반 성인으로 변경 (#89)
* 단위 예시를 글의 소제목이나 문단, 슬라이드의 헤드라인이나 구성요소, 데이터 항목 등의 열린 목록으로 변경 (#89)
* 내부 작업 내용, 스킬 용어, 메타적 표현을 산출물에 담지 않는 산출물 규칙 추가 (#89)
* 산출물에 쓰지 않는 용어의 범위를 스킬이 정의한 고유 용어와 내부 프레임워크로 변경 (메시지, 독자, 범위 등 일반 단어의 산출물 사용 허용) (#90)
* 독립 메시지로 진단한 산업 구조 항목을 세 번째 슬라이드로 옮기도록 슬라이드 예시 수정 (#90)

### logical-write
- Added a reason to the positive phrasing rule: a positive sentence states the target state directly, so it is clear and easy to revise and combine sentence by sentence (#86)

* 긍정 표현 우선 규칙에 근거 문장 추가 (목표 상태의 직접 제시에 따른 명료성 및 문장 단위의 수정과 결합 용이성) (#86)

### logical-write-lite
- Added a reason to the positive phrasing rule: a positive sentence states the target state directly, so it is clear and easy to revise and combine sentence by sentence (#86)

* 긍정 표현 우선 규칙에 근거 문장 추가 (목표 상태의 직접 제시에 따른 명료성 및 문장 단위의 수정과 결합 용이성) (#86)

### md-parser
- Fixed HWPX tables missing from the Markdown output with python-hwpx 7.0, which moved export_markdown to a separate package, by pinning python-hwpx to 6.12.0 in the install command (#99)

* python-hwpx 7.0의 export_markdown 이동에 따른 HWPX 표의 마크다운 변환 누락 오류 수정 (설치 명령의 python-hwpx 6.12.0 고정) (#99)

### practical-calc-lite
- Fixed HWPX tables missing from the Markdown output with python-hwpx 7.0, which moved export_markdown to a separate package, by pinning python-hwpx to 6.12.0 in the install command (#99)

* python-hwpx 7.0의 export_markdown 이동에 따른 HWPX 표의 마크다운 변환 누락 오류 수정 (설치 명령의 python-hwpx 6.12.0 고정) (#99)

### pref-architect
- Added a rule to the code-standard module that writes prompts and instructions for LLMs and agents in the positive form (#86)
- Added a reason to the rule of the always-on instruction guide that writes what to do (#86)
- Added a reason to the positive phrasing rule of the write-standard module (#86)
- Changed the metadata version and the generator-version of the bundled modules from 1.0 to 1.1 (#86)
- Added a rule that raises the metadata version when a bundled source or the always-on instruction template changes (#86)
- Added a rebuilding step that compares the installed skill's metadata version with the distribution repository when version values differ and lets the user choose how to proceed (#86)

* code-standard 모듈에 LLM 및 에이전트에 전달하는 프롬프트와 지침의 긍정형 작성 규칙 추가 (#86)
* 상시 지침 작성법의 해야 할 일 기재 규칙에 근거 문장 추가 (#86)
* write-standard 모듈의 긍정 표현 규칙에 근거 문장 추가 (#86)
* metadata version 및 동봉 모듈의 generator-version을 1.0에서 1.1로 변경 (#86)
* 동봉 원본 또는 상시 지침 서식 변경 시의 metadata version 상향 규칙 추가 (#86)
* 버전 값 불일치 시 배포 저장소와의 metadata version 대조 및 사용자의 진행 방식 선택 단계를 재구성 절차에 추가 (#86)

### project-plan
- Fixed HWPX conversion falling back to the built-in XML reader with python-hwpx 7.0, which moved export_markdown to a separate package, by naming python-hwpx 6.12.0 as the optional HWPX dependency (#99)

* python-hwpx 7.0의 export_markdown 이동에 따른 HWPX 변환의 내장 XML 추출 전환 오류 수정 (선택 의존성의 python-hwpx 6.12.0 지정) (#99)

### rfp-strategy
- Fixed HWPX tables missing from the Markdown output with python-hwpx 7.0, which moved export_markdown to a separate package, by pinning python-hwpx to 6.12.0 in the install command (#99)

* python-hwpx 7.0의 export_markdown 이동에 따른 HWPX 표의 마크다운 변환 누락 오류 수정 (설치 명령의 python-hwpx 6.12.0 고정) (#99)

### skill-forge
- Added a body-writing rule that states instructions in the positive form, with the reason that a positive instruction states the target state directly (#86)
- Added Guide mode that explains how to use a specific skill and writes a copy-ready request prompt (#93)
- Added deliverables to the items of the Guide mode usage table (#95)
- Added the skill's limits and the harness features it needs to the items of the Guide mode usage table (#96)
- Added a table to the Guide mode answer that explains the skill's own terms and proper nouns for first-time users (#97)
- Added the skill's purpose and intended users to the items of the Guide mode usage table (#98)

* 본문 작성 규칙에 지시의 긍정형 기술 규칙 추가 (목표 상태를 직접 나타내는 긍정형 지시의 명료성을 근거로 명시) (#86)
* 특정 스킬의 사용 방법 설명과 복사용 요청 프롬프트 작성을 담당하는 안내 모드 추가 (#93)
* 안내 모드의 사용 안내 표 항목에 산출물 추가 (#95)
* 안내 모드의 사용 안내 표 항목에 한계 및 필요한 하네스 기능 추가 (#96)
* 안내 모드의 답변에 처음 접하는 사용자를 위한 스킬 고유 용어 및 고유명사 풀이 표 추가 (#97)
* 안내 모드의 사용 안내 표 항목에 목적 및 대상 사용자 추가 (#98)

## 2026-11-21

### grand-viz-style
- Added the grand-viz-style skill that sets the visual direction for rich, formal slides at large project briefings, policy announcements and vision ceremonies of Korean public institutions and large corporations (#81)

* 국내 공공기관과 대기업의 대형 사업 설명회, 정책 발표, 비전 선포식에 맞는 장표 시각화 방향 설정 스킬 추가 (#81)

### no-meta-commentary
- Added the no-meta-commentary skill that removes meta-commentary about the text, the writing process, the writer or the user's request, and unrequested reverse statements such as counterexamples and reverse logic (#81)

* 글 자체, 작성 과정, 작성자, 사용자 요청을 다루는 메타적 서술과 요청하지 않은 역방향 서술(반례, 역논리 등)의 제거 스킬 추가 (#81)

### no-meta-commentary-lite
- Added the lite edition of no-meta-commentary, which holds the same type names and examples in a single SKILL.md (#81)

* 정식판과 같은 유형 이름과 예시를 SKILL.md 하나에 담은 no-meta-commentary 경량판 추가 (#81)

## 2026-11-20

### pref-architect
- Added an optional off-switch skill that keeps chosen modules from loading in the conversation where the user calls it, with interview group G and a bundled source file (#80)
- Added a section that defines the generation mark (generator and generator-version) as a part of the rebuilding function (#80)

* 사용자가 호출한 대화에서 지정한 모듈의 로드를 끄는 선택형 해제 스킬 추가 (인터뷰 G묶음 및 동봉 원본 파일 포함) (#80)
* 생성 표시(generator 및 generator-version)를 재구성 기능의 구성 요소로 정의하는 절 추가 (#80)

## 2026-11-18

### biz-code-style
- Added a vocabulary-level rule that keeps jargon and software-design phrasing (input value, output, mapping and so on) within the reader's level and prevents oversimplification that underestimates the reader (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Changed the scope of the rule that states cited content in place from sources to other pages, slides and so on (#79)
- Added a rule against replacing content with codes, numbers, abbreviations or summary labels (#79)

* 독자 수준에 맞춘 어휘 규칙 추가 (전문용어와 소프트웨어 설계 어투의 남발 및 독자를 과소평가한 과잉 평이화 방지) (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 인용 내용 직접 기재 규칙의 적용 범위를 문헌에서 다른 쪽, 슬라이드 등으로 확대 변경 (#79)
* 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지 규칙 추가 (#79)

### biz-code-style-lite
- Added a vocabulary-level rule that keeps jargon and software-design phrasing (input value, output, mapping and so on) within the reader's level and prevents oversimplification that underestimates the reader (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Added a self-contained writing rule that states the needed content in place when referring to other pages, slides, sources, data and so on, without replacing content with codes, numbers, abbreviations or summary labels (#79)

* 독자 수준에 맞춘 어휘 규칙 추가 (전문용어와 소프트웨어 설계 어투의 남발 및 독자를 과소평가한 과잉 평이화 방지) (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 자기완결 서술 규칙 추가 (다른 쪽, 슬라이드, 문헌, 데이터 등의 언급 시 필요한 내용의 직접 기재 및 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지) (#79)

### clear-comm
- Added a vocabulary-level rule that keeps jargon and software-design phrasing (input value, output, mapping and so on) within the reader's level and prevents oversimplification that underestimates the reader (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Added a self-contained writing rule that states the needed content in place when referring to an earlier email, a page of an attachment, a meeting agenda number and so on, without replacing content with codes, numbers, abbreviations or summary labels (#79)

* 독자 수준에 맞춘 어휘 규칙 추가 (전문용어와 소프트웨어 설계 어투의 남발 및 독자를 과소평가한 과잉 평이화 방지) (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 자기완결 서술 규칙 추가 (이전 메일, 첨부 문서의 쪽, 회의 안건 번호 등의 언급 시 필요한 내용의 직접 기재 및 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지) (#79)

### digest
- Added a vocabulary-level rule that keeps jargon and software-design phrasing (input value, output, mapping and so on) within the reader's level and prevents oversimplification that underestimates the reader (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Added a self-contained writing rule that states the needed content in place when referring to other pages, slides, agenda items, cited sources and so on in the original, without replacing content with codes, numbers, abbreviations or summary labels (#79)

* 독자 수준에 맞춘 어휘 규칙 추가 (전문용어와 소프트웨어 설계 어투의 남발 및 독자를 과소평가한 과잉 평이화 방지) (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 자기완결 서술 규칙 추가 (원문의 다른 쪽, 슬라이드, 안건, 인용 문헌 등의 언급 시 필요한 내용의 직접 기재 및 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지) (#79)

### environment-analysis
- Added a vocabulary-level rule that keeps jargon and software-design phrasing (input value, output, mapping and so on) within the reader's level and prevents oversimplification that underestimates the reader (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Added a self-contained writing rule that states the needed content in place when referring to other sections, sources, data and so on, without replacing content with codes, numbers, abbreviations or summary labels (#79)
- Added a rule that each implication sentence states the key facts of its supporting evidence, with fact IDs kept as tracing tags (#79)

* 독자 수준에 맞춘 어휘 규칙 추가 (전문용어와 소프트웨어 설계 어투의 남발 및 독자를 과소평가한 과잉 평이화 방지) (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 자기완결 서술 규칙 추가 (다른 절, 문헌, 데이터 등의 언급 시 필요한 내용의 직접 기재 및 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지) (#79)
* 시사점 문장의 근거 팩트 핵심 사실 기재 규칙 추가 (팩트 번호는 추적용 표지로 병기) (#79)

### environment-analysis-lite
- Added a vocabulary-level rule that keeps jargon and software-design phrasing (input value, output, mapping and so on) within the reader's level and prevents oversimplification that underestimates the reader (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Added a self-contained writing rule that states the needed content in place when referring to other sections, sources, data and so on, without replacing content with codes, numbers, abbreviations or summary labels (#79)
- Added a rule that each implication sentence states the key facts of its supporting evidence, with fact IDs kept as tracing tags (#79)

* 독자 수준에 맞춘 어휘 규칙 추가 (전문용어와 소프트웨어 설계 어투의 남발 및 독자를 과소평가한 과잉 평이화 방지) (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 자기완결 서술 규칙 추가 (다른 절, 문헌, 데이터 등의 언급 시 필요한 내용의 직접 기재 및 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지) (#79)
* 시사점 문장의 근거 팩트 핵심 사실 기재 규칙 추가 (팩트 번호는 추적용 표지로 병기) (#79)

### lean-work
- Added a vocabulary-level rule that keeps jargon and software-design phrasing (input value, output, mapping and so on) within the reader's level and prevents oversimplification that underestimates the reader (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Added a self-contained writing rule that states the needed content in place when referring to other documents, pages, sections, data and so on, without replacing content with codes, numbers, abbreviations or summary labels (#79)

* 독자 수준에 맞춘 어휘 규칙 추가 (전문용어와 소프트웨어 설계 어투의 남발 및 독자를 과소평가한 과잉 평이화 방지) (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 자기완결 서술 규칙 추가 (다른 문서, 쪽, 절, 데이터 등의 언급 시 필요한 내용의 직접 기재 및 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지) (#79)

### logical-write
- Added software-design phrasing (input value, output, mapping and so on) to the wording that may not stand in for formality (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Changed the scope of the rule that states cited content in place from sources to other pages, sections, slides, data and so on (#79)
- Added a rule against replacing content with codes, numbers, abbreviations or summary labels (#79)
- Changed the grammar error lists into examples that end with "and so on" (#79)

* 격식을 대신하지 않는 어휘에 소프트웨어 설계 어투(입력값, 출력, 매핑 등) 추가 (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 인용 내용 직접 기재 규칙의 적용 범위를 문헌에서 다른 쪽, 절, 슬라이드, 데이터 등으로 확대 변경 (#79)
* 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지 규칙 추가 (#79)
* 비문 유형 목록을 '등'으로 끝나는 예시 목록으로 변경 (#79)

### logical-write-lite
- Added software-design phrasing (input value, output, mapping and so on) to the wording that may not stand in for formality (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Changed the scope of the rule that states cited content in place from sources to other pages, sections, slides, data and so on (#79)
- Added a rule against replacing content with codes, numbers, abbreviations or summary labels (#79)
- Changed the grammar error lists into examples that end with "and so on" (#79)

* 격식을 대신하지 않는 어휘에 소프트웨어 설계 어투(입력값, 출력, 매핑 등) 추가 (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 인용 내용 직접 기재 규칙의 적용 범위를 문헌에서 다른 쪽, 절, 슬라이드, 데이터 등으로 확대 변경 (#79)
* 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지 규칙 추가 (#79)
* 비문 유형 목록을 '등'으로 끝나는 예시 목록으로 변경 (#79)

### network-analysis
- Added a vocabulary-level rule that keeps jargon and software-design phrasing (input value, output, mapping and so on) within the reader's level and prevents oversimplification that underestimates the reader (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Added a self-contained writing rule that states the needed content in place when referring to other sections, figures, tables, sources and so on, and names nodes and groups along with any number or code (#79)

* 독자 수준에 맞춘 어휘 규칙 추가 (전문용어와 소프트웨어 설계 어투의 남발 및 독자를 과소평가한 과잉 평이화 방지) (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 자기완결 서술 규칙 추가 (다른 절, 그림, 표, 문헌 등의 언급 시 필요한 내용의 직접 기재 및 노드와 집단의 이름 병기) (#79)

### no-jargon
- Added software-design phrasing used outside its field (input value, output, mapping and so on) to the jargon criteria (#79)

* 분야 밖에서 사용한 소프트웨어 설계 어투(입력값, 출력, 매핑 등)의 전문용어 판별 기준 추가 (#79)

### pref-architect
- Added a vocabulary-level rule that keeps jargon and software-design phrasing (input value, output, mapping and so on) within the reader's level and prevents oversimplification that underestimates the reader (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Changed the scope of the rule that states cited content in place from sources to other pages, slides, data and so on (#79)
- Added a rule against replacing content with codes, numbers, abbreviations or summary labels (#79)

* 독자 수준에 맞춘 어휘 규칙 추가 (전문용어와 소프트웨어 설계 어투의 남발 및 독자를 과소평가한 과잉 평이화 방지) (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 인용 내용 직접 기재 규칙의 적용 범위를 문헌에서 다른 쪽, 슬라이드, 데이터 등으로 확대 변경 (#79)
* 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지 규칙 추가 (#79)

### project-plan
- Added a vocabulary-level rule that keeps jargon and software-design phrasing (input value, output, mapping and so on) within the reader's level and prevents oversimplification that underestimates the reader (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Added a self-contained writing rule that states the needed content in place when referring to WBS tasks, other sections, sources and so on in the overview, without replacing content with codes, numbers, abbreviations or summary labels (#79)

* 독자 수준에 맞춘 어휘 규칙 추가 (전문용어와 소프트웨어 설계 어투의 남발 및 독자를 과소평가한 과잉 평이화 방지) (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 자기완결 서술 규칙 추가 (오버뷰의 WBS 작업, 다른 절, 문헌 등의 언급 시 필요한 내용의 직접 기재 및 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지) (#79)

### rfp-strategy
- Added a vocabulary-level rule that keeps jargon and software-design phrasing (input value, output, mapping and so on) within the reader's level and prevents oversimplification that underestimates the reader (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Added a self-contained writing rule that states the needed content in place when referring to RFP clauses, other sections, sources, data and so on, without replacing content with codes, numbers, abbreviations or summary labels (#79)

* 독자 수준에 맞춘 어휘 규칙 추가 (전문용어와 소프트웨어 설계 어투의 남발 및 독자를 과소평가한 과잉 평이화 방지) (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 자기완결 서술 규칙 추가 (RFP 조항, 다른 절, 문헌, 데이터 등의 언급 시 필요한 내용의 직접 기재 및 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지) (#79)

### slop-proof
- Added software-design phrasing outside system design explanations (input value, output, interface, pipeline and so on) to the non-preferred words (#79)

* 시스템 설계 설명 밖의 소프트웨어 설계 어투(입력값, 출력, 인터페이스, 파이프라인 등) 비선호 어휘 추가 (#79)

### strategy-builder
- Added a vocabulary-level rule that keeps jargon and software-design phrasing (input value, output, mapping and so on) within the reader's level and prevents oversimplification that underestimates the reader (#79)
- Added a rule that states specialized and technical content accurately, plainly and clearly (#79)
- Added a grammar rule that applies regardless of technicality or plainness (#79)
- Added a self-contained writing rule that states the needed content in place when referring to other elements or steps in the body, without replacing content with codes, numbers, abbreviations or summary labels (#79)

* 독자 수준에 맞춘 어휘 규칙 추가 (전문용어와 소프트웨어 설계 어투의 남발 및 독자를 과소평가한 과잉 평이화 방지) (#79)
* 전문적, 기술적 내용의 정확하고 쉽고 명료한 서술 규칙 추가 (#79)
* 글의 전문성 및 평이함 정도와 무관한 문법 준수 규칙 추가 (#79)
* 자기완결 서술 규칙 추가 (본문의 다른 요소나 단계 언급 시 필요한 내용의 직접 기재 및 코드, 번호, 약칭, 요약 문구 등으로의 내용 치환 금지) (#79)
## 2026-11-07

### biz-code-style
- Added a rule that sources cite only external material the reader can look up (#76)

* 출처 대상을 독자가 찾아볼 수 있는 외부 자료로 한정하는 규칙 추가 (#76)

### biz-code-style-lite
- Added a rule that sources cite only external material the reader can look up (#76)

* 출처 대상을 독자가 찾아볼 수 있는 외부 자료로 한정하는 규칙 추가 (#76)

### digest
- Changed the scope of `>` source blocks from every figure to each input of a report (#77)
- Added a rule that keeps labels that fail to identify the original out of the body and sources: conversion file names, "the input", "the transcript", and internal reasoning (#77, #78)
- Added a rule against repeating as a source the original's details already given in an overview (#77, #78)
- Added a write-up rule that writes external material the input names as its basis in the same sentence as the content it supports (#77)
- Added a rule that cites the original material by its bibliographic details, including text written from a conversion (#78)

* `>` 출처 블록의 적용 범위를 모든 수치에서 보고서의 입력 자료별 출처로 변경 (#77)
* 원본을 특정하지 못하는 표기의 본문 및 출처 미기재 규칙 추가 (변환본 파일명, "입력 자료", "녹취록", 내부 추론) (#77, #78)
* 개요에 기재한 원본 정보의 출처 중복 기재 방지 규칙 추가 (#77, #78)
* 입력 자료에 명시된 외부 근거 자료의 동일 문장 기재 규칙 추가 (#77)
* 원본 자료 서지 정보 기준의 출처 표기 규칙 추가 (변환본을 읽고 작성한 글 포함) (#78)

### environment-analysis
- Added an internal source disclosure item to scoping: the full document name, "[기관명] 내부 자료", or no source in the body, chosen by disclosure scope, internal security, and personal-information sensitivity (#76)
- Added a rule that names each source by the material itself and never by the user's request, the drafting process, or labels such as "사용자 제출 자료" (#76)

* 범위 설정의 내부 자료 출처 표기 수준 항목(문서명 전체, "[기관명] 내부 자료", 본문 출처 생략) 추가 (#76)
* 자료를 특정하는 출처 이름 규칙 추가 (사용자 요청, 작성 과정, "사용자 제출 자료" 표기 제외) (#76)

### environment-analysis-lite
- Added a step that confirms the disclosure level of internal sources with the user before internal material is used: the source format, "[기관명] 내부 자료", or no source line (#76)
- Added a rule that names each source by the material itself and never by the user's request, the drafting process, or labels such as "사용자 제출 자료" (#76)
- Changed figures the user states in the conversation to be recorded as "사용자 제시" in the evidence register only, outside the deliverable's source blocks (#76)
- Fixed the English submitted-file source format to name the title of the material instead of the file name (#76)

* 내부 자료 사용 전 출처 표기 수준(출처 형식, "[기관명] 내부 자료", 출처 생략)의 사용자 확인 절차 추가 (#76)
* 자료를 특정하는 출처 이름 규칙 추가 (사용자 요청, 작성 과정, "사용자 제출 자료" 표기 제외) (#76)
* 대화 중 사용자 제시 수치의 "사용자 제시" 기록 위치를 근거 대장으로 변경 (#76)
* 영문판 제출 자료 출처 형식의 표기 대상을 파일명에서 자료 제목으로 수정 (#76)

### logical-write
- Added a rule that sources and notes cite only external material the reader can look up (#76)

* 출처와 주석의 출처 대상을 독자가 찾아볼 수 있는 외부 자료로 한정하는 규칙 추가 (#76)

### logical-write-lite
- Added a rule that sources and notes cite only external material the reader can look up (#76)

* 출처와 주석의 출처 대상을 독자가 찾아볼 수 있는 외부 자료로 한정하는 규칙 추가 (#76)

### pref-architect
- Added a rule to the writing standard module that sources and notes cite only external material the reader can look up (#76)

* 글쓰기 기준 모듈에 출처와 주석의 출처 대상을 독자가 찾아볼 수 있는 외부 자료로 한정하는 규칙 추가 (#76)

## 2026-11-06

### biz-code-style
- Added new entries to the vocabulary lists: 가치 (preferred); 갈래, 묶음, 판, 통독 (non-preferred); 판정, 약속, 출발, the -측 words (cautionary) (#69, #71)
- Added informal style and a colloquial or informal tone in endings, words, and expressions to the colloquial style rule (#69)
- Changed the plain-wording rule to describe the writing behavior without a group label (#73)
- Changed the usage condition for 약속 to content the user can actually deliver (#75)

* 어휘 목록의 신규 어휘(가치, 갈래, 묶음, 판, 통독, 판정, 약속, 출발, '-측' 어휘) 추가 (#69, #71)
* 구어체 규칙의 대상에 비격식체, 구어적 어감, 비격식적 어감 추가 (#69)
* 쉬운 표현 규칙의 문구를 집단 명칭 없이 작성 방식을 서술하는 문장으로 변경 (#73)
* 약속의 사용 조건을 사용자가 실제로 이행할 수 있는 내용으로 변경 (#75)

### biz-code-style-lite
- Added new entries to the vocabulary lists: 묶음, 판 (non-preferred); 판정, 약속, 출발, 계측, 실측 (cautionary) (#69)
- Added a writing rule against a colloquial or informal tone in endings, words, and expressions (#69)
- Changed the placeholder noun rule to cover all placeholder nouns such as 것, 곳, 거, 셈, and 부분 in any position (#69)

* 어휘 목록의 신규 어휘(묶음, 판, 판정, 약속, 출발, 계측, 실측) 추가 (#69)
* 종결, 어휘, 표현의 구어적 어감 및 비격식적 어감 미사용 규칙 추가 (#69)
* 빈자리 명사 규칙의 적용 범위를 문장 전체의 빈자리 명사(것, 곳, 거, 셈, 부분 등)로 변경 (#69)

### digest
- Changed the register rule from informal endings and colloquial words to a colloquial or informal tone across endings, words, and expressions (#69)

* 비격식 표현 규칙의 적용 범위를 종결 및 어휘에서 표현 전반으로 변경 (#69)

### environment-analysis
- Added a writing rule against a colloquial or informal tone in endings, words, and expressions (#69)
- Changed the placeholder noun rule to cover all placeholder nouns such as 것, 곳, 거, 셈, and 부분 in any position (#69)

* 종결, 어휘, 표현의 구어적 어감 및 비격식적 어감 미사용 규칙 추가 (#69)
* 빈자리 명사 규칙의 적용 범위를 문장 전체의 빈자리 명사(것, 곳, 거, 셈, 부분 등)로 변경 (#69)

### environment-analysis-lite
- Added a writing rule against a colloquial or informal tone in endings, words, and expressions (#69)
- Added a writing rule against placeholder nouns such as 것, 곳, 거, 셈, and 부분 (#69)

* 종결, 어휘, 표현의 구어적 어감 및 비격식적 어감 미사용 규칙 추가 (#69)
* 빈자리 명사(것, 곳, 거, 셈, 부분 등) 미사용 규칙 추가 (#69)

### logical-write
- Added new entries to the vocabulary lists: 가치 (preferred); 정립, 묶음, 판 (non-preferred); 판정, 약속, 출발, the -측 words (cautionary) (#69, #71)
- Added informal style and a colloquial or informal tone in endings, words, and expressions to the colloquial style rule (#69)
- Changed the usage condition for 약속 to content the user can actually deliver (#75)

* 어휘 목록의 신규 어휘(가치, 정립, 묶음, 판, 판정, 약속, 출발, '-측' 어휘) 추가 (#69, #71)
* 구어체 규칙의 대상에 비격식체, 구어적 어감, 비격식적 어감 추가 (#69)
* 약속의 사용 조건을 사용자가 실제로 이행할 수 있는 내용으로 변경 (#75)

### logical-write-lite
- Added new entries to the vocabulary lists: 가치 (preferred); 묶음, 판 (non-preferred); 판정, 약속, 출발, 계측 (cautionary) (#69)
- Added informal style and a colloquial or informal tone in endings, words, and expressions to the colloquial style rule (#69)

* 어휘 목록의 신규 어휘(가치, 묶음, 판, 판정, 약속, 출발, 계측) 추가 (#69)
* 구어체 규칙의 대상에 비격식체, 구어적 어감, 비격식적 어감 추가 (#69)

### network-analysis
- Added a writing rule against a colloquial or informal tone in endings, words, and expressions (#69)
- Added a writing rule against placeholder nouns such as 것, 곳, 거, 셈, and 부분 (#69)

* 종결, 어휘, 표현의 구어적 어감 및 비격식적 어감 미사용 규칙 추가 (#69)
* 빈자리 명사(것, 곳, 거, 셈, 부분 등) 미사용 규칙 추가 (#69)

### pref-architect
- Added new entries to the vocabulary lists: 가치 (preferred); 묶음, 판 (non-preferred); 판정, 출발, the -측 words, 약속 (cautionary) (#69)
- Added informal style and a colloquial or informal tone in endings, words, and expressions to the colloquial style rule (#69)
- Changed the placeholder noun rule to cover all placeholder nouns such as 것, 곳, 거, 셈, and 부분 in any position (#69)
- Changed the plain-wording rule to describe the writing behavior without a group label (#73)

* 어휘 목록의 신규 어휘(가치, 묶음, 판, 판정, 출발, '-측' 어휘, 약속) 추가 (#69)
* 구어체 규칙의 대상에 비격식체, 구어적 어감, 비격식적 어감 추가 (#69)
* 빈자리 명사 규칙의 적용 범위를 문장 전체의 빈자리 명사(것, 곳, 거, 셈, 부분 등)로 변경 (#69)
* 쉬운 표현 규칙의 문구를 집단 명칭 없이 작성 방식을 서술하는 문장으로 변경 (#73)

### project-plan
- Added a writing rule against a colloquial or informal tone in endings, words, and expressions (#69)
- Added a writing rule against placeholder nouns such as 것, 곳, 거, 셈, and 부분 (#69)

* 종결, 어휘, 표현의 구어적 어감 및 비격식적 어감 미사용 규칙 추가 (#69)
* 빈자리 명사(것, 곳, 거, 셈, 부분 등) 미사용 규칙 추가 (#69)

### rfp-strategy
- Added a writing rule against a colloquial or informal tone in endings, words, and expressions (#69)
- Added a writing rule against placeholder nouns such as 것, 곳, 거, 셈, and 부분 (#69)

* 종결, 어휘, 표현의 구어적 어감 및 비격식적 어감 미사용 규칙 추가 (#69)
* 빈자리 명사(것, 곳, 거, 셈, 부분 등) 미사용 규칙 추가 (#69)

### slop-proof
- Added new entries to the vocabulary lists: 가치 (preferred); 묶음, 판 (non-preferred); 판정, 약속, 출발, the -측 words (cautionary) (#69, #71)
- Changed the usage condition for 약속 to content the user can actually deliver (#75)

* 어휘 목록의 신규 어휘(가치, 묶음, 판, 판정, 약속, 출발, '-측' 어휘) 추가 (#69, #71)
* 약속의 사용 조건을 사용자가 실제로 이행할 수 있는 내용으로 변경 (#75)

### strategy-builder
- Changed the viewpoint in the writing rules to an expert with extensive experience in management, economics, and public administration (#68)
- Added a writing rule against a colloquial or informal tone in endings, words, and expressions (#69)
- Added a writing rule against placeholder nouns such as 것, 곳, 거, 셈, and 부분 (#69)

* 작성 원칙의 판단 관점을 경영학, 경제학, 행정학 분야의 경험이 풍부한 전문가로 변경 (#68)
* 종결, 어휘, 표현의 구어적 어감 및 비격식적 어감 미사용 규칙 추가 (#69)
* 빈자리 명사(것, 곳, 거, 셈, 부분 등) 미사용 규칙 추가 (#69)

### think-review
- Added informal style to the colloquial style rule for rewrite suggestions (#69)

* 수정 제안 문체 규칙의 대상에 비격식체 추가 (#69)

## 2026-11-05

### digest
- Changed the evidence lines of meeting minutes to omit the level-2 label by default (#60)
- Added examples of evidence that needs a level-2 label in meeting minutes, such as several categories or a complex concept (#60)
- Changed the next-step lines of meeting minutes from a comma list to one sentence that states the follow-up action (#61)
- Added example next-step sentences with the deadline, the deliverable's recipient, and the deliverable (#61)
- Added a writing style rule and a matching pre-delivery check item for classifying headings, labels, and bullets by one criterion without overlap or omission (#63, #64)
- Added a label usage rule that labels every item in a group divided by one criterion and labels other items only when the label adds information the heading and the sentence lack (#65)
- Added a writing style rule and a matching pre-delivery check item for labels that repeat their heading, their sentence, or the content of another label (#65)
- Added a formal written register rule that bans informal endings, colloquial words, and placeholder nouns (#65)
- Changed the end of every example list to an open-ended marker ("등" in Korean, "and so on" in English) (#65)
- Changed speaker-grouped meeting minutes to name each speaker once in a `##` header, with topic and keyword labels for the claims under it (#66)
- Added optional breakdown headers to meeting minutes, with `##` headers for topic and time grouping and `###` headers under each speaker header for speaker grouping (#66, #67)
- Added a meeting minutes rule and a matching pre-delivery check item against duplicating header information in the labels and sentences below (#66)

* 회의록 근거 줄의 기본 형식을 2단계 소제목 생략 형식으로 변경 (#60)
* 회의록 2단계 소제목이 필요한 근거의 예시(여러 개의 카테고리, 복잡한 개념) 추가 (#60)
* 회의록 향후 계획 줄의 형식을 쉼표 나열에서 후속 조치 서술 문장으로 변경 (#61)
* 회의록 향후 계획의 예시 문장(기한, 결과물 수령자, 결과물 포함) 추가 (#61)
* 헤더, 소제목, 불릿을 한 가지 기준으로 중복 및 누락 없이 분류하기 위한 작성 문체 규칙 및 산출 전 점검 항목 추가 (#63, #64)
* 소제목 사용 규칙(한 가지 기준으로 나뉜 항목 묶음은 전체 부착, 그 밖의 항목은 헤더와 문장에 없는 정보가 있을 때만 부착) 추가 (#65)
* 헤더, 문장, 다른 소제목과 내용이 겹치는 소제목을 정리하기 위한 작성 문체 규칙 및 산출 전 점검 항목 추가 (#65)
* 격식 문어체 작성 규칙(비격식 종결, 구어체 어휘, 빈자리 명사 미사용) 추가 (#65)
* 예시 목록의 끝 표기를 열린 목록 표기(한국어 "등", 영어 "and so on")로 변경 (#65)
* 발언자 기준 회의록의 발언자 이름 표기를 1단계 소제목 반복에서 발언자별 `##` 헤더 1회 표기(하위 소제목은 주제 및 키워드)로 변경 (#66)
* 회의록 세분화용 헤더의 선택 사용 방식(주제 기준 및 시간 기준은 `##` 헤더, 발언자 기준은 발언자 헤더 아래 `###` 헤더) 추가 (#66, #67)
* 하위 소제목 및 문장의 헤더 정보 중복을 막기 위한 회의록 규칙 및 산출 전 점검 항목 추가 (#66)

## 2026-11-04

### digest
- Added a `--probe` option that measures transcription speed on the machine and estimates the expected time per Whisper model (#54)
- Changed the transcription model choice from tiny by default to the model the user selects after seeing the expected time per model (#54)
- Added peak memory and a relative recognition accuracy grade to the Whisper model table (#54)
- Fixed audio decoding without ffmpeg by adding the PyAV version condition av<19 to the installation (#55)
- Added an explanation of the transcription model to the model choice guidance for users meeting it for the first time (#57)
- Changed the model recommendation to the fastest model that meets the accuracy the output needs and the recording conditions confirmed by the user (#57)

* 기기의 전사 속도 측정 결과로 Whisper 모델별 예상 시간을 계산하는 `--probe` 옵션 추가 (#54)
* 전사 모델 결정 방식을 tiny 기본 사용에서 모델별 예상 시간 안내 후 사용자 선택으로 변경 (#54)
* Whisper 모델 표에 최대 메모리 및 인식 정확도 상대 등급 추가 (#54)
* PyAV 버전 조건(av<19) 추가로 ffmpeg 미설치 환경의 음성 디코딩 실패 수정 (#55)
* 전사 모델 선택 안내에 처음 접하는 사용자를 위한 전사 모델 설명 추가 (#57)
* 전사 모델 추천 기준을 결과물에 필요한 정확도와 사용자가 확인한 녹음 상태를 충족하는 최단 시간 모델로 변경 (#57)

## 2026-11-02

### rfp-strategy
- Changed the competitor candidate search criteria (#52)

* 경쟁 후보 탐색 기준 변경 (#52)

## 2026-10-31

### digest
- Added steps that explain how to get captions for a video page address when the user asks, with official and lawful routes first (#46, #47)
- Added a step that carries out the caption method in the current environment after the user agrees (#47)
- Added a step that continues the workflow from step 2 with the .srt or .vtt captions obtained (#47)
- Changed the first section of meeting minutes into a meeting overview with the meeting name, purpose, date and time, and attendees (#48, #49)
- Added a default date and time format for meeting minutes, YYYY-MM-DD HH:MM-HH:MM, that follows the user's regional convention when it differs (#48)
- Added a question before writing meeting minutes that asks once for the unconfirmed meeting name, date and time, attendees, and speaker names (#48)
- Changed the meeting purpose from three to five lines to one concise simple sentence written from the transcript (#49)
- Removed the bold markup from the claim lines and next steps lines of meeting minutes (#50)
- Changed the level-2 label of meeting minutes to be used in cases where the evidence needs structuring (#50, #51)

* 사용자 요청 시 영상 페이지 주소의 자막 확보 방법을 공식적이고 합법적인 경로 우선으로 안내하는 절차 추가 (#46, #47)
* 사용자 동의 후 실행 환경에서 자막 확보 방법을 실행하는 단계 추가 (#47)
* 확보한 .srt나 .vtt 자막으로 작업 순서 2번부터 이어가는 단계 추가 (#47)
* 회의록 첫 절을 회의명, 회의목적, 회의일시, 참석자로 구성된 회의 개요로 변경 (#48, #49)
* 사용자 지역 관례를 우선하는 회의일시 기본 형식(YYYY-MM-DD HH:MM-HH:MM) 추가 (#48)
* 회의록 작성 전에 확인되지 않은 회의명, 회의일시, 참석자, 발언자 이름을 한 번에 묻는 단계 추가 (#48)
* 회의목적의 분량을 3-5줄에서 녹취록 기반의 1줄 단문으로 변경 (#49)
* 회의록 주장 줄 및 향후 계획 줄의 굵게 표시 삭제 (#50)
* 회의록 2단계 소제목의 사용 조건을 근거 구조화가 필요한 경우로 변경 (#50, #51)

## 2026-10-28

### biz-code-style
- Changed the 및 rule exception that keeps 와 or 과 from comparisons and partners to relations between two nouns, such as 연계 and 격차, and partners of an action (#44)
- Added the 및 rule to the Korean text rules of the English edition (#44)

* 및 규칙에서 '와', '과'를 유지하는 예외의 범위를 두 명사 사이의 관계(연계, 격차 등) 및 동작의 상대로 변경 (#44)
* 영어판의 한국어 텍스트 규칙에 및 규칙 추가 (#44)

### biz-code-style-lite
- Changed the 및 rule exception that keeps 와 or 과 from comparisons and partners to relations between two nouns, such as 연계 and 격차, and partners of an action (#44)

* 및 규칙에서 '와', '과'를 유지하는 예외의 범위를 두 명사 사이의 관계(연계, 격차 등) 및 동작의 상대로 변경 (#44)

### digest
- Changed the 및 rule exception that keeps 와 or 과 from comparisons and partners to relations between two nouns, such as 연계 and 격차, and partners of an action (#44)

* 및 규칙에서 '와', '과'를 유지하는 예외의 범위를 두 명사 사이의 관계(연계, 격차 등) 및 동작의 상대로 변경 (#44)

### environment-analysis
- Changed the 및 rule exception that keeps 와 or 과 from comparisons and partners to relations between two nouns, such as 연계 and 격차, and partners of an action (#44)

* 및 규칙에서 '와', '과'를 유지하는 예외의 범위를 두 명사 사이의 관계(연계, 격차 등) 및 동작의 상대로 변경 (#44)

### environment-analysis-lite
- Changed the 및 rule exception that keeps 와 or 과 from comparisons and partners to relations between two nouns, such as 연계 and 격차, and partners of an action (#44)

* 및 규칙에서 '와', '과'를 유지하는 예외의 범위를 두 명사 사이의 관계(연계, 격차 등) 및 동작의 상대로 변경 (#44)

### logical-write
- Changed the 및 rule exception that keeps 와 or 과 from comparisons and partners to relations between two nouns, such as 연계 and 격차, and partners of an action (#44)

* 및 규칙에서 '와', '과'를 유지하는 예외의 범위를 두 명사 사이의 관계(연계, 격차 등) 및 동작의 상대로 변경 (#44)

### logical-write-lite
- Changed the 및 rule exception that keeps 와 or 과 from comparisons and partners to relations between two nouns, such as 연계 and 격차, and partners of an action (#44)

* 및 규칙에서 '와', '과'를 유지하는 예외의 범위를 두 명사 사이의 관계(연계, 격차 등) 및 동작의 상대로 변경 (#44)

### network-analysis
- Changed the 및 rule exception that keeps 와 or 과 from comparisons and partners to relations between two nouns, such as 연계 and 격차, and partners of an action (#44)

* 및 규칙에서 '와', '과'를 유지하는 예외의 범위를 두 명사 사이의 관계(연계, 격차 등) 및 동작의 상대로 변경 (#44)

### pref-architect
- Changed the 및 rule exception that keeps 와 or 과 from comparisons and partners to relations between two nouns, such as 연계 and 격차, and partners of an action (#44)

* 및 규칙에서 '와', '과'를 유지하는 예외의 범위를 두 명사 사이의 관계(연계, 격차 등) 및 동작의 상대로 변경 (#44)

### project-plan
- Changed the 및 rule exception that keeps 와 or 과 from comparisons and partners to relations between two nouns, such as 연계 and 격차, and partners of an action (#44)

* 및 규칙에서 '와', '과'를 유지하는 예외의 범위를 두 명사 사이의 관계(연계, 격차 등) 및 동작의 상대로 변경 (#44)

### rfp-strategy
- Changed the 및 rule exception that keeps 와 or 과 from comparisons and partners to relations between two nouns, such as 연계 and 격차, and partners of an action (#44)

* 및 규칙에서 '와', '과'를 유지하는 예외의 범위를 두 명사 사이의 관계(연계, 격차 등) 및 동작의 상대로 변경 (#44)

### strategy-builder
- Changed the 및 rule exception that keeps 와 or 과 from comparisons and partners to relations between two nouns, such as 연계 and 격차, and partners of an action (#44)

* 및 규칙에서 '와', '과'를 유지하는 예외의 범위를 두 명사 사이의 관계(연계, 격차 등) 및 동작의 상대로 변경 (#44)

## 2026-10-27

### biz-code-style
- Added a rule for Korean text that joins two parallel nouns with 및 in place of 와 or 과, except in idiomatic names (#42, #43)

* 관용 명칭 외의 대등한 명사 2개를 '와', '과' 대신 '및'으로 잇는 규칙 추가 (#42, #43)

### biz-code-style-lite
- Added a rule for Korean text that joins two parallel nouns with 및 in place of 와 or 과, except in idiomatic names (#42, #43)

* 관용 명칭 외의 대등한 명사 2개를 '와', '과' 대신 '및'으로 잇는 규칙 추가 (#42, #43)

### digest
- Added a rule for Korean text that joins two parallel nouns with 및 in place of 와 or 과, except in idiomatic names (#42, #43)

* 관용 명칭 외의 대등한 명사 2개를 '와', '과' 대신 '및'으로 잇는 규칙 추가 (#42, #43)

### environment-analysis
- Added a rule for Korean text that joins two parallel nouns with 및 in place of 와 or 과, except in idiomatic names (#42, #43)

* 관용 명칭 외의 대등한 명사 2개를 '와', '과' 대신 '및'으로 잇는 규칙 추가 (#42, #43)

### environment-analysis-lite
- Added a rule for Korean text that joins two parallel nouns with 및 in place of 와 or 과, except in idiomatic names (#42, #43)

* 관용 명칭 외의 대등한 명사 2개를 '와', '과' 대신 '및'으로 잇는 규칙 추가 (#42, #43)

### logical-write
- Added a rule for Korean text that joins two parallel nouns with 및 in place of 와 or 과, except in idiomatic names (#42, #43)

* 관용 명칭 외의 대등한 명사 2개를 '와', '과' 대신 '및'으로 잇는 규칙 추가 (#42, #43)

### logical-write-lite
- Added a rule for Korean text that joins two parallel nouns with 및 in place of 와 or 과, except in idiomatic names (#42, #43)
- Removed the "A와 B" option for joining two items (#42)

* 관용 명칭 외의 대등한 명사 2개를 '와', '과' 대신 '및'으로 잇는 규칙 추가 (#42, #43)
* 2개 항목을 잇는 표현에서 "A와 B" 허용 삭제 (#42)

### network-analysis
- Added a rule for Korean text that joins two parallel nouns with 및 in place of 와 or 과, except in idiomatic names (#42, #43)

* 관용 명칭 외의 대등한 명사 2개를 '와', '과' 대신 '및'으로 잇는 규칙 추가 (#42, #43)

### pref-architect
- Added a rule for Korean text that joins two parallel nouns with 및 in place of 와 or 과, except in idiomatic names (#42, #43)

* 관용 명칭 외의 대등한 명사 2개를 '와', '과' 대신 '및'으로 잇는 규칙 추가 (#42, #43)

### project-plan
- Added a rule for Korean text that joins two parallel nouns with 및 in place of 와 or 과, except in idiomatic names (#42, #43)

* 관용 명칭 외의 대등한 명사 2개를 '와', '과' 대신 '및'으로 잇는 규칙 추가 (#42, #43)

### rfp-strategy
- Added a rule for Korean text that joins two parallel nouns with 및 in place of 와 or 과, except in idiomatic names (#42, #43)

* 관용 명칭 외의 대등한 명사 2개를 '와', '과' 대신 '및'으로 잇는 규칙 추가 (#42, #43)

### strategy-builder
- Added a rule for Korean text that joins two parallel nouns with 및 in place of 와 or 과, except in idiomatic names (#42, #43)

* 관용 명칭 외의 대등한 명사 2개를 '와', '과' 대신 '및'으로 잇는 규칙 추가 (#42, #43)

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
