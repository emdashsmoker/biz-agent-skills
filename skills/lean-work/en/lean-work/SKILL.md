---
name: lean-work
description: A lean work skill that first fixes the purpose, reader, and scope, then keeps only the elements a work process or deliverable needs. It applies necessity, reader relevance, feasibility, and proportionality checks to every element to produce minimum-step work plans, one-message-per-unit expression, concise sentences, and fixed-format summaries. It supports both writing new output and revising existing output. Use this skill when the user asks for "/lean-work", "keep it lean", "be practical", "be realistic", "minimum steps", "no unnecessary steps", "be concise", "just the key points", "short version", "no fluff", "TL;DR", "focus this", "one message per slide", "boil it down to one message", "don't just list everything", "summarize", "brief me", "sum this up", "start from first principles", or asks for a summary of a web page, file, or pasted text. Do not apply it automatically to general tasks without such a request.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Lean Work

> This English version is a translation of the Korean original. It may behave differently from the intent of the original.

This skill defines a way of working that filters out elements that do not serve the reader's purpose and explains the remaining elements in enough depth. Fix the purpose, reader, and scope before filtering anything. You can only judge what is needed once these criteria are set.

It applies to work processes, the expression of answers and documents, and summaries of external material.

## Definitions

Use the terms below only in the sense given in this table.

| Term | Definition |
|------|------------|
| Purpose | The judgment or action the reader will make or carry out after receiving the output |
| Reader | The person who reads or acts on the output. If the user does not specify one, a non-specialist adult with the general knowledge of a first-year university student |
| Scope | The boundary of what the output covers |
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
| Summary | Briefings on web pages, files, and pasted text | All rules of the expression mode plus the summary format |

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

Handle any element that fails even one of the checks that apply to it as follows.

- The default is deletion. Do not keep something in the body because writing it took effort.
- If it has value as an independent message, split it into a separate unit.
- If it only has reference value, move it to an appendix, footnote, or attachment.
- Merge a work step into an adjacent step or delete it.
- Do not use the halfway option of naming something in the body and leaving out its content.

If the constraints needed to judge feasibility are unclear, confirm them with the user before proceeding. If the user has stated constraints, use them as the basis for judging feasibility. Keep steps with high sensitivity, such as law, regulation, and safety, regardless of the judgment result.

## Work Design Rules

The work design mode presents only the minimum steps needed to reach the goal.

- If the user has defined the problem, do not add a step that redefines it. If the user has given a direction, do not add a step that explores directions.
- Write steps that run at the same time, or that finish naturally within one task, as a single step.
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

In the expression and summary modes, every unit delivers exactly one message. A department-store listing hands the burden of choosing what to look at to the reader. When one unit packs in several independent claims, the reader cannot tell what that unit says.

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

### Selecting Components

The default is three to four components or fewer per unit to support the message. People can hold only a limited number of information chunks at once, so as items increase, the attention each item gets decreases.

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
- Replace expressions the reader could not understand on one reading with plain ones. If a technical term cannot be avoided, add a short definition in parentheses once, at its first appearance.
- State uncertainty once. Do not repeat hedges in every sentence.
- Instead of contrast constructions of the form "not A, but B", state B directly.
- Put only one message in each bullet. The recommended length is about 100 characters for Korean text and about 15 words on average for English text. Do not cram unnecessary information into that length.

## Summary Format

The goal of the summary mode is a briefing that lets a third party with no background knowledge grasp the gist of a document and the author's intent within five minutes. The summary mode adds the format below on top of the expression mode rules.

### Obtaining the Input

| Input type | How to obtain it |
|------------|------------------|
| URL | Retrieve the full body text with an available web page reading tool |
| PDF, image, document file | Read the file directly and apply text recognition (OCR) if needed |
| Pasted text | Use the text as given |
| Mixed input | Obtain each source separately, then combine them |

- If the input is incomplete or access is blocked, tell the user and proceed with only the information obtained.
- Do not work around logins, paid subscriptions, or access restrictions to obtain material.
- Write the output in the user's language, whatever the language of the input.

### Output Template

Do not change the section names, section levels, or section order.

```
# [Document title or a title extracted from the body]
[Input type] | [Author] | [Year of publication]

## Overview
- A [document type] written by [author] for [target reader] to [purpose]

## Background
- [Background and motive for publication]

## Main Points
- (Subheading) [Main claim]
- [Evidence or elaboration supporting the claim]
- (Subheading) [Main claim]
- [Evidence or elaboration supporting the claim]

> Organization or author (year), title of material (link)

## Implications
**[One sentence of assessment that runs through the whole document]**
- [Evidence or elaboration 1]
- [Evidence or elaboration 2]
- [Evidence or elaboration 3]
```

