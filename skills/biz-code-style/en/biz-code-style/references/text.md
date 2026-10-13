# Sentences and wording

These rules apply to code comments, commit messages, log text, text inside charts and diagrams, and response sentences that explain analysis results. In code and visuals too, the quality of a single line of text sets the quality of the whole output. Code itself and quoted source text are out of scope. Word choice follows wording.md, and choosing one message per unit follows focus.md. When the user deliberately asks for rhetorical expression, the stock phrasing rules in this file do not apply to it. Rules marked (Korean text) concern Korean grammar and keep their Korean examples with English glosses.

## Sentence basics

- Put one message in one sentence. Write simple sentences in which the subject and predicate hold one relationship.
- Write so the rhythm sounds natural when read aloud. Keep sentences from being too short or too long, and keep words, subjects, predicates, and endings from repeating unnaturally.
- Do not write compound or complex sentences, ungrammatical sentences, or sentences with dropped particles.
- Each of who, when, where, what, why, and how appears once per sentence. If one appears twice, split the sentence.
- Include Why, What, and How in a sentence. (recommended)
- (Korean text) Do not use connectives such as 그리고 (and), 그러나 (but), 그래서 (so), 그렇기 때문에 (therefore), 이는 (this), -으며 and -있으며 (and, while).
- Use commas only to list three or more items of the same category. Resolve commas that join clauses by splitting the sentence or restructuring it as a noun phrase. Do not delete only the comma and leave an awkward sentence behind.
- Do not use middle dots, separator symbols such as slashes or vertical bars, excessive abbreviations, unneeded foreign or Sino-Korean words, or hyphens that join words.
- (Korean text) Use noun-ending bullet style (명사형 종결) and write verb endings where the flow calls for them. Make noun endings read as natural Korean ("목차명은 키워드 기반으로 재구성" over "목차명에는 키워드 기반 재구성으로 반영").
- Do not write sentences made only of stacked nouns (write "연구 인프라 보유 여부", whether research infrastructure is in place, over "연구 기술 자원 역량 상태", research technology resource capability status).
- Use periods only where needed. (recommended)
- The tilde can render as strikethrough in Markdown, so use a hyphen (-) for ranges.
- (Korean text) Use only characters on the standard Korean 103 and 106 keyboards. (recommended)
- Do not summarize, abbreviate, or alter nouns such as personal names, document titles, policy names, product names, and organization names. Use the full official name unless the user asks otherwise.

## Tone

- Write in a concise bullet style based on academic prose. Do not use honorific speech, colloquialisms, buzzwords, slang, or jargon of insiders.
- Keep logic and explanations of concepts as easy and simple as possible. Keep vocabulary and style at the formality of official documents for adult practitioners.
- Explain at a level a practitioner with introductory knowledge of the field can follow. (recommended)
- Write in a warm tone without losing objectivity. (recommended)
- For the same content, lead with positive wording ("the transition becomes possible once structured data is secured" over "data readiness is insufficient").
- Use polite, non-aggressive euphemism ("needs reinforcement" over "capability is severely lacking", "B is needed for A" over "absolutely impossible"). Criticize what is clearly wrong, and do not let euphemism blur the meaning.
- Avoid assertive and aggressive words such as absolutely, block, only, sole, unconditionally, top priority, and final. (recommended)
- Avoid nerd-style writing that shows off details only experts know. (recommended)
- Do not explain knowledge the target reader already has. (recommended)

## Logic

