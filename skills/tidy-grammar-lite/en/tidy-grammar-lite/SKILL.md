---
name: tidy-grammar-lite
description: "Polishing guidelines for grammar in Korean and English text. Checks agreement between sentence parts, particles, passives and causatives, honorifics, spelling, and spacing, and covers Korean itemized-style (gaejosik) endings, particle omission, and parallel items. For English, covers number agreement, countability and articles, tense and the subjunctive, and list grammar. Supports writing and correcting, and corrects only the grammar within the user's chosen style. When asked for strict mode, it checks each word against dictionaries and language norms. Use this skill when the user asks for '/tidy-grammar-lite', 'check the grammar', 'fix ungrammatical sentences', 'check spelling', 'itemized-style grammar', 'check nominal endings', 'check agreement', 'polish this text', 'grammar check', 'proofread', 'fix the grammar', or 'strict mode', or asks for a grammar check of a report, proposal, official document, or English report."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# tidy-grammar-lite

> Translation notice: This English edition was translated from the Korean original and may behave differently from what the original intends. The Korean edition holds the authoritative wording.

These guidelines correct grammar in Korean and English writing. They check whether sentence parts fit each other, whether word forms follow language norms, and whether items at the same level share the same grammatical form. No separate norm governs the endings and dropped particles of Korean itemized-style (gaejosik) items, so writers follow convention. The Korean itemized-style grammar section states that convention as explicit criteria.

## Terms

| Term | Meaning |
|---|---|
| Grammar error | A form that differs from language norms or dictionaries, or a combination of sentence parts whose meaning or form does not fit together |
| Sentence style | Sentences closed with finite endings such as '-다' or '-습니다' |
| Itemized style (gaejosik) | Items that state a point after a list marker and close with a nominal form or a noun |
| Item | A sentence or phrase introduced by one list marker |
| Level | All items at the same indentation depth |
| Norms | For Korean, Hangeul Orthography (한글 맞춤법), the Standard Language Rules (표준어 규정), and the Standard Korean Language Dictionary (표준국어대사전). For English, major English dictionaries and public style guides |

## How it works

- (Writing mode) Apply these guidelines from the start when writing new text. Put only the body content in the output.
- (Correction mode) Find and fix grammar errors in the given text. Present the correction summary first, then the corrected text.
- (Strict mode) When the user asks for strict mode or a norm check, add the checks in the Strict mode section to writing mode and correction mode.
- (Style neutrality) The choice between sentence style and itemized style, sentence length, and vocabulary follow the user's instructions and the document's conventions. These guidelines cover whether the grammar is correct within the chosen style.
- (Minimal change) Fix only forms that contain grammar errors, and keep vocabulary, word order, style, facts, and figures as in the original. The corrected text should still read as the original author's writing.
- (User choice first) Use any form the user specifies, even when it differs from the norms. In correction mode, list that location under "needs confirmation" in the correction summary.
- (Keep as is) Keep quotations, proper nouns, legal provisions, and code exactly as in the original.

## Detection tests

The rules in Korean sentence grammar, Korean itemized-style grammar, and English grammar collect common grammar errors. Apply the tests below to sentences that no rule covers.

| Test | Method | If the test fails |
|---|---|---|
| Restoration | Restore omitted particles, predicates, and subjects, and read whether the result is a complete sentence with the intended meaning | Restore any omission that readers cannot recover, or rebuild the sentence |
| Pairing | Pair the predicate with the subject, object, and adverbial one at a time and read each pair as a short sentence. For coordinated parts, attach the predicate to each part in turn | Change to a predicate that fits the pair, or give each part its own predicate |
| Parallelism | Check whether items at the same level, and parts joined by '와/과', '및', 'and', or 'or', share the same grammatical form | Align the rest to the form the original uses most |

