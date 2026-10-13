# Designing the Work Structure

> Translated from the Korean original. It may behave differently from the original's intent. Korean regulations and document names are glossed in English.

Rules for designing section 7 (work structure) of 02_proposal_strategy.md. Use the project type judged in 01_rfp_analysis.md and confirmed by the user in the intake questions. Read the section for that project type and the common standards section.

## Principles

- The RFP's scope takes precedence over the module skeleton. The skeleton is a starting point for design.
- Structures that differ from the skeleton are allowed. Only avoid reversed order (environment analysis after strategy formulation).
- For mixed projects, mix types module by module.
- Stages the RFP does not ask for may be omitted.
- Scale the analysis effort to the size of the project. Presenting a large public-investment-grade analysis for a project worth a few hundred million won reads as unworkable.
- Name only the techniques the RFP asks for (SWOT, AHP (analytic hierarchy process), Delphi, logic model, and so on). Describe other techniques by what is done, without naming them.
- Strategies and tasks inherit their parent number (1. strategy, 1-1. strategic task, 1-1-1. implementation task).
- Assign every requirement to at least one task.
- Evaluators judge practical understanding from the names of surveyed organizations, source names, survey sizes, and preliminary findings. A method name cannot stand in for this evidence, so state targets and sizes with names and numbers in every task.
- Choose the channels for gathering tasks and demand from demand surveys, perception surveys, expert participation, and direct derivation according to the RFP. Plan a task for each chosen channel. If only direct derivation is used, add an advisory or demand-confirmation step.

The status of the skeleton depends on the track.

| Track | Project types | Status of the skeleton |
|---|---|---|
| Regulation-based | Performance analysis and evaluation, management evaluation support, R&D program planning within program planning | Regulations set the skeleton and wording, so the type skeleton is the default |
| Conditionally regulated | IT planning, non-R&D program planning within program planning | If the project is subject to a regulatory review or mandate, apply that guideline's structure. Otherwise use the skeleton as a reference and fit it to the RFP scope and project size |
| Discretionary | Strategic planning, problem solving, support program operation | The skeleton is a reference example. Derive modules and tasks from the RFP scope and key issues. Copying the example skeleton as is makes the proposal indistinguishable from competitors |

## Lines of thinking

The differences between type skeletons are differences in deliverable specifications. The order of reasoning splits into two lines. The line decides module order and does not appear in the proposal manuscript.

| Line | Order of reasoning | Project types |
|---|---|---|
| Goal setting | Define target state → align with higher-level policy → build goal hierarchy → cascade downward | Strategic planning, IT planning, goal-hierarchy part of program planning |
| Gap analysis | Establish current state → find gap to target → structure causes → design alternatives | Problem solving, performance analysis and evaluation, management evaluation support, support program operation, current-state part of program planning |

Program planning overlaps both lines in one project. For programs under regulatory review, such as a preliminary feasibility study, give more weight to the goal hierarchy and alignment with higher-level policy.

## Strategic planning

M1 Internal and external environment analysis → M2 Current state and case analysis → M3 Vision and strategy → M4 Implementation plan

| Module | Content | Deliverables |
|---|---|---|
| M1 Internal and external environment analysis | Only the trends relevant to the topic among policy, economy, society, technology, and law. Global first, then domestic | List of environmental change factors |
| M2 Current state and case analysis | Capability diagnosis of the target organization, domestic and international leading cases | Diagnosis results, case implications |
| M3 Vision and strategy | Synthesis of implications, vision framework, strategies and strategic tasks by area | Vision framework chart, strategic task list |
| M4 Implementation plan | Implementation tasks, priorities, roadmap, funding and governance, performance indicators, expected effects | Implementation task cards, roadmap, indicator table |

