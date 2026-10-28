# Sentence rules

> Translated from the Korean original. See the translation notice in SKILL.md.

## One message per sentence and 5W1H singularity

Put one message in one sentence. The test for this is 5W1H singularity. Within one sentence, who, when, where, what, why, and how each appear only once. When an element appears twice, the sentence is a compound sentence carrying two messages.

- Including why, what, and how in each sentence is recommended. Use each element once.
- Splitting a sentence must not drop the 5W1H information each new sentence needs.
- The reason to split a sentence is a repeated 5W1H element. Do not break sentences at random.
- The conjunction limits of strict mode and the comma and semicolon limits common to both modes exist to block the paths through which the same element enters one sentence twice.
- Do not write ungrammatical sentences with dropped particles or mismatched subjects and predicates.

Test procedure:

1. Find the 5W1H elements in the sentence.
2. Check whether any element appears twice or more.
3. If so, split the sentence at the element boundary.
4. Check again that each new sentence has why, what, and how.

```markdown
Wrong (two whats, two results)
- The company expanded its training budget and reorganized its evaluation system to improve the learning environment and raise results

Correct
- Company to expand the job training budget in stages to improve the learning environment
- Company to reorganize the training evaluation system to raise training results
```

```markdown
Wrong (two hows)
- The institute raised the share of self-directed projects and merged administrative forms to increase research focus

Correct
- Institute to raise the share of self-directed projects in stages to increase research focus
- Institute to merge repeatedly submitted administrative forms to reduce researchers' administrative load
```

## Common notation

These apply in both sentence modes.

| Target | Example | Handling |
|---|---|---|
| Joining commas | Commas that join clauses, insert phrases, or add asides | Split the sentence or rebuild it as a noun phrase |
| Listing commas | Lists of three or more items of the same category | Keep the commas (semiconductors, displays, secondary batteries). Write two items as "A and B". In Korean output, join two parallel nouns with 및 in place of 와 or 과 ("예산과 인력 확보" becomes "예산 및 인력 확보"). Keep 와 or 과 when it marks a relation between two nouns (사이, 간, 격차, 차이, 일치, 불일치, 연계, 연동, 정렬, 비교, 구분, 분리, 협력, as in "현행과 기준의 격차") or the partner of an action (as in "유관기관과 공유"), or when it belongs to an established term, such as "학습과 성장" in the BSC |
| `+` inside a sentence | "budget + staffing" | `+` is reserved for indenting child items. Inside a sentence, use "and" or rebuild the sentence |
| Periods | Periods mid-sentence or at the end of an item | Delete them. A mid-sentence period marks the place to split the item |
| Semicolons | Semicolons that join sentences | Delete and split the item |
| Separator symbols | /, \|, ·, →, ←, ↑, ↓, vs ("cost/benefit") | Delete or write out as a sentence |
| Joining hyphens | "cost-benefit", "short-mid term" | Write out as a sentence |
| Tildes | Tildes in ranges | Replace with a hyphen (-) |
| Excessive abbreviations | Unneeded English abbreviations, informal short forms | Spell them out |
| Unneeded loanwords and Sino-Korean words | Loanwords with a native equivalent | Use the native word |
| Honorific endings | Korean -합니다, -입니다, -하세요 | Replace with noun-form endings |

Do not simply delete a joining comma. Deleting the comma alone leaves the compound sentence in place. Split the sentence or rebuild it as a noun phrase. Keep the commas in lists of three or more. Nouns separated only by spaces blur the meaning.

```markdown
Wrong handling (comma deleted, compound sentence remains)
- The company expanded the budget and accordingly the training environment improved

Correct handling (split and noun-phrase rebuild)
- Company to expand the job training budget in stages
- Improvement of the training environment expected from the budget expansion
```

```markdown
Wrong handling (listing commas deleted)
- Comprehensive analysis of public industry research sector demand

Correct handling (listing commas kept)
- Comprehensive analysis of demand in the public, industry, and research sectors
```

## Strict mode

