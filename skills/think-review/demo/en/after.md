## Overall assessment
- As it stands, the plan is unlikely to win executive approval and needs revision before submission
    + Conflict between the security rule that forbids entering work documents into external generative AI services and the plan to query company documents directly through an external cloud hyperscale AI
    + No baseline or formula behind the 50% reduction and KRW 300 million savings that support the investment decision
- The interpretation of the security rules could overturn the critical finding
    + If enterprise contract services that neither train on nor retain input data are confirmed as outside the ban, item 1 is resolved by citing the relevant clause
    + The other findings need revision regardless of how the rules are interpreted

## Findings

| No. | Location | Severity | Problem | Impact | Fix |
|---|---|---|---|---|---|
| 1 | Approach (model) | Critical | The plan to query company documents directly through an external cloud hyperscale AI conflicts with "no work documents into external generative AI services" in the current state and "comply with company security rules" in the goals | • Possible rejection at the first stage of executive review<br>• If approved, implementation in breach of the rules | • State a pilot-only security rule exception among the decisions requested<br>• Propose exception conditions of a contract with no training on or retention of input data, and exclusion of confidential documents |
| 2 | Goals (impact) and expected benefits | Major | • The target widens from "document search and report drafting" in the background to all "document work" in the goals<br>• No baseline for 50% and no formula for KRW 300 million<br>• Reduced work time presented as labor cost savings | • No answer to executive questions on the basis for the impact<br>• KRW 300 million assumes KRW 600 million a year of document work labor cost for the people covered<br>• With headcount and overtime unchanged, actual labor spending stays at the current level | • Define the target as "time per case for past document search and report drafting"<br>• Measure the baseline in the first month after kickoff<br>• Present KRW 300 million with its formula as "labor cost equivalent of hours saved" |
| 3 | Approach (schedule) | Major | • A March briefing for all departments and an April company-wide rollout fixed without evaluating the two-team pilot<br>• No interim checkpoints or criteria for the expansion decision | • Company-wide rollout regardless of pilot results<br>• A failed pilot spreads its damage company-wide | • Make April the point for reporting pilot results and deciding on company-wide rollout<br>• Move the all-department briefing after the expansion decision<br>• Set expansion conditions of meeting the time reduction target, an answer error rate within tolerance and zero security incidents |
| 4 | Budget and approach (build and operations) | Major | • Only service fees in the budget<br>• Missing the IT team's integration development and operations effort (5 people, no one dedicated to AI) and external technical support costs<br>• No usage assumptions or scope for the KRW 120 million | • Additional budget requests likely after approval because total cost is understated<br>• Gaps in the IT team's existing work | • Show the budget split into service fees, IT staff effort and external support<br>• Name the IT team members and their hours<br>• Limit integration scope to the two teams' document repositories |
| 5 | Whole document | Major | No risks and responses section | • Errors in generated output may flow straight into quality and design documents<br>• Documents outside a user's rights may surface in search | • Add a risk response section<br>• Show the source location for every answer, checked by the author<br>• Allow search only within each user's existing access rights<br>• If the security exception is not approved, resubmit with an in-house server model |
| 6 | Top of document | Major | No statement of the decisions and approval scope requested from executives | Unclear what is up for approval among the pilot budget, the security rule exception and the company-wide rollout | Add a decisions requested section right under the title |
| 7 | Background and approach (model) | Minor | • No source for "the cost has dropped sharply"<br>• No performance criterion for "highest-performing" | Weak basis for the timing of adoption and the service choice | • Add a source for the price drop (delete if none)<br>• Change the service selection criterion to the answer error rate on the two teams' work documents |

## Items to confirm
- Whether services contracted to neither train on nor retain input data fall under the security rule's ban, and the exception approval procedure
- The formula and scope of the KRW 300 million (if there is no formula, delete the amount and derive it from the April pilot results)
- The user count, usage assumptions and scope behind the KRW 120 million
- Where the two teams' documents are stored and how far they are digitized (if spread across several repositories or mostly scanned images, the integration scope and period grow)
- The integration development period estimated by the IT team (if over one month, the pilot operation and results reporting schedule needs adjusting)

