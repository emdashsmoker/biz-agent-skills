---
name: lean-work
description: A lean work skill that first fixes the purpose, reader, and scope, then keeps only the elements a work process or an expression needs. It applies necessity, reader relevance, feasibility, and proportionality checks to every element, then sorts the elements out in the order of eliminate, combine, rearrange, and simplify (ECRS). The result is a minimum-step work process or texts, slides, charts, and so on with one message per unit. It supports both writing new output and revising existing output. Use this skill when the user asks for "/lean-work", "keep it lean", "be practical", "be realistic", "minimum steps", "no unnecessary steps", "cut the pointless steps", "a simple process", "make it doable", "improve this with ECRS", "focus this", "find the focus", "one message per slide", "one message per paragraph", "boil it down to one message", "don't just list everything", "no laundry lists", or "start from first principles". Do not apply it automatically to general tasks without such a request.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Lean Work

> This English version is a translation of the Korean original. It may behave differently from the intent of the original.

This skill defines a way of working that selects only the elements that serve the reader's purpose and explains them in enough depth. Fix the purpose, reader, and scope before selecting elements. Whether an element is needed can be judged only once these three are set.

It applies to work processes and to expression. A work process is built from the minimum steps needed to reach the goal. Expression is built so that each unit delivers one message. A unit is a subheading or paragraph of a text, the headline or a component of a slide, a data item, and so on. Both judge elements with the same checks, then sort them out in the order of eliminate, combine, rearrange, and simplify.

## Definitions

Use the terms below only in the sense given in this table.

| Term | Definition |
|------|------------|
| Purpose | The judgment or action the reader will make or carry out after receiving the output |
| Reader | The person who reads or acts on the output. If the user does not specify one, a general adult reader without background in the field |
| Scope | The boundary of what the output covers |
| Element | The smallest thing that is judged and sorted out. In a work process the element is a work step. In expression the elements are the expression elements that make up a unit, such as a sentence, bullet, figure, shape, and so on |
| Unit | A block of expression the reader sees and understands at once. A subheading or paragraph of a text, the headline or a component of a slide, a data item of a chart or table, and so on. A smaller unit inside a larger unit is treated as an element of the larger unit |
| Message | The one judgment the reader should remember after seeing a unit. A sentence with a subject and a predicate |
| Topic label | A title that names a subject without making a judgment. "Market overview", "Background", "Key issues", and so on |
| Department-store listing | Expression that lays out related information at equal weight without a message |
| Message overload | A state in which one unit holds two or more independent claims |
| ECRS | The order of improvement used in work study. The initials of Eliminate, Combine, Rearrange, and Simplify |

## Workflow

1. (Fix the criteria) Set the purpose, reader, and scope, and verify the premises
2. (Choose a mode) Select the mode that fits the type of output
3. (Sort out the elements) Following the procedure of the chosen mode, judge every element and sort it out in ECRS order
4. (Pre-delivery check) Go through the checklist, then deliver

## Fixing the Criteria

When the criteria change, the elements to keep and the elements to delete change with them. Settle the items below before selecting elements. Use what you settle only for judgment, and do not write it in the output.

- Settle first why the work is needed, what output you will make, and how you will make it.
- Write the purpose, reader, and scope in one sentence each. Use an item the user has already set as it is.
- Use each definition and criterion in the same sense through the end of the output. Call the same thing by one name.
- Treat both the premises in the user's request and the model's own knowledge as things to verify. Common sense, authority, well-known frameworks, buzzwords, and marketing terms do not count as evidence on their own.
- When given a problem, trace its causes back to the deepest cause the user can act on. Derive the improvement from that cause.
- Explain the conclusion so that a third party with no background knowledge can follow the evidence and accept it. Use expressions with a clear meaning in the explanation.
- Match the depth of verification to the impact the item under check has on the conclusion. Do not verify in depth the details that cannot change the conclusion.

## Choosing a Mode

