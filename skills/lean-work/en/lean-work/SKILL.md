---
name: lean-work
description: A lean work skill that first fixes the purpose, reader, and scope, then keeps only the elements a work process or an expression needs. It applies necessity, reader relevance, feasibility, and proportionality checks to every element and handles the elements in the order of eliminate, combine, rearrange, and simplify (ECRS) to produce minimum-step work processes and slides, charts, and paragraphs with one message per unit. It supports both writing new output and revising existing output. Use this skill when the user asks for "/lean-work", "keep it lean", "be practical", "be realistic", "minimum steps", "no unnecessary steps", "cut the pointless steps", "a simple process", "make it doable", "improve this with ECRS", "focus this", "find the focus", "one message per slide", "one message per paragraph", "boil it down to one message", "don't just list everything", "no laundry lists", or "start from first principles". Do not apply it automatically to general tasks without such a request.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Lean Work

> This English version is a translation of the Korean original. It may behave differently from the intent of the original.

This skill defines a way of working that filters out elements that do not serve the reader's purpose and explains the remaining elements in enough depth. Fix the purpose, reader, and scope before filtering anything. You can only judge what is needed once these criteria are set.

It applies to work processes and to expression. A work process is built from the minimum steps needed to reach the goal. Expression is built so that each unit, such as a slide, a chart, or a paragraph, delivers one message. Both use the same checks to judge elements and handle them in the order of eliminate, combine, rearrange, and simplify.

## Definitions

Use the terms below only in the sense given in this table.

| Term | Definition |
|------|------------|
| Purpose | The judgment or action the reader will make or carry out after receiving the output |
| Reader | The person who reads or acts on the output. If the user does not specify one, a general adult reader without background in the field |
| Scope | The boundary of what the output covers |
| Element | The smallest thing that is judged and handled. In a work process the element is a work step. In expression the elements are expression elements such as a sentence, bullet, table row, chart series, or slide component |
| Unit | A block of expression the reader sees and takes in at once. One slide, one chart or diagram, one paragraph, one table |
| Message | The one judgment the reader should remember after seeing a unit. A sentence with a subject and a predicate |
| Topic label | A title that names a subject without making a judgment. For example "Market overview", "Background", "Key issues" |
| Department-store listing | Expression that lays out related information at equal weight without a message |
| Message overload | A state in which one unit holds two or more independent claims |
| ECRS | The order of improvement used in work study. The initials of Eliminate, Combine, Rearrange, and Simplify |

## Workflow

1. (Fix the criteria) Set the purpose, reader, and scope, and verify the premises
2. (Choose a mode) Pick the mode that fits the type of output
3. (Judge and handle) Within the procedure of the chosen mode, judge every element and handle it in ECRS order
4. (Pre-delivery check) Go through the checklist, then deliver

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

| Mode | Output | Procedure to follow |
|------|--------|---------------------|
| Work design | Work processes for problem solving, planning, analysis, research, coding, and similar tasks | Work design procedure |
| Expression | Answers, documents, slides, charts, diagrams | Expression procedure |

- Both modes split into writing new output and revising existing output. Revision follows the revision procedure.
- If one request calls for both a work process and expression, set the process with the work design procedure, then apply the expression procedure to the output of that process.
- If the user or another instruction specifies an output structure (a table template, rating scale, fixed workflow, and so on), keep that structure. In that case, apply element judgment and ECRS handling to each item and step inside the structure.

## Element Judgment

Every element must pass the checks below to stay as it is. Each check applies to different elements.

| Check | Question | Applies to |
|-------|----------|------------|
| Necessity | If this element is deleted, does the message come across less well or does the quality of the output fall? | All elements |
| Reader relevance | Is this information the reader does not yet know, and does the reader have a reason to know it? | Expression elements |
| Feasibility | Can the user carry it out with the resources and constraints they have? | Work steps |
| Proportionality | Is the effort put in smaller than the value gained? | Work steps |

- If the constraints needed to judge feasibility (deadline, budget, people, materials and tools on hand) are unclear, confirm them with the user before proceeding. Use the constraints the user has stated as the basis for judging feasibility.
- Keep steps with high sensitivity, such as law, regulation, and safety, regardless of the judgment result. The loss from skipping such a step is larger than the effort saved.

## ECRS Handling

Put each judged element through the four questions below in the order of the table. Pass over a question that does not apply without handling.