- Use the restoration test on itemized items, English list items, and sentences with omitted subjects. Omission shortens text, but an omission that readers cannot recover erases meaning.
- Check word forms with the grammar rules in these guidelines and your knowledge of language norms. When you are unsure of the normative form, keep the original form and list it under "needs confirmation" in the correction summary. A form corrected by guesswork easily becomes a new error.
- Also list under "needs confirmation" any sentence whose fix depends on the author's intent, such as the scope of a modifier.

## How to revise

- Try revisions in this order: replace a particle or ending, supply a missing part, then split or reorder the sentence. Stop at the first step that resolves the error. Smaller revisions keep more of the original wording and rhythm.
- Place each revised sentence beside the original and confirm that facts, figures, strength of claims, and honorific level stay the same.

## Procedure

### Step 1. Identify the conditions of the text

Identify the language, the style (sentence style, itemized style, or mixed), the document type (report, official document, notice, English report, and so on), and any style instructions from the user. When there are no style instructions, take the style used in most of the original as the baseline.

### Step 2. Select the grammar rules

- If the text contains Korean sentences, apply Korean sentence grammar.
- If the text contains Korean itemized-style items, also apply Korean itemized-style grammar.
- If the text contains English sentences or English lists, apply English grammar.
- If the task converts itemized-style items into English lists or the reverse, apply Korean itemized-style grammar and English grammar together.

### Step 3. Check and revise

Check from larger units to smaller units. Rebuilding a sentence changes the word forms inside it, so the word-level check comes last.

- Apply the pairing test and the restoration test to each sentence.
- Apply the parallelism test to lists and coordinated parts.
- Check the spelling, spacing, inflected forms, English spelling, and plurals of each word.

### Step 4. Pre-output check

Go through the pre-output checklist below, fix any item that fails, then produce the output.

## Strict mode

Apply strict mode when the user asks for strict mode or a norm check. Strict mode adds the norm check test to the word-level check in step 3.

- (Norm check test) Compare spelling, spacing, inflected forms, English spelling, and plurals against the norms. Correct a form that differs from the norms to the normative form. When the norms allow two forms, use one form throughout the document.
- (Sources) If a search tool is available, check the Standard Korean Language Dictionary, Hangeul Orthography, or an English dictionary.
- (Scope of correction) Correct only forms whose norm you have confirmed. Leave unconfirmed forms as in the original and list them under "needs confirmation" in the correction summary.

## Korean sentence grammar

Korean grammar that applies to both sentence style and itemized style. The endings and particle omission specific to itemized style are covered in Korean itemized-style grammar.

### Agreement between sentence parts

#### Subject and predicate

When the subject is a noun that refers to content, such as '목적' (purpose), '목표' (goal), '이유' (reason), '원인' (cause), '특징' (feature), '문제' (problem), or '과제' (task), write the predicate in a form that takes that content: '-이다', '-하기 위함이다', or '-기 때문이다'. An action verb as the predicate makes the noun perform an action that a person performs.

| Original | Revision |
|---|---|
| 본 조사의 목적은 이용자 불편을 파악한다 | 본 조사의 목적은 이용자 불편 파악이다 |
| 일정 지연의 원인은 승인 절차가 중복되었다 | 일정 지연의 원인은 승인 절차 중복이다 |
| 이 제도의 특징은 신청 절차를 줄였다 | 이 제도의 특징은 신청 절차 축소이다 |

When the subject of the later clause differs from that of the earlier clause, state the later clause's subject. An omitted subject is read as the subject of the earlier clause.

| Original | Revision |
|---|---|
| 담당 부서는 초안을 작성한 뒤 위원회 심의를 거쳐 다음 달 확정된다 | 담당 부서가 작성한 초안은 위원회 심의를 거쳐 다음 달 확정된다 |

#### Object and predicate

When several objects are joined with '와/과' or '및', attach the predicate to each object in turn. If the predicate does not fit one of them, give that object its own fitting predicate.

| Original | Revision |
|---|---|
| 운영 비용과 처리 시간을 단축한다 | 운영 비용을 줄이고 처리 시간을 단축한다 |
| 주민 의견과 협조를 수렴한다 | 주민 의견을 수렴하고 협조를 구한다 |

