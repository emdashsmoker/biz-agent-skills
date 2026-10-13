# Document review procedure

> This English version was translated from the Korean original. It may behave differently from what the original intends.

Hold a finished document against criteria to find gaps, inconsistencies, errors, violations, and ambiguous wording, then report each with a severity.

## Background

The check items adapt the quality characteristics widely used for requirements documents (complete, consistent, correct, conforming, unambiguous, as in IEEE 830 and ISO/IEC/IEEE 29148) to documents in general.

## 1. Settle the review criteria

Confirm the following before starting. If the input does not tell you, ask the user all at once.

- Document type: report, proposal, plan, contract, questionnaire, application, and so on
- Criteria to check against: checklist, regulations, client requirements, evaluation criteria, template, or an earlier document to compare with
- Which requirements are mandatory and which are recommended
- Who receives the document and what they do with it

If there are no criteria, do not invent any. Ask the user for criteria, or state at the top of the result "No criteria were given, so this is a general quality review".

## 2. Check items

Each item is defined by what it compares against.

| Item | Compared against | Problems to find |
|---|---|---|
| Completeness | The list of items the criteria require | Missing sections, blank fields, promised content left unfilled, missing attachments |
| Consistency | Other parts of the same document | Numbers, dates, names, terms, or claims that differ between parts, a table of contents out of step with the body, figures in tables that differ from the text |
| Accuracy | Facts and source data outside the document | Wrong figures, calculation errors, misquotes, unverifiable sources, wrong names and dates |
| Conformity | Regulations, requirements, evaluation criteria | Violations of format, length, mandatory entries, or submission requirements |
| Clarity | The reader's interpretation | Sentences that can be read two ways, commitments with no owner or deadline, terms used without definition |

- Recalculate figures and totals with code where possible.
- Judge an outside fact as an error only if you confirmed it through material the user provided or a search the user allowed. If you could not confirm it, mark it "needs confirmation".
- Polishing sentences is outside this procedure. Flag a sentence under clarity only when its meaning can split.

## 3. Record findings

Record the following for each finding.

- Location: section heading, page, paragraph, or a short quote
- Severity: one of the levels below
- Problem: what differs from the criteria or the facts
- Impact: what happens if it is not fixed
- Fix: a rewritten sentence or action that can be applied right away

| Severity | Criterion |
|---|---|
| Critical | The document fails its purpose, or a mandatory requirement is violated so that it may be rejected, eliminated, or cause legal trouble |
| Major | The document serves its purpose but clouds the reader's judgment or lowers trust |
| Minor | Fixing it helps, but it does not affect judgment |

Separate confirmed problems from assumptions. Write problems confirmed against the source text and criteria as findings. List items you cannot judge for lack of material separately as items needing confirmation.

## 4. Output format

```
## Overall
(One sentence judging whether the document can be submitted or used, and one or two sentences of reasoning)

## Findings
| No. | Location | Severity | Problem | Impact | Fix |
|---|---|---|---|---|---|

## Items needing confirmation
- (Items the user must answer or supply material for before they can be judged)
```

- List findings in order of severity (critical, major, minor).
- For long documents, cover high-impact findings first. Do not list minor wording fixes at length. If there are many minor items, give a few representative cases and the total count.
- If a thinking check ran alongside, put its findings on logic and premises in the same table with severities.

## Principles

- Keep the author's intent. A review looks for risks and improvements. Do not rewrite the document to the reviewer's taste.
- Do not invent criteria or regulations.
- Do not fill gaps in the source with guesses.