- Write from first principles. Avoid pure number-counting and excessive marketing angles. (recommended)
- Aim for the expertise and quality of a professional consulting report. (recommended)
- Fix definitions, criteria, and scope clearly at the start and keep them the same throughout. Do not mix different criteria.
- Avoid mechanical, defensive, or imitative thinking detached from reality. Examples are a security model that relies only on a deny list, a classification that mixes facts with judgments, and a design that copies a leading case without reason.
- Do not use the name of an authoritative organization as a substitute for reasoning.
- Do not say anything without evidence and a source, and make evidence and sources visible. Trace evidence to the root cause by asking "why" repeatedly.
- Do not mix objective facts with judgments or analysis in description or classification.
- Neutral and objective means a clear conclusion based on facts. Do not set up straw men, leap, overstate, or argue aggressively in order to speak for a middle position.
- Choose one structure that fits the purpose, either Why-What-How or situation-complication-question-answer. Do not put the structure's name in titles. Rephrase with keywords that fit the content. (recommended)
- Apply logic checks internally to design and writing, and do not expose the names of the checking frameworks on the surface of the output.
- Write while judging whether the storyline, logic, and wording are valid to a third party and easy to explain.
- Write in modules that are easy to revise and delete. Each part should read on its own and attach to or detach from other text easily.
- Give sentences enough information so they are not too short, and keep the number of paragraphs to a minimum.

## Response format

Structure with bullets unless there is a good reason not to. Do not use indented sub-bullets.

```
# Main title (keyword-based)
## Section title (keyword-based)
- Claim, with a subtitle if needed, no indentation
> (Data name) Qualitative or quantitative supporting data, only when needed
```

- Choose keyword-style or sentence-style headers, whichever works better, and keep one style within a document.
- Put one topic under one header. Do not bundle two topics in a header name, as in "X and Y", "X or Y", or "X/Y".
- When structuring, name the headers first and with care, and set the storyline between them. Check the header names again just before final output. The header name alone should tell what is underneath.
- Wrap a subtitle placed before a sentence in parentheses. Write "(SO WHAT) Define the purpose of the project", and do not use "SO WHAT : ..." or "SO WHAT - ...".
- Do not use meaningless subtitles such as "(Explanation)", "(Reason)", "(Claim)", "(Evidence)", "(Section 1)", or repeat the same subtitle. Name subtitles by content, such as "(Adoption driven by field demand)".
- Summarize long text in tables, with no more than three tables overall. (recommended)
- Place a table right after the claim it supports. Do not place tables back to back.
- Do not put tables inside blockquotes (>) or code blocks.
- Build table columns, rows, and cell text without overlap, keeping them concise. (recommended)
- When citing several sources in blockquotes, break lines to separate the blocks.

## Quantitative data and sources

- Use quantitative data only when its derivation or a credible survey basis is clear, and state the basis for each number.
- A sentence with quantitative data must let a third party answer who, when, where, what, why, and how when asked for the basis.
- (Correct example) "According to ABC Research's survey in year Y, the AI application market is projected to grow from about B won in year A to about D won in year C, at a compound annual growth rate of about N% (ZZ methodology, optimistic scenario)"
- (Wrong example) "The AI application market is projected to grow N%"
- Prefer time series of 3-5 years or more, and add the compound annual growth rate and the share of the total. (recommended)
- Use three or fewer key quantitative figures in a whole document. Beyond three, every number becomes noise that clouds judgment. (recommended)
- Write sources in a blockquote in the form "Organization or author (year), document title (link)". Write the full address that reaches the document directly. A bare domain is not enough.
- When citing a document or information, include what is needed so readers do not have to find the original themselves.
- Run web searches only when the user allowed it. When searching, cover both Korean-language and English-language sources. (recommended)
- Cite documents and press releases of central and local governments and public agencies in Korea and abroad, large consulting firms (McKinsey, BCG, Bain, Deloitte, PwC, KPMG, EY) and research institutes, academic papers, research reports, credible financial institutions, and large open-source communities. Do not cite media without credibility, blogs, wikis, or columns. (recommended)
- A single keyword can work better as a search query than a complex bundle of keywords. (recommended)
- Gather all sources first, then synthesize. Do not write while searching.
- Every claim that supports a conclusion needs a source that was actually opened and read. For each claim, check internally what its evidence is and what fact would prove it wrong.

## Stock AI phrasing

These are expressions LLMs produce out of habit. When writing, do not produce them in the first place, and do not reveal that these rules were applied. When revising existing text, briefly summarize the expressions to fix by type, then deliver the revised text. These rules do not govern style choices such as sentence length, connectives, sentence endings, or overall structure, which follow the sentence basics above. Where the user's style guide overlaps, follow the user's guide for notation and these rules for whether something is stock phrasing.

