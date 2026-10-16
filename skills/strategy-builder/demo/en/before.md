# OO Precision AI Strategy Framework (2027–2029)

## Key points

1. **The way AI contributes directly to the company's cost goal is by preventing "design changes that recur because past cases were not checked."** In 2025, 61 of 412 design changes (14.8%) were of this kind. The first goal is to halve this rate (to 7.4%) by 2029.
2. **External generative AI cannot be used, so we will build on company servers with open-weight models.** Company security rules and customers' tighter security checks point the same way, and the narrowing performance gap of open models supports this choice.
3. **Of the KRW 1.5 billion investment cap, only a base KRW 1.01 billion is committed.** The remaining KRW 490 million is spent only after results are confirmed. The only spending committed before the first gate (June 2027) is the KRW 50 million PoC.
4. **AI alone cannot deliver the full "20% cost cut."** If a recurrence costs about as much as an average design change, halving recurrences saves at most about KRW 440 million a year, about 38% of the KRW 1.18 billion savings target. The rest has to come from tasks other than AI.
5. **This program does not pay back within 3 years on cost savings alone.** The payback point depends on the cost of one recurrence, which is not yet known. So the plan estimates that value first in Q1 2027 and reconsiders the investment at the first gate.

---

## 1. Strategy framework at a glance

| Item | Details |
|---|---|
| **Vision** | A company where anyone can safely find and use its accumulated design and quality experience |
| **Linked goal** | Company mid-term business plan: cut design change and quality defect costs by 20% by 2029 (KRW 5.9 billion → KRW 4.72 billion) |
| **Strategic goal 1** | Fewer repeats of the same problem: recurring design change rate 14.8% → 7.4% or less |
| **Strategic goal 2** | Give staff their time back: weekly document search 4.8 hours → 2.4 hours, one report draft 6.5 hours → 3.9 hours |
| **Strategic goal 3** | Invest safely and with verification: 0 security incidents, 90% weekly use, investment only in stages that pass the performance gates |
| **Principles** | ① In-house build: documents never leave the company ② Measure, then invest: baselines and gate results open the next stage's budget ③ Build it into the workflow: add a similar-case check to the design change procedure, not just a tool ④ Build outside, run inside: buy the solution, keep operating capability in-house |
| **Tasks** | A performance measurement base · B in-house AI document search · C design change procedure integration · D report drafting support · E document data cleanup · F in-house infrastructure and security · G operating organization, guidelines and training · H rollout to other departments (conditional) |

---

## 2. Environment analysis and implications

### External environment

| Fact | What it means for OO Precision |
|---|---|
| Inference cost of GPT-3.5-level AI fell more than 280-fold between November 2022 and October 2024 (Stanford HAI, 2025) | AI is now affordable for a mid-sized company. This figure is based on API prices, though. On-premises server costs need to be checked separately with supplier quotes. |
| Performance gap between open-weight and closed models on some benchmarks narrowed from 8% to 1.7% in one year (same report) | Building an open model in-house has become a realistic option even under the constraint of not using external services. As this is from some benchmarks, performance on Korean technical documents needs to be checked in a PoC. |
| Share of companies reporting AI use rose from 55% in 2023 to 78% in 2024 (same report) | Adoption alone no longer sets a company apart. Showing the effect in numbers is what matters. As this covers responding companies worldwide, it was not applied directly to Korean mid-sized manufacturers. |
| Ministry of Science and ICT "Plan to Strengthen Hyperscale AI Competitiveness" (April 2023): computing support goes to small and venture companies, universities and research institutes, and 200 kinds of training data and 130 Korean-language corpora are to be built by 2027 | Mid-sized companies are not eligible for computing support, so it was not included in the budget. Korean corpora indirectly help improve open models' Korean quality. As this was announced in 2023, support programs for mid-sized companies as of 2027 need to be checked separately. |
| 2 competitors in the same industry adopted AI for design document search in 2025 | A gap in document search speed may open. As the competitors' results are unknown, we proceed by verifying with our own figures rather than copying them. |
| Major customers tightened checks on suppliers' technical document security from 2026 | External AI is blocked by both the rules and customer requirements. An in-house build with access logs gives evidence for customer checks. Conversely, if AI shows documents outside a user's permissions, that itself becomes a finding in the check. |

