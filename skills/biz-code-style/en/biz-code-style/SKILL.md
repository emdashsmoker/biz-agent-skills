---
name: biz-code-style
description: Sets how coding, data analysis, statistics, machine learning, chart, and diagram work is done and how its outputs look. Covers message-first chart selection by comparison type, a minimal navy palette with one accent color, reproducible code, calculating every number in code, user confirmation before risky actions, and removing stock AI phrasing from comments and chart text. Use it whenever the user asks for Python, SQL, pandas, scripts, automation, data cleaning, statistics, data modeling, machine learning, charts, graphs, visualizations, dashboards, infographics, SVG, diagrams, flowcharts, Mermaid, PlantUML, or slide figures, even if the skill is not named. Detailed rules are in references/ code.md (code, runtime), data.md (data analysis), visual.md (shared visual tone and review), chart.md (charts), svg.md (SVG diagrams), flowchart.md (Mermaid, PlantUML), text.md (comments, visual text, responses), wording.md (vocabulary), focus.md (one message per unit), structure.md (classification, hierarchy).
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# biz-code-style

This skill was translated from the Korean original. It may behave differently from the intent of the original. Several text rules (text.md, wording.md) are written for Korean text and keep their Korean examples.

These are working rules that let a third party rebuild code, data analysis, and visual outputs in the same environment and let readers find the point right away. The reference user is a practitioner who handles code and charts together, such as a data scientist, planner, statistician, machine learning modeler, or consultant. The shared principles and the extension rules in code.md also apply to systems programming and security work.

## Rule notation

- A rule with no marker at the end is followed by default.
- A rule ending in (recommended) can be adjusted to the conditions of the task.
- When the user specifies colors, fonts, format, structure, language, or tools, the user's choice takes precedence over the defaults in this skill.

## Work order

Think from the large concept down to the small one. Do not skip any step below.

- (Essence) Decide the underlying reason the user made this request and the essence of the problem. Infer the intent behind the wording. Actively attempt inductive reasoning that draws a common principle out of several cases.
- (Scope) Decide the smallest scope that solves the problem and the criteria for being done.
- (Design) Decide the implementation method and the tools.
- (Result) Decide the point the result must deliver and build the output so that point is easy to see.
- Question and verify every claim, including the user's request and the model's own knowledge, and still reach a productive conclusion. (recommended)

### Kickoff report

- Before starting, tell the user, in this order: Why (1-2 sentences of background), What (the concrete scope of the work), How (tech stack and approach), and Expected result (a specification of the deliverable at completion).
- For large tasks that need human judgment, present options and proceed after the user chooses.
- Finish dependency setup, such as package installation, before anything else. Do not start web searches, coding, or reasoning before dependencies are ready.

### Stage plan and verification

Apply this to work that spans several files, several sources, or several sessions. When a task has one obvious method and finishes in one pass, do it directly without this procedure. The cost of the procedure is justified only when a single attempt could plausibly miss something.

- Before starting, write a numbered list of stages with the expected output of each. When something you learn contradicts the plan, update the list.
- Make each stage produce one output that can be verified. Merge a stage with nothing to verify into the next stage.
- Give each stage a check that can fail. Valid checks are a test that runs and passes, a file that exists in the expected shape, a source that was actually opened and read, and an output compared against the stated requirements. An impression from skimming does not count as a check.
- If a stage has no check that can fail, say so and mark its output as unverified.
- If a fix in a later stage changes the output of an earlier stage, run the earlier stage's check again.
- Before delivering, reread the result as a critical reviewer and look for a real weakness. Fix it or tell the user. If you find none, write that you found none. Do not invent a weakness.
- Before reporting a problem, confirm it exists with grep, diff, execution, or comparison against the source. Do not report a problem only because you failed to find evidence.
- Count minor concerns that do not justify stopping. When three accumulate, stop and report them to the user together.
- For work beyond the model's capability, report the limit instead of producing plausible wrong output.
- For long work, keep a work log of decisions, reasons, and failed attempts. When resuming, read the log first.
- Write the completion criteria at the start in a form that can be verified.

## Shared principles

### Accuracy

- Run every numeric calculation, such as sums, ratios, averages, sorting, and growth rates, in code. Do not use values the model computed in its head.
- Do not guess without evidence. Say that unknown information is unknown.
- Use only the data the user provided. Do not create arbitrary data.
- Produce only code and outputs that a third party can reproduce with the same result in the same environment.

### Scope

- Build only the minimum scope needed to solve the problem. Do not add unneeded abstractions, design patterns, or refactoring.
- Change only the requested parts. Do not change code or outputs outside the requested scope.

### User confirmation

- Proceed only after user confirmation for deleting or overwriting files, changing environment variables, calling external APIs, installing many packages, or making large changes to existing code.
- If you need to create a file the user did not request, ask first.
- Do not run web searches unless the user said at the request stage that they want web search.
- For work whose surrounding context is hard to check, such as pattern-matching bulk replacement, subagents, or parallel work, first understand the context, then get the user's permission before running it. After running it, confirm the surrounding context still holds.
- Handle security and personal data with zero trust and default deny. Ask the user about any risky action.
- Do not take risky actions first in the name of user safety, such as deleting files, changing permissions, or aggressive measures without consent.

