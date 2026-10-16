# OO Precision AI strategy framework (2027-2029)

## Executive summary

- **What we do**: We keep the security rule that forbids external generative AI as it is. We run an in-house AI built on open-weight models in the headquarters server room and use it first for design and quality document search and report drafting.
- **What we get (2029)**: Search time per staff member from 4.8 to 2.4 hours a week, one report draft from 6.5 to 3.9 hours, and repeat design changes caused by not checking past cases from 61 to 30 or fewer.
- **Link to the parent goal**: AI alone cannot deliver the 20% cost cut (KRW 1.18 billion). Even removing all 61 repeats yields at most KRW 870 million at the average design change cost. AI takes on part of the parent goal (26.3% of the 2029 savings target under the assumptions), and other tasks such as quality defect measures must cover the rest.
- **How we spend**: We do not spend the KRW 1.5 billion at once. Short term KRW 400 million, mid term KRW 550 million and long term KRW 350 million, plus a KRW 200 million reserve, with each year-end deciding the next stage by the KPIs (2 investment gates).
- **Return on investment**: Under the assumptions (KRW 40,000 hourly labor cost and others), cumulative benefit divided by cumulative spending reaches 0.80-0.93 by 2029, with payback in 2030. These assumptions must be replaced with Q1 2027 measurements.

## 1. Reading the input and assumptions

### How each input item is applied

| Item | Input | Applied as |
|---|---|---|
| Hypothesis | OO Precision, headquarters and 2 plants, 2027-2029 | AI servers at headquarters, the 2 plants connect over the internal network. 3-year period |
| Beneficiaries | Staff, executives | Staff link to strategic goal 1, executives to strategic goal 2 |
| Upper alignment | 20% cost cut | KRW 5.9 billion → KRW 4.72 billion (assuming 2025 as the base). Linked to strategic goal 2 and the financial KPI |
| Draft issues | Auto | 5 draft issues derived from the internal status (chapter 4) |
| External environment | Free input | 4 macro and 2 micro items summarized as implications (chapter 2) |
| Internal status | Free input | Summarized as baselines, strengths and weaknesses (chapter 3) |
| Benchmarking | Skip | Not done. Only the micro-environment items are used for competitor information |
| Analysis tool | SWOT | Chapter 5 |
| SWOT mode | Fixed | 3 per quadrant, fixed at 12 in total |
| SWOT follow-up | Y | 8 SO, ST, WO and WT cross strategies (chapter 6) |
| Issue confirmation | Refine | 5 drafts grouped by cause into 4 confirmed issues (chapter 7) |
| Strategy type | Standard | Vision → strategic goals → strategies → strategic tasks → KPIs |
| Strategic goal | Dual | 2 goals (work efficiency, business results), each with a qualitative statement and a quantitative target |
| Strategic tasks | Auto-derive | 1 strategic task per cross strategy, 8 in total |
| Implementation tasks | Skip | No detailed implementation tasks, only the end point of each stage |
| KPIs | Strategy level | 9 KPIs at the strategic goal and task level plus 1 KPI shared with the parent goal |
| KPI track | BSC | Financial, customer, internal process, learning and growth |
| Time format | Short, mid and long term | Short term 2027, mid term 2028, long term 2029 |
| Check method | Script | Calculations, links, budget and figures in the document checked by script (chapter 12) |

### Premises and assumptions

| Area | Content | Used in |
|---|---|---|
| Base year of the parent goal | 2025 actual of KRW 5.9 billion taken as the base | Strategic goal 2, financial KPI |
| Reading of the internal status | It says both "no measurement" and "2-week sample measurement," so I took it that there is no ongoing measurement, only one 2-week sample in Q3 2026 | Baselines, weakness W3 |
| Working weeks per year | 46 weeks | Time conversion |
| Hourly labor cost | KRW 40,000 | Return on investment (chapter 11) |
| Report drafts per person per year | 24 (2 a month) | Return on investment |
| Cost of one repeat design change | KRW 10 million. Even if all KRW 5.9 billion were design change cost, the average could not exceed KRW 14.32 million per case, so a lower figure is used | Return on investment |
| Labor cost treatment | Pay for newly hired AI staff is outside the KRW 1.5 billion cap (HR budget) | Budget |

## 2. External environment analysis

### Macro environment

