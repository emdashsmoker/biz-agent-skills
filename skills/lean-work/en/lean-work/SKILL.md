---
name: lean-work
description: "A lean work skill that fixes the purpose, reader, and scope first, then keeps only the elements a work process or an expression needs by applying ECRS (Eliminate, Combine, Rearrange, Simplify) in that order. The work design mode uses necessity, feasibility, and proportionality checks with ECRS to design a minimum-step process or improve an existing one. The expression mode gives answers, documents, slides, charts, and diagrams one message per unit to remove department-store listing. It supports writing and revision. Use this skill when the user asks for '/lean-work', '/lean', 'keep it lean', 'be practical', 'minimum steps', 'no unnecessary steps', 'streamline this process', 'improve this workflow', 'ECRS', 'be concise', 'just the key points', 'no fluff', 'focus this', 'one message per slide', 'don't just list everything', or 'start from first principles'. Summaries and briefings of documents, web pages, and files are outside its scope. Do not apply it automatically to general tasks without such a request."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Lean Work

> This English version is a translation of the Korean original. It may behave differently from the intent of the original.

This skill defines a way of working that filters out elements that do not serve the reader's purpose and explains the remaining elements in enough depth. Fix the purpose, reader, and scope before filtering anything. You can judge what is needed only after these criteria are set.

It applies to work processes and expression. A work process means the steps of problem solving, planning, analysis, research, coding, and similar tasks. Expression means answers, documents, slides, charts, and diagrams.

## Definitions

Use the terms below only in the sense given in this table.

| Term | Definition |
|------|------------|
| Purpose | The judgment or action the reader will make or carry out after receiving the output |
| Reader | The person who reads or acts on the output. If the user does not specify one, a general adult without background knowledge of the field |
| Scope | The boundary of what the output covers |
| Value | Information or work results that the reader uses directly to achieve the purpose |
| Element | The smallest thing being judged. A work step, sentence, bullet, table row, chart series, slide component, and so on |
| Necessary non-value-adding element | An element that creates no value directly but without which the output becomes unusable or untrustworthy. Steps that meet legal, regulatory, safety, or contractual obligations, and steps that check the accuracy of results |
| Unit | A block of expression the reader sees and takes in at once. One slide, one chart or diagram, one paragraph, one table |
| Message | The one judgment the reader should remember after seeing a unit. A sentence with a subject and a predicate |
| Topic label | A title that names a subject without making a judgment. For example "Market overview", "Background", "Key issues" |
| Department-store listing | Expression that lays out related information at equal weight without a message |
| Message overload | Expression that packs two or more independent claims into one unit |

## Workflow

1. (Fix the criteria) Set the purpose, reader, and scope, and verify the premises
2. (Choose a mode) Pick the mode and the way of writing that fit the type of output
3. (Fix the target) For work design, set the final output and the constraints. For expression, set the message of each unit
4. (Process elements) Apply the checks to every element and process the elements in ECRS order
5. (Output) Build the output with the rules of the chosen mode and the sentence rules
6. (Pre-delivery check) Go through the checklist, then deliver

## Fixing the Criteria

If the criteria shift, the choice of what to keep and what to delete shifts with them. Settle the items below before filtering elements.

- Answer first why the output is needed, what you will make, and how you will make it.
- Write the purpose, reader, and scope in one sentence each. Use any item the user has already set as the criterion as it is.
- Use each definition and criterion in the same sense through the end of the output. Call each thing by a single name.
- Treat both the premises in the user's request and the model's own knowledge as things to verify. Use common sense, authority, well-known frameworks, buzzwords, and marketing terms as evidence only after verifying them.
- When given a problem, trace its causes back to the deepest cause the user can act on. Derive the improvement from that cause. A measure that treats only the surface symptom lets the same problem return.
- Write the conclusion so that a third party with no background knowledge can follow the evidence and accept it. Fill the explanation with expressions whose meaning is clear.
- Match the depth of verification to the impact the judgment has on the conclusion. Check details that cannot change the conclusion lightly.

## Choosing a Mode

| Mode | Way of writing | Output |
|------|----------------|--------|
| Work design | New design | A new work process for problem solving, planning, analysis, research, coding, and similar tasks |
| Work design | Process improvement | An improved version of a current process the user provides, with a record of how each step was handled |
| Expression | Writing | New answers, documents, slides, charts, and diagrams |
| Expression | Revision | A revised version of existing output with a short diagnosis for each unit |

