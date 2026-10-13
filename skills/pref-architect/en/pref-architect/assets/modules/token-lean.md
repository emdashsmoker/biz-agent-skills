---
name: token-lean
description: "Procedure for producing the same quality of output with fewer input and output tokens. Cuts unneeded file loads, repeated source output, extra turns, and trial and error. Load it when the always-on instructions say to load this module, when the work is token-heavy (bulk parsing, mass research, many tool calls, long outputs, repetitive file operations), or when the user asks for \"/token-lean\", \"save tokens\", \"save context\", \"keep it light\", and similar."
metadata:
  generator: pref-architect
  generator-version: "1.0"
---

# token-lean

A procedure for completing the same output with fewer tokens. What gets cut is waste in the work process. The content of the output is not cut.

## Screening questions

All text loaded into context or output must pass the questions below. If it does not pass, do not load it or output it.

- (Input) Would the output's quality actually drop without this text in context?
- (Output) Will the user actually read and use this text?
- (Turn) Is it impossible to proceed without this turn?

As a conversation grows, each turn's input includes the whole earlier conversation. So one unneeded load or output adds cost again in every later turn.

## Cutting input

### Loading files

- Before reading a whole file, check its structure (line count, table of contents, headers, column names).
- After checking the structure, read only the range the work needs.
- Read a whole file only when it is small or all of it is actually needed.
- Do not read the same file repeatedly. Get the needed information on the first read.
- Misjudging the range costs more through rereads. If the boundary is unclear, read with some margin.

### Bulk parsing

- When there are many files or the source is large, parse, filter, and aggregate with code and load only the result into context.
- Avoid having the model scan the entire source directly.
- Check that parsing results are right with one or two samples and aggregate numbers.

### Search and page fetching

- Keep the number of searches to the minimum the answer needs.
- If search result summaries are enough to answer, do not fetch full pages.
- If the full source is needed, use only the needed parts.
- Do not fetch the same material repeatedly.

### Tool output

- When running code, keep standard output to the minimum needed for checking.
- For large data, do not print everything. Check with samples, aggregates, and shape information.
- Show logs and warnings only at the level the work needs.

## Cutting output

- Do not restate user input, uploaded file contents, or earlier responses. Keep quotations of source text to the minimum an argument needs.
- For outputs made as files, give only the path and gist in the response. Do not print the file body again in the response. Report that the output was made correctly with a structure summary or key numbers.
- When revising an existing output, show only what changed. For files, prefer partial edits over rewriting the whole file.
- Keep kickoff reports and progress notes short, limited to what the user needs to decide.
- Keep intermediate reasoning and work notes short. Their language follows the (Reasoning language) setting of write-standard or code-standard, or English if there is no such setting. Write only the final result in the user's language.
- Do not repeat summaries of the same information.
- The default is quality-neutral saving. Keep the output's content and evidence. Cut down to the core conclusion and minimal evidence only when the user asks for less, as in "just the gist" or "keep it short."

## Cutting turns

- Bundle the questions that need confirmation into one turn.
- For items with a reasonable default, do not ask. State the default applied and proceed.
- Save intermediate outputs as files so handoffs and restarts do not need repeated explanation.
- If a new large task starts in a session whose history has grown very long, suggest moving to a new session based on the output files.

## Cutting trial and error

- Before running code, check paths, dependencies, and input formats to reduce fail-and-rerun loops.
- For large repetitive work, test the approach on a small batch first, then process everything in a code loop.
- Narrow checks to the points that can fail, and rerun only the points where defects appear.
- If the same error repeats, stop trying, diagnose the cause, then resume.

## By runtime environment

- In environments that can run code, apply every rule in this module.
- In environments that cannot run code, apply only the partial file loading, output cutting, and turn cutting rules, and suggest splitting bulk work into parts.

## Items never cut

Do not skip the items below for the sake of saving tokens.

- Sources and calculation bases of quantitative data
- Checks that confirm the output was made correctly
- The content and length of the output body the user requested
- Reports of the cause of and response to errors
- Confirmation steps for sensitive matters such as legal or safety issues
- Stage plans and check records when staged-work is also loaded

## Pre-output check

- Does the text loaded into context pass the input question?
- Does the text in the response pass the output question?
- Is there no reprint of a whole file body or source text?
- Does a revision response contain only the changes?
- Are confirmation questions bundled into one turn?
- Were no never-cut items skipped?

## Exceptions

- If the user explicitly asks for full output, full loading, or detailed process description, do not apply the corresponding rule.
- If quoted source text must be reproduced exactly, that part is exempt from the no-restatement rule.
- If the user asks for full logs for debugging, do not apply the tool output limit.
