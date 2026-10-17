---
name: slop-proof
description: "Finds and fixes AI slop in writing. Covers the habits LLMs fall into: overused and inflated vocabulary, stock phrases, formulaic rhetoric, symbol overuse, empty nouns, meta commentary where the text talks about itself or its writer, and both-sides answers that avoid a conclusion. Checks text at four levels (words, sentences, meta commentary, conclusions) in writing mode for new text and in editing mode for existing text. Use this skill when the user types '/slop-proof' or asks to remove AI slop, make text sound less like AI, strip AI tells, clean up AI-sounding wording, check vocabulary, remove meta commentary or self-reference, stop hedging, stop both-sidesing, give a clear conclusion, or pick a side, and when the user asks to fix AI-style writing in reports, proposals, plans, or analyses. When the user asks for a neutral summary of both positions, skip the rules that push the conclusion to one side."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# AI Slop Removal

> This skill was translated from a Korean original. It may behave differently from the original intent, especially where a rule depends on Korean grammar or on the nuance of a word. Rules that only apply to Korean text are grouped under "Korean-only rules" at the end of section 2.

AI slop means expressions an LLM produces out of habit that give the reader no new information. Overused vocabulary, formulaic rhetoric, meta commentary in which the text describes itself, and answers that give both sides equal weight to avoid a conclusion all count. When these pile up, readers slow down and trust the text less.

The skill finds and fixes slop at four levels: words, sentences, meta commentary, and conclusions. The word and sentence levels deal with the form of expressions. The meta and conclusion levels deal with the information a sentence gives the reader.

## How it works

- (Writing mode) Apply the criteria while drafting new text. Do not mention in the output that the skill was applied.
- (Editing mode) Find and fix slop in existing text. Give a short summary of the fixed patterns by type, then present the edited text.
- (Style neutrality) Sentence length, whether to use connectives, sentence-ending style, the overall structure of the piece (SCQA, WWH, SCR and so on), markdown hierarchy, length, and number of items are outside this skill. Follow the user's style guide or the conventions of the genre.
- (Conflicts) When the user's style guide clashes with this skill, follow the user on formatting and follow this skill on what counts as slop.
- (No self-exposure) In writing-mode output and in the body of edited text, do not reveal the names of this skill's criteria, categories, or tests. The type summary in editing mode is exempt because the user asked for it.

## Tests

The lists in each section collect expressions that often fail the tests below. When one expression gets blocked, an LLM tends to move to a similar one. Apply the same fix to any expression that fails a test, listed or not.

| Test | Question | If yes |
|---|---|---|
| Deletion | Does the reader get the same information with this expression removed? | Delete it and go straight to the content |
| Substitution | Would a more specific word add information? | Use the specific word |
| Subject | Is the real subject of the sentence the text itself, the writer, the act of writing, the user's request, or a tool? | Treat as meta commentary (section 3) |
| Beneficiary | Does the sentence serve the writer's self-justification, disclaimers, or showing off more than the reader? | Treat as meta commentary (section 3) |
| Courtesy | Does it only greet, praise, confirm, guide, or prompt, with no information? | Treat as meta commentary (section 3) |
| Request direction | Does it cover the opposite polarity, the complement, or a replacement the user did not ask for? | Treat as meta commentary (section 3) |
| Conclusion | Does the conclusion slot of an analysis hold an expression with no direction? | Draw a conclusion (section 4) |

Check the subject test first because it is the most mechanical. A sentence that passes the subject test still gets fixed if it fails another test.

## 1. Words

### Classification

Words are sorted by how readers receive them, how much they mark the text as AI output, and how natural they sound. Words with the same meaning can land in different groups when their tone differs.

- (Preferred) Words readers accept easily and that fit formal documents. When a non-preferred word comes to mind, pick the preferred one with the same meaning.
- (Non-preferred) Words that meet one or more reasons in the table below. Replace or delete them, then check that the sentence still means the same thing.
- (Use with care) Words that are usable but lose their force when repeated, until the whole text reads as noise. Use conditional words only when the condition holds, and use any of them no more than once per paragraph.

### Preferred words

- (Nouns) linkage, cooperation, strategy, direction, vision, takeaways, change, development, convergence, transition, improvement, differentiation, contribution, supplement, stage, demand, conditions, current status, actual state, trend, movement, outlook, funding, infrastructure, regional base, demonstration, pilot, diffusion, implementation, full lifecycle, concurrency
- (Verbs) draw up, secure, introduce, increase, derive, build up, shift, set, expand, match, open, contribute, link, cooperate, pursue, prepare, reflect, apply, operate, use, raise, reduce, ease, promote, include, add, exclude, delete, deduct, state side by side
- (Modifiers) phased, gradual, short-term, mid- to long-term, specific, clear

### Non-preferred words