- (Common mistakes) Mixing the target picture into environment analysis, jumping to strategy without implications
- (Environment analysis) Stick to facts. Interpretation, forecasts, the target picture, and solutions do not belong in this stage.
- (Current state) Diagnose strengths and weaknesses together. Show the gap between the requirements found in environment analysis and the current state. Keep introductory facts about the organization (history, structure, budget) separate from the capability diagnosis.
- (Implications) This stage links analysis to strategy. State the source of the supporting facts (external, internal, case) for each implication.
- (SWOT factor sources) Use current-state implications only for strengths and weaknesses. Use external-environment implications only for opportunities and threats. Case implications may feed all four.
- (SWOT cross strategies) An SO strategy combines only S and O. ST, WO, and WT likewise combine only their two quadrants.
- (Gap analysis) Use a four-column table: current picture, target picture, gap, solution strategy. The target picture rests on case analysis and higher-level plans.
- (Strategy framework alignment) Connect vision, mission, strategies, strategic tasks, implementation tasks, and performance indicators into one numbered system.
- (Link check) Create no child without a parent and no parent without a child. Place every implication so it leads to at least one task.
- (Vision) Reflect both the direction of higher-level plans and national policy (top-down) and the common aims of the strategies (bottom-up). Present a three-column table: top-down, bottom-up, final.
- (Priorities) Present evaluation criteria and weights in a table and name the evaluators and procedure. Close with a short-, mid-, and long-term roadmap.
- (Expected effects) If the RFP asks for spillover effects, place them in M4. Use the input-output analysis table in the program planning section.
- (Regional industry development) Place industry specialization (location quotient), company demand surveys, access to anchor institutions and customers, and workforce supply in M2.
- (New business discovery) Narrow candidates in this order: redefine the business → long list → first screen (market attractiveness, fit with the client, financial feasibility) → second-screen indicators → evaluation of new businesses → detailed business plans. Split activation measures into before- and after-development scenarios.

Example priority criteria. Adjust the weights to the project.

| Criterion | What is judged | Weight | Evidence |
|---|---|---|---|
| Policy fit | Link to national agenda and higher-level plans | 30 | National agenda, higher-level plans |
| Urgency | When losses start if not pursued | 20 | Environment analysis results |
| Feasibility | Budget, staff, and regulatory conditions | 30 | Current-state diagnosis |
| Spillover | Reach of benefits and linked industries | 20 | Case analysis |

Evaluators are usually the advisory committee or subcommittees. Scores are collected through an online survey and weights derived with AHP.

### Combined management strategy projects

Mid- to long-term management strategies for public institutions often cover management strategy, organizational diagnosis, and efficiency together.

- (Management strategy) Environment analysis, reset of mission, vision, and core values, development strategy, strategic and action tasks cascaded to departments, priorities and timing, annual performance indicators
- (Organizational diagnosis and redesign) Job analysis, quantitative and qualitative workload study, appropriate headcount and allocation, restructuring plan, delegation-of-authority improvements
- (Management efficiency) Business portfolio, management evaluation indicator improvements, ESG, the government's public institution reform direction. Wording for management evaluation indicators follows the management evaluation support section
- (Organization and HR projects) Job analysis → span-of-control analysis → comparison with similar organizations → redesign → phased implementation
- (Internal performance indicator development) Run from analysis of internal and external evaluation systems to proposals for system improvement. Derive a pool of indicator candidates through stakeholder interviews and check validity and measurability with an expert survey and AHP weights. After writing indicator definitions (definition, formula, weight, measurement method), present a pilot application and system improvements. Place output indicators and outcome indicators separately.

Do not use the performance analysis and evaluation skeleton for management evaluation support, indicator development, or organizational diagnosis.

## IT planning

M1 Environment analysis → M2 Current state analysis → M3 Target model design → M4 Implementation plan

| Module | Content | Deliverables |
|---|---|---|
| M1 Environment analysis | Policy and technology trends, alignment with higher-level plans, IT cases of similar organizations | Environmental factors and implications |
| M2 Current state analysis | Business processes, information systems (applications, data, infrastructure, security), user needs | Current-state diagnosis and list of improvement needs |
| M3 Target model design | Business, information, application, technology, and security models | Target architecture |
| M4 Implementation plan | Implementation tasks, priorities, phased schedule, required budget, expected effects | Implementation roadmap, task cards, budget estimate |

