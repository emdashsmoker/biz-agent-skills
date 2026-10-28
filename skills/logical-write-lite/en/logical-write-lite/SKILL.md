---
name: logical-write-lite
description: "Skill for Korean-style bullet-point report writing (gaejosik), translated from the Korean edition. It applies Markdown hierarchy (#, ##, -, +, quote blocks), conclusion-first order, single-criterion classification, one message per unit and per sentence, each 5W1H element used once, nominal endings, evidence and source notation, directional conclusions, jargon handling, and removal of meta commentary and AI cliches. Short-sentence mode with no connectives is the default. Flow mode, which allows connectives and subordinate clauses, applies when the user asks for flowing prose. Use it to write, revise, or diagnose reports, plans, proposals, policy or business analyses, research summaries, and environment-to-strategy documents. Always use this skill when the user asks for '/logical-write-lite', 'bullet-point report style', 'nominal endings', 'conclusion first', 'build the storyline', 'make it flow', 'style edit', 'structure review', or 'logic review'. Do not use it for fiction, essays, or conversational writing."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# logical-write-lite

> This is an English translation of the Korean edition of logical-write-lite. The translation may not work exactly as the original intends. Rules that target Korean grammar and vocabulary (nominal endings, particles, the dependent noun 것, Japanese-influenced phrasing, Korean word lists) keep the Korean terms with English glosses. When writing in another language, apply the purpose each rule states.

This skill writes and revises gaejosik text in Markdown hierarchy. Gaejosik is the Korean report style of short itemized statements that end in nouns. The skill puts the conclusion first, groups evidence by one criterion, and puts one message in each sentence. Use it for reports, plans, proposals, and analysis memos that a reader must read and then decide on.

## 1. How it works

### Work types
| Type | Example request | Output |
|------|-----------------|--------|
| Write | A request for new text | The finished text only |
| Revise | A request to fix existing text | The revised text first, then a summary of about three lines listing the types of fixes and where they occur. No completion reports such as "I have revised it" |
| Diagnose | A request to review structure or logic | Pass or fail for each item of the Chapter 17 checklist, the location of each problem, and the fix direction (revised text only on request) |

### Short-sentence mode and flow mode
The two modes differ only in whether connectives and subordinate clauses are allowed. All other rules are the same.
- Short-sentence mode is the default. Split sentences and do not join clauses with connectives (Chapter 8).
- When the user asks for flow, with phrases such as "make it flow", "narrative style", "connect the sentences", "give it a storyline", or "tell it like a story", write in flow mode (Chapter 9).
- When the user asks for "short sentences", "break it up", or "strict bullet style", return to short-sentence mode.
- Keep the chosen mode for the rest of the conversation until the user asks to change it. Do not ask the user which mode to use.

### Priority and non-disclosure
- Format, skeleton, classification criteria, order, and terms the user specifies take priority over this skill. If a user instruction has a structural flaw, follow the instruction and point out the flaw in one line.
- The rules of this skill work only inside the writing process. The output never shows rule names, framework names (SCQA, MECE, 5W1H, and so on), the fact that rules were applied, or an evaluation of the text itself.
- Diagnosis reports also describe the problem in place of framework names. Example: "The conclusion is missing from the opening."

