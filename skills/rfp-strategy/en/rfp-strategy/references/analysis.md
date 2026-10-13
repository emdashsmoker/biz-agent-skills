# RFP Analysis Template

> Translated from the Korean original. It may behave differently from the original's intent.

Rules and template for writing 01_rfp_analysis.md. Read in analysis mode and in step 1 of strategy mode. Every item in this document is filled from the RFP alone.

## Rules

- Copy requirements, detailed evaluation items, eligibility wording, and writing rules verbatim. A summary makes it impossible to check the proposal's wording against the RFP later.
- Give the source location (page number or clause number) for every item.
- Write "Not stated in RFP" for items the RFP does not cover.
- Bold any condition that could lead to disqualification, point deductions, or exclusion.
- When the RFP presents its scope as a table, carry each row and cell over as a requirement row. Put the path of parent headings in the parent item column so the placement decision can be traced.
- Do not read a grouped score as the score of one part. Break a grouped score such as "validity of research content, 30 points" down into its detailed evaluation items.
- Record statutes and guidelines cited by the RFP with their names and article numbers exactly as written.

## Judging the project type

The project type decides which module skeleton strategy mode uses. Look for the signals below in the RFP's project name, purpose, and deliverable list.

| Project type | Signals | Line of thinking |
|---|---|---|
| Strategic planning | Master plan, mid- to long-term strategy, development strategy, promotion plan, vision, roadmap, management strategy, organizational diagnosis, internal performance indicator development, new business discovery | Goal setting |
| IT planning | Information strategy plan (ISP), information system master plan (ISMP), intelligent information society plan, system and platform build planning, data and AI adoption plan, digital transformation plan, next-generation system and upgrade plan | Goal setting |
| Program planning | New program planning, preliminary planning, detailed planning, feasibility review, planning report, facility construction master plan | Goal setting and gap analysis |
| Performance analysis and evaluation | Performance analysis, performance evaluation support, self-evaluation, performance management, effectiveness analysis | Gap analysis |
| Management evaluation support | Public institution management evaluation support, management performance report, evaluation manual indicators | Gap analysis |
| Problem solving | Fact-finding survey, trend survey, demand survey, institutional improvement, business process improvement, project discovery | Gap analysis |
| Support program operation | Business support program operation, commercialization support, startup support, workforce training operator | Gap analysis |

- The line of thinking is where the project's reasoning starts. Goal setting defines the target state first and works downward. Gap analysis establishes the current state first and closes the distance to the target.
- If no signal matches, judge by the line of thinking. A project that asks to define a target state defaults to strategic planning. A project that asks to find the causes of a current problem defaults to problem solving.
- For mixed projects, record a primary type and a secondary type. Mixing by module is designed in strategy mode.
- Attach the RFP wording and source location that support the judgment.

## Key wording dictionary

- Record 5-15 terms the RFP uses for project names, deliverable names, phase names, and target names.
- If the RFP uses different terms for the same thing, take the one it uses most as standard and list the others in the variant column.
- Record the client's official name together with any abbreviation used in the RFP or the client's official documents.
- The proposal uses only the standard terms. Evaluators look for score items using the RFP's wording.

## Template

Copy this template and fill it in. Do not break lines or use the `|` character inside a table cell. Separate multiple values in one cell with commas.

```markdown
# RFP Analysis: [Project name]

## Project overview

| Item | Content | Source |
|---|---|---|
| Project name | | |
| Client | | |
| Department and contact | | |
| Budget | Amount, whether VAT is included | |
| Project period | | |
| Contract method | | |
| Proposal deadline | | |
| Where and how to submit | | |
| Presentation | Presentation time, Q&A time, presenter requirements | |
| Other notes | Submission, security, or contract conditions the RFP stresses | |

## Eligibility

| Category | RFP requirement | Source |
|---|---|---|
| Business registration | | |
| Company size restriction | SME-only restriction, large-company participation limit | |
| Regional restriction | | |
| Certification | | |
| Track record requirement | Accepted period, amount, project type | |
| Staff requirement | Field of study, degree, experience, licenses | |
| Required team composition | | |
| Joint bidding and subcontracting | Allowed or not, number of members, share conditions | |

## Submission documents

| Document | Copies and format | When | Source |
|---|---|---|---|

## Evaluation criteria

- (Evaluation method) Technical-to-price ratio, threshold for negotiation eligibility
- (Price scoring formula) Verbatim

| Section | Evaluation item | Detailed evaluation item (verbatim) | Points | Quantitative | Source |
|---|---|---|---|---|---|

- (Point total) Value computed in code and the RFP's stated total

## Scope

| ID | Parent item | Requirement (verbatim) | Source |
|---|---|---|---|
| T1 | | | |

## Deliverables and reporting

| Category | Content | Timing | Format and copies |
|---|---|---|---|
| Final deliverables | | | |
| Reporting meetings | | | |
| Other submissions | | | |

## Writing rules

| Item | RFP rule | Source |
|---|---|---|
| Page limit | | |
| Required table of contents | | |
| Format | Paper size, font, file format | |
| Designated vague expressions | Expressions the RFP says not to use | |
| Quantification requirement | | |
| Requirement cross-reference table | | |
| Abbreviation list | | |
| Sanctions for false statements | | |

## Reading the RFP

- (Stated need) Background and purpose sentences, verbatim
- (Problem to solve) Conditions the background describes negatively and the causes the RFP gives
- (Project type) Primary type, secondary type, supporting wording and source location
- (Domain knowledge needed) Up to 5 items of legal, industry, or technical knowledge needed to deliver. Attach the related requirement IDs to each
- (Techniques named by the RFP) Analysis techniques the RFP asks for by name

| RFP standard term | Variant terms | Source |
|---|---|---|

## Items to confirm

- (Internal inconsistencies) Places where point totals, periods, or amounts disagree
- (Ambiguous clauses) Clauses open to more than one reading. List them as candidate questions to the client
```

## Item guidance

- (Contract method) Record the notice's wording as is, such as negotiated contract, qualification review, or two-stage competition. Evaluation and negotiation steps depend on the contract method.
- (Quantitative) Mark items scored from submitted documents, such as credit rating or number of past projects, as "quantitative". Proposal writing cannot raise these scores.
- (Negotiation eligibility threshold) Bold any minimum technical score. Falling below it removes the bid from negotiation regardless of price, so prepare every evaluation item evenly.
- (Domain knowledge needed) Pick only knowledge whose absence would derail a deliverable. Leave out general knowledge that the project name already suggests.
- (Items to confirm) Report point totals and amount conversions only after checking them in code.
