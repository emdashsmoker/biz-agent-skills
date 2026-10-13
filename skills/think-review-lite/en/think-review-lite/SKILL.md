---
name: think-review-lite
description: "Checks the soundness of thinking (plans, arguments, decisions, cause analyses) and the quality of documents (reports, proposals, project plans). Starts with a first-principles base check and adds the Cause (5 Whys), Plan (Heilmeier questions), Beneficiary, Novelty (Zero to One), Argument, Classification (MECE), Conclusion, Requirements, Consistency, Accuracy, or Reader lens only when needed. When the user names a lens, checks with that lens only. Use this skill when the user says '/think-review-lite', 'review this', 'find the holes', 'push back on this', 'check the logic', 'is this sound', 'review my plan', 'review this document', 'what is missing', 'does it meet the requirements', 'root cause', 'use 5 whys', 'use the Heilmeier questions', 'Zero to One lens', 'from the beneficiary view', 'MECE check', 'give me a conclusion', 'does this fit the reader', or shares a thought or document and asks about its soundness, gaps, or completeness. Do not use it for requests that only polish sentence wording."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# think-review-lite

> This English version is a translation of the Korean original. It may behave differently from the original intent.

Find the gaps in a thought or a document and give a direction for fixing them. Every check starts with the base check. Add a lens only when the base check reveals a gap it cannot judge on its own.

## Terms

| Term | Meaning |
|---|---|
| Target | The thought or document the user hands over for checking |
| Base check | The first-principles check applied to every request |
| Lens | A set of check questions that looks deeper at one kind of gap |
| Finding | A point in the target that needs work, backed by evidence in the target |
| Needs verification | A matter whose truth cannot be decided from the target and the available material |

## Scope

| Request | Signal | Applies |
|---|---|---|
| Thinking check | The user gives an idea, plan, argument, decision, or cause explanation and asks whether it holds or where it breaks | Base check, plus content and reasoning lenses as needed |
| Document review | The user gives a finished document and asks about requirement fit, omissions, consistency, accuracy, or completeness | Base check, plus every document lens whose signal is present |
| Combined check | The user gives a document and asks for a review without limiting its scope, or asks about both the content logic and the document quality | Both the thinking check and the document review |

If the user asks you to write a new text or plan through a specific lens, do not produce a review report. Apply that lens's check questions while writing and deliver only the requested output. Keep question numbers, verdict tables, and lens names out of that output.

Sentence wording (word choice, style, filler) is outside the scope of the check. Handle wording only when it blurs meaning. That covers one word used in two senses and references whose target is unclear.

## Workflow

1. Secure the target. If there is none, ask for the thought or document to check.
2. Fix the basis. Confirm the target's purpose, reader, scope, and judgment criteria. Infer anything the user did not give from the target itself and record the inference under Review basis in the result. Do not stop the work to ask questions at this step.
3. Run the base check.
4. Add lenses following the lens selection rules.
5. Assign a severity to each finding and settle an overall verdict on the target.
6. Write the result following the output format and output principles.

## Base Check

The base check applies first-principles thinking in a simple way. Trace the premises the target relies on down to their most basic units and question whether the conclusion built on them holds.

- Doubt every premise. The target's claims, the premises inside the user's request, and the checking model's own knowledge are all subject to checking.
- When a finding rests on the model's own knowledge, verify it if a means of verification (search, cross-checking material, calculation) is available. If none is available, classify it as needs verification.
- Ask why, what, and how. A missing answer, or three answers that do not fit together, is a finding.
- Check definitions, criteria, and scope. See whether each key term is defined at a basic unit that cannot be broken down further, whether judgment criteria are stated, and whether the scope is set. Also see whether each definition, criterion, and scope keeps the same meaning from start to finish once set.
- Do not accept common sense, authority, famous frameworks, trends, or marketing terms as evidence by themselves. Check separately the facts and evidence they point to.
- Write down what must be true for the conclusion to stand. Any of those conditions that is unconfirmed is a hidden assumption.
- Follow the problem to its root before proposing a fix. Also ask whether the problem the target tries to solve is the problem that needs solving.
- A finding must convince a third party who hears it. Wordplay and distinctions between expressions that mean the same thing do not count as findings.

## Lens Selection

### Named Lenses

If the user names a lens or method, apply that lens only. If the user names several, apply all of them. The principles of the base check remain the premise when applying a named lens.

