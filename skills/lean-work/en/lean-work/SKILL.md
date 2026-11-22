---
name: lean-work
description: A lean work skill that keeps only the elements that serve the purpose in work processes and in expression. For a work process, it applies necessity, feasibility, and proportionality checks to every step and reduces the process to the minimum steps the user can carry out. For answers, documents, slides, charts, and tables, it sets one message per unit and selects three to four components or fewer to support that message. It compresses by selecting the elements to deliver. It supports both writing new output and revising existing output. Use this skill when the user asks for "/lean-work", "keep it lean", "be practical", "be realistic", "minimum steps", "no unnecessary steps", "no overblown process", "make it doable", "be concise", "just the key points", "short version", "no fluff", "TL;DR", "focus this", "one message per slide", "boil it down to one message", or "don't just list everything". Do not apply it automatically to general tasks without such a request.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Lean Work

> This English version is a translation of the Korean original. It may behave differently from the intent of the original.

This skill defines a way of working that keeps only the elements that serve the purpose and then carries out or explains the remaining elements in enough depth. It applies to work processes and to expression.

Language model output often presents every step the model can think of and every piece of information it holds, without selection. In work processes, this produces an excessive process that goes beyond the user's time, budget, and staff. In expression, it produces a department-store listing in which the reader has to pick what to read. This skill handles both problems with the same method, element selection.

## Definitions

Use the terms below only in the sense given in this table.

| Term | Definition |
|------|------------|
| Purpose | The judgment the reader will make or the action the reader will take after receiving the final output |
| Reader | The person who reads or acts on the final output. If the user does not specify one, a non-specialist adult with the general knowledge of a first-year university student |
| Scope | The boundary of what the final output covers |
| Final output | The result the reader receives when the work is finished. For a work process, the result that comes out after every step is carried out |
| Element | The smallest thing being judged. A step in a work process. A sentence, bullet, table row, chart series, or slide component in expression |
| Step | A piece of work that takes inputs and produces one output |
| Excessive process | A work process that still contains steps that fail the checks |
| Unit | A block of expression the reader sees and takes in at once. One slide, one chart or diagram, one paragraph, one table |
| Message | The one judgment sentence the reader should remember after seeing a unit |
| Judgment sentence | A sentence that has a subject and a predicate and that the reader can agree or disagree with |
| Topic label | A title that names a subject without making a judgment. For example "Market overview", "Background", "Key issues" |
| Department-store listing | Expression that lays out related information at equal weight without a message |
| Message overload | A state in which one unit holds two or more independent claims |

## Workflow

1. (Fix the criteria) Set the purpose, reader, and scope
2. (Choose a mode) Pick the mode that fits the type of output
3. (Judge elements) Apply the checks to every element
4. (Apply mode rules) Handle the elements that fail and build the output with the rules of the chosen mode
5. (Pre-delivery check) Go through the checklist, then deliver

## Fixing the Criteria

Element judgment decides whether an element is needed in light of the purpose. The same element gets the same result only when the purpose, reader, and scope are set.

- Write the purpose, reader, and scope in one sentence each. Use an item the user has already set as it is.
- Infer the items you can read from the request and the material provided. Confirm with the user any item whose inference would change the output.
- For a work process, also list the constraints the user has stated (deadline, budget, staff, material on hand, tools, authority).
- Use each criterion and term in the same sense through the end of the output.

## Choosing a Mode

| Mode | Output | Rules applied |
|------|--------|---------------|
| Work process | A process proposed to the user for problem solving, planning, analysis, research, coding, and similar tasks, and a plan the model makes for work it will carry out itself | Work process rules |
| Expression | Answers, documents, slides, charts, diagrams, tables | Expression rules |

- Both modes support writing new output and revising existing output. Revision follows the revision procedure.
- For a request that asks for the work and a resulting document, apply the work process rules to the plan and the expression rules to the document.
- Apply sentence selection from the expression rules to the sentences of an answer that proposes a work process.
- If the user or another instruction specifies an output structure (a table template, rating scale, fixed workflow, and so on), keep that structure. In that case, apply element judgment to each step and item inside the structure.

## Element Judgment

An element stays only when it passes every check that applies to it. Each pass criterion is a fact that can be confirmed, so that a third party reaches the same result.