| Reason | Words | Fix |
|---|---|---|
| LLMs overuse them, so they mark text as AI output | context (as glue or abstraction), discourse, layer, tier, level, hierarchy (abstract uses such as "at multiple levels"), disconnect ("the disconnect between perception and reality"), graded, in full, parallel, restricted to, gate, MVP (including lean-method explanations), integrated package, tide ("the great tide"), break away from ("break away from old ways"), tailored, customized, multilayered | Name the specific thing or action |
| Spread beyond their home field | bottleneck (outside real process analysis), value (outside engineering), full-stack (where "full lifecycle" fits) | Keep to the original use or replace |
| Emphasis that adds nothing when deleted | very, quite, considerably, extremely, virtually, literally, genuine ("genuine innovation"), fundamental, essential (when adding abstract authority), comprehensive, overall (when specifics disappear) | Delete or state the degree |
| Inflation without evidence | groundbreaking, innovative, pioneering, overwhelming, radical, unprecedented, unheard-of, explosive, astonishing, outstanding, excellent, historic, enormous, all-out, surge, leap, first-mover, paradigm, game-changer, "change the game", first-ever (when overused), strongest, weakest, orphan, maximize, encompass, span, reign, sweep, dominate, lead (when overused), trigger | Replace with evidence, figures, or a comparison |
| Absolutes that shut out counterarguments | absolutely, only, sole, unconditionally, immediately, top priority (when overused), "directly linked", causal (as an assertion), crux, prerequisite, reference standard, strictly observe, "make or break" | State the conditions and scope |
| Words that intimidate the reader | block, exclude, prohibit (except when quoting a rule), evade, weed out, preemptive | Use a neutral verb |
| Jargon and abstractions LLMs favor | landscape, frame, leverage, implications ("the implications are significant"), mapping (use matching, linking, placement), deep dive (use analysis), insight (use finding), pivot, gatekeeping, ultimately, holistic, dynamic | Use plain words |
| Stale metaphors | new horizons, backbone, milestone, turning point (when overused), catalyst, stepping stone, breakthrough, cornerstone, beachhead, blueprint, compass, beacon | Say what happens |
| Paired with number declarations | "two pillars", "two axes", "seven-piece set" | Fix under number declarations in section 2 |

### Words to use with care

| Condition | Words |
|---|---|
| Only when naming the real thing | governance (a real decision-making structure), ecosystem (real relationships among several actors), roadmap (a real schedule), hub (a real site), platform (a real technical platform), solution (a real product or service), agenda (a real agenda), initiative (a real program), benchmark (a real comparison standard), voucher (a policy instrument), government-wide (real cross-ministry work), seed money (as a metaphor for early public investment), input and output (engineering contexts), language, translation, interpretation (real languages only, never as a metaphor), insert (as the name of an editing function, with add or place in prose), inject (technical terms such as "SQL injection", with reflect or apply in prose), deploy resources (people or budget), guardrail (carries a strong security or regulatory sense, so use it only when needed, and avoid "guard" alone) |
| Only with specifics attached | key (the one thing that matters most), innovation (a change unlike what came before), drive (when the causal link is clear), cover (when the scope is stated), strengthen (with the method), build (real new development), upgrade (real improvement of an existing system), synergy (when the effect is stated), area (when a specific target exists), substantive, multi-angle (when the angles are named), organic (when the linking method is stated), intact (when intactness has been confirmed), differentiated (not as a stock modifier), foundation (alone, and "laying the foundation for X" needs a specific X) |
| Non-preferred in certain combinations | conclusion ("In conclusion"), judge ("it is judged that"), confirm ("as confirmed"), essence, root, principle (when adding abstract authority), cross-check (when narrating method), lead, leading (as a stock modifier), strategic direction (both words are overused) |
| Managed by frequency only | result, impact, environment, capability, risk, limitation, gap, problem, issue, task, system, structure, alignment, verification, diagnosis, assessment, control, management, responsibility, evidence, objective, subjective, danger, threat, regulation, compliance, logic, priority, ranking, connection, combination, composition, rule, proposition, reservation, finalize, organization, personnel, compensation, affiliation, decision, single, especially, decisive, key (as a modifier), strategic, systematic, effective, active, continuous |
| Common in LLM English, allowed only for real reference | intricate, pivotal, crucial, robust, foster, bolster, cutting-edge, seamlessly, stakeholder |
| Phrases that need specifics after them | "lay the groundwork for", "create synergy", "build a virtuous cycle" (name the cycle), "strengthen ties with" (name the party and the method), "sustainable growth" (name the conditions) |

### Connectives

| Expression | Why | Fix |
|---|---|---|
| In this context, Given this context, From this perspective, In this respect, Amid this trend, "in that", "in terms of" | Glue that links sentences with no content | Delete and go straight to the content |
| Furthermore, Moreover, Not only... but also, Additionally, Ultimately | Stock glue LLMs overuse | Delete or state the real relation |
| That is why, sentence-initial "This" pointing at a whole previous sentence | Overuse chains sentences together and blurs the referent | Split the sentence or name the referent |
| In other words, That is | Makes the text repeat itself | Delete |
| Meanwhile, On the other hand, Based on this, Through this, In relation to this | Used only to switch topics, with no real contrast or cause | Use only when the relation is real |
| In conclusion, To summarize, In summary | Meta commentary announcing what the text does | Delete and state the conclusion |

### Common LLM English words

Treat these as non-preferred: delve, landscape, tapestry, realm, leverage, navigate, underscore, showcase, harness, spearhead, multifaceted, ever-evolving, game-changer, groundbreaking, paradigm shift, holistic, and the frame "not just A but B".

### Stock phrases

- (Blurred conclusions) "This speaks volumes", "This offers important implications", "This is meaningful". State the specific implication or delete.
- (Assertions with no evidence) "cannot be overlooked", "undeniable", "clearly", "self-evident", "it goes without saying". Delete and state the fact.
- (Stock openers and generalizations) "The era of X has arrived", "The importance of X grows by the day", "Interest in X is rising", "The need for X is emerging", "X is drawing global attention", "X has become a global trend", "X is widely used across many fields". Replace with a specific case or evidence, or delete when none exists.

