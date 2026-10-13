# Writing the Proposal Strategy

> Translated from the Korean original. It may behave differently from the original's intent.

Rules and templates for writing 02_proposal_strategy.md and 03_project_charter.md. Read from step 3 of strategy mode. 01_rfp_analysis.md must be complete.

## Order of writing

Write the strategy document in the order below. Each later section is derived from the results of earlier ones. When an earlier section changes, revise the later sections that use it.

| Order | Section | Main inputs | Reference |
|---|---|---|---|
| 1 | Bid decision | Eligibility in 01_rfp_analysis.md, bidder information | This document |
| 2 | Client needs | Reading the RFP in 01_rfp_analysis.md, public sources | This document |
| 3 | External conditions | Public sources | This document |
| 4 | Competitive structure | Eligibility, public sources, bidder information | references/competition.md |
| 5 | Bidder capability | Bidder information, track record list | This document |
| 6 | Proposal strategy | Sections 2-5 | This document |
| 7 | Work structure | Project type, requirements, section 6 | references/modules.md |
| 8 | Storyline | Sections 2, 6, 7, evaluation criteria | This document |
| 9 | Execution decisions | Sections 1-8, price scoring formula | This document |

## 1 Bid decision

| Requirement | RFP requirement | Bidder has | Met |
|---|---|---|---|
| Eligibility | | | |
| Track record | | | |
| Staff | | | |
| Certification | | | |
| Delivery capacity | Project period, budget, number of requirements | Available staff and time | |

- Fill the Met column with met, not met, or [CONFIRM].
- If any requirement is not met, set the proposed decision to "hold" and give the reason and the remedy (forming a consortium, adding staff, joint bidding with an organization that has the track record).
- Compute delivery capacity in code only when the user gives an average monthly labor rate. Available person-months equal the labor portion of the budget divided by the average monthly labor rate. The labor portion is the budget multiplied by the labor share the user sets. If the share is unknown, mark it [CONFIRM]. Compare the result with the person-months required by the RFP's mandatory team composition over the project period.
- Write the proposed decision as one of bid, hold, or no bid, with the reason and the conditions for lifting a hold. The user makes the final decision.

## 2 Client needs

Take the stated need from "Reading the RFP" in 01_rfp_analysis.md. Build underlying-need hypotheses by answering three questions.

- Why is the client commissioning this now? Typical reasons are the revision cycle of a higher-level plan, an audit finding, the first year of a new program, reorganization, budget review, or a weak result from the previous contractor.
- Whom does the client's department need to persuade with the deliverables? Typical audiences are the budget ministry, a supervising agency, the legislature, or an internal decision body.
- What does the client see as the cause of the conditions the RFP background describes negatively?

Test each hypothesis as follows.

- Delete from the hypothesis whatever the RFP already says. New information must remain. If nothing remains, it is a summary of the RFP; rewrite it.
- A hypothesis must say where the client will use the deliverables.
- Attach a public source name and date to each hypothesis. If web search is not allowed, use user-provided material; if there is none, mark [CONFIRM].
- Record the module or task that answers each hypothesis in the response column. Fill this column after section 7.

The client's outcome is the change at the client after the project ends. Examples are passing a supervising agency's review, securing a budget line, launching a program, starting a follow-on project, or reaching agreement among implementing departments. Write it as who gets what, by when, in what state. A sentence without a subject and a time, such as "improved execution", fits any project; rewrite it around the client's situation. Submitting a report is not an outcome. Deliverables are the means to reach an outcome.

| Item | Content | Evidence | Response module |
|---|---|---|---|
| Stated need | | RFP location | |
| Underlying-need hypothesis 1 | | Source (year), URL | |
| Client's outcome | | | |

## 3 External conditions

Research the policy calendar, higher-level plans, budget review schedule, and similar programs around the client. Record where in the proposal each finding will be used.

| Category | Content | Evidence | Where used |
|---|---|---|---|
| Opportunity | | | |
| Threat | | | |

## 4 Competitive structure

Write this section with the procedure and template in references/competition.md. The result consists of the eligibility judgment, expected strengths and weaknesses by competitor type, the competitor candidate table, the client's previous contractor, and a note on excluded organizations.

## 5 Bidder capability

| Category | Track record | People | Domain knowledge | Methods |
|---|---|---|---|---|
| Strengths | | | | |
| Weaknesses | | | | |
| Remedies | | | | |

- Judge strengths and weaknesses against this project's requirements and evaluation items. Leave out general capabilities unrelated to the project.
- Choose remedies from consortium, outside advisors, and added staff.

### Similar-project screening