| Code | Fact (source) | Meaning for OO Precision | SWOT |
|---|---|---|---|
| M1 | Inference cost of a GPT-3.5-level system fell more than 280-fold between November 2022 and October 2024 (Stanford HAI, 2025) | The burden of running models in-house is falling fast. An in-house build within the KRW 1.5 billion cap becomes a realistic option. | O1 |
| M2 | Performance gap between open-weight and closed models on some benchmarks narrowed from 8% to 1.7% in one year (same report) | Even without external services, an in-house model gives up little performance. Benchmark scores do not guarantee performance on company document work, though, so the pilot must check it. | O2 |
| M3 | Companies reporting AI use rose from 55% in 2023 to 78% in 2024 (same report) | AI use is becoming the industry default. The later we start, the wider the gap. | T1 |
| M4 | Ministry of Science and ICT "Plan to Strengthen Hyperscale AI Competitiveness" (April 2023). Computing support goes to small and venture companies, universities and research institutes. 200 kinds of training data and 130 Korean corpora by 2027 | As a mid-sized company, OO Precision is not eligible for computing support and must invest on its own (T3). Public data and corpora can strengthen Korean performance, subject to their release terms (O3). | T3, O3 |

### Micro environment

| Code | Fact | Meaning for OO Precision | SWOT |
|---|---|---|---|
| m1 | Two competitors in the same industry adopted AI for design document search in 2025 | Starting in 2027 puts us 2 years behind. A design team pilot must show results quickly from the first year. | T1 |
| m2 | Major customers tightened checks on suppliers' technical document security from 2026 | If AI becomes a leak path for technical documents, it puts business at risk. Conversely, an in-house build with permission and usage log management gives grounds for passing those checks. | T2 |

Sources: Stanford HAI(2025), AI Index Report 2025 / Ministry of Science and ICT(2023), KRW 390.1 billion invested to strengthen hyperscale AI competitiveness... "accelerating the digital economy" (korea.kr)

## 3. Internal status analysis

| Item | Status | Reading | SWOT |
|---|---|---|---|
| Security rules | No work documents into external generative AI | Commercial AI services cannot be used right away. An in-house build is effectively the only route. | W1 |
| Measurement | No ongoing measurement, one 2-week sample in Q3 2026 | There is a baseline, but the sample period is short and reports per person are missing. | S3, W3 |
| Staff | IT team of 5, 0 dedicated to AI | No one to build and run it. | W2 |
| Documents | Electronic files from 2015, paper before that | Over 10 years of electronic documents can be searched right away. Paper documents are left out of search. | S2, W3 |
| Infrastructure | Space and power for more servers in the headquarters server room | In-house GPU servers can be installed. | S1 |
| Target size | 48 quality and design staff | People covered by the strategy | - |
| Time baselines | Search 4.8 hours a week per person, report draft 6.5 hours each | Across the 48 staff, search alone takes 230.4 hours a week. That is 5.8 people at 40 hours a week, or 10,598 hours over 46 weeks a year. | S3 |
| Cost and repeats | 2025 cost KRW 5.9 billion. 61 of 412 design changes were repeats from not checking similar past cases (14.8%) | The cause of the repeats is pinned to "similar past cases not checked," which links directly to AI search. | S3 |
| Investment cap | KRW 1.5 billion for 2027-2029 | Executive commitment is confirmed, and so is the demand to prove the effect. | S3 |

**Data gaps**: report drafts per person, the split of the KRW 5.9 billion into design changes and quality defects, the cost of the 61 repeats, quality defect counts and repeats, and the makeup of the 48 staff by team and site. Task 3-2 fills these gaps in Q1 2027.

## 4. Draft issues (auto)

| Draft | Problem | Basis |
|---|---|---|
| D1 | Searching past documents takes a lot of time | 4.8 hours a week per person |
| D2 | Drafting reports takes a lot of time | 6.5 hours each |
| D3 | Design changes repeat because similar past cases are not checked | 61 of 412 |
| D4 | External AI cannot be used and there are no AI staff | Security rules, 0 dedicated to AI |
| D5 | There is no system to measure the effect | No ongoing measurement |

## 5. SWOT analysis (fixed, 3 per quadrant)