### Section Rules

| Section | Length | Writing criteria |
|---------|--------|------------------|
| Overview | 1 line | Write only the author, document type, purpose, and target reader. Do not include assessments or conclusions. Add a short definition in parentheses for technical terms |
| Background | 1-3 lines | Write the background and motive for publication. If the stated purpose differs from the actual motive, write both |
| Main Points | The longest section of the summary | Write three main claims or fewer. Extract only what the document states. Mark inferences as inferences, for example with "appears to" |
| Implications | Fixed at 4 lines | Write one line of assessment in bold and exactly three bullets of evidence. Do not exceed four lines |

- Arrange bullets in Main Points this way. A bullet that starts with a parenthesized subheading is a claim, and the bullets without a subheading that follow it are the evidence for that claim.
- Set the number of evidence bullets to match the complexity of the claim. The total line count of Main Points must exceed the line count of Implications.
- Add a parenthesized subheading only when it is needed to tell claims apart.

### Citation Criteria

- Use three pieces of quantitative data or fewer in the whole summary. The more figures there are, the harder it becomes for the reader to pick the ones that matter for a decision.
- When you use quantitative data, give the source in a `>` block in the form "Organization or author (year), title of material (link)".
- Quote only short phrases of the original in quotation marks and give the source. Put the rest in your own words.

### Edge Cases

| Situation | Handling |
|-----------|----------|
| Text without claims (personal impressions, lists of opinions, and so on) | List the main content under Main Points and state that there is no main claim |
| URL not accessible | Tell the user and proceed with only the information provided |
| Input in several languages | Unify the output in the user's language |
| Short input such as a brief post | Keep the format and shorten each section |
| Input containing personal information | Summarize it and mask information that could identify individuals |

## Revision Procedure

Apply this when revising existing output in the expression mode.

1. Extract every message by unit and diagnose the number of messages in each unit
2. Split units with two or more messages and reduce components to within the standard
3. Apply element judgment and the sentence rules to the remaining sentences
4. Deliver the revised result with a short diagnosis for each unit

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

(Handling) The user had already set the purpose of the report, so the redefinition step was deleted. Benchmarking, framework design, and interviews took too much effort relative to the purpose of reporting survey results, so they failed the proportionality check. Descriptive statistics and cross-tabulations finish in one tabulation task, so they were merged. Deriving implications was merged into the message selection step.

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

### Summary

(Input) A press release from a fictional metropolitan city announcing a plan to expand public bicycles

(after)

```
# Public Bicycle Expansion Plan
Web (press release) | City of OO | 2025

## Overview
- A press release issued by the City of OO for residents and transport departments to announce the direction of expanding public bicycle rental stations

## Background
- Reliance on cars for short trips in the city center was identified as a cause of traffic congestion
- Existing rental stations were concentrated downtown, which made them hard to use for residents of outer residential areas

## Main Points
- (Station expansion) The city presents a plan to add rental stations in outer residential areas and around subway stations
- The aim appears to be encouraging people to use bicycles for trips between subway stations and homes
- (Fare reform) The city presents a plan to discount bicycle fares when transferring to public transit
- The press release does not state the size of the discount or when it takes effect
- (Operations) The city is considering outsourcing breakdown reports and bicycle redistribution to a private operator
- The operator and selection process are to be announced later

> City of OO (2025), Public Bicycle Expansion Plan (link)

## Implications
**An expansion plan aimed at demand for trips between outer residential areas and subway stations**
- If the transfer discount takes effect, trips that combine public transit and bicycles may increase
- The size and timing of the discount are missing, so follow-up announcements need checking
- If operations are outsourced, the standards for managing redistribution quality appear to decide the plan's success
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
- Does every unit deliver exactly one message in the form of a judgment sentence?
- Does each unit have three to four components or fewer (excluding built-in framework counts and exceptions)?
- Did you compress by selecting elements?
- Does each unit have one point of emphasis?
- Does the first sentence start with the answer, and does the last sentence avoid courtesies and unrequested offers?
- Does each bullet hold one message within the recommended length?
- Did you follow the section names, order, and length standards of the summary format?
- Are there three pieces of quantitative data or fewer, each with a source?
- Is the output free of any sign that this skill was applied or of its rule names?
