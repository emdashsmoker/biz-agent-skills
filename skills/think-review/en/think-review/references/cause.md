# Cause lens

> This English version was translated from the Korean original. It may behave differently from what the original intends.

Ask "why" repeatedly to trace a problem to its root cause, and pair that root cause with a direction for the fix.

## Background

This lens builds on the "5 whys" technique from the Toyota Production System. The technique has been criticized for forcing a single line of causes and for assuming the deepest cause is the best place to intervene (Card, 2017, BMJ Quality & Safety). To offset those limits, this lens records cause branches and picks the intervention point by its effect.

## Core principles

- Separate symptoms from causes. A symptom is what you see as soon as the problem occurs. A fix that removes only the symptom is temporary.
- A root cause is the point where removing the cause structurally stops the problem from recurring.
- Each "why" answer becomes the subject of the next "why". Move one step at a time from surface symptoms to structural causes.
- "Five" is a rule of thumb. Three rounds are sometimes enough, and seven or more are sometimes needed. Do not add or cut steps to hit five.
- Stop tracing when either condition below holds. Removing this cause keeps the problem from coming back. Or asking further yields no meaningful answer, or the answer moves into an area the target cannot control.
- If the causes split into branches, record every branch. Trace the most likely branch to the end first. Ask the user whether to trace the remaining branches.
- Do not choose the intervention point by depth. Choose the point that cuts recurrence the most and that the target can change in practice.

## Diagnosis steps

### 1. Check the input

The input is one of these kinds: the user describes the problem directly, the user gives only a plan, or the user gives a plan and names the problem to analyze. If the lens is called with no input, ask for the problem or the plan.

### 2. Define the problem

Set the problem that serves as the starting point. A vague problem sends the whole analysis off course.

- If the user described the problem, use that description as the problem definition.
- If you received only a plan, pull the core problem from its background or its description of current issues.
- If the user named a separate problem, use that problem first.

A problem definition meets three requirements.

- Describe a concrete, observable phenomenon.
- Do not build a cause or a solution into it.
- Focus on one problem. Split a compound problem and analyze each part.

Show the chosen problem to the user and say that you will trace causes from it, so the user has a chance to correct it.

### 3. Ask about answer depth

Ask the user how detailed the countermeasures should be.

- A: one or two key lines per fix direction
- B: a table per fix direction comparing the current state with the changed state

### 4. Trace the cause chain

- At each step, confirm that the answer causes the question just before it.
- Do not ask who made the mistake. Ask which process or structure allowed the problem.
- If a person's mistake comes up as an answer, ask once more what condition allowed that mistake.
- Write each answer as a fact confirmed by the input material. Do not fill in causes the material does not contain.
- When the chain is complete, read it backward from the root cause to the problem as "A, so B happens". If the logic breaks at a step, rewrite that step.

### 5. Output

Write in this order.

The analysis overview summarizes the problem in two or three sentences. If a plan came with it, include the plan's core as well.

Write the cause chain as a table. Put the fix direction only in the root cause row.

| Step | Question | Answer | Fix direction |
|---|---|---|---|
| Problem | - | (problem definition) | - |
| Why 1 | Why (problem definition)? | (answer) | - |
| Why 2 | Why (answer to why 1)? | (answer) | - |
| ... | ... | ... | - |
| Root cause | Why (previous answer)? | (root cause) | (fix direction) |

If there were several cause branches, list the untraced branches below the table, one line each.

The root cause diagnosis covers why you consider this the root cause, and how far its effects reach along with what happens if it is left alone.

Write the countermeasures at the depth chosen in step 3 (A or B).

## When applying

If the user asks for something like "write this with root causes in mind" or "list issues using the 5 whys", write only the requested output.

- Do not use the cause chain table, step labels such as "Why 1", or diagnosis sections.
- Avoid statements at the symptom level, and define each issue at the root cause level.
- Avoid wording that pins responsibility on individuals, and describe the problem in terms of processes and structures.

## Example

Problem: Replies to customer inquiries often miss the promised deadline.

| Step | Answer |
|---|---|
| Why 1 | The inquiry handler waits a long time for the technical team to confirm details |
| Why 2 | The technical team receives confirmation requests with no priority |
| Why 3 | Requests travel through personal messengers, so there is no request list |
| Root cause | There is no process for logging cross-team confirmation requests with deadlines |

The fix direction is a process that logs cross-team confirmation requests in one place and attaches a response deadline to each. Stopping at "the handler confirmed late" changes the person and leaves the problem to repeat.

## Exceptions

- If the user did not ask for analysis, diagnosis, or cause finding, do not produce a cause chain table or diagnosis sections on your own.
- Search the web only when the user asks for it.
