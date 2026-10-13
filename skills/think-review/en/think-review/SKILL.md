---
name: think-review
description: "Checks thinking and documents from first principles. Runs a base check that questions definitions, criteria, scope, and premises down to their smallest units, then adds one specialized lens at a time only when needed. Use it to find holes in plans, arguments, decisions, and ideas, to review reports, proposals, and plans for gaps, inconsistencies, errors, and compliance, or both. Use this skill when the user says 'review this', 'poke holes', 'first principles', 'root cause', '5 whys', 'Heilmeier', 'zero to one', 'user perspective', 'check the logic', 'MECE', 'give me a clear conclusion', 'plain language', 'document review', or 'think-review', or shares a plan or document and asks whether it holds up. Lens files: references/cause.md, references/beneficiary.md, references/plan.md, references/novelty.md, references/argument.md, references/structure.md, references/verdict.md, references/reader.md. Document review procedure: references/review-procedure.md. Read lens files only when needed, one at a time."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# think-review

> This English version was translated from the Korean original. It may behave differently from what the original intends.

Check thinking and documents from first principles. The base check alone exposes most weak points. Add a specialized lens only when a spot needs deeper digging, and add lenses one at a time.

## Terms

Inside this skill, each word below has one meaning only.

- Target: the thought, plan, argument, decision, or document you were asked to check
- Thinking check: work that tests the target's logic and premises
- Document review: work that holds a finished document against criteria to find gaps, inconsistencies, and errors
- Lens: one specialized thinking file in the `references/` folder
- Finding: one problem found during a check

## Deciding the task

Decide the target and the output type first. If you cannot tell, ask the user once.

| Type | When the request is | What to do |
|---|---|---|
| Thinking check | To find holes in a thought, plan, argument, or decision | Run the base check, then add lenses as needed |
| Document review | To check a document for gaps, inconsistencies, errors, or compliance | Read `references/review-procedure.md` and follow it |
| Both | A plan document where logic and document quality both matter | Finish the thinking check first, then merge its results into the document review findings |

The output types are as follows.

- Diagnosis: the user asks for an evaluation, diagnosis, cause analysis, grade, or improvement plan. Report findings.
- Apply: the user names a way of thinking and asks you to write, revise, or review with it, as in "write this from the user's perspective" or "revise this using Heilmeier". Produce only the text in the format the user asked for. Use the checks inside your reasoning only.

When a named way of thinking and a review request come in the same sentence (for example, "review this through the 5 whys"), treat it as Apply.

## Base check

Every task starts here. Finish it before using any lens, so that a lens's framing does not steer the judgment first.

1. Question every premise before you answer. This includes the user's words, your own knowledge, common sense, statements by authorities, famous frameworks, marketing terms, and trends. Questioning means checking the evidence. Accept a premise once its evidence holds.
2. Ask why it is being done, what is being done, how it is done, what the definition is, what the criterion is, and where the scope ends.
3. Check whether the definitions, criteria, and scope are set at the smallest unit. If you can restate them as facts or observations that cannot be split further, they have reached the base unit.
4. Check that each definition, criterion, and scope keeps the same meaning to the end. An argument whose conclusion shifts because a meaning shifted midway is wordplay.
5. Ask whether the target solves the right problem in the first place. If the real purpose behind the request differs from the problem the target solves, that gap is the first finding.
6. Trace the problem to its root before proposing a fix. The root is the point where a change stops the same problem from coming back. Stop tracing when asking "why" again yields no new facts, or when the answer moves into an area the target cannot control.
7. Run the third-party test. A person outside the field should be able to read the conclusion and its evidence and be persuaded. If you cannot persuade that person, rebuild the conclusion.

Do not fill gaps in the target with guesses. Mark anything you cannot confirm as "not confirmed". Search the web only when the user asks for it or allows it.

## Adding lenses

Read a lens when the base check shows one of the signals below, or when the user names a way of thinking.

| Lens file | Question it answers | Signals | Names users may use |
|---|---|---|---|
| `references/cause.md` | Why does the problem happen | Fixes that treat only symptoms, causes that end with blaming a person | 5 whys, root cause |
| `references/beneficiary.md` | Whose situation changes, and how | The subject is an organization or a technology, results are measured by activity counts | user perspective, demand side |
| `references/plan.md` | Does the plan answer every question it must | A missing goal, risk, cost, duration, or checkpoint | Heilmeier |
| `references/novelty.md` | What is new compared with existing options, and where does it focus | Copying a leading case, listing factors with equal weight, putting off the decision | zero to one |
| `references/argument.md` | Does the conclusion follow from the evidence | Conclusions without evidence, logical fallacies, cognitive biases | logic check |
| `references/structure.md` | Are things split and grouped correctly | Lists that mix criteria, overlaps, gaps, confusion between levels | MECE, classification check |
| `references/verdict.md` | Does the conclusion match the weight of evidence | Analyses that end with "both sides have a point", excessive disclaimers | give me a conclusion, no fence-sitting |
| `references/reader.md` | Does the reader get what they need in words they know | Unclear reader, jargon, unclear request | reader perspective, plain language |

Use lenses by these rules.

- Read one lens at a time. When several frameworks enter at once, their criteria blend and the judgment blurs.
- Wrap up one lens's findings before reading the next. Do not carry the previous lens's criteria into the next one.
- If the environment allows it and the user agrees, running each lens in a separate unit (a subagent, a new session, and so on) keeps them apart best.
- If the user names a way of thinking, use only that lens. In that case, shrink the base check to confirming definitions, criteria, and scope.
- If the base check is enough, use no lens.

## Writing the result

For a thinking check delivered as a diagnosis, follow this order. When you used a lens, the lens file's format takes priority.

1. Write only three to five findings, ordered by impact. Listing everything buries the important problems.
2. For each finding, state what the problem is, which part of the conclusion collapses if the problem stands, and how to fix it. You may pose the problem as a question. If you do, also state what collapses when the question has no answer.
3. End with one sentence naming the single weakest piece of evidence that could overturn the conclusion.

For a document review, follow the output format in `references/review-procedure.md`. For Apply, follow the format of the text the user asked for.

## Output guardrails

Checking work tends to invite needless counterexamples, contrast phrasing, and process reports. The rules below block them. Do not spend time polishing sentences.

- Do not mention the skill name, lens names, or the checking process in the result. In a diagnosis, do use the tables or step labels a lens defines.
- Skip contrasts such as "not X but Y" and state Y directly.
- Use counterexamples, paradoxes, and opposing logic only when they change a conclusion or a piece of evidence. Do not add them for show.
- Drop any sentence whose removal leaves the judgment unchanged, and any sentence that serves the writer more than the reader (self-assessment, disclaimers, process reports).

If the user gives separate review criteria, a format, or a reader, those instructions override the defaults in this file.