### Internal status

| Status | Implication |
|---|---|
| Work documents may not be entered into external generative AI | Only an in-house build is possible. |
| The only time measurement is a 2-week sample from Q3 2026 | The baseline is weak. Measure again before investing (task A). |
| 5 IT staff, 0 dedicated to AI | Building it ourselves is unrealistic. Build with an external solution and hire 1 AI staff member to bring operation in-house. |
| Design documents from before 2015 are on paper | AI cannot see them. First check whether the precedents for the 61 recurrences are in paper documents, then decide the scope of digitization. |
| Space and power for expansion in the headquarters server room | Little extra construction burden for an in-house build. |
| 48 staff × 4.8 hours of search a week | About 10,600 hours a year (assuming 46 weeks), about 5.8 people's working time. That is about 12% of working hours. |
| 6.5 hours per report draft | The number of reports per person is unknown, so the annual total cannot yet be calculated. Measure the count. |
| 2025 design change and quality defect costs of KRW 5.9 billion, 61 of 412 design changes recurring | What AI can reduce directly is the recurring share. But how the KRW 5.9 billion splits between design changes and quality defects, and what one recurrence costs, are unknown. |
| 2027–2029 investment cap of KRW 1.5 billion | Split into a base KRW 1.01 billion and a conditional KRW 280 million, with KRW 210 million held back. |

---

## 3. Strategic goals and KPIs

### 3-1. Baselines

| Item | Baseline | Source and limits |
|---|---|---|
| Recurring design changes | 61 / 412 = **14.8%** | 2025 actuals |
| Design change and quality defect costs | **KRW 5.9 billion** | 2025 actuals. Not split by type |
| Weekly document search time per person | **4.8 hours** | 2-week sample in Q3 2026. Seasonality and sample representativeness need checking |
| Time to draft one report | **6.5 hours** | Same as above. No report count |
| AI users | **0** / 48 | No in-house AI at present |

### 3-2. KPIs and targets

| Strategic goal | KPI | Baseline | 2027 | 2028 | 2029 | Measurement |
|---|---|---|---|---|---|---|
| (Linked) | Design change and quality defect costs | KRW 5.9 billion | Company plan path | Company plan path | **KRW 4.72 billion or less** (−20%) | Financial and quality cost totals. Split design changes and quality defects from 2027 |
| 1 | **Recurring design change rate** (core) | 14.8% | 13.3% or less (−10%) | 10.4% or less (−30%) | **7.4% or less** (−50%) | Recurrence judgment on design change requests, applying the same criteria that identified the 61 cases |
| 1 | Rate of similar-case lookups at the start of a design change | Measured in Q1 2027 | Manual check introduced | 80% or more | 95% or more | Share of design change requests with a lookup record attached |
| 1 | Trace-back hit rate (share of recurrences whose precedent document appears in the top 5 search results) | First measured in the PoC | 70% or more | 80% or more | 85% or more | Measured quarterly on a test set built from the 61 recurrences and real queries |
| 2 | **Weekly past document search time per person** | 4.8 hours | 3.8 hours (−20%) | 2.9 hours (−40%) | **2.4 hours** (−50%) | 2-week sample measurements every May and November. Yearly targets judged on the November figure |
| 2 | **Time to draft one report** | 6.5 hours | Baseline remeasured, count established | 4.9 hours (−25%) | **3.9 hours** (−40%) | Report writing log (count and time) |
| 2 | (Supporting) Draft review rejection rate | Measured in Q1 2027 | Measure | At or below baseline | At or below baseline | Review records. Check that quality does not drop as time falls |
| 3 | Weekly active user rate (of 48) | 0% | 60% (29) | 80% (39) | **90%** (44) | System access logs |
| 3 | Document leaks and permission violations | – | 0 | 0 | **0** | Monthly access log checks |
| 3 | AI-related findings in customer security checks | – | 0 | 0 | **0** | Customer check results |
| 3 | Investment spending | Cap KRW 1.5 billion | Only what passes the gate | Only what passes the gate | **KRW 1.5 billion cumulative or less** (base KRW 1.01 billion) | Budget execution records |

