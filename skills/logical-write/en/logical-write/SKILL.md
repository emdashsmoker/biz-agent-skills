---
name: logical-write
description: "Logical outline-style (gaejosik) writing for reports, plans, proposals, and analyses in a Markdown hierarchy. Writes, revises, and diagnoses text with a conclusion-first layout, one-criterion classification without overlaps or gaps, paired claims and evidence, one message per sentence, noun-phrase endings, and cited sources, ready for hwpx or docx. Strict mode (no conjunctions) by default, flow mode on request. Use when the user types '/logical-write' or asks for report style, logical writing, conclusion first, a pyramid structure, MECE, flow, a clear conclusion, no meta commentary, no AI tells, less jargon, or tighter focus. Rules: references/sentence.md (sentences), references/structure.md (structure), references/logic.md (arguments), references/judgment.md (conclusions), references/classification.md (classification), references/expression.md (formulaic phrasing, meta commentary), references/vocabulary.md (word list), references/terms.md (jargon). Translated from the Korean original."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# logical-write

> Translation notice: this English edition was translated from the Korean original. It may behave differently from the original intent. Rules about Korean grammar and the Korean word lists assume Korean output, so their examples stay in Korean with English glosses.

These rules govern writing and revising reports, plans, proposals, and analyses in Markdown outline style (gaejosik, the Korean bullet-point report style). Heading levels (`#`, `##`) and item levels (`-`, `+`) map directly onto the chapter numbers and item markers of hwpx and docx reports. People can transcribe them easily and LLMs can process them easily.

The rules fall into logic, structure, sentences, and expression. Logic decides what to say, structure decides the order, sentences decide how to write each line, and expression decides which words to choose. This file holds the core rules. Detailed criteria and examples live in the `references/` files.

## Task modes

Choose the task mode from the wording of the request.

| Mode | Example requests | Output |
|---|---|---|
| Write | "write", "draft" | Output the result only |
| Revise | "fix", "polish", "revise" | Summarize the types of change, one line per type, then output the revised text. Do not mention the revision inside the revised text. Keep the facts, figures, sources, and quotations of the original |
| Diagnose | "review", "diagnose", "check" | Give pass or fail for each check item, the location of each failure, and the direction of improvement. When the structure needs rebuilding, add a rearrangement plan |

In all three modes, keep the skill name, rule names, framework names (SCQA, MECE, So What, and so on), and the checking process out of the output. Diagnostic reports also point to the structure itself. Write "The conclusion is missing from the first section" and never "Violates the pyramid principle."

## Sentence modes

The two sentence modes differ only in whether they allow conjunctions and clause-linking endings. All other rules are the same.

| Item | Strict mode (default) | Flow mode |
|---|---|---|
| Conjunctions (그리고 "and", 그러나 "but", 그래서 "so", 그렇기 때문에 "therefore", 이는 "this", 이에 따라 "accordingly", and so on) | Do not use them. Show relations between sentences through item order and hierarchy | Use them only when a real causal, elaborating, contrasting, temporal, or conditional relation links the sentences |
| Clause-linking endings (-으며 and -이며 "and", -고 "and", -면서 "while", -지만 "although", -함에 따라 "as", -할 경우 "if", and so on) | Do not use them. Write two facts as two sentences. Carry a means or cause inside one sentence as a single 5W1H element, such as -하여 "by" or -으로 "due to" | Use them only for clauses that support the core message: cause, condition, specification, or means |
| Common rules | One message per sentence, each 5W1H element once, noun-phrase endings, parenthesized subheadings, source citations | Same as strict mode |

Choose the mode by these criteria.

- Strict mode is the default.
- Use flow mode when the user asks for "flow", "narrative", "connected sentences", "a storyline", or "context" (Korean requests include "흐름 있게", "서사적으로", "연결되게", "스토리라인 있게", "맥락 있게").
- Use strict mode when the user asks for "short sentences", "broken up", or "strict" (Korean: "단문으로", "끊어서", "엄격하게").
- Apply the mode per request. When the user names a section, apply the mode to that section only. Without a named section, write the whole output in one mode.
- Do not ask the user about the mode while writing.

The same content in both modes looks like this.

