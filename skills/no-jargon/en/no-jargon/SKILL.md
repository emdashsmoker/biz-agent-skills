---
name: no-jargon
description: "Reduces jargon so that adult readers outside a field can read a text without looking up terms. It guards against using terms readers do not know without explanation, and against losing information or formality while trying to write simply. Supports a writing mode for new text and an editing mode for existing text. Use this skill whenever the user explicitly asks for it with phrases such as \"/no-jargon\", \"cut the jargon\", \"remove jargon\", \"less jargon\", \"use plain terms\", \"use simpler terms\", \"write so non-experts can understand\", \"write for a general audience\", \"explain the terms\", or \"plain language version\". Apply it only when the user explicitly asks. Do not apply it automatically."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Minimizing Jargon

*This skill is an English translation of a Korean original and may behave differently from what the original intends.*

This skill revises vocabulary so that adult readers outside a field can read a text to the end without looking up meanings. When it swaps a term for plain words, it keeps the precision of the information and the formality of the tone.

## Failure types

Adjusting vocabulary level fails in two directions: over-expertise and over-simplification. Over-simplification shows up as vague abstraction or a childish tone. Avoiding one failure often leads to the other, so check all three types together.

- (Over-expertise) Using terms the reader does not know without explanation
- (Vague abstraction) Replacing a precise term with a loose general phrase to sound simple, so the sentence no longer points to anything specific (e.g., rewriting "currency swap agreement" as "a money-related deal")
- (Childish tone) Lowering the tone along with the vocabulary to sound simple (e.g., conversational phrasing, exclamations, talking directly to the reader, analogies that distort the concept)

Over-expertise is handled by jargon identification and the handling order. Vague abstraction is handled by precision preservation, and childish tone by tone preservation.

## Reference reader

Judge whether a word is jargon against the reader below.

- An average adult without training in the field
- Someone who studied the primary and secondary school curriculum but has forgotten most of the details (do not assume a reader who remembers the curriculum perfectly)
- Someone who lacks undergraduate knowledge of a specific field, industry conventions, and an organization's internal abbreviations

Use the reference reader only to judge vocabulary. Do not lower the tone because the reader is not an expert. If the user names a different reader (e.g., "for semiconductor engineers"), shift the judgment to what that reader already knows.

## Identifying jargon

A word is jargon if the reference reader cannot understand it without a definition. Whether an identified term stays in the text is decided in the handling order.

- Treat words the reference reader understands without a definition as everyday words and use them as they are
- Treat words people pick up through everyday conversation and life experience as everyday words
- Treat words people learn only by studying or working in a specific field as jargon
- (Disguised everyday words) Treat a word as jargon when it looks like an everyday word but carries a different meaning within a field (e.g., "significant" in statistics, "consideration" in contract law, "exposure" in finance)
- (Abbreviations) Write the full name alongside an abbreviation, acronym, or shortened form the first time it appears, even if the reader seems likely to know it
- (Familiar words) Writers find it hard to notice jargon from their own field, so question the most familiar words first

## Handling order

For each identified term, check the conditions in the table from the top and apply the first action that fits. Decide whether the term is needed at all before thinking about how to define it.

| Step | Condition | Action |
|------|-----------|--------|
| 1 | The term does not help deliver the text's purpose or conclusion | Remove the term |
| 2 | The term can be replaced with everyday words without losing meaning | Replace it with plain words |
| 3 | Replacing it changes the meaning or makes it impossible to tell apart from other things | Keep it in the text and add an explanation block |

### Plain replacement

Replace terms with everyday words when this loses no meaning. If the rewritten sentence fails the precision preservation criteria, use an explanation block instead.

| Before | After |
|--------|-------|
| migration | move |
| onboarding | helping new staff settle into their work |
| establish a governance framework | set out who makes which decisions and how |
| pain point | difficulty users face |
| create synergy | gain combined benefits |

### Explanation block

When replacing a term with everyday words would change or blur its meaning, keep the term in the text and add an explanation block. This applies mainly to terms whose precision is part of their meaning, such as legal terms, names of technical standards, names of institutional programs, and academic concepts. The format is one line in a quote block with a label in parentheses.

```
> (term) One-sentence explanation
```