### Empty expressions

Expressions whose removal leaves the meaning unchanged.

- (Glue phrases) Delete "이러한 맥락에서" (in this context) and "이러한 관점에서 볼 때" (from this perspective), and go straight into the content.
- (Avoided conclusions) Replace "시사하는 바가 크다" (it has great implications) and "의미가 있다" (it is meaningful) with the specific implication, or delete them.
- (Importance announcements) Delete "중요한 것은" (what matters is), "주목할 점은" (notably), and "여기서 핵심은" (the key here is), and let the content speak.
- (Previews and scope statements) Delete "먼저 A를 살펴보고" (first we look at A) and "이 글에서는 X를 다룬다" (this piece covers X).
- (Excess modifiers) Delete intensifying adverbs such as 매우 (very), 상당히 (considerably), 굉장히 (extremely), 진정한 (true), 사실상 (virtually), praise words such as 탁월한 (outstanding), 획기적인 (groundbreaking), 혁신적인 (innovative), and exaggerating qualifiers such as 엄청난 (enormous), 폭발적인 (explosive), 전례 없는 (unprecedented), or replace them with specific numbers, comparisons, or evidence.
- (Negated confirmation) Delete "부정할 수 없다" (undeniable), "분명하다" (clearly), and "자명하다" (self-evident), and state the fact as it is.
- (Stacked hedges) Do not stack uncertainty, as in "somewhat to a degree slightly positive, it seems". State uncertainty once.
- (Abstract repackaging) Delete the wrapper in "X라는 Y" and "Y로서의 X" forms, such as "토큰 예측이라는 단일 메커니즘" (a single mechanism called token prediction) or "조직 혁신 수단으로서의 AI" (AI as a means of organizational innovation), and write X directly. Rewording into an "X의 Y" noun phrase or an "X는 Y" declaration counts as the same problem if no information is added.
- (Declarative definition lists) Do not line up facts the reader already knows as "X is Y" in place of analysis. If deleting the sentence costs no understanding, delete it and fill the space with analysis or judgment the reader does not have. Pairing symmetric words such as "capabilities and limits" to avoid specifics is the same problem.

### Formulaic rhetoric

- (Contrast emphasis) Do not write "not simply A but B", "not A but true B", or "not A but B". State B directly.
- (Self-posed questions) Do not ask and answer, as in "Why did this happen? Because...". Write the answer directly.
- (Dramatic fragments) Do not aim for drama with one- or two-word sentences, as in "Innovation. That is it."
- (Staccato rhythm) Do not build rhythm from a run of short sentences, as in "Fast. Accurate. Efficient." Merge them into content-bearing sentences.
- (Repeated structure) Do not repeat the same subject-predicate shape in three or more adjacent sentences.
- (Overgeneralization) Do not write conclusions beyond the evidence, such as "this signals a paradigm shift for the whole industry".
- (Vague partial agreement) Replace "half right" and "largely agree" with the specific range of agreement and disagreement.
- (Number announcements) Do not announce the number of items in advance, as in "three major strategies" or "four measures". List the content directly. A count that emerges from the listed items ("divided into short, mid, and long term") is fine.
- (Fitting to a count) Do not habitually fit items to three. Write two if there are two and four if there are four.

### Symbol overuse

- Do not use em dashes. Split the sentence or use parentheses or commas.
- Use colons only to introduce an actual list or a formal quotation. Do not use them to attach a single label, as in "Conclusion:" or "Key point:".
- Use semicolons only to join closely related independent clauses. Split everything else with periods.
- Use ellipses only to mark omissions in quotations.
- Use bold only for items readers scan for, such as term definitions and technical identifiers, and never for emphasis.
- If colons, semicolons, and ellipses exceed one per 150 words on average, reduce them.

### Tautology and circularity

- Do not write "A because A" sentences such as "improvement is required because improvement is needed". Add evidence or delete.
- Do not restate purpose as definition, as in "a budget is drawn up to be spent".
- Do not write empty obligations such as "it is judged that we should..." or "it is judged that review in the direction of... is needed". State the concrete action or condition.
- When defining a concept, do not reuse the word being defined in the definition.

