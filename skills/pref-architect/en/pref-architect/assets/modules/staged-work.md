---
name: staged-work
description: "Procedure for large tasks that span several steps, files, sources, or sessions: plan the stages, check each stage, and review before delivery. Load it before starting work when the always-on instructions say to load this module or when the user asks for \"/staged-work\", \"be thorough\", \"be systematic\", \"verify step by step\", and similar. Do not use it for simple requests that finish in one pass."
metadata:
  generator: pref-architect
  generator-version: "1.0"
---

# staged-work

A procedure that keeps a wrong early assumption from surfacing only at the end of a large task. It sets how the work is done and does not raise the model's reasoning ability itself. If a task is beyond that ability, tell the user about the limit instead of producing a plausible-looking result.

## When not to use it

For work with one clear approach that finishes in one pass, skip this procedure and do the work directly. Staging a simple task buries the answer under process. Use this procedure only for work where a single pass could plausibly miss something.

## 1. Stage plan

Before starting, write out all the stages. Give each stage a number and an expected output.

```
Stage 1 [name], expected output [content]
Stage 2 [name], expected output [content]
```

- Each stage produces one output that can be checked. Merge a stage with no checkable output into the next stage.
- If something learned during the work makes the plan wrong, revise the plan. The plan can change during the work.

## 2. Check each stage

Set a check condition that can fail for each stage. Judge the check with an external output.

- A test runs and passes.
- A file or output actually exists in the expected form.
- A source was actually opened and read.
- The output was compared against the requested specification.

"I reviewed it and it looks right" is not a check condition. A model inclined to skip checks will also pass its own judgment easily. If a stage has no check condition that can fail, write that down and mark its output as unchecked, so the gap stays visible in later stages.

If a fix in a later stage invalidates an earlier stage's output, rerun the earlier stage's check before continuing. The earlier an error is caught, the cheaper it is to fix.

Examples of check conditions by type of work are below.

| Type of work | How to proceed | Check condition |
|---|---|---|
| Software development | Read the relevant code first, and write tests together with the implementation. Plan large changes before making them | Tests run, and error paths are exercised too |
| Research and knowledge work | Collect sources before synthesizing. For each claim, weigh the evidence and what would disprove it. Separate confirmed facts from inferences and mark inferences | Every claim supporting the conclusion traces to a source actually read |
| Data analysis | Understand the shape of the data first. Write the hypothesis before computing. Look at missing values, duplicates, and outliers first | Data quality check code passes on the actual data |
| Work across several sessions | Keep a work log of decisions, reasons, and failed attempts. Read the log first when resuming. Set completion criteria first | The completion criteria are written down and can be checked |

## 3. Self-review before delivery

Before delivering the result, reread it with the eyes of a skeptical reviewer. If you find a real weakness, fix it or tell the user. If a proper check finds no weakness, say so. Do not invent weaknesses to fill the procedure.

Before reporting a problem, confirm that it actually exists, by searching, comparing, running, or checking against the source. Do not raise a warning just because you could not find evidence. An unconfirmed warning creates a problem that does not exist and costs the user time.

## Operating rules

- (Accumulated warnings) Count small concerns that come up during the work and are not worth stopping for. When three accumulate, stop and tell the user about all of them at once before continuing. Small concerns that point the same way often signal one larger problem.
- (Safe bulk replacement) When bulk-replacing strings in files, set word boundaries. Without boundaries, parts of other words change too. After replacing, search to confirm that no words got glued together or broken.
- (With token saving) Even if token-lean is also loaded, do not shorten the stage plan or check records. The user needs these records to follow the work.
