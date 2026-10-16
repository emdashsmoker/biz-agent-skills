# In-house artificial intelligence (AI) deployment paced by stages of verified results

## Problem setting that starts from beneficiary needs
- (Hypothesis) Deploying in-house document AI that complies with the security rules at OO Precision's headquarters and 2 domestic plants in 2027-2029 can cut staff document work time and recurring design changes
- (Beneficiaries) 48 quality and design team staff, and executives
    + Staff need less time spent searching past documents and drafting reports
    + Executives need to confirm the return on AI investment
- (Upper alignment) The mid-term business plan goal "cut costs from design changes and quality defects by 20% by 2029"
- (Draft problem issues) Set from beneficiary needs and upper alignment
    + Draft 1 Excessive staff time spent searching past documents and drafting reports
    + Draft 2 Design change and quality defect costs from not checking past cases
    + Draft 3 No means of confirming the effect of AI investment

## Conditions ripe for in-house AI, assuming self-funded investment
- Macro 1. Falling AI running costs and a narrowing performance gap of open-weight models ease the cost and performance constraints of generative AI run on company servers
    + Running cost of systems performing at the GPT-3.5 level fell more than 280-fold between November 2022 and October 2024
    + On some performance evaluations, the gap between open-weight and closed models narrowed from 8% to 1.7% in one year

> (Open-weight model) An AI whose trained internal parameters are published so anyone can download and run it on their own servers

- Macro 2. The share of companies reporting AI use rose from 55% in 2023 to 78% in 2024, raising concern that companies not using AI fall behind in work efficiency