| Order | Question | Handling of work steps | Handling of expression elements |
|-------|----------|------------------------|---------------------------------|
| 1. Eliminate | Is the purpose still met without this element? | Delete steps that fail the necessity check | Delete elements that do not support the message and elements the reader already knows. Pass elements that another unit or an appendix will use on to rearrange |
| 2. Combine | Can it be handled in one go together with another element? | Merge steps that run at the same time or finish within one task into one step | Group items of the same category under a higher category |
| 3. Rearrange | Does changing the order or position reduce rework or the reader's search? | Move a step that decides the content of later steps to the front | Move the message to the head of the unit, and move the elements passed on from eliminate to another unit or an appendix |
| 4. Simplify | Can a simpler means or form produce the same result? | Switch to a method that uses the materials, templates, and tools the user already has | Set one point of emphasis and lower the visual weight of the other elements |

- (Reason for the order) Effort spent merging or refining an element that will be eliminated leaves nothing in the result. Finish elimination first, then apply combine, rearrange, and simplify to the elements that remain.
- (Where elimination starts) Review elimination from the key steps that directly produce the output. When a key step is eliminated, the supporting steps that prepare or check it are eliminated with it.
- (Necessary steps with large effort) For a step that passes necessity but fails feasibility or proportionality, reduce the effort by combining and simplifying, then judge it again. Eliminate a step that still fails after the second judgment.
- (Confirm before eliminating) Before eliminating a step whose removal would make the goal hard to reach, confirm with the user.
- (Coverage of remaining elements) Cover the elements that remain after the four kinds of handling in enough depth. The four kinds of handling reduce the number of elements so that the reader's attention gathers on those that remain.

## Work Design Procedure

The work design mode presents only the minimum steps needed to reach the goal. A model tends to propose processes with added steps that ignore the user's time, cost, and resources, so apply element judgment and ECRS handling to every step.

1. Confirm the final output, the input materials the user has, and the constraints
2. List the steps that lead to the final output, and write the input and output of each step
3. Apply element judgment and ECRS handling to every step
4. Write the remaining steps in the output format

### Step Handling Criteria

- (Eliminate) Use the problem definition and direction the user has set as the starting point of the process. Eliminate steps that redefine the problem and steps that explore directions again.
- (Combine) Write steps that run at the same time, or that finish naturally within one task, as a single step. Also write steps that process the same input material in the same way as a single step.
- (Rearrange) Place a step that uses the output of an earlier step as its input after that step.
- (Rearrange) Place a step early when its result changes the scope or method of later steps. Placing such a step late means remaking output that was already made.
- (Rearrange) Gather steps with the same purpose in one module.
- (Simplify) First choose a method that uses the materials, templates, and tools the user already has. Choose a method that builds something new when the resources on hand cannot meet the purpose.
- (Simplify) Match the scope and precision of the work to the level the purpose requires.

### Writing Criteria

- Write only the actions to perform in a process. Sentences that explain the significance, background, or expected benefits of the process are to be eliminated. Sentences such as "We propose the following process", "In this step, data is collected", and "This will improve efficiency" fall under this.
- Decide the number of modules within the range that passes the checks.
- Apply the same judgment and handling to the plan for work the model carries out itself. Use the output format when the user has asked for a process.

### Output Format

Unless another format is specified, output in the format below. Write only the action performed in the content column.

```
## Module N. Module name
- (Purpose) One-line statement

| Task | Input | Content | Output |
|------|-------|---------|--------|
| N-1. Task name | Input material or list | Action performed | Output name or list |
| N-2. Task name | Input material or list | Action performed | Output name or list |
```

## Expression Procedure

In the expression mode, every unit delivers exactly one message. A department-store listing hands the burden of choosing what to look at to the reader. Message overload leaves the reader unable to tell what the unit says. Both problems arise when all the information on hand is laid out without selecting the elements to deliver.

1. Break the output into a list of units
2. Set the message of each unit as one judgment sentence
3. Apply element judgment and ECRS handling to the elements in each unit
4. Check for the signs of department-store listing, then deliver

### Setting the Message

- For each unit, answer "What is the one sentence a reader should remember after seeing this unit?"
- If there is no answer, the unit has no message. Write a judgment sentence or delete the unit.
- If the answer strings together two or more independent claims, the unit has message overload. Split the unit by adding a slide, splitting the paragraph, or dividing the chart.
- A topic label carries no judgment, so it does not count as a message. An example of a message is "Low-priced imports cut profitability in the domestic market", a judgment sentence with a subject and a predicate.