| Lens | Names users often use |
|---|---|
| Cause | 5 Whys, root cause, cause analysis |
| Plan | Heilmeier, Heilmeier catechism, plan feasibility |
| Beneficiary | demand side, beneficiary view, user's perspective |
| Novelty | Zero to One, challenge conventional wisdom, vertical progress, copy or creation |
| Argument | logic check, logical fallacies, evidence check |
| Classification | MECE, classification check, ontology view, outline structure |
| Conclusion | fence-sitting check, give me a conclusion, which side is right |
| Requirements | requirement fit, missing items, template compliance |
| Consistency | cross-check numbers, internal agreement |
| Accuracy | fact check, source check |
| Reader | reader fit, jargon check, fit for the audience |

### No Named Lens

In a thinking check, finish the base check first. Add a content or reasoning lens only when a gap found by the base check belongs to that lens and the target shows that lens's signal. Do not add a lens for a gap the base check has already judged. Add at most three lenses at a time, in order of impact.

In a document review, apply every document lens whose signal is present. The document lenses are the standard set for a document review. In a combined check, apply the document lenses by this rule and add content and reasoning lenses by the thinking check rule.

| Group | Lens | Signal |
|---|---|---|
| Content | Cause | Explains the cause of a problem, incident, failure, or worsening indicator, or proposes a countermeasure |
| Content | Plan | Proposes starting a project, program, policy, or initiative |
| Content | Beneficiary | Claims that a policy, service, or technology gives value to someone |
| Content | Novelty | Claims newness, competitive advantage, or superiority over existing options, or sets a strategic direction |
| Reasoning | Argument | Makes claims backed by evidence or claims causation |
| Reasoning | Classification | Splits or groups items, presents an outline or structure chart, or defines terms |
| Reasoning | Conclusion | Compares options or positions, or answers a question that calls for a judgment |
| Document | Requirements | A standard to follow exists (template, request for proposal, statement of work, checklist, regulation) |
| Document | Consistency | Numbers, dates, names, or cross-references appear in several places |
| Document | Accuracy | Presents facts, statistics, quotations, or sources |
| Document | Reader | Someone other than the author will read it, or it uses jargon |

## Content Lenses

### Cause

Follow the 5 Whys technique used in the Toyota Production System. Sakichi Toyoda devised it and Taiichi Ohno systematized it at Toyota. Start from the symptom and repeat "why" until you reach a cause whose removal prevents recurrence.

- Define the starting problem as one observable phenomenon. Keep causes and solutions out of the problem definition. If several problems are tangled together, split them and analyze one at a time.
- If the user stated a problem, start from it. If the user gave only a plan, draw the starting problem from its background or its description of current problems. Put the starting problem at the top of the result so the user can correct it.
- Repeat "why" while checking that each answer is the cause of the answer right before it.
- Stop at the point where removing that cause keeps the problem from returning. Also stop when further questions yield no meaningful answer or reach an area the target cannot control. Use three to seven rounds as needed. Do not stretch or cut the chain to make it exactly five.
- If a person's mistake comes up as an answer, ask once more what procedure or structure allowed that mistake. Do not end by naming someone to blame.
- Once the chain is complete, read it back from the root cause to the problem as "A, therefore B" and confirm no step was skipped.
- If causes branch, finish the chain along the most likely branch and list the other branches as candidates for separate analysis.
- Do not invent causes the target gives no evidence for. Mark them as hypotheses to verify when needed.
- Deliver the root cause and the direction of the fix as a pair. If the target's countermeasure only removes the symptom, record it as a finding.

### Plan

Use the list of questions created by George H. Heilmeier, director of DARPA from 1975 to 1977, rewritten in domain-neutral terms. The questions come from research and development planning, and they apply unchanged to other plans such as building facilities, designing policies, or setting organizational strategy.

| No. | Question | What to check |
|---|---|---|
| 1 | What are you trying to do? | Does it explain the goal without jargon? |
| 2 | How is it done today, and what are the limits? | Does it cover current practice, the state of the art, the options considered, and the limits of each? |
| 3 | What is new, and why do you think it will succeed? | Does it state how it differs from existing practice and give grounds for expecting success? |
| 4 | Who cares, and what difference will success make? | Does it state the beneficiaries, the need and urgency, and the before and after change in measurable terms? |
| 5 | What are the risks? | Does it cover failure factors, side effects, and second-order effects that follow success? |
| 6 | How much will it cost? | Are the amount and its basis appropriate for the goal? |
| 7 | How long will it take? | Are the schedule, the approach (top-down or bottom-up), the responsible parties, and the stages appropriate for the goal? |
| 8 | What are the mid-term and final checks? | Are interim goals, final goals, and measures set? |

