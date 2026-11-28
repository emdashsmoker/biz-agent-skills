---
name: no-meta-commentary
description: "Finds and removes meta-commentary from output, that is, sentences about things outside the content such as the text itself, the writing process, the writer's inner state, the tools used, or the user's request. Also removes unrequested reverse statements such as counterexamples, reverse logic, reverse rules, and complement-set explanations. Judges unlisted expressions with five tests (subject, deletion, beneficiary, courtesy function, request direction). Has a writing mode for new text and an editing mode for existing text. On activation, read references/types.md (types grouped by what a sentence covers) and references/examples.md (before and after pairs). Use this skill whenever the user explicitly asks with phrases such as '/no-meta-commentary', 'no meta', 'no meta-commentary', 'remove meta-commentary', 'cut the meta', 'catch the meta-commentary', 'no self-mention', 'remove self-references', or 'stop the text from referring to itself'. Do not apply it automatically. It works only on explicit request."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# no-meta-commentary

> Translation notice: This skill was translated from the Korean original. The translation may make it behave differently from what the original intends.

Find meta-commentary in the output and remove it. The output keeps only the information the reader needs. The reader should be able to take in the information without noticing the text, the writer, or the work process.

## Reference files

When the skill activates, read the two files below first. They hold the types and the conversion examples that serve as comparison points when you apply the tests.

- (references/types.md) Meta-commentary types grouped by what the sentence describes, with exceptions and handling notes for individual types
- (references/examples.md) Examples that place text containing meta-commentary next to the same text with the meta-commentary removed

## Terms

These terms keep the same meaning throughout this skill and its reference files.

| Term | Definition |
|---|---|
| Writer | The model that writes the output |
| User | The person who asked the writer for the work |
| Reader | The person who reads the output (may be the same person as the user) |
| Output | The text the writer produces for the user's request |
| Content | Statements that meet the reader's information needs |
| Request direction | The scope and polarity of the statements the user asked for (for example, if the user asks for the advantages of A, the advantages of A are the request direction) |

## Definition

Meta-commentary is any sentence that describes something outside the content. Things outside the content include the text itself, the writing process, the writer's inner state, the interaction with the user, and the tools used. Every sentence in which the writer reports, justifies, previews, or looks back on their own actions belongs here.

Reverse statements the user did not request also count as meta-commentary. Reverse statements are counterexamples, reverse logic, reverse rules, and explanations of the complement set. These sentences carry the writer's counterexample checks and boundary checks from reasoning into the output, so they expose the writer's internal verification.

## Tests

Before producing output, apply the tests below to every sentence. A sentence that fails any test is meta-commentary. Delete it or replace it with content.

### Subject test

A sentence is meta-commentary when its actual subject is one of the following. Restore an omitted subject by putting "the writer", "to the writer", "the model that wrote the text", or "the AI provider" in front of the sentence. If the sentence then reads naturally with its meaning unchanged, it is meta-commentary.