Pick the projects in the user's track record list that are closest to this project. The result supports the strengths column and the track record section of the proposal.

1. Judge whether each project is accepted under the RFP's track record rules (accepted period, amount, project type).
2. Score each project on the five criteria below: match 2 points, partial match 1 point, unrelated 0 points.
3. Sort accepted projects first, then by total score in descending order. Break ties by the most recent end date.
4. Present the top 20 as a table. Do the scoring and sorting in code.

| Criterion | Match (2 points) |
|---|---|
| Theme | Same project type and subject |
| Method | Used the techniques the RFP names or the survey and analysis methods this project will use |
| Keywords | Terms from the key wording dictionary appear in the project name or description |
| Domain | Same target industry or policy area |
| Client | Same organization. Same supervising agency or same type of organization scores 1 point |

| Rank | Project | Client | Period | Amount | Accepted | Theme | Method | Keywords | Domain | Client score | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|

## 6 Proposal strategy

### Differentiators

- Set 1-3 differentiators. Back each with at least one piece of evidence from track record, data, or people. Write evidence as named facts a third party can check, such as project names, dataset names, and people's histories.
- For each competitor strength found in section 4, find bidder evidence that offsets it and turn it into a differentiator.
- For each differentiator, list the capability claims and execution strategies it leads to. One differentiator may support several claims.
- Do not claim strengths in the proposal that are not in this section.

| Differentiator | Evidence | Competitor strength it offsets | Execution strategy it leads to |
|---|---|---|---|

### Deriving execution strategies

An execution strategy starts from why this project is hard. Why the client is doing the project is answered by the project as a whole. Starting from the background problem leads to renaming the module list as strategies. Fill one row of the table below per strategy. This table stays out of the proposal body. The body states only the strategy, the risk it resolves, and the value it creates.

| Column | Definition | Example |
|---|---|---|
| Project characteristic | The scope the project must finish and the nature of what it deals with. Scope content, procedures, compliance duties, and constraints set by the RFP also go here | Unstructured material mostly in HWP and PDF, network-separated security environment, technology areas that differ by field, number of stakeholders, scope relative to duration |
| Risk | Where the deliverables could go wrong because of that characteristic | Poor text extraction from documents, sensitive material that cannot leave the network, tasks disconnected from field needs, a plan shelved after adoption |
| Critical success factor | The condition the deliverables must meet to get past the risk, with a one-line test | For "discovering practical tasks", the test is "selecting tasks that cut real workload" |
| Value secured | The value the client gains when the success factor is met. Paired with the risk it resolves | "Reliability that removes distrust of wrong answers", "safety that prevents sensitive data from leaking" |
| Execution strategy | The tailored approach that secures the success factor. Written as a design principle for the deliverables or as the design of a work activity | Design principles: answers that cite sources, performance analysis with a comparison group. Work activities: subcommittees split by technology characteristics, pre-testing indicators by subcommittee |

| Project characteristic | Risk | Critical success factor (test) | Value secured | Execution strategy |
|---|---|---|---|---|

A critical success factor is one of the few areas that must go right for a goal to be reached (John F. Rockart (1979), Chief Executives Define Their Own Data Needs, Harvard Business Review 57(2)). Here the concept is narrowed to a single project.

An execution strategy must be tailored to this project and different from what competitors offer. Tailoring means a design fitted to the nature of what the project deals with. Differentiation is what the bidder adds above what the RFP and regulations require. Accept a row as an execution strategy only if it passes all four tests below.

- (Duty deletion test) Delete from the strategy sentence any compliance with RFP scope, regulatory duties, or constraints. An approach must remain. "Complying with security rules" or "meeting the schedule" leaves nothing, so neither is a strategy. "Separating processing paths by data classification so generative AI can be used inside the security environment" still has a method after the goal is removed.
- (Module repetition test) If deleting the strategy table leaves the module summary table saying the same thing, the strategy repeats the modules. Rewrite a strategy that stops at an activity name (diagnosis, pilot, running an advisory committee) as the design of that activity (composition criteria, targets, timing).
- (Generic means test) If both the risk and the means fit any project (schedule delay and a monthly meeting), it is not a strategy. Move such rows to the committee design in section 7.
- (Schedule declaration test) A sentence that declares a completion date, such as "finalize X by year N", is the writer's schedule. Put dates in the schedule in section 7 and write the strategy as a design principle and the risk it resolves. Express alignment with the client's calendar as a property of the approach, such as "a pilot timed to the planning calendar".

### Proposal keywords

