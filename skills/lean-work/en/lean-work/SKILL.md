---
name: lean-work
description: A lean work skill that first fixes the purpose, reader, and scope, then keeps only the elements a work process or expression needs. It applies necessity, reader relevance, feasibility, and proportionality checks to every element. It tidies a work process in the order eliminate, combine, rearrange, simplify, leaving minimum steps that connect inputs and outputs without gaps. It builds answers, documents, slides, charts, and diagrams with one message per unit and three to four supporting elements or fewer, in concise sentences. It supports both writing new output and revising existing output. Use this skill when the user asks for "/lean-work", "keep it lean", "be practical", "be realistic", "minimum steps", "no unnecessary steps", "be concise", "just the key points", "short version", "no fluff", "TL;DR", "focus this", "one message per slide", "boil it down to one message", "don't just list everything", or "start from first principles". Do not apply it automatically to general tasks without such a request.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Lean Work

> This English version is a translation of the Korean original. It may behave differently from the intent of the original.

This skill defines a way of working that filters out elements that do not serve the reader's purpose and explains the remaining elements in enough depth. Fix the purpose, reader, and scope before filtering anything. You can only judge what is needed once these criteria are set.

It applies to work processes and to expression (answers, documents, slides, charts, diagrams).

## Definitions

Use the terms below only in the sense given in this table.

| Term | Definition |
|------|------------|
| Purpose | The judgment or action the reader will make or carry out after receiving the output |
| Reader | The person who reads or acts on the output. If the user does not specify one, a non-specialist adult with the general knowledge of a first-year university student |
| Scope | The boundary of what the output covers |
| Final deliverable | The result handed to the reader when the whole work process is finished |
| Element | The smallest thing being judged. A work step, sentence, bullet, table row, chart series, slide component, and so on |
| Unit | A block of expression the reader sees and takes in at once. One slide, one chart or diagram, one paragraph, one table |
| Message | The one judgment the reader should remember after seeing a unit. A sentence with a subject and a predicate |
| Topic label | A title that names a subject without making a judgment. For example "Market overview", "Background", "Key issues" |
| Department-store listing | Expression that lays out related information at equal weight without a message |

## Workflow

1. (Fix the criteria) Set the purpose, reader, and scope, and verify the premises
2. (Choose a mode) Pick the mode that fits the type of output
3. (Judge elements) Apply the checks to every element and handle the elements that fail
4. (Apply mode rules) Build the output with the rules of the chosen mode
5. (Pre-delivery check) Go through the checklist, then deliver

## Fixing the Criteria

If the criteria shift, the choice of what to keep and what to delete shifts with them. Settle the items below before filtering elements.

- Answer first why the output is needed, what you will make, and how you will make it.
- Write the purpose, reader, and scope in one sentence each. Do not redefine an item the user has already set.
- Use each definition and criterion in the same sense through the end of the output. Do not call the same thing by several names.
- Treat both the premises in the user's request and the model's own knowledge as things to verify. Common sense, authority, well-known frameworks, buzzwords, and marketing terms do not count as evidence on their own.
- When given a problem, trace its causes back to the deepest cause the user can act on. Derive the improvement from that cause.
- A third party with no background knowledge must be able to follow the evidence and accept the conclusion. Do not substitute wordplay or empty expressions for explanation.
- Match the depth of verification to the impact the judgment has on the conclusion. Do not dig deep into details that cannot change the conclusion.

## Choosing a Mode

| Mode | Output | Rules applied |
|------|--------|---------------|
| Work design | Work processes for problem solving, planning, analysis, research, coding, and similar tasks | Fixing the criteria, element judgment, work design rules, sentence rules |
| Expression | Answers, documents, slides, charts, diagrams | Fixing the criteria, element judgment, unit rules, sentence rules |