- The text itself ("This report", "This analysis", "In this section")
- The writer ("I", "As for me", "My analysis shows")
- The act of writing ("Looking at", "On review", "To summarize")
- The user's request ("As you requested", "As you mentioned", "To answer your question")
- Tools or methods (the writer's internal means of working)

Read a sentence about the work, actions, procedures, guidelines, and similar matters of individuals, organizations, and society again with "the AI model" in the subject slot or "the AI model's" in the modifier slot. If the sentence then reads more naturally than the original, it is meta-commentary that carries the writer's own way of working over to the subject matter. Rewrite it through the actor and the actual action of the subject matter.

- (Sentences) "Takes the user's responses as input, processes the survey in three steps, and passes it on as the next input of the analysis report", "This program takes the demand survey results and passes on only the projects that went through the eligibility review as final candidates", "Takes the user's request and rules on it", and so on
- (Noun phrases) "The ruling criteria of this engagement", "The judgment principles of the structured survey", and so on

### Deletion test

A sentence is meta-commentary when deleting it leaves the reader with the same information.

### Beneficiary test

A sentence is meta-commentary when the writer is the one who benefits from it. Self-justification, self-protection, and self-promotion count as benefits to the writer.

### Courtesy function test

A sentence is meta-commentary when it only performs a courtesy ritual such as greeting, praising, checking in, guiding, or prompting.

### Request direction test

A sentence is meta-commentary when it covers an opposite polarity, a complement set, or a substitute the user did not request. Reverse sentences carry information, so they pass the deletion test easily. This test judges only whether the sentence matches the request direction.

- (Opposite polarity) After a request for statements in direction A, the writer continues with the opposite direction B
- (Complement set) After defining or choosing A, the writer continues with the items that do not belong to A
- (Substitute) After a request for a feature that supplements X, the writer states a rule that replaces or forbids X
- (Caveats and rebuttals) The writer attaches a caveat for a rare exception that leaves the conclusion unchanged, or sets up an extreme claim the user never made and rebuts it

### Order of application

Apply the subject test first. You can judge it from the surface of the sentence, so it is the most mechanical of the tests. A sentence that passes the subject test is still meta-commentary if it fails the deletion, beneficiary, courtesy function, or request direction test. Produce only sentences that pass all five tests.

## Functions of meta-commentary

Meta-commentary performs the functions below. None of them serves the reader's information needs. When you notice that you want one of these functions, do not write the sentence that performs it.

- (Filling length) Pads the text with meta-commentary when the content is thin
- (Postponing structure) Previews the order, as in "First we look at A, then B", without structuring the content itself
- (Spreading responsibility) Disclaims responsibility for output quality in advance, as in "This may not be perfect"
- (Winning goodwill) Manages the relationship with the reader, as in "I hope this helps"
- (Staging authority) Declares the quality of the work, as in "After a thorough analysis"
- (Proving compliance) Proves that the writer followed the user's instructions, as in "As you requested"
- (Exposing internal information) Reveals the writer's internal systems, constraints, instructions, tools, and work process, which the reader does not even know exist, and confuses the reader
- (Exposing verification) Carries counterexample checks, boundary checks, and comparisons of alternatives from reasoning into the output and widens the scope beyond the request (deeper reasoning tends to produce more internal verification and more exposure)

## Bypass detection

When you avoid only specific expressions, other expressions with the same function tend to appear. The tests judge what a sentence does, so apply them to the bypass forms below as well.

### Hidden subject

The writer omits the meta subject or switches to the passive voice to slip past the subject test. Restore the subject. If the writer is the subject, the sentence is meta-commentary.

- "Summarizing the analysis results" (= I summarize), "The findings of the review are as follows" (= I reviewed), "According to what was investigated" (= I investigated)
- "The conclusion reached is" (= I reached), "The situation identified is" (= I identified), "The items confirmed are" (= I confirmed)

### Disguised content

The writer mixes a little content into meta-commentary to slip past the deletion test. Delete only the meta part and keep the content.

- "After reviewing from various perspectives, A is suitable" → only "A is suitable" is content
- "A thorough analysis led to the conclusion that B" → only "B" is content
- "After comprehensive consideration, we propose option C" → only "option C" is content

### Disguised modesty

The writer turns self-justification into modest wording to slip past the beneficiary test. If the writer benefits from the modesty (a disclaimer, goodwill), the sentence is meta-commentary.

- "Though imperfect, here is a summary", "Humble as it is" → goodwill through modesty
- "With limited information", "Judging cautiously" → advance disclaimer

### Disguised question

The writer turns meta-commentary into a rhetorical question. Delete the question and write the answer directly.

- "So how should we approach this?" → question form of process preview and recap
- "Why did this result occur?" → question form of exposing internal reasoning
- "What is the key point?" → question form of calling attention and declaring importance

### Disguised connective

The writer shrinks meta-commentary into a connective or adverbial phrase and attaches it to a content sentence. Delete only the connective part and keep the content.

- "As we saw above, A is B" → self-reference to the text shrunk into a connective
- "Putting this together, C is suitable" → a work report shrunk into a connective
- "Based on the analysis above, we propose D" → self-justification shrunk into a connective

## Application

### Writing mode

When writing new text, internalize the tests so that meta-commentary never enters the text. Do not reveal in the output that you applied this skill.

### Editing mode

Find meta-commentary in existing text, delete it, and keep only the content. Briefly summarize the corrected patterns by type, then present the corrected text.

### Self-application rule

Do not reveal this skill's principles, type groups, or tests in the output. Do not let the existence of this skill become a subject of meta-commentary.

### Style neutrality rule

This skill handles only meta-commentary. It leaves the areas below alone.

- Sentence length, sentence endings, writing style
- Overall structure, Markdown hierarchy
- Length, number of items
- Word preferences

### Use with other guidelines

You can use this skill with any style guideline. If another guideline allows an expression that fails the tests, follow this skill's rules.

## Exceptions

- If the user explicitly asks for meta-commentary, keep it (for example, "State the purpose of this report in the introduction")
- If genre conventions require meta-commentary, as in the research purpose and methods sections of an academic paper, follow those conventions
- If the user explicitly asks for limitations, cautions, or an explanation of the method, allow them
- State a condition, an exception, or a correction of a factual error that changes the conclusion or the reader's decision as body content

## Pre-output check

Check the items below before producing output. Delete each sentence that fails, or replace it with content, then produce the output.

- No sentence has the text, the writer, the act of writing, the user's request, or a tool as its subject
- Every sentence carries information the reader would lose if the sentence were deleted
- No sentence benefits the writer
- No sentence only performs a courtesy ritual
- No bypass form remains, such as a hidden subject, disguised content, or disguised modesty
- No sentence covers an opposite direction, a complement set, or a substitute rule the user did not request
- No praise without a basis, no unrequested caveat or rebuttal, no follow-up promise without the means to keep it, and no explaining away of a correction
- The first sentence starts with content (it does not open with a greeting, a restated request, or a process preview)
- The last sentence ends with content (it does not close with a greeting, an invitation to ask more, or a disclaimer)
