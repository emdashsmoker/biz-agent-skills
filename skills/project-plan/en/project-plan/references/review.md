# Reviewing an existing WBS

The order to follow when reviewing a WBS or schedule the user already made. Items 1-4 make the schedule itself wrong, so if any of them applies, report and fix it before looking at the rest. From item 5 on, the defects concern completeness.

For each finding, write the location (row number or task name), the defect and the fix in one line each. If the table can be moved into plan.json, add the `plan.py check` result.

## 1. No buffer and no deadline check

- (Symptom) The last task ends on the contract end date, or the table has no buffer
- (Fix) Add a buffer row and compute its share of the total period. The target is in the schedule buffer section of SKILL.md
- (Test) If the buffer calculation ignores wait time and allocations, the buffer looks larger than it is

## 2. No project management stage

- (Symptom) The first rows jump into analysis or design, with no kickoff, progress tracking or closing
- (Fix) Put kickoff preparation, kickoff meeting, progress and risk management, interim report, final report and closing as the first stage
- (Test) Without this stage, reporting and acceptance time drops out and the plan looks shorter than reality

## 3. Waits mixed into work

- (Symptom) Our work and the client's time sit in one row, as in "reflect client review, 2 weeks"
- (Fix) Split into submission (work), review wait (wait) and revision (work)
- (Test) If a row contains time for which "is it our team's fault if this runs late?" gets a no, split it

## 4. Wrong survey and FGI order

- (Symptom) Survey and FGI run in parallel, or the FGI comes before the survey
- (Fix) Reorder to survey, basic survey analysis, FGI topics, FGI, qualitative analysis. An exploratory FGI for writing survey questions stays as a separate row with a different name
- (Test) If the FGI topics were set without survey results, the order is wrong

## 5. Data collection in one row

- (Symptom) A single row such as "data collection, 4 weeks"
- (Fix) Split into collection plan, data request, reply wait, cleaning and final dataset
- (Test) If one row holds both the request and the receipt, split it

## 6. Advisory meetings and hearings placed too late

- (Symptom) Advisory meetings bunch up at the end, or the public hearing sits right before the final report
- (Fix) Split advisory meetings into request, meeting and reflection rows. Keep them at least 4 weeks apart and the last one at least 4 weeks before the final report. Hold the public hearing at least 6 weeks before the final report
- (Test) If the last event is less than 4 weeks before the final report, there is no time to reflect the input

## 7. Contract deliverables missing

- (Symptom) Slides, summary report, database or raw data named in the contract are missing or buried inside the final report row
- (Fix) Give each contract deliverable its own row, running in parallel with the final report row. Allow 1-2 weeks for cleaning raw data and statistical tables
- (Test) Compare the contract deliverable list with the table one to one. Any blank is a missing deliverable

## 8. Report writing only at the end

- (Symptom) Earlier stages have no write-up rows and a long "write report" row sits at the end
- (Fix) End each stage with a row that fixes its output in writing and shrink the last row to editing and combining
- (Test) If the last report row exceeds 15% of the total period, stage write-up rows are missing

## 9. No review cycle

- (Symptom) Deliverables have writing rows only, with no review or revision rows
- (Fix) For each major report, use draft, internal review, submission, client review wait and revision
- (Test) If the interim and final reports lack review cycles, the schedule is short by that much

## 10. Numbers without a source

- (Symptom) Sample sizes, meeting counts or durations that appear in neither the RFP nor the proposal
- (Fix) Ask the user for the source, and if it cannot be confirmed, replace the value with `[To confirm: item]`. If the schedule was computed from an assumption, note it and recompute once the value is fixed
- (Test) Any number not in the documents needs a source or a one-line reason

## 11. Duplicate work or totals that do not add up

- (Symptom) The same deliverable name appears in two rows, or a stage's length does not match its rows. This often happens when two templates are merged
- (Fix) Follow the mixed projects section of `references/skeletons.md`, decide between replacing and inserting, and merge the duplicate rows
- (Test) Every RFP task item maps to at least one row and no work appears twice