- Every mode follows the fixing of criteria, element judgment, ECRS, and the sentence rules. The work design mode adds the work design rules, and the expression mode adds the unit rules.
- If the user specifies an output structure (a table template, rating scale, fixed table of contents, and so on), keep that structure. In that case, apply element judgment and the sentence rules to each item inside the structure.
- Apply ECRS to each step of a workflow that another instruction defines. Keep the steps and the order that the instruction marks as required.

## Element Judgment

Every element must pass the checks below before delivery to stay. Each check applies to different elements.

| Check | Question | Applies to |
|-------|----------|------------|
| Necessity | If this element is deleted, does the message or the quality of the output change? | All elements |
| Reader relevance | Is this information the reader does not yet know, and does the reader have a reason to know it? | Sentences and expression components |
| Feasibility | Can the user carry it out with the resources and constraints they have? | Work steps |
| Proportionality | Is the effort put in smaller than the value gained? | Work steps |

- Judge necessity against the target. In work design, the target is the final output. In expression, the target is the message of the unit.
- If the constraints needed to judge feasibility are unclear, confirm them with the user before proceeding. Use the constraints the user states as the basis for judging feasibility.
- Keep necessary non-value-adding elements regardless of the judgment result. Apply only Rearrange and Simplify to such elements.
- Handle elements that fail a check in the Eliminate stage of ECRS.

## Applying ECRS

ECRS stands for Eliminate, Combine, Rearrange, and Simplify. It is a work improvement technique that asks about the purpose, place, sequence, performer, and method of each element and sets the direction of improvement from the answers. This skill applies the same questions and the same order to work steps and expression elements.

| Principle | Question | Handling |
|-----------|----------|----------|
| Eliminate | What is this element for, and does the result change without it? | Delete elements that fail the checks |
| Combine | Can it be handled together with another element or grouped into one? | Merge steps and group items into higher categories |
| Rearrange | Does changing the sequence, position, or performer improve the result? | Adjust the sequence, position, and performer |
| Simplify | Can the remaining element be handled in an easier way? | Change the method and the wording to easier ones |

### Order of Application

Fix the order as Eliminate, Combine, Rearrange, Simplify. Each earlier principle reduces what the later principles have to handle.

- Apply Eliminate first. Effort spent polishing an element you will delete leaves nothing in the result.
- Apply Simplify last. If you keep every element and only shorten the sentences, the density of the writing rises while the number of items the reader must process stays the same.
- Consider automation and scripts in the Simplify stage. Automating a step you have not eliminated locks the unnecessary step inside the tool.
- If a later principle creates new targets for an earlier one, apply again from that earlier principle. For example, if duplicates appear after combining, apply Eliminate again.
- Handle every element in one of three ways: keep it in the body in full, move it to another place, or delete it. Naming something in the body while leaving out its content only shifts the burden of looking it up to the reader.

### Eliminate

- The default handling of an element that fails a check is deletion. The effort spent writing an element is no reason to keep it.
- Pass elements that have value as an independent message or reference value to the Rearrange stage.
- A step that resets a problem, direction, or purpose the user has already set is a target for elimination.
- Review deletion candidates among expression elements in the order below.

1. Information unrelated to the message
2. Background the reader already knows
3. Evidence that repeats support for the same conclusion
4. Decorative figures and examples that do not contribute to the judgment

### Combine

- Write steps that run at the same time, or that finish naturally within one task, as a single step.
- Merge consecutive steps that use the same input into one round of processing.
- Group sub-items of an expression into three or four higher categories and move the details to a lower level. Name each category so that it represents all the sub-items under it.
- Group only elements of the same kind in one category. Put causes and effects, symptoms and remedies, and facts and opinions in separate categories.
- Merge units that deliver the same message into one.

### Rearrange

- Order work steps so that the output of each step becomes the input of the next.
- Put checks that could invalidate the whole plan (whether the material exists, constraints, user decisions) at the very front. The later you check, the more steps you have to redo.
- Put a step that checks results right after the step that produced them. An error is cheapest to fix where it was made.
- Place steps that do not depend on each other in the same module so they can run at the same time.
- Assign steps that carry responsibility for the result, such as setting direction and approval, to the user. Assign material processing and drafting to the model or a tool.
- Put the message of an expression at the head of the unit. Move elements with value as an independent message to a separate unit. Move elements that only have reference value to an appendix, footnote, or attachment.
- Arrange the supporting elements in a unit by one criterion chosen from chronological order, structural order, and order of importance.