- (Common mistakes) Not checking whether the project is mandated, forcing ISP (information strategy plan) procedures and deliverable names on non-mandated IT planning, a budget total without a basis, invented classification codes
- (Mandate check) Under the budget formulation guidelines, central government agencies prepare an ISP or ISMP (information system master plan) before requesting a budget to build or rebuild an information system. The procedure follows the ISP·ISMP 수립 공통가이드 (Common Guide to ISP and ISMP) published by the National Information Society Agency (NIA). Judge whether the project is mandated from the RFP's governing guideline, project size, and deliverable list (information strategy plan, draft RFP). If unclear, ask in the intake questions.
- (Parts set by regulation for mandated projects) The four-stage skeleton (environment analysis, current state analysis, target model, implementation plan), the requirement classification scheme, the budget estimation basis (소프트웨어사업 대가산정 가이드, Software Project Cost Estimation Guide), and public IT security design (국가 망 보안체계, National Network Security Framework)
- (Parts left to discretion even for mandated projects) Module names and splits, task composition, survey design, level of detail of the target model, and implementation priority criteria
- (Non-mandated IT planning) For system and platform build planning, data and AI adoption plans, digital transformation plans, and next-generation or upgrade plans, build modules around the scope the client asks for. The skeleton above and the standard deliverable names are reference examples. A light IT plan can be shortened to current state and needs analysis → target system design → build and operation plan.
- (Public plans) For public plans such as an intelligent information society plan, replace M3 with a policy task framework and add governance and performance indicators to M4.
- (Current state analysis) State the size of user surveys and interviews in numbers. Present the current systems in a table with system names, year introduced, and operator. State the gap with a current-versus-target comparison table.
- (Requirements) Split into functional and non-functional. Use only the classification codes the RFP specifies. If the RFP gives no codes, use category names only.
- (Security design) Public IT security design uses the procedure of the National Network Security Framework (N2SF) (prepare, C/S/O classification, threat identification, security control selection, adequacy assessment) and the wording of the controls for each level verbatim. C is classified, S is sensitive, and O is open.
- (Budget) Present the required budget in a table with its basis (labor rates, equipment quotation basis). State the year of the cost estimation guide applied.
- (Implementation plan) Structure it as implementation task definitions → roadmap → sizing and budget → build project plan (review of separate procurement, RFP).
- (PoC, proof of concept) Bundle goal setting → data preparation → model selection and environment → pilot service and performance analysis into one round and repeat the round. State performance conditions (concurrent users, throughput) in numbers.
- (Standard deliverable names) Environment analysis report, current state analysis report, IT vision and strategy definition, business process design, target model design, data management framework design, operations framework design, implementation plan, next-year project plan, RFP. Names set by the RFP take precedence.
- (Project understanding) In IT proposals, project understanding is usually built from the policy environment, the client's data situation, the client's constraints (security, data, decision structure), and a comparison of the current and target pictures.

## Program planning

M1 Policy and environment analysis → M2 Similar programs and review findings → M3 Goal hierarchy and logic model → M4 Feasibility → M5 Review and reporting support

| Module | Content |
|---|---|
| M1 Policy and environment analysis | Fit with higher-level plans, policy and technology trends, problems and issues |
| M2 Similar programs and review findings | Review of similar programs, overlap and distinctiveness, item-by-item response to review findings on earlier plans |
| M3 Goal hierarchy and logic model | Purpose, strategic goals, performance goals, indicators, detailed activities, alignment check |
| M4 Feasibility | Governance, funding, legal and regulatory risks, cost estimation and economic analysis |
| M5 Review and reporting support | Writing the planning report, in-person meetings and Q&A. Include only when the RFP asks |