- Give each question one verdict: Met, Partly met, Not met, or Not stated.
- Met means the target contains a logically complete answer with concrete evidence. Partly met means an answer exists but lacks specifics or skips steps in its logic. Not met means the answer has a serious logical flaw. Not stated means the target has no answer.
- Back each verdict with the relevant part of the target text. Do not fill gaps with guesses. Do not grade leniently.
- Check coherence across questions. Confirm that what is new in question 3 addresses the limits in question 2, that the change in question 4 is measured by the measures in question 8, and that the resources in questions 6 and 7 match the scale of the goal in question 1.

### Beneficiary

Check whether the target starts from the supplier's position (the planner, the technology) or from the problems and changes the final beneficiary experiences.

- Trace the final beneficiary to the end. The final beneficiary is the person who faces the actual problem when the means is absent. Treat those who build or run the means (the responsible department, developers, the manager who decides to adopt it) as intermediate operators. Even when the service passes through an institution or a company, follow it down to the citizens or consumers who finally use it.
- The final beneficiary of a job training subsidy is the job seeker who must finish training and find work. The final beneficiary of a bank's security solution is the depositor and customer who need safe transactions.
- Record a finding when supplier-side wording leads in any of the items below.

| Item | Supplier-side wording | Beneficiary-side wording |
|---|---|---|
| Subject | The planner or the technology is the subject of sentences and headings | The final beneficiary is the subject |
| Problem definition | The supplier lacks capacity, infrastructure is missing, or the technology has internal limits | The inconvenience and loss the beneficiary suffers |
| Solution | Supplier actions such as building a center, developing a platform, or designing an architecture | Changes in the beneficiary's situation (time saved, cost cut, tasks that were impossible before) |
| Performance measure | Budget execution rate, number of projects, number of participants, technical benchmarks | Before and after change in the outcomes the beneficiary experiences |
| Grounds for need | Higher-level plans, institutional mission, academic importance | Demand surveys, complaints, usage data, field cases |

- Do not treat supplier logic and technical measures as material to delete. Propose putting the beneficiary's change first and placing supplier logic and technical measures after it as supporting evidence.
- A text that explains how a technology works may keep the technology as the subject. In that case, propose opening the paragraph with the situation the beneficiary faces.
- In improvement proposals, call beneficiaries by specific names (patients, job seekers, small business owners, depositors, and so on). Avoid generic labels such as "beneficiaries", "users", or "stakeholders". If a job title (developer, analyst) refers to the operator of the means, trace further to whoever uses that person's output.
- If the user set the reader, treat that reader as the beneficiary. The less expert the beneficiary, the larger the share of why it is needed and the smaller the share of how it works. Keep essential content such as working principles and constraints.
- Propose changing the perspective only, and keep the original facts, numbers, and institution names. Do not create data the original does not contain.

### Novelty

Turn the thinking principles in Zero to One (2014) by Peter Thiel and Blake Masters into check questions. Check whether the target repeats existing options or commits to a new conclusion.

- Check conventional wisdom. Is there any part of the conclusion most people would not agree with? If the conclusion matches conventional wisdom, is the basis of that wisdom confirmed as fact? Does the target use the fact that many agree as evidence? Does a conclusion that departs from conventional wisdom carry stronger evidence than conventional wisdom has? Do not make choosing the opposite of conventional wisdom a goal in itself.
- Check the gap. Does the target name the best existing option? Is the difference large enough to remove the reason to use the existing option? Is the structure the same with only the name changed? Copying an existing option is allowed, but the target must say it is a copy and give the reason for copying. If the gap cannot be measured in numbers, judge by whether the target can replace the existing option.
- Check the dominant variable. Does the target identify the one variable that decides most of the outcome and give grounds for it? Does it list factors with equal weight? If their real weights are similar, listing them side by side is fine. Does it narrow the scope to the smallest unit it can command and state a path for expanding from there?
- Check definiteness. Does the target specify who achieves what and by when? Does it only list options and postpone the decision? Does it fix definitions, scope, and criteria at the start? Is there a reason the conclusion will last? Is there a delivery path by which the conclusion reaches those who need it? If the decision must wait, does it state the conditions for waiting and when to decide again? Accept experiments built on a hypothesis as a way to test the design.
- If the user asked for a copy of an existing option or for a list of options itself, do not treat the matching item as a problem. If conventional wisdom is verified fact, adopting it as the conclusion is fine.

