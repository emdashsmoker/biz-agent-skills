I have built the project overview and the WBS. One schedule problem comes first. There are only 7 days between the final report meeting (1/22) and the contract end date (1/29). After the final report feedback is addressed, only **2 days (2.2% of the whole period)** of schedule buffer remain. The standard is 15%. The best place to negotiate the schedule is the kickoff meeting (11/6), so the options are set out below.

## Plan structure

The 5 scope items in the statement of work became phases, with a project management phase added in front. The phases run project management, current-state diagnosis, target task selection, model comparison test, pilot operation design and reporting. Each of the 4 deliverables has its own row. The security team advisory meeting is split into 3 rows (request, meeting, follow-up), and the meeting is on 11/26, before the model comparison test.

| Checkpoint | Date | Done by this point |
|---|---|---|
| Kickoff meeting | 2026-11-06 | Kickoff report approved, support contacts named |
| Security team advisory meeting | 2026-11-26 | Test plan draft and document handling reviewed |
| Interim report meeting | 2026-12-18 | Current-state findings, 2 target tasks and impact indicators, test plan |
| Final report meeting | 2027-01-22 | Test report, pilot design, pilot recommendation |

Two things were moved earlier to make these dates.

- **Support requests go out before the kickoff meeting.** On 11/3, interviewees, measurement participants, document samples and the test server are requested at once. Only then can the 2-week work time measurement (11/16-11/27) and 10+ interviews finish before the interim report is submitted (12/11).
- **Test design starts before the target tasks are confirmed.** The test is designed around the two task types named in the project purpose (document search and report drafting). Once the interim report meeting confirms the target tasks, only the mix of evaluation items is adjusted.

Rows with uncertain results have separate follow-up rows. These are the extra interviews, follow-up measurement and retest, each 30% of its base row.

## Check results (plan.py check)

- 0 errors, 1 warning.
- The remaining warning is "schedule buffer of 2 days (2.2% of the total) is below the 15% standard." As long as the final report date is fixed, reordering work or adding staff does not solve it. It is therefore left as an item to negotiate with the client.
- The M/M totals check out. Principal researcher 1.5, senior researcher 3.0 and researcher 3.0, for 7.5 M/M in total. The contract documents give no M/M figures, though, so these are assumed values calculated as participation × 3 months.

## Options for securing schedule buffer

| Option | What changes | Schedule buffer | Cost |
|---|---|---|---|
| A. Extend the contract end by 2 weeks to 2/12 and keep the final report meeting on 1/22 | Contract end date | 16 days (15.5%), meets the standard | Requires a contract change. Agreement should also allow moving the final report meeting within the extension, so delays in earlier phases can be absorbed too |
| B. Move the final report meeting 1 week earlier to 1/15 and keep the end date | Report schedule | 9 days (10.1%), below the standard | Test analysis and recommendation writing lose a week and overlap with staff evaluation over the year-end holidays |
| C. Keep the current schedule | Nothing | 2 days (2.2%) | Any delay in the test server or document samples pushes back the final report submission (1/14) by the same amount |

**I recommend A.** It is the only option that meets the standard while leaving the work plan as it is. It also barely affects when the client decides on a pilot in the first half of 2027. If an extension is hard to get, propose B with the condition that the final report meeting can move back to 1/22 if delays occur. Either way, record the outcome in the meeting minutes. The buffer days in all three cases were calculated with plan.py.

## Risks tied directly to the deadline

- **Securing the test server:** Assumed to take 4 weeks (11/9-12/4). Every task after testing waits on this server. Confirm the schedule at the 11/20 weekly check, and if it is uncertain, agree to scale the test models down to what one GPU can run.
- **Transferring document samples:** Samples can be moved only once the security team's advisory conditions are met. If the conditions tighten, agree to narrow the sample scope.
- **Year-end holidays:** Staff evaluation of the report drafts (12/28-1/6) overlaps with Christmas and New Year's Day. Raters and evaluation dates need to be fixed in early December.

## Items to confirm

The items below are assumed values for now and are marked `[to confirm]` in the plan. Let me know and I will update plan.json and export again.

1. Client name, contract type and amount, M/M per person in the contract documents
2. Whether the senior researcher and researcher work on other projects at the same time (now assumed not, at 100% participation)
3. Whether the company has in-house GPU servers, the allocation procedure and the IT infrastructure department
4. Delivery format of the executive briefing: it is in scope item 5 but not in the deliverables list, so it needs confirming whether it is a separate deliverable or an appendix to the final report
5. Document sample size, number of evaluation items, pass criteria for practical use, impact indicator targets
6. Security team availability for the advisory meeting, and the client's review periods for the interim and final reports (now assumed to be 4 days and 1 week)
