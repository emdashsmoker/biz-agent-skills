# Plan lens

> This English version was translated from the Korean original. It may behave differently from what the original intends.

Check whether a plan answers every question it must answer. The questions follow the Heilmeier Catechism used by the US Defense Advanced Research Projects Agency (DARPA).

## Background

George H. Heilmeier, DARPA director from 1975 to 1977, wrote these questions to judge research and development projects. DARPA's published list of questions follows (https://www.darpa.mil/about/heilmeier-catechism). They were written for research projects, and this lens applies them to every kind of plan, including infrastructure, industrial development, HR strategy, public policy, and organizational strategy.

## The questions

Each question lists what to check.

### Question 1. What are you trying to do? Articulate your objectives using absolutely no jargon

- Does the plan explain what it aims to achieve in words a layperson understands?
- Does it say why this matters?

### Question 2. How is it done today, and what are the limits of current practice?

- Does it describe the current level and limits of the technology, market, and policy?
- Does it reflect domestic and international trends?
- Does it know the state of the art and consider the available options broadly?
- Is there a strategic need and urgency to support it now?

### Question 3. What is new in your approach and why do you think it will be successful?

- Does it state how the new approach differs from the existing one?
- Does it give evidence for why it will succeed?

### Question 4. Who cares? If you are successful, what difference will it make?

- Who needs this plan?
- Does it describe the difference and ripple effects if it succeeds?
- Compared with question 1, does it state the current and changed states in measurable form (for example, cutting processing time from its current level to a target level)?

### Question 5. What are the risks?

- Does it list where it could fail (technology, demand, execution, regulation, schedule)?
- Does it list side effects of success (operating burden, extra cost, effects on surrounding systems)?
- Does each risk have a response or mitigation?

### Question 6. How much will it cost?

- Does the budget fit the goal and scope?
- Does it reflect the type of project (top-down or bottom-up), who carries it out, and its stage (such as technology readiness level)?

### Question 7. How long will it take?

- Does the duration fit the goal and the stage?

### Question 8. What are the mid-term and final "exams" to check for success?

- Are the targets and measures for the midpoint and final checks defined?
- Are the measures measurable and tied to the goal?

## Using it outside R&D

Swap the research terms for terms from the plan's field. At the start of a diagnosis, state which terms you swapped and how.

| Original term | Infrastructure | HR strategy | Industrial development |
|---|---|---|---|
| What this R&D aims to achieve | What this infrastructure aims to achieve | What this HR strategy aims to achieve | What this strategy aims to achieve |
| Current state of technology | Current state of the infrastructure | Current HR practices | Current state of the industry ecosystem |
| Awareness of the state of the art | Awareness of similar infrastructure elsewhere | Awareness of HR practices elsewhere | Awareness of industrial policies elsewhere |
| Difference from existing methods | Difference from current facility operation | Difference from current HR policies | Difference from past development policies |
| Who performs the research | Client, contractor, operator | HR team, business units, outside experts | Central ministries, local governments, public agencies, private firms |
| Research stage | Concept, feasibility study, design, construction | Diagnosis, policy design, pilot, full rollout | Agenda setting, policy design, pilot program, main program |
| Mid-term and final exams | Progress inspections and completion inspection | Pilot evaluation and post-rollout measurement | Pilot evaluation and post-program policy evaluation |

Handle fields not in the table (education, defense, environment, culture, and so on) the same way.

## Diagnosis steps

### 1. Check the plan

Receive the plan as text or a file. If the lens is called without a plan, ask for one.

### 2. Ask about depth

Before summarizing or analyzing the plan, ask how deep the improvement suggestions should go.

- A: key improvement points per question only (current state and improvement direction)
- B: A plus the reasoning for each improvement
- C: B plus rewritten sample sentences

### 3. Identify the field

For an R&D project, use the questions as they are. For other fields, swap terms as in the table above.

### 4. Grade

| Grade | Criterion |
|---|---|
| High | The answer to the question is logically complete, with enough concrete evidence and data |
| Medium | An answer exists but lacks detail or has a logical leap |
| Low | No answer, or a serious logical flaw |

- Mark anything the plan does not state as "not stated in the plan". That verdict is useful feedback in itself.
- Do not fill blanks with unsupported inferences or assumptions.
- Do not grade leniently.
- Quote the plan's text as the basis for each grade.

### 5. Output

Write in this order.

1. Overview: summarize the plan's core in two or three sentences. If you swapped terms, state it here.
2. Grade summary table: question, grade, and a one-line basis
3. Detail per question: for each question, a table of current state and improvement direction, plus reasoning and rewritten sentences according to the chosen depth
4. Overall assessment: look at the logical links between questions instead of listing per-question results. For example, check whether the ripple effect in question 4 is measured by the exams in question 8, and whether the risks in question 5 show up in the cost and time of questions 6 and 7. Write the current state and the direction for improvement at the chosen depth.

Make every improvement specific enough to act on right away.

## When applying

If the user asks for something like "write a plan using Heilmeier", follow the format of the requested output.

- Do not use question numbers, grade tables, or current-state and improvement tables.
- Work these elements into the output naturally: a goal in plain words, the current state and its limits, a difference backed by evidence, the people who need it and a measurable effect, risks and responses, whether resources and schedule fit, and midpoint and final measures.

## Exceptions

- If the user did not ask for a review, evaluation, diagnosis, or improvement, do not produce grades or improvement tables on your own.
- Write the result in the conversation. Create a file only when the user asks.
- Search the web only when the user asks for it.