| Mode | Output | Procedure to follow |
|------|--------|---------------------|
| Work design | Work processes for problem solving, planning, analysis, research, coding, and similar tasks | Work design procedure |
| Expression | Answers, documents, slides, charts, diagrams | Expression procedure |

- Both modes split into writing new output and revising existing output. Revision follows the revision procedure.
- If one request calls for both a work process and expression, first set the work order with the work design procedure. Then apply the expression procedure to the output of that work.
- If the user or another instruction specifies an output structure (a table template, rating scale, fixed workflow, and so on), keep that structure. In that case, apply element judgment and ECRS to each item and step inside the structure.

## Element Judgment

Keep an element only when it meets the checks below. Each check applies to different elements.

| Check | Question | Applies to |
|-------|----------|------------|
| Necessity | If this element is deleted, does the message come across less well or does the quality of the output fall? | All elements |
| Reader relevance | Is this information the reader does not yet know, and does the reader have a reason to know it? | Expression elements |
| Feasibility | Can the user carry it out with the resources and constraints they have? | Work steps |
| Proportionality | Is the effort put in smaller than the value gained? | Work steps |

- Use the constraints the user has stated as the basis for judging feasibility. If the constraints are unclear, confirm them with the user before proceeding.
- Keep steps in highly sensitive areas, such as law, regulation, and safety, regardless of the judgment result. Skipping such a step causes a loss larger than the effort saved.

## Applying ECRS

Apply the questions below to each judged element in the order of the table. When the answer is "no", move on to the next question without action.

| Order | Question | Action when the answer is "yes" |
|-------|----------|---------------------------------|
| 1. Eliminate | Is the purpose still met without this element? | Delete the element |
| 2. Combine | Can it be handled in one go together with another element? | Merge the elements into one |
| 3. Rearrange | Does changing the order or position reduce rework or the reader's search? | Change the order or position of the element |
| 4. Simplify | Can a simpler means or form produce the same result? | Change the means or form of the element |

- Apply eliminate first. Effort spent merging or refining an element that will be eliminated leaves nothing in the result.
- Cover the elements that remain after ECRS in enough depth. ECRS reduces the number of elements so that the reader's attention gathers on those that remain.
- The detailed criteria for work steps are in the work design procedure, and those for expression elements are in the expression procedure.

## Work Design Procedure

The work design mode presents only the minimum steps needed to reach the goal. A model tends to propose processes with added steps that ignore the user's time, cost, and resources.

1. Confirm the final output, the input materials the user has, and the constraints
2. List the steps that lead to the final output, and set the input and output of each step
3. Judge every step and apply ECRS by the criteria in the table below
4. Write the remaining steps in the output format

### ECRS Criteria for Work Steps

| Order | Criteria applied to work steps |
|-------|--------------------------------|
| Eliminate | Delete steps that do not meet the necessity check. Also delete steps that redo a problem definition or direction the user has already set |
| Combine | Merge steps that run at the same time or finish within one task into one step. Also merge steps that handle the same input material in the same way into one step |
| Rearrange | Place a step that uses the output of an earlier step as its input after that step. Place a step early when its result changes the scope or method of later steps. Gather steps with the same purpose in one module |
| Simplify | First select a method that uses the materials, templates, and tools the user already has. Match the scope and precision of the work to the level the purpose requires |

- Review elimination from the steps that directly produce the output. When a step that directly produces the output is deleted, also delete the steps that prepare or check it.
- If a step that decides the scope or method of later steps comes late, output that was already made has to be made again.
- For a step that meets necessity but does not meet feasibility or proportionality, reduce the effort by combining and simplifying, then judge it again. Delete a step that still does not meet the checks after the second judgment.
- Apply the same judgment and ECRS to the plan for work the model carries out itself.

### Criteria for Writing a Process

- Write only the actions to perform in a process. Delete sentences that explain the significance, background, or expected benefits of the process. Sentences such as "We propose the following process", "In this step, data is collected", and "This will improve efficiency" are to be deleted.
- Decide the number of modules within the range that meets the checks.
- When the user asks for a process without specifying a format, output in the format below. Write only the action performed in the content column.

