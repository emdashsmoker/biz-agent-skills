# Reader lens

> This English version was translated from the Korean original. It may behave differently from what the original intends.

Check whether readers can find what they need in a text, understand it, and act on it right away. This lens covers both reshaping the same facts for each reader and matching jargon to the reader's level.

## Background

The checks follow the principles of the plain language standard ISO 24495-1:2023 (relevant, findable, understandable, usable). Putting the conclusion first follows BLUF (bottom line up front), a principle from military writing.

## 1. Is it relevant?

Identify the reader first. If the user named a reader, use that reader. If not, treat as the reader the person who must actually do something after receiving the text.

Ask these questions about each reader.

- What does this reader do after reading?
- What do they already know?
- Without which information can they not do their job?
- What information do they not need, or must not be promised?

What goes in depends on what the reader does with the text.

| What the reader does | Show first | Include | Leave out |
|---|---|---|---|
| Decides (approves, allocates resources, sets priorities) | The conclusion and its effect on the organization | The risk of not deciding, the decision or resources you are asking for | Implementation details, technical architecture, feature lists |
| Builds (creates and operates) | The problem to solve and its constraints | Scope, what is out of scope, edge cases, dependencies, completion criteria, open questions | Promotional language, unsupported timelines, vague requirements |
| Relays (explains to customers or outsiders) | What changes for the other party | What they can say, what they must not promise, known limits, timeline | Internal debates, unconfirmed plans |
| Integrates (plugs the result into their own system or work) | What changed | Steps they must change, breaking changes, end-of-support dates, where the reference docs are | Business rationale, internal circumstances |

When sending the same facts to several readers, follow these rules.

- Keep the facts. Change only the order and emphasis.
- Give each version one reader. Each version must make sense without the others.
- If something one reader must hear clashes with something another reader must not hear, raise that clash with the user.

## 2. Is it findable?

- For readers who decide, put the conclusion and the request at the top.
- Write headings so that the heading alone tells what follows.
- Keep one topic under each heading.
- Order content the way the reader looks for it. Deciders read from conclusion to evidence. Builders read from problem to method.

## 3. Is it understandable?

Use words the reader can read without stopping. The goal is to avoid words the reader does not know unless you explain them. Keep the technical terms you need.

### Failures on both sides

When adjusting vocabulary, guard against both failures at once. Avoiding one tends to push you into the other.

- Too technical: using terms the reader does not know without explanation. The more familiar the writer is with the field, the less they notice which words are jargon.
- Too simplified: losing information while trying to be easy. Precise terms get swapped for vague ones until the sentence says nothing (turning "currency swap agreement" into "a money-related deal"). Or the tone drops along with the vocabulary and formality collapses (casual speech, exclamations, talking to the reader directly, metaphors that distort the idea).

### Reference reader

If the user did not name a reader, judge jargon against this person.

- An average adult with no particular specialty
- Someone who went through school but has forgotten most of the details
- Someone without undergraduate knowledge of a specific field, industry practice, or in-house abbreviations

The reference reader is a yardstick for vocabulary only. Do not lower the tone because the reader is not an expert. If the user names a reader (for example, semiconductor engineers), adjust the yardstick to that reader's background knowledge.

### Test questions

Ask these questions of every word.

Question 1 is whether the reader understands it without explanation.

- If the reference reader understands it without explanation, treat it as an everyday word and use it as is.
- Judge by how people learn the word: through daily life, or through studying or working in a specific field. The second kind is jargon.
- Words that look everyday but mean something else within a field count as jargon. Examples are "significant" in statistics, "good faith" in law, and "exposure" in finance.
- Spell out every abbreviation and acronym in full the first time, whether or not the reader knows it.
- The more familiar a word feels to the writer, the easier it is to skip the test. Suspect familiar words first.

Question 2 is whether the term must be used. Apply it only to words that question 1 flagged as jargon.

- If the term does not help deliver the text's purpose and conclusion, remove it entirely. Ask whether it belongs in the text before asking whether an explanation could save it.
- If a plain word can replace it without losing meaning, replace it.
- If a plain word would change the meaning or make it impossible to tell the term apart from similar things, the term is essential. Keep it in the body and add an explanation block.

### Order of treatment

Treat jargon in this order. Do not move down a step if an earlier step works.

Step 0 is removal. Delete terms that do not help deliver the purpose and conclusion before trying to replace or explain them.

Step 1 is replacing with plain words.

| Before | After |
|---|---|
| leverage | use |
| onboarding | helping new staff settle into the job |
| governance framework | who decides what, and by which steps |
| pain point | problem |
| create synergies | get a combined effect |

Step 2 is the explanation block. Keep terms that would change meaning if replaced, and put an explanation block right after the item where the term first appears. After that, use the term without explanation.

```
> (term) one-line explanation
```

