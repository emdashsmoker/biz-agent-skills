# Jargon handling

> Translated from the Korean original. See the translation notice in SKILL.md.

Do not use words a non-specialist reader cannot understand without a definition. The goal is text the reader can read without stopping.

## Two failures

Adjusting vocabulary level produces failures at both ends. Avoiding one end makes it easy to slide into the other, so check both directions together.

- (Excess expertise) Using terms the reader does not know without defining them. The more familiar the writer is with a field, the less the writer notices which words are jargon.
- (Excess simplification) Losing information while trying to write simply. It takes two forms: vague abstraction, where a precise term becomes a catch-all word and the sentence says nothing ("currency swap agreement" becomes "money-related promise"), and childish style, where lowering the vocabulary also lowers the tone until formality collapses (colloquial endings, exclamations, addressing the reader, metaphors that distort the essence).

## Reference reader

- The reference reader for judging jargon is an average adult without specialist training.
- Assume the reader studied the school curriculum but has forgotten most of the details. Do not assume a reader who remembers the curriculum perfectly.
- Assume the reader lacks undergraduate knowledge of any particular field, industry conventions, and internal abbreviations of any organization.
- Pitch explanations at the level an experienced expert uses with a newcomer to the field.
- The reference reader is only a standard for judging words. The reader's lack of expertise is no reason to lower the tone or to treat the reader as immature.
- When the user names the reader (for example, "for semiconductor engineers"), adjust the standard to that reader's background knowledge.

## Judging a word

Every word passes two questions before output. Does the reader know this word? Is this word needed?

### Question 1. Does the reader understand it without a definition?

- When the reference reader understands a word without a definition, treat it as ordinary and use it.
- A word learned through daily life is ordinary. A word learned only through study of, work in, or a degree in a field is jargon.
- A word that looks like an everyday word but carries a different meaning in a field counts as jargon ("significant" in statistics, "good faith" in law, "exposure" in finance).
- Spell out English abbreviations and acronyms in full on first use, whether or not the reader knows them.
- The more familiar a word feels to the writer, the easier it is to skip the check, so doubt familiar words first.

### Question 2. Is it needed?

Apply this only to words that Question 1 marks as jargon.

- When the term does not serve the purpose or conclusion of the text, remove it entirely. Decide whether it belongs in the text before asking whether it deserves a definition.
- When an ordinary word can replace it without losing meaning, the term is not needed. Replace it with the plain word.
- When an ordinary word would change the meaning or blur the distinction from other things, the term is needed. Keep it in the body and attach an explanation block.

## Handling order

Handle jargon in the order below. Move to a later step only when the earlier one is impossible.

The explanation block carries the definition of any jargon kept in the body. Body sentences only use the term and do not define or paraphrase it. When the body and the explanation block state the same information twice, the reading flow breaks and the text turns into a glossary. When the purpose of the text is to explain that concept, the body's account of the concept is the content itself, so the body carries the definition and no explanation block is attached. Either way, define each term once, in either the body or the explanation block.

### Step 1. Remove

Remove a term that does not serve the purpose or conclusion of the text, before replacing or defining it.

### Step 2. Replace with a plain word

Replace a term with an ordinary word when the meaning survives.

| Before | After |
|---|---|
| migration | move |
| onboarding | helping new staff settle into the work |
| establishing a governance framework | setting decision responsibilities and procedures |
| pain point | inconvenience |
| creating synergy | securing a combined effect |

### Step 3. Explanation block

When a plain word would change or blur the meaning, keep the term in the body and place an explanation block right after the item where it first appears. Later appearances need no explanation. Do not tuck parenthetical definitions into body sentences, because they make sentences hard to read.

```markdown
> (Term) One-line simple sentence explanation that follows 5W1H
```

- (Position) Right after the item where the term first appears. Do not collect explanations in a glossary or footnotes at the end.
- (Several terms) When several terms appear in one place, separate their blocks with blank lines.
- (Targets) Terms whose precision is part of their meaning, such as legal terms, names of technical standards, names of institutional programs, and academic concepts.
- (Explanation sentence) Write one simple sentence. Do not use other jargon inside the explanation. Do not reuse the defined word. "(Post-quantum cryptography) Cryptography resistant to quantum attacks" is wrong. "(Post-quantum cryptography) Encryption designed to stay hard to break even for future computers with far greater computing power" is right.
- (Abbreviations) Spell out an abbreviation in full on first use in the body, and add an explanation block when the full name is itself jargon. Spelling out is notation, so it does not count as a duplicate definition. Write "PIM (Processing-In-Memory)" in the body and place "> (PIM) Semiconductor structure that performs computation inside the memory device" right after it.
- (No duplicates) Do not paraphrase a term in the body when it already has an explanation block. Writing "the call rate, which applies to very short-term interbank funds, rose" in the body and defining it again in the block is a duplicate. Write only "the call rate rose" in the body.

### Handling to avoid

- Using jargon without explanation
- Defining in the body what the explanation block should carry
- Replacing with a vague catch-all word that loses the meaning
- Tucking a long parenthetical definition into a body sentence
- Pushing explanations to a glossary or footnotes at the end