#### Adverbial and predicate

The adverbs below pair with set predicate forms.

| Adverb | Paired predicate form | Original | Revision |
|---|---|---|---|
| 결코, 전혀 | Negative expression | 목표 달성이 결코 쉽다 | 목표 달성이 결코 쉽지 않다 |
| 비록 | '-지만', '-더라도', '-어도' | 비록 예산이 적어서 성과를 냈다 | 비록 예산이 적었지만 성과를 냈다 |
| 만약, 만일 | '-면', '-ㄴ다면', '-더라도' | 만약 신청자가 늘어나서 기간을 연장한다 | 만약 신청자가 늘어나면 기간을 연장한다 |
| 왜냐하면 | '-기 때문이다' | 왜냐하면 신청자가 늘었다 | 왜냐하면 신청자가 늘었기 때문이다 |

#### Time expressions and tense

Match tense to time adverbials. Use '-었-' for a past point, and the present form, '-ㄹ 예정이다', or '-겠-' for a future point.

| Original | Revision |
|---|---|
| 지난해 시범 사업을 실시한다 | 지난해 시범 사업을 실시했다 |
| 내년에 조사를 완료했다 | 내년에 조사를 완료할 예정이다 |

#### Scope of modification

When one modifier precedes nouns joined with '와/과', readers can take the modifier to describe only the first noun or both nouns. If it describes both, attach the modifier to each noun. If it describes only the first, move that noun to the end. If the original does not show the intent, list the sentence under "needs confirmation" in the correction summary.

| Original | When it modifies both nouns | When it modifies only the first noun |
|---|---|---|
| 새로운 정책과 제도를 검토한다 | 새로운 정책과 새로운 제도를 검토한다 | 제도와 새로운 정책을 검토한다 |

### Particles

| Particle | Use | Original | Revision |
|---|---|---|---|
| 에, 에게 | '에게' after people and animals, and '에' after institutions, organizations, places, and things | 정부에게 건의한다 | 정부에 건의한다 |
| 로서, 로써 | '로서' marks capacity or status, and '로써' marks means or instrument. After a nominal form that expresses means, use '-ㅁ으로써' | 신청 기준을 완화함으로서 참여가 늘었다 | 신청 기준을 완화함으로써 참여가 늘었다 |
| 와/과, 및, 또는 | Join parts of the same grammatical form (noun phrase with noun phrase, clause with clause) | 예산 확보와 인력을 충원한다 | 예산을 확보하고 인력을 충원한다 |

Sentence-style sentences keep their case particles. Dropping particles is a convention of itemized items and headings.

### Predicate forms

#### Passive

Mark the passive once. Adding '-어지다' to a passive verb (a verb with '-이-, -히-, -리-, -기-') or to '-되다' doubles the passive. A doubled passive adds no meaning, so keep only one.

| Original | Revision |
|---|---|
| 보여지다 | 보이다 |
| 잊혀지다 | 잊히다, 잊어지다 |
| 쓰여지다 | 쓰이다 |
| 믿겨지다 | 믿기다, 믿어지다 |
| 되어지다 | 되다 |
| 생각되어지다 | 생각되다 |

To decide, check whether the verb before '-어지다' is already a passive verb. If it is a causative verb (알리다, 밝히다), then '알려지다, 밝혀지다' mark the passive only once.

Write judgments and actions that the speaker or the sentence subject performs in the active voice.

| Original | Revision |
|---|---|
| 저희는 이 방안이 적절하다고 생각되어집니다 | 저희는 이 방안이 적절하다고 생각합니다 |

#### Causative

Use '-시키다' when the subject makes someone else perform an action. When the subject performs the action directly, use '-하다'.

| Original | Revision |
|---|---|
| 업무 절차를 개선시켰다 | 업무 절차를 개선했다 |
| 담당자를 소개시켜 드리겠습니다 | 담당자를 소개해 드리겠습니다 |

#### Honorifics

Use '-시-' when the person to be honored is the subject of the sentence. When a thing, system, product, or result is the subject, leave out '-시-'.