- Do not use conjunctions or clause-linking endings. Targets include 그리고 "and", 그러나 "but", 그래서 "so", 그렇기 때문에 "therefore", 이는 "this", -으며, -있으며, -이며, and -고 (all "and").
- When a conjunction seems necessary, split the sentence or rebuild it as a noun phrase.
- Do not join two facts in one sentence. Give each fact its own sentence and show the relation between sentences through item order and hierarchy.
- Carry a means or cause inside one sentence as a single 5W1H element, such as -하여 "by" or -으로 "due to". "예산을 단계적으로 확대하여 학습 환경 개선 추진" ("improvement of the learning environment by expanding the budget in stages") is a simple sentence holding one how and one what.

```markdown
Wrong
- The application process is complicated, so the dropout rate is high and consultation requests also increase

Correct
- Mid-process dropout rate up due to too many steps in the online application
- Waiting time at the consultation desk up due to more process inquiries
```

## Flow mode

### Allowed scope

Use subordinate clauses only to support the core message.

- (Cause) A clause that elaborates the cause or result of the core message
- (Condition) A clause that states the condition under which the core message holds
- (Specification) A clause that narrows the scope or gives an example of the core message
- (Means) A clause that explains how the core message is achieved

Do not attach a new, independent message as a subordinate clause. When two facts are simply parallel, write them as separate sentences or separate items.

### Linking expressions allowed

- (Cause) 이에 따라 "accordingly", 따라서 "therefore", 이를 통해 "through this", 이러한 한계를 극복하고자 "to overcome these limits", 이러한 변화에 대응하여 "in response to these changes"
- (Elaboration) 특히 "in particular", 더욱이 "moreover", 또한 "also", 동시에 "at the same time", 아울러 "in addition"
- (Contrast) 그러나 "however", 반면 "whereas", 한편 "meanwhile", 이와 달리 "unlike this"
- (Time) 최근 "recently", 향후 "going forward", 이후 "after", 이전 "before", 기존에는 "previously"
- (Reference) 이러한 "such", 이와 같은 "like this", 해당 "the relevant", 본 "this"
- (Linking endings) coordinate (-으며, -이며, -하며 "and"), concessive (-으나, -지만, -함에도 "although"), causal (-함으로써 "by doing", -함에 따라 "as", -기 때문에 "because"), conditional (-할 경우, -한다면, -할 때 "if" or "when")

### Limits

- Use a linking expression only when a real causal, elaborating, contrasting, temporal, or conditional relation exists. Do not insert one out of habit.
- Do not repeat the same linking expression.
- Do not stack linking endings such as -며, -고, -면서, -으나 in one sentence.
- Build flow from item order and causal logic more than from the number of linking expressions. When the flow is natural, a short ending without any linking expression is fine.
- Do not let a subordinate clause bring in a 5W1H element the core message already has. When the same element is needed twice, merge it into one causal chain or split the sentence.

```markdown
Wrong (two parallel causes)
- Budget constraints and staffing gaps delayed the launch

Correct (causes merged into one chain)
- The launch was delayed as budget constraints slowed hiring
```

```markdown
Wrong (two independent messages from different points in time)
- Without a policy, ad hoc use piled up in each department and resistance arose at standardization time

Correct (one core message, "organizational resistance", with the pile-up as a middle step)
- Ad hoc use that piled up in each department without a policy provoked organizational resistance to later standardization
```

```markdown
Correct (core message "timely decisions became difficult", preceding clause as causal support)
- As technology changes faster, timely decisions have become difficult under the existing linear management process
```

### Sentence skeleton and grammar

- Give one sentence one subject-predicate skeleton for the core message. Subordinate clauses support this skeleton.
- As clauses increase, keep each clause's scope clear so the core subject and predicate stay visible.
- Avoid dropped particles, broken subject-predicate agreement, and modifiers with unclear targets.
- Adjust the number of clauses and the sentence length so a reader reading aloud can follow the core subject and predicate in one breath.
- No rule tells you to shorten sentences. A sentence with several clauses is fine when its skeleton is clear.

```markdown
Wrong (chained clauses blur the subject and predicate)
- In the absence of a policy, while cases piled up in each department, with responsibility boundaries also forming informally, leading to a structure that makes later cleanup difficult

Correct
- Later cleanup grew harder as department-level cases piled up without a policy
```

### Patterns to avoid in flow mode