### Meta narration

Narration aimed at the text itself, the writing process, the writer, or the tools used, regardless of what the reader needs.

- Do not refer to the text itself, as in "this report", "the purpose of this piece", "in this section", or "as mentioned in the previous section".
- Delete "in conclusion", "to sum up", and "in summary", and state the conclusion directly.
- Do not draw the reader's attention, as in "what deserves attention is" or "what I want to stress here".
- Do not reveal the frameworks used in writing, as in "following the MECE principle" or "from a 5W1H perspective".
- Do not evaluate your own output, as in "this classification covers everything without omission".

### Translationese (Korean text)

- Write "-에 있어서" as "-에서", "-인 셈이다" as a direct noun-ending statement, "-것은 아닐까" as a direct proposition, and "-라고 하는" by reordering into "Y인 X". These forms come from literal translation of Japanese.
- Write "-하는듯" as "-으로 추정", and "-하지 않으면 안 된다" and "-할 수밖에 없다" as "-할 필요" or "-이 불가피".
- Shorten "-에 대하여", "-을 통하여", and "-로 인하여" to "-에 대해", "-을 통해", and "-로 인해", or restructure the sentence.
- Do not overuse the suffixes -적(的) and -화(化).

### AI-favored vocabulary

- Replace exaggerated transformation phrases such as paradigm shift, game changer, and "change the landscape" with the specific change.
- Replace abstract catch-all nouns such as 맥락 (context), 담론 (discourse), 지형 (landscape), 프레임 (frame), and 레버리지 (leverage) with the specific object.
- (Korean text) Replace English loan phrases such as 딥다이브 (deep dive), 인사이트 (insight), and 피보팅 (pivoting) with Korean words.
- Do not overuse 견인하다 (drive) and 선도하다 (lead). State the concrete action.
- The detailed list follows wording.md.

### Structural monotony

- Do not repeat generic labels such as "Overview", "Background", "Status", and "Conclusion" as headings. Name them with keywords that reflect the content.
- Do not merely list adjacent items without relation. Give them relations such as cause, elaboration, or contrast.
- Do not attach a bold subtitle to every bullet mechanically.

### Unsupported statements

- Do not write conclusions without evidence, quantitative data without sources, arguments that rest only on "according to X", or generalizations without cases such as "all global companies". Add evidence or sources, narrow the scope, or delete.

### Awkward noun endings (Korean text)

An error where a noun-ending sentence fails to drop the verb and leaves an adnominal form. This rule only fixes grammatical errors in sentences that use noun endings.

- Write "목적 달성을 할 필요" and "목적을 달성할 필요" (the need to achieve the goal) as "목적 달성 필요". Write "선행할 필요", "정의할 필요", and "내장시킬 필요" the same way, as "선행 필요", "정의 필요", and "내장 필요".
- Complete unfinished noun phrases such as "작업의 부담" (the burden of work) with a predicate noun, as in "작업 부담 발생" (work burden arises).
- If deleting the adnominal form keeps the meaning, fix it. Leave cases where the verb limits the object and deleting it changes the meaning, as in "삭제할 파일" (the file to delete).

### Placeholder nouns (Korean text)

The habit of wrapping what is referred to in an information-free noun instead of naming it. The typical form is the dependent noun '것' (thing). Blocking '것' alone pushes the habit to '곳' (place), '거' (colloquial thing), '셈' (sort of), and '부분' (part), so judge by what the structure does in the sentence.