| Check | Applies to | Question | Pass criterion |
|-------|------------|----------|----------------|
| Necessity | Work steps | If this step is removed, does the final output change? | You can point to the later step or the place in the final output where the output of this step is used |
| Feasibility | Work steps | Can the user carry it out with the resources and constraints they have? | The time, budget, staff, material, tools, and authority the step needs are all within what the user has stated |
| Proportionality | Work steps | Does the effort match the value gained? | The effort of the step matches the use of its output. Assign large effort to a step that produces evidence able to change the conclusion of the final output, and small effort to a step that produces secondary evidence |
| Message contribution | Expression elements | If this element is deleted, does the message get weaker? | The element carries one of the reasons, evidence, examples, or details of the message and does not overlap with another element |
| Reader relevance | Expression elements | Is this information the reader does not yet know and has a reason to know? | The information is new to the reader and the reader uses it for a judgment or an action |

- Judge a work step in the order of necessity, feasibility, and proportionality. A step that fails necessity needs no further checks.
- If the feasibility result depends on a constraint and that constraint is unclear, confirm it with the user before proceeding.
- If the user has stated constraints, use them as the pass criterion for feasibility.

## Work Process Rules

Build a work process from the minimum steps needed to reach the goal.

### Handling Steps

Handle a step that fails in the order below. Considering deletion first saves the effort of refining a step that will be deleted.

1. (Delete) Delete a step that fails necessity
2. (Merge) When the work of a step is needed but the step runs at the same time as another step or finishes within one task, merge it into that step and write them as one
3. (Reduce) When a step passes necessity but fails feasibility or proportionality, replace it with a method that produces an output of the same use with fewer resources

| Step that fails | Reduced step |
|-----------------|--------------|
| Interviews with all stakeholders | Confirm only the items with divided interpretations with one person in charge |
| Full survey of the population | Sample survey |
| Collecting new material | Using the material the user already has |

For a step that has no way to be reduced, tell the user what resources it needs and confirm whether to proceed.

### Writing Steps

- Accept the problem, purpose, and direction the user has set as they are. Start the process from the work that follows them.
- Write each step as an action to perform. Leave out sentences that explain the significance, background, or expected benefits of the process. Sentences to leave out include "We propose the following process", "In this step, data is collected", and "This will improve efficiency".
- Keep steps that involve law, regulation, or safety regardless of the judgment result. Leaving out such a step leads to penalties or accidents even when the step does not contribute directly to the final output.
- Apply the same checks to the plan for work the model carries out itself. Carry out the requested scope, and carry out extra work that was not requested (extra files, extra analysis, extra features) only when it passes necessity.
- Match the number of modules and steps to the steps that pass the checks. If few steps pass, write one module.

### Signs to Recheck a Process

If one or more of the signs below appear, apply element judgment to that step again.

- A step whose output is used neither as input to a later step nor in the final output
- A step whose output cannot be named concretely
- A step that resets a problem, purpose, or direction the user already set
- Work that one task finishes is split into several steps
- A step that assumes resources the user has not stated (extra staff, extra budget, cooperation from outside organizations, paid material)
- Extra research steps (benchmarking, interviews, surveys, workshops) are included although the final output can be made from the request and the material provided
- A step that produces secondary evidence takes the largest effort in the process

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

## Expression Rules

Every unit delivers one message. A department-store listing hands the burden of choosing what to read to the reader. Message overload leaves the reader unable to tell what the unit is trying to say. Both problems arise when all the information on hand is laid out without selection.

### Setting the Message

- Break the output into a list of units.
- For each unit, answer "What is the one sentence a reader should remember after seeing this unit?"
- Confirm the answer with the two tests below.

| Test | Question | Result |
|------|----------|--------|
| Judgment sentence test | Can the reader agree or disagree with this sentence? | If so, it is a judgment sentence. If it only names a subject, so that agreeing or disagreeing does not apply, it is a topic label |
| Independent claim test | Is one of the two claims a reason, evidence, example, or detail of the other? | If so, they are one message and its support. If neither supports the other, they are two independent claims |

- If there is no answer, or the answer is a topic label, the unit has no message. Write a judgment sentence or delete the unit.
- If there are two or more independent claims, the unit has message overload. Split the unit by adding a slide, splitting the paragraph, or dividing the chart.
- "Market overview" is a topic label, and "Low-priced imports cut profitability in the domestic market" is a judgment sentence.
- "The inflow of low-priced imports lowers the average selling price" is evidence for "Profitability in the domestic market is falling", so the two sentences form one message. "Profitability in the domestic market is falling" and "The regulatory sandbox program allows new services" do not support each other, so they are two independent claims.

### Message Placement