| Original | Revision |
|---|---|
| 신청 결과가 나오셨습니다 | 신청 결과가 나왔습니다 |
| 해당 상품은 품절이십니다 | 해당 상품은 품절입니다 |
| 원장님의 말씀이 계시겠습니다 | 원장님의 말씀이 있겠습니다 |

Within one text, keep one speech level for addressing the reader (합쇼체, 해요체, 해라체). If the body of a notice starts in 합쇼체, keep 합쇼체 to the end.

### Spelling

#### Nominalizing endings

'-ㅁ' attaches to stems without a final consonant, stems ending in 'ㄹ', the stem of '이다', and '-시-'. '-음' attaches to stems with a final consonant other than 'ㄹ' and to '-었-' and '-겠-'.

| Base form | Nominal form | Incorrect forms |
|---|---|---|
| 만들다 | 만듦 | 만듬, 만들음 |
| 알다 | 앎 | 암, 알음 |
| 줄다 | 줆 | 줄음 |
| 있다, 없다 | 있음, 없음 | 있슴, 없슴 |
| 하였다 | 하였음 | 하였슴 |

#### 률 and 율

Write '율' after a vowel or a final 'ㄴ', and '률' after any other final consonant (Hangeul Orthography, Article 11, Note 1). '렬' and '열' follow the same rule.

| Words written with '율' | Words written with '률' |
|---|---|
| 비율, 증가율, 감소율, 점유율, 백분율 | 경쟁률, 이용률, 합격률, 성장률, 달성률 |

#### 되 and 돼

'돼' is the contraction of '되어'. Read the spot with '되어' in its place: write '돼' if it sounds natural and '되' if it sounds awkward.

| Sentence | Reading with '되어' | Spelling |
|---|---|---|
| 검토가 아직 안 ( )다 | 안 되었다 (natural) | 안 됐다 |
| 검토가 ( )도록 조치한다 | 되어도록 (awkward) | 되도록 |
| 이 방식은 사용하면 안 ( ) | 안 되어 (natural) | 안 돼 |

#### Spacing

Write dependent nouns apart from the preceding word (Hangeul Orthography, Article 42). When the same form works as a particle or an ending, attach it.

| Form | Use | Spacing | Example |
|---|---|---|---|
| 데 | Place, matter, case | Separate | 자료를 찾는 데 사흘이 걸렸다 |
| 데 | Connective ending '-는데' | Attach | 자료를 찾는데 오류가 났다 |
| 지 | Elapsed time | Separate | 시행한 지 2년이 지났다 |
| 지 | Ending '-ㄴ지' | Attach | 효과가 있는지 확인한다 |
| 대로, 만큼, 뿐 | Dependent noun after a modifier | Separate | 계획한 대로, 예상한 만큼, 검토했을 뿐이다 |
| 대로, 만큼, 뿐 | Particle after a noun | Attach | 계획대로, 예상만큼, 서류뿐이다 |

- Write unit nouns apart, though they may attach after Arabic numerals (Article 43): 세 개, 3개.
- Auxiliary predicates are written apart in principle, and attaching them is also allowed (Article 47). Use one choice throughout the document.

## Korean itemized-style grammar

Itemized items shorten text by omitting particles and predicates. Readers restore omitted elements from word order and meaning, so meaning survives only when the omitted elements can be restored. This section covers the endings, the range of particle omission, and item composition for itemized items that close with a nominal form or a noun. Apply the agreement and spelling rules in Korean sentence grammar as well.

### Endings

Statement items in itemized style close with the nominal form of a predicate, '-(으)ㅁ', or with a predicative noun. Titles and item names are written as noun phrases and are not treated as sentences.