```
## Module N. Module name
- (Purpose) One-line statement

| Task | Input | Content | Output |
|------|-------|---------|--------|
| N-1. Task name | Input material or list | Action performed | Output name or list |
| N-2. Task name | Input material or list | Action performed | Output name or list |
```

## Expression Procedure

In the expression mode, every unit delivers exactly one message. A department-store listing hands the burden of choosing what to look at to the reader. Message overload makes it hard for the reader to grasp what the unit is trying to deliver. Both problems arise when all the information on hand is laid out without selecting the elements to deliver.

1. Break the output into a list of units
2. Set the message of each unit as one judgment sentence
3. Judge the elements in each unit and apply ECRS by the criteria in the table below
4. Check for the signs of department-store listing, then deliver

### Setting the Message

- For each unit, answer "What is the one sentence a reader should remember after seeing this unit?"
- If there is no answer, the unit has no message. Set a judgment sentence or delete the unit.
- If the answer strings together two or more independent claims, the unit has message overload. Split the unit by adding a slide, splitting the paragraph, dividing the chart, and so on.
- A topic label carries no judgment, so it does not count as a message. A message is a judgment sentence with a subject and a predicate, such as "Low-priced imports cut profitability in the domestic market".

### ECRS Criteria for Expression Elements

| Order | Criteria applied to expression elements |
|-------|-----------------------------------------|
| Eliminate | Delete elements that do not support the message and elements the reader already knows. Leave elements that another unit or an appendix will use for rearranging |
| Combine | If five or more components remain after elimination, merge the sub-items into three or four higher categories. Move the details to a lower level |
| Rearrange | Put the message at the head of the unit. Split an element that has value as an independent message into a separate unit. Move an element that only has reference value to an appendix, footnote, or attachment |
| Simplify | Set one point of emphasis per unit. Lower the visual weight of the other elements |

### Selecting Components

By default, each unit has three to four or fewer components that support the message. People can remember and handle only a limited number of pieces of information at once. As items increase, the attention each item gets decreases.

Review deletion candidates in the order below. The effort spent writing an element is not a reason to keep it.

1. Information unrelated to the message
2. Background the reader already knows
3. Evidence that repeats support for the same conclusion
4. Decorative figures and examples that do not contribute to the judgment

- Sort out an element that does not support the message in one of three ways: delete it, split it into a separate unit, or move it to an appendix. Do not name something in the body and leave out its content.
- If five or more components remain after elimination, first check whether two or more messages are mixed. If they are mixed, split the unit. If there is one message, merge the components into higher categories.
- Selected components cover different parts of the message without overlap.
- Keep only as many components as the message requires. Finish content that two components cover with two.
- Place elements of different kinds, such as causes and effects, symptoms and remedies, or facts and opinions, in separate groups by kind.
- Keep the built-in count of frameworks with a fixed number of parts, such as a four-quadrant matrix or a five-stage process.

Compress by reducing the number of elements. If you keep every element and only shorten the sentences, only the density of the writing rises. The number of items the reader must read stays the same.

### Message Placement

Put the message at the head of the unit.

- On a slide, the headline carries the message.
- On a chart, the title carries the message.
- In a paragraph, the first sentence carries the message. The remaining sentences support only the first sentence.
- With a sentence-style header, the header carries the message and the first sentence of the body opens with evidence.
- With a keyword-style header, the header announces the subject of the message and the first sentence of the body carries the judgment.
- If the subject the header announces differs from the message in the first sentence, rename the header or move the content.
- For other units, such as a component of a slide, a data item, and so on, put the message where the reader reads first.

### Emphasis Placement

- Arrange the elements in a unit with decreasing weight in the order of message, supporting elements, and details.
- Set one point of emphasis per unit.
- In slides and designs, draw the eye to the point of emphasis with size, position, and color. Show the other elements at smaller size and lower saturation.
- In charts, highlight only one series and show comparison series at lower saturation. Attach data labels only to points related to the message.
- Reduce colors, lines, and decoration that do not help deliver the message.
- If every element carries the same weight, treat the unit as having no point of emphasis and rearrange it.