## Reasoning Lenses

### Argument

- Check that every conclusion has evidence attached. Check that the conclusion follows from the evidence and that tracing back from the conclusion leads to the same evidence.
- If a conclusion goes beyond the reach of its evidence, propose narrowing the conclusion. If a conclusion is too narrow to support a decision, propose strengthening the evidence.
- The burden of proof lies with whoever makes the claim. Rejecting something because it is unproven, or accepting it because it is unrefuted, is a finding.
- Check that the claim can be falsified. Do not treat a claim that no result could ever prove wrong as a checkable claim.
- Check separately whether the form of the inference is valid and whether the premises are true. Even a valid form cannot make the conclusion trustworthy if a premise is false.
- If the target set a hypothesis and then gathered material, check whether it revised the hypothesis when contrary material appeared.
- Check for the fallacies and biases below. The names are standard terms in logic and cognitive psychology.

| Group | Fallacies to check |
|---|---|
| Formal | Denying the antecedent, affirming the consequent (only the contrapositive of a conditional is valid), affirming a disjunct, undistributed middle, four terms, modal confusion |
| People and circumstances | Appeal to authority (including authority from another field, anonymous authority, and authority with a stake), ad hominem, tu quoque, circumstantial ad hominem, guilt by association, appeal to pity, appeal to force, appeal to wealth, appeal to the crowd, appeal to moderation (treating the arithmetic middle as the answer), appeal to ridicule, tone policing, genetic fallacy, appeal to tradition, appeal to novelty |
| Meaning | Equivocation (one word in two senses within one argument), vague reference, use-mention confusion, persuasive redefinition, accent fallacy, straw man, quoting out of context, reification by naming, treating a metaphor as fact, loaded language |
| Causation | Post hoc (treating sequence as cause), ignoring a common cause, reversed causation, single-cause reduction, false analogy, false equivalence, gambler's fallacy, conjunction fallacy, base rate neglect, confusing ends and means, inflating intent |
| Generalization and category | Hasty generalization, generalizing from a biased sample, hidden qualifier (concluding about all from "most"), accident fallacy, confusing principles, fallacy of composition, fallacy of division, fallacy of the peak, no true Scotsman, distinction without a difference, category error |
| Point of dispute | Red herring, irrelevant conclusion, removing the issue instead of solving it, poisoning the well, appeal to ignorance, personal incredulity, slippery slope (no evidence for the middle steps), false dilemma, black-and-white thinking, nirvana fallacy, loaded question, special pleading, argument by repetition, circular reasoning (begging the question, tautology, circular definition), using a flaw in the opposing argument as proof that its conclusion is false |
| Fact and value | Deriving ought from is, deriving is from ought, wishful thinking, stretching a counterfactual beyond its assumption, adding an ad hoc assumption for each rebuttal |
| Cognitive bias | Confirmation bias, cherry picking, availability bias, representativeness bias, survivorship bias, halo effect, anchoring, proximity bias, backfire effect, selection bias, out-group homogeneity bias, rosy retrospection |

### Classification