Targets were set as reduction rates. If the Q1 2027 remeasurement differs greatly from the 2026 sample, only the baseline changes and the reduction rates stay.

### 3-3. Basis for the targets

**50% fewer recurrences.** The reduction in recurrences can be seen as the product of four steps.

> Recurrence reduction ≈ ① share of precedents in electronic documents × ② share of precedents the AI finds (hit rate) × ③ share of design changes where a lookup is actually done × ④ share of lookup results reflected in the design

With the 2029 targets of ② 85% and ③ 95%, a 50% reduction results when ① × ④ is about 62% or more (e.g., ① 80% × ④ 78%). ① is checked by a trace-back study in Q1 2027. If ① falls short of 70%, selective digitization of paper documents (conditional budget) is carried out.

**50% less search time.** What AI cuts is the time spent "finding" documents, while the time to read and judge them remains. So half was treated as a target near the upper limit. If the June 2027 PoC results fall well short of this level, the 2028–2029 targets will be reset.

**Relation to the company's 20% goal.** Even if all KRW 5.9 billion were design change costs, the average cost of one design change would be no more than KRW 14.32 million (KRW 5.9 billion ÷ 412). If a recurrence costs about this average, cutting 31 recurrences in 2029 saves at most about KRW 440 million, about 38% of the KRW 1.18 billion savings target. So **the company's mid-term plan needs to state separately the share of AI tasks and the share of other tasks (such as process quality control).** If recurrences were costlier problems than average, AI's share grows. This value is estimated in Q1 2027.

---

## 4. Tasks

| Task | Details | Timing | Related goals |
|---|---|---|---|
| **A. Performance measurement base** | ① Remeasure search time and report counts and times over 4 weeks ② Split the KRW 5.9 billion into design changes and quality defects and estimate the cost of each of the 61 recurrences ③ Trace back where the precedent documents for the 61 cases are (electronic or paper) ④ Document the recurrence criteria | Q1 2027 | All |
| **B. In-house AI document search** | Build a retrieval-based AI (RAG) that answers with source documents, covering design change history, design review minutes, quality defect reports, test reports and customer claim reports. Each answer shows its source document and page. The design team's 10 people run a PoC in Q2 (8 weeks, comparing 2 suppliers), then it opens to the design team in September and the quality team (including plants) in October. Drawing image search is left out of the first stage. | From Q2 2027 | 1, 2 |
| **C. Design change procedure integration** | Make a "similar case check" item mandatory on the design change request. In Q2 2027 the check is done manually as now, and in H1 2028 AI search results can be attached directly on the PLM design change request screen. The 61 recurrences may have happened because there was no check procedure rather than no tool, so this task is the core of goal 1. | Q2 2027–H1 2028 | 1 |
| **D. Report drafting support** | Generate drafts in the formats of quality defect reports and design review reports, based on similar past reports and test data. The author is responsible for the draft, and showing source documents is mandatory. Piloted by the quality team in H1 2028 and applied fully in H2. | 2028 | 2 |
| **E. Document data cleanup** | Deduplicate electronic design and quality documents from 2015 onward, mark final versions, and add item, customer and process metadata (80% by end-2027, 100% in H1 2028). Paper documents are digitized only for the scope the trace-back shows is needed among those related to current products (conditional). | 2027–2028 | 1, 2 |
| **F. In-house infrastructure and security** | Install GPU servers in the headquarters server room, with the 2 plants connecting over the company network. The AI follows existing document permissions so it never shows documents a user could not already see, and documents are separated by customer. Query and answer logs are kept, with an external security check once a year. | From H2 2027 | 3 |
| **G. Operating organization, guidelines and training** | Hire 1 AI staff member, write in-house AI usage guidelines (allowed scope, duty to check sources, responsibility for drafts) and train key users. Starts in Q1 2027. | 2027–2029 | 3 |
| **H. Rollout to other departments** (conditional) | Extend use to production engineering, purchasing and others, and expand the servers. Carried out only if the end-2028 gate is passed. | 2029 | 2, 3 |

