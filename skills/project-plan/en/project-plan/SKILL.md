---
name: project-plan
description: Reads the RFP or statement of work, proposal, kickoff report, and contract and staffing documents of a project that is already under contract, then writes a project overview and a WBS (task schedule). Covers schedule buffer, person-month (M/M) allocation, optional RACI, schedule delay response and review of an existing WBS, with output as MD, CSV, XLSX or PDF. Use it for requests like "build a WBS", "make the project schedule", "plan after kickoff", "project overview", "project charter", "allocate person-months", "Gantt chart", "we are behind schedule", "the deadline is at risk" or "review our WBS", even when the word WBS is missing. Reads references/skeletons.md (stage templates by project type), references/survey.md (survey schedule risk), references/recovery.md (delay recovery options), references/review.md (WBS review order) and references/output.md (plan.json format and file export) when needed.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Project Overview and WBS

> This skill was translated from the Korean original (project-plan-ko). The translation may make it behave differently from the original intent.

This skill produces one overview and one task schedule for a project that is already under contract and running. The target is a single table that the project manager and team leads open every week. `scripts/plan.py` computes dates, buffer ratios and M/M totals. File paths in this document are relative to the folder that holds SKILL.md.

## Design principles

A plan with too many things to manage tends to get written once and never used, so the plan stays light under these principles.

- (One table) The number of rows follows the size of the work. A one-month project gets a short table close to a to-do list, a one-year project gets a long one, and the rules stay the same
- (Defaults) M/M is on by default and RACI is off by default. Either can be switched when the user asks
- (Division of labor) The model reads documents, drafts and replans. Code computes dates, ratios and totals. Progress tracking continues in the spreadsheet or PM tool the user already uses
- (Unknown values) Mark any number missing from the documents as `[To confirm: item]`. Date fields cannot be empty, so enter an assumed date and write `[To confirm: date]` in the notes. A table filled with plausible guesses becomes the basis for a wrong schedule and budget

## Inputs

If no documents are attached, first ask: "Please upload whatever you have among the RFP or statement of work, proposal, kickoff report, contract and staffing documents." When the environment cannot read a file directly, extract text first with `python scripts/to_md.py files -o inputs.md`.

| Document | What to take from it |
|---|---|
| RFP or statement of work | Scope, task items, deliverables, number and timing of reports, required advisory meetings and public hearings, project period |
| Proposal | Method, planned schedule, staffing, promised survey sizes and meeting counts |
| Kickoff report | Schedule agreed with the client, agreed decisions, changes from the proposal |
| Contract and staffing documents | Contract period, contract amount, team members and allocations, person-months used for labor cost |

- Treat survey sizes and meeting counts promised in the proposal as commitments and put them in the rows
- When documents disagree, use the document below for each item and record the conflict in the overview notes
- (Source for period, amount and staffing) Contract and staffing documents
- (Source for scope and deliverables) RFP or statement of work
- (Source for method and schedule) Kickoff report. Without one, the proposal

## Steps

1. Read the documents and list the project name, period, client, report dates, deliverables and staffing
2. Ask in one message only for required items the documents do not answer. Required items are the contract end date, report meeting dates and staffing. State the default for each question, and if there is no answer, proceed with the default and mark it `[To confirm]`
3. Pick the stage template for the project type in `references/skeletons.md` and turn the RFP task items into rows. If there is a survey, also read `references/survey.md`
4. Write plan.json in the format of `assets/plan_example.json`. Field descriptions are in `references/output.md`
5. Run `python scripts/plan.py check plan.json`. With 1-2 warnings, fix them and run once more. If 3 or more remain, present the draft together with the list of remaining warnings
6. Build the overview with `python scripts/plan.py md plan.json -o overview.md`. Produce CSV, XLSX or PDF when the user asks

From the second request on the same project, edit plan.json and export again. Report only the changed rows, the change in buffer days and any remaining warnings.

## Writing rows

### Row types

Every row has one of the types below. The question that separates them is "if this row runs late, is it our team's fault?"

| Type | Meaning | Examples |
|---|---|---|
| Work (work) | Our team does it and controls when it ends | Drafting a questionnaire, status analysis, report draft |
| Wait (wait) | The client or an outside body decides when it ends | Client review, data reply, survey responses, recruiting participants |
| Checkpoint (check) | A report or meeting on a fixed date | Kickoff meeting, interim report meeting, advisory meeting, public hearing |
| Buffer (buffer) | Time kept empty to absorb delays | Between the last task and the contract end date |

