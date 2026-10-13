# Stage templates by project type

Project types are split by one criterion: the nature of the final deliverable. Pick the type, start from its template and add or remove rows to match the task items in the RFP. The RFP always takes priority over the template.

| Type | Final deliverable | Examples |
|---|---|---|
| Plan | A document with directions and actions | Master plan, mid to long-term strategy, roadmap, information strategy plan (ISP), business planning, R&D program planning, commercialization strategy, policy improvement plan |
| Research | Verified facts and analysis results | Status survey, trend study, demand survey, performance analysis, evaluation |
| Build | A working result | Information system, prototype, experiment and test results, database, content |
| Operate | A record of services delivered | Running training courses, running events, operating a support program |

A project that plans R&D the client will carry out later is a Plan project. Experiments and tests become work rows only in Build projects where our team runs them.

## Stages shared by all types

- (First stage, project management) Kickoff preparation, kickoff meeting, progress and risk management, interim report meeting, final report meeting, closing
- (Last stage, deliverables) Editing and combining the final report, summary report, supplementary deliverables named in the contract, handover of raw data and statistical tables
- (Schedule buffer) The buffer row between the last task and the contract end date
- Raw data handover takes 1-2 weeks of cleanup, so it gets its own row. Leaving it to the end delays delivery

## Plan

The base template runs situation analysis, direction setting, action planning, performance management and stakeholder input, in that order. Choosing actions before the diagnosis leaves no answer to "why this action?" at review.

| Stage | Typical rows | Typical outputs |
|---|---|---|
| Situation analysis | Review of the previous plan's results, external environment analysis, internal capability assessment, benchmarking, SWOT and implications | Previous plan comparison table, environment analysis, assessment results, SWOT table |
| Direction setting | Vision and goal structure, strategic directions by area, links among goals, strategies and expected results | Vision and goal chart, strategic direction table |
| Action planning | Strategic actions and priorities, merging overlapping actions, action definition sheets, a specialization strategy if needed | Strategic action list, priority table, action definition sheets |
| Performance management | Indicator design, indicator management cards, feedback procedure | Indicator table, management cards, feedback procedure |
| Stakeholder input | Survey, in-depth interviews or FGI, advisory meetings, public hearing, review and approval | Result reports, advisory input table, approved plan |

Dependencies

- Start SWOT after every other situation analysis row is done. SWOT combines the earlier analyses
- Design indicators after the action list exists. Indicators attach to actions
- Start stakeholder input after a draft direction exists. Input needs something to react to
- Strategic directions and the link to expected results can start at the same time
- Action definition sheets grow with the number of actions and items, so they are usually deadline critical. Split them into three rows: fixing the template, first draft, review and revision
- If a committee must approve the plan, check how often the committee meets and add that as a wait row

Completion criteria examples

| Output | Done when |
|---|---|
| Previous plan comparison table | Every previous plan is broken down to action level and no carry-over decision (strengthen, keep, adjust, close, new) is blank |
| SWOT table | At least 3 entries per factor, and factor combinations link one to one with direction candidates |
| Vision and goal chart | Every goal has a quantitative target |
| Action definition sheets | Every action has budget, funding source, yearly investment and indicator |
| Indicator table | Overall, per-direction and per-action indicators exist and overlaps between indicators are resolved |
| Committee review | Approved at least with conditions, and a plan for the conditions is written |

The action definition sheet is the key output of this type. After approval, the client uses it directly as the basis for budget requests and funding applications.

What to cut first in a small project

- Cut benchmarking, the public hearing and the number of items in action definition sheets (from four down to budget and indicator)
- Keep SWOT, because it feeds direction setting

### R&D program planning

Add technology trends, patent and paper analysis, and an overlap check against similar programs to situation analysis, and add these rows to action planning.

