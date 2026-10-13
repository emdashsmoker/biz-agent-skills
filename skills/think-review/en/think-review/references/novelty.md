# Novelty lens

> This English version was translated from the Korean original. It may behave differently from what the original intends.

Check whether a conclusion restates conventional wisdom, copies an existing option, lists factors with equal weight, or puts off the decision. Use it in the reasoning behind analysis, planning, writing, design, and decisions, beyond business planning.

## Background

This lens turns ideas from Peter Thiel and Blake Masters' book "Zero to One" (2014) into questions for checking thought. The ideas come from a startup context, so outside business, read "market" as "the target area" and "competitor" as "the existing option".

## Principles

### 1. Testing conventional wisdom

Agreement by the majority is no proof of truth. Restating an agreed conclusion creates no new information. Every field still holds facts nobody has found.

| Test question | Violation pattern | Treatment |
|---|---|---|
| Which part of this conclusion would most people disagree with? | Adopting conventional wisdom as the conclusion without evidence | Demote the conventional view to a hypothesis, then check its evidence |
| If the conclusion matches conventional wisdom, what is that wisdom's evidence? | Using majority opinion as proof | Remove the majority opinion and keep only factual evidence |
| What supports the assumption that this field has been fully explored? | Ending the search on the assumption that nothing is left to find | Look for evidence where most people do not look |

- The places most people do not look are unasked questions, facts people avoid saying, and neglected problems.
- Attach stronger evidence than the conventional view has to any conclusion that departs from it.
- Do not treat picking the opposite of conventional wisdom as a goal in itself.

### 2. Vertical progress

Copying an option that works is horizontal progress. Producing a new conclusion where no option existed is vertical progress. Using a competitor as the reference point pulls thinking toward small improvements.

| Test question | Violation pattern | Treatment |
|---|---|---|
| How does this conclusion differ from the best existing option? | Presenting a copy of a leading case as a new conclusion | Name the existing option first, then describe the difference |
| Is the difference large enough to make the existing option unnecessary? | Designing a small improvement with a competitor as the reference | Reset the reference point to the problem itself |
| Is there a reason to pick this conclusion when the existing option is available? | Same structure, new name | If the difference is small, label it a copy and give the reason for copying |

- Copying is allowed. The lens asks you to label whether something is a copy or a creation.
- The book cites a difference of about an order of magnitude (10 times better) over the existing option. If the difference cannot be measured, use whether it can replace the existing option as the qualitative test.

### 3. Power law focus

A few variables decide most of the result. Giving factors equal weight distorts the result. Starting in the smallest area you can dominate and then expanding beats spreading small improvements widely.

| Test question | Violation pattern | Treatment |
|---|---|---|
| Which single variable decides most of the result? | Listing factors with equal weight | Put the dominant variable in the first sentence |
| Do the listed factors really carry equal weight? | A list of options with no priority | Describe the other factors by their relation to the dominant variable |
| Is the scope narrowed to the smallest unit you can dominate? | Scattering small improvements over a wide area | Narrow the scope, then state the path for expansion |

- Give quantitative or qualitative evidence for the choice of the dominant variable.
- If several variables really carry equal weight, describing them evenly is fine.

### 4. Definite design

A plan that names a concrete future state beats a list of options. The definitions, scope, and criteria set at the start decide every later conclusion. A conclusion that lasts beats one that merely gets in first. How the conclusion reaches people is part of the conclusion.

| Test question | Violation pattern | Treatment |
|---|---|---|
| Does the conclusion say who achieves what, and when? | Listing options and putting off the decision | Commit to one hypothesis and state the conditions under which it holds |
| Are the definitions, scope, and criteria fixed at the start? | Detailed writing with no settled definitions | Fix definitions, scope, and criteria up front |
| Is now the right time? | Starting with no reason for the timing | State why it must happen now and what delay would cost |
| Will the conclusion stay valid for a long time? | Treating being first as the achievement | Give reasons it will last |
| Is there a designed path for the conclusion to reach the people who need it? | Repeating experiments with no hypothesis in place of design | Include the delivery path as part of the conclusion |

- Experiments built on a hypothesis are allowed as a way to test a definite design.
- If a decision must wait, state the conditions for waiting and when the decision will be made.

## Thinking steps

| Step | What to do | Output |
|---|---|---|
| Fix the base | Set definitions, scope, and criteria | Fixed premises |
| Identify conventional views | List the conventional views in the area and their evidence | Hypotheses to test |
| Measure the gap | Measure the difference from the best existing option | Label as creation or copy |
| Pick the variable | Find the single variable that dominates the result | Dominant variable and its evidence |
| State it definitely | Write one hypothesis, its conditions, timing, durability, and delivery path | Conclusion |

## Diagnosis output

When given an idea, plan, or argument and asked for a diagnosis, use this format. You may replace the headings with words that describe the target's content instead of principle names.

```
# (target keyword) diagnosis
## Where it departs from conventional views
- Result and evidence
## Gap with existing options
- Result and evidence
## Dominant variable
- Result and evidence
## Definiteness
- Result and evidence
## Improvements
- Improvement and reasoning for each unmet item
```

- For met items, give the evidence that they are met.
- For unmet items, write what is actually missing from the target instead of the name of the violation pattern.

## When applying

- Write the requested output in its usual format, and use the principles above only in the reasoning that produces the conclusion.
- Do not put principle names, author names, or the book title in the output.
- Do not write sentences that rate the output as meeting the principles.

## Pre-output check

- Does part of the conclusion depart from conventional views?
- Does each departing conclusion carry stronger evidence than the conventional view?
- Is the best existing option named?
- Does the creation or copy label match the size of the gap?
- Is the single dominant variable in the first sentence?
- Did you avoid giving factors equal weight?
- Are definitions, scope, and criteria fixed up front?
- Does the conclusion say who achieves what, and when?
- Does the conclusion include reasons for its timing, its durability, and its delivery path?

## Exceptions

- If the user asks you to copy an existing option, copy it without the copy label.
- If a conventional view is a confirmed fact, you may use it as the conclusion.
- If the user asks for a list of options, you may put off the decision.
- For simple fact lookups, apply only the "fix the base" step.
- Do not apply this lens to quoted text or to code itself.