If a wait sits inside a work row, the row keeps its length while the wait grows, so the delay stays hidden. Dated wait rows also serve as evidence when a delay comes from the client side.

### Size of one row

- One row is a unit one owner can finish and whose completion can be confirmed
- A work row should end within one progress check cycle. `plan.py` warns about work rows longer than 28 days. Split long work at an interim output
- Monthly recurring management work stays as one row with `allow_long` set
- Use two levels, stage and task, and number rows by their position in the table
- Write the next weeks in detail and later months in larger rows, then split those rows when their time comes

### Completion criteria

The deliverable (done when) cell states in one line what meets which condition and who confirms it.

- e.g. Previous plan comparison table has no blank carry-over decisions, PM approved
- e.g. Valid responses reach 80% of the target sample, PM approved
- Take condition values from the RFP and proposal. If the documents give no value, write `[To confirm]`

### Rows people forget

- (Project management stage) Put kickoff preparation, kickoff meeting, progress and risk management, interim report, final report and closing as the first stage. Without it, reporting and acceptance time disappears from the schedule and the plan looks shorter than reality
- (External events) Split an advisory meeting into three rows: request (work), meeting (checkpoint), reflecting input (work). Split a public hearing into four rows: preparation (including a wait), hearing, summary of results, reflecting input
- (Event spacing) Hold the first advisory meeting right after the main research and analysis. Keep advisory meetings at least 4 weeks apart, the last one at least 4 weeks before the final report, and a public hearing at least 6 weeks before the final report. An event without time to reflect its input ends as a formality
- (Client review) For each major report, add rows in this order: draft, internal review, submission, client review wait, revision
- (Data collection) Split into collection plan, data request, reply wait, cleaning and final dataset
- (Stage write-ups) End each stage with a row that fixes that stage's output in writing. The last report row only edits and combines. If the last report row exceeds 15% of the total period, the stage write-up rows are missing
- (Contract deliverables) Presentation slides, summary report, database, raw data and other deliverables named in the contract each get their own row. Check the contract deliverable list against the rows one to one

### Scope check

- Every RFP task item and contract deliverable maps to at least one row
- The same work does not appear in two rows
- Work outside the scope does not become a row and goes into the notes

### Estimating durations

- Duration equals pure work days divided by the owner's allocation. A 5-day task for someone at 50% allocation takes about 10 days
- If the allocation is unknown, use 0.8 for a dedicated person, 0.4 for someone on two projects and 0.2 for someone on three. A dedicated person still spends time on meetings and admin, and switching between projects costs more time
- For waits, use the actual processing time of the organization first. Without one, assume 1-2 weeks for client review, 2-4 weeks for data replies from agencies, 1-3 weeks for advisory replies and 2-3 weeks for recruiting, and note that these are assumptions
- For rows that depend on formal procedures such as ethics review (IRB), statistics approval, permits or accredited testing, check the processing time with the organization right after kickoff

### Standard notes

Use these phrases first in the notes and write the response next to them.

- (Uncertain result) A row whose result cannot be guaranteed, such as survey responses or an experiment. Add the follow-up row to run if it falls short
- (Depends on one person) A row that stops without a specific expert or piece of equipment. Name the backup person or source
- (Deadline critical) A row whose delay moves the final deadline. Check it first in the monthly review

## Schedule buffer

People tend to estimate durations optimistically. Slack hidden in each task gets used up inside the task through late starts and filling the remaining time. So the buffer sits in one place, visible in the table, and its use is tracked.

- (Location) Put one row of type buffer between the last work row and the contract end date. The end date of the last work row becomes the team's internal target
- (Size) If past similar projects have delay records, use their average delay ratio. Without records, keep at least 15% of the total period. `plan.py` computes the ratio and warns when it falls short
- (Task durations) Write realistic estimates for individual tasks. For uncertain rows, keep the base duration and add a follow-up row for the shortfall case. The follow-up row takes 30-50% of the base row's duration, and the criteria for choosing the ratio are in `references/survey.md` and `references/skeletons.md`
- (When 15% is out of reach) Choose among overlapping loosely dependent tasks, adding people, and negotiating scope or deadline. The effects of each option are in `references/recovery.md`
- (Tracking use) Record the original plan's last work end date in `baseline_last_end` in plan.json. Each month compare progress with buffer used, and if buffer used exceeds progress, go through the options in `references/recovery.md`