## Revised plan
- (Structure) Decisions requested placed at the top, risk response and performance check sections added
- (Consistency) Conflicts resolved between the security rules and the service setup and between the pilot scope and the rollout schedule
- (Basis) Target definition, baseline measurement timing and formulas added to the impact figures
- (Wording) Technical terms such as "connect by API" replaced with plain terms
- (Open values) Figures and bases still to be confirmed marked as [ ] fields

# In-house hyperscale AI pilot plan (draft)

## Decisions requested
- Approval requested for a hyperscale AI pilot (January-March 2027) for the quality and design teams
    + (Pilot budget) Spend a pilot-period total of [enter total]
    + (Security rule exception) Allow processing of work documents by an external hyperscale AI service for the pilot period only
    + (Company-wide rollout) Submitted separately with the April pilot results report

## Background
- A hyperscale AI pilot is needed for the quality and design teams
    + (Time burden) The two teams report a heavy time burden from searching past documents and drafting reports
    + (Cost conditions) Falling hyperscale AI service fees have reached a level a mid-sized company can adopt [enter source for the price change]

## Current state
- Security rules and IT staffing constrain adoption of an external hyperscale AI service
    + (Security rules) No work documents into external generative AI services
    + (IT staffing) IT team of 5 people with no one dedicated to AI

## Goals
- (Time reduction) Cut the per-case time for past document search and report drafting in the quality and design teams by 50% against the baseline measured in the first month after kickoff
- (Security) Comply with the conditions of the approved security rule exception and keep security incidents at zero during the pilot

## Approach
- (Service setup) Connect an external cloud hyperscale AI service to the two teams' document repositories to support document search and drafting
    + Limit candidate services to those contracted to neither train on nor retain input data
    + Choose the final service by comparing answer error rates on the two teams' work documents
- (Build and operations) The IT team develops and runs an integration limited to the two teams' document repositories
    + Name the IT team members and their hours [enter people and hours]
    + Include the vendor's technical support for integration development and incident response in the contract terms
- (Schedule) Kick off in January 2027, report pilot results in April
    + (January) Service selection, integration development, baseline measurement for the two teams
    + (February-March) Pilot with the two teams and interim check at the end of February
    + (April) Pilot results report and decision on company-wide rollout

## Budget
- Total pilot cost is the sum of service fees, IT staff effort and external support costs [enter total]
    + (Service fees) Pilot-period share of the estimated KRW 120 million a year (based on the external service's published pricing) [enter amount and usage assumptions]
    + (IT staff effort) Labor cost equivalent of the hours spent on integration development and operations [enter amount]
    + (External support) Vendor technical support and security review costs [enter amount]

## Risk response
- Pilot risks managed with response measures fixed before kickoff
    + (Document leakage) Exclude confidential documents from the connection scope
    + (Viewing beyond rights) Return search results only within each user's existing document access rights
    + (Errors in generated output) Show the source location with every answer, reflected in documents only after the author checks it
    + (Security exception not approved) Switch to an in-house server model and resubmit the budget and schedule

## Performance check
- Same indicators applied at the end-of-February interim check and the April results report
    + (Time reduction rate) Reduction in per-case time by task type against the baseline
    + (Answer error rate) Share of sampled answers containing factual errors [enter sample size and tolerance]
    + (Security) Number of security incidents and of views beyond access rights
- Company-wide rollout submitted once the time reduction and security targets are met and the answer error rate is within tolerance

## Expected benefits
- If targets are met, [ ] hours a year saved in the two teams' document search and drafting
    + (Monetary equivalent) Labor cost equivalent of hours saved estimated at KRW 300 million a year [enter formula: people covered × annual hours on these tasks × reduction rate × hourly labor cost]
    + (Spending impact) Actual labor spending falls only if headcount or overtime is adjusted
