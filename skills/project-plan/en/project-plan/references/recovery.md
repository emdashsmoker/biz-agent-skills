# Responding to schedule delays

Most plans people make are shorter than reality. The buffer row absorbs that gap, and this document covers what to do when a delay grows beyond the buffer. Follow the order below, but present only the options that fit the user's situation, and keep them short.

## 1. Assess the situation

- Update plan.json to the current state and run `plan.py check` to get the remaining buffer days, progress and buffer used
- Assign each late row one of the causes below
- (Team cause) Work took longer than estimated, someone left, rework
- (External cause) Late client review, late data replies, missing survey responses, force majeure
- (Scope growth) Requests that are not in the RFP
- List the deliverables the contract requires and their acceptance criteria, then separate the work that can shrink from the work that cannot
- Record the date and reason of every external delay in writing on the day it happens. The record supports any later request for more time

## 2. Options

| Option | What changes | How | Works best when | Cost |
|---|---|---|---|---|
| Resequencing | Task order | Overlap loosely dependent tasks | The next task can start with part of the previous result | Changes upstream cause rework. Set dates to share interim results during the overlap |
| Adding people | Staffing | Add people to deadline critical rows | Someone already knows the project and the work splits easily | New people need time to learn and coordinate first. The later they join, the smaller the gain. Long hours do not raise output in proportion to time, so keep them short |
| Scope and depth | Amount and depth of deliverables | Finish the required deliverables first and cut extra analysis. Switch methods (survey to secondary data) or move parts to a follow-up project | There is a lot of analysis beyond the required deliverables | Needs client agreement. Put the agreement in writing |
| More time | Deadline | Request a contract extension or a scope change | The delay has an external cause or comes from scope growth | Whether and how depends on the contract terms |

Order of review by cause

- (Team cause) Look at resequencing, then adding people, then scope and depth
- (External cause) Request more time based on the records, and at the same time pull remaining work forward by resequencing
- (Scope growth) Raise the extra requests as a scope change and adjust scope together with time or price

## 3. Contract terms

- General conditions of public service contracts in Korea usually exclude delays caused by things outside the contractor's responsibility (client circumstances, force majeure) from the late days and accept them as grounds for extension. The extension is usually requested in writing without delay before the contract period ends
- Delays with a team cause can trigger liquidated damages. Check the rate and clauses in the contract and its general conditions
- Korean public software projects have a procedure in which a task review committee reviews scope changes and the resulting price and schedule adjustments
- Private contracts follow the change clause and change request procedure in the contract
- Extension grounds in Korean public contracts are narrow, so for team-caused delays look at resequencing and scope first
- The contract notes here describe general procedure only. For a specific contract, confirm with the contract officer or a legal professional

## 4. Talking with the client

- (When) As soon as buffer used exceeds progress. Notice given right before the deadline removes the options
- (What to bring) Remaining work and time, causes and records, two or three options, the schedule, quality and cost effect of each, and a recommendation
- (Record) Keep the outcome in meeting minutes or an official letter

## 5. Replanning

- Put the agreement into plan.json and run `plan.py check` again
- Keep the original value of `baseline_last_end`. If the contract period changes, record the new end date and new baseline, and keep the old values in the notes
- Shorten the review cycle to weekly and check deadline critical rows first
- Keep a buffer row after replanning

## Short explanation

When the user asks, for an interview or a report, "no project runs on schedule, so what do you do when the deadline is about to slip?", answer with this frame.

- Keep the buffer in one place in the plan and compare buffer used with progress every month to catch delays early
- In a crisis, split the causes into team, external and scope growth
- For team causes, look at resequencing, adding people, then scope and depth; for external causes, request more time based on the records
- Either way, bring the options and their effects to the client before the deadline, agree, and put the result in writing