## Preserving precision

- Verify that the paraphrase carries all the information the original term held. A reader of the paraphrase alone must be able to tell the original referent apart from other things. When the reader cannot, switch to an explanation block.
- When a term has built-in figures, conditions, or scope, keep them in the paraphrase. Replacing "call rate" with "bank interest rate" makes it impossible to tell which rate is meant. Keep "call rate" in the body and attach an explanation block.
- When the boundary with a neighboring concept is the reason a term exists, preserve that boundary. Paraphrasing "supplementary budget" as "extra budget" alone blurs the line with an increase in the main budget, so use the formal name "supplementary budget" in the body with an explanation block.

## Preserving tone

Simplicity applies to word choice and concept explanation. Do not lower the formality of the tone.

- Keep the tone at the level of official documents for adults even when you simplify words.
- Do not use informal wording, colloquialisms, exclamations, emoji, or direct address such as "everyone".
- Do not comment on difficulty with phrases such as "simply put", "in short", or "this may sound hard". Writing the content plainly removes the need.
- Use metaphors only when they preserve the structure of the concept exactly. Do not use a metaphor that conveys only some properties while seeming to stand for the whole. Even with a metaphor, do not end the explanation on it. Describe how the thing actually works as well.
- Do not stage simplicity by chopping sentences short. Secure simplicity through words and logic.

## Jargon density

- When new explanation blocks pile up in one paragraph until explanations outweigh the body, reconsider the paragraph design. Before solving a term with a definition, decide whether the text's purpose needs it. Remove terms that do not serve the conclusion instead of defining them.
- Use one term for one concept across the whole text. Do not mix "migration", "move", and "transition" in one text.

## When revising

- Keep the facts, figures, sources, and structure of the original and handle only the vocabulary.
- Summarize the terms revised and how you handled them, then give the revised text.
- Keep out of the result any mention of replacing terms, judging the reader's level, or these rules. Do not declare self-application such as "written with minimal jargon".

## Examples

### Solved by plain words alone

```markdown
Before
- In an on-premises legacy system cloud migration, lift-and-shift is a second-best option from a TCO perspective
    + Cloud-native transition through replatforming or rearchitecting is superior in operational efficiency

After
- Moving the existing systems from company servers to the cloud without changing their structure costs more over the long run
    + Redesigning the system structure for the cloud before moving it is more efficient to operate
    + Scope of redesign expanded in stages, starting with functions that take the largest share of operating cost
```

### An explanation block is needed

```markdown
Before
- Central bank's big step lifts the call rate and expands RP sales

After
- Central bank raises the base rate by 0.50 percentage points at once
    + The call rate rises in step with the increase
    + Expanded sales of repurchase agreements absorb market liquidity at the same time

> (Call rate) Interest rate on very short-term funds that banks lend each other for a day

> (Repurchase agreement) Bond sold under the condition that the seller buys it back after a set period
```

"Big step" can be written as a figure, so it becomes plain wording. "Call rate" and "RP" cannot be told apart from other rates and bonds once paraphrased, so they stay in the body with explanation blocks. The abbreviation "RP" becomes its formal name in the body.

### Fixing vague abstraction

```markdown
Before
- The government implements a policy that affects the market through money-related measures
    + These measures are expected to improve the economic situation

After
- Government compiles a supplementary budget to fund loss compensation for small businesses
    + Compensation payments expected to ease small businesses' short-term cash shortages
    + Recipients and criteria set by proof of sales decline

> (Supplementary budget) Budget that revises the main budget and is compiled again during the fiscal year
```

### Fixing a childish style

```markdown
Before
Blockchain is simply a diary everyone writes in together! Once someone writes in it, it can never be erased. It may sound hard, but it's really like the minutes of a neighborhood meeting.

After
- Blockchain is a ledger technology in which many participants keep identical copies of transaction records
    + A participant who forges a record is exposed when the copy is compared with other participants' copies
    + Trust in the records is secured without a central administrator, so the parties can verify transactions directly
```

## Checklist

- Are words the reference reader cannot understand without a definition absent?
- Are jargon terms that do not serve the purpose or conclusion absent?
- Are words that look everyday but mean something else in a field absent?
- Are abbreviations spelled out in full?
- Did replacing with plain words keep the distinguishing information of the original term?
- Does each explanation block sit right after the item where the term first appears?
- Is each term defined once, in either the body or the explanation block?
- Are explanation blocks free of other jargon and of the defined word?
- Are long parenthetical definitions absent from body sentences?
- Is one term used for one concept throughout?
- Are informal wording, colloquialisms, exclamations, and difficulty comments absent?
- Does no explanation end on a metaphor alone?

## When these rules do not apply

- When the user names an expert reader, adjust the standard to that reader's background knowledge.
- Do not change original quotations, original statutory text, or code itself. Apply the rules only to the explanatory sentences around them.
- Do not replace proper nouns such as names of organizations, products, policies, or standards. Attach an explanation block when the reader needs one.
- When the user asks to keep a particular term, leave that term as it is.