**Use of the time freed up.** Halving search time frees about 5,300 hours a year in 2029 (about 2.9 people). Only if team goals direct this time to similar-case reviews before design changes and to upstream quality activities will the time saved turn back into cost savings.

---

## 5. Roadmap and stage gates

| Period | Main activities | Gate |
|---|---|---|
| Q1 2027 | Task A (measurement, trace-back, cost breakdown), requests for information to suppliers (3 or more), usage guidelines, start of AI staff hiring | |
| Q2 2027 | PoC with 10 design team members (8 weeks), similar case check item added to design change requests (manual) | **G1 (June): whether to proceed with the full build** |
| H2 2027 | Server installation, search launch (design team in September, quality team in October), electronic document cleanup | **G2 (December): whether to spend the 2028 budget** |
| H1 2028 | PLM integration, report drafting pilot (quality team), selective digitization of paper documents (conditional) | |
| H2 2028 | Full use of report drafting, performance measurement | **G3 (December): whether to roll out in 2029** |
| 2029 | Rollout to other departments (conditional), 3-year performance review, operating plan for 2030 onward | Final year-end review |

| Gate | Pass criteria | Action if not met |
|---|---|---|
| **G1** | ① Trace-back hit rate of 70% or more (for recurrences whose precedent is in electronic documents) ② PoC participants' search time down 30% or more ③ Internal security check passed ④ Cost of one recurrence estimated and the payback conditions in section 6 recalculated | Re-verify for up to 3 months with a different supplier or model. Stop if still not met (loss within KRW 50 million) |
| **G2** | Weekly use rate of 60% or more, search time down 20% or more, 0 security incidents | Postpone PLM integration and drafting, and focus on improving search quality |
| **G3** | Recurrence rate of 10.4% or less, search time down 40% or more, drafting time down 25% or more | Hold the rollout (conditional KRW 200 million) and improve within the existing scope |

---

## 6. Investment plan and return on investment

### 6-1. Investment plan (KRW million)

| Category | Item | 2027 | 2028 | 2029 | Total |
|---|---|---|---|---|---|
| Base | PoC and baseline measurement | 50 | – | – | 50 |
| Base | GPU servers, storage and backup | 200 | – | – | 200 |
| Base | AI search and drafting solution build (document system, permissions, PLM integration) | 200 | 100 | – | 300 |
| Base | Electronic document cleanup and metadata | 60 | 30 | – | 90 |
| Base | Labor cost of 1 AI staff member (hired in H2 2027) | 40 | 80 | 80 | 200 |
| Base | Operation and maintenance (licenses, model replacement) | – | 40 | 40 | 80 |
| Base | Security (access control, logs, external checks) | 30 | 10 | 10 | 50 |
| Base | Training and change management | 10 | 20 | 10 | 40 |
|  | **Base subtotal** | **590** | **280** | **140** | **1,010** |
| Conditional | Selective digitization of paper documents (if G1 confirms the need) | – | 80 | – | 80 |
| Conditional | Rollout to other departments and server expansion (if G3 is passed) | – | – | 200 | 200 |
| Reserve | Unallocated |  |  |  | 210 |
|  | **Total (cap)** |  |  |  | **1,500** |

- Server and solution amounts are estimates. They will be fixed with quotes from 3 or more suppliers in Q1 2027.
- The only spending committed before G1 is the KRW 50 million PoC. The KRW 400 million for servers and solutions is spent after G1 is passed.
- From 2030 on, operating costs of about KRW 130 million a year continue, including KRW 80 million for staff, KRW 40 million for maintenance and KRW 10 million for security.

### 6-2. Return on investment (based on the base investment of KRW 1.01 billion)

**Time effect.** Adding the cut in search time in 2028 and 2029 (an average of 30% and 45% in each year) gives about 7,900 hours, worth about KRW 400 million at KRW 50,000 an hour. This is the value of time freed for other work, though, not cash. The 2027 share and the report drafting effect are left out because there is no count data (a conservative calculation).