```markdown
## Merge of repeated input fields needed
- Field staff re-enter the same customer data on several screens, raising handling time per case
    + Complaints about repeated entry up with the month-end closing workload
    + Input-error correction requests concentrated in the repeated fields
- Operations team to merge the repeated fields into one screen to cut the input burden
    + Merge priority set from field survey results
    + Rollout to all departments after checking handling-time change in pilot departments
```

```markdown
## Merge of repeated input fields needed
- Handling time per case has grown as field staff re-enter the same customer data on several screens
    + Complaints about repeated entry rise as input volume peaks during month-end closing
    + Input-error correction requests arise mainly in the repeated fields
- Accordingly, the operations team plans to merge the repeated fields into one screen to reduce the input burden
    + Merge priority set by reflecting field survey results
    + Pilot departments first, then all departments after checking the change in handling time
```

## Writing procedure

Work from large units to small units.

1. Set the purpose and the reader. Look past the literal wording and infer why the user asked. First settle the minimum scope needed to handle the request, what the reader already knows, and the definition, scope, and criteria of key terms. Keep a definition, scope, or criterion unchanged to the end of the text once you set it.
2. Set the core message. Write one judgment sentence the reader should remember. When you must judge between opposing positions, read `references/judgment.md`.
3. Design the structure. Pick one macro structure and settle the heading names and the flow between headings first. Read `references/structure.md`. When you split or group items, read `references/classification.md`.
4. Write the sections. Give each section one message and attach evidence to every claim. Follow `references/sentence.md` for sentences and `references/logic.md` for claims and evidence.
5. Check. Run the pre-output checklist below. Check expression with `references/expression.md`, `references/vocabulary.md`, and `references/terms.md`.
6. Review the heading names one last time. A reader should know the content under each heading from the heading alone.

| File | Contents | When to read |
|---|---|---|
| `references/sentence.md` | 5W1H test procedure, detailed rules per mode, punctuation, endings, empty nouns such as 것, sentence rhythm | When writing or revising sentences |
| `references/structure.md` | Conclusion first, macro structures, order of analysis stages, heading names, one message per unit, placement of tables and data, diagnostic items | When designing or diagnosing structure |
| `references/logic.md` | Paired claims and evidence, hypothesis thinking, formal fallacies, informal fallacies, cognitive biases, burden of proof | When building claims or reviewing arguments |
| `references/judgment.md` | Fence-sitting tests, evidence quality ranking, placement of counterarguments, conditions for withholding a conclusion | When concluding between opposing positions |
| `references/classification.md` | Classification criteria, overlap and gap checks, hierarchy relations, definitions, handling missing information | When splitting, grouping, or defining |
| `references/expression.md` | Empty expressions, formulaic LLM rhetoric, meta commentary | Pre-output check, revision |
| `references/vocabulary.md` | Preferred, non-preferred, and cautionary words, translationese | Pre-output check, revision |
| `references/terms.md` | Jargon test and handling order | Text for non-expert readers, text with heavy jargon |

## Output format

```markdown
# Document title
## Section title
- Claim (no indent)
    + Evidence for the claim (4-space indent)
    + A second, parallel piece of evidence
> (Data name) Description of qualitative or quantitative supporting data

> Organization or author (year), title of the source (URL)
```

- Write a claim in a `-` item and its evidence or elaboration in `+` items.
- Use `+` items only when two or more parallel items exist. When only one remains, merge it into the parent sentence or lift it to its own `-` item. One `+` item is allowed when the parent is a proper name or a framework and the child gives its definition or scope in one line.
- Three or four `+` items per parent are recommended.
- The `+` mark is for indentation only. Do not use it inside a sentence to list or join things.
- Use `>` blocks only for supporting data, sources, and jargon explanations. Separate multiple blocks with blank lines.
- Put a subheading in front of a sentence as `- (Subheading) content`. Do not use `Subheading : content` or `Subheading - content`.
- Name subheadings with keywords that carry content. Do not use empty labels such as "(Explanation)", "(Reason)", "(Claim)", "(Evidence)", or "(Section 1)", and do not repeat the same subheading. Add subheadings only where they help.
- Subheadings under the same parent follow the same classification criterion. Within one group, give every item a subheading or give none a subheading.
- Keep headings at the same level in one form: all keyword headings or all sentence headings.
- Give each heading one topic. Split "Policy trends" and "Technology trends" into two headings and do not join two topics with "and", "with", or "/" as in "Policy and technology trends".
- Write ranges with a hyphen (`-`) instead of a tilde (`~`). Two tildes on one line render as strikethrough in Markdown.
- Prefer characters you can type on a standard keyboard.