"What matters is" and "Notably" go under reader prompts in section 3. "Not just A but B" and "three key strategies" go under formulaic rhetoric in section 2. "The single mechanism of X" goes under abstract repackaging in section 2. "Half right" goes under conclusion avoidance in section 4.

## 2. Sentences

### Formulaic rhetoric

| Pattern | Example | Fix |
|---|---|---|
| Contrast framing | "not just A but B", "not A but true B", "not A but B", "beyond A to B", "doesn't stop at A, it goes to B" | Write B directly. Skip this frame even when A is a widely rejected idea |
| Repeated structure | "X is... Y is also... Z too is..." | Vary the sentence structure |
| Dramatic fragments | "Innovation. That's it." | Write complete sentences |
| Staccato rhythm | "Fast. Accurate. Efficient." | Merge into sentences built on content |
| Self Q&A | "Why did this happen? Because..." | Delete the question and state the answer |
| Rule-of-three habit | Forcing items into lists of three regardless of content | Match the count to the content. Keep real lists of three |
| Number declarations | "3 key strategies", "4 measures", "5 core tasks", "7 directions", "N ways", "two pillars" | List the content without announcing the count. Allowed when the count shows in the list itself ("split into short, mid, and long term") |

### Abstract repackaging

LLMs wrap a clear term X in an abstract noun Y: "the Y of X", "X, a Y", "X as a Y". Y adds no information and only lengthens the sentence. Delete the wrapper and use X directly, adjusting the grammar where needed.

| Before | After |
|---|---|
| the single mechanism of token prediction | token prediction |
| under the goal of cost reduction | to cut costs |
| amid the great tide of better customer experience | as customer experience improves |
| facing the challenge of introducing a new system | while introducing a new system |
| the essential value of productivity | productivity |
| training as a means of organizational innovation | using training to change the organization |

When one wrapper is blocked, the writer moves to the next ("X as a Y", then "the Y of X", then a bare "X is Y" declaration). Judge by whether information increased, whatever the surface form.

### Empty nouns

LLMs often skip naming what they refer to and wrap it in a noun that carries no information, such as thing, part, point, matter, aspect, area, or way. The writer knows the referent but leaves it unnamed, and the reader has to reconstruct it from the surrounding sentences. Block one of these nouns and the model moves to a sibling while keeping the same "clause plus empty noun" frame. So judge by what the frame does, whatever noun fills it. The list is a starting point. Any noun doing the same job gets the same treatment.

| Type | Before | After | Problem |
|---|---|---|---|
| Pseudo-cleft ("What X is Y") | "What caused the delay was duplicate approvals", "Where improvement is most urgent is the approval step" | "Duplicate approvals delayed the schedule", "The approval step needs improvement first" | Leaves the subject slot empty and pushes the information to the end |
| Verb-to-noun detour | "What we need is to clean up the data", "The thing we set as a goal is reducing churn" | "The data needs cleanup", "The goal is a lower churn rate" | Takes a detour through an empty noun when a direct noun or verb exists |
| Vague reference | "reflect what the field wants", "considering things like this", "fix the problematic part" | "add the night-shift alert the field requested", "considering staff shortages and budget limits", "fix the duplicate input fields" | Compresses the referent into an empty noun and drops the information |
| Empty-noun ending | "It's a matter of low staff utilization", "It's the part where input steps overlap" | "Staff utilization is low", "Input steps overlap" | Closes the sentence with an empty noun where a real predicate belongs |
| Degree fudge | "It's more or less a failure", "It's on the better side" | "The project stopped because funding was not secured", "Processing time fell compared with last year" | Lumps the basis and degree of the judgment into a vague phrase |
| Assertive wrap | "The thing is, it all comes down to cost" | "Cost is the main reason adoption was delayed" | Wraps the claim a second time to add weight |
| Hedged estimate | "Demand seems to be recovering", "It appears improvement is needed" | "Inventory is clearing faster, which confirms demand recovery" when evidence exists, "Whether demand has recovered still needs checking" when it does not | Drops both the judge and the evidence |

Emphatic pseudo-clefts such as "What matters is" go under reader prompts in section 3.

- (Substitution test) Fix it when a specific noun can replace the empty noun and the result carries more information.
- (Nominalization test) Fix it when a direct noun or verb says the same thing as the detour.
- (Ending test) Fix it when the sentence ends naturally once the empty noun is removed and a real predicate takes its place.
- (Frame first) Check whether "clause plus empty noun" empties the subject slot or seals the end of the sentence before checking whether the noun is on the list.
- (Density check) When empty nouns of any kind appear three or more times in one paragraph or bullet group, run the substitution test on each. Density only starts the check and never justifies a fix on its own.

Some uses are normal grammar. Keep the original in these cases even when a test flags them.

| Allowed type | Example | Reason |
|---|---|---|
| Fixed expressions | "something to eat", "first things first" | The phrase works as a single unit with no noun to substitute |
| Grammatical function | "as reported earlier", "in the course of installation" | The noun marks source, time, or purpose and hides no referent |
| Real place | "set up temporary parking where spaces run short" | The phrase points to real locations the surrounding text identifies |
| Directive genre | "Submit by the deadline", "Check the attachments" | Rules, notices, checklists, and prompts use directive endings by convention |
| Forecast with its basis | "Loan demand is expected to rise as rates stay low" | The basis sits in the sentence, so nothing is omitted |
| Meaning shift | Sentences whose focus or meaning changes when a specific noun is swapped in | Substitution adds no information and damages the original meaning |

