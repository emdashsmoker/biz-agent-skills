# In-house hyperscale AI pilot consulting: project overview and WBS

## 1. Project overview

| Item | Details |
|---|---|
| Project | In-house hyperscale AI pilot consulting |
| Purpose | ① Prepare a plan to pilot an in-house hyperscale AI on the quality and design teams' past document search and report drafting<br>② Give executives the basis to decide on a pilot in the first half of 2027 |
| Contract period | Mon 2026-11-02 - Fri 2027-01-29, 13 weeks. 63 working days (excluding Christmas 12/25 and New Year's Day 1/1) |
| Target | Quality team, design team / past document search, report drafting |
| Scope | 1. **Current-state diagnosis**: survey document work processes and time spent (10+ staff interviews, 2 weeks of work time measurement)<br>2. **Target task selection**: select 2 pilot tasks, define impact indicators<br>3. **Model comparison test**: compare 3+ open-weight models on samples of company documents<br>4. **Pilot operation design**: in-house server design, security check criteria, operations staffing and cost estimate<br>5. **Reporting**: pilot recommendation, executive briefing |
| Reports and meetings | Kickoff Fri 11/6, interim Fri 12/18, final Fri 1/22<br>1 security team advisory meeting (before the model comparison test). Planned **for Fri 11/27**, to be agreed |
| Deliverables | Kickoff report, interim report, final report (with pilot recommendation), model comparison test report |
| Staff | 1 principal researcher (50%), 1 senior researcher (100%), 1 researcher (100%) |
| Effort | 157.5 person-days available (principal 31.5, senior 63, researcher 63). 151 person-days assigned in the WBS, 6.5 person-days kept in reserve |

---

## 2. Phases and key dates

| Phase | Period | Result at the end of the phase |
|---|---|---|
| 1. Project management | 11/2 - 1/29 | Kickoff and interim reports, weekly progress management |
| 2. Current-state diagnosis | 11/6 - 12/4 | Document work processes of both teams and baseline time by task |
| 3. Target task selection | 11/26 - 12/11 | 2 pilot tasks, impact indicators by task |
| 4. Model comparison test | 11/10 - 1/20 | Comparison of 3+ models, recommended model |
| 5. Pilot operation design | 12/21 - 1/13 | Server design, security check criteria, operations structure, cost, pilot plan |
| 6. Reporting and close | 1/4 - 1/29 | Pilot recommendation, final report, executive briefing, delivery |

**Key milestones**

| Date | Milestone | Note |
|---|---|---|
| Fri 11/6 | ◆ Kickoff meeting | Confirm interviewees, measurement staff and the security advisory date here |
| Mon 11/16 | Work time measurement starts | 2 weeks to 11/27 |
| Fri 11/27 | ◆ Security team advisory meeting | Held before the model comparison test (statement of work condition) |
| Fri 12/4 | ◆ 2 pilot tasks confirmed | Starting point for the evaluation dataset and document samples |
| Fri 12/18 | ◆ Interim report meeting | Current-state diagnosis, target tasks and indicators, test plan and progress |
| Thu 12/24 | Blind staff evaluation closes | Closes before the year-end holidays |
| Fri 1/22 | ◆ Final report meeting | Recommendation, executive briefing, model comparison test report |
| Fri 1/29 | Delivery, contract ends | |

---

## 3. WBS

Lead: principal = principal researcher, senior = senior researcher. All dates fall between November 2026 and January 2027.

| WBS | Task | Period | Lead | Output |
|---|---|---|---|---|
| **1** | **Project management** | **11/2 - 1/29** | | |
| 1.1 | Project execution plan | 11/2 - 11/3 | Principal | Execution plan (in the kickoff report) |
| 1.2 | Data request and working group setup | 11/2 - 11/5 | Senior | Data request list |
| 1.3 | Kickoff report | 11/4 - 11/5 | Senior | Kickoff report |
| 1.4 | ◆ Kickoff meeting | 11/6 | Principal | Minutes |
| 1.5 | Weekly progress and issue management | 11/9 - 1/29 | Principal | Weekly progress report |
| 1.6 | Interim report | 12/9 - 12/16 | Senior | Interim report |
| 1.7 | ◆ Interim report meeting | 12/18 | Principal | Minutes |
| 1.8 | Reflect interim report feedback | 12/21 - 12/23 | Senior | Interim report (revised) |
| **2** | **Current-state diagnosis** | **11/6 - 12/4** | | |
| 2.1 | Baseline data analysis (work manuals, document storage, report templates) | 11/6 - 11/13 | Senior | Data analysis results |
| 2.2 | Interview design (5+ per team) | 11/6 - 11/11 | Senior | Questionnaire, interviewee list |
| 2.3 | Work time measurement design | 11/6 - 11/12 | Senior | Log form, participant guide |
| 2.4 | Staff interviews (10+) | 11/12 - 11/25 | Senior | Interview notes |
| 2.5 | Work time measurement (2 weeks) | 11/16 - 11/27 | Researcher | Raw measurement data |
| 2.6 | Measurement analysis, baseline | 11/30 - 12/2 | Researcher | Work time analysis |
| 2.7 | Current process mapping, problems | 11/26 - 12/4 | Senior | Current-state findings |
| **3** | **Target task selection** | **11/26 - 12/11** | | |
| 3.1 | Candidate tasks, evaluation criteria | 11/26 - 11/27 | Principal | Candidate list, criteria |
| 3.2 | Evaluate candidates, select 2 pilot tasks | 11/30 - 12/3 | Principal | Target task proposal |
| 3.3 | ◆ Target tasks confirmed | 12/4 | Principal | Agreed result |
| 3.4 | Impact indicator definition (indicator, baseline, target, method) | 12/7 - 12/11 | Principal | Impact indicator definitions |
| **4** | **Model comparison test** | **11/10 - 1/20** | | |
| 4.1 | Candidate model survey (Korean performance, license, GPU needs) | 11/10 - 11/17 | Researcher | Candidate model survey |
| 4.2 | Test plan (select 3+ models) | 11/18 - 11/24 | Senior | Model comparison test plan |
| 4.3 | Security advisory materials | 11/25 - 11/26 | Senior | Advisory materials |
| 4.4 | ◆ Security team advisory meeting | 11/27 | Principal | Advisory results |
| 4.5 | Reflect advice, approve test start | 11/30 - 12/2 | Senior | Test plan (revised) |
| 4.6 | Test environment build (in-house GPU server, document search setup) | 12/3 - 12/11 | Researcher | Environment setup record |
| 4.7 | Document samples, de-identification | 12/7 - 12/11 | Researcher | Test document samples |
| 4.8 | Evaluation dataset | 12/7 - 12/11 | Senior | Evaluation dataset |
| 4.9 | Run tests (automatic scoring, speed and resource measurement) | 12/14 - 12/18 | Researcher | Raw test data |
| 4.10 | Blind staff evaluation | 12/21 - 12/24 | Senior | Staff evaluation results |
| 4.11 | Test result analysis | 12/28 - 1/7 | Researcher | Test analysis |
| 4.12 | Model comparison test report (draft 1/15) | 1/8 - 1/20 | Researcher | **Model comparison test report** |
| **5** | **Pilot operation design** | **12/21 - 1/13** | | |
| 5.1 | Security check criteria | 12/21 - 12/31 | Senior | Security check criteria |
| 5.2 | In-house server design | 12/28 - 1/8 | Researcher | In-house server design |
| 5.3 | Operations staffing and structure | 1/4 - 1/8 | Senior | Operations structure |
| 5.4 | Cost estimate (build, operations) | 1/11 - 1/13 | Senior | Cost estimate |
| 5.5 | Pilot operation plan | 1/11 - 1/13 | Principal | Pilot operation plan |
| **6** | **Reporting and close** | **1/4 - 1/29** | | |
| 6.1 | Pilot recommendation | 1/14 - 1/18 | Principal | Pilot recommendation |
| 6.2 | Final report | 1/4 - 1/20 | Senior | **Final report** |
| 6.3 | Executive briefing | 1/19 - 1/21 | Principal | Executive briefing |
| 6.4 | ◆ Final report meeting | 1/22 | Principal | Minutes |
| 6.5 | Reflect final feedback, complete outputs | 1/25 - 1/27 | Senior | Final outputs |
| 6.6 | Final delivery and acceptance | 1/28 - 1/29 | Principal | All deliverables |

Main content, predecessors, effort by role and client support for each task are in the WBS sheet of the Excel file.

---

## 4. Effort allocation (person-days)

| Phase | Principal researcher | Senior researcher | Researcher | Total |
|---|---:|---:|---:|---:|
| 1. Project management | 8.0 | 9.0 | 5.5 | 22.5 |
| 2. Current-state diagnosis | 2.5 | 11.5 | 8.5 | 22.5 |
| 3. Target task selection | 4.0 | 4.0 | 1.5 | 9.5 |
| 4. Model comparison test | 5.5 | 15.5 | 29.0 | 50.0 |
| 5. Pilot operation design | 4.5 | 9.0 | 4.5 | 18.0 |
| 6. Reporting and close | 7.0 | 11.5 | 10.0 | 28.5 |
| **WBS plan** | **31.5** | **60.5** | **59.0** | **151.0** |
| Available (63 working days × participation) | 31.5 | 63.0 | 63.0 | 157.5 |
| Reserve | 0.0 | 2.5 | 4.0 | 6.5 |

- The senior researcher and researcher are allocated so that no week exceeds their weekly availability (5 days, 4 days in the two year-end weeks).
- The principal researcher's 50% is treated as an average over the period. They put in about 3 days a week during target task selection (W5-W6) and close to 4 days a week in the two weeks before the final report (W11-W12), and cut back by the same amount right after kickoff (W2) and in the interim report week (W7).
- The 6.5 person-day reserve covers year-end leave, security approval delays and acceptance fixes.

---

## 5. Scheduling considerations

1. **The critical path runs through the security team advisory meeting.** It goes advisory meeting (11/27) → test approval → environment build and document samples → test runs (12/14-18) → result analysis → server design and cost → recommendation → final report, with almost no slack. If the advisory meeting slips a week, the test runs fall into the year-end holidays, so the advisory date should be fixed at the kickoff meeting.
2. **Work time measurement starts Monday 11/16.** The log form and participant briefing must be done in the week after kickoff (11/6) for the 2-week measurement to end by 11/27 and the target tasks to be confirmed on 12/4. The participant list is needed by 11/10.
3. **The interim report (12/18) overlaps with the test run week.** The interim report covers the current-state diagnosis, the 2 target tasks, impact indicators and the test plan and progress, and the model comparison results go into the final report.
4. **The two year-end weeks (12/21-1/1) have 4 working days each.** Blind evaluation involving staff ends by 12/24, and after that the plan places analysis and design work the project team can do without staff.
5. **There are only 5 working days from the final report (1/22) to delivery (1/29).** To avoid major revisions after the final report, it is best to agree the format and audience of the executive briefing early in January.

---

## 6. Items to confirm

The items below cannot be settled from the statement of work and contract details alone, so the plan rests on assumptions. Please confirm them with the client before the kickoff meeting.

1. **Who provides the GPU server for the model comparison test?** I assumed the client provides an in-house server available from 12/3. Its spec (GPU type, memory, count) sets which model sizes can be tested, and if equipment must be brought in or rented, the schedule needs redoing.
2. **Can the security team advisory meeting be held on Friday 11/27?**
3. **How far can past documents be used for testing, by security grade?** The plan assumes documents never leave the company network.
4. **When is the model comparison test report due?** The statement of work gives no date, so I assumed it is reported with the final report and the final version is delivered on 1/29.
5. **When is the budget for a pilot in the first half of 2027 set?** If a budget request is needed before the final report on 1/22, the schedule should change so that a rough cost range is presented at the interim report (12/18).
6. **Makeup of the 2 pilot tasks.** The default splits them into one "past document search" task and one "report drafting" task. Let me know if the client wants a different makeup.