## Core rules

### Sentences

- Put one message in one sentence. Who, when, where, what, why, and how each appear once per sentence. Including why, what, and how in each sentence is recommended.
- End sentences with noun forms (Korean -함, -임, -필요, -전망, -예정; in English a noun phrase such as "Budget expansion needed"). Do not use honorific endings, colloquialisms, trendy words, slang, or jargon of closed groups. Keep the formality of academic writing.
- Make noun-form endings read naturally. Revise "목차명에는 키워드 기반 재구성으로 반영" ("reflected in table-of-contents names as keyword-based restructuring") to "목차명은 키워드 기반으로 재구성" ("table-of-contents names restructured by keyword").
- Do not write sentences that only chain nouns. Keep the particles and write "연구 인프라 보유 여부" ("whether research infrastructure is in place") instead of "연구 기술 자원 역량 상태" ("research technology resource capability status").
- Use commas only for lists of three or more items of the same category. Write two items as "A and B". In Korean output, join two parallel nouns with 및 in place of 와 or 과 ("예산과 인력 확보" becomes "예산 및 인력 확보"). Keep 와 or 과 when it marks a relation between two nouns (사이, 간, 격차, 차이, 일치, 불일치, 연계, 연동, 정렬, 비교, 구분, 분리, 협력, as in "현행과 기준의 격차") or the partner of an action (as in "유관기관과 공유"), or when it belongs to an established term, such as "학습과 성장" in the BSC. Do not just delete a joining comma. Split the sentence or rebuild it as a noun phrase.
- Do not use sentence-final periods, semicolons, separator symbols (/, |, ·, →, vs), joining hyphens ("short-mid term"), excessive abbreviations, or unnecessary loanwords and Sino-Korean words.
- Do not hide the referent behind empty nouns such as the bound noun 것 ("thing") or 곳 ("place"), 부분 ("part"), 셈 ("amount to").
- Do not use negate-then-assert contrasts such as "not A but B" or "not merely A but B". Write B directly.
- Prefer the positive form when the meaning is the same. "Cloud migration possible once structured data is secured" beats "Data readiness for cloud migration insufficient".

### Structure

- Put the conclusion first. Place the conclusion of the whole text in the document title or the first section, and the conclusion of each section in its first sentence.
- Use one macro structure for the whole text: SCQA (situation, complication, question, answer), Why-What-How (need, action, execution), or SCR (situation, complication, resolution).
- Text that covers environmental analysis and strategy follows the order macro environment, micro environment, internal status, benchmarking, strategy, implementation.
- A parent item is the conclusion of its children, and the children are evidence for the parent. Group items at the same level by kind and arrange them in one order.
- Give each section, item group, and table one message. Three or four components supporting the message are recommended. At five or more, group them under higher categories.
- Write each section so it makes sense on its own. Sections should be easy to combine with or separate from other sections.
- Use tables to summarize the core of the text, and always use them in long texts. Three tables or fewer per text are recommended. Place a table right after the related claim and never place two tables back to back. Do not put tables inside `>` blocks or code blocks.

### Logic and judgment

- Attach evidence to every claim. Tracing must work both ways, from evidence to claim and from claim to evidence.
- Do not stop at surface evidence. Repeat "why" until you reach the root cause.
- Verify the request, common beliefs, authority, buzzwords, famous frameworks, and your own knowledge before accepting them.
- Do not mix facts and judgments in one sentence or one classification.
- Classify by one criterion so items do not overlap and nothing falls outside. Three or four items per level are recommended.
- Reach a conclusion in one direction. Examine the counterargument in its strongest form and place it under the conclusion. Do not present the midpoint as the conclusion.
- Do not substitute the name of an authoritative institution for evidence. Do not use the absence of information as evidence of absence.
- Do not borrow the form of a method without checking it against reality. This covers number designs that ignore real demand, reasoning that bends facts to fit a goal, defense designs that rely only on block lists, theories that cannot be falsified, rosy forecasts without grounds, and plans that copy only the form of a leading case. Also avoid a view that chases cost figures alone and an exaggerated marketing view.
- Do not insert counterexamples, paradoxes, reverse rules, opposing logic, explanations of what falls outside, or replacement rules that the user did not request.
- Draw conclusions from a neutral and objective reading of the facts. Do not speak for a middle ground. Do not leap to assertive or aggressive reasoning.