### Simplify

- Use existing tools, templates, and defaults for work steps first. Add a step that builds a new tool or template only when existing means cannot reach the target.
- Match precision and depth of analysis to the level the purpose requires.
- Turn a step that repeats the same processing many times into batch processing or a script.
- For necessary non-value-adding elements, keep the requirement and make the method easier. Checklists and standard templates are typical methods.
- Rewrite expression elements in plain words and simple sentences according to the sentence rules.

## Work Design Rules

The work design mode presents only the minimum steps needed to reach the final output.

### Target

- Set the final output, the criteria for judging completion, and the constraints (deadline, people, tools, budget, and so on).
- Use the problem and direction the user has defined as fixed inputs.

### New Design

1. Trace back from the final output through the inputs it needs to derive candidate steps
2. Apply element judgment and ECRS to each candidate step
3. Arrange the remaining steps in the output format

When you trace back from the final output, every step produces something the next step uses. A step whose output no later step uses is a target for elimination.

### Process Improvement

1. Record every step of the current process. For each step, note the input, the action, the output, and the performer
2. Apply the ECRS questions to each step and note the answers and the reasons
3. Build the improved process in the order Eliminate, Combine, Rearrange, Simplify
4. Deliver the improved process together with the handling record

The handling record lists every current step. With it, the reader can trace what was done to each step and why.

```
| Current step | Handling | Reason |
|--------------|----------|--------|
| Name of the current step | Eliminate, Combine, Rearrange, Simplify, or Keep, as applicable | The answer to a check or an ECRS question |
```

### Writing Standards

- Process descriptions contain only the actions performed. Leave out the significance, background, and expected benefits of the process. Sentences such as "We propose the following process", "In this step, data is collected", and "This will improve efficiency" are left out.
- Decide the number of modules within the range that passes the checks.
- Attach the handling record only to process improvement.

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

## Unit Rules

In the expression mode, every unit delivers exactly one message. A department-store listing hands the burden of choosing what to look at to the reader. Message overload makes it hard for the reader to grasp the claim of the unit. Both problems come from the same writing habit of placing all the information at hand without selection.

### Setting the Message

- Break the output into a list of units.
- For each unit, answer "What is the one sentence a reader should remember after seeing this unit?"
- If there is no answer, the unit has no message. Write a judgment sentence or delete the unit.
- If the answer strings together two or more independent claims, the unit has message overload. Split the unit by adding a slide, splitting the paragraph, or dividing the chart.
- A topic label carries no judgment, so it does not count as a message. An example of a message is "Low-priced imports cut profitability in the domestic market", a judgment sentence with a subject and a predicate.

### Message Placement

Put the message at the head of the unit.

- On a slide, the headline sentence carries the message.
- On a chart, the title carries the message.
- In a paragraph, the first sentence carries the message. The remaining sentences support only the first sentence.
- With a sentence-style header, the header carries the message and the first sentence of the body opens with evidence.
- With a keyword-style header, the header announces the subject of the message and the first sentence of the body carries the judgment.
- If the subject the header announces differs from the message in the first sentence, rename the header or move the content.

### Number of Components

The default is three to four components or fewer per unit to support the message. People can hold about four chunks of information at once on average. As items increase, the attention each item gets decreases.

- Selected components do not overlap, and each covers a different side of the message.
- Use only as many components as the content requires. If two are enough, use two.
- Keep the built-in count of frameworks with a fixed number of parts, such as a four-quadrant matrix or a five-stage process.
- If five or more seem necessary, check for message overload first. If there is one message, apply Eliminate and then Combine to bring the count to three or four or fewer.
- Apply the same standard to answers that hold several items. If the user asks for a complete list, list everything.

### Emphasis Placement

- Arrange the elements in a unit with different weight in the order of message, supporting elements, and details.
- Set one point of emphasis per unit.
- In slides and designs, guide the eye with size, position, and color. Give the other elements smaller size and lower saturation.
- In charts, highlight only one series and show comparison series at lower saturation. Attach data labels only to points related to the message.
- If every element carries the same weight, treat the unit as having no point of emphasis and rearrange it.