- (Common mistakes) Confusing outputs with outcomes, describing an abolished or changed program as current
- (Weighting by program nature) Weight the analysis toward the spillover logic for programs that secure leading technology, toward market demand and cost-benefit for industrial application programs, and toward utilization and cost-effectiveness for infrastructure and workforce programs.
- (Regulation check) Korea's preliminary feasibility study for national R&D programs was abolished by a 2026 legal amendment and replaced by pre-review systems split into research-type and construction-type programs. The preliminary feasibility study for general fiscal programs remains. Do not mix the two. At kickoff, check the current names, thresholds, and procedures.
- (Private service planning) Adapt the order to market and user research → competition and case analysis → service model and feature definition → business case and execution plan.

### Logic model

- The boxes run: problems and issues → program goals → inputs → activities (detailed activities) → outputs → outcomes → impact.
- Test each link between adjacent boxes. The later box cannot stand without the earlier one.
- Put detailed activities (sub-programs, task groups) in the activities box. Put the direct products of the activities in the outputs box. Put the changes that happen to beneficiaries in the outcomes box.
- Mixing outputs and outcomes undermines trust in the whole logic model. Paper counts are outputs. A change in the domestic production rate is an outcome.
- An outcomes box without specified beneficiaries does not hold.

### Goal hierarchy alignment

| Goal hierarchy | Logic model box | Alignment check |
|---|---|---|
| Program purpose | Impact | Does it match the state the program aims to change? |
| Strategic goal | Outcomes | Is it written at the level of change in beneficiaries? |
| Performance goal | Outputs, short-term outcomes | Can it be achieved within the program period? |
| Performance indicator | Means of measurement | Is it linked one-to-one to a performance goal? Is the formula objective? |
| Detailed activity | Activities | Is it clear which performance goal it contributes to? |

- Presenting a filled-in alignment table is evidence that the design is complete.
- Indicators must be both representative and measurable. State the measurement formula and the source of the evidence.

### Combining diagnostic tools

| Variant | Structure | When to use |
|---|---|---|
| Full | Issue diagnosis → gap analysis or SWOT → goal setting → logic model | Large new programs, regulatory review, when the basis for goals must be shown |
| Logic-model-centered | Problem definition and goal setting handled inside the logic model | The client provides a logic model form, program scope is clear |
| Diagnostic-tool | Goals linked to tasks with gap analysis or SWOT, without a logic model | Small programs, restructuring of existing programs |

Do not use both gap analysis and SWOT. State the reason for the chosen variant in one line.

### Non-R&D program planning

| Track | Order of analysis |
|---|---|
| Construction and facilities | Issues → economic analysis (demand, benefits, costs) → policy analysis → regional balance → overall judgment |
| Welfare and income transfer | Issues → socioeconomic environment → adequacy of program design → cost-effectiveness → overall judgment |
| IT | Issues → technological and social environment → adequacy of program design → cost-effectiveness → overall judgment |

- For small and mid-sized planning, adequacy of program design weighs most in the verdict. Its sub-items are appropriateness and urgency of program goals, appropriateness of beneficiaries, appropriateness of the delivery method, appropriateness of the delivery system, and appropriateness of implementation and operation plans.
- (Facility master plan and feasibility study) Proceed as current-state diagnosis → case for building → basic direction and strategy → detailed plan → total project cost, funding, and annual revenue forecast → economic feasibility and spillover effects. Build the current-state diagnosis from relevant laws and higher-level plans, national facility statistics, domestic and international cases, and regional conditions. Build the detailed plan from facility size, exhibition or operating programs, basic architectural concept, and management and operation plan. If the client's aim is to be selected in a central-government competition, put support for the competition's review criteria and for writing the application in the expected effects. Use non-R&D regulatory terms.

### Rules for economic analysis

- Compare doing the program with not doing it. Do not use before-and-after comparison.
- Count only benefits directly related to the program's purpose. Exclude sunk costs, include opportunity costs, and exclude VAT.
- Include operating costs, reinvestment, and residual value along with initial investment. State the discount rate and analysis period with their values and basis.
- If benefits are hard to quantify, switch to cost-effectiveness analysis and state why. Run sensitivity analysis on the main variables.
- Compute in code and present formulas in a two-column table.