- (Position) Place the block right after the item where the term first appears. An item means one bullet or one paragraph.
- (Later mentions) Use the term without explanation when it appears again
- (Several terms) When one position needs blocks for several terms, separate the blocks with a blank line
- (No glossary) Do not gather explanations in an end-of-text glossary or in footnotes. Readers would have to move back and forth between the term and its explanation.
- (No parenthetical definitions) Do not insert long definitions in parentheses inside a body sentence. The sentence gets longer and harder to read.

Write explanation sentences by these criteria.

- Write the explanation as one simple sentence in which elements such as the subject, the object, and the method each appear only once
- Do not use other jargon inside the explanation
- Do not reuse the part of the defined term that carries its specialized meaning
- Words that name the general category the term belongs to (e.g., encryption, budget, bond, interest rate) may appear in the explanation
- (Violation) `> (convertible bond) A bond that can be converted into stock`
- (Correct) `> (convertible bond) A bond a company issues to borrow money that can be exchanged for that company's shares under set conditions`

Write the full name of an abbreviation in parentheses the first time it appears in the body. If the full name is also jargon, add an explanation block. For example, write "PIM (Processing-In-Memory)" in the body and place `> (PIM) A chip design that performs calculations inside the device that stores data` right after it. Writing the full name in parentheses counts as notation and does not count toward the definition count.

### Definition count

Define each term only once, either in the body or in an explanation block. Writing the same information twice breaks the flow of reading and turns the text into a glossary.

- Do not define or spell out a term again in a body sentence once it has an explanation block. The body only uses the term, and the block carries the definition.
- (Violation) Writing "the call rate, the interest rate on overnight money that financial institutions lend each other, rose" in the body and then adding a call rate explanation block right after it
- (Correct) Writing only "the call rate rose" in the body and keeping the definition in the explanation block
- If the purpose of the text is to explain the concept itself, the body's explanation of the concept is the definition. In that case, do not add an explanation block.

## Precision preservation

These rules prevent vague abstraction. A sentence rewritten in plain words must pass all criteria below. If it fails any of them, keep the original term in the body and add an explanation block.

- (Distinction test) A reader who reads only the rewritten sentence must be able to tell the thing the original term pointed to apart from other things
- (Built-in information) If the term carries numbers, conditions, or ranges, keep them when spelling it out
- (Boundary information) If the term exists to separate a concept from a neighboring one, keep that distinguishing information

Rewriting "call rate" as "bank interest rate" drops the condition of overnight, very short-term lending, so readers cannot tell which rate it is. In this case keep "call rate" in the body and add `> (call rate) The interest rate on very short-term money that financial institutions lend to and borrow from each other overnight`.

Rewriting "supplementary budget" as only "extra spending" hides that it is a formal procedure for changing a budget the legislature has already passed, which the legislature must approve again. In this case keep the formal term "supplementary budget" in the body and add an explanation block.

## Tone preservation

These rules prevent a childish tone. Keep vocabulary and explanations simple, and keep the tone at the level of an official document written for adult readers.

- Do not use informal wording, conversational phrasing, exclamations, emoji, or direct address to readers (such as "folks" or "everyone")
- Do not use phrases that comment on difficulty ("simply put", "in plain terms", "this may sound complicated, but"). If the content is written simply, there is no need to comment on its difficulty.
- Use an analogy only when it carries the structure of the concept accurately
- Do not use an analogy that conveys only some properties of a concept while giving the impression that it represents the whole
- When using an analogy, also describe how the thing actually works
- Do not chop sentences short to make the text look easy. Achieve ease through vocabulary and reasoning.

## Term density

- If explanation blocks in a paragraph run longer than its body text, redesign the paragraph. First re-check whether each term is needed for the purpose of the text, and remove the terms that are not.
- Use one term for one concept throughout the text (e.g., do not mix "migration", "move", and "transition" in the same text)

## How to apply

### Writing mode

When writing a new text, output only the result of applying jargon identification and the handling order.

### Editing mode

- Find jargon in the existing text and revise it following the handling order
- Keep the original's facts, figures, sources, and structure, and change only the vocabulary
- When fixing vague abstraction, recover the original term from the source text or source material. If it cannot be found, do not invent one. Ask the user instead.
- Put a short summary of the revised terms and how each was handled before the revised text

### Areas outside this skill

This skill handles vocabulary only. The areas below follow the original text or other guidelines. The formality of the tone follows the tone preservation rules.