- (Chopping compulsion) Cutting every sentence to a few syllables and breaking the flow
- (Listing compulsion) Repeating simple lists with no relation between adjacent sentences
- (Connector avoidance compulsion) Deleting even the needed linking expressions and cutting causal links between sentences
- (Rambling sentences) Tying two or more independent messages together with subordinate clauses until the core message blurs
- (Colloquial drift) Using colloquial endings such as -합니다, -군요, -네요 in the name of flow

## Endings

- End every sentence with a noun form. Korean examples: -임, -함, -됨, -필요 "needed", -전망 "expected", -예정 "planned", -확인 "confirmed", -기대 "anticipated", -수행 "carried out".
- Do not use verb endings (-한다, -된다, -한다고 밝혔다 "stated that"). Turn "-한다고 밝혔다" into a noun form such as "-한다고 밝힌 바 확인" ("statement confirmed"). Keep the original wording when you quote or transcribe statutes or definitions.
- Do not use honorific endings (-합니다, -입니다, -하세요).
- When one item holds two or more independent points, split the item.
- Make noun-form endings read as natural Korean.

| Awkward | Natural |
|---|---|
| 목차명에는 키워드 기반 재구성으로 반영 ("reflected in table-of-contents names as keyword-based restructuring") | 목차명은 키워드 기반으로 재구성 ("table-of-contents names restructured by keyword") |
| 온전 세트 ("whole set", adjective ending dropped) | 온전한 세트 |

- Watch for awkward sentence endings on nouns such as 구조 "structure", 우선 "priority", 결론 "conclusion", 훌륭 "excellent", -것 "thing", -곳 "place", and nouns ending in the final consonant ㅅ.

### Leftover adnominal forms

In noun-ending style, adnominal forms such as -할, -을 할, -시킬 or the particle -의 sometimes remain and make the sentence awkward.

| Awkward form | Natural form | Problem |
|---|---|---|
| 목적 달성을 할 필요 | 목적 달성 필요 ("goal achievement needed") | "을 할" inserted |
| 목적을 달성할 필요 | 목적 달성 필요 | Adnominal form clashes with the noun ending |
| 선행할 필요, 후행할 필요 | 선행 필요, 후행 필요 ("precedence needed", "follow-up needed") | "할" left over |
| 접근할 필요, 정의할 필요 | 접근 필요, 정의 필요 ("access needed", "definition needed") | "할" left over |
| 내장시킬 필요 | 내장 필요 ("embedding needed") | "시킬" inserted |
| 접근할 시사 | 접근 가능 ("accessible") or a rebuilt sentence | "할" does not fit 시사 ("implication") |
| 작업의 부담 | 작업 부담 발생 ("workload arises") | "의" inserted. "작업 부담" alone is incomplete, so add a predicate noun such as 발생 "arises", 증가 "rises", or 우려 "concern" |

- (Test) When an adnominal form precedes a noun such as 필요, 시사, or 부담, and deleting the adnominal form keeps the meaning, revise it.
- (Handling) Delete the adnominal form and end on the noun phrase, or rebuild the particles.
- (Allowed) Keep the adnominal form when it restricts the target and deleting it changes the meaning. The gap between 검토할 사항 and 검토 사항 ("items to review" and "review items") is small, so revise it. Keep 삭제할 파일 ("files to delete") because the verb picks out the target.
- Handle "-할 것", an adnominal form followed by 것, under the empty-noun rules below.

### Sentences made only of nouns

Do not write sentences that only chain nouns. Keep the particles and predicates that show the relations.

| Wrong | Correct |
|---|---|
| 디지털 산업 집적 지표 ("digital industry agglomeration indicator") | 디지털 산업의 집적도 ("degree of agglomeration of the digital industry") |
| 연구 기술 자원 역량 상태 ("research technology resource capability status") | 연구 인프라 보유 여부 ("whether research infrastructure is in place") |

## Empty nouns

An empty noun wraps the referent in a noun that carries no information instead of naming it. The typical case is the Korean bound noun 것 ("thing"). The writer knows the referent but leaves it unnamed, and the reader must recover it from the surrounding sentences.