### Signs of Department-Store Listing

If one or more of the signs below appear, rebuild the unit.

- Five or more parallel items sit at the same level
- One paragraph holds two or more sentences with independent claims
- The title or headline is a topic label
- Every item has the same visual weight and length, leaving no point of emphasis
- Elements of different kinds, such as causes and effects, symptoms and remedies, or facts and opinions, are mixed in one list
- The subject the header announces differs from the message in the first sentence of the body
- You cannot answer "the one sentence to remember from this unit"

## Revision Procedure

Apply this when revising existing output. Add a short diagnosis to the revised result so that the user can check the reasons for the changes. State in the diagnosis what changed and why, in terms of the content of the output.

### Revising a Work Process

1. Identify the input and output of each step in the existing process
2. Judge every step and apply ECRS
3. Deliver the revised process with a short note on the steps that changed and the reasons

### Revising Expression

1. Extract the messages of each unit and diagnose how many each unit has
2. Split units with two or more messages, and for units with no message set a judgment sentence or delete the unit
3. Judge the elements in each unit and apply ECRS
4. Deliver the revised result with a short diagnosis for each unit

## Common Output Rules

Put only the finished result in the output. The process that produced the result is not needed for the reader's judgment.

- Keep everything that comes from the internal work of this skill out of the output. The table below gives typical cases. The same rule applies to internal work content that the table does not list.
- Do not use in the output the name of this skill, the fact that it was applied, or any term this skill defines or uses (ECRS, element judgment, department-store listing, message overload, and so on). A term the user used first in the request may be used.
- Do not use meta-commentary in the output. Meta-commentary is wording that describes the text itself, the writing process, or the writer's judgment and way of working. Sentences such as "To sum up the key points", "Unnecessary steps were left out", "This was boiled down to one message", "This is kept concise", and so on fall under it. Such wording does not serve the reader's purpose, so it runs against this skill's way of working, which keeps only the elements that are needed.

| Internal work | Cases of content kept out of the output |
|---------------|-----------------------------------------|
| Fixing the criteria | The sentences that set the purpose, reader, and scope, the process of verifying premises, and so on |
| Element judgment | The result of each check, the answers to the check questions, and so on |
| Applying ECRS | The list of elements that were deleted, merged, moved, or simplified and the reasons, and so on |
| Pre-delivery check | The checklist items, their results, and so on |

- Do not mention in the output the elements deleted from the body. Listing deleted elements adds back items the reader must read.
- The diagnosis from the revision procedure is the exception, because the user uses it to check the reasons for the changes. Add a diagnosis only when existing output was revised.
- If the user asks for the judgment process or the deleted elements, provide only the scope requested.
- Follow the user or other instructions for writing style and sentence endings, word choice, the length of individual sentences, overall structure and table of contents, and markdown format. This skill governs the selection and order of work steps, the selection of expression elements, and the placement of the message and emphasis.

## Examples

The organizations, products, and situations in the examples below are all fictional. The tables of what was applied list only the orders that applied. The diagnosis sentences and the tables of what was applied are material that explains how the rules apply. Put only the result after revision in the output.

### Work Design Example

The user asks for the steps to make an executive report from last month's raw employee survey data in Excel. The user also has an executive report template used every quarter.

The process before revision is below.

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

| Order | What was applied |
|-------|------------------|
| Eliminate | The user had already set the purpose of the report, so the redefinition step was deleted. Benchmarking, framework design, and interviews were deleted because the quality of the survey report holds without them |
| Combine | Descriptive statistics and cross-tabulations finish in one tabulation task, so they were merged |
| Rearrange | Checking the report template moved to the first step. The template decides the tabulation items, so checking it late means tabulating again |
| Simplify | The step that designs a new report structure was switched to using the existing report template and merged into the material writing step. Deriving implications for every question took too much effort relative to the purpose of the report, so its scope was narrowed to message selection. Message selection picks only three to four results that need an executive decision |