- It applies to terms where precision is part of the meaning, such as legal terms, technical standard names, program names, and academic concepts.
- Keep the explanation to one line. Do not use other jargon or the term itself inside it. "(post-quantum cryptography) cryptography resistant to quantum attacks" repeats the term. Write something like "(post-quantum cryptography) encryption designed to stay hard to break even for future computers with far greater computing power".
- If several terms appear in the same place, put a blank line between their blocks.
- Do not push explanations into a glossary or footnotes at the end.
- Do not explain a term again in the body once it has a block. The body uses the term and the block defines it. A definition given twice breaks the flow of reading.
- Do not wedge long parenthetical explanations into body sentences.
- Spell out an abbreviation in full at its first appearance in the body, and add a block if the full name is itself jargon. Spelling out a full name counts as notation, so it is not a duplicate definition.
- If the text's purpose is to explain the concept, the explanation in the body is the content itself. In that case, add no block. Either way, define each term once, in one place.

### Keeping precision

- Check that a reader of the plain version alone can still tell the original term's object apart from similar things. If not, information was lost, so switch to an explanation block.
- If a term carries figures, conditions, or ranges, keep them when rewriting it. Turning "overnight call rate" into "a bank interest rate" makes it impossible to tell which rate is meant.
- If the boundary with a neighboring concept is the reason the term exists, keep the boundary. Shortening "supplementary budget" to "extra money" blurs it with an increase in the main budget, so use the formal name and add a block.

### Keeping tone

- Keep the tone of a formal document for adults even when the vocabulary is simple.
- Do not use casual speech, exclamations, emoji, or direct address to the reader ("folks", "you guys").
- Do not use phrases that comment on difficulty, such as "simply put", "in plain terms", or "this may sound hard, but". If the content is easy, no commentary is needed.
- Use metaphors only when they carry the concept's structure accurately. Do not end an explanation on a metaphor. Describe how the thing actually works as well.
- Do not chop sentences short to make them look easy. Ease comes from words and logic.

### Term density

- If new explanation blocks pile up in one paragraph until they outweigh the body, rethink the paragraph. First judge whether each term is needed for the text's purpose.
- Use one term for one concept across the whole text. Do not mix "migration", "move", and "transition" in one text.

## 4. Is it usable?

- Can the reader tell what to do after reading? Give deciders the decision you want and its deadline, builders the completion criteria, and integrators the steps and schedule.
- If the reader has to find material outside the text before acting, put what they need in the text or state exactly where it is.

## Diagnosis output

When asked for a diagnosis, write the following.

- One line naming the reader and what they do with the text
- Findings: which principle above each falls under, location, problem, and rewritten sentence
- Jargon table: term, treatment (removed, plain word, explanation block), and the new wording

## When applying

- When writing new text, apply the test questions and order of treatment internally. Do not mention in the output that terms were changed, your judgment of the reader's level, or this lens.
- When revising existing text, keep the original facts, figures, sources, and structure, and change the order and vocabulary for the reader. Summarize the changed terms and how you treated them briefly, then deliver the result.
- When producing versions for different readers, title each version with the reader's name and make each stand alone.

## Examples

Fixing text that is too technical:

```
Before: For on-prem legacy workloads, a lift-and-shift cloud migration is second-best from a TCO standpoint
After: Moving existing systems from company-owned servers to the cloud without changing their structure costs more over the long run
```

A case that needs explanation blocks:

```
Before: The central bank's big step pushed up the call rate and expanded RP sales
After: The central bank raised its policy rate by 0.50 percentage points at once. The overnight call rate rose to reflect the increase. The bank also sold more repurchase agreements to absorb money from the market.

> (overnight call rate) the interest rate on very short-term loans that banks make to each other for one day

> (repurchase agreement) a sale of bonds with a promise to buy them back after a set period
```

Fixing text that is too simplified:

```
Before: Blockchain is basically a diary everyone writes in together! Once you write something, it can never be erased.
After: Blockchain is a ledger technology in which many participants each keep an identical copy of the transaction records. If one participant forges a record, comparing it with the others' copies exposes the forgery.
```

## Pre-output check

- Did you identify the reader and what they do?
- Did you leave out what the reader does not need and what must not be promised?
- For deciders, are the conclusion and the request at the top?
- Did you avoid using words the reference reader cannot understand without explanation?
- Did you avoid using everyday-looking words with field-specific meanings unexplained?
- Did you spell out abbreviations in full?
- Did replacing terms with plain words keep the information needed to tell things apart?
- Does each explanation block sit right after the term's first appearance, with each definition given once in one place?
- Did you use one term per concept?
- Is the text free of casual speech, exclamations, and difficulty commentary?
- Can the reader tell what to do after reading?

## Exceptions

- If the user names an expert reader, adjust the yardstick to that reader's background knowledge.
- Do not change quoted text, statutory text, or code itself. Apply the lens only to the explanatory text around them.
- Do not replace proper nouns (organization, product, policy, and standard names). Add an explanation block if the reader needs one.
- If the user asks to keep a term, leave it untreated.