### Signs of Department-Store Listing

If one or more of the signs below appear, rebuild the unit.

- Five or more items of equal rank sit at the same level
- One paragraph holds two or more sentences with independent claims
- The title or headline stays at a topic label
- Every item has the same visual weight and length, leaving no point of emphasis
- Elements of different kinds, such as causes and effects, symptoms and remedies, or facts and opinions, are mixed in one list
- The subject the header announces differs from the message in the first sentence of the body
- You cannot answer "the one sentence to remember from this unit"

## Sentence Rules

Sentences in every mode must pass the necessity and reader relevance checks. Judge length by information density. Every sentence delivers new information.

- Start the answer from the first sentence and end with content in the last sentence. Openers such as "Great question", previews such as "First I will explain A, then B", and closing courtesies such as "I hope this helps" are left out.
- Match the scope of the writing to what the question asks for. Leave out repeated summaries of what you already said, related knowledge outside the question's scope, and alternatives and extra options the user did not ask for.
- Put only one idea in each sentence. Put only one message in each bullet. Do not lengthen a sentence by attaching extra information.
- Use expressions the reader can understand on a first reading. If a technical term is truly needed, add a short definition in parentheses once, at its first appearance. Replace engineering and software-design phrasing (input value, output, mapping, interface, and so on) by the same standard.
- When you switch to plain wording, keep a tone that treats the reader as a general adult. Choose concrete words over catch-all words that blur the meaning. State specialized and technical content accurately and clearly, without distorting its meaning.
- Keep grammar correct regardless of how technical or plain the text is.
- When referring to another document, page, section, data, and so on, write the needed content in the sentence itself so the reader does not have to consult it. Do not replace content with codes, numbers, abbreviations, or summary labels.
- State uncertainty once. Do not repeat hedges in every sentence.
- Instead of contrast constructions of the form "not A, but B", state B directly.
- When the content is the same, state it in the positive form. Write "conversion is possible once structured data is secured" in place of "data readiness is insufficient". A positive sentence states the target state directly, so it is clear and easy to revise and combine sentence by sentence. A negative sentence describes problems case by case, so it is complex and the reader has to infer the target state.

## Revision Procedure

Apply this when revising existing output in the expression mode.

1. Extract every message by unit and diagnose the number of messages in each unit
2. Write a judgment sentence for a unit without a message or delete it, and split units with two or more messages
3. Apply ECRS to each unit and reduce its components to within the standard
4. Apply the sentence rules to the remaining sentences
5. Deliver the revised result with a short diagnosis for each unit

## Common Output Rules

- Put only what the reader needs in the output. Do not reveal in the output that this skill was applied, the names of its rules, or the checking process. The handling record of process improvement and the diagnosis of the revision procedure are exceptions.
- Follow the user or other instructions for writing style and sentence endings, overall structure and table of contents, and markdown format. This skill governs element selection, message placement, and the information density of sentences.

## Examples

The organizations, products, and situations in the examples below are all fictional.

### Process Improvement

(Request) A request to cut down the current process for making an executive report from last month's raw employee survey data in Excel

(Current process)

```
1. Redefine the purpose of the report
2. Benchmark domestic and international survey analysis cases
3. Design an analysis framework
4. Draft the report
5. Clean the data by reviewing responses one by one
6. Compute descriptive statistics
7. Run cross-tabulations
8. Interview stakeholders
9. Derive implications
```

(Improved process)