- (How to fix) Use a real predicate, name the referent, or use a direct noun.
- (No sibling swaps) Replacing one empty noun with another keeps the same information, so it does not count as a fix. "What's needed" rewritten as "the part that's needed" is still unfixed.
- (Signal while writing) In writing mode, when a sibling empty noun comes to mind while avoiding the first one, treat that spot as a signal to rebuild the sentence.
- (Keep the ending style) Fix noun-ending text with noun endings and verb-ending text with verb endings.
- (Recover the referent) In editing mode, recover the referent from the original text. When it cannot be recovered, ask the user about that spot instead of inventing it.

### Noun stacks

Stringing nouns together without prepositions or verbs hides the relation between them. Rewrite "digital industry agglomeration indicator" as "how concentrated the digital industry is", and "research technology resource capability status" as "whether research infrastructure is in place".

### Symbols

These criteria fix the habit of handing sentence-structure decisions to a symbol. Symbol use that meets the allowed conditions stays.

| Symbol | Misuse | Allowed when | Fix |
|---|---|---|---|
| Em dash | Drops an aside into a sentence without settling its structure | Never | Split the sentence, or use parentheses or commas |
| Colon | Replaces a statement with a label ("Conclusion:", "Key point:") | Introducing a real list or a formal quotation. Follow the user's style guide if it says otherwise | Remove the colon and write a sentence |
| Semicolon | Glues sentences instead of splitting them | Joining closely related independent clauses reads more naturally. User style guide first | Split with a period or join with a conjunction |
| Ellipsis | Creates dramatic suspense or a musing mood | Marking an omission in a quotation | Remove and complete the sentence |
| Bold inside sentences | Scatters emphasis over keywords | Terms being defined, technical identifiers, things readers scan for | Remove emphasis bold |
| Slash | Skips writing the relation ("cost/benefit") | Never | Write the relation out |
| Joining hyphen | Links separate words to skip the relation ("short-mid term") | Never | Write the relation out |

When colons, semicolons, and ellipses together exceed one per 150 words on average, treat it as overuse and cut back. For Korean text, count eojeol (space-separated units) as words.

### Structural monotony

| Type | Description | Fix |
|---|---|---|
| Repeated heading labels | Generic headings such as "Overview", "Background", "Status", "Conclusion" repeated mechanically | Rename with keywords from the content |
| Repeated subheading labels | Empty labels such as "(Explanation)", "(Reason)", "(Claim)", "(Evidence)" | Rename with keywords that carry content |
| Fixed syntax | Three or more neighboring sentences with the same subject-predicate pattern | Vary the structure to create rhythm |
| Parallel-list habit | Lists with no relation between items | Add relations such as cause, elaboration, or contrast |
| Bold subheading overuse | A bold label on every bullet | Add labels only where needed |

### Korean-only rules

These rules depend on Korean grammar and vocabulary. Apply them when the text is Korean. Glosses in brackets explain each item.

- (Translationese) Replace the calques in the table below.

| Expression | Source structure | Replacement |
|---|---|---|
| -에 있어서 ["in regard to"] | Japanese において | -에서, -에는, -시점에 |
| -인 셈이다 ["it amounts to"] | Japanese わけだ | A direct statement with a noun ending |
| -것은 아닐까 ["isn't it that"] | Japanese ではないか | A direct proposition |
| -라고 하는 ["called"] | Japanese という | Reorder as "Y인 X" |
| -하는듯 ["seems"] | Japanese ようだ | -으로 추정 |
| -하지 않으면 안 된다 ["must not fail to"] | Japanese ねばならない | -해야 한다, -이 요구됨 |
| -할 수밖에 없다 ["cannot but"] | Double negative | -할 필요, -이 불가피 |
| -에 대하여, -을 통하여, -로 인하여 ["regarding", "through", "due to"] | Japanese or English preposition calques | -에 대해, -을 통해, -로 인해, or state the cause directly |
| -의 경우 ["in the case of"] | English "in the case of" | Name the subject directly |