| Ending | Example | Restored as a sentence-style sentence |
|---|---|---|
| Nominal form of a predicate, '-(으)ㅁ' | 시범 운영을 완료함, 추가 검토가 필요함 | 시범 운영을 완료했다, 추가 검토가 필요하다 |
| Predicative noun | 시범 운영 완료, 추가 검토 필요, 다음 달 착수 예정 | 시범 운영을 완료했다, 추가 검토가 필요하다, 다음 달 착수할 예정이다 |
| Noun phrase (title, item name) | 추진 배경, 사업 개요 | Not a sentence, so no restoration |

- A predicative noun is a noun that becomes a predicate when followed by '-하다', '-되다', or '-이다' (추진, 완료, 필요, 부족, 증가, 예정, 계획, 전망).
- Statement items may mix '-(으)ㅁ' and predicative nouns. Both forms close a statement, so parallelism holds.
- End adjective predicates that have no predicative-noun form with '-(으)ㅁ' (수요가 많음, 비용이 높음).
- When converting an English list into itemized style, render statement items with the statement endings in the table above, and render titles and item names as noun phrases.

### Ending restoration test

Restore the end of the item into sentence style and check whether it yields a sentence with the intended meaning. To restore, add '-하다', '-되다', or '-이다' after the predicative noun or noun, or change '-(으)ㅁ' to '-다'. If this yields a sentence with the intended meaning, the item passes. If the intended meaning requires another predicate, such as '있다', '없다', '기대되다', or '우려되다', write that predicate in the item.

This test tells whether the final noun works as the predicate. A noun modified by a relative clause is often the head of a noun phrase whose predicate was omitted, so it often fails this test.

| Original | Restored sentence | Result | Revision |
|---|---|---|---|
| 목적 달성 필요 | 목적 달성이 필요하다 | Pass | No change |
| 목적을 달성할 필요 | 목적을 달성할 필요가 있다 | '있다' omitted | 목적 달성 필요, or 목적을 달성할 필요가 있음 |
| 다음 달 착수할 예정 | 다음 달 착수할 예정이다 | Pass | No change |
| 추가 비용이 발생할 가능성 | 추가 비용이 발생할 가능성이 있다 | '있다' omitted | 추가 비용 발생 가능성 있음 |
| 업무 처리 시간 단축 효과 | 업무 처리 시간 단축 효과가 기대된다 | '기대되다' omitted | 업무 처리 시간 단축 효과 기대 |
| 사업 기간은 2026년까지 | 사업 기간은 2026년까지이다 | Pass | No change |

### Range of particle omission

- Subject and object particles directly before a predicative noun may be dropped. '보고서를 제출' shortens to '보고서 제출', and '예산이 부족' to '예산 부족'.
- Keep adverbial particles ('에', '에서', '에게', '(으)로', '와/과', '보다', '부터', '까지'). Word order alone cannot restore relations of place, counterpart, means, or comparison.
- When an item contains both the agent and the target of an action, keep the agent's particle.
- When nouns run together without particles, each pair of neighboring nouns must read with one relation. If a pair reads with two or more relations, restore '의' or a case particle, or add a predicate.

| Original | Relations it can be read with | Revision |
|---|---|---|
| 협력 기관 자료 공유 | shared to the institution (에), shared with the institution (와), the institution's data shared (의) | 협력 기관에 자료 공유 |
| 지자체 주민 의견 수렴 | the local government collects opinions (가), the opinions of the local government's residents are collected (의) | 지자체가 주민 의견 수렴 |
| 학생 교사 평가 | students evaluate teachers (이), students and teachers are evaluated (와) | 학생의 교사 평가, or 학생과 교사 평가 |

### Agreement between voice and particles

After the object particle '을/를', use the active form ('-함' or an active predicative noun). When the subject particle '이/가' attaches to the target of the action, use the passive form ('-됨' or the nominal form of a passive verb). A predicative-noun ending does not mark active or passive, so if the target noun carries '이/가', end with '-됨'.

| Original | Revision |
|---|---|
| 자료를 제출됨 | 자료를 제출함, or 자료가 제출됨 |
| 계약이 체결함 | 계약을 체결함, or 계약이 체결됨 |
| 예산이 확보 | 예산 확보, or 예산이 확보됨 |

### Tense and aspect