The process after revision is below.

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

### Slide Example

In the slide before revision, the title is a topic label. Its seven parallel items mix independent messages about falling profitability, regulatory change, and industry structure. There is no point of emphasis either.

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

After revision, the slide is split by message. Below is the first of the split slides.

```
(Headline) Low-priced imports and crowded competition cut profitability in the domestic market
- Many players compete in a flat market, which intensifies pressure to cut prices
- Rising inflow of low-priced imports lowers the average selling price
- With the market flat, higher sales volume cannot offset the fall in profitability
```

| Order | What was applied |
|-------|------------------|
| Eliminate | Consumer awareness, distribution structure, and slow technology adoption do not support falling profitability, so they were deleted |
| Rearrange | The judgment sentence moved up to the headline. The regulatory sandbox program moved to the next slide, which covers opportunity factors |

### Paragraph Example

The paragraph before revision holds three independent messages: a cause diagnosis, a competitive trend, and a response plan. The first sentence does not represent the whole paragraph.

```
The launch of the new product is delayed because the parts supply is unstable.
The supplier also lacks production capacity. Meanwhile, a competitor launched a
similar product first and is taking the market, and its marketing budget is
larger than ours. Therefore, we should move up the launch date, raise the
marketing budget, and diversify suppliers.
```

After revision, the paragraph is split by message. Each paragraph opens with its message. The remaining sentences support only the first sentence.

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

### Chart Example

In the chart before revision, the title is a topic label. Twelve bars carry the same weight, so the reader cannot tell where to look.

```
(Title) Results by division
- Twelve bars for all divisions shown in the same color
- Data labels attached to every bar
```

The chart after revision is below.

```
(Title) The materials division accounts for more than half of the company's revenue growth
- Only the materials division bar shown in the emphasis color, with a data label
- The two divisions with the next largest revenue growth shown at lower saturation
- The other nine divisions summed into one "Other" bar
```

| Order | What was applied |
|-------|------------------|
| Combine | The nine divisions with small revenue growth were merged into "Other", which cut the bars from twelve to four |
| Rearrange | The judgment sentence moved up to the chart title |
| Simplify | One series was set as the emphasis, and data labels remain only on the bar related to the message |

## Exceptions

- If the user asks for "a detailed process" or "all the steps", do not apply element judgment and ECRS to that process.
- If the user asks for a complete list or a detailed inventory, do not apply the count standard to that part.
- For output that must be a complete list, such as laws, regulations, and checklists, do not apply the count standard. Apply only the emphasis placement rules to such output.
- Keep the built-in count of frameworks and standard templates with a fixed number of parts.
- Exclude quotations, verbatim reproductions of source text, and code bodies.

## Pre-Delivery Checklist

### Common Checks

- Are the purpose, reader, and scope set, and are definitions and criteria used in the same sense through the end of the output?
- Did you accept the user's premises and the model's knowledge only after checking the evidence?
- Is the improvement for a problem derived from the deepest cause the user can act on?
- Does every element meet the checks that apply to it?
- Did you apply eliminate, combine, rearrange, and simplify to every element in this order?
- Does the output hold only the finished result?
- Is the output free of internal work content, the name and terms of this skill, and meta-commentary?

### Work Design Checks

- Did you follow the problem definition and direction the user set as they are?
- Are steps that finish within one task merged into one step?
- Are the steps that decide the scope or method of later steps placed early?
- Did you first select methods that use the materials, templates, and tools the user already has?
- Are the legal, regulatory, and safety steps kept?
- Does the process contain only the actions to perform?

### Expression Checks

- Does every unit deliver exactly one message in the form of a judgment sentence?
- Is the message at the head of the unit, and do the header and the first sentence point to the same subject?
- Does each unit have three to four components or fewer (excluding built-in framework counts and exceptions)?
- Did you compress by reducing the number of elements?
- Did you sort out each element that does not support the message by deletion, splitting, or moving?
- Did you place elements of different kinds in separate groups by kind?
- Does each unit have one point of emphasis?
