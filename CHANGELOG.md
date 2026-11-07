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

## 2026-11-07

### biz-code-style
- Added a rule that sources cite only external material the reader can look up (#76)

* 출처 대상을 독자가 찾아볼 수 있는 외부 자료로 한정하는 규칙 추가 (#76)

### biz-code-style-lite
- Added a rule that sources cite only external material the reader can look up (#76)

* 출처 대상을 독자가 찾아볼 수 있는 외부 자료로 한정하는 규칙 추가 (#76)

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