- Before judging a classification, confirm its purpose and conditions. See what decision the classification supports, how far the scope reaches, whether the criterion has one dimension, and whether every case in scope can be placed.
- Check the criterion. Items from different dimensions mixed at one level are a finding. If items by technology and items by urgency sit at one level, propose splitting the levels into a staged classification.
- Check overlap. If one case falls into two items at once, propose redrawing the item boundaries or merging them under a higher item. If overlap cannot be avoided, propose handling it as attribute tags instead of a classification and saying so.
- Check omissions. A case that fits no item is a finding. If "other" is larger than the main items, propose setting a new criterion.
- Check the number of items. For classifications that support decisions, three to four items per level is recommended. Above five, check whether a middle level is missing. At two, check for a false dichotomy. Systems where many items are natural, such as biological taxonomy, industry classification codes, or legal article structures, are not defects.
- Check relationships. Confirm whether each parent and child item is a kind relationship ("X is a kind of Y"), a part relationship ("X is part of Y"), or an attribute relationship ("Y has X"). If different relationships are mixed at one level, propose separating them. In a kind relationship, the attributes of the parent must hold for the child.
- Check depth. Three levels or fewer is recommended, and at four or more, check again whether the middle levels are needed. Systems where deep levels are natural, such as administrative districts, are not defects.
- Distinguish missing information. "Not confirmed" and "does not exist" are different. Assert "none" only within a range that was checked exhaustively, and state that range and its basis.
- Check format bias. Bending the real classification to fit a chart, framework, or template is a finding.
- Find isolated items and empty categories. Propose reconsidering where an item with no relationship to any other item belongs. Propose deleting a category with no cases, or stating the grounds on which it will be filled.
- Check new items. If items were added to an existing system, check whether their relationships to existing items (parent, child, peer, dependency, sequence) are stated. If a new item creates overlap, propose setting a new criterion.
- Check how relationships are described. Confirm that the direction (the effect of A on B and the effect of B on A are separate), the type (causation, correlation, dependency, or simple association), and the cardinality (one-to-one, one-to-many, many-to-many, required or optional) are stated. For relationships lumped together as "related", propose specifying the type.
- Check definitions. If the defined word or a derivative of it appears in its own definition, the definition is circular. Propose redefining it through a broader concept, its components, its purpose, or its attributes.
- Do not treat rankings or simple lists as classifications. If the user set the classification criterion, follow it and point out any defect you see.

### Conclusion

- Check whether the target ends with a conclusion that has a direction. Apply the same standard when writing the review result.
- If any of the expressions below sits where the conclusion should be, treat the conclusion as missing. If the same expression appears as a condition or caveat after a conclusion is given, do not treat it as a problem.

| Type | Examples |
|---|---|
| Partial agreement without scope | It has a point, it is half right, it is not wrong |
| Equal credit to both sides | Each has pros and cons, a double-edged sword, both an opportunity and a threat |
| Deferral without reason | It depends on the situation, hard to say, too early to tell |
| Compromise without grounds | A balanced approach is needed, the two views should be harmonized |
| Replacing the conclusion with further work | A comprehensive review is needed, more research is needed |
| Handing off the judgment | Left to the reader's judgment, each should decide for their own situation |

- Check whether the two positions were forced into equal length and equal modifiers even though their evidence differs in weight. Check whether deferral expressions repeat two or more times.
- Weigh evidence by quality. The order is logical soundness, explanatory power about causes, resistance to counterexamples, rigor of empirical method, and fit of scope. If an earlier criterion decides which side is stronger, conclude in that direction regardless of the later criteria.
- Do not weigh evidence by the number of pieces, their length, the number of people who agree, citation counts, or the number of authorities.
- Rebuild the opposing position in its strongest form before evaluating it. Accept as a conclusion only what still stands against that form.
- Place counterarguments under the conclusion and use them to adjust the conclusion's range.
- Accept conditional conclusions as conclusions. "On current evidence A fits, and we revisit if X changes" is a conclusion. Do not treat a deferral without direction as a conclusion.
- A conclusion may wait only when all three conditions hold. The evidence on both sides must be lacking. The target must state which evidence, once secured, would settle the conclusion. The target must state which way current evidence leans.
- If the user asks for a summary of both positions or a neutral summary, do not force a conclusion. For legal questions without settled precedent, a deferral as "interpretation not settled" is fine, with majority and minority views distinguished. If a decision maker asks for a comparison of options, give a recommendation and state that the final choice rests with them.

## Document Lenses

### Requirements

- Confirm the document type, the standard to follow (template, request for proposal, statement of work, checklist, regulation), the required and recommended requirements, and any reference template to compare against.
- If a standard exists, compare item by item. Check whether required items are present, whether the required format is followed, and whether each evaluation or scoring item has matching content.
- If no standard exists, do not invent requirements. Proceed as a general quality review and record that under Review basis.
- Record missing items as Not stated and do not fill them with guesses.

### Consistency

- Check whether the same information agrees everywhere in the document. This covers numbers, units, dates, periods, names of people and institutions, abbreviations, tables against text, summary against body, table of contents against body, figure and table numbers, and cross-references.
- Recalculate totals, ratios, and growth rates if a calculation tool is available.
- Whether each term keeps one meaning is checked in the base check.

### Accuracy

- Check whether facts, numbers, and quotations match their sources. Record quantitative data with no source, or with a source that cannot be traced, as a finding.
- When looking at a source, check whether it produced the original data, whether the publisher is independent of the subject in interest, and whether its method and sample can be traced.
- Classify matters that cannot be judged true or false for lack of a means of verification as needs verification, and do not assert they are wrong.

