# Adopting Hyperscale AI In-House

**Executive meeting briefing** | Decision requested: whether to run a pilot in January to June 2027

## 1. Recommendation

We recommend approving a small pilot for the first half of 2027. It would cover only the quality and design teams and would run entirely on systems the company controls.

The case rests on three points:

- **The technology is now cheaper and can be run in-house.** The cost of running AI at a given level of performance has dropped sharply. Models that a company can host on its own servers now perform close to the leading commercial services.
- **We have a clear first use.** The quality and design teams say that searching past documents and drafting reports take a lot of their time. This technology handles that kind of work well.
- **Our constraints decide how we pilot, not whether we pilot.** Our security rules mean documents must stay inside the company. Our IT team has five people and no AI specialist, so we need outside help to build and run the pilot. A limited pilot can work within both constraints.

## 2. What hyperscale AI is

Hyperscale AI means very large AI models trained on huge amounts of text. It is the technology behind services such as ChatGPT. When asked in plain language, these models can search large sets of documents, summarize what they find, and write first drafts. They can also give answers that sound right but are wrong, so a person must check their output.

There are two kinds of model. **Closed models** are available only as online services run by their providers, so documents have to be sent outside the company to use them. **Open-weight models** are published so that a company can run them on its own servers, and documents never leave.

## 3. Why now: what has changed

| Change | Evidence | What it means for us |
|---|---|---|
| Much cheaper to run | The cost of running a system that performs at GPT-3.5's level fell more than 280-fold between November 2022 and October 2024 [1] | Cost is less likely to block a small pilot. Our actual cost depends on the setup we choose and needs vendor quotes. |
| In-house models have nearly caught up | On some benchmarks, the performance gap between open-weight and closed models narrowed from 8% to 1.7% in one year [1] | Keeping documents inside the company, as our rules require, no longer means settling for a much weaker model. The pilot must test whether this holds for our Korean technical documents. |
| Use has become mainstream | The share of organizations reporting AI use rose from 55% in 2023 to 78% in 2024 [1] | The figure covers organizations in general, not manufacturers, so it tells us nothing direct about our competitors. It does show that most organizations no longer treat AI as an experiment. |
| Government support | In April 2023, the Ministry of Science and ICT announced a plan running to 2027, starting with KRW 390.1 billion in 2023. It builds 200 types of training data and 130 Korean-language corpora, and expands computing resources for SMEs, startups, universities and research institutes [2] | More Korean-language data should help Korean-language performance. Computing support could lower our pilot cost, but we must check whether a mid-sized company qualifies and what is still on offer in 2027, the plan's final year. Manufacturing is not one of the plan's five flagship fields. |

## 4. Where to start: quality and design

The quality and design teams are the right place to start, for three reasons:

- **The pain point is already known.** Both teams raised it at last week's meeting.
- **Errors can be caught.** The people reading the AI's output are experts in the content, so they can spot mistakes before anything is used.
- **The scope is small.** Two teams and two tasks keep results measurable, and the pilot can be stopped cleanly.

We have not yet measured how much time these tasks take. The first step of the pilot is to measure it, so the results can be compared with a baseline.

## 5. Constraints and how the pilot handles them

| Constraint | Pilot response |
|---|---|
| Security rules do not allow work documents to be entered into external generative AI services | Run an open-weight model on servers the company controls, so no documents leave. The security team approves the design before launch. |
| The IT team has five people and no one dedicated to AI | An outside partner builds and runs the pilot. IT handles access and the security review, and one IT member acts as point of contact to build in-house know-how. |
| Running a model in-house needs computing equipment | Compare purchase and lease options, and check government computing support, before setting the budget. |
| AI output can be wrong | Use AI only for search and first drafts. Every answer shows its source documents, and a person reviews every draft before use. |

## 6. Options considered

| Option | Benefit | Drawback |
|---|---|---|
| A. Wait and watch | No cost or effort now | No evidence on whether AI works for our documents; the teams' time problem stays |
| **B. Limited pilot (recommended)** | Real evidence at limited cost and risk; easy to stop | Needs a budget, a partner, and some staff time |
| C. Company-wide rollout | Fastest possible benefit | Too large for a five-person IT team; performance on our documents is unproven |

## 7. Proposed pilot plan

- **January to February:** Select a partner, complete the security review, choose the document set, and measure current time spent on search and drafting.
- **March to May:** Run the pilot with volunteers from both teams.
- **June:** Evaluate the results and report to the executive meeting with a recommendation on wider use.
- **Success measures, fixed before launch:** time saved against the baseline, share of AI drafts usable after review, zero security incidents, and user feedback.
- **Staff usage rules:** Draft internal rules for AI use, using the government's guidelines for civil servants [2] as a reference.

The budget has not been estimated yet; see decision 4 below.

## 8. Decisions requested today

1. Approve in principle a pilot for January to June 2027, limited to the quality and design teams.
2. Confirm that no work documents may leave company-controlled systems during the pilot.
3. Name an executive sponsor and a pilot lead.
4. Direct the IT team to obtain partner quotes and check eligibility for government support, and to return with a budget and detailed plan before year-end.

---

**Sources**

[1] Stanford HAI (2025), *AI Index Report 2025*. https://hai.stanford.edu/ai-index/2025-ai-index-report

[2] Ministry of Science and ICT (2023), 초거대 AI 경쟁력 강화에 3901억 투입…"디지털 경제 가속화". https://www.korea.kr/news/policyNewsView.do?newsId=148913885