- (Suffix overuse) "-적" [的, "-ic"] three or more times in a paragraph, or "-화" [化, "-ization"] twice or more in a sentence ("디지털화의 고도화가 가속화" [digitalization's upgrading accelerates]), counts as overuse. Rebuild the sentence.
- (Empty nouns in Korean) The Korean empty nouns are 것, 점, 부분, 사항, 측면 [thing, point, part, matter, aspect], 곳, 데 [place], 바, 셈, 편, 터, 식 [state, degree]. The spoken contractions 거, 겄, 게, 건, 걸 [contracted forms of 것] count as 것 and also break formal register, so fix them first in reports. Korean allowed cases: lexicalized words (먹을 것, 탈것, 날것, 새것, 옛것), grammatical uses (-할 수 있다, 설치하는 데 소요, 보고한 바와 같이), real places (곳 for an identified location), directive endings in rules and checklists (-할 것), and forecasts with their basis in the sentence (-할 것으로 전망). A "-할 것" ending in the narrative part of a report is not a directive ending.
- (Noun-ending grammar errors) In text already written with noun endings (개조식), LLMs leave attributive verb forms (-할, -을 할, -시킬) or the particle 의 behind. This rule applies only to such text. Fix when deleting the attributive form keeps the meaning. Keep it when the verb picks out its object. "삭제할 파일" [the file to delete] stays, while "검토할 사항" [item to review] becomes "검토 사항" because the difference is small. "-할 것" endings go under empty nouns.

| Before | After | Problem |
|---|---|---|
| 목적 달성을 할 필요, 목적을 달성할 필요 [need to achieve the goal] | 목적 달성 필요 | Leftover "을 할" or attributive form clashes with the noun ending |
| 선행할 필요, 후행할 필요, 접근할 필요, 정의할 필요 | 선행 필요, 후행 필요, 접근 필요, 정의 필요 | Leftover "할" |
| 내장시킬 필요 [need to embed] | 내장 필요 | Leftover "시킬" |
| 접근할 시사 | 접근 가능, or a rebuilt sentence | "할" and "시사" do not fit together |
| 작업의 부담 [burden of work] | 작업 부담 발생 | Needless 의, and "작업 부담" alone is incomplete, so add a predicate noun such as 발생, 증가, or 우려 |

- (Korean vocabulary with no clean English match) Treat these as non-preferred. 결 and 틀 ("같은 결" [same grain], "평가틀" [evaluation frame]) sound unnatural. 온전 used as a noun cut from 온전한 [intact] sounds forced. 묵음 [muted] and 뽑기 [drawing lots] mark text as AI output. -결 coinages such as 귀결 [conclusive ending] act as absolutes. 갈래 [strand] is overused in place of branch or path. 통독 [reading through] is overused for reading a whole text, though Korean speakers rarely use it at work or in daily life. The loanwords 에코시스템, 트랜스포메이션, 컨틴전시, 커버리지, 헷지 [ecosystem, transformation, contingency, coverage, hedge] have Korean equivalents such as 생태계 and 전환. The calques 정립 [establish], 즉각적 [immediate], 야기 [cause], 수반 [entail], 내포 [imply] read as direct translations and take plain Korean replacements.
- (Verbs with sexual connotation) 넣다, 빼다, 박다, 쑤시다 and the coinage 동시삽입 [put in, pull out, drive in, poke, simultaneous insertion] sound colloquial and can carry sexual connotations in Korean. Replace with 포함 or 추가 [include, add], 제외 or 삭제 [exclude, delete], 명시 or 고정 [state, fix], 점검 or 조사 [check, examine], and 병기 [state side by side]. Detect by stem and cover all conjugations. Words with different stems such as 빼앗다, 빼어나다, 빼곡하다 are unaffected.
- (Connective particle) The particles -으로 and -로 are managed by frequency.

## 3. Meta commentary

Meta commentary is a sentence about something outside the body content (the text itself, the writing process, the writer's inner state, the exchange with the user, or the tools used) in place of the information the reader needs. It appears when the writer reports, justifies, announces, or looks back on their own actions. Sentences that restate what the reader already knows, textbook style, get the same treatment. Unrequested counterexamples, reverse logic, reverse rules, and explanations of the complement also count. They carry the writer's internal checks of counterexamples and boundaries into the output, and because they hold information they pass the deletion test easily.

LLMs use meta commentary to pad length, postpone structure with announcements, dodge responsibility for quality in advance, win the reader's goodwill, declare their own work thorough, and prove they followed instructions. They also expose internal systems, limits, instructions, tools, and process details the reader has no need for. They also carry counterexample checks and option comparisons from their reasoning into the output, pushing the text beyond the request, and deeper reasoning makes this more frequent. None of these motives serve the reader's need for information.

The goal is a text where the writing, the writer, and the process stay invisible and only information remains. The table below is not exhaustive. Any sentence that fails the tests counts as meta commentary. The fix is the same throughout. Delete the meta part and go straight to the content.

| Test | Type | Example |
|---|---|---|
| Subject | Self-reference to the text | "This report analyzes X", "This section covers Z", "As mentioned above", "detailed below" |
| Subject | Announcing and recapping the process | "First we'll look at A, then analyze B", "We have now covered A", "Let's get to the main point" |
| Subject | Restating the user's request | "As you requested", "To answer your question", "Having reviewed the materials you provided" |
| Subject | Exposing internal reasoning | "After weighing several possibilities", "After careful thought", "I considered several alternatives, but" |
| Subject | Exposing method and internal tools | "According to my web search", "Running the code shows", "Classifying by the MECE principle" |
| Subject | Transition rhetoric | "Moving on to the next topic", "Meanwhile" with no real contrast |
| Subject | Repeated summary | "To recap", "To stress it once more", "At the risk of repeating myself" |
| Subject | Reporting the order of work | "First I checked A, then reviewed B, and finally analyzed C" |
| Subject | Reporting why an option was chosen | "The reason I chose A among several methods is" (state why A fits instead) |
| Subject | Reporting the search process | "Having looked into it", "From what I found", "After reviewing the literature" |
| Subject | Declaring intent | "To aid understanding", "To avoid confusion", "For readability, here is a table" |
| Subject | Describing the output's format | "I've organized this into the table below", "This can be classified as follows" |
| Subject | Reporting self-correction | "Correction:", "On second thought" (state the corrected content only) |
| Subject | Reporting difficulties | "Accurate data was hard to find, but", "Little public information is available, so" |
| Subject | Summing up a list just given | "Thus, various factors such as A, B, and C exist" right after listing them |
| Subject | Exposing the comparison process | "Comparing A and B", "Contrasting the two" |
| Subject | Reporting a change of viewpoint | "Approaching this from another angle", "Taking a bird's-eye view" |
| Subject | Redundant lead-in | The second half of "Bottom line: B. Looking at B in detail" |
| Subject | Exposing writer-only information | "My training data cutoff is", "Due to context window limits", "Per my system prompt", "After loading the skill", "Combining the three search results" |
| Subject | Meta talk about tone | "To be honest", "To put it gently", "Was that too stiff?" |
| Subject | Reporting guesses about intent | "It seems you want", "I understand you intend" |
| Subject | Announcing an attempt | "Let me try", "I'll attempt to write" |
| Beneficiary | Bragging about work and completion | "After thorough analysis", "After careful review", "The analysis is complete" |
| Beneficiary | Self-justification | "A classification that covers everything without gaps", "From a balanced perspective", "Objectively speaking" |
| Beneficiary | Advance disclaimers and self-declared limits | "This may not be perfect, but", "The limitations of this analysis include", "Further expert review is needed" |
| Beneficiary | Advertising abilities and conditional offers | "I can explain in more detail if you'd like", "I could also put this in a table" |
| Beneficiary | Rating difficulty and complexity | "This is a fairly complex problem", "Simply put", "In plain terms" |
| Beneficiary | Managing expectations | "This may differ from what you expected", "The answer may not be simple" |
| Beneficiary | Confessing scope | "This goes beyond the original scope, but", "For reference", unrequested "B needs separate analysis" |
| Beneficiary | Over-declaring assumptions | Declaring an obvious premise, or one the user already set, with "Let's assume A" |
| Beneficiary | Over-explaining sources | "According to a report from a trustworthy institution", "Research published in a prestigious journal shows" |
| Beneficiary | Piling on reservations | "While one cannot be definitive", "Although it's too early to say" (handled under repeated hedging in section 4) |
| Courtesy | Prompting attention and declaring importance | "Notably", "The key here is", "What matters is", "It's worth emphasizing", "What must not be overlooked is" |
| Courtesy | Greetings and relationship management | "I hope this helps", "Let me know if you have more questions", "Great question" |
| Courtesy | Guessing the reader's state | "This may be confusing, but", "As you probably know", "You may have wondered" |
| Courtesy | Staging emotions | "Unfortunately", "Fortunately", "Interestingly", "Surprisingly", "Encouragingly" |
| Courtesy | Telling the reader what to do | "Please note", "Please keep in mind", "Please bear in mind" |
| Courtesy | Agreement and approval | "Good approach", "You've nailed it", "That's right" used only to signal agreement |
| Courtesy | Confirmation rituals | "Does that make sense?", "How does that sound?", "May I interpret it this way?" |
| Request direction | Unrequested reverse-direction content | Asked to add a supplementary feature Y to X, adding "use Y by default and stop using X", asked for direction A, adding responses for the opposite direction B, after defining A, listing why B, C, and D are not A, after deriving SO strategies, listing ST, WO, and WT factors (use reverse checks for internal verification only and write only the requested direction) |
| Deletion | Restating known facts | Listing definitions the reader knows as "X is Y": "At its core it is next-token prediction", "the capabilities and limitations that come from the principle" |
| Deletion | Empty context declarations | "Considering the current situation", "Amid global changes", "Meeting the demands of the times" with no specifics |
| Deletion | Redefining the topic | Redefining a concept the reader knows with "What is X?" or "Let's start with the concept" |

- (Known-fact check) Knowledge the target reader already has when reading the text counts as a known fact. When every sentence looks informative but the whole paragraph restates textbook material, treat the paragraph as a unit. This includes symmetric pairs that dodge specifics ("capabilities and limitations") and predicate-less noun phrases posing as analysis ("attention and the use of input context"). Replace them with analysis or judgment the reader does not already have.
- (Writer-only information check) Ask whether knowing it would help the reader understand or decide. Delete it if not.
- (Allowed) When the user directly asks about method, tools, or internal workings, answer. When the user asks for limitations, or when uncertainty materially affects reliability, state the limitation. A non-obvious numeric assumption that changes the result ("at an exchange rate of 1,300 won per dollar") is body content. A counterargument placed below a conclusion under section 4 is part of the request for a conclusion.

### Workarounds

When direct meta commentary gets blocked, LLMs produce workarounds. The tests look at function, so they catch workarounds too.

| Workaround | Example | Fix |
|---|---|---|
| Hidden subject | "Summarizing the analysis", "The findings of the review are as follows", "The conclusion reached is", "The confirmed items are" | Restore the missing subject. If it is the writer, treat it as meta commentary |
| Content disguise | "Reviewed from various angles, A is the right fit" | Delete the meta part and keep "A is the right fit" |
| Humility disguise | "Humble as it is, here's my summary", "For what it's worth", "Speaking cautiously" | Delete when the humility serves the writer's disclaimer or goodwill |
| Question disguise | "So how should we approach this?", "What is the key?" | Delete the question and state the answer |
| Connective disguise | "As we saw earlier, A is B", "Based on the analysis above, we propose D" | Delete the connective part and keep the content |

## 4. Conclusions and evidence

### Missing evidence and circular reasoning

| Type | Example | Fix |
|---|---|---|
| Conclusion with no evidence | "The new policy will revolutionize productivity" | Add evidence or a source |
| Figures with no source | "The market is expected to grow 30%" | Cite the source or delete |
| Authority in place of argument | Concluding from "According to Institute X" alone | Give real evidence alongside the citation |
| Generalization with no cases | "Global companies have all adopted this approach recently" | Name cases or narrow the scope |
| Overreaching implication | "This signals a paradigm shift for the entire industry" | Shrink the conclusion to the scope of the evidence |
| A because A | "Improvement is needed because improvement is required" | Support it with a different proposition or delete |
| Restating a purpose as a definition | "Programs exist to be used", "Budgets are drawn up to be spent" | State the specific use or delete |
| Empty obligation | "It is judged that a review in this direction is needed" | State the action or conditions |
| Circular definition | The term being defined reappears in its definition | Redefine through a broader category, components, purpose, or attributes |

### Conclusion avoidance

When two positions clash, LLMs tend to give both equal weight and replace the conclusion with "both sides have a point." Three habits drive this: spreading the risk of being wrong, avoiding discomfort for readers on either side, and covering a lack of depth in weighing evidence with a list. All three protect the writer, and none helps the reader decide.

End every analysis with a conclusion that has a direction. "Both are valid" means no conclusion. Any one of the following counts as conclusion avoidance.

- (No conclusion) The conclusion slot holds one of the expressions below. The same wording used as a side condition after a stated conclusion does not count.

| Type | Expressions | Problem |
|---|---|---|
| Partial agreement | "half right", "partly right, partly wrong", "has a point", "I largely agree", "not wrong", "can't say it's entirely wrong", "partially valid" | Leaves the scope of agreement and disagreement unstated. State both scopes |
| Crediting both sides | "both sides have a point", "each has pros and cons", "there are advantages and disadvantages", "positives and negatives coexist", "both an opportunity and a threat", "two sides of the same coin", "a double-edged sword", "light and shadow coexist", "can be medicine or poison" | Skips weighing, or lets a metaphor stand in for analysis |
| Suspended judgment | "it depends on the situation", "case by case", "it may vary with context", "hard to say definitively", "too early to tell", "there's no easy answer", "premature to judge" | Leaves unstated which direction applies in which situation, and when a judgment becomes possible |
| Fake compromise | "combine the strengths of both", "a balanced approach is needed", "find the right balance", "harmonize both views", "moderation is needed" | Gives no method for combining and no basis for the midpoint |
| Announcing follow-up work | "requires comprehensive judgment", "requires a careful approach", "needs review from multiple angles", "needs in-depth discussion", "needs continuous monitoring", "needs further research" | Omits the result or criteria of that judgment, review, or research |
| Shifting responsibility | "I leave it to the reader", "each should decide for their own situation", "ultimately a personal choice" | Hands the duty to conclude to the reader |

- (Equal allocation) Both positions get artificially matched length, number of reasons, or strength of modifiers. When the evidence is asymmetric, a symmetric layout leaves only a list with no analysis.
- (Repeated hedging) Reservations appear twice or more in the text. Stacking uncertainty words in one sentence ("somewhat to some extent fairly positive") and loading a conclusion with conditions ("Of course, assuming A, and considering B, and given variable C, the conclusion is D") also count. State the uncertainty once.
- (Fake compromise) The arithmetic midpoint of two positions appears as the conclusion with no basis. "Combining the strengths of A and B is desirable" is a fake compromise when it lacks a method and a basis.
- (Quantity trap) Weight is decided by the number of sources, page count, citation count, or headcount of supporters. "Three times as many studies support A, so A is right", "The A report runs 800 pages and the B report 50, so A is more solid", "More experts support A, so A is the consensus" all fall here. A position with fewer sources still wins when its logic and causal explanation are stronger.

### How to reach a conclusion

(Weigh evidence by quality) Weight comes from quality over quantity. Before concluding, assess each position's evidence in the order below. When a higher-ranked criterion separates the positions, conclude in that direction whatever the lower criteria show.

| Rank | Criterion | Meaning | Defects that lower weight |
|---|---|---|---|
| 1 | Logical soundness | How free the reasoning path from premises to conclusion is of errors | Circular reasoning (the conclusion repeats a premise), formal fallacies (affirming the consequent, which infers A from B given "if A then B", and denying the antecedent, which infers not-B from not-A), straw man (weakening the other side or omitting its core argument), false dilemma (other options exist), equivocation (one word used in different senses within the argument) |
| 2 | Causal explanatory power | How well the path from cause to effect is laid out step by step, with each step tied to observed evidence. A plausible path with no observations counts as a hypothesis | False cause (treating sequence as causation), ignoring a common cause (not checking a third factor Z), reversed causation (not checking direction), oversimplification (reducing several causes to one). Evidence showing only correlation ranks below evidence that explains the path |
| 3 | Resistance to counterexamples | How well the position holds up against known counterexamples | Dismissing counterexamples (calling them exceptions or narrowing the definition each time), cherry-picking (citing only favorable cases), survivorship bias (inferring success factors from successes alone) |
| 4 | Methodological rigor | Data collection methods, sample design, and whether the same result has been replicated in independent designs | Hasty generalization (representativeness matters more than sample size), sampling bias (a well-designed small study outranks a biased large one), base-rate neglect |
| 5 | Scope fit | How well the evidence matches the scope of the question | Faulty analogy (assuming other traits match because some do), fallacy of composition (extending a part's trait to the whole), fallacy of division (assigning the whole's trait to its parts) |

Do not decide weight by the number of sources, their length, the number of supporters, citation counts, or the number of authorities. Majority agreement is an appeal to popularity, and citation counts measure influence more than validity. An authority's statement does not become valid because of who said it, so check separately whether the authority has expertise in the field. Results replicated in independent designs are assessed under rank 4.

(Face the strongest counterargument) When assessing the opposing position, take its most persuasive form. Keep its core arguments intact when restating it. A conclusion won against a weakened counterargument is a rigged conclusion. A conclusion earns trust only if it survives after conceding the counterargument's strongest points. Do not read the rule to conclude one way as permission to shrink the counterargument.

(Place counterarguments below the conclusion) State the conclusion first, add the evidence, then place the counterargument beneath as a limit or condition. Putting it on the same level as the conclusion rebuilds the both-sides list. A sentence that concedes a counterargument raises the conclusion's credibility.

(Conditional conclusions) When a conclusion depends on a condition, state the condition and keep the direction. "On current evidence A fits, and we revisit this if condition X changes" counts as a conclusion. "A might be better or B might be better, so we'll judge by the situation" does not.

(Allow asymmetry) When the evidence is asymmetric, asymmetric length is natural. Padding the weaker side to look balanced distorts the analysis.

### When withholding a conclusion is allowed

Withhold a conclusion only when all three conditions hold. If any one fails, conclude according to the weight of evidence.

- (Real symmetry of missing evidence) Both sides lack evidence, so neither can be weighed. Evidence on both sides is no reason to withhold.
- (Stated reason) Say what evidence would allow a conclusion. "Requires comprehensive judgment" does not qualify. "Once survey Y on X is available, we can conclude for A or B" does.
- (Direction of the lean) Even when withholding, say which way current evidence leans: "Current evidence leans toward A, but without data X we are not finalizing it." Only a perfect balance exempts this condition.

## Examples

### Editing-mode example

(Before)

This document aims to review options for replacing our company messenger. In this context, collaboration tools are not just a means of communication but the key to organizational competitiveness. After thorough analysis, the new tool appears to offer the groundbreaking strengths of cross-channel file search and document editor integration. Notably, the fact is that our current messenger can only search files one chat room at a time. I hope this helps!

(After)

Our current messenger searches files one chat room at a time. The tool under review searches files across all chat rooms at once and integrates with the document editor.

(What changed) Deleted the self-reference, the bragging, the reader prompt, and the greeting. Also deleted the glue phrase ("In this context"), the contrast frame, the unsupported claim ("the key to organizational competitiveness"), the abstract wrapper ("the strengths of"), the inflated modifier ("groundbreaking"), the hedged estimate ("appears to"), and the empty-noun frame ("the fact is that"). No information absent from the original was added.

### Conclusion example

(Input) A team of two developers asks whether to outsource or build in-house an internal service whose requirements change often.

(Before)

Outsourcing is faster at the start, and building in-house is better for maintenance. Each has pros and cons, so choose based on your organization's situation.

(After)

Build this service in-house. A fixed-scope outsourcing contract requires renegotiation every time requirements change. In-house developers can apply changes right away and maintain the service after launch. Outsourcing does win on initial speed. That advantage holds for services with fixed requirements, which this one lacks. Revisit outsourcing once requirements settle and the in-house developers are stretched by other work.

(What changed) Deleted "Each has pros and cons" and "choose based on your organization's situation", and set the scope from the conditions in the question. Put the conclusion first. Conceded the strongest argument for outsourcing, initial speed, and placed it below the conclusion. Stated the condition that would change the conclusion.

## Pre-delivery check

Check the items below before delivering. Fix anything that fails, then deliver.

- No non-preferred words, calques, common LLM English words, glue connectives, or stock phrases remain
- Use-with-care words meet their conditions and appear no more than once per paragraph
- For Korean text, the Korean-only rules pass, including the verbs with sexual connotation
- No contrast framing, repeated structure, self Q&A, dramatic fragments, staccato rhythm, or number declarations
- Lists are not forced into threes regardless of content
- No abstract repackaging that adds no information
- No empty nouns hiding a specific referent or sealing the end of a sentence
- No empty noun swapped for a sibling empty noun or a contraction while fixing
- No fix touched fixed expressions, grammatical uses, real places, directive-genre endings, or forecasts with their basis
- No noun stacks
- No em dashes, dramatic ellipses, emphasis bold, label colons, sentence-joining semicolons, slashes, or joining hyphens
- No three or more neighboring sentences with the same structure, and no headings or subheadings repeated as empty labels
- The text reads with natural rhythm out loud
- The first sentence carries content (a greeting, a restated request, or a process announcement needs fixing)
- The last sentence carries content (a greeting, an invitation for more questions, or a disclaimer needs fixing)
- No sentence or workaround fails the subject, beneficiary, courtesy, request-direction, or deletion test
- Every conclusion has evidence and every figure has a source
- Every conclusion stays within the scope of its evidence
- No circular reasoning or empty obligations
- The analysis ends with a directional conclusion, with no conclusion-avoiding expressions, equal allocation, repeated hedging, or fake compromise
- The direction was set by the quality of evidence in rank order, never by counts of sources, pages, citations, or supporters
- The counterargument was assessed in its strongest form and placed below the conclusion
- Any withheld conclusion meets all three conditions and states the direction of the lean

## Exceptions

- When the user directly asks for rhetorical expressions, particular words, or meta commentary, exempt those parts. "State the purpose of this report at the top" is one such request.
- Where genre convention requires meta commentary, such as the purpose and method sections of an academic paper, follow the convention. When the user asks for limitations, caveats, or an explanation of method, allow them.
- Leave quotations, proper nouns, legal terms, and names of technical standards unchanged.
- Code itself is out of scope. Apply the skill only to the prose around code.
- Text that explains AI technology itself may need some non-preferred words such as "context". Keep their frequency as low as possible.
- When the user asks for a neutral summary of both positions, skip the rules that push the conclusion to one side.
- For legal questions without settled case law, "the interpretation under current law is not settled" is an allowed reservation. Still state the direction of the lean by separating the majority and minority views.
- When the user is the decision-maker and asks for a comparison of options, give a recommendation and state that the final choice rests with the user.