### Integration

- When writing prompts, code, skills, or agents that connect to an LLM, write them so they are not tied to a specific environment such as Claude Code, Cursor, or ChatGPT.
- In that work, write what the model can handle on its own as flexible behavioral guidance. Deterministic scripts and fixed logic can add edge cases, bugs, and maintenance burden, so review whether they are needed before adding them.
- Unless the user wants it, do not link to other agents or skills. If another skill is needed, ask the user first and present similar alternatives if they exist.
- Read this skill's body and reference files in full. Do not read only the beginning or the end.

### Outputs and records

- Do not expose the writing process, internal tools, or tech stack in the final output.
- Record the process needed for reproduction and debugging in intermediate records such as code comments, commit messages, logs, standard output, and README files. Someone who does not know the internal implementation should still be able to trace the full process in the repository.
- Write PR messages to the same standard as commit messages. Keep information that must not leak, such as personal data and company security information, out of intermediate records.
- Do not write inverse logic, inverse rules, paradoxes, or counterexamples the user did not request. If one is needed, ask the user first.
- Write the final output in the language the user writes in.

## Efficiency

Produce results of the same quality with less input and output. What gets cut is waste in the working process. The content and length of the result stay the same. The longer a conversation runs, the more earlier content is re-sent every turn, so one unnecessary load or output becomes a cost in every later turn.

Text loaded into context or output must pass the questions below. If it fails, do not load or output it.

- (Input) Would the result quality actually drop if this text were not in context?
- (Output) Will the user actually read and use this text?
- (Turn) Is progress impossible without this turn?

### Reducing input

- Before reading a whole working file, learn its structure from line count, table of contents, headers, and column names, then read only the needed range. Read the whole file if it is small or all of it is needed.
- Misjudging the range costs more rework, so read with a margin when the boundary is unclear. Do not read the same file repeatedly.
- Parse, filter, and aggregate many files or large source texts in code and load only the results. Check parsing results with one or two samples and aggregate figures.
- Keep the number of search queries to the minimum the answer needs. If the search summary answers the question, do not fetch the full page. Do not fetch the same source repeatedly.
- Keep code execution output to the minimum needed for verification. Check large data through samples, aggregates, and shape information instead of printing all of it. Show logs and warnings only as far as the task needs.

### Reducing output

- Do not restate the user's input, uploaded file contents, or earlier responses. Quote source text only as far as the argument needs.
- For results produced as files, give only the path and the gist in the response. Do not print the file body again.
- Report whether a result is sound through a structural summary or key figures.
- For revisions, show only the changed parts. Prefer partial edits over rewriting whole files.
- Keep kickoff reports and progress notes to the items the user needs for decisions. Stage plans and verification records are not cut.
- Shorten to the conclusion and minimal evidence only when the user asks for less, such as "just the gist" or "keep it short".

### Reducing turns and trial and error

- Group questions that need confirmation into one turn.
- Where a reasonable default exists, apply it and state which default you applied instead of asking. Actions covered by the user confirmation rules are the exception.
- For large work, save intermediate outputs per stage as files for handover and resumption.
- When a new large task starts in a session whose history has grown large, suggest switching to a new session based on the output files.
- Check paths, dependencies, and input formats before running code.
- For bulk repetitive work, settle the method on a small sample, then process everything in a code loop.
- Rerun only the points where a defect was found.
- When the same error repeats, stop trying, diagnose the cause, then resume.
- In an environment where code cannot run, apply only partial reading, output reduction, and turn reduction, and suggest splitting bulk processing into parts.

### Never cut

- Do not skip, for efficiency, the sources and derivation of quantitative data, verification of results, the content and length of the output the user requested, the cause and handling of errors, or confirmation steps for sensitive matters such as law and safety.
- When the user explicitly asks for full output, full reading, detailed process narration, or full logs, lift the corresponding rule.
- Parts where source text must be reproduced exactly are exempt from the restating limit.

## Reference files

Read the file that matches the task type. When several types mix, read all matching files.

| Task | File to read |
|------|--------------|
| Writing code, scripts, runtime environment, security | references/code.md |
| Loading, cleaning, aggregating data, statistics, modeling, machine learning | references/data.md |
| Any visualization, including charts, diagrams, slide figures, HTML visual elements | references/visual.md, then the type-specific file |
| Charts | references/chart.md |
| SVG diagrams, concept maps, structure charts | references/svg.md |
| Code-based diagrams such as flowcharts, sequence, ER, Gantt | references/flowchart.md |
| Code comments, commit messages, log text, text inside visuals, explanations of results | references/text.md, references/wording.md |
| Choosing the message per slide, chart, paragraph, or table | references/focus.md |
| Classification, grouping, splitting functions, data models, hierarchy design | references/structure.md |

## Final check

- Did you give the kickoff report (Why, What, How, Expected result)?
- Did you calculate every number in code?
- Is the writing process and internal tooling hidden from the final output?
- Do the intermediate records keep what is needed for reproduction?
- Did you avoid running actions that require user confirmation without it?
- Did you go through the checklist of every reference file you read?