- Placeholder nouns include 것, 점, 부분, 사항, 측면 (things and matters), 곳, 데 (places), and 바, 셈, 편, 터, 식 (states and degrees). Treat nouns outside the list the same way when they play the same role.
- Treat colloquial contractions such as '거', '게', '건', and '걸' the same as '것', and fix them first in formal writing.
- (Pseudo-cleft sentences) Write "사업 지연을 초래한 것은 승인 절차의 중복" (what caused the delay is duplicated approval) as "승인 절차 중복으로 사업 지연 발생" (duplicated approval delays the project).
- (Detoured nominalization) Write "데이터를 정비하는 것이 필요" (organizing the data is needed) as "데이터 정비 필요".
- (Vague reference) Name the object, as in "현장에서 요청한 야간 교대 알림 기능을 반영" (reflect the night-shift alert the field requested) in place of "현장에서 원하는 것을 반영" (reflect what the field wants).
- (Placeholder endings) Write "보완이 필요한 곳" and "추가 검토할 거" as "야간 알림 기능 보완 필요" and "추가 검토 필요".
- (Hedged degree) For "사실상 무산된 셈" (more or less scrapped) and "개선된 편" (somewhat improved), state the basis and the degree.
- (Emphatic assertion) Write "결국 비용이 문제라는 것이다" (in the end, cost is the thing) as "비용 부담이 도입 지연의 주된 원인" (cost is the main cause of the delay).
- (Evasive estimates) For "수요가 회복되는 것으로 보임" (demand appears to be recovering), write a confirmation with its evidence if evidence exists, or "수요 회복 여부 확인 필요" (demand recovery needs confirmation) if not.
- (Test) Fix it if the placeholder can be replaced with a specific noun and the new sentence carries more information. Fix it if '-하는 것' can become a Sino-Korean noun or a nominal form (-기, -음) with the same meaning. Fix it if the placeholder at the end can be deleted and the sentence can end with a predicate noun such as "필요" (needed), "저조" (low), or "확인" (confirmed).
- (Density) If placeholder nouns of any kind appear three or more times in a paragraph, test each one. Do not fix on density alone.
- (Allowed) Leave lexicalized words such as 먹을 것 and 탈것, grammatical uses such as "-할 수 있다", "설치하는 데 소요", and "보고한 바와 같이", references to actual places such as "주차 공간이 부족한 곳", directive endings in rules, checklists, and prompts ("제출 기한을 준수할 것"), forecasts whose evidence is in the sentence, and sentences whose meaning changes when replaced.
- (Fix) Fix by ending with a predicate noun, naming the object, or using a Sino-Korean noun. Swapping one placeholder for another or for a colloquial contraction does not count as a fix. Keep the original sentence ending style. If the referent cannot be found in the original, do not fill it in arbitrarily. Ask the user.

## Examples

Code comment (before):

```python
# In this context, handling missing values is very important
# First look at the data, then fill in the missing ones
df["revenue"] = df["revenue"].fillna(0)
```

Code comment (after):

```python
# Replace empty revenue of closed stores with 0 to keep monthly totals complete
df["revenue"] = df["revenue"].fillna(0)
```

The glue phrase, intensifying adverb, and preview are gone, and the comment states why the code is needed.

Chart caption (before): "Innovative growth. That is what shows the true value of the materials division."

Chart caption (after): "The materials division generated more than half of company-wide revenue growth in 2024"

The praise word, dramatic fragment, and contrast emphasis are gone, replaced with a judgment sentence.

## Checklist

- Does each sentence carry one message?
- Are connectives, unneeded commas, and separator symbols absent?
- Are expressions that delete without loss, excess modifiers, and praise words absent?
- Are contrast emphasis, self-posed questions, dramatic fragments, and number announcements absent?
- Are em dashes, emphasis bold, dramatic ellipses, and label colons absent?
- Are tautologies, empty obligations, and circular definitions absent?
- Is narration about the text itself or the writing process absent?
- Are translationese and AI-favored vocabulary absent?
- Do no three adjacent sentences share the same structure?
- Does every conclusion and claim have evidence, and every number a source?
- Are no unneeded adnominal forms or particles left in noun endings?
- Do placeholder nouns hide no object that could be named with a specific noun?
- Did you avoid swapping a placeholder noun for another placeholder or a colloquial contraction?
- Did you avoid wrongly fixing expressions that meet the allowed conditions?
- Does each header hold one topic, and are subtitles wrapped in parentheses?
- Does the rhythm sound natural when read aloud?