Blocking only 것 makes the same structure move to 곳 ("place"), 거 (colloquial "thing"), 셈 ("amount to"), or 부분 ("part"). So judge by the function of the structure, not by a word list. Many of these nouns also have normal grammatical uses, so judge by whether a specific noun or predicate noun can replace them, never by their mere presence.

### Scope

The list below is a starting point for detection and is open-ended. A noun outside the list gets the same treatment when it plays the same role.

| Referring function | Example nouns |
|---|---|
| Thing or matter | 것 "thing", 점 "point", 부분 "part", 사항 "item", 측면 "aspect" |
| Place | 곳 "place", 데 "place" |
| State or degree | 바 "what", 셈 "amount to", 편 "tend to", 터 "about to", 식 "manner" |

- Treat the colloquial contractions of 것 (거, 겄, 게 for 것이, 건 for 것은, 걸 for 것을) the same as 것.
- Colloquial contractions also damage the formal register, so fix them first in report style.

### Detection types

| Type | Before | After | Problem |
|---|---|---|---|
| Pseudo-cleft | "사업 지연을 초래한 것은 승인 절차의 중복" ("what delayed the project is the duplicated approval steps"), "개선이 시급한 곳은 승인 단계" ("the place urgently needing improvement is the approval stage") | "승인 절차 중복으로 사업 지연 발생" ("project delay from duplicated approval steps"), "승인 단계 개선 시급" ("approval stage needs urgent improvement") | Leaves the subject slot empty and pushes the information to the end |
| Nominalizing detour | "데이터를 정비하는 것이 필요" ("doing the data cleanup is needed"), "고객 이탈을 줄이는 것을 목표로 설정" ("set reducing churn as the goal") | "데이터 정비 필요" ("data cleanup needed"), "고객 이탈률 감소를 목표로 설정" ("churn-rate reduction set as the goal") | Uses "-하는 것" although a Sino-Korean noun or a -기/-음 form exists |
| Vague reference | "현장에서 원하는 것을 반영" ("reflect what the field wants"), "이런 것들을 고려하면" ("considering these things"), "문제가 되는 부분을 개선" ("improve the problematic part") | "현장에서 요청한 야간 교대 알림 기능을 반영" ("reflect the night-shift alert feature the field requested"), "인력 부족과 예산 제약을 고려하면" ("considering staff shortage and budget limits"), "중복 입력 항목을 개선" ("improve the duplicated input fields") | Compresses the referent into an empty noun and drops information |
| Empty-noun ending | "현장 인력의 활용도가 낮은 것" ("the thing that field staff utilization is low"), "보완이 필요한 곳" ("the place needing improvement"), "추가 검토할 거" ("the thing to review further"), "입력 절차가 중복되는 부분" ("the part where input steps overlap") | "현장 인력 활용도 저조" ("field staff utilization low"), "야간 알림 기능 보완 필요" ("night alert feature needs improvement"), "추가 검토 필요" ("further review needed"), "입력 절차 중복" ("input steps duplicated") | Seals the sentence with an empty noun to look like a noun ending |
| Degree-fudging ending | "사실상 무산된 셈" ("practically amounts to cancellation"), "개선된 편" ("improved, more or less") | "예산 미확보로 추진 중단" ("work halted for lack of budget"), "전년 대비 처리 기간 단축" ("processing time shorter than last year") | Hides the grounds and degree of the judgment |
| Emphatic assertion ending | "결국 비용이 문제라는 것이다" ("in the end it is that cost is the problem") | "비용 부담이 도입 지연의 주된 원인이다" ("cost burden is the main cause of the delay") | Wraps the claim in "-것이다" to add assertive weight |
| Hedging ending | "수요가 회복되는 것으로 보임" ("demand seems to be recovering"), "개선이 필요한 것 같다" ("improvement seems needed") | With grounds: "재고 소진 속도 회복으로 수요 회복 확인" ("demand recovery confirmed by faster inventory turnover"). Without: "수요 회복 여부 확인 필요" ("need to confirm whether demand recovers") | Omits both the judge and the grounds |

Handle emphatic pseudo-clefts such as 중요한 것은 ("what matters is") and 주목할 점은 ("the notable point is") under empty expressions in `expression.md`.