| | Positive | Negative |
|---|---|---|
| **Internal** | **Strengths (S)**<br>S1 Space and power for more servers in the headquarters server room<br>S2 Design documents kept electronically since 2015 (over 10 years of records)<br>S3 KRW 1.5 billion investment cap set, with quantitative baselines (search 4.8 hours, drafts 6.5 hours, 61 repeats) | **Weaknesses (W)**<br>W1 No work documents into external generative AI<br>W2 IT team of 5, 0 dedicated to AI<br>W3 Paper documents before 2015, no ongoing measurement or cost breakdown |
| **External** | **Opportunities (O)**<br>O1 Inference cost down more than 280-fold<br>O2 Gap between open-weight and closed models 8% → 1.7%<br>O3 Government building 200 kinds of training data and 130 Korean corpora (by 2027) | **Threats (T)**<br>T1 2 competitors adopted (2025), 78% of companies use AI<br>T2 Customers tightening checks on suppliers' technical document security (from 2026)<br>T3 Mid-sized companies left out of government computing support, so self-investment is needed |

## 6. SWOT follow-up: cross strategies

| Type | Code | Combination | Cross strategy | Task derived |
|---|---|---|---|---|
| SO | SO1 | S1·O1·O2 | Install open-weight models in the spare server room space and use cheaper AI within the security rules | 1-1 |
| SO | SO2 | S2·O2 | Put electronic design documents from 2015 onward into AI search first to show effects in the first year | 2-1 |
| ST | ST1 | S1·T2 | Add document permission and usage log management to the in-house build as grounds for passing customer security checks | 1-2 |
| ST | ST2 | S3·T1 | Use the 61 repeats with a known cause as the baseline, add similar-case lookup to design change review, and close the gap with competitors through results | 2-2 |
| WO | WO1 | W1·O2·O3 | Draft reports with in-house models and public Korean data instead of external services | 2-4 |
| WO | WO2 | W2·O1·O2 | Building on models becoming easier and cheaper to use, go with an external build partner and a small dedicated team | 3-1 |
| WO | WO3 | W3·O1 | With the cost of reading and indexing scanned documents falling along with AI processing costs, digitize only the paper documents for product lines at risk of repeats | 2-3 |
| WT | WT1 | W3·T3 | With no government support to count on, build the measurement system first and spend the KRW 1.5 billion gate by gate | 3-2 |

## 7. Confirmed issues (refined)

Checking the drafts against the SWOT results led to four changes.

- D1 and D3 are merged. Search time is a symptom and repeats are a result, and both come from the same cause: "there is no route to the knowledge."
- D4 is redefined as "security and staffing constraints," adding the external threat (tighter customer security checks).
- D5 is redefined as "the investment effect cannot be proven," adding the executive demand and the KRW 1.5 billion cap.
- Each issue now has supporting figures and a link to the parent goal, and the issues are ranked.

| Confirmed issue | Definition | Supporting figures | Drafts | Link to parent goal | Priority | Tasks |
|---|---|---|---|---|---|---|
| I-1 | Company knowledge cannot be searched, so the same design problems repeat | 61 repeats (14.8%), 230.4 search hours a week, paper documents before 2015 | D1, D3 | Direct (design change cost) | 1 | 2-1, 2-2, 2-3 |
| I-2 | Report drafting ties up experienced staff time | 6.5 hours each | D2 | Indirect (frees review time) | 3 | 2-4 |
| I-3 | Security rules and staffing leave no route to use AI | External AI banned, 0 dedicated to AI, tighter customer checks | D4 | Precondition | 2 | 1-1, 1-2, 3-1 |
| I-4 | There is no measurement system to prove the investment effect | No ongoing measurement, no breakdown of KRW 5.9 billion, KRW 1.5 billion cap | D5 | Basis for executive decisions | 2 | 3-2 |

## 8. Strategy framework (standard)

### Strategy framework chart

```
Vision        OO Precision never hits the same problem twice
              - reuse accumulated design and quality knowledge with AI

Strategic     [1] Work efficiency: halve search time, cut report drafting time by 40%
goals         [2] Business results: halve repeat design changes or better, prove the investment effect in numbers

Strategy 1  In-house AI base that works within security
  ├ 1-1  Build an in-house generative AI platform
  └ 1-2  Set up AI security and data management
Strategy 2  Prevent repeats and save time by reusing knowledge
  ├ 2-1  AI search service for design and quality documents
  ├ 2-2  Built-in similar-case lookup in design change review
  ├ 2-3  Selective digitization of paper documents for product lines at risk of repeats
  └ 2-4  Report drafting support
Strategy 3  Operations that prove results
  ├ 3-1  AI operations staff and staff capability
  └ 3-2  Impact measurement and staged investment gates

KPIs (BSC)  Financial F1 / Customer C1·C2·C3 / Internal process P1·P2·P3 / Learning and growth L1·L2
```