## Person-months (M/M)

1 M/M is one person working a full month on this project. A 50% allocation for 6 months is 3.0 M/M.

- The staffing table has people as rows and months as columns. Monthly values follow the workload of that month's rows
- A person's monthly value stays at or below 1.0 and each person's total equals the M/M in the contract documents. `plan.py` checks both
- If allocations on other projects are known, check that the combined allocation stays within 100%
- If the user does not need M/M tracking, set `options.mm` to false

## RACI (optional)

Only when the user asks, set `options.raci` to true and write each person's role on each work row.

| Letter | Role |
|---|---|
| R | Does the work. Several people allowed |
| A | Owns the outcome. Exactly one person per task |
| C | Gives input before the work is done |
| I | Receives the result |

## Overview

`plan.py md` assembles the overview in the order below. The model fills the `overview` fields in plan.json, and code builds the WBS, checkpoint list and detail tables from the rows.

| Section | How to fill it |
|---|---|
| Basic Information | Project name, period and staffing are automatic. Client and contract type go in `summary` |
| Why (Beneficiaries & Needs/Problems) | Who benefits from the result and which problem the project solves, based on the documents |
| Project Goals | Derived from the purpose in the RFP. Each goal is a sentence whose achievement can be judged at the end |
| WBS | Automatic. One buffer line and a stage summary |
| Hypotheses & Solutions | A hypothesis is a judgment that shapes the result but is not yet confirmed. A solution is work that tests the hypothesis or brings it into the result, named like the matching WBS row |
| Success Criteria | Three lines or fewer. Each can be answered yes or no at the end |
| Reviews, Advisory Meetings and Other Checkpoints | Automatic. Rows of type checkpoint |
| Notes | Risks, possible scope changes, external changes, conflicts between documents, the `[To confirm]` list |
| WBS Detail, Staffing | Automatic. Full row table and monthly M/M per person |

- Keep a terse bullet style with one point per line
- Dates and numbers in the overview must match plan.json, so take any number added to a sentence from plan.json

## Export commands

```bash
python scripts/plan.py check plan.json            # checks only
python scripts/plan.py md   plan.json -o overview.md
python scripts/plan.py csv  plan.json -o wbs.csv   # also writes wbs_mm.csv when M/M is on
python scripts/plan.py xlsx plan.json -o wbs.xlsx
python scripts/md2pdf.py overview.md -o overview.pdf
```

- `check`, `md` and `csv` need no packages. `xlsx` needs openpyxl, PDF needs fpdf2 and markdown-it-py, and document conversion needs markitdown (python-hwpx optional for HWPX)
- The XLSX has one WBS sheet, plus one staffing sheet when M/M is on. Black text, thin borders and a gray header only. Gantt headers run horizontally. The upper row has one merged white cell per month, such as "Mar 2026", and the row below shows the Monday date of each week. Gantt cells are formulas, so the marks move when dates change
- CSV is saved as UTF-8 with BOM so spreadsheet programs read non-English text correctly. Use it to move the plan into another PM tool
- The PDF script finds an installed font. If none is found, pass `--font path/to/font`
- In environments with a file delivery feature, deliver the files. Otherwise give the file paths

## Delays and crises

When the user says the project is behind or the deadline is at risk, or when buffer used exceeds progress, read `references/recovery.md` and present options. First update plan.json to the current state, compute the remaining buffer with `plan.py check`, then compare the options.

## Reviewing an existing WBS

When the user asks for a review of a WBS or schedule they already have, follow the order in `references/review.md`. Look at the items that make the schedule itself wrong first and at completeness items after.

## Before delivery

- Does every RFP task item and contract deliverable map to a row?
- Are waits separated from work rows?
- Are the `plan.py check` warnings fixed, or reported to the user?
- Is there a buffer row and does its ratio meet the target?
- Are the `[To confirm]` items collected in the notes?
- Do the dates and numbers in the overview match plan.json?