### Tests

- (Replacement test) When a specific noun can replace the empty noun and the new sentence carries more information, revise it.
- (Nominalization test) When "-하는 것" can become a Sino-Korean noun or a -기/-음 form with the same meaning, revise it.
- (Ending test) When you can delete the sentence-final empty noun and end naturally on a predicate noun such as 필요 "needed", 저조 "low", or 확인 "confirmed", revise it.
- (Structure first) Before checking the word list, check whether "adnominal clause plus information-free noun" empties the subject slot or seals the sentence end.
- (Density check) When empty nouns of any kind appear three or more times in one paragraph or item group, run the replacement test on each. Density only triggers the check. Do not revise on density alone.

### Allowed cases

Keep the original in these cases even when a test flags it.

| Allowed type | Example | Reason |
|---|---|---|
| Lexicalized words | 먹을 것 "food", 탈것 "vehicle", 날것 "raw food", 새것 "new item", 옛것 "old things" | Fixed as single words with no replacement noun |
| Grammatical function | "-할 수 있다" ("can"), "설치하는 데 소요" ("required for installation"), "보고한 바와 같이" ("as reported") | 수, 데, and 바 express ability, purpose, or reference and hide no referent |
| Real places | "주차 공간이 부족한 곳에 임시 주차장 설치" ("temporary parking where spaces are short") | 곳 points to physical locations specified by context |
| Directive endings in directive genres | "제출 기한을 준수할 것" ("meet the deadline"), "첨부 서류를 확인할 것" ("check the attachments") | Idiomatic ending for regulations, notices, checklists, and prompts. Does not cover "-할 것" in the narrative part of a report |
| Grounded forecasts | "금리 인하 기조 유지로 대출 수요가 늘어날 것으로 전망" ("loan demand expected to rise as rate cuts continue") | The grounds sit inside the sentence |
| Replacement changes the meaning | A sentence whose focus or meaning shifts when a specific noun replaces the empty one | Replacement adds nothing and damages the meaning |

### Handling

- Revise by ending on a predicate noun, naming the referent, or nominalizing with a Sino-Korean noun.
- Swapping one empty noun for another or for a colloquial contraction does not count as a revision. Turning "필요한 것" into "필요한 곳", "필요한 거", or "필요한 부분" leaves the information unchanged.
- When a substitute noun comes to mind while you avoid 것 during writing, treat the spot as a signal to rebuild the sentence with a predicate-noun ending or a named referent.
- Keep the original ending style. Revise noun-ending text with noun endings and verb-ending text with verb endings.
- In revise mode, recover the referent of each empty noun from the original context. When it cannot be recovered, do not fill it in. Ask the user about that spot.

```markdown
Before
- 민원 처리가 지연되는 곳은 부서 간 이관 단계
    + 담당 부서를 재지정하는 데 평균 이틀이 소요되는 부분
- 현재 체계는 사실상 이관을 방치하는 셈
    + 자동 배정 규칙을 도입할 거

After
- 부서 간 이관 단계에서 민원 처리 지연 발생
    + 담당 부서 재지정 과정에서 평균 이틀 소요
    + 재지정 기준이 문서로 정해지지 않아 담당자 판단에 의존
- 현행 체계에서 이관 민원의 후속 관리 미흡
    + 민원 유형별 자동 배정 규칙 도입 필요
    + 이관 후 처리 기한 경과 시 담당 부서에 알림 발송
```

Gloss: the "before" text says complaint handling is delayed at "the place" of inter-department transfer, reassignment takes two days on average "as a part", the system "practically amounts to" neglect, and "the thing" is to introduce auto-assignment. The "after" text states that delays occur at the transfer stage, reassignment takes two days, the reassignment criteria are undocumented, follow-up on transferred complaints is weak, auto-assignment rules by complaint type are needed, and the department receives an alert when a deadline passes.

## Sentence rhythm

- Keep each sentence from growing too short or too long. Even a simple sentence must carry enough 5W1H information.
- Keep the number of child items under one item neither too small nor too large.
- Avoid repeating the same word, subject, predicate, or ending in adjacent sentences.
- Read the text aloud and fix places where the rhythm stumbles.