Pick 3-5 message words the proposal will repeat for the bidder. Draw them from the differentiators and the values the execution strategies secure. The key wording dictionary in 01_rfp_analysis.md is a list for keeping the RFP's terms. The proposal keywords are a list for gathering the bidder's claims. When both lists name the same thing, use the RFP's term.

## 7 Work structure

Produce the following with the procedure in references/modules.md.

- Final project type, as confirmed by the user in the intake questions.
- Module summary table. Columns are Module, Task, Activities, Deliverables, and Requirement IDs. Separate items in the Activities cell with commas.
- Requirement placement check. Compare all requirement IDs in 01_rfp_analysis.md with the requirement IDs in the module summary table in code. The number of unplaced IDs must be 0.
- Committee and consultation design. For each committee, give its name, members, number and timing of meetings, agenda, and where results feed in.
- Schedule. First column Module, second column Task, then one column per month (1M, 2M) or week. Mark periods with ■ and reporting meetings with ●.
- Reporting and review calendar. Timing of the kickoff report, interim report, final report, advisory meetings, and other meetings the RFP sets.
- Project success criteria. Up to three lines on how to judge whether the project succeeded. They must connect to the client's outcome in section 2.

```markdown
| Module | Task | Activities | Deliverables | Requirement IDs |
|---|---|---|---|---|
| Module 1. Current state analysis | Task 1-1. Policy document review | Review of 12 national agenda items and higher-level plans | List of policy requirements | T1, T2 |
```

When a module or task name joins two objects, join them with "and" (for example, "current state analysis and diagnosis").

## 8 Storyline

The storyline fixes the proposal's argument before the manuscript is written. Whoever writes the proposal turns the statements in this section into headings and opening sentences. Design vocabulary such as stage names (S, C, Q, A) and "differentiator" stays in this document. The proposal manuscript uses the project's own language.

### One-line storyline

Write one sentence that runs from the background problem through the execution strategies and modules to the client's outcome. A sentence that ends in deliverables reads as report delivery, so end it with the outcome. The material for the outcome is the underlying-need hypotheses in section 2.

### Background argument

The background answers why the client needs this project now. It does not describe the bidder's capabilities or methods. Use SCQA or SCR as the skeleton. Skipping a stage makes the background read as generic.

| Stage | Definition |
|---|---|
| S Situation | Facts the reader already knows or accepts without dispute |
| C Complication | A change or problem arising in that situation. It raises a question in the reader's mind |
| Q Question | The question the complication raises |
| A Answer | The answer to the question. Leads into the proposal scope and execution strategies |
| R Resolution | The last stage of SCR. Presents the resolution to the complication without a question stage |

Stage definitions follow Barbara Minto (2009), The Pyramid Principle: Logic in Writing and Thinking (3rd ed.), Pearson Education.

- Narrowing from the outside in is recommended: macro environment (policy, technology, society), then conditions in the field or industry, then the client's internal situation. Choose the stages that fit the project and keep the chosen stages in this order.
- Strategic planning, IT planning, and program planning develop S and C over several points. Performance analysis and evaluation, management evaluation support, problem solving, and organization and HR projects compress S and C to 1-2 points each.
- The subject of background statements is the client and its wider environment. Do not make the bidder the subject.

| Order | Stage | Statement | Evidence (source, year) |
|---|---|---|---|

### Execution strategy statements

- Turn each row of the strategy table in section 6 into a sentence.
- Each statement carries a design principle or activity design together with the risk it resolves or the value it secures.
- (Before) "Designing the system with RAG technology". Only a technology name.
- (After) "Removing distrust of wrong generative-AI answers with a retrieval structure that cites a source document for every answer". It has both a design principle (citing sources) and a risk resolved (distrust of wrong answers).
- The message of the execution strategy section combines the values the strategies secure into a phrase that describes the deliverable (for example, "a master plan for X with distinctiveness, benefit, and feasibility").

| Order | Statement | Risk resolved | Value secured | Implementing task |
|---|---|---|---|---|

### Capability statements

- The subject is the bidder. State facts the bidder holds.
- Attach a differentiator and named evidence (projects, people, data) to each statement.

| Order | Statement | Differentiator | Evidence |
|---|---|---|---|

### One line per module and task

Write one line for each module and task. The order is target, action, result of the deliverable or activity, and use. Use is the later step inside the project where the result is used. Record the underlying need or differentiator it answers in the next column.

| Module | Task | One line | Underlying need or differentiator answered |
|---|---|---|---|

### Evaluation item mapping

For each qualitative evaluation item, record the argument and evidence that answer its score. If a high-scoring item has weak evidence, move it to the failure points in section 9.