- The expression mode splits into writing new output and revising existing output. Revision follows the revision procedure.
- If the user or another instruction specifies an output structure (a table template, rating scale, fixed workflow, and so on), keep that structure. In that case, apply element judgment and the sentence rules to each item and step inside the structure.

## Element Judgment

Every element must pass the checks below before delivery to stay. Each check applies to different elements.

| Check | Question | Applies to |
|-------|----------|------------|
| Necessity | If this element is deleted, does the message or the quality of the output change? | All elements |
| Reader relevance | Is this information the reader does not yet know, and does the reader have a reason to know it? | Sentences and expression components |
| Feasibility | Can the user carry it out with the resources and constraints they have? | Work steps |
| Proportionality | Is the effort put in smaller than the value gained? | Work steps |

Judge reader relevance against the reader set when fixing the criteria. An explanation a novice reader needs only adds reading load for a reader who already knows its content.

Handle any element that fails even one of the checks that apply to it as follows.

- The default is deletion. Do not keep something in the body because writing it took effort.
- If it has value as an independent message, split it into a separate unit.
- If it only has reference value, move it to an appendix, footnote, or attachment.
- Merge a work step into an adjacent step or delete it.
- Do not use the halfway option of naming something in the body and leaving out its content.

If the constraints needed to judge feasibility are unclear, confirm them with the user before proceeding. If the user has stated constraints, use them as the basis for judging feasibility. Keep steps with high sensitivity, such as law, regulation, and safety, regardless of the judgment result.

## Work Design Rules

The work design mode presents only the minimum steps needed to reach the goal.

### Order of Tidying Steps

Tidy both a newly drafted process and an existing process given by the user or another instruction in the order below. Elimination comes first because any effort spent refining a step that will be deleted is wasted. Ordering comes after combining because fewer steps are then left to arrange.

1. (Eliminate) Delete the steps that fail the checks. If the user has defined the problem, do not add a step that redefines it. If the user has given a direction, do not add a step that explores directions.
2. (Combine) Write steps that run at the same time, or that finish naturally within one task, as a single step.
3. (Rearrange) Order the steps so that each step's input is secured before that step. Put checks that affect every later step, such as checking input material for gaps and format, near the start.
4. (Simplify) If several methods give the same result, use the method that finishes with the tools and material the user already has as the default.

### Input and Output Links

The Input and Output columns of the work process table show the links between steps. Apply the conditions below so that a third party can reach the same judgment from the table alone.

- The Output of every Task is used as the Input of a later Task or as the final deliverable. Delete any Task whose Output is used nowhere.
- The Input of every Task is material the user provided or the Output of an earlier Task. For an Input with no source, add a Task that secures it before the step or confirm it with the user.
- The final deliverable comes out as the Output of one Task.

### Output Format

- Write only the procedure, without adding its significance, background, or expected benefits. Do not write sentences such as "We propose the following process", "In this step, data is collected", or "This will improve efficiency".
- Decide the number of modules within the range that passes the checks.
- Unless another format is specified, output in the format below. Write only the action performed in the content column.

```
## Module N. Module name
- (Purpose) One-line statement

| Task | Input | Content | Output |
|------|-------|---------|--------|
| N-1. Task name | Input material or list | Action performed | Output name or list |
| N-2. Task name | Input material or list | Action performed | Output name or list |
```

## Unit Rules

In the expression mode, every unit delivers exactly one message. A department-store listing hands the burden of choosing what to look at to the reader. When one unit packs in several independent claims, the reader cannot tell what that unit says.

### Setting the Message

- Break the output into a list of units.
- For each unit, answer "What is the one sentence a reader should remember after seeing this unit?"
- If there is no answer, the unit has no message. Write a judgment sentence or delete the unit.
- If the answer strings together two or more independent claims, split the unit. Add a slide, split the paragraph, or divide the chart.
- A topic label carries no judgment, so it does not count as a message. An example of a message is "Low-priced imports cut profitability in the domestic market", a judgment sentence with a subject and a predicate.

### Message Placement