Put the message at the head of the unit. The reader interprets the remaining elements in light of the message read at the head.

| Unit | Where the message goes |
|------|------------------------|
| Slide | The headline sentence |
| Chart, diagram | The title |
| Table | The table title or the sentence right above the table |
| Paragraph | The first sentence. The remaining sentences support the first sentence |

- With a sentence-style header, the header carries the message and the first sentence of the body opens with evidence.
- With a keyword-style header, the header announces the subject of the message and the first sentence of the body carries the judgment sentence.
- If the subject the header announces differs from the message in the first sentence, rename the header or move the content.

### Selecting Components

The default is three to four components or fewer per unit to support the message. People can hold only a limited number of items in memory at once, so as items increase, the attention each item gets decreases.

- Selected components do not overlap, and each covers a different part of the message.
- Write content that two components cover with two components.
- Keep the built-in count of frameworks with a fixed number of parts, such as a four-quadrant matrix or a five-stage process.
- If five or more seem necessary, handle them in the order below.

1. Check with the independent claim test whether messages are mixed, and split the unit if there are two or more messages
2. Group sub-items into three or four higher categories and move the details to a lower level
3. Delete items that fail the message contribution check

Compress by selecting elements. If you keep every element and only shorten the sentences, the density of the writing rises while the number of items the reader must process stays the same. Explain the elements that remain after selection in enough depth. Review deletion candidates in the order below.

1. Information unrelated to the message
2. Background the reader already knows
3. Evidence that repeats support for the same conclusion
4. Decorative figures and examples the reader does not use for a judgment

Handle an element that fails as follows.

- The default is deletion. The effort spent writing an element is no reason to keep it.
- If it has value as an independent message, split it into a separate unit.
- If it only has reference value, move it to an appendix, footnote, or attachment.
- Keep in the body only elements whose content is fully explained. Handle an element that is named but not explained by deleting, splitting, or moving it.

### Emphasis Placement

Set one point of emphasis per unit. Several points of emphasis divide the reader's attention and weaken the message.

- Arrange the elements in a unit with different weight in the order of message, supporting elements, and details.
- In slides and designs, guide the eye with size, position, and color, and give the other elements smaller size and lower saturation.
- In charts, highlight only one series and show comparison series at lower saturation. Attach data labels to the points related to the message.
- In tables, set apart the one row or column related to the message with bold type or color.
- If every element carries the same weight, treat the unit as having no point of emphasis and rearrange it.

### Sentence Selection

A sentence also stays only when it passes message contribution and reader relevance. Every sentence delivers new information to the reader.

- Start the first sentence with the answer or the message, and end the last sentence with content. Openers such as "Great question", previews such as "First I will explain A, then B", and closing courtesies such as "I hope this helps" are to be deleted.
- Repeated summaries of what was already said, related knowledge outside the question's scope, and alternatives and extra options the user did not ask for are to be deleted.
- If the answer has several items, select three to four or fewer. List everything when the user asks for a complete list.
- State uncertainty once, in the sentence where the content first appears.
- Put one message in each bullet. If a bullet runs past about 100 characters in Korean or about 15 words in English, apply the independent claim test again. If it holds one message, leave the length as it is.

### Signs to Recheck Expression

If one or more of the signs below appear, rebuild the unit.

- Five or more items sit side by side at the same level
- One paragraph holds two or more sentences with independent claims
- The title or headline stays at a topic label
- Every item has the same visual weight and length, leaving no point of emphasis
- Elements of different kinds, such as causes and effects, symptoms and remedies, or facts and opinions, are mixed in one list
- The subject the header announces differs from the message in the first sentence of the body
- You cannot answer "the one sentence to remember from this unit"

## Revision Procedure

Apply this when revising existing output.

1. Confirm the purpose, reader, and scope of the existing output
2. (Work process) Apply the checks to each step and handle the steps that fail in the order of delete, merge, and reduce
3. (Expression) Extract every message by unit and find the units with no message and the units with message overload. Split the units with message overload and select components to within the standard
4. Apply sentence selection to the remaining sentences
5. Deliver the revised result with a short diagnosis for each step or unit handled

## Common Output Rules

- Put in the output only the content to deliver to the reader. Mention that this skill was applied, the names of its rules, and the checking process only in the diagnosis from the revision procedure.
- Follow the user or other instructions for writing style and sentence endings, word choice, overall structure and table of contents, and markdown format. This skill governs the selection of steps and elements, message placement, and emphasis placement.