**Cost effect.** Meeting the recurrence reduction targets cuts about 55 recurrences in total over 2027–2029 (6 + 18 + 31). The amount saved depends on the cost of one recurrence.

| Average cost of one recurrence (assumed) | Cumulative cost savings to 2029 | Payback on cost savings alone | Payback including time value |
|---|---|---|---|
| KRW 7 million | About KRW 390 million | Around 2037 (effectively out of reach) | 2030 |
| KRW 10 million | About KRW 550 million | 2032 | 2030 |
| KRW 14.32 million (upper limit of the design change average) | About KRW 790 million | 2030 | Within 2029 |

**Conditions for paying back the base investment within the planning period:** One recurrence must cost about KRW 11 million or more including time value, or about KRW 18.4 million or more on cost savings alone. The latter is above the upper limit of the average design change cost. So the accurate message for executives is not "cash payback within 3 years" but **"payback in 2030–2032 if one recurrence costs KRW 10 million or more, with the final call based on the recurrence cost fixed at G1."**

Some effects do not show up in the numbers. The company gains evidence for customer security checks and can keep competitors from opening a gap in search speed. These effects are not included in the payback calculation.

---

## 7. Governance

| Body or role | Members | Responsibilities |
|---|---|---|
| AI steering committee (quarterly) | Executive in charge of technology (chair), design team head, quality team head, IT team head, security officer | Gate (G1–G3) decisions, budget approval, KPI review |
| AI staff (IT team) | 1 new hire. 1 existing IT staff member also covers infrastructure | Solution operation, search quality management, test set management, supplier management |
| Business key users | 2 from the design team, 2 from the quality team (including plants) | Writing test queries, PoC evaluation, spreading use within teams, improvement requests |
| Supplier | Supplier of the on-premises solution | Build, maintenance, support for model replacement (included in the maintenance contract) |

**Key points of the usage guidelines**
- The existing rule barring work documents from external generative AI stays, and only in-house AI use is newly allowed.
- When using AI answers in designs or reports, source documents must be checked. The author is responsible for drafts.
- Customer documents are searchable only by people with work permissions for that customer.

---

## 8. Risks and responses

| Risk | Response |
|---|---|
| Search quality on Korean technical documents falls short of expectations | Compare 2 suppliers in the PoC, apply the G1 hit rate criterion, contract for a structure where models are easy to replace |
| The tool is installed but not used | Build it into the procedure as a mandatory item on design change requests (task C), run key users, publish use rates quarterly |
| Reliability of the baseline (2-week sample) | 4-week remeasurement in Q1 2027, then repeated measurement by the same method at the same times |
| Precedents are in paper documents | Check the scale by trace-back first, then digitize only the needed scope (conditional KRW 80 million) |
| Knowledge concentrated in the 1 AI staff member | Document operating procedures, name 1 IT staff member as backup, supplier maintenance contract |
| AI exposes documents outside a user's permissions | Design it to follow existing document permissions, test permissions before launch, check logs monthly |
| Server price rises or delivery delays | Quotes from 3 or more suppliers, order preparation during the PoC, KRW 210 million reserve |
| Changes in the number of design changes distort recurrence comparisons | Use the rate (recurrences ÷ all design changes) as the core KPI, not the count |

---

## 9. Assumptions and items to confirm

- **Assumptions:** 46 working weeks a year, labor cost of KRW 50,000 an hour, design changes holding at about 412 a year
- **Interpretation:** The internal status contains both "there is no measurement of the time spent" and "a 2-week sample measurement." This was read as meaning there is no systematic measurement, only a 2-week sample, and the sample figures were used as an interim baseline.
- **To confirm in Q1 2027:** Cost of one recurrence, breakdown of the KRW 5.9 billion by type, number of reports per person, share of the 61 recurrences whose precedents are in paper documents
- **Scope of external figures:** The AI Index figures are based on a global survey, some benchmarks and API prices. The Ministry of Science and ICT material was announced in 2023, so current support programs need to be checked separately.

---

The labor cost of 1 AI staff member was included within the KRW 1.5 billion investment cap to keep the estimate conservative. If labor costs are handled as a separate budget, the base investment falls to KRW 810 million and payback comes sooner.