| Item | Formula |
|---|---|
| Present value | Future value ÷ (1 + discount rate)^years elapsed |
| Net present value | Sum of benefit present values - sum of cost present values |
| Benefit-cost ratio | Sum of benefit present values ÷ sum of cost present values |
| Internal rate of return | Discount rate that makes net present value 0 |
| Cost-effectiveness ratio | Cost per unit of effect |

Input-output analysis formulas are as follows.

| Item | Formula |
|---|---|
| Production inducement | Σ(spending by commodity group × production inducement coefficient) |
| Value-added inducement | Σ(spending by commodity group × value-added inducement coefficient) |
| Employment inducement | Σ(spending by commodity group × employment inducement coefficient), in persons per KRW 1 billion |

- Use coefficients from the Bank of Korea input-output tables. State the publication year and the commodity classification. Present the basis for allocating the total project cost to commodity groups in a table.
- Do not count inducement effects again as benefits in the economic analysis. Adding the two counts the same effect twice.

## Performance analysis and evaluation

Current state of the target program → analysis criteria → performance survey and verification → analysis of inputs, outputs, and effects → representative results and improvements → report and review support

- (Common mistakes) Presenting inputs versus outputs without a comparison group, ignoring when the year's guideline is announced
- Written for the Korean national R&D performance evaluation system. For non-R&D program evaluation, check the relevant evaluation guideline and replace the track table and performance types.
- Institutional management evaluation support follows the management evaluation support section.