### Evidence and sources

- Use quantitative data only when its calculation basis or survey basis is clear. When a third party asks for the basis, you should be able to answer in 5W1H.

```markdown
- (Correct) According to a 20XX survey by OO Research, the domestic A market is expected to grow from about B won in 20XX to about D won in 20XX, an average annual rate of about N% (C methodology, optimistic scenario)
- (Wrong) A market expected to grow N%
```

- Three key quantitative data points or fewer per text are recommended. The more figures, the harder it becomes to see which one matters.
- For time series, three to five years or more is recommended, with the compound annual growth rate or the share of the total alongside.
- Do numerical calculations with code, never by the model directly.
- Cite sources as "Organization or author (year), title (URL)". Place the citation in a `>` block right below the sentence that holds the quantitative data. When consecutive data share a source, cite it once at the end of the data group. Sources for qualitative quotations may go at the end of the section.
- Use quantitative data only from sources whose origin is clear and verifiable. For figures in news articles or blogs, confirm the original source and cite that source.
- Cite primary sources that have editing and verification processes: government and public agency publications, reports of international organizations, academic papers, material from credible research and financial institutions, and official documentation of large open-source projects. Do not cite blogs, wikis, or anonymous boards with unclear sources.
- Keep organization names and source titles exactly as the original writes them. Never invent a source. Give the full URL that opens the source directly, never the domain alone.
- Write numbers with thousands separators and units (1,000,000 or 1 million).
- When you introduce or quote a document, include its key content in full so the reader does not need to look up the original.
- Say you do not know when you do not know.
- Use the official full names of people, organizations, sources, policies, programs, and products. Do not shorten or alter them unless the user asks.

### Expression

- Do not write meta commentary about the text itself, the writer, the writing process, the user's request, or the tools used.
- Do not use modifiers, evaluative words, or filler connectors whose removal leaves the meaning intact.
- Do not announce counts in advance, as in "three major strategies" or "four measures". Write the content directly.
- Do not re-explain what the reader already knows. Avoid information overload.
- Avoid assertive and aggressive words (absolutely, block, only, sole, unconditionally) and use polite, softened wording the reader can accept. Too much softening blurs meaning, so point out clear errors plainly.
- Keep a warm tone without losing objectivity. Avoid showy expressions that only insiders understand.
- Use simple logic and plain words. Simplicity applies to the flow of logic and the explanation of concepts. Keep the tone at the formality of official documents for adult professionals.
- Aim for the expertise and finish of a professional consulting report.

## Priority and scope

- Structures, classification criteria, sentence modes, notation, reader level, and length that the user specifies take priority over the defaults of this skill.
- When the user explicitly asks for rhetorical expressions, meta commentary (for example, "state the purpose of the report at the start"), a conclusion placed last, a balanced summary of both sides, or an exhaustive list, the matching rule does not apply.
- Follow genre conventions where they require certain statements, such as the research purpose and method sections of an academic paper.
- Do not change original quotations, original statutory text, or code itself. Apply the rules only to the explanatory sentences around them.
- Proper nouns, legal terms, and names of technical standards are outside the vocabulary rules.
- When the rules conflict with the user's notation guidelines, follow the user's guidelines for notation and use this skill's criteria to decide whether an expression is formulaic.

## Pre-output checklist

- Does the document title or first section hold the conclusion, and does each section open with its own conclusion?
- Can the reader follow the flow and the content from the headings alone?
- Does each section and item group deliver one message?
- Is there one classification criterion, with no overlaps or gaps between items?
- Does every claim have evidence, and does each conclusion stay within the scope of its evidence?
- Does the conclusion point in one direction?
- Does each 5W1H element appear only once per sentence?
- In strict mode, are conjunctions and clause-linking endings absent?
- In flow mode, do conjunctions appear only where they show a real relation, with no stacked linking endings in one sentence?
- Do noun-form endings read naturally, with no honorific or colloquial endings?
- Are `+` items used only when two or more exist?
- Does every quantitative data point have a basis and a source?
- Are meta commentary, empty modifiers, count announcements, and negate-then-assert contrasts absent?
- Are the skill name, rule names, and framework names absent from the output?
- Are counterexamples and reverse rules that the user did not request absent?
- Are em dashes, tildes, and sentence-final periods absent?
