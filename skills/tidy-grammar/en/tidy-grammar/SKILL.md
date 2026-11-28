---
name: tidy-grammar
description: "Polishing guidelines for grammar in Korean and English text. Checks agreement between sentence parts, particles, passives and causatives, honorifics, spelling, and spacing, and covers Korean itemized-style (gaejosik) endings, particle omission, and parallel items. For English, covers number agreement, countability and articles, tense and the subjunctive, and list grammar. Supports writing and correcting, and corrects only the grammar within the user's chosen style. When asked for strict mode, it checks each word against dictionaries and language norms. Rules are in references/korean-sentence.md (Korean), references/korean-itemized.md (itemized style), and references/english.md (English). Use this skill when the user asks for '/tidy-grammar', 'check the grammar', 'check spelling', 'itemized-style grammar', 'check nominal endings', 'check agreement', 'polish this text', 'grammar check', 'proofread', 'fix the grammar', or 'strict mode', or asks for a grammar check of a report, proposal, or official document."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# tidy-grammar

> Translation notice: This English edition was translated from the Korean original and may behave differently from what the original intends. The Korean edition holds the authoritative wording.

These guidelines correct grammar in Korean and English writing. They check whether sentence parts fit each other, whether word forms follow language norms, and whether items at the same level share the same grammatical form. No separate norm governs the endings and dropped particles of Korean itemized-style (gaejosik) items, so writers follow convention. A separate reference file states that convention as explicit criteria.

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

The rules in the reference files collect common grammar errors. Apply the tests below to sentences that no rule covers.

| Test | Method | If the test fails |
|---|---|---|
| Restoration | Restore omitted particles, predicates, and subjects, and read whether the result is a complete sentence with the intended meaning | Restore any omission that readers cannot recover, or rebuild the sentence |
| Pairing | Pair the predicate with the subject, object, and adverbial one at a time and read each pair as a short sentence. For coordinated parts, attach the predicate to each part in turn | Change to a predicate that fits the pair, or give each part its own predicate |
| Parallelism | Check whether items at the same level, and parts joined by '와/과', '및', 'and', or 'or', share the same grammatical form | Align the rest to the form the original uses most |

- Use the restoration test on itemized items, English list items, and sentences with omitted subjects. Omission shortens text, but an omission that readers cannot recover erases meaning.
- Check word forms with the rules in the reference files and your knowledge of language norms. When you are unsure of the normative form, keep the original form and list it under "needs confirmation" in the correction summary. A form corrected by guesswork easily becomes a new error.
- Also list under "needs confirmation" any sentence whose fix depends on the author's intent, such as the scope of a modifier.

## How to revise

- Try revisions in this order: replace a particle or ending, supply a missing part, then split or reorder the sentence. Stop at the first step that resolves the error. Smaller revisions keep more of the original wording and rhythm.
- Place each revised sentence beside the original and confirm that facts, figures, strength of claims, and honorific level stay the same.

## Procedure

### Step 1. Identify the conditions of the text

Identify the language, the style (sentence style, itemized style, or mixed), the document type (report, official document, notice, English report, and so on), and any style instructions from the user. When there are no style instructions, take the style used in most of the original as the baseline.

### Step 2. Read the reference files

- If the text contains Korean sentences, read references/korean-sentence.md.
- If the text contains Korean itemized-style items, also read references/korean-itemized.md.
- If the text contains English sentences or English lists, read references/english.md.
- If the task converts itemized-style items into English lists or the reverse, read references/korean-itemized.md and references/english.md together.

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
- Do word forms follow the rules in the reference files, with each allowed variant used consistently throughout the document?
- (Strict mode) Do spelling, spacing, and inflected forms match the norms?
- Do revised sentences keep the original facts, figures, strength of claims, and honorific level?
- Is the corrected text free of the guideline name and any description of the checking process?