## Examples

The organizations, products, and situations in the examples below are all fictional.

### Work Process

(Request) A request for the steps to make an executive report from last month's raw employee survey data in Excel. The deadline is this week and one person is in charge

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

(Handling) The user had already set the purpose of the report, so the redefinition step was deleted. The outputs of benchmarking and framework design are not used in the tabulation or the report, so they failed necessity and were deleted. Descriptive statistics and cross-tabulations finish in one tabulation task, so they were merged. Stakeholder interviews are used to confirm the interpretation of results, but one person cannot carry them out within this week, so the step was reduced to a check with the person in charge of the survey. Deriving implications was merged into the message selection step.

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
| 2-1. Message selection | Tabulation sheet | Select three to four results that need an executive decision, and confirm results with divided interpretations with the person in charge of the survey | Message list |
| 2-2. Material writing | Message list | Write one slide per message | Report material |
```

### Slide

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

(Diagnosis) The title is a topic label. There are seven items at the same level. Independent claims about falling profitability, regulatory change, and industry structure are mixed, and there is no point of emphasis.

(after, the first slide after splitting)

```
(Headline) Low-priced imports and crowded competition cut profitability in the domestic market
- Many players compete in a flat market, which intensifies pressure to cut prices
- Rising inflow of low-priced imports lowers the average selling price
- With the market flat, higher sales volume cannot offset the fall in profitability
```

(Handling) Only the three elements that support falling profitability remain. The regulatory sandbox program moved to the next slide, which covers opportunity factors. Consumer awareness, distribution structure, and slow technology adoption do not contribute to this message, so they were deleted or moved to an attachment.

### Paragraph

(before)

```
The launch of the new product is delayed because the parts supply is unstable.
The supplier also lacks production capacity. Meanwhile, a competitor launched a
similar product first and is taking the market, and its marketing budget is
larger than ours. Therefore, we should move up the launch date, raise the
marketing budget, and diversify suppliers.
```

(Diagnosis) Three independent claims, a cause, a competitive trend, and a response plan, sit in one paragraph. The first sentence does not represent the whole paragraph.

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

### Chart

(before)

```
(Title) Results by division
Twelve bars (all divisions) in the same color, with a data label on every bar
```

(Diagnosis) The title is a topic label. All twelve divisions are shown at equal weight, so the reader cannot tell where to look.

(after)

```
(Title) The materials division generates more than half of company-wide revenue growth
Only the materials division bar in the highlight color, with a data label
Of the other divisions, only the top two at lower saturation, and the rest combined into "Other"
```

(Handling) One judgment sentence was set as the title. Only one series was highlighted. The lower divisions were combined into "Other", which reduced the items shown to four.

### Concise Answer

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

- If the user asks for "more detail", "be specific", "a detailed process", or "all the steps", lift the minimum-step standard and the count standard for the requested scope.
- If the user asks for a complete list or a detailed inventory, lift the count standard for the requested scope.
- For output whose purpose is a complete list, such as laws, regulations, and checklists, lift the count standard and apply only the emphasis placement rules.
- Keep the built-in count of frameworks and standard templates with a fixed number of parts.
- Exclude quotations, verbatim reproductions of source text, and code bodies. Apply the rules to the explanatory sentences before and after code.

## Pre-Delivery Checklist

- (Common) Are the purpose, reader, and scope set, and are criteria and terms used in the same sense through the end of the output?
- (Common) Is the output free of any sign that this skill was applied or of its rule names?
- (Work process) Is the output of every step used as input to a later step or in the final output?
- (Work process) Can every step be carried out within the constraints the user stated?
- (Work process) Did you handle the steps that failed in the order of delete, merge, and reduce?
- (Work process) Are the problem, purpose, and direction the user set used as they are?
- (Work process) Do the steps that involve law, regulation, or safety remain?
- (Work process) Is the process free of steps that match the signs to recheck a process?
- (Expression) Does the message of every unit pass the judgment sentence test, with one message per unit?
- (Expression) Is the message at the head of the unit?
- (Expression) Does each unit have three to four components or fewer (excluding built-in framework counts and exceptions)?
- (Expression) Did you compress by selecting elements and explain the remaining elements in enough depth?
- (Expression) Did you handle each failed element by deleting, splitting, or moving it?
- (Expression) Does each unit have one point of emphasis?
- (Expression) Does the first sentence start with the answer or the message, and does the last sentence end with content?
- (Expression) Is the output free of units that match the signs to recheck expression?