| Row | Typical output |
|---|---|
| Core technology selection | Core technology list, technology tree |
| Technology readiness assessment and target | TRL table (current level, target level, reasoning) |
| Performance targets | Performance indicator sheet (indicator, current level, target, measurement method) |
| Technology sourcing decision | Decision table for in-house development, acquisition or partnership |
| Sub-projects and yearly plan | Sub-project table, yearly roadmap |
| Budget estimate | Budget breakdown with unit cost basis per cost item |
| Governance design | Governance chart, roles table |
| Results and use plan | Indicator table, use and dissemination plan |
| Feasibility analysis | Economic and policy feasibility judgment |

- Put economic analysis after the budget estimate. The program cost is an input to the economic analysis
- Hold one advisory meeting right after the readiness assessment. Experts often disagree on the current level
- Patent and paper analysis often depends on access to paid databases. Note "depends on one person" and set public databases and a smaller sample as the fallback
- A performance indicator sheet without measurement methods turns later program calls into targets nobody can verify
- Patent analysis is done when the search query, database, search period, count and screening rule are documented. The similar program table is done when every program is marked as overlapping, complementary or new

### Commercialization strategy

Technology commercialization, new business planning and investment preparation follow the order below. Looking at the market before knowing the technology leads to designing for a market the technology cannot reach.

| Stage | Typical rows |
|---|---|
| Technology and IP diagnosis | Technology inventory, IP status, technology maturity, competing technology comparison, freedom-to-operate review |
| Market and business case | Market size estimate, customer and demand analysis, competitor and substitute analysis, profitability analysis |
| Commercialization path | Business model, market entry strategy, permits and regulatory response, partners and supply chain, IP strategy |
| Execution and funding | Phased roadmap, funding needs, investment and support program links, organization and hiring plan |

- Finish the freedom-to-operate review before the IP strategy. Label the result as a review finding
- Permit lead time sets the market entry date, so start the permit review together with or before the entry strategy. Use the regulator's published processing time, and if there is none, write `[To confirm]`
- Keep profitability ("does it make money when sold?") and funding needs ("how much does it take to start?") as separate rows. Profitability assumptions feed the funding plan
- Customer validation can change the business model, so add a business model revision row after validation. Recruiting customer companies is a wait row
- Investment and support program links follow call and review calendars, so they are wait rows
- IP diagnosis depends on patent databases or patent attorney review. Note "depends on one person" with a fallback (public databases, narrower scope)
- The market size estimate has three levels (total, serviceable, obtainable market) with the basis for each
- Even in a small project, keep the freedom-to-operate review, reduced to about one key claim

## Research

The base template runs research design, data collection, analysis, and interpretation with recommendations, in that order. Collection that starts before the design produces data that does not fit the analysis frame.

| Stage | Typical rows | Typical outputs |
|---|---|---|
| Research design | Research frame, population and sample design, instrument development, pilot test, approvals | Research design, sample design, questionnaire and interview guide |
| Data collection | Secondary data plan, data request, reply wait, cleaning, survey, in-depth interviews or FGI, field work | Source list, cleaned data, raw survey data, interview summaries |
| Analysis | Descriptive statistics, cross and in-depth analysis, qualitative analysis, integration | Statistical tables, analysis results, theme tables |
| Interpretation and recommendations | Implications, recommendations, use plan | Evidence-to-recommendation table, use plan |

Dependencies

- Order: survey, basic survey analysis, FGI topics, FGI. The FGI asks why the survey results came out as they did, so it needs the survey results first
- An exploratory FGI that helps write survey questions goes before the survey as a separate row with a different name
- Research that needs ethics review or statistics approval starts after approval. Data collected before approval cannot be used
- Qualitative analysis starts right after the interviews and merges with the quantitative analysis at integration. Keep the integration row only when both kinds of data exist
- Performance analysis and evaluation projects add an evaluation frame (indicators, comparison baseline, data sources) to research design
- Plan one round of question revision after the pilot as its own row
- If cross and in-depth analysis depends on a statistician, note "depends on one person" and name a backup

Completion criteria examples