| Detailed evaluation item | Points | Statement or task that answers it | Evidence (track record, data, tables) |
|---|---|---|---|

### Self-check before presenting

- Do the background statements narrow from the macro environment to the client's internal situation?
- Does every risk in the strategy table have an execution strategy statement that answers it?
- Do the execution strategy statements avoid repeating module names and activities?
- Does every differentiator have a capability statement and an execution strategy statement?
- Does every underlying-need hypothesis have a module or task that answers it?
- Is the value in each strategy row paired with the risk it resolves?
- Does the one-line storyline end with the outcome?
- Are the execution strategy statements free of completion-date declarations?
- Do module and task names match the module summary table?
- Could a competitor write the same statement? Each statement needs evidence only the bidder has (track record, data, people).
- Does each background statement read as why the client needs this, each capability statement as what the bidder has, and each execution strategy statement as how the work is done? Move a statement that reads as another section's role to that section.

### Presenting and confirming

- Present the storyline section and the module summary table in one turn.
- Help the user narrow down what to fix by listing up to three points to confirm (for example, whether the second point of background C is an audit finding or a new program).
- Apply requested changes to this section first. If module or task names, order, or count change, update the module summary table and requirement placement together and rerun the placement check.
- When the user confirms, record the date and scope on the first line of the section (for example, "Confirmed 2026-09-17, full storyline").
- After confirmation, changing the meaning of a statement, or adding, deleting, or reordering statements, needs the user's confirmation again. Wording polish with the same meaning can be applied directly and noted in one line in the completion report.

## 9 Execution decisions

### Staffing

| Role | Candidate | Scoring requirement | Fit |
|---|---|---|---|
| Principal investigator | | | |
| Team members | | | |

- List only staff the user provides.
- Record fit as met, partly met, or not met, with the reason.

### Advisory committee candidates

- Pick candidates who fit the project field from the list the user provides.
- Without a list, give only the field, affiliation type (industry, academia, research institutes, public sector), and number of people.

### Price direction

Give only the bid range (as a ratio of the budget) and the reasoning. The user sets the final amount. Build the reasoning from these items.

- The RFP's price scoring formula and price points
- Price score for each bid ratio range. Compute with the formula in code and present as a table
- Award ratios for the same and similar projects from public award records
- The bidder's cost. Compute only when the user provides staffing and rates

Base the price judgment only on the bidder's own data and public information.

### Win points and loss points

- Up to five of each.
- Draw win points from high-scoring items where the bidder's evidence is strong.
- Draw loss points from high-scoring items where the bidder's evidence is weak, from risks of breaching eligibility or writing rules, and from items where competitors lead.
- Attach the related evaluation item or competitor type to each point. Attach a countermeasure to each loss point.

### Delivery risks

Record risks that could arise while delivering the project after winning. Typical risks are changes in project scope, delays in client data, and external changes (regulatory revisions, budget adjustments). Attach warning signs and countermeasures to each.

| Risk | Warning sign | Countermeasure |
|---|---|---|

## Project charter

03_project_charter.md gathers the confirmed content of 02_proposal_strategy.md into one document. Make it usable as is for a kickoff meeting or an internal briefing. Do not add claims that are not in the strategy document.

| Charter item | Taken from |
|---|---|
| Overview | Project overview in 01_rfp_analysis.md |
| Beneficiaries and needs | Section 2 |
| Project goals | Client's outcome in section 2, deliverables in section 7 |
| Schedule | Schedule in section 7 |
| Hypotheses and responses | Underlying-need hypotheses and response modules in section 2 |
| Success criteria | Project success criteria in section 7 |
| Reporting and review calendar | Reporting and review calendar in section 7 |
| Risks to manage | Delivery risks in section 9 |

```markdown
# Overview
- Project name
- Project period

# Beneficiaries and needs
- (Beneficiaries) Organizations and groups that change as a result of the project
- (Needs and problems) Stated need and underlying-need hypotheses

# Project goals
- (Goal 1) The plan, strategy, or measure the client holds at the end of the project

# Schedule
## Module 1. Module name (January-March)
- Main tasks and deliverables

# Hypotheses and responses
## Hypothesis 1: hypothesis sentence
- Responding modules and tasks

# Success criteria
- Up to three lines

# Reporting and review calendar
- Timing of the kickoff, interim, and final reports, advisory meetings, and other meetings

# Risks to manage
- Risk, warning sign, countermeasure
```

A project goal is the result the project sets out to achieve. The usual goal is a plan, strategy, or measure the client holds at the end of the project. The project purpose is the higher-level state the client aims to reach through that result; record it separately from the goals.