### Message Placement

The first thing to rearrange is the message. Put the message at the head of the unit.

- On a slide, the headline sentence carries the message.
- On a chart, the title carries the message.
- In a paragraph, the first sentence carries the message. The remaining sentences support only the first sentence.
- With a sentence-style header, the header carries the message and the first sentence of the body opens with evidence.
- With a keyword-style header, the header announces the subject of the message and the first sentence of the body carries the judgment.
- If the subject the header announces differs from the message in the first sentence, rename the header or move the content.

### Selecting Components

The default is three to four components or fewer per unit to support the message. People can hold only a limited number of information chunks at once, so as items increase, the attention each item gets decreases.

Finish the handling of an element that does not support the message of this unit in one of the three ways below. Naming something in the body and leaving out its content is none of the three, so do not use it.

| Handling | ECRS order | When it applies |
|----------|------------|-----------------|
| Delete | Eliminate | The default. The effort spent writing an element is not a reason to keep it |
| Split | Rearrange | Move an element that has value as an independent message into a separate unit |
| Move | Rearrange | Move an element that only has reference value to an appendix, footnote, or attachment |

Review deletion candidates in the order below.

1. Information unrelated to the message
2. Background the reader already knows
3. Evidence that repeats support for the same conclusion
4. Decorative figures and examples that do not contribute to the judgment

Arrange the remaining components by the criteria below.

- (Combine) If five or more items remain after elimination, first check whether two or more messages are mixed, and split the unit if they are. If there is one message, group the sub-items into three or four higher categories and move the details to a lower level.
- (Rearrange) Place elements of different kinds, such as causes and effects, symptoms and remedies, or facts and opinions, in separate groups by kind.
- Selected components do not overlap, and each covers a different part of the message.
- Keep only as many components as the message requires. Finish content that two components cover with two.
- Keep the built-in count of frameworks with a fixed number of parts, such as a four-quadrant matrix or a five-stage process.

Compress by reducing the number of elements. If you keep every element and only shorten the sentences, the density of the writing rises while the number of items the reader must process stays the same.

### Emphasis Placement

Simplifying expression elements means setting one point for the reader to look at first and reducing the visual load of the other elements.

- Arrange the elements in a unit with different weight in the order of message, supporting elements, and details.
- Set one point of emphasis per unit.
- In slides and designs, guide the eye with size, position, and color, and give the other elements smaller size and lower saturation.
- In charts, highlight only one series and show comparison series at lower saturation. Attach data labels only to points related to the message.
- Reduce colors, lines, and decoration that are not used to tell the message apart.
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

## Revision Procedure

Apply this when revising existing output. Add a short diagnosis to the revised result so that the user can check the reasons for the changes.

### Revising a Work Process

1. Identify the input and output of each step in the existing process
2. Apply element judgment and ECRS handling to every step
3. Deliver the revised process with a short note on the steps that were eliminated, combined, rearranged, or simplified and the reasons

### Revising Expression

1. Extract every message by unit and diagnose the number of messages in each unit
2. Split units with two or more messages, and for units with no message write a judgment sentence or delete the unit
3. Apply element judgment and ECRS handling to the elements in each unit
4. Deliver the revised result with a short diagnosis for each unit

## Common Output Rules

- Do not reveal in the output that this skill was applied, the names of its rules, or the checking process. The diagnosis from the revision procedure is the exception.
- Follow the user or other instructions for writing style and sentence endings, word choice, the length of individual sentences, overall structure and table of contents, and markdown format. This skill governs the selection and order of work steps, the selection of expression elements, and the placement of the message and emphasis.

## Examples

The organizations, products, and situations in the examples below are all fictional. The handling notes list only the kinds of handling that applied.

### Work Design