- '-(으)ㅁ' marks tense when it follows '-었-' or '-겠-' (완료하였음, 협조하겠음).
- A predicative-noun ending does not mark tense. When the time changes the meaning, add a time expression (2026년, 상반기) or a noun that marks aspect (완료, 중, 예정).
- Items at the same level that describe the same time use the same way of marking tense.

| Original | Revision that states the time |
|---|---|
| 시범 운영 | 2025년 시범 운영 완료, 시범 운영 중, 2026년 시범 운영 예정 |

### Item composition

- Put one predicate in each item. The ending at the end of an item serves as the predicate of the whole item, so a second predicate stays in a connective form and tends to break the agreement between the ending and the particles. Split two facts into two items.
- Keep items at the same level in either sentence style or itemized style. Different endings make content at the same level read as different kinds of information.
- Judge parallelism within one level. Levels may differ in form, for example heading-style items at the upper level and statement items at the lower level.

| Original | Revision |
|---|---|
| 예산 확보하고 인력 충원 | 예산 확보 (first item), 인력 충원 (second item) |

## English grammar

Grammar for English sentences and English lists. When American and British English use different forms, choose one form for the document's audience and use it throughout.

### Agreement and reference

- (Subject-verb number) The verb agrees in number with the head noun of the subject. Nouns inside modifiers between the subject and the verb do not set the number.
- Subjects led by each, every, either, or neither take a singular verb. Use a plural verb after a number of and a singular verb after the number of.
- Data is standard with both plural and singular constructions. Use one construction throughout a document.
- (Reference words) What this, it, they, or which refers to must read as one thing. When two or more candidates exist, write the noun it refers to.
- (Dangling modifiers) An introductory participial or to-infinitive phrase modifies the subject of the main clause. When the doer of the phrase differs from that subject, make the doer the subject of the main clause. Dangling modifiers often appear when the main clause is in the passive voice.

| Original | Revision | Reason |
|---|---|---|
| The list of approved projects are attached. | The list of approved projects is attached. | Agreement with the head noun list |
| Each department submit a report. | Each department submits a report. | A subject led by each is singular |
| Costs rose after the vendor changed the schedule. This delayed the launch. | Costs rose after the vendor changed the schedule. The schedule change delayed the launch. | This could refer to two things |
| After reviewing the data, the plan was revised. | After reviewing the data, the team revised the plan. | The doer of reviewing becomes the subject |

### Nouns and determiners

- (Uncountable nouns) information, advice, equipment, research, feedback, evidence, progress, and knowledge take no plural and no a/an. To count them, use expressions such as a piece of, some, or much.
- (Singular countable nouns) In complete sentences, put a determiner such as a, an, the, this, or our before a singular countable noun. Omitting determiners is a convention of headings and labels.
- (Foreign plurals) Distinguish singular and plural in criterion and criteria, phenomenon and phenomena, analysis and analyses, and hypothesis and hypotheses. The plurals of appendix and index are both appendices and appendixes, and indices and indexes.

| Original | Revision | Reason |
|---|---|---|
| We received many feedbacks. | We received a lot of feedback. | Feedback is uncountable |
| The team conducted survey in May. | The team conducted a survey in May. | Determiner before a singular countable noun |
| The main criteria is cost. | The main criterion is cost. | A singular subject takes criterion |

### Verb forms

- (Present perfect and past) With expressions that point to a finished time (yesterday, last year, in 2020), use the simple past. Use the present perfect with expressions of a period that continues to now (this year, so far, since 2020).
- (Tense consistency) Within a paragraph, keep the tense unless the time being described changes.
- (Mandative subjunctive) In that-clauses after recommend, require, suggest, insist, or propose, and after essential, important, or necessary, use the base form of the verb regardless of the subject's person. For the negative, put not before the base form. British English often uses should plus the base form in the same position, so choose one form for the audience and use it throughout.
- (Conditions contrary to fact) For a condition contrary to present fact, use the past form in the if-clause and would, could, or might plus the base form in the main clause. In formal documents, write the be-verb in the if-clause as were for every person.