Put the message at the head of the unit.

- On a slide, the headline sentence carries the message.
- On a chart, the title carries the message.
- In a paragraph, the first sentence carries the message. The remaining sentences support only the first sentence.
- With a sentence-style header, the header carries the message and the first sentence of the body opens with evidence.
- With a keyword-style header, the header announces the subject of the message and the first sentence of the body carries the judgment.
- If the subject the header announces differs from the message in the first sentence, rename the header or move the content.
- In output with two or more units, reading only the units' messages in order must still convey the overall conclusion, because each message summarizes the content of its unit.

### Selecting Components

The default is three to four components or fewer per unit to support the message. Adults can hold about four information chunks at once, so when items go beyond that, the attention each item gets decreases.

- Selected components do not overlap, and each covers a different part of the message.
- Do not stretch content that two components cover into three or four to fill a count.
- Keep the built-in count of frameworks with a fixed number of parts, such as a four-quadrant matrix or a five-stage process.
- If five or more seem necessary, handle them in the order below.

1. Check whether messages are mixed, and split the unit if there are two or more messages
2. Group sub-items into three or four higher categories and move the details to a lower level
3. Delete items that do not support the message

Compress by selecting elements. If you keep every element and only shorten the sentences, the density of the writing rises while the number of items the reader must process stays the same. Explain the elements that remain after selection in enough depth. Review deletion candidates in the order below.

1. Information unrelated to the message
2. Background the reader already knows
3. Evidence that repeats support for the same conclusion
4. Decorative figures and examples that do not contribute to the judgment

### Emphasis Placement

Emphasis draws the eye through contrast with the surrounding elements. As points of emphasis multiply, the contrast shrinks until no point stands out.

- Arrange the elements in a unit with different weight in the order of message, supporting elements, and details.
- Set one point of emphasis per unit.
- In slides and designs, guide the eye with size, position, and color, and give the other elements smaller size and lower saturation.
- In charts, highlight only one series and show comparison series at lower saturation. Attach data labels only to points related to the message.
- If every element carries the same weight, treat the unit as having no point of emphasis and rearrange it.

### Signs of Department-Store Listing

If one or more of the signs below appear, rebuild the unit.

- Five or more parallel items sit at the same level
- One paragraph holds two or more sentences with independent claims
- The title or headline stays at a topic label
- Every item has the same visual weight and length, leaving no point of emphasis
- Elements of different kinds, such as causes and effects, symptoms and remedies, or facts and opinions, are mixed in one list
- The subject the header announces differs from the message in the first sentence of the body
- You cannot answer "the one sentence to remember from this unit"

## Sentence Rules

Sentences in every mode must pass the necessity and reader relevance checks. Judge length by information density, and make every sentence deliver new information.

- Start the answer from the first sentence. Do not write openers such as "Great question", previews such as "First I will explain A, then B", or closing courtesies such as "I hope this helps".
- Do not write repeated summaries of what you already said, related knowledge outside the question's scope, or alternatives and extra options the user did not ask for.
- If the answer has several items, select three to four or fewer. List everything only when the user asks for a complete list.
- Replace expressions the reader could not understand on one reading with plain ones. If a technical term cannot be avoided, add a short definition in parentheses once, at its first appearance. Apply the same test to engineering and software-design phrasing (input value, output, mapping, interface, and so on). Plain wording must not underestimate the reader's level or obscure the meaning with catch-all words. State specialized and technical content accurately and clearly, without distorting its meaning.
- Keep grammar correct regardless of how technical or plain the text is.
- When referring to another document, page, section, data, and so on, write the needed content in the sentence itself so the reader does not have to consult it. Do not replace content with codes, numbers, abbreviations, or summary labels, and so on.
- State uncertainty once. Do not repeat hedges in every sentence.
- Instead of contrast constructions of the form "not A, but B", state B directly.
- When the content is the same, state it in the positive form. Write "conversion is possible once structured data is secured" in place of "data readiness is insufficient". A positive sentence states the target state directly, so it is clear and easy to revise and combine sentence by sentence. A negative sentence describes problems case by case, so it is complex and the reader has to infer the target state.
- Put only one independent claim in each sentence and each bullet. When a sentence grows long, first check whether two or more independent claims are mixed in it, and split it if they are. In a sentence with one claim, keep only the modifiers and conditions that claim needs.