### Reader

- Identify the reader. Confirm who reads it, what they decide or do after reading, and what they already know. If the user did not specify, infer it from the document's purpose and distribution.
- Check the order. See whether what the reader must know first (the conclusion, the request, what changes for the reader) comes first. See whether details the reader does not need for the decision bury the conclusion. See whether the document states what it does not cover.
- Check the level. The less expert the reader, the larger the share of why it is needed and the smaller the share of how it works. Keep essential content such as working principles and constraints even at a lower level.
- Unless the user specifies otherwise, the baseline reader for terms is an average adult without a degree in the field. This person studied school subjects but no longer remembers the details, and does not know field-specific academic knowledge, industry conventions, or internal abbreviations. Use the baseline reader only to judge terms, and do not use it as grounds for lowering the document's formality.
- Ask two questions about each term. Does the reader understand it without a definition? Is the term needed? Treat words learned in daily life as known and words learned only by studying a field as unknown. Treat a word that looks like an everyday word but carries a different meaning in the field (such as "significant" in statistics) as jargon. An English abbreviation needs its full name at first use.
- Propose term handling in this order. Delete terms that do not contribute to the conclusion. Replace a term with plain words if it can be done without losing meaning. Keep an essential term that plain words would fail to distinguish from other things, and attach a definition at its first appearance.
- Do not propose changes that lose information in the name of plain language (such as turning "supplementary budget" into "a money-related measure") or that drop the level of formality. If one concept goes by several terms, propose unifying them into one.
- If one document targets several readers whose needs conflict, record the conflict as a finding and propose separating the versions by reader. If the user asks for a rewrite for a different reader, keep the facts as they are and write each reader's version separately, changing only order and level.

## Judgment

| Severity | Criterion |
|---|---|
| Critical | Left unfixed, the target's conclusion or purpose does not hold, or a required item is not met |
| Major | The conclusion holds, but weaker evidence or persuasiveness could change the reader's judgment |
| Minor | No effect on the judgment, only clarity or polish improves |

- Keep confirmed problems apart from items that need verification. Do not assert that an item needing verification is a problem.
- Write the overall verdict with a direction, following the Conclusion lens standard. Verdicts such as usable as is, usable after revision, or core premises need rethinking fit here.
- If nothing needs fixing, say so. Do not invent weaknesses to fill the review format.

## Output Format

Write the result in the language the user wrote in. Unless the user asks for a file, write it in the response body.

```
## Overall verdict
(One sentence judging the target's state, one sentence on what to fix first)

(Review basis) Purpose, reader, and the standard applied. Include when inferred or when a general quality standard was used

## Revisions
| Severity | Location | Problem and grounds | Fix direction |
|---|---|---|---|

## Needs verification
(Only when present. Information to get from the user or facts to confirm)
```

- List revisions in the order Critical, Major, Minor. Do not pile up trivial points that do not change the verdict, and group Minor items briefly.
- For location, use whichever is easiest to find: section heading, page, paragraph, or a short quotation. In a thinking check, give the relevant claim or assumption.
- In the problem and grounds column, state why the problem affects the verdict.
- Make the fix direction concrete enough to act on right away. If the user asks, add a rewritten example.
- If the user names the Cause lens, put a table before the revisions with the starting problem, each "why" and its answer, the root cause, and the fix direction.
- If the user names the Plan lens, put a per-question verdict table (question, verdict, evidence from the target text) before the revisions. In the revisions, give the current state and improvement direction for every question not rated Met, and add a verdict on coherence across questions.
- Name headings and subheadings after the target's content. Use lens names and method names only when the user named them.
- Do not change the target's facts, numbers, or the author's intent.

## Output Principles

- Write only the check results. Leave out that a lens was applied, the check procedure, and any self-assessment of the result's completeness.
- Instead of a contrast sentence of the form "not X but Y", state Y directly.
- Raise only problems whose grounds you confirmed in the target. Do not create hypothetical counterexamples absent from the target, or inverse rules and paradoxes the user did not ask for.
- Do not replace the verdict with disclaimers or advice to consult an expert. Only when a judgment requires professional qualifications, such as law, medicine, or investment, add one sentence at the end, and do not repeat it within the same conversation.
- Do not attach moral lectures unrelated to the request.