```
## Module 1. Survey Tabulation
- (Purpose) Identify the survey results that need an executive decision

| Task | Input | Content | Output |
|------|-------|---------|--------|
| 1-1. Data cleaning | Raw survey data in Excel | Remove non-responses and duplicate responses in one pass with filters and duplicate removal | Cleaned data |
| 1-2. Tabulation | Cleaned data | Tabulate response distribution by question and differences by department | Tabulation sheet |

## Module 2. Report Writing
- (Purpose) Write material executives can read once and decide on

| Task | Input | Content | Output |
|------|-------|---------|--------|
| 2-1. Message selection | Tabulation sheet | Select three to four results that need an executive decision | Message list |
| 2-2. Material writing | Message list | Write one slide per message in the existing company report template | Report material |

| Current step | Handling | Reason |
|--------------|----------|--------|
| 1. Redefine the purpose of the report | Eliminate | The user has already set the purpose of the report |
| 2. Benchmark domestic and international survey analysis cases | Eliminate | The effort is too large for the purpose of reporting survey results, so it fails proportionality |
| 3. Design an analysis framework | Eliminate | The survey questions already set the units of analysis, so it fails necessity |
| 4. Draft the report | Rearrange, Simplify | It uses the tabulation results as input, so it moves after message selection and uses the existing company report template |
| 5. Clean the data | Simplify | Review of responses one by one changes to batch processing |
| 6. Compute descriptive statistics | Combine | It finishes within the same tabulation task as the cross-tabulations |
| 7. Run cross-tabulations | Combine | It finishes within the same tabulation task as the descriptive statistics |
| 8. Interview stakeholders | Eliminate | The effort is too large for the purpose of reporting survey results, so it fails proportionality |
| 9. Derive implications | Combine | It is the same task as message selection, which picks the results that need an executive decision |
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

(Diagnosis) The title is a topic label. There are seven items at the same level. Independent messages about falling profitability, regulatory change, and industry structure are mixed, and there is no point of emphasis.

(after, the first slide after splitting)

```
(Headline) Low-priced imports and crowded competition cut profitability in the domestic market
- Many players compete in a flat market, which intensifies pressure to cut prices
- Rising inflow of low-priced imports lowers the average selling price
- With the market flat, higher sales volume cannot offset the fall in profitability
```

(Handling) Consumer awareness, distribution structure, and slow technology adoption do not contribute to the message of falling profitability, so they were deleted or moved to an attachment. The regulatory sandbox program moved to the next slide, which covers opportunity factors. The three remaining elements were rewritten as sentences that show cause and effect.

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
(Title) Performance by division
Bars for all 12 divisions in the same color, with data labels on every bar
```

(Diagnosis) The title is a topic label. All 12 divisions carry the same weight, so the reader has no point to look at.

(after)

```
(Title) The materials division generated more than half of company-wide revenue growth
Only the materials division bar in the accent color, with a data label
Only the top three other divisions at low saturation, with the rest summed as "Other"
```

(Handling) The title now carries the message. Lower divisions were grouped as "Other" to reduce the number of items shown. The highlighted series was set to the materials division alone.

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
- Check where meeting audio and records are stored and who can access them. The tool must pass your internal security rules before the other conditions are worth weighing.
- Test speech recognition accuracy with real meeting recordings. The benefit of adoption remains only if people spend little time fixing errors.
- Check whether it integrates with the collaboration tools you already use. With integration, meeting records flow into those tools automatically.
```

## Exceptions

- If the user asks for "more detail", "be specific", "a detailed process", or "all the steps", do not apply Eliminate, Combine, the concision standard, or the count standard to that scope.
- If the user asks for a complete list or a detailed inventory, do not apply the count standard to that scope.
- For output whose purpose is a complete list, such as laws, regulations, and checklists, apply only the emphasis placement rules in place of the count standard.
- Keep the built-in count of frameworks and standard templates with a fixed number of parts.
- Exclude quotations, verbatim reproductions of source text, and code bodies. Apply the rules to the explanatory sentences before and after code.

## Pre-Delivery Checklist

- Are the purpose, reader, and scope set, and are definitions and criteria used in the same sense through the end of the output?
- Did you use the user's premises and the model's knowledge as evidence only after verifying them?
- Is the improvement for a problem derived from the deepest cause the user can act on?
- Did every element pass the checks that apply to it?
- Did you apply Eliminate, Combine, Rearrange, and Simplify in this order?
- Do the necessary non-value-adding elements remain in the output?
- Did you delete each failed element or move it to another unit or an attachment?
- Is the work process free of steps that reset a problem or direction the user already set?
- Are the work steps in an order where each step's output becomes the next step's input?
- Are the checks that could invalidate the plan near the front of the process?
- Does the handling record of a process improvement list every current step?
- Does every unit deliver exactly one message in the form of a judgment sentence?
- Does each unit have three to four components or fewer (excluding built-in framework counts and exceptions)?
- Does each unit have one point of emphasis?
- Does the first sentence start with the answer, and does the last sentence end with content?
- Does each sentence hold one idea and each bullet one message?
- Is the output free of any sign that this skill was applied or of its rule names (excluding the handling record and the diagnosis)?