## Revision Procedure

Apply this when revising existing output in the expression mode.

1. Extract every message by unit and diagnose the number of messages in each unit
2. Split units with two or more messages and reduce components to within the standard
3. Read only the messages in order, and where the flow breaks, add the missing message or change the order of units
4. Apply element judgment and the sentence rules to the remaining sentences
5. Deliver the revised result with a short diagnosis for each unit

## Common Output Rules

- Do not reveal in the output that this skill was applied, the names of its rules, or the checking process. The diagnosis from the revision procedure is the exception.
- Follow the user or other instructions for writing style and sentence endings, overall structure and table of contents, and markdown format. This skill governs element selection, message placement, and the information density of sentences.

## Examples

The organizations, products, and situations in the examples below are all fictional.

### Work Design

(Request) A request to lay out the steps for making an executive report from last month's raw employee survey data in Excel

(before)

```
1. Redefine the purpose of the report
2. Benchmark domestic and international survey analysis cases
3. Design an analysis framework
4. Clean the data
5. Compute descriptive statistics
6. Run cross-tabulations
7. Interview stakeholders
8. Derive implications
9. Draft the report
```

(Handling) The user had already set the purpose of the report, so the redefinition step was deleted. Benchmarking, framework design, and interviews took too much effort relative to the purpose of reporting survey results, so they failed the proportionality check. Descriptive statistics and cross-tabulations finish in one tabulation task, so they were merged. Deriving implications was merged into the message selection step. The remaining Tasks were arranged so that each Output feeds the Input of the next Task and the last Output becomes the report material.

(after)

```
## Module 1. Survey Tabulation
- (Purpose) Identify the survey results that need an executive decision

| Task | Input | Content | Output |
|------|-------|---------|--------|
| 1-1. Data cleaning | Raw survey data in Excel | Remove non-responses and duplicate responses | Cleaned data |
| 1-2. Tabulation | Cleaned data | Tabulate response distribution by question and differences by department | Tabulation sheet |

## Module 2. Report Writing
- (Purpose) Write material executives can read once and decide on

| Task | Input | Content | Output |
|------|-------|---------|--------|
| 2-1. Message selection | Tabulation sheet | Select three to four results that need an executive decision | Message list |
| 2-2. Material writing | Message list | Write one slide per message | Report material |
```

### Expression (Slide)

(before)

```
(Title) Market overview
- Domestic market size flat
- Many major players competing
- Rising inflow of low-priced imports
- Regulatory sandbox program allows new services
- Consumer awareness needs to improve
- Complex distribution structure
- Slow adoption of new technology
```

(Diagnosis) The title is a topic label. There are seven parallel items. Independent messages about falling profitability, regulatory change, and industry structure are mixed, and there is no point of emphasis.

(after, the first slide after splitting)

```
(Headline) Low-priced imports and crowded competition cut profitability in the domestic market
- Many players compete in a flat market, which intensifies pressure to cut prices
- Rising inflow of low-priced imports lowers the average selling price
- With the market flat, higher sales volume cannot offset the fall in profitability
```

(Handling) Only the three elements that support falling profitability remain. The regulatory sandbox program moved to the next slide, which covers opportunity factors. Consumer awareness, distribution structure, and slow technology adoption do not contribute to this message, so they were deleted or moved to an attachment.

### Expression (Paragraph)

(before)