### Strategic goals (dual)

| Goal | Qualitative goal | Quantitative goal (2029) | Baseline | Beneficiary |
|---|---|---|---|---|
| Goal 1. Work efficiency | Design and quality staff spend less time finding documents and drafting, and put that time into review and improvement | Search 2.4 hours a week per person (50% less), drafts 3.9 hours each (40% less) | 4.8 hours, 6.5 hours | Quality and design staff |
| Goal 2. Business results | Fewer repeats by building past-case checks into the design change process, and the investment effect shown in numbers | 30 or fewer repeat design changes (cut by 50% or more), investment benefit ratio of 0.7 or more | 61, 0 | Executives (including the parent goal) |

The basis for the reductions is as follows. Search is work AI takes over directly, so it is set at 50%. Drafts still need human review and editing, so they are set lower at 40%. Repeats have a known cause, "similar cases not checked," and task 2-2 makes the lookup mandatory, so they are set at 50%. Cases buried in paper documents can be found only after the 2-3 digitization is done, so no more than that is expected.

### Strategies and strategic tasks (auto-derived)

| Task | Content | Derived from | Issue solved | KPI |
|---|---|---|---|---|
| 1-1 Build an in-house generative AI platform | Put GPU servers in the headquarters server room and connect open-weight language models and a document search engine to the internal network only. The 2 plants use it over the internal network. Choose models by comparing them on a set of in-house queries, such as questions about the 61 repeats, and check commercial use terms. Design the setup so a better model can replace it later. | SO1 | I-3 | L2 |
| 1-2 Set up AI security and data management | Set the AI search scope by document security grade, apply existing document permissions to search results as they are, and keep query and viewing logs. Treat customers' technical documents as a separate grade after checking whether contracts allow it. Document it in a form that can be submitted at customer checks. | ST1 | I-3 | C3 |
| 2-1 AI search service for design and quality documents | Index electronic design documents from 2015 onward first. Show the source document and location with every answer so staff can check right away. Expand from the design team to the quality team (defect analysis and corrective action documents) and then the 2 plants. | SO2 | I-1 | C1, P1 |
| 2-2 Built-in similar-case lookup in design change review | Analyze the 61 repeats first to set lookup criteria for which cases should have been found. Add an "AI similar-case lookup result" item to the design change review form, recommended in 2027 and mandatory in 2028. | ST2 | I-1 | P1, P2 |
| 2-3 Selective digitization of paper documents for product lines at risk of repeats | Rather than scanning all paper documents from before 2015, scan and OCR only the product and part lines related to repeat cases and add them to search. The targets are fixed in Q1 2027. | WO3 | I-1 | C1, P3 |
| 2-4 Report drafting support | Pick frequently used report templates. AI finds related past documents and drafts, and the author reviews and edits. Sources must be shown in drafts, and submitting an AI draft as is is forbidden. | WO1 | I-2 | C2 |
| 3-1 AI operations staff and staff capability | In 2027, move 1 IT team member to AI operations and hire 1, then hire 1 more in 2028. A partner does the build, with transfer of operating know-how written into the contract. Name and train usage leads in the design team, quality team and the 2 plants. | WO2 | I-3 | L1, L2 |
| 3-2 Impact measurement and staged investment gates | In Q1 2027, remeasure the baseline with the same 2-week sample method and also survey reports per person. Split the KRW 5.9 billion into design changes and quality defects and cost the repeats to fix the benefit criteria. Measure every October and hold the gate review in December. | WT1 | I-4 | F1 |

## 9. Short, mid and long-term roadmap and investment gates

| Stage | Focus | Key milestones | Budget (rough) |
|---|---|---|---|
| Short term (2027) | Build the base and pilot with the design team | Q1: remeasure baselines and split costs, set security rules, analyze the 61 repeats, pick digitization targets / Q2: build servers and models, design team search pilot / Q3: report drafting pilot / October: first performance measurement | KRW 400 million |
| Mid term (2028) | Spread to the quality team and the 2 plants | Expand search to the quality team and plants, make the lookup item mandatory in design change reviews, more draft templates, 70% of paper documents digitized | KRW 550 million |
| Long term (2029) | Settle in and prove results | Lookup established for all design changes, digitization complete, extend to quality defect reviews, decide on investment from 2030 | KRW 350 million |
| Reserve | Only when a gate is passed | Server expansion as usage grows, wider scope | KRW 200 million |