> Stanford HAI(2025), AI Index Report 2025(https://hai.stanford.edu/ai-index/2025-ai-index-report)

- Macro 3. Mid-sized companies are not among those eligible for government computing support, so OO Precision must fund its AI computing equipment itself
    + Computing support under the Ministry of Science and ICT's "Plan to Strengthen Hyperscale AI Competitiveness" (April 2023) goes to small companies, venture companies, universities and research institutes
    + As a mid-sized company, OO Precision falls outside the eligible categories

> Ministry of Science and ICT(2023), KRW 390.1 billion invested to strengthen hyperscale AI competitiveness... "accelerating the digital economy"(https://www.korea.kr/news/policyNewsView.do?newsId=148913885)

## Industry conditions that call for AI adoption that keeps documents secure
- Micro 1. Two competitors' adoption of AI for design document search in 2025 raises concern that OO Precision falls behind in the speed of using design documents
- Micro 2. Major customers' tighter checks on suppliers' technical document security from 2026 make AI that keeps technical documents in-house a requirement for keeping the business

## Internal conditions with much room for improvement under resource limits

### Operating constraints that set the scope of AI
- Internal 1. The operating path for AI that handles work documents is limited to in-house deployment in the headquarters server room
    + Company security rules forbid entering work documents into external generative AI services
    + The headquarters server room has space and power for more servers
- Internal 2. Operating staff and the investment cap set the upper limit on the scale of AI adoption
    + No one of the 5 IT team members is dedicated to AI
    + Executives set the AI investment cap for 2027-2029 at KRW 1.5 billion
- Internal 3. Design documents from before 2015 are kept on paper and excluded from AI search until digitized

### Gaps in the baselines for measuring effects
- Internal 4. The baseline for document work time rests on a single 2-week sample and needs remeasuring before effects are compared
    + In a 2-week sample in Q3 2026, past document search averaged 4.8 hours a week per staff member and drafting one report averaged 6.5 hours
    + Across the 48 staff, past document search totals 230.4 hours a week
    + No ongoing measurement beyond complaints about the time burden
    + The number of reports per staff member is unknown, so the total drafting time cannot be calculated
- Internal 5. The cost AI document search can cut directly is the share tied to design changes that recur because past cases were not checked
    + In 2025, 61 of 412 design changes (14.8%) were recurrences because past similar cases were not checked
    + The cost of the 61 recurrences is not separated within the KRW 5.9 billion of 2025 design change and quality defect costs
    + AI's share of the KRW 1.18 billion savings target in the mid-term business plan can be confirmed once recurrence costs are estimated

> (Internal data) OO Precision internal status: 2-week sample measurement in Q3 2026, 2025 cost and count actuals, executives' decision on the 2027-2029 investment cap

## Strategies derived from the gaps in the problem issues
- The gap between the current and target states is the absence of a search tool, a design change check procedure, a secure operating base and effect measurement
    + (As-is) With external AI unavailable, no in-house tool supports past document search and case checks
    + (To-be) With in-house AI supporting past document search and case checks, the effect in money is confirmed every quarter
- The means of closing the gaps are linked as preconditions for one another
    + The in-house operating base is a precondition for the search and drafting functions
    + Reducing the 61 recurrences requires combining a search tool with a mandatory check in the review procedure
    + Effect measurement is the premise for executives' stage-by-stage investment decisions

| Problem issue addressed | As-is implications | Gap | To-be measures | Strategy |
|---|---|---|---|---|
| Problem 1. Continuing document work burden on staff without an AI tool for company documents<br>(refined from draft 1) | Macro 2 AI use by 78% of companies<br>Micro 1 2 competitors adopted AI for design document search<br>Internal 4 4.8 hours of search a week per person and 6.5 hours per draft | No AI tool supporting company document search and report drafting | AI search of electronic design and quality documents from 2015 onward<br>AI drafting for recurring report types | 1. AI support for staff document work |
| Problem 2. Recurrence costs from design change reviews that do not ensure past cases are checked<br>(refined from draft 2) | Internal 3 documents before 2015 kept on paper<br>Internal 5 61 of 412 design changes recurring, recurrence costs not separated | No procedure for checking past cases in design change reviews and no way to search paper documents | Mandatory attachment of AI similar-case search results to design change reviews<br>Priority digitization of recurrence-related paper documents | 2. Preventing recurring design changes through past case checks |
| Problem 3. No in-house AI operating base that meets security requirements<br>(added on the basis of the implications) | Macro 1 falling running costs and narrowing performance gap of open-weight models<br>Macro 3 outside government computing support<br>Micro 2 tighter customer checks on technical document security<br>Internal 1 external generative AI unavailable, spare server room capacity<br>Internal 2 no dedicated AI staff, KRW 1.5 billion investment cap | No in-house AI infrastructure or operating staff meeting customers' security standards | In-house AI on open-weight models installed in the headquarters server room<br>Document access permissions and usage log management<br>2 AI operators secured in the IT team | 3. Securing a secure in-house AI operating base |
| Problem 4. No measurement standard for confirming the effect of AI investment in money<br>(refined from draft 3) | Internal 4 time baseline from a single 2-week sample<br>Internal 5 cost of the 61 recurrences not separated | No effect measurement cycle and no criteria for moving between investment stages | Quarterly effect measurement and half-yearly executive reports<br>Year-by-year investment following stage transition reviews | 4. Investment management linked to verified effects |

## A vision framework aimed at reusing design knowledge

- The aim of OO Precision's AI use is to cut costs by reusing accumulated design and quality knowledge

| Item | Top-down | Bottom-up | Final |
|---|---|---|---|
| Vision | Cut design change and quality defect costs by 20% by 2029 | Reuse of past design and quality knowledge, the common aim of the strategies | A precision manufacturer that reuses its accumulated design and quality knowledge with AI to lower design change and quality defect costs |
| Mission | Confirming cost savings in numbers | Staff need for time savings<br>Executives' need to confirm the investment effect | Deliver savings in staff document work time and cost savings executives can confirm, through secure in-house AI |
| Core values | Numerical management of the cost goal | Benefit staff can feel<br>Checking past cases<br>Customers' security requirements<br>Confirming the investment effect | Practical benefit<br>Evidence checks<br>Information protection<br>Measurement-based decisions |

- Each core value is a standard of conduct matched to one strategy
    + (Practical benefit) Use the time savings staff actually feel as the criterion for adoption decisions
    + (Evidence checks) Check past similar cases before deciding on a design change
    + (Information protection) Keep technical documents in-house and keep access logs
    + (Measurement-based decisions) Decide whether to expand investment based on measured results

## Strategic goals tied to internal baselines
- Quantitative strategic goals are set as improvement rates against internal measurements from 2025-2026 as baselines
    + The 4-week remeasurement in Q1 2027 records search time, drafting time and the number of drafts together
    + If the remeasurement differs from the sample baseline, the same improvement rates apply to the remeasured values
    + The recurrence cost baseline is fixed by classifying the costs of the 61 recurrences by Q2 2027

| Strategy no. | Strategy | Core value | Qualitative strategic goal | Quantitative strategic goal |
|---|---|---|---|---|
| 1 | AI support for staff document work | Practical benefit | AI embedded in the daily document work of quality and design team staff | Weekly past document search time per staff member from 4.8 hours (2026) to 2.88 hours or less in 2029 |
| 2 | Preventing recurring design changes through past case checks | Evidence checks | Past similar cases checked as standard practice in design change reviews | Design changes recurring because past cases were not checked from 61 (2025) to 30 or fewer in 2029 |
| 3 | Securing a secure in-house AI operating base | Information protection | Stable operation of in-house AI meeting customers' security check standards | Share of staff using in-house AI at least once a week from 0% (2026) to 90% or more in 2029 |
| 4 | Investment management linked to verified effects | Measurement-based decisions | Executives' investment decisions based on measured effects | Annual AI effect of KRW 500 million or more in 2029 |

- The size of improvement in each target is set differently by KPI to match the scope AI acts on
    + (40% less search time) Reflects that AI search covers only electronic documents from 2015 onward
    + (30% less drafting time) A lower reduction rate than search because staff still spend time reviewing technical content
    + (50% fewer recurrences) A higher reduction rate than the time KPIs because mandatory past case checks act directly on the cause of recurrence, the missing check
    + (90% use rate) A once-a-week use standard based on all staff averaging 4.8 hours of search a week
- The annual effect of KRW 500 million is the average annual spending of the KRW 1.5 billion investment cap, a benchmark for judging whether the 2029 annual effect exceeds the investment burden
    + The effect in money is the sum of hours saved multiplied by the standard hourly labor cost, plus savings in recurrence costs
    + The standard hourly labor cost uses the HR standard rate
    + Recurrence costs use the results of classifying the 61 recurrences

## Strategic tasks that close the gaps
- Each strategic task is placed to close one component of a gap

| Strategy no. | Task no. | Strategic task | Logical link |
|---|---|---|---|
| 1 | 1-1 | Introducing AI search of company documents | Closes gap 1's missing search tool to cut search time |
| 1 | 1-2 | AI drafting support for recurring reports | Closes gap 1's missing drafting tool to cut drafting time |
| 2 | 2-1 | Introducing a past case check procedure in design change reviews | Closes gap 2's missing check procedure to cut unchecked recurrences |
| 2 | 2-2 | Digitizing recurrence-related paper documents | Closes gap 2's inability to search paper documents so cases before 2015 can be checked |
| 3 | 3-1 | Building in-house AI infrastructure that meets customers' security check standards | Closes gap 3's missing infrastructure so AI runs with technical documents kept in-house |
| 3 | 3-2 | Securing AI operating staff | Closes gap 3's missing operating staff for stable operation of in-house AI |
| 4 | 4-1 | Regular measurement of AI effects | Closes gap 4's missing measurement cycle to calculate the effect in money |
| 4 | 4-2 | Stage-by-stage investment linked to verified effects | Closes gap 4's missing stage transition criteria to control spending within the investment cap |

## Implementation tasks that follow the order of verifying effects
- Implementation tasks are placed in the order baseline remeasurement, secure base installation, pilot operation, effect review and expansion
    + Tasks rated high on both necessity and urgency are baseline remeasurement, recurrence case classification, server installation, access permission management and naming operators in H1 2027
    + The internal status lists no existing AI projects, so overlap is rated low for all tasks

| Task no. | Implementation task no. | Implementation task | Necessity | Urgency | Feasibility | Timing | Prerequisite tasks |
|---|---|---|---|---|---|---|---|
| 1-1 | 1-1-1 | AI document search pilot for the design team | High | Medium | Medium | Q3-Q4 2027 | 3-1-2<br>3-2-1<br>4-1-1 |
| 1-1 | 1-1-2 | Expanding AI document search to the quality team and the 2 plants | High | Low | Medium | Q1-Q2 2028 | 4-2-1 |
| 1-2 | 1-2-1 | Applying AI drafting to recurring report types | Medium | Low | Medium | Q2-Q3 2028 | 4-1-1<br>4-2-1 |
| 2-1 | 2-1-1 | Classifying the source documents and costs of the 61 recurrences | High | High | High | Q1-Q2 2027 | None |
| 2-1 | 2-1-2 | Mandatory attachment of similar-case search results to design change reviews | High | Medium | High | Q1 2028 | 1-1-1<br>2-1-1 |
| 2-2 | 2-2-1 | Priority digitization of recurrence-related paper documents from before 2015 | Medium | Medium | High | Q3 2027-Q1 2028 | 2-1-1 |
| 3-1 | 3-1-1 | AI server installation in the headquarters server room and open-weight model setup | High | High | Medium | Q1-Q2 2027 | None |
| 3-1 | 3-1-2 | Applying document access permissions and usage log management | High | High | High | Q2 2027 | 3-1-1 |
| 3-2 | 3-2-1 | Naming 2 AI operators in the IT team and technology transfer training | High | High | Medium | Q1-Q2 2027 | None |
| 4-1 | 4-1-1 | 4-week baseline remeasurement of the 48 staff | High | High | High | Q1 2027 | None |
| 4-1 | 4-1-2 | Quarterly effect measurement and half-yearly executive reports | High | Medium | High | Q4 2027-Q4 2029 | 1-1-1 |
| 4-2 | 4-2-1 | Stage transition reviews and management of cumulative spending | High | Medium | High | December 2027 and December 2028 reviews | 4-1-2 |

- Stage transition reviews set the next year's spending scope based on the latest measurement
    + The December 2027 review approves 2028 expansion spending if the design team pilot users' search time is confirmed down 20% or more
    + The December 2028 review approves 2029 spending if search time is 3.84 hours or less and recurrences are 45 or fewer
    + If the criteria are not met, the next year's spending is limited to the tasks behind the missed KPIs

## KPI targets by level
- The central KPIs for judging 2029 performance are search time of 2.88 hours or less, 30 or fewer recurrences and an annual effect of KRW 500 million or more
- Strategy KPIs are spread evenly across the financial, customer, internal process and learning and growth perspectives
    + (Financial) 2-KPI-2 recurrence cost savings and 4-KPI-1 annual effect in money
    + (Customer) 3-KPI-2 findings in customer security checks and 4-KPI-2 executives' rating of the confirmed effect
    + (Internal process) 1-KPI-1 search time, 1-KPI-2 drafting time, 2-KPI-1 number of recurrences
    + (Learning and growth) 3-KPI-1 share of staff using it at least once a week
- Lower-level KPIs roll up by document-count weighted average for load and digitization rates, by summing items for the effect in money, and by the representative indicator method for the others
- 2-KPI-2 is an impact KPI that shows AI's contribution to the mid-term business plan's cost savings goal separately

| No. | Parent element | KPI | Type | Measurement | Target | Deadline |
|---|---|---|---|---|---|---|
| 1-KPI-1 | Mission | Weekly past document search time per staff member | Outcome | (Formula) Total search time in quarterly 2-week logs ÷ (people measured × 2 weeks) | Baseline 4.8 hours<br>2028 3.84 hours or less<br>2029 2.88 hours or less | December 2029 |
| 1-KPI-2 | Mission | Time to draft one report | Outcome | (Formula) Total drafting time in the measurement period ÷ number of drafts | Baseline 6.5 hours<br>2029 4.55 hours or less | December 2029 |
| 2-KPI-1 | Vision | Design changes recurring because past cases were not checked | Outcome | (Count) Annual total of unchecked recurrences in the design change cause classification | Baseline 61<br>2028 45 or fewer<br>2029 30 or fewer | December 2029 |
| 2-KPI-2 | Vision | Savings in recurring design change costs | Impact | (Formula) Cost of the 61 recurrences in 2025 − cost of recurrences in the given year | 50% or more of the cost of the 61 recurrences in 2025 | December 2029 |
| 3-KPI-1 | Mission | Share of staff using in-house AI at least once a week | Outcome | (Formula) Staff with usage logs at least once a week ÷ quality and design team staff × 100 | Baseline 0%<br>2028 70% or more (34 or more of 48)<br>2029 90% or more (44 or more of 48) | December 2029 |
| 3-KPI-2 | Mission | AI-related findings in customer security checks | Outcome | (Count) Annual total of findings related to in-house AI in customer check results | 0 every year | Every December 2027-2029 |
| 4-KPI-1 | Mission | Annual AI effect in money | Outcome | (Formula) (search hours saved + drafting hours saved) × standard hourly labor cost + recurrence cost savings | KRW 500 million or more in 2029 | December 2029 |
| 4-KPI-2 | Mission | Executives' rating of the confirmed investment effect | Outcome | (Scale) Average of a 5-point Likert scale for executives after each half-yearly report | 4.0 or higher | Every half year from 2028 |
| 1-1-KPI-1 | Strategy 1<br>(contributes to 1-KPI-1) | Load rate of electronic documents for AI search | Output | (Formula) Documents loaded ÷ electronic design and quality documents from 2015 onward × 100 | 100% | June 2028 |
| 1-2-KPI-1 | Strategy 1<br>(contributes to 1-KPI-2) | Share of reports using AI drafts | Output | (Formula) Reports written from AI drafts ÷ reports of the applied types × 100 | 80% or more | December 2029 |
| 2-1-KPI-1 | Strategy 2<br>(contributes to 2-KPI-1) | Share of design change reviews with similar-case search results attached | Output | (Formula) Reviews with attachments ÷ all design change reviews × 100 | 100% | June 2028 |
| 2-2-KPI-1 | Strategy 2<br>(contributes to 2-KPI-1) | Share of recurrence-related paper documents added to AI search | Output | (Formula) Documents added to search ÷ documents selected in 2-1-1 × 100 | 100% | June 2028 |
| 3-1-KPI-1 | Strategy 3<br>(contributes to 3-KPI-2) | Share of customer security check items met in advance | Output | (Formula) Items met ÷ customer check items × 100 | 100% | June 2027 |
| 3-2-KPI-1 | Strategy 3<br>(contributes to 3-KPI-1) | Number of AI operators | Output | (Count) IT team AI operators who completed job training | Baseline 0<br>2 | June 2027 |
| 4-1-KPI-1 | Strategy 4<br>(contributes to 4-KPI-1) | Share of effect calculation items measured each quarter | Output | (Formula) Items measured ÷ 4 calculation items (search time, drafting time, recurrence count, recurrence cost) × 100 | 100% every quarter | Every quarter from December 2027 |
| 4-2-KPI-1 | Strategy 4<br>(contributes to 4-KPI-2) | Share of investment stage decisions based on measured effects | Output | (Formula) Decisions based on measurements ÷ stage transition decisions × 100 | 100% | December 2028 |
| 1-1-1-KPI-1 | Task 1-1<br>(contributes to 1-1-KPI-1) | Load rate of electronic design documents | Output | (Formula) Design documents loaded ÷ electronic design documents from 2015 onward × 100 | 100% | September 2027 |
| 1-1-2-KPI-1 | Task 1-1<br>(contributes to 1-1-KPI-1) | Load rate of electronic quality documents | Output | (Formula) Quality documents loaded ÷ electronic quality documents from 2015 onward × 100 | 100% | June 2028 |
| 1-2-1-KPI-1 | Task 1-2<br>(contributes to 1-2-KPI-1) | Share of report types with AI draft templates | Output | (Formula) Types with templates ÷ recurring report types identified in 4-1-1 × 100 | 100% | September 2028 |
| 2-1-1-KPI-1 | Task 2-1<br>(contributes to 2-1-KPI-1) | Completion rate of classifying source documents and costs of the 61 recurrences | Process | (Formula) Cases classified ÷ 61 × 100 | 100% | June 2027 |
| 2-1-2-KPI-1 | Task 2-1<br>(contributes to 2-1-KPI-1) | Review form with a similar-case search item in effect | Output | (Count) Whether the revised form is in effect | In effect | March 2028 |
| 2-2-1-KPI-1 | Task 2-2<br>(contributes to 2-2-KPI-1) | Digitization rate of recurrence-related paper documents | Output | (Formula) Documents digitized ÷ documents selected in 2-1-1 × 100 | 100% | March 2028 |
| 3-1-1-KPI-1 | Task 3-1<br>(contributes to 3-1-KPI-1) | AI server and open-weight model installed | Output | (Count) Whether installation and test operation in the headquarters server room are complete | Complete | June 2027 |
| 3-1-2-KPI-1 | Task 3-1<br>(contributes to 3-1-KPI-1) | Share of documents under access permission and usage log management | Output | (Formula) Documents under permission and log management ÷ documents loaded into AI × 100 | 100% | June 2027 |
| 3-2-1-KPI-1 | Task 3-2<br>(contributes to 3-2-KPI-1) | Completion rate of technology transfer training | Process | (Formula) Operators who completed training ÷ 2 named operators × 100 | 100% | June 2027 |
| 4-1-1-KPI-1 | Task 4-1<br>(contributes to 4-1-KPI-1) | Participation rate in the baseline remeasurement | Process | (Formula) Staff taking part in the 4-week measurement ÷ 48 × 100 | 90% or more | March 2027 |
| 4-1-2-KPI-1 | Task 4-1<br>(contributes to 4-1-KPI-1) | Number of quarterly effect measurements | Process | (Count) Cumulative quarterly measurements from Q4 2027 | 9 | December 2029 |
| 4-2-1-KPI-1 | Task 4-2<br>(contributes to 4-2-KPI-1) | Number of stage transition reviews held | Process | (Count) Cumulative stage transition reviews held | 2 | December 2028 |
| 4-2-1-KPI-2 | Task 4-2<br>(contributes to 4-2-KPI-1) | Cumulative AI investment spending | Input | (Count) Cumulative AI investment spent from 2027 | Within KRW 1.5 billion | December 2029 |

## OO Precision AI vision house
- Strategy 3's secure in-house AI operating base is a precondition for strategies 1 and 2
- Strategy 4's effect measurements decide the scope of investment each year

| Item | Details |
|---|---|
| Vision | A precision manufacturer that reuses its accumulated design and quality knowledge with AI to lower design change and quality defect costs |
| Mission | Deliver savings in staff document work time and cost savings executives can confirm, through secure in-house AI |
| Core values | Practical benefit, evidence checks, information protection, measurement-based decisions |

### Strategy 1 AI support for staff document work

| Item | Details |
|---|---|
| Core value | Practical benefit |
| Qualitative strategic goal | AI embedded in the daily document work of quality and design team staff |
| Quantitative strategic goal | Weekly past document search time per staff member from 4.8 hours to 2.88 hours or less in 2029 |
| Strategy KPIs | 1-KPI-1 Weekly past document search time per staff member<br>1-KPI-2 Time to draft one report |

- Design team pilot in 2027, then expansion to the quality team and the 2 plants in 2028

| Strategic task | Implementation task | Key KPIs |
|---|---|---|
| 1-1. Introducing AI search of company documents | 1-1-1. AI document search pilot for the design team<br>1-1-2. Expanding AI document search to the quality team and the 2 plants | 1-1-KPI-1 Load rate of electronic documents for AI search<br>1-1-1-KPI-1 Load rate of electronic design documents<br>1-1-2-KPI-1 Load rate of electronic quality documents |
| 1-2. AI drafting support for recurring reports | 1-2-1. Applying AI drafting to recurring report types | 1-2-KPI-1 Share of reports using AI drafts<br>1-2-1-KPI-1 Share of report types with AI draft templates |

### Strategy 2 Preventing recurring design changes through past case checks

| Item | Details |
|---|---|
| Core value | Evidence checks |
| Qualitative strategic goal | Past similar cases checked as standard practice in design change reviews |
| Quantitative strategic goal | Design changes recurring because past cases were not checked from 61 to 30 or fewer in 2029 |
| Strategy KPIs | 2-KPI-1 Design changes recurring because past cases were not checked<br>2-KPI-2 Savings in recurring design change costs |

- Classifying the source documents of the 61 recurrences fixes the digitization targets and the scope of the check procedure

| Strategic task | Implementation task | Key KPIs |
|---|---|---|
| 2-1. Introducing a past case check procedure in design change reviews | 2-1-1. Classifying the source documents and costs of the 61 recurrences<br>2-1-2. Mandatory attachment of similar-case search results to design change reviews | 2-1-KPI-1 Share of design change reviews with similar-case search results attached<br>2-1-1-KPI-1 Completion rate of classifying source documents and costs of the 61 recurrences<br>2-1-2-KPI-1 Review form with a similar-case search item in effect |
| 2-2. Digitizing recurrence-related paper documents | 2-2-1. Priority digitization of recurrence-related paper documents from before 2015 | 2-2-KPI-1 Share of recurrence-related paper documents added to AI search<br>2-2-1-KPI-1 Digitization rate of recurrence-related paper documents |

### Strategy 3 Securing a secure in-house AI operating base

| Item | Details |
|---|---|
| Core value | Information protection |
| Qualitative strategic goal | Stable operation of in-house AI meeting customers' security check standards |
| Quantitative strategic goal | Share of staff using in-house AI at least once a week from 0% to 90% or more in 2029 |
| Strategy KPIs | 3-KPI-1 Share of staff using in-house AI at least once a week<br>3-KPI-2 AI-related findings in customer security checks |

- Installation completed in H1 2027 sets up the pilot conditions for strategies 1 and 2

| Strategic task | Implementation task | Key KPIs |
|---|---|---|
| 3-1. Building in-house AI infrastructure that meets customers' security check standards | 3-1-1. AI server installation in the headquarters server room and open-weight model setup<br>3-1-2. Applying document access permissions and usage log management | 3-1-KPI-1 Share of customer security check items met in advance<br>3-1-1-KPI-1 AI server and open-weight model installed<br>3-1-2-KPI-1 Share of documents under access permission and usage log management |
| 3-2. Securing AI operating staff | 3-2-1. Naming 2 AI operators in the IT team and technology transfer training | 3-2-KPI-1 Number of AI operators<br>3-2-1-KPI-1 Completion rate of technology transfer training |

### Strategy 4 Investment management linked to verified effects

| Item | Details |
|---|---|
| Core value | Measurement-based decisions |
| Qualitative strategic goal | Executives' investment decisions based on measured effects |
| Quantitative strategic goal | Annual AI effect of KRW 500 million or more in 2029 |
| Strategy KPIs | 4-KPI-1 Annual AI effect in money<br>4-KPI-2 Executives' rating of the confirmed investment effect |

- The December 2027 and December 2028 reviews decide the next year's spending scope

| Strategic task | Implementation task | Key KPIs |
|---|---|---|
| 4-1. Regular measurement of AI effects | 4-1-1. 4-week baseline remeasurement of the 48 staff<br>4-1-2. Quarterly effect measurement and half-yearly executive reports | 4-1-KPI-1 Share of effect calculation items measured each quarter<br>4-1-1-KPI-1 Participation rate in the baseline remeasurement<br>4-1-2-KPI-1 Number of quarterly effect measurements |
| 4-2. Stage-by-stage investment linked to verified effects | 4-2-1. Stage transition reviews and management of cumulative spending | 4-2-KPI-1 Share of investment stage decisions based on measured effects<br>4-2-1-KPI-1 Number of stage transition reviews held<br>4-2-1-KPI-2 Cumulative AI investment spending |