| Output | Done when |
|---|---|
| Research design | Research subjects, unit of analysis and comparison baseline are stated, client approved |
| Sample design | Population size, target sample, sampling method and margin of error are stated |
| Questionnaire | Every research item is covered by questions, and the question-to-analysis table has no blanks |
| Pilot test | Response time and misunderstood questions are checked, revised version fixed |
| Cleaned data | Rules for missing values and outliers are documented and counts match the raw data |
| Raw survey data | Valid responses reach 80% of the target sample |
| Interview results | Planned count completed, transcripts summarized, consent forms collected |
| Recommendations | Every item links one to one with an analysis result, client reviewed |

The evidence-to-recommendation table is the key output of this type. When recommendations do not connect to the analysis, most review comments land there.

What to cut first in a small project

- Cut the pilot size (replace with expert review) and the analysis scope (descriptive statistics and the main cross tabs)
- Keep the approvals, because the agency's calendar does not adjust to ours

## Build

The base template runs preliminary research and design, implementation, testing and verification, deployment, and wrap-up, in that order.

| Stage | Typical rows | Typical outputs |
|---|---|---|
| Preliminary research and design | Prior technology review, requirements definition, detailed design | Review report, requirements specification, design document |
| Implementation | Securing equipment, materials and environments, module development, integration | Purchase records, module outputs, integrated build |
| Testing and verification | Test plan, internal testing, accredited testing or user acceptance, judgment against targets | Test plan, test report, certificate, achievement table |
| Deployment | Pilot or trial environment, pilot run, improvements | Pilot report, improvement record |
| Wrap-up | IP filing, dissemination, operations handover and user training | Filing list, handover documents |

Dependencies

- Development starts after equipment, materials and environments are in place. Split procurement into request, wait and delivery rows, and check supplier lead times for imports
- Accredited testing can take weeks to book, so request the booking when the test plan is written
- The requirements specification goes through the client review cycle (draft, internal review, submission, review wait, revision) before design
- Experiment and test rows do not assume success. If one retest is plausible, add a retest row at 30% of the base row's duration; if two or more, 50%. Note the reason for the ratio in one line

Completion criteria examples

| Output | Done when |
|---|---|
| Requirements specification | Every requirement has an ID and a verification method, client confirmed |
| Test report | Every indicator shows target and measured value, PM approved |
| Accredited test certificate | Original received and target achievement judged |

## Operate

The base template runs preparation, recruiting and selection, operation, and performance management, in that order.

| Stage | Typical rows | Typical outputs |
|---|---|---|
| Preparation | Operation plan, selection criteria, call for applications | Operation plan, selection criteria |
| Recruiting and selection | Call posted, application wait, document and presentation review, notification | Applicant list, review results |
| Operation | Sessions, participant support, satisfaction survey | Session results, satisfaction results |
| Performance management | Results tally, performance analysis, final report | Results table, final report |

- Applicants decide when the application period ends, so it is a wait row. Add an extra call as a follow-up row for when applications fall short
- Sessions with the same format go into one grouped row, with the session count and dates in the notes
- If the satisfaction survey is a survey, apply the response rules in `survey.md`

## Mixed projects

For a project that spans two types, pick one main template by the final deliverable and replace or insert stages from the other type. Decide first whether to replace or insert. The same work in two stages breaks the scope check.

| Combination | How to merge |
|---|---|
| Plan and Research | Replace the Plan situation analysis with Research design, data collection and analysis |
| Plan with some technology development actions | Insert the technology target rows from R&D program planning into action planning. Only technology development actions get readiness levels and performance targets |
| Plan with some commercialization actions | Insert the market and business case stage from the commercialization strategy before performance management |
| Research and commercialization | Replace Research interpretation and recommendations with the market and business case stage |
| Plan and Build | For planning that includes a pilot, insert the testing and verification stage into the Plan template |

- Keep only one project management stage
- Run `plan.py check` again after merging. Merging usually makes the schedule longer