(Request) A request to lay out the steps for making an executive report from last month's raw employee survey data in Excel. There is an executive report template used every quarter

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
9. Design a new report structure
10. Check the executive report template
11. Draft the report
```

(Handling)

- (Eliminate) The user had already set the purpose of the report, so the redefinition step was deleted. Benchmarking, framework design, and interviews were deleted because the quality of the survey report holds without them.
- (Combine) Descriptive statistics and cross-tabulations finish in one tabulation task, so they were merged.
- (Rearrange) Checking the report template moved to the first step. The template decides the tabulation items, so placing it late means tabulating again.
- (Simplify) The step that designs a new report structure was switched to using the existing report template and merged into the material writing step. Deriving implications for every question took too much effort relative to the purpose of the report, so its scope was narrowed to message selection, which picks three to four results that need an executive decision.

(after)

```
## Module 1. Survey Tabulation
- (Purpose) Identify the survey results that need an executive decision

| Task | Input | Content | Output |
|------|-------|---------|--------|
| 1-1. Template check | Quarterly executive report template | Identify the tabulation items the template requires | List of tabulation items |
| 1-2. Data cleaning | Raw survey data in Excel | Remove non-responses and duplicate responses | Cleaned data |
| 1-3. Tabulation | Cleaned data, list of tabulation items | Tabulate response distribution by question and differences by department in Excel | Tabulation sheet |

## Module 2. Report Writing
- (Purpose) Write material executives can read once and decide on

| Task | Input | Content | Output |
|------|-------|---------|--------|
| 2-1. Message selection | Tabulation sheet | Select three to four results that need an executive decision | Message list |
| 2-2. Material writing | Message list, quarterly executive report template | Write one slide per message in the template | Report material |
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

(Handling)

- (Eliminate) Consumer awareness, distribution structure, and slow technology adoption do not support falling profitability, so they were deleted.
- (Rearrange) The judgment sentence moved up to the headline. The regulatory sandbox program moved to the next slide, which covers opportunity factors.

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

(Handling)

- (Rearrange) The paragraph was split by message, and each paragraph opens with its message. The remaining sentences support only the first sentence.

### Expression (Chart)

(before)

```
(Title) Results by division
- Twelve bars for all divisions shown in the same color
- Data labels attached to every bar
```

(Diagnosis) The title is a topic label. Twelve bars carry the same weight, so the reader cannot tell where to look.

(after)

```
(Title) The materials division accounts for more than half of the company's revenue growth
- Only the materials division bar shown in the emphasis color, with a data label
- The two divisions with the next largest revenue growth shown at lower saturation
- The other nine divisions summed into one "Other" bar
```

(Handling)

- (Combine) The nine divisions with small revenue growth were merged into "Other", which cut the bars from twelve to four.
- (Rearrange) The judgment sentence moved up to the chart title.
- (Simplify) One series was set as the emphasis, and data labels remain only on the bar related to the message.

## Exceptions

- If the user asks for "a detailed process" or "all the steps", do not apply element judgment and ECRS handling to that process.
- If the user asks for a complete list or a detailed inventory, do not apply the count standard to that part.
- For output whose purpose is a complete list, such as laws, regulations, and checklists, do not apply the count standard and apply only the emphasis placement rules.
- Keep the built-in count of frameworks and standard templates with a fixed number of parts.
- Exclude quotations, verbatim reproductions of source text, and code bodies.

## Pre-Delivery Checklist

- (Common) Are the purpose, reader, and scope set, and are definitions and criteria used in the same sense through the end of the output?
- (Common) Did you accept the user's premises and the model's knowledge only after checking the evidence?
- (Common) Is the improvement for a problem derived from the deepest cause the user can act on?
- (Common) Did every element pass the checks that apply to it?
- (Common) Did you put every element through eliminate, combine, rearrange, and simplify in this order?
- (Common) Is the output free of any sign that this skill was applied or of its rule names?
- (Work design) Is the problem definition and direction the user set used as the starting point of the process?
- (Work design) Is work that one task finishes written as one step?
- (Work design) Are the steps that decide the scope or method of later steps placed early?
- (Work design) Did you first choose methods that use the materials, templates, and tools the user already has?
- (Work design) Are the legal, regulatory, and safety steps kept?
- (Work design) Does the process contain only the actions to perform?
- (Expression) Does every unit deliver exactly one message in the form of a judgment sentence?
- (Expression) Is the message at the head of the unit, and do the header and the first sentence point to the same subject?
- (Expression) Does each unit have three to four components or fewer (excluding built-in framework counts and exceptions)?
- (Expression) Did you compress by reducing the number of elements?
- (Expression) Did you handle each element taken out of the body by deletion, splitting, or moving?
- (Expression) Are elements of different kinds kept out of the same list?
- (Expression) Does each unit have one point of emphasis?