| Original | Revision | Reason |
|---|---|---|
| We have completed the pilot in 2024. | We completed the pilot in 2024. | Finished time: in 2024 |
| We recommend that the agency adopts the plan. | We recommend that the agency adopt the plan. | Base form in the that-clause after recommend |
| It is essential that the data is not shared. | It is essential that the data not be shared. | Negative: not plus the base form |
| If the budget was larger, we would hire two analysts. | If the budget were larger, we would hire two analysts. | Contrary-to-fact condition in a formal document |

### Sentence boundaries and lists

- (Comma splices) Join two independent clauses with a period, a semicolon, or a comma plus a coordinating conjunction (and, but, so). Two independent clauses joined by a comma alone form a sentence-boundary error.
- (Fragments) Sentences in prose need a subject and a finite verb. Fragments without a subject or a finite verb belong in headings, labels, and list items.
- (List parallelism) Give items in the same list the same grammatical form. Choose one: all noun phrases, all phrases that start with a base-form verb, or all complete sentences.
- (Lead-in and items) When items complete a fragment lead-in, each lead-in-plus-item combination must be grammatical. In documents that will be translated, write the lead-in as a complete sentence. Fragment lead-ins are hard to translate because word order differs across languages.
- (Capitals and periods) Capitalize the first letter of every item. End items that are complete sentences, or that complete the lead-in, with a period, and leave periods off other fragment items. Use periods consistently within a list. If usage is mixed, rewrite the items in parallel form.
- (Compound modifiers) Hyphenate a compound modifier that modifies a noun as a unit before the noun (long-term plan). Leave out the hyphen when the same words follow the noun in predicate position (the plan is long term) or when the compound starts with an -ly adverb (newly hired staff).

| Original | Revision | Reason |
|---|---|---|
| The pilot ended in March, the results are attached. | The pilot ended in March. The results are attached. | Independent clauses joined by a comma alone |
| Next steps: collect feedback, budget review, and we will update the plan. | Next steps: collect feedback, review the budget, and update the plan. | Parallel phrases that start with a base-form verb |
| a long term plan | a long-term plan | Compound modifier before a noun |

### Itemized style and English lists

When converting itemized items into an English list, or an English list into itemized items, choose the form by the item type.

| Itemized item type and ending | English list form | Example |
|---|---|---|
| Statement ('-(으)ㅁ', predicative noun) | Complete sentence, or a phrase that starts with a past-tense verb | The team completed the pilot in March. / Completed the pilot in March |
| Title, item name (noun phrase) | Noun phrase | Project background |

- Use one form from the table within a list.
- Write articles and prepositions in English items by the same rules as complete sentences. Carrying the particle omission of itemized style into English produces errors with missing articles and prepositions.

## Correction summary format

In correction mode, place the summary before the corrected text. When many revisions share a type, list up to two representative examples.

```
| Type | Original | Revision | Basis |
|---|---|---|---|
| Subject-predicate agreement | 본 조사의 목적은 이용자 불편을 파악한다 | 본 조사의 목적은 이용자 불편 파악이다 | Replaced the predicate with one that fits the subject '목적은' |
| Itemized ending | 추가 비용이 발생할 가능성 | 추가 비용 발생 가능성 있음 | Supplied the omitted predicate '있다' |

(Needs confirmation) Location, reason
```

When there are no grammar errors to fix, a single line "No grammar errors" replaces the summary.

## Pre-output checklist

- Does every predicate agree with its subject, object, and adverbials?
- When the omitted particles and predicates are restored, does each sentence carry the intended meaning?
- Do items at the same level and coordinated parts share the same grammatical form?
- Do word forms follow the grammar rules in these guidelines, with each allowed variant used consistently throughout the document?
- (Strict mode) Do spelling, spacing, and inflected forms match the norms?
- Do revised sentences keep the original facts, figures, strength of claims, and honorific level?
- Is the corrected text free of the guideline name and any description of the checking process?