```
The launch of the new product is delayed because the parts supply is unstable.
The supplier also lacks production capacity. Meanwhile, a competitor launched a
similar product first and is taking the market, and its marketing budget is
larger than ours. Therefore, we should move up the launch date, raise the
marketing budget, and diversify suppliers.
```

(Diagnosis) Three independent messages, a cause diagnosis, a competitive trend, and a response plan, sit in one paragraph. The first sentence does not represent the whole paragraph.

(after)

```
The launch of the new product is delayed because the parts supply is unstable.
We source the main part from a single supplier. That supplier's production
capacity falls short of our order volume.

While the launch slips, the competitive position is getting worse. A competitor
launched a similar product first and captured early demand. It also runs a
larger marketing budget than ours.

The first step in our response is to diversify suppliers. The parts supply must
stabilize before a shorter launch schedule and a larger marketing budget can
take effect.
```

### Expression (Chart)

(before)

```
(Title) Results by division
- Show the revenue bars of all 12 divisions in the same color
- Attach data labels to every bar
```

(Diagnosis) The title is a topic label. All 12 divisions are laid out at equal weight, so the reader has no point to look at.

(after)

```
(Title) The materials division generated more than half of company-wide revenue growth
- Show only the materials division bar in the accent color and attach its data label
- Show the top two divisions other than materials at lower saturation and combine the rest into "Other"
```

(Handling) The title was turned into a judgment sentence that carries the message. The highlighted series was set to the materials division alone, the subject of the message. Only the divisions needed for comparison remain, and the rest were combined into "Other", which cut the displayed items to four.

### Expression (Concise Answer)

(Question) What to check first when adopting an automatic meeting-notes tool

(before)

```
Great question! Adopting a meeting-notes tool is an important decision with many
aspects to consider. First I will look at security, then cost and features in turn.
You should check security, cost, speech recognition accuracy, integration with
existing collaboration tools, ease of use, vendor stability, and training support.
I hope this helps!
```

(after)

```
- Check where meeting audio and records are stored and who can access them. If the tool fails your internal security rules, the other conditions do not need checking.
- Test speech recognition accuracy with real meeting recordings. If people spend long hours fixing errors, the benefit of adoption disappears.
- Check whether it integrates with the collaboration tools you already use. Without integration, moving the records becomes a new task.
```

## Exceptions

- If the user asks for "more detail", "be specific", "a detailed process", or "all the steps", do not apply the concision and count standards to that part.
- If the user asks for a complete list or a detailed inventory, do not apply the count standard to that part.
- For output whose purpose is a complete list, such as laws, regulations, and checklists, do not apply the count standard and apply only the emphasis placement rules.
- Keep the built-in count of frameworks and standard templates with a fixed number of parts.
- Exclude quotations, verbatim reproductions of source text, and code bodies. Apply the rules to the explanatory sentences before and after code.

## Pre-Delivery Checklist

- Are the purpose, reader, and scope set, and are definitions and criteria used in the same sense through the end of the output?
- Did you avoid accepting the user's premises and the model's knowledge without evidence?
- Is the improvement for a problem derived from the deepest cause the user can act on?
- Did every element pass the checks that apply to it?
- Did you handle each failed element by deletion, splitting, moving, or merging?
- Is the work process free of steps that reset a problem or direction the user already set?
- Did you avoid splitting work that one action finishes into several steps?
- Did you tidy the process in the order eliminate, combine, rearrange, simplify?
- Is the Output of every Task used as the Input of a later Task or as the final deliverable, and does the table show a source for every Input?
- Does every unit deliver exactly one message in the form of a judgment sentence?
- Does reading only the units' messages convey the overall conclusion?
- Does each unit have three to four components or fewer (excluding built-in framework counts and exceptions)?
- Did you compress by selecting elements?
- Does each unit have one point of emphasis?
- Does the first sentence start with the answer, and does the last sentence avoid courtesies and unrequested offers?
- Does each sentence and each bullet hold one independent claim?
- Is the output free of any sign that this skill was applied or of its rule names?