## 2. Terms
| Term | Meaning in this skill |
|------|-----------------------|
| Unit | A block the reader sees and absorbs at once: one paragraph, one bullet group, one table, one slide, one chart |
| Message | The one judgment sentence the reader should remember from a unit. A claim with a subject and a predicate |
| Level | A layer of the text marked with Markdown: title (#), section (##), bullet (-), sub-bullet (+) |
| Group | Items on the same level under the same parent item |
| Subtitle | A short name in parentheses at the start of a bullet sentence. Example: (Investment structure reform) |
| Connective | A word or ending that joins two clauses or sentences: and, but, which, Korean -으며, and so on |
| Subordinate clause | A clause attached to the main clause that adds a cause, condition, scope, or means |
| 5W1H element | Who, when, where, what, why, how |
| Evidence | A fact, source, or inference that gives a reason to accept a claim |
| Quantitative data | Facts expressed in numbers, such as figures, ratios, amounts, and counts |

## 3. Thinking order before writing
Think in this order before writing any sentence. Move from large units to small ones.
1. (Why requested) Infer why the user asked for this text, who the reader is, and what decision the reader must make after reading. Look past the literal wording of the request.
2. (Definitions, criteria, scope) Fix the definitions of key terms, the criteria for judgment, and the scope. Keep each definition and criterion unchanged and unmixed to the end of the text.
3. (Question premises) Use first-principles thinking. Check the user's request, your own knowledge, common beliefs, authorities, famous frameworks, and buzzwords against facts before accepting them. Trace problems by repeating "why" until no deeper cause remains.
4. (Conclusion) State the conclusion of the whole text in one sentence.
5. (Skeleton and headers) Choose a skeleton from Chapter 4 and name the headers first. The flow should be visible from the headers alone.
6. (Units and elements) Set one message per unit and choose the elements that support it (Chapter 5).
7. (Sentences) Write with the rules in Chapters 6 through 16.
8. (Check) Run the Chapter 17 checklist and review the header names once more.

Avoid these ways of thinking while you work.
- Mechanical thinking detached from facts on the ground. Examples: models that stack elaborate form on unverified assumptions, imitation that copies only the surface of leading cases, and defensive logic that stops at formality and delivers no results.
- A view that only counts costs, and an inflated promotional view.
- Empty wordplay. Text has meaning only when a third party can read it and accept its reasoning as valid.

## 4. Document skeleton

### Put the conclusion first
- Compress the conclusion of the whole text into the document title or the first section. Do not fill the first section with topic introductions or source guides.
- For skeletons that start with the situation (SCQA, SCR), put the conclusion in the document title as a proposition. Example: `# Supply chain sites need to be dispersed`
- Put each section's conclusion in its first sentence. Do not hold the conclusion back and leave the reader to infer it.

### Choose one skeleton
Choose one skeleton that fits the purpose of the text and do not mix skeletons in one text. If the user specifies a skeleton, follow it. Ask the user about the purpose only when the request and materials do not reveal it.

| Skeleton | Flow | Fits |
|----------|------|------|
| SCQA | Situation, complication (the change that disturbed the situation), question, answer | Analysis reports that give a decision maker an answer |
| WWH | Why it is needed, what to do, how to do it | Proposals and recommendations that ask for action |
| SCR | Situation, problem or change, resolution | Improvement plans after diagnosis, and implications and outlooks after environment analysis or internal diagnosis |

### Documents that run from environment analysis to strategy
Order the sections from the external environment inward to the organization, then forward to strategy and execution. Treat this order as a concrete form of the SCR skeleton. The analysis stages and implications cover the situation and the problem, and strategy and the implementation plan cover the resolution.

| Order | Stage | Content |
|-------|-------|---------|
| 1 | Macro environment | External changes and trends the target organization cannot control. Only the items the topic needs among policy, economy, society, technology, environment, and law |
| 2 | Micro environment | Industry, market, competition, customers, and supply chain that interact with the target organization |
| 3 | Internal status | The target organization's capabilities, resources, and operations |
| 4 | Benchmarking | Experience of similar organizations and precedent cases |
| 5 | Strategy | Direction, goals, and strategic options |
| 6 | Implementation plan | Tasks, schedule, and resource allocation |

- Choose stages by purpose. Trend scanning uses stage 1 (add stage 2 if needed), status diagnosis uses stages 1-3, direction setting uses stages 1-3 and stage 5, and strategy development uses all of stages 1-6.
- Keep the chosen stages in the order of the table. Skipping a middle stage is fine. Reversing the order is not used.
- Analysis stages (1-4) contain facts only. Interpretation and outlook go into implications, and solutions and target states go into the strategy stage. The strategy stage does not repeat the analysis.
- An environment the target organization cannot influence is macro, and one it interacts with is micro. Choose classification items and their order to fit the topic, and do not list unrelated items to fill a framework. Frameworks also differ in order (PEST runs political, economic, social, technological; STEEP runs social, technological, economic, environmental, political).
- Internal status covers both strengths and weaknesses and shows the gap between industry requirements found in the micro environment and internal capabilities. An organization profile (history, organization chart, budget, staff) may come before the environment analysis. A capability diagnosis comes after it.
- Benchmarking states why each case was chosen, its similarities to and differences from the target organization, and both success and failure factors, and produces implications that connect to the earlier diagnosis.
- Draw the evidence for strategy only from the earlier analysis stages, and choose derivation tools to fit the purpose. Implementation tasks derive from the strategy, and tasks unrelated to the strategy are left out.
- An implication is a sentence that compresses the meaning of analyzed facts by induction. Put implications at the end of each stage or gather them in one section after the analysis. Do not jump from analysis to strategy without implications. In a text without a strategy stage, the implications are the conclusion. Implications from macro and micro facts are external factors (opportunities, threats), and those from internal status are internal factors (strengths, weaknesses).
- Each stage narrows the focus of the next. Tracing back from tasks to strategy, strategy to analysis, internal to micro, and micro to macro, the evidence must remain visible. Add evidence for any element whose basis is not visible, or delete it.
- Reflect every fact in at least one implication. When a strategy stage exists, reflect every implication in at least one strategy. Delete items that are not reflected.
- When covering both global and domestic trends, write the global trend first and then the domestic trend within each classification item (for example, policy trends), and show how the two relate (influence, response, gap). Section titles use keywords that carry content in place of stage names such as "macro environment" or "internal status".

## 5. Units and bullets

### Markdown hierarchy
```
# Document title
## Section title
- Claim (no indent)
    + Evidence or elaboration for the claim (4-space indent)
> (Data name) Description of supporting data, or a source
```

- `+` marks sub-bullets only. `>` is only for data, sources, and term explanations.
- The #, ##, ### levels can shift depending on whether the document stands alone or sits inside a larger one. Keep the relative relation between levels.
- Moving down the levels, abstraction decreases and specificity increases.

### Headers
- Name the headers first and set the flow between them. Check them again right before output. Name each header so the reader can tell the content below from the header alone.
- One header holds one topic. Do not bundle two topics as in "Policy and technology trends", "A and B", or "A/B". Split the header.
- Choose keyword headers (example: Policy trends) or sentence headers (example: Supply chain sites need to be dispersed) and keep one type throughout the text.
- Do not repeat generic labels unrelated to content, such as "Overview", "Background", "Status", "Conclusion". If the user specifies a template, follow it.
- Name sibling headers with the same pattern and keep their length and information density similar. Example: "Global market trends" and "Regional market trends"
- A keyword header announces the subject and the first sentence carries the judgment. A sentence header carries the message and the first sentence starts the evidence. If the header and the first sentence point at different subjects, rename the header or move the content.

### One message per unit
- Each unit has one message. If a unit has two or more messages, split it.
- A message is a judgment sentence. Topic labels such as "Market status" or "Background" are not treated as messages.
- The test question is "What one sentence should a reader remember from this unit?" No answer means the message is missing. Two independent claims joined in the answer mean the unit is overloaded.
- Put the message at the head of the unit. The parent bullet carries it for a bullet group, the first sentence for a paragraph, the title for a table or chart, and the headline for a slide.
- Divide weight inside a unit into three layers: message, supporting elements, and details. Set one point of emphasis. If every element has equal weight, rearrange. In charts and slides, highlight only one target with size, position, and color, and attach data labels only to points related to the message.

### Choosing elements
- By default, a unit has at most 3-4 elements supporting the message. Elements do not overlap, and each covers a different part of the message. People are reported to hold about 3-5 chunks of information at once, and the default of 3-4 stays within that range.
- If two are enough, keep two. Do not add elements to reach a count. Frameworks with a fixed count, such as a four-quadrant matrix or a five-step process, keep their count.
- If five or more seem necessary, first check whether messages are mixed and split the unit. Next, group items under 3-4 higher categories and move details down a level. If items still remain, delete those that do not support the message.
- Compress by choosing and discarding elements. Keeping every element and only shortening sentences leaves the reading load unchanged. Write the kept elements with enough substance.
- Delete in this order: information unrelated to the message, background the reader already knows, evidence that repeats support for the same conclusion, and decorative numbers and cases that do not help the decision.
- Deleting is the default for dropped content. Content with independent message value becomes a new unit, and content with only reference value moves to an appendix or attachment. Do not mention something by name in the body and skip its explanation.
- Restructure when any of these appears: five or more parallel items on one level, two or more independent claims in one paragraph, a title that stays a topic label, no point of emphasis, or elements of different kinds mixed together, such as causes with results or phenomena with remedies.

### Relations between levels
- A parent message is the conclusion of its child messages, and child messages are the evidence for the parent.
- Going down, each child must answer "Why can we say that?" Going up, each parent must answer "So what does this mean?" Move or delete any message that fails either direction.
- Messages on the same level use one grouping method. Do not mix an inductive group (facts of the same kind that lead to a shared conclusion) with a deductive group (a major and minor premise that lead to a conclusion) in one group.
- Each adjacent sentence and bullet plays one role toward the previous content: elaboration, evidence, example, contrast, or conclusion. Do not list facts that have no relation to each other.

### Sub-bullets and subtitles
- Use sub-bullets only when there are two or more parallel items. If only one remains, merge it into the parent sentence or promote it to its own bullet. One sub-bullet is fine when the parent is a proper name or framework and the single sub-bullet gives its definition or scope.
- Three to four sub-bullets per bullet is recommended. Avoid counts so small or large that the rhythm breaks.
- Wrap subtitles in parentheses. Write `- (Investment structure reform) Gradual increase in the share of basic research`. Do not write `Subtitle : content` or `Subtitle - content`.
- Name subtitles by content. Do not use empty labels such as (Explanation), (Reason), (Claim), (Evidence), (Section 1), and do not repeat the same subtitle.
- Subtitles in one group follow the same classification criterion. (Policy), (Accountability), (Monitoring) fit together because each is an area of work. (Policy gap), (Missing verification), (Collecting department opinions) mix a limitation, an infrastructure issue, and an activity, so they do not fit.
- Within one group, give every item a subtitle or give none. Different groups may differ. Add subtitles only to groups that need them.

### Tables and composition
- Use at most three tables in the whole text. With more tables, it becomes unclear which table matters. When the text grows long, summarize the main points in a table.
- Place a table after a claim. Do not place a table right after another table. Alternating claim, table, claim, table is fine.
- Do not put tables inside `>` blocks or code blocks. Divide rows, columns, and cell text by one criterion so nothing overlaps or is missing.
- Write each section so it reads on its own and fits when combined with other sections. Prefer structures that are easy to edit and delete, and keep the number of paragraphs minimal without overlap.

## 6. Classification
This chapter applies to classifying, grouping, and building tables of contents. It is not enforced when the user asks for a simple list, such as a ranking.
- Before classifying, answer these questions. What decision will this classification support? What is the scope? Is the criterion one-dimensional? Can every case in scope be placed without omission?
- One classification uses a one-dimensional criterion. Do not mix items by technology, by industry, and by urgency on one level. With several criteria, split into a first and second classification. Choose one axis among time, process, structure, and causation to fit the purpose.
- Look for counterexamples that fall into two items at once. If items overlap, redraw the boundary or merge them into a higher category. If overlap cannot be avoided, treat it as an attribute (tag) in place of a class and say so.
- Look for cases that fall into no item. If you use "Other", its share must be smaller than the main items. If it is larger, rebuild the criterion.
- Three to four items per level is recommended. With five or more, check whether a middle level is missing. With two, check that splitting into two options is valid (false dilemma). Established systems such as biological taxonomy, industry classification codes, and articles of law are not flawed for having many items.
- Distinguish the kinds of hierarchical relation and do not mix them on one level: kind-of (an electric car is a kind of car), part-of (a battery is part of an electric car), and has-a (a budget is an attribute of a project). In a kind-of relation, the attributes of the parent must hold for the child.
- Three levels of hierarchy is recommended. With four or more, check whether the middle levels are needed. Systems that are deep by nature, such as administrative districts, are exceptions.
- Recheck the placement of any item with no relation to other items. If isolation is justified, as with a new area or an exception, state why. Delete categories with no cases, and if they will be filled later, state the basis.
- When adding an item to an existing classification, state its relation to existing items (parent, child, parallel, dependent, sequential). If the new item belongs to a different axis, as when "urgent" is added to a short-term, mid-term, long-term classification, split it onto its own axis or attach it as an attribute of existing items.
- Do not change a real-world classification because it is easier to chart or fits a framework better. Understand the real structure first, then decide how to present it, and do not mix facts and judgments in one classification.

## 7. Common sentence rules
These rules apply equally to short-sentence mode and flow mode.

### One message per sentence
- Each sentence carries one message. Split two independent contents into two sentences or two bullets.
- Within one sentence, each 5W1H element appears once. The same element appearing twice signals that two messages are mixed. Where possible, include why, what, and how in each sentence.
- Judge in this order. Find the 5W1H elements in the sentence. Check whether any element appears twice or more. If so, split the sentence at the element boundary. Check again that each new sentence has why, what, and how.
- When splitting, keep the 5W1H information each sentence needs. Do not write fragments of two or three words.

```
(Before) The government expanded the R&D budget and reformed the evaluation system to improve the research environment and raise performance
(After)
- Government to expand the R&D budget in stages to improve the research environment
- Government to reform the performance evaluation system to raise research performance
```

### Endings and notation
- End sentences in nominal form. Korean examples: -임, -함, -필요 (needed), -전망 (expected), -예정 (planned), -확인 (confirmed), -추진 (pursued). In English, the equivalent is a verbless phrase such as "Review required" or "Rollout planned".
- Do not use verbal endings (Korean -한다, -된다) or honorific endings (Korean -합니다, -입니다). Quotations, legal texts, and original definitions keep their original form.
- Keep nominal endings natural. Drop leftover adnominal verb forms: write 달성 필요 (achievement needed), 접근 필요, 내장 필요 in place of 달성할 필요, 접근할 필요, 내장시킬 필요. Untangle clumped phrases: rewrite 목차명에는 키워드 기반 재구성으로 반영 as 목차명은 키워드 기반으로 재구성 (table of contents names rebuilt around keywords). Keep an adnominal form when the verb limits its object, as in 삭제할 파일 (files to delete).
- Do not close a sentence awkwardly with words such as 구조 (structure), 우선 (priority), 결론 (conclusion), -것, -곳.
- Do not write sentences made only of stacked nouns. Restore particles and endings: 디지털 산업 집적 지표 becomes 디지털 산업의 집적도 (the concentration of the digital industry), and 온전 세트 becomes 온전한 세트 (a complete set).
- Do not write ungrammatical sentences: dropped particles, broken subject and predicate agreement, or unclear modification targets.
- Do not put a period at the end of a sentence. The Korean punctuation rules allow omitting the period after sentences that end in a noun.
- Do not use the tilde (`~`), since Markdown may render it as strikethrough. Write ranges with a hyphen. Example: 3-5 years
- Add thousands separators and units to numbers. Example: 1,000,000 or 1 million. Use only symbols that can be typed on a standard keyboard.

### Rhythm
- Write so the text sounds natural when read aloud. Do not mechanically repeat sentence length, sub-bullet count, subject, predicate, or ending, and when three or more adjacent sentences share one structure, change one.

## 8. Short-sentence mode
This is the default mode. Connectives easily become a path for putting one 5W1H element into a sentence twice, so split the sentence at those points.
- Do not use connectives such as and, but, so, therefore, because of this, which, or the Korean clause-joining endings -으며, -있으며, -이며. Split the sentence or rebuild it in nominal form.
- Means or cause markers (Korean -하여, -으로; English "by", "through", "due to") are allowed as long as how or why appears only once in the sentence.
- Use commas only to list three or more items of the same category. Join two items with "A and B" in place of a comma. In Korean output, join two parallel nouns with 및 in place of 와 or 과 ("예산과 인력 확보" becomes "예산 및 인력 확보"). Keep 와 or 과 when it marks a relation between two nouns (사이, 간, 격차, 차이, 일치, 불일치, 연계, 연동, 정렬, 비교, 구분, 분리, 협력, as in "현행과 기준의 격차") or the partner of an action (as in "유관기관과 공유"), or when it belongs to an established term, such as "학습과 성장" in the BSC. Do not use commas to join sentences, insert phrases, or add asides.
- Do not just delete a comma and leave the sentence as it was. "The government expanded the budget, and as a result the research environment improved" becomes "Government to expand the R&D budget in stages" and "Research environment improvement expected from the budget expansion".
- Always keep the commas in a list of three or more. Do not list with spaces only, as in "public industry research sectors". Write "public, industry, and research sectors".

## 9. Flow mode
Use this mode when the user asks for flowing prose. It lifts only the connective restriction of short-sentence mode and keeps every other rule. Flow comes from bullet order and causal logic more than from the number of connectives.
- Use subordinate clauses only to reinforce the main message. The allowed roles are cause (a cause or a result), condition (when the message holds), specification (scope or example), and means (how the result is achieved).
- A sentence has one subject and predicate frame. Subordinate clauses hang from that frame. Added clauses must not blur the main subject and predicate, and the sentence must read in one breath.
- A subordinate clause must not bring in a 5W1H element that the main message already has. If two of the same element are needed, merge them into one causal chain or split the sentence. Split two facts that are only parallel.
- Do not stack clause joints (Korean -며, -고, -면서, -으나; English "and", "while", "but") in one sentence. Do not repeat the same connective. When the flow is already natural, end without a connective.
- Allowed connectives are causal (accordingly, therefore, through this), additive (also, at the same time, in addition), contrastive (however, whereas, unlike this), temporal (recently, going forward, afterward, previously), and referential (this, the said). Allowed subordinate endings are Korean -으며, -으나, -함에 따라, -함으로써, -할 경우 (while, although, as, by, if).
- Choose one paragraph flow to fit the purpose: change flow (previous state, driver of change, new pattern, implication), problem flow (status, limitation, alternative, expected effect), or diffusion flow (emergence, spread, application cases, outlook).
- In this mode, do not write text where every sentence is chopped short, text with every connective removed so causation breaks, run-on text that ties several independent messages together with subordinate clauses, or colloquial text written in the name of storytelling.

```
(Two parallel causes) Adoption delayed by budget limits and staffing gaps
(One causal chain) Adoption delayed as budget limits slowed staff recruitment
```

## 10. Logic and evidence

### Claims and evidence
- Every claim pairs a conclusion with evidence. Do not declare conclusions without evidence or list evidence without a conclusion.
- Do not stop at the surface reason. Ask "why" repeatedly and go down to the root cause.
- The scope of the conclusion does not exceed the scope of the evidence. If the conclusion becomes too narrow to support a decision, strengthen the evidence.
- The burden of proof lies with the party making the claim. Write claims in a falsifiable form. Form hypotheses before gathering data and revise them when counterevidence appears.
- Do not use authority in place of evidence. The name of an institution or expert only marks the source, and the evidence is the content of that source. Check that the cited authority has expertise in the relevant field.
- Do not mix fact and judgment in one sentence. State unknown information as unknown.
- Do not treat missing information as evidence of absence. Distinguish "not confirmed" from "does not exist". Write "none" only within a scope that was fully surveyed, and state that scope.
- State the type and direction of each relation. For causation, confirm order and mechanism. For correlation, do not assert causation. For dependence, state which side cannot exist without the other. For association, state its specific nature. Do not lump relations together as "related". Give separate evidence for each direction of a two-way relation, and when needed state whether it is 1:1, 1:N, or N:M and whether it is required.
- Do not reuse the defined word in its definition. Define by parent concept, components, purpose, or attributes. "Digital transformation is the activity of transforming with digital technology" is circular. "The activity of redesigning existing work procedures on a software basis to raise operating efficiency" is not.
- Do not write tautologies (improvement is needed, so improvement is needed), restated purposes (a budget is drawn up to be spent), or empty obligations (a review is judged necessary). Replace them with specific evidence, uses, or actions.

### Fallacy check
| Family | Check question | Typical fallacies |
|--------|----------------|-------------------|
| Formal | If the premises are true, must the conclusion follow? | Denying the antecedent, affirming the consequent, treating the converse or inverse as true, affirming a disjunct, undistributed middle, a syllogism that uses one word in two senses, confusing possibility with necessity |
| Speaker and circumstance | Does it lean on people, numbers, emotion, or power in place of content? | Authority from another field, anonymous, or with a conflict of interest; ad hominem; tu quoque; judging by affiliation or camp; appeal to pity, threat, wealth, or the majority; mechanical middle ground; ridicule; tone policing; judging only by origin |
| Meaning | Is each word used in one sense, and is the opposing claim restated as it was? | Equivocation, vague reference, confusing a word with its referent, covert redefinition, claiming existence by naming, distortion by emphasis, straw man, quoting out of context, treating a metaphor as fact, emotionally loaded modifiers |
| Causal | Does it avoid treating sequence or correlation as cause? | False cause, ignoring a common cause, reversed causation, reducing to a single cause, false analogy, false equivalence, gambler's fallacy, overrating joint probability, ignoring base rates, confusing means and ends, exaggerating intent |
| Generalization and category | Can the sample and category carry the conclusion? | Hasty generalization, biased sample, stretching "most" to "all", mechanical use of a general rule, mixing principles from different situations, confusing part and whole, judging an average by the top case, dismissing counterexamples as "not the real thing", distinguishing the same meaning by different words, category error |
| Issue | Does it stay on topic and leave room for rebuttal? | Red herring, a conclusion other than what the premises support, poisoning the well, argument from ignorance, rejecting something as hard to understand, slippery slope, false dilemma, demanding a perfect solution, loaded question, double standard, removing the issue in place of the problem, repeating the same question |
| Value and fact | Does it avoid deriving ought from is, or fact from wish? | Naturalistic fallacy, moralistic fallacy, appeal to novelty, appeal to tradition, wishful thinking, conclusions beyond a hypothetical's scope, adding ad hoc assumptions after each rebuttal |
| Circular | Is the conclusion hidden inside a premise? | Begging the question, tautology, circular definition, using an error in the opposing argument as proof that its conclusion is false |
| Cognitive bias | Was counterevidence looked for? | Confirmation bias, cherry picking, availability, representativeness, survivorship bias, halo effect, anchoring, favoring what is close, beliefs hardening against counterevidence, selection bias, out-group homogeneity, rosy retrospection |

## 11. Reaching a conclusion
End an analysis with a conclusion that has a direction. Text that lays out both sides equally protects the writer from being wrong or from annoying readers on the other side, and it does not help the reader decide. "Both sides have a point" is an empty conclusion. When the user asks for a summary of both positions or a neutral summary, this chapter's requirement to conclude does not apply.
- Weigh evidence by quality. Do not count the number of pieces of evidence, their length, citation counts, the number of people who agree, or the number of authorities when weighing.
- Assess quality in the order below. If one side wins on a higher criterion, follow that criterion regardless of lower ones.

| Order | Criterion | Question |
|-------|-----------|----------|
| 1 | Logical soundness | Is the reasoning from premises to conclusion free of fallacies? (Chapter 10 fallacy check) |
| 2 | Causal explanation | Does it explain the mechanism of why, in concrete terms? |
| 3 | Resistance to counterexamples | Does it withstand known counterexamples without dismissing them as exceptions or picking only favorable cases? |
| 4 | Methodological rigor | Are the sample design, representativeness, and base rates handled properly? |
| 5 | Scope fit | Does the evidence match the scope under discussion? |

- Rebuild the opposing view in its strongest form before assessing it. A conclusion that beats a weakened version without its key arguments cannot be trusted. The requirement to conclude does not permit shrinking the opposing view.
- Place counterarguments under the conclusion. Placing them on the same level as the conclusion blurs it.

```
- Cloud deployment suited to new business systems at companies with fewer than 100 employees
    + Small upfront equipment investment eases the financial burden on companies with limited capital
    + Outsourced operation a practical option where in-house operations staff are scarce
    + Data control concerns reducible by choosing certified services hosted in domestic data centers
    + Hybrid setup with on-premises equipment to be considered for industries where data location is restricted by law
```

- A conditional conclusion is a conclusion. Write, for example, "On current evidence A fits, and the choice needs review if condition X changes." Do not write reservations without direction ("decide depending on the situation").
- When the evidence leans one way, the text may lean too. Do not pad the weaker side to balance length.
- Do not put the expressions below in the place of the conclusion. They are fine as side conditions after the conclusion is stated.
- (Partial agreement) half right, has a point, not wrong, partly valid
- (Both-sides acknowledgment) each has pros and cons, a double-edged sword, both opportunity and crisis, two sides of the same coin
- (Suspended judgment) it depends on the situation, hard to say for sure, too early to tell
- (False compromise) a balanced approach is needed, combine the strengths of both, the right balance
- (Evasive ending) comprehensive judgment needed, careful approach needed, continuous monitoring needed, further research needed
- (Shifting responsibility) left to the reader's judgment, decide according to your own situation
- Deliberately matching the length and modifier strength of two positions, using reservations twice or more, or presenting the midpoint of two positions as the conclusion without evidence counts as avoiding a conclusion.
- Withhold a conclusion only when all of these conditions hold: evidence on both sides is equally lacking; the text states which evidence, once secured, would allow a conclusion; and it states which way the current evidence leans.
- For legal issues without settled case law, reserving judgment as "interpretation under current law is not settled" is allowed. Even then, separate the majority and minority views and state the trend.
- When the person asking for a comparison of options is the decision maker, present a recommendation and state that the final choice rests with that person.
- Neutrality means perceiving facts neutrally. State the conclusion clearly without speaking for a middle position, setting up straw men, or making leaps and aggressive assertions.

## 12. Quantitative data and sources
- Use quantitative data only when who surveyed it, when, how, and the calculation basis are clear. When a third party asks for the basis, the answer must cover the 5W1H.

```
- (Do not write) The AI application services market is expected to grow N% per year
- (Write) According to A Research's 2025 survey, the AI application services market is expected to grow about N% per year, from B won in 2024 to C won in 2030 (estimated by summing company revenues)
```

- Run calculations such as sums, ratios, and compound annual growth rates with code or a calculator, and recalculate figures from the source to check them. Do not use numbers the model computed in its head.
- Use at most three key quantitative data points in the whole text. With more numbers, it becomes unclear which number matters for the decision.
- Where possible, use time series of three to five years or more, and state the compound annual growth rate and the share of the total. When statistics serve as evidence, state the sample size, sampling method, and representativeness.
- Write sources as `> Institution or author (year), title (link)`. With multiple sources, put a blank line between `>` blocks.
- Put the source once, right below the sentence with quantitative data or right after the data block. Sources for qualitative citations may go at the end of the paragraph or section.
- Write links as full addresses that reach the material directly. Do not leave only the domain.
- Use the official full names of institutions, titles, policies, programs, products, and people as they appear in the source. Do not abbreviate or alter them. Do not invent sources.
- When introducing a document, include its main points so the reader does not need to look up the original.
- Cite primary sources with editorial and verification processes first. These include publications of governments and public bodies, reports of public research institutes, peer-reviewed papers, statistics of international organizations, and official materials of financial institutions and professional research firms. Do not cite personal blogs, wiki articles, anonymous communities, aggregator sites without sources, or auto-generated content. For news reports, find and cite the original source the report used.

## 13. Vocabulary

### Jargon
- The reference reader is an adult professional who did not major in the field. Assume the reader has forgotten most details learned in school. If the user specifies a reader, adjust to that reader.
- First ask whether the reference reader understands the word without a definition. Treat as jargon any word learned only by studying the field, any word that looks like everyday language but has a different meaning in the field ("significant" in statistics, "exposure" in finance), and English abbreviations. Doubt first the words most familiar to the writer.
- Handle jargon in this order. Delete it if it is not needed to deliver the conclusion. Replace it with a plain word if the meaning stays the same ("migration" becomes "move", "pain point" becomes "inconvenience"). If replacing it changes the meaning or blurs the distinction from other things, keep it in the body and attach an explanation block.
- Write the explanation block in one line right after the item where the term first appears, as in `> (Call rate) The interest rate on very short-term funds that banks lend each other for one day`. Do not use other jargon or the defined word inside the explanation. With several blocks, put blank lines between them. Do not defer explanations to an end glossary or footnotes, and do not insert long definitions in parentheses in the body.
- Define each term once, in the body or in an explanation block. When explaining the concept is the purpose of the text, the body carries the definition and no block is added.
- Write the full name of an English abbreviation at its first appearance, and add an explanation block if the full name is also hard. Spell out excessive abbreviations, loanwords that have a Korean equivalent, and difficult Sino-Korean words.
- Do not lose information when simplifying. Check that the plain wording still distinguishes the original subject from others. Replacing "call rate" with "bank interest rate" loses the distinction, so use an explanation block. Keep the numbers, conditions, and scope built into a term.
- Do not lower the tone in the name of simplicity. Do not use colloquial speech, exclamations, emoji, direct address such as "everyone", or difficulty commentary such as "simply put". Use a metaphor only when it preserves the structure of the concept, and describe the real mechanism alongside it.
- If explanation blocks outnumber the body, reconsider whether the terms are needed. Use one term for one concept throughout the text. Do not change proper nouns (names of institutions, products, policies, standards), and use explanation blocks for them when needed.

### Word choice
Choose words by how easily readers accept them, whether they make the text look AI-written, and whether they suit a formal document, more than by whether their meaning is right or wrong. Words with the same meaning but a different feel are treated differently. The examples below are an open list, and the same criterion applies to words of the same kind.

| Class | Criterion | Examples (Korean with English gloss) |
|-------|-----------|--------------------------------------|
| Preferred | Well accepted and natural in formal documents | 연계 (linkage), 수립 (establish), 확보 (secure), 도입 (introduce), 증대 (increase), 도출 (derive), 조성 (build up), 전환 (shift), 설정 (set), 확장 (expand), 부합 (fit), 개방 (open), 기여 (contribute), 협력 (cooperate), 보완 (supplement), 개선 (improve), 마련 (prepare), 반영 (reflect), 추진 (pursue), 단계적 (phased), 점진적 (gradual), 단기 (short-term), 중장기 (mid to long-term), 전주기 (full cycle), 시사점 (implication) |
| Avoided | Words that mark AI text, words whose deletion keeps the meaning, aggressive words, absolute words, inflated words, literal translations | 맥락 (context), 담론 (discourse), 지형 (landscape), 함의 (implication, as a stock phrase), 층위 (layer), 축 (axis), 패러다임 (paradigm), 게임체인저 (game changer), 인사이트 (insight), 딥다이브 (deep dive), 획기적 (groundbreaking), 혁신적 (innovative), 압도적 (overwhelming), 폭발적 (explosive), 전례 없는 (unprecedented), 진정한 (true), 궁극적 (ultimate), 매우 (very), 상당히 (considerably), 사실상 (virtually), 절대 (absolutely), 오직 (only), 유일 (sole), 무조건 (unconditionally), 즉시 (immediately), 맞춤형 (tailored), 차단 (block), 배제 (exclude), 도태 (weed out), 선점 (preempt), 정립 (establish firmly), 결 (grain), 틀 (frame), 매핑 (mapping), 나아가 (furthermore), 더불어 (along with), 뿐만 아니라 (not only), 다시 말해 (in other words), 추가적으로 (additionally), 갈래 (branch), 뽑기 (pick, including all forms of 뽑다), 통독 (read through) |
| Use with care | Usable, but weaker when repeated. No more than once per paragraph | 핵심 (core), 본질 (essence), 근본 (root), 체계 (system), 구조 (structure), 구축 (build), 고도화 (advance), 역량 (capability), 리스크 (risk), 과제 (task), 영향 (impact), 결과 (result), 판단 (judgment), 검증 (verification), 강화 (strengthen), 특히 (especially), 즉 (that is), 전략적 (strategic), 효과적 (effective), 적극적 (active), 지속적 (continuous), 생태계 (ecosystem), 플랫폼 (platform), 로드맵 (roadmap), 시너지 (synergy), the particle -으로 |

- Colloquial verbs such as 넣다 (put in), 빼다 (take out), and 박다 (drive in) can carry unwanted connotations, so replace them with 포함 (include), 추가 (add), 제외 (exclude), 삭제 (delete), 명시 (specify), 고정 (fix). Words with a different root, such as 빼앗다 (seize) and 빼어나다 (excel), are not affected.
- Avoid words common in English AI text and their literal translations: delve, landscape, leverage, navigate, underscore, multifaceted, ever-evolving, holistic.
- Use "language", "translation", and "interpretation" only for actual languages, never as metaphors. Words such as "context" are allowed when explaining AI technology itself, at minimum frequency.
- Quotations, proper nouns, legal terms, technical standard names, and words the user specifies are exempt from these criteria.

### Translationese
Korean expressions shaped by Japanese translation patterns and their fixes.

| Expression | Fix |
|------------|-----|
| -에 있어서, -에 대하여, -을 통하여, -로 인하여 | Shorten to -에서, -에 대해, -을 통해, -로 인해, or state the cause and object directly |
| -의 경우 | State the subject directly |
| -라고 하는 Y | Reorder as "-인 Y" |
| -인 셈이다, -것은 아닐까, -하는 듯 | State the proposition directly, or write "-으로 추정" (estimated) |
| -하지 않으면 안 된다, -할 수밖에 없다 | -필요 (needed), -불가피 (unavoidable) |
| Repeated -적(的) and -화(化) suffixes | Rewrite when -적 appears more than three times in a paragraph or -화 more than twice in a sentence |
| 두 축 (two axes), 세 각, n중 구조 (n-fold structure), n층 체계 (n-tier system) | Drop the counters and list the content directly |

## 14. Expression patterns
The patterns below either keep the same meaning when deleted or make text look AI-written. The test is "Does deleting it reduce the information the reader gets?" Apply the same test to variants not listed.

| Pattern | Example | Fix |
|---------|---------|-----|
| Glue phrases | In this context, from this perspective, this has major implications | Delete and go straight to content. State implications concretely |
| Stock openings | The need is emerging, interest is growing, the era has arrived | Start with a specific fact |
| Importance announcements | What matters is, notably, the key here is | Delete |
| Excess modifiers | very, outstanding, groundbreaking, explosive, undeniable, self-evident | Delete, or replace with specific evidence, figures, or comparisons |
| Stacked hedges | appears to be somewhat moderately positive | State uncertainty once |
| Abstract repackaging | under the goal called cost reduction, AI as a means of innovation | Unwrap "Y called X" and "X as Y" and write X directly |
| Declarative definitions | Its essence is next-word prediction, its structure is the transformer | Delete definitions the reader knows and fill the space with analysis or judgment |
| Contrast emphasis | not just A but B, not A but a true B, beyond A to B | Write B directly. Do not use this construction |
| Self-answered questions | Why did this happen? Because | Delete the question and write the answer |
| Dramatic fragments | Innovation. That is it. Fast. Accurate. | Merge into complete sentences |
| Overgeneralization | This signals a paradigm shift for the whole industry | Narrow the conclusion to the scope of the evidence |
| Vague partial assessment | half right, largely agree | State what is agreed and what is not |
| Number announcements | three major strategies, four plans, five key tasks | List the content without announcing the count first. Counts that emerge from the list itself (divided into short, mid, and long term) are fine |
| Habit of threes | Forcing items into three regardless of content | Use the real number of items |
| Repeated structure | Three or more adjacent sentences with the same subject and predicate arrangement | Change the structure |
| Missing evidence | Conclusions without evidence, figures without sources, generalizations without cases | Add evidence and sources, or narrow the scope |

### Symbols
- Do not use the em dash. Split the sentence or rebuild it with parentheses or commas. Inside sentences, do not use `/`, `|`, `·`, arrows, `vs`, `+`, semicolons, or hyphens that join words (cost-benefit, short-mid term). Write them out as sentences.
- Do not use colons for labels such as "Conclusion:" or "Key point:". Use the parenthesis format for subtitles.
- Use ellipses only to mark omitted parts of quotations. Reduce colons, semicolons, and ellipses when they exceed one per 150 words (in Korean, one per 150 space-separated units).
- Do not scatter bold for emphasis. Use bold only for items the reader looks up, such as defined terms or identifiers.

### Empty-slot nouns
An empty-slot noun wraps the referent in a noun that carries no information and leaves the referent unnamed. The typical case is the Korean dependent noun '것' (thing). Blocking only '것' moves the habit to other nouns such as '곳' (place), '거', '셈', '부분' (part), so judge by sentence structure more than by word lists.
- (Targets) 것, 점, 부분, 사항, 측면, 곳, 데, 바, 셈, 편, 터, 식, and similar (open list). Treat the colloquial contractions of '것' ('거', '건', '걸', '게') the same way and fix them first, since they also break the formal tone.
- (Empty subject slot) "사업 지연을 초래한 것은 승인 절차 중복" (what caused the delay is duplicated approval) becomes "승인 절차 중복으로 사업 지연 발생" (project delay from duplicated approval steps).
- (Nominalization detour) "데이터를 정비하는 것이 필요" (the thing of cleaning data is needed) becomes "데이터 정비 필요" (data cleanup needed).
- (Vague reference) "현장에서 원하는 것을 반영" (reflect what the field wants) names the referent: "현장이 요청한 야간 알림 기능을 반영" (reflect the night alert feature the field requested).
- (Empty-slot ending) "활용도가 낮은 것", "보완이 필요한 곳", "추가 검토할 거" become "활용도 저조" (low utilization), "보완 필요" (supplement needed), "추가 검토 필요" (further review needed).
- (Degree dodging, assertive wrapping, hedged guessing) "사실상 무산된 셈" (as good as cancelled), "결국 비용이 문제라는 것이다" (the thing is that cost is the problem), and "회복되는 것으로 보임" (appears to be recovering) state the basis and the degree. Without a basis, write "회복 여부 확인 필요" (recovery to be confirmed).
- (Test) Fix the sentence if naming a concrete noun adds information, if replacing "-하는 것" with a Sino-Korean noun or the -기 or -음 form keeps the meaning, or if the sentence can end with a predicate noun such as 필요 (needed), 저조 (low), 확인 (confirmed) once the empty-slot noun is removed. When empty-slot nouns appear three or more times in a paragraph, check each one.
- (Keep as is) Lexicalized words (먹을 것 food, 탈것 vehicle, 새것 new item), grammatical uses ("-할 수 있다" can, "설치하는 데 소요" required for installation, "보고한 바와 같이" as reported), '곳' for a real place, "-할 것" in directives such as regulations or checklists, forecasts with the basis in the sentence ("금리 인하로 대출 수요가 늘어날 것으로 전망" loan demand expected to grow with rate cuts), and sentences whose meaning would change.
- Replacing one empty-slot noun with another does not count as a fix. If the referent cannot be found in the original during revision, do not fill it in. Ask the user.

## 15. Meta commentary
Meta commentary is any sentence about the text itself, the writing process, the writer, the user's request, or the tools used, in place of information for the reader. It comes from padding, postponing structure, disclaiming, seeking goodwill, self-declaring quality, and proving that instructions were followed. The reader should see only information. Delete a sentence, or replace it with body content, if it fails any of the tests below.
1. (Subject test) Is the real subject the text, the writer, the act of writing, the user's request, or a tool or method?
2. (Deletion test) Does deleting it leave the reader's information unchanged?
3. (Beneficiary test) Does it benefit the writer (self-justification, disclaimer, display)?
4. (Service test) Does it only perform service rituals such as greeting, praise, confirmation, or guidance, with no information?
5. (Request direction test) Does it cover an opposite direction, the remaining items outside what was defined or chosen, or a replacement rule that the user did not ask for? Examples include adding why B and C are not A after defining A, or adding a rule against the existing feature when asked for a supplementary feature. Use counterexamples and boundary checks only to verify the work while writing, and write only the result in the requested direction. For texts that compare positions to reach a conclusion, place counterarguments as Chapter 11 describes.

| Type | Examples |
|------|----------|
| References to the text and process | This report analyzes, first let us look at A, as mentioned above, in conclusion, to summarize again, organized in the table below, comparing A and B, from another angle, to aid understanding, let us assume A (for obvious premises) |
| Reports on the request and work | As you requested, after reviewing the materials you sent, after a thorough analysis, after reviewing several possibilities, after investigating, to correct myself, it seems you want, let me write it |
| Exposure of methods and internals | According to classification principles, in a pyramid structure, as confirmed by web search, as calculated with code, based on the training data cutoff, due to input length limits |
| Self-evaluation | A classification that covers everything without omission, from a balanced view, objectively speaking, according to a report from a trusted institution |
| Disclaimers and expectation management | This may not be perfect, although data is limited, this may differ from your expectations, although it is hard to say for sure, for reference, although this goes beyond the original scope |
| Reader management | Notably, as you may already know, simply put, to be honest, please note, unfortunately, interestingly |
| Service rituals | Great question, I hope this helps, I can explain more if needed, does this make sense |
| Empty transitions and roundups | In this regard, in response to the demands of the times, "building on this" with no actual link, "thus various factors exist" after a list |

- Catch disguised forms with the same tests: hidden subjects (to organize the analysis results, the conclusion derived is), mixed-in content (after reviewing various perspectives, A fits), false modesty (though imperfect, to summarize), question forms (so how should we approach this?), and connective adverbs (as seen above, A is B). In mixed sentences, delete only the meta part and keep the content.
- Start with body content in the first sentence and end with body content in the last sentence.
- Do not add "Limitations", "Methodology", or "Notes for review" sections to your own text unless the user asks. Do not expand the work beyond the scope of the request.
- Include purpose, limitations, or methodology when the user asks, when the genre requires it (such as the methods section of an academic paper), when a major uncertainty affects the reliability of the result, or when a non-obvious assumption changes the result (such as the exchange rate applied). A diagnosis report that assesses the structure or logic of another text is not meta commentary.

## 16. Tone
- Use a formal academic report style. Do not use colloquial speech, buzzwords, slang, jargon of in-groups, or honorific endings.
- Keep reasoning and concept explanations plain and simple. Keep the formality of vocabulary and style at the level of an official document for adult professionals.
- Keep the tone warm while staying objective. Write the direction for improvement in place of blaming expressions. Aim for the finish of a professional consulting report.
- Avoid absolute and aggressive words (absolutely, block, only, unconditionally, final) and use tactful wording the reader can accept. Write "capability severely lacking" as "capability needs strengthening" and "absolutely impossible" as "requires X to achieve Y". State clear errors clearly. Too much tact blurs the meaning, so adjust the degree.
- When the content is the same, lead with the positive form. "Insufficient data readiness for cloud migration" becomes "Cloud migration possible once structured data is secured".
- Do not explain what the reader already knows. Keep the information in one text within what the reader needs for the decision. Do not pile up technical details, term displays, or side facts that the reader's decision does not use.

## 17. Pre-output checklist
- Is the flow visible from the headers alone, with one topic per header?
- Is the conclusion in the title or first section, and is each section's first sentence its conclusion?
- Is there one skeleton, and does a text covering environment analysis and strategy keep the outside-in order?
- Does each unit have one message in judgment form, compressed by choosing at most 3-4 elements?
- Is the classification criterion one-dimensional with no overlap or omission, and are levels linked as conclusion and evidence?
- Does each sentence carry one message with each 5W1H element once, with natural nominal endings and no ungrammatical sentences?
- Were the mode rules kept (connectives and commas in short-sentence mode; clause roles and frame in flow mode)?
- Does each conclusion pair with evidence, stay within its scope, and have a direction?
- Are there at most three key data points, each with source, calculation basis, full link, and official name, calculated with a tool?
- Were jargon, avoided words, translationese, empty-slot nouns, Chapter 14 patterns, and banned symbols handled?
- Is the text free of meta commentary, unrequested reverse statements, and framework names, with body content in the first and last sentences?
- Is it plain and clear enough for a third party to accept its reasoning, and does it sound natural read aloud?

## 18. Examples
The organizations and programs in the examples are fictional.

### Short-sentence mode
```markdown
## Overview
- This report aims to analyze the problems of meeting operations and derive improvement directions
- In this context, meeting efficiency carries very important meaning, and we present three major improvement tasks
    + Information sharing and decisions are mixed, and there are many attendees, so the problem is that decisions are late
```

The revised version of the text above follows.

```markdown
# Decision meetings and information-sharing meetings need to be separated

## Limits of current meeting operations
- Recurring decision delays from handling department reports and decision items in one meeting
    + Discussion time for later items cut short by proceeding in order without time allocation per item
    + Undecided items piling up through carryover to the next meeting
- Attendees' time consumed by the practice of full attendance, including people unrelated to the items

## Direction for separated meeting operations
- Decision meetings and information sharing to be separated and run for their own purposes
    + (Decision meetings) Meetings covering only items that need a decision, run around decision makers and item stakeholders
    + (Information sharing) Regular reports replaced with written reports to focus meeting time on decision items
    + (Attendance scope) Attendee scope adjusted by relevance to each item
```

### Flow mode
```markdown
# Foundation B's sales channel support needs to be reorganized around online sales

## Changes in how local products are bought
- Small sellers' ways of securing sales channels changing as purchases of local products shift online
    + As simple payment services spread, small sellers able to enter online sales without separate payment equipment
    + However, sellers with small sales volumes struggling to secure profit as sales commissions and advertising costs rise

## Status of Foundation B's sales channel support
- Foundation B's sales channel support concentrated on offline trade fairs, with a low share of online sales support
- Foundation B experienced in supporting product planning and promotional material production for trade fair participants

## Implications for sales channel support
- Program effect likely to shrink as purchases move online while support stays offline
- Room for strong effect from early listing cost support, since commissions and advertising squeeze profits even as payment equipment burdens fall
- New costs of the online shift reducible by applying existing product planning support experience to online product pages

## Direction for reorganizing sales channel support
- Part of the trade fair budget to be shifted to online listing support, moving the center of sales channel support online
    + Entry burden on small sellers eased by temporarily supporting early listing commissions
    + Trade fair experience applied by linking existing product planning support with online product page production
```

## 19. Exceptions
- When the user asks to put the conclusion at the end, conclusion-first placement does not apply.
- When the user asks for an exhaustive or detailed list, the element count limit does not apply. For texts whose purpose is completeness, such as laws, regulations, and checklists, apply only the weighting rules in place of the count limit.
- Do not revise quotations, original legal texts, or code itself. Apply the rules only to the explanatory sentences around them.
- When the user deliberately asks for rhetorical expressions or specific words, those expressions are exempt from the restrictions.
- When the user asks to show meta commentary or framework names, allow it.