- Sentence length, sentence form (full sentences or note-style fragments), and writing style
- Overall structure, markdown hierarchy, and length
- Expression habits beyond vocabulary

### Output labeling

- Do not state in the output text that terms were changed, how the reader's level was judged, or that this skill exists
- Do not add self-referential statements such as "Written with minimal jargon"
- Keep the editing-mode summary outside the revised text

## Exceptions

- Leave quoted text, the original wording of statutes, and code unchanged, and apply this skill only to the surrounding explanatory text
- Do not replace proper nouns (names of organizations, products, policies, and standards). Add an explanation block if the reader needs one to understand them.
- Exclude terms the user has asked to keep

## Examples

### Fixing over-expertise

Before

```
- Lift-and-shift migration of on-prem legacy systems to the cloud is suboptimal from a TCO perspective
- Replatforming or rearchitecting toward cloud-native delivers superior operational efficiency
```

After

```
- Moving existing systems that run on in-house servers to the cloud without design changes costs more once setup and running costs are counted together
- Moving systems after adjusting part or all of their design to the cloud environment runs more efficiently
```

"On-prem", "legacy", "migration", "lift-and-shift", "TCO", "replatforming", "rearchitecting", and "cloud-native" were all replaced with everyday words. The difference between replatforming and rearchitecting is kept as "part or all of their design". In this case plain replacement alone keeps the meaning.

### Fixing text that needs explanation blocks

Before

```
- The central bank's jumbo hike pushed up the call rate and expanded repo sales
```

After

```
- The central bank raised its policy rate by 0.5 percentage points at once
- The call rate rose to reflect the size of the increase

> (call rate) The interest rate on very short-term money that financial institutions lend to and borrow from each other overnight

- The central bank sold more repurchase agreements to absorb money from the market

> (repurchase agreement) A sale of bonds on the condition that the seller buys them back after a set period
```

"Jumbo hike" can be spelled out with a number, so it was replaced with plain words. "Call rate" and "repo" would become indistinguishable from other rates or transactions if spelled out, so they stay in the body with explanation blocks. "Repo" is a shortened form, so the body uses the formal name "repurchase agreement". Each block sits right after the item where its term first appears.

### Fixing vague abstraction

Before

```
- The government carried out a money-related measure that affects the market
- This measure is expected to improve the economic situation
```

After

```
- The government drew up a supplementary budget to secure funds for compensating small businesses for their losses

> (supplementary budget) A budget the government draws up to change an annual budget the legislature has already passed, which the legislature must approve again

- Compensation payments are expected to ease small businesses' short-term cash shortages
```

"A money-related measure" does not identify which policy is meant. The policy name and the group it supports were recovered from the source material, and the policy name received an explanation block.

### Fixing a childish tone

Before

```
Simply put, blockchain is a diary that everyone writes in together! Once someone writes something, it can never ever be erased. Sounds hard, but honestly it's just like the minutes from your neighborhood meeting.
```

After

```
Blockchain is a record-keeping technology in which many participants each hold an identical copy of the transaction records. If one participant alters a record, the change shows up when that copy is compared with the copies held by the other participants. This design lets the parties to a transaction verify records directly with each other without a central administrator.
```

Conversational phrasing, exclamations, difficulty commentary ("Simply put", "Sounds hard, but"), and a distorting analogy were removed. A diary suggests a record kept by one person, so it fails to convey that many participants each hold a copy. The original was a paragraph, so the revision stays a paragraph. Because the purpose of the text is to explain blockchain, the body carries the definition and no explanation block is added.

## Pre-output check

Before producing the result, check the items below and fix anything that does not meet them.

- Is any word the reference reader cannot understand without a definition used without explanation?
- Does any jargon remain that does not help deliver the text's purpose or conclusion?
- Is any disguised everyday word used without explanation?
- Does each abbreviation have its full name written alongside it the first time it appears?
- Do sentences rewritten in plain words pass the precision preservation criteria?
- Does each explanation block sit right after the item where its term first appears?
- Is each term defined only once, either in the body or in an explanation block?
- Is each explanation block free of other jargon and of the specialized part of the defined term?
- Is the body free of long parenthetical definitions?
- Does each concept use a single term throughout the text?
- Is the text free of informal wording, conversational phrasing, exclamations, and difficulty commentary?
- Wherever an analogy appears, are the actual workings of the concept also described?