| R&D regulatory track | Timing | Main deliverables |
|---|---|---|
| Strategic plan | Start of a new program or end of a planning period | Strategic goals, performance goals, performance indicators, evaluation plan |
| Interim self-evaluation | During the program (check the cycle in that year's guideline) | Self-evaluation report, comprehensive performance analysis report, representative result profiles |
| Performance management and utilization plan | After the program ends | Performance management and utilization plan, final goal attainment rate |
| Effectiveness analysis | After the program ends (check the timing in the guideline) | Effectiveness analysis report, spillover estimate |

- Each track's guideline is announced every year. Until it is announced, prepare against the previous year's guideline, and state in the proposal that the response will be updated after the announcement.
- If there are several target programs, present an overview of each first (purpose, legal basis, period, size, summary table of performance goals and indicators).
- If there are several tracks, split modules by track.

| Step | Content |
|---|---|
| 1 Current state of the target program | Strategic plan, annual reports, links among purpose, strategic goals, performance goals, and indicators |
| 2 Analysis criteria | Four-column table of performance type, analysis item, analysis indicator, and measurement method, with weights |
| 3 Performance survey and verification | Data from the managing agency, principal investigator survey, beneficiary survey, check against raw data |
| 4 Input and process analysis | Appropriateness of purpose and government support, governance, budget size and program mix |
| 5 Efficiency of outputs | Inputs versus outputs, shown with comparison groups (overall average, similar programs) |
| 6 Effectiveness of outcomes | Qualitative excellence, goal attainment, influencing factors, spillover effects |
| 7 Representative results | Set selection criteria, gather result information, write profiles (3-5 at most) |
| 8 Synthesis and improvements | Improvements and action plans for weak areas, feedback plan |
| 9 Report and review support | Writing the report, support for the self-review committee and higher-level review |

- R&D performance types are scientific, technological, economic, social, and infrastructure results. Refer to the national R&D standard performance indicators and add program-specific results.
- For the principal investigator survey, state the target, period, distribution method, follow-up procedure, and verification method. List in advance the data to request from the managing agency. For non-R&D programs, survey program staff and beneficiaries instead.
- Classify the causes of missed indicators (insufficient outputs for inputs, missing evidence, a problem with the indicator itself).
- Write the goal attainment rate as the sum over indicators of weight times attainment.
- Analyze both success and failure factors for utilization and diffusion of results. Leaving out failure factors fails the review criteria.
- (Non-R&D support program performance study) Build the analysis criteria from indicators by input, output, and outcome type. Analyze factors affecting performance with statistical methods such as regression. Estimate regional economic spillover with input-output analysis. Survey participating companies on satisfaction and improvements. Use general terms such as performance analysis, performance indicators, and development plan.

## Management evaluation support

Analysis of the evaluation manual's indicator structure → analysis of last year's results and findings → rebuilding the performance argument for each indicator → strategy for non-quantitative indicators → comparison with other institutions' best practices → support for writing the management performance report

- (Common mistakes) Mixing in the performance analysis and evaluation skeleton, ignoring when the manual is revised
- This is a regulation-based track whose skeleton and wording are set by the public institution management evaluation manual and the local public enterprise management evaluation.
- Main deliverables are an improved management performance report, arguments for each indicator, and non-quantitative narratives.
- Use indicator names and weights exactly as written in that year's manual. State a plan for reflecting manual revisions.
- The client's aim is often a higher evaluation grade, so keep the background short.

## Problem solving

Define the problem → break down the issues → prioritize the issues → build a work plan → critical analysis (hypothesis testing) → synthesize findings → communicate conclusions and actions

This sequence is usually compressed into the 3-4 modules below.

M1 Current state diagnosis → M2 Gap analysis → M3 Improvement design

| Module | Content |
|---|---|
| M1 Current state diagnosis | Problem definition and causal hypotheses, issue breakdown, establishing the current state (whichever of literature, statistics, and surveys fits the project) |
| M2 Gap analysis | Gap against the comparison standard, stakeholder views (FGI (focus group interview), surveys), structuring causes |
| M3 Improvement design | Setting and comparing alternatives, priorities, improvements and how to implement them |

- (Common mistakes) Defining the problem at the level of an RFP summary, not specifying survey size
- (Problem definition) From the background, derive the problem the client wants solved and causal hypotheses. Include at least one problem structure of the bidder's own.
- (Issue breakdown) Split by one criterion and check for overlaps and gaps. Keep a table of which module handles each issue.
- (Hypothesis testing) Design surveys and analysis to test hypotheses. Write hypotheses in a form that can be refuted. Drop hypotheses no result could refute.
- (Survey-centered projects) For fact-finding, trend, and demand surveys, use the RFP's scope items as the module structure. Detail tasks as survey design (target, sample, method, questionnaire structure) → data verification → synthesis. State population, sample size, survey period, and follow-up methods in numbers.
- (Institutional improvement) Current system analysis → problem typology → comparison with foreign systems → design of alternatives → comparison table of alternatives → roadmap.
- (Improvement targets) Cover whichever the RFP specifies: regulations, procedures and business processes, organization and staffing, services and programs, systems, guidelines and forms.
- (Comparison standard) Choose the gap analysis standard by target. Regulations are compared with laws and other institutions' rules, processes with standard procedures and leading cases, services with user experience and competing services.
- (Improvements) Present a three-column table: change, implementing body, timing by phase. For regulations, include the amended provisions.

| Alternative | Improvement effect | Cost | Legal amendment | Acceptance | Overall |
|---|---|---|---|---|---|
| Option 1: keep and supplement current system | Low | Low | Not needed | High | Short term |
| Option 2: new system | High | Medium | Enforcement decree amendment | Medium | Mid term |

## Support program operation

M1 Policy and program background → M2 Beneficiary status and difficulties → M3 Program design → M4 Performance management → M5 Operation and budget execution

| Module | Content | Deliverables |
|---|---|---|
| M1 Policy and program background | Higher-level policy and underlying program, regional and sector conditions, program purpose | Program purpose definition |
| M2 Beneficiary status and difficulties | Statistics on target companies and participants, surveys, difficulties and requests | Demand summary table |
| M3 Program design | Diagnosis and selection, training, consulting, networking, links to sales channels and investment | Program design document |
| M4 Performance management | Performance goal framework, indicators and targets, evidence and review methods | Performance indicator table |
| M5 Operation and budget execution | Governance and staff, annual schedule, budget allocation and execution plan | Execution plan table |

- (Common mistakes) Confusing outputs with outcomes, not specifying the size of each program stage
- Support beneficiary difficulties with statistics: number surveyed, response rate, share of top responses.
- Lay out the program by stage. For each stage, state the target, method, frequency, and deliverables.
- Split performance goals into core and voluntary goals. Columns of the indicator table are category, indicator, interim target, final target (cumulative), and evidence.
- Place output indicators (counts, number of companies) and outcome indicators (sales, investment attracted, jobs) separately.
- Present the budget as an allocation table by item and a quarterly execution plan.

## Common standards

### Purpose of modules and tasks

The purpose is what a unit's deliverables and activities supply to the project's final result. Activities such as running a council, gathering opinions, advising, and supporting demonstrations also count as a unit's result.

| Unit | Question the purpose answers |
|---|---|
| Project goal | What is secured when the project ends? |
| Module purpose | Which part of the final result do this module's deliverables and activities become, or which part do they support? |
| Task purpose | Which part of the module's deliverable do this task's deliverables and activities become, or which judgment do they support? |

- Write the purpose sentence in the order target, action, result, use. One of each.
- (Target) The material and scope to analyze or synthesize. For activity-type units, the participants
- (Action) One of analyze, diagnose, compare, synthesize, operate, gather
- (Result) What the deliverable contains (implications, factors, criteria, arguments, candidate lists) or what the activity secures (opinions, agreement, review results)
- (Use) The later step inside the project where the result is used. Name it by step or deliverable
- End the purpose according to the unit's nature. Analysis units end with "securing the basis for X" or "deriving X". Formulation units end with "formulating X", "designing X", or "finalizing X". Activity units end with what the activity secures ("gathering views on X", "securing agreement on X").
- One purpose per unit. Split a task whose purpose divides in two.
- The client's outcome is covered in the background, execution strategy, and expected effects. Do not repeat it for every module and task. For a module whose deliverable is used directly for the client's external persuasion or regulatory review, state that use too.

Example purpose sentences.

- (Analysis module) Analyze domestic and international policy, industry, and technology trends to derive the opportunities and threats that ground strategy formulation
- (Formulation module) Synthesize the implications of environment analysis and demand survey results to formulate the vision, goals, and execution strategies
- (Analysis-centered task) Analyze the development stage of key technology areas to secure the basis for judging technical feasibility when discovering strategic tasks
- (Derivation-centered task) Screen candidate tasks against evaluation criteria to finalize detailed tasks for each strategy
- (Activity task) Run an industry-academia-research expert council to secure expertise in prioritizing detailed tasks

Purpose sentences that need work:

- A purpose with only an action ("survey and analyze domestic and international trends"). Add the result and the use.
- A purpose that ends with submitting a document ("prepare and submit a status table"). End with the result and the use.
- A use that fits any project ("used for strategy formulation"). Specify which judgment in strategy formulation it serves.

### Task types

Task types are split by the nature of the deliverable. If the deliverable is the current state of the target (status, conditions, gaps, causes), the task is analysis-centered. If it is a future direction (implications, strategies, tasks, indicators, models), the task is derivation-centered. Type names are design vocabulary and do not appear in the proposal manuscript.

| Type | Methods | Items to state | Tables to include |
|---|---|---|---|
| Analysis-centered | Literature and data review, interviews and surveys, diagnosis and process analysis, data analysis | Purpose, analysis target, analysis method, deliverables | Named list of targets, preliminary findings, question areas and questionnaire structure, diagnosis items, current procedure steps |
| Derivation-centered | Turns analysis results into implications, strategies, tasks, and indicators | Purpose, material used, criteria, procedure, deliverables | Selection criteria, draft evaluation criteria, draft deliverable |

- For analysis-centered tasks, name the analysis targets (organizations, sources, interviewee ranks, business procedures) and methods. "Broadly survey related material" leaves the target unspecified.
- Where counts are fixed, state the size in numbers.
- For derivation-centered tasks, write the criteria and procedure so someone else could follow them. "Derived by synthesizing expert opinion" cannot be followed.
- Name the criteria item after the task's action: selection criteria for choosing among candidates, evaluation criteria for ranking and weighting, setting criteria for fixing indicators and targets, design criteria for building models and frameworks.
- State the procedure as the order of candidate generation, first screen, quantitative evaluation, and committee consultation, with who handles each step.
- The deliverables cell holds only the deliverable name. Put its components, judgment criteria, and uses on the lines below. Give submission timing once, in the schedule.

### Committee design

Committee design is a signal the client uses to gauge the bidder's practical understanding. State the name, members, number of meetings, agenda, and where results feed in. If the RFP names a committee, use that name.

| Committee | Members | Role | Usual meetings |
|---|---|---|---|
| Advisory committee | 5-9 outside experts from industry, academia, and research | Review of stage deliverables and advice on direction | 3-4 (after kickoff, before interim report, before final report) |
| Subcommittee | 3-5 experts per field | Proposing candidates by field, reviewing classification and indicators, reviewing pilot results | 2 per subcommittee plus written reviews as needed |
| Working council | Client staff and the project team | Data requests, decisions on current issues, checking interim deliverables | Every two weeks or monthly |
| Reporting meeting | Client decision makers and the project team | Kickoff, interim, and final reports | 3 |

- Present committee candidates in a draft candidate table. Columns are number, sector (industry, academia, research, government), affiliation, title, and name. Note below the table that members will be finalized in consultation with the client.
- Choose candidates from the list the user provides. A pool of about 15-20 is customary; for small projects, about twice the committee size. Without a list, give only fields and numbers.
- Columns of the meeting-by-meeting table are meeting, timing, agenda, and where results feed in (deliverable name).

| Meeting | Timing | Agenda | Where results feed in |
|---|---|---|---|
| 1st | 3 weeks after kickoff | Review of analysis criteria and survey design | Finalize Task 1-2 questionnaire |
| 2nd | Before interim report | Review of implications and strategic direction | Revise Task 3-1 strategy candidates |
| 3rd | Before final report | Review of implementation plan and indicators | Reflected in final report |

### Consultation tools

| Tool | When to use | Items to state |
|---|---|---|
| Survey | Conditions, perceptions, demand | Target group and population size, sample size, number of questions per area, distribution channel, target response rate, follow-up procedure |
| In-depth interview | Finding causes, how a system operates in practice | Interviewee rank and number, sessions, question areas |
| FGI | Identifying disagreements among stakeholders | Group composition criteria, number of groups, participants per session |
| Delphi | Expert consensus (indicators, technology level, future outlook) | Panel size, number of rounds, consensus criteria (coefficient of variation, quartiles) |
| AHP | Priorities and weights | Hierarchy, number of raters, consistency ratio threshold (usually 0.1 or below) |
| Demand survey | Task discovery | Submission form items, distribution targets, cleaning criteria (duplicates, out of scope, excessive budget) |

Listing only tool names leaves the design unfinished. Numbers for size and procedure are the evidence of design.

## Sources for the methods

- Order of reasoning for problem solving: Charles Conn, Robert McLean (2018), Bulletproof Problem Solving, Wiley
- Logic model boxes: W.K. Kellogg Foundation (2004), Logic Model Development Guide (https://wkkf.issuelab.org/resources/10124/10124.pdf)
- SWOT cross strategies: Heinz Weihrich (1982), The TOWS Matrix: A Tool for Situational Analysis, Long Range Planning 15(2)
- AHP consistency ratio: Thomas L. Saaty (1980), The Analytic Hierarchy Process, McGraw-Hill
- IT planning procedure: National Information Society Agency (2025), ISP·ISMP 수립 공통가이드 9th edition (https://nia.or.kr/site/nia_kor/ex/bbs/View.do?cbIdx=99835&bcIdx=28088&parentSeq=28088)