The budget is a rough split before quotes and will be fixed with quotes in Q1 2027. The total equals the cap, KRW 1.5 billion.

| Gate | When | Pass criteria (that year's targets) | If passed | If not |
|---|---|---|---|---|
| Gate 1 | December 2027 | C1 4.3 hours or less, C3 0 cases, L2 30% or more | Release mid-term KRW 550 million | Analyze the cause, narrow or redesign the rollout, hold back part of the mid-term budget |
| Gate 2 | December 2028 | P1 42 or fewer, F1 0.4 or more, L2 70% or more | Release long-term KRW 350 million, consider using the KRW 200 million reserve | Release only the long-term budget needed to keep operations running, reserve unused |

## 10. KPIs (strategy level, BSC)

**Target-setting rules**

- Reduction KPIs multiply the baseline by (1 − reduction rate) and round down, which guarantees at least the reduction rate. Example: 61 repeats × 0.9 = 54.9 → 54.
- Reduction rates are 10% in the short term (pilot), 30% in the mid term (rollout) and 50% (search and repeats) or 40% (drafts) in the long term.
- Time KPIs are remeasured every October with the same 2-week sample method as the baseline, as the average across all 48 staff.
- "Customer" in the BSC covers both internal customers (staff) and external customers.

| Perspective | Code | KPI | Formula and measurement | Baseline | Short (2027) | Mid (2028) | Long (2029) | Link |
|---|---|---|---|---|---|---|---|---|
| Financial | F1 | AI investment benefit ratio | Cumulative benefit (time savings value + repeat costs avoided) ÷ cumulative AI spending | 0 (before investment) | Benefit criteria set, executive approval | 0.4 or more | 0.7 or more | Goal 2, 3-2 |
| Financial (reference) | Shared | Cost of design changes and quality defects (shared with the parent goal) | Accounting totals | KRW 5.9 billion (2025) | Annual target of the mid-term plan | Annual target of the mid-term plan | KRW 4.72 billion or less | Parent goal, AI contributes |
| Customer | C1 | Weekly past document search time per staff member | 2-week sample, average of 48 | 4.8 hours | 4.3 hours | 3.3 hours | 2.4 hours | Goal 1, 2-1·2-3 |
| Customer | C2 | Time to draft one report | 2-week sample, average per report | 6.5 hours | 5.8 hours | 4.5 hours | 3.9 hours | Goal 1, 2-4 |
| Customer | C3 | AI-related findings in customer security checks | Customer check results | None (no AI yet) | 0 | 0 | 0 | 1-2 |
| Internal process | P1 | Repeat design changes from similar cases not checked | Cause classification of design changes | 61 (2025) | 54 or fewer | 42 or fewer | 30 or fewer | Goal 2, 2-1·2-2 |
| Internal process | P2 | Rate of AI similar-case lookup in design change reviews | Changes with lookup results attached ÷ all design changes | 0% | 50% | 80% | 95% | 2-2 |
| Internal process | P3 | Digitization rate of paper documents for at-risk product lines | Documents done ÷ targets set in Q1 2027 | 0% | 30% | 70% | 100% | 2-3 |
| Learning and growth | L1 | Dedicated AI and operations staff | Headcount | 0 | 2 | 3 | 3 | 3-1 |
| Learning and growth | L2 | Monthly usage rate among staff | Users at least once a month ÷ 48 | 0% | 30% (15) | 70% (34) | 90% (44) | 1-1, 3-1 |

**Causal chain between KPIs**: Staff and usage (L1, L2) → lookup and digitization (P2, P3) → fewer repeats (P1) and time savings (C1, C2) → investment benefit (F1) and the parent cost KPI. If F1 falls short at a gate review, trace this chain backward to find where it stalled.

**Caution**: The P1 baseline is the 2025 actual. When the 2026 actual comes out in early 2027, recheck the baseline against it.

## 11. Return on investment (for executives)

Assumptions: 46 weeks a year, KRW 40,000 hourly labor cost, 24 drafts per person a year, KRW 10 million per repeat, reserve unused. Each year's target is treated as met for the whole year, so the figures may run somewhat higher than reality.

| Stage | Hours saved | Time value (KRW million) | Repeats avoided | Cost avoided (KRW million) | Annual benefit (KRW million) | Cumulative benefit (KRW million) | Cumulative spending (KRW million) | Benefit ratio |
|---|---|---|---|---|---|---|---|---|
| Short term (2027) | 1,910.4 hours | 76 | 7 | 70 | 146 | 146 | 400 | 0.37 |
| Mid term (2028) | 5,616.0 hours | 225 | 19 | 190 | 415 | 561 | 950 | 0.59 |
| Long term (2029) | 8,294.4 hours | 332 | 31 | 310 | 642 | 1,203 | 1,300 | 0.93 |

How to read it:

- The 2029 cumulative ratio is 0.93 with the reserve unused and 0.80 if the KRW 200 million reserve is spent. Both clear the 0.7 target with room to spare.
- If only 70% of the benefit materializes, the ratio is 0.65 with the reserve unused, below the target. That is why gate 2 ties use of the reserve to results.
- Time savings are not cash. Counting only the cash-like benefit of avoided repeats gives 0.44. Executives will be convinced only if the report also shows where the freed time went (for example, stronger design review).
- For F1 to reach 0.7, a repeat must cost at least KRW 4.86 million (reserve unused) to KRW 7.32 million (reserve used). I recommend checking this value first in the Q1 2027 cost breakdown.
- The KRW 310 million of repeat costs avoided in 2029 is 26.3% of the parent goal's KRW 1.18 billion savings.
- If the 2029 annual benefit of KRW 642 million continues and 2030 operating costs stay at KRW 345 million or less, cumulative benefit passes KRW 1.5 billion within 2030 and the investment pays back.

## 12. Script check results

The strategy framework's figures and links were entered as data into `check_strategy.py` and checked. All 91 items passed.

| Area | What was checked | Result |
|---|---|---|
| A Baseline arithmetic | 230.4 hours, 14.8%, KRW 1.18 billion, KRW 4.72 billion, upper bound if all 61 repeats were removed | All 5 passed |
| B Targets | Round-down rule for reductions, consistent direction across short, mid and long term, 3 time points defined | All 21 passed |
| C SWOT | 3 per quadrant, all 12 items used in cross strategies, cross types match combinations | All 14 passed |
| D Links | All 8 tasks derived from cross strategies, issue-task, task-KPI, goal-KPI, beneficiary-goal, 4 BSC perspectives | All 12 passed |
| E Budget and gates | Stage budgets and reserve total KRW 1.5 billion, gate criteria equal that year's targets | All 3 passed |
| F Investment effect | F1 mid and long-term targets fall within the assumed scenarios | Both passed |
| G Document check | This reply contains the key calculated values, the 9 KPI rows and the 8 tasks as they are | All 34 passed |

Some things the script cannot confirm. Whether the assumptions (labor cost, report counts, cost per repeat) are right, whether the external environment figures match their sources, and whether the reduction rates are appropriate are matters of judgment that a person needs to review.

- Script: `check_strategy.py`
- Check results: `check_result.txt`
- Rerun: `python3 check_strategy.py reply.md` (after replacing the assumptions with measured values, it recalculates the investment effect and the adequacy of the targets)

## 13. Items to confirm

Once the values below are set, I will recalculate the return on investment in chapter 11 and the F1 targets.

1. Report drafts per staff member per year (now assumed at 24)
2. Hourly labor cost (now assumed at KRW 40,000)
3. The share of design changes and quality defects in the KRW 5.9 billion, and the cost of the 61 repeats (now assumed at KRW 10 million each)
4. Base year of the parent goal "20% cut" (now assumed to be 2025)
5. Whether pay for dedicated AI staff falls within the KRW 1.5 billion cap (now assumed outside it)
6. Makeup of the 48 staff by team and site (needed to set the design team pilot scope)
7. Quality defect counts and repeat data (if available, a quality-side repeat KPI would be added next to P1)
8. Reading of the input: "SWOT fixed" was read as 3 per quadrant, and "dual strategic goals" as 2 goals each with a qualitative and a quantitative target. Let me know if you meant otherwise.
