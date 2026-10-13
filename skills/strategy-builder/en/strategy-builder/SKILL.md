---
name: strategy-builder
description: Builds an organization's strategy framework in 10 steps for public agencies, companies, and nonprofits. Covers hypothesis and beneficiary setup, external analysis (PEST, STEEP, PESTEL, Five Forces) and internal analysis (VRIO), benchmarking, implications, SWOT or gap analysis, issue confirmation, vision, mission, and core values, strategic goals, strategic tasks, implementation tasks, and KPIs (BSC, Korean government performance evaluation, national R&D, qualitative). Works from user input and checks the links between elements at every step with a bundled script. Use this skill whenever the user mentions strategic planning, mid- to long-term strategy, business strategy, information strategy planning (ISP), vision framework, vision house, mission, core values, SWOT, TOWS, gap analysis, strategic tasks, implementation tasks, KPIs, performance indicators, BSC, VRIO, PEST, or Five Forces, or asks for the strategy part of a business plan, consulting report, or research contract.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Strategy Builder

> This English version was translated from the Korean original (strategy-builder). The translation may behave differently from what the original intends.

Build the strategy framework of a public agency, company, or nonprofit in 10 steps. Start from the hypothesis and beneficiaries, then derive environment analysis, implications, issues, vision, strategies, strategic tasks, implementation tasks, and KPIs in that order. Every element links to elements from earlier steps, and each step is checked so that no element is left without its links.

## Writing rules

- Judge from first principles, from the viewpoint of a PhD-level consultant with 20 years of experience in management, economics, and public administration.
- Write deliverables as terse report-style bullets in an academic report tone. Keep noun-phrase endings where natural and avoid conversational or polite phrasing.
- Describe the beneficiary's view first and apply the beneficiary tracing rule to every strategy element.
- At each step, present the input form, get the user's confirmation, then move to the next step.
- Put comparisons and links in tables. Numbers carry over the number of the parent element.

## User input rules

The user supplies the material for the strategy. If the model fills gaps with plausible guesses, assumptions the user never reviewed spread through the whole strategy.

- The hypothesis, subject, spatial scope, beneficiaries and their needs, upper alignment, external facts, internal status, benchmark cases, implications, issues, SWOT factors, vision, mission, core values, strategies, strategic tasks, implementation tasks, and KPIs all come from user input.
- On entering a step, show that step's input form first and wait until the user submits it. The form explains both how to write the item directly and how to request automatic drafting under the exceptions below.
- If the user submits only part of the form, do not guess the missing items. Ask for them again.

The model may draft without user input only in the cases below. Drafting ahead in any other case breaks this rule.

- (One-stop mode) The user submitted the one-stop input form in one go. Use only what was submitted and ask again for empty items at the step where they are needed.
- (RFP attached) The user attached an RFP and asked for the hypothesis and requirements to be extracted from it.
- (Automatic option chosen) The user picked a step's automatic option, such as "auto" for draft issues or "auto-derive" for strategic or implementation tasks.
- (Explicit request) The user asked for a step or item to be drafted automatically, such as "fill it in for me" or "write it automatically".

## Terms

| Term | Definition |
|---|---|
| Beneficiary | The party the strategy ultimately delivers benefits to: customers, citizens, tenant firms, employees, and so on |
| Beneficiary tracing rule | For every implication, strategy, task, and KPI, you can explain which beneficiary gains what benefit |
| Upper alignment | Higher-level direction the organization must follow: a parent agency's strategy, national policy, the vision of a parent company or organization, relevant laws |
| Fact | An objective phenomenon or trend collected in steps 2-4. Contains no solution or desired state |
| Implication | The meaning read from facts. Each implication belongs to one source (macro environment, micro environment, internal status, benchmarking) |
| Grouping (induction) | Bundling several implications that point to a common problem into one issue |
| Issue | A problem the strategy solves. The step 1 draft is confirmed in step 6 on the basis of implications |
| As-is, To-be, gap | Current state, target state, and the difference between them |
| CSF | Critical Success Factor. The decisive reason a benchmark case succeeded |
| Strategy candidate | A draft strategy combining SWOT factors. Belongs to one quadrant: SO, ST, WO, or WT |
| Unlinked element | An element missing a required upward or downward link |
| Candidate pool | A list of task or KPI candidates drawn up in sufficient number before selection |

## Alignment rules

Everything from the vision down to the KPIs forms one strategy framework. Upper elements set the direction of lower elements, and lower elements are the means to achieve upper elements.

| Element | Role |
|---|---|
| Vision | The future the organization aims for over the long term. A sentence that condenses why it exists |
| Mission | A sentence stating what value the organization delivers to which beneficiaries and how |
| Core value | The code of conduct for carrying out the mission. One per strategy |
| Strategy | The direction for achieving the vision and mission |
| Strategic goal | The state in which the strategy is achieved. Uses the strategy number as is |
| Strategic task | A concrete way to achieve the strategy. Carries over the parent strategy's number |
| Implementation task | A detailed unit of activity that carries out a strategic task. Carries over the parent task's number |
| KPI | An indicator measuring how far each level is achieved. Carries over the number of the element it measures |

The links below must all hold. Each time you derive an element, check its links upward and downward so that no unlinked element remains.

- Every fact feeds at least one implication.
- Every implication is grouped into at least one issue.
- Every issue maps to at least one strategy, and every strategy resolves at least one issue.
- Every SWOT factor is used by the strategy candidates of its quadrants.
- Every strategy has exactly one core value and at least one strategic task.
- When the implementation task step runs, every strategic task has implementation tasks.
- Every lower KPI links to a KPI of the element directly above and contributes to it.

## Run modes

- (Sequential mode) The default. Present each step's input form, take the input, write the deliverable, and get the user's confirmation. Do not write later steps ahead of time.
- (One-stop mode) Used when the user submits the form below in one go. Skip the intermediate confirmations, produce the full result within what was submitted, then take revision requests. Ask again for empty items on entering the step that needs them. The step checks still run right after each step in one-stop mode.

### One-stop input form

```
[Hypothesis] subject, spatial scope, time scope, or attach an RFP
[Beneficiaries] key beneficiaries and their needs
[Upper alignment] parent agency strategy, national policy, parent organization vision, or "none"
[Draft issues] written by the user, or auto
[External environment] macro (free input, PEST, STEEP, or PESTEL) and micro (free input or Five Forces)
[Internal status] free input or VRIO; demand survey materials may be attached
[Benchmarking] describe cases, or skip
[Analysis tool] SWOT or gap analysis
[Gap mode] split or integrated (gap analysis only; default split)
[Issue confirmation] refine, keep, or re-derive (default refine)
[SWOT mode] fixed, flexible, or issue-linked (SWOT only; default fixed)
[SWOT follow-up] fixed: Y or N; flexible: as-is, representative, or cross-combination
[Strategy type] standard or R&BD (SWOT only; default standard)
[Strategic goal] integrated, dual, qualitative, or quantitative (default integrated)
[Strategic tasks] user submission, fixed count n, or auto-derive (default user submission)
[Implementation tasks] skip, user submission, fixed count n, or auto-derive; priority assessment Y or N
[KPIs] skip, all levels, lower level, or strategy level (default all levels)
[KPI track] BSC, Korean government performance evaluation, R&D (include Impact or not), model-led, or qualitative
[Time format] short, mid, and long term; dates; or both
[Check method] script or manual (default script)
```

## Step checks

The "Check" items in each step are conditions that find missing links and rule violations. Checks run right after steps 1, 5, 6, 7, 8, 9, and 10; facts from steps 2-4 are covered by the step 5 check. If code can run, use the script. If it cannot, or the user picks manual checks, compare the same items by hand. When a violation appears, show it to the user, fix it, and check again. Do not move to the next step before the check passes.

The script is `scripts/check_strategy.py` in this skill folder and needs only the Python 3.8+ standard library. Use `python3` if the environment has no `python` command. Keep all work in one state file (JSON); the same file lets you resume an interrupted session.

```bash
python scripts/check_strategy.py --template > strategy_state.json         # create an empty state file
python scripts/check_strategy.py strategy_state.json --step 6 --lang en   # check steps 1-6
python scripts/check_strategy.py strategy_state.json --step all --lang en --chart   # full check and link charts
```

- Look up the state file's keys, fields, and option values with `python scripts/check_strategy.py --schema --lang en` and follow them. Record the options listed by `--schema` from the one-stop form and later choices in settings.
- The parent of a strategic task, implementation task, or KPI is read from its id, so keep the numbering format exact.
- `--step N` runs every check for steps 1 to N, so an edit in a later step that breaks an earlier rule still shows up.
- Exit codes: 0 pass, 1 violation, 2 unreadable input file. Lines starting with "(recommendation)" are advice and do not affect the result.
- `--chart` prints two Mermaid charts: a trace chart from implications to KPIs and a vision-house chart.

## Overall flow

| Step | Content | When |
|---|---|---|
| 1 | Setup (hypothesis, beneficiaries, upper alignment, draft issues) | Required |
| 2, 3 | External environment analysis, internal status analysis | Required for SWOT and split gap mode, skipped in integrated gap mode |
| 4 | Benchmarking | Optional on every path |
| 5 | Implications | Required |
| 6 | Issue confirmation and strategy derivation | Required |
| 7 | Vision, mission, and core values | Required |
| 8 | Strategic goals and strategic tasks | Required |
| 9 | Implementation tasks and priority assessment | Optional |
| 10 | KPIs | Optional |

## Step 1 Setup

- (Hypothesis) Take the subject of the strategy, its spatial scope, and its time scope. If an RFP is attached, extract them from it and get the user's confirmation.
- (Beneficiaries) Take the key beneficiaries and their needs.
- (Upper alignment) Take the parent agency strategy, national policy, parent organization vision, and laws. If none apply, have the user answer "none" and record that. The upper alignment becomes the top-down input for the vision in step 7.
- (Draft issues) The user writes them or picks "auto". With auto, draft them from the hypothesis, beneficiary needs, and upper alignment. The drafts are tested against the implications in step 6.
- Deliverables: the hypothesis with purpose, subject, spatial scope, and time scope; the beneficiaries and their needs; the upper alignment; the list of draft issues.
- Check: the hypothesis has a subject, spatial scope, and time scope. At least one beneficiary exists. Either at least one upper alignment exists or "none" is recorded, never both. At least one draft issue exists.

After the step 1 check passes, ask for the analysis tool (SWOT or gap analysis). If the user picks gap analysis, ask for the gap mode next. Split mode (default) runs steps 2-5 in order and suits mid- to long-term strategies where environmental factors must not be missed, including information strategy planning (ISP). Integrated mode skips steps 2-3, asks whether to benchmark, and goes on to step 5; it suits smaller decisions and short-term operational improvement.

## Step 2 External environment

Collect facts separately for the macro environment and the micro environment. A macro framework does not cover the micro environment, so run both. The default is free input, and the user may pick a framework.

| Scope | Framework | Components |
|---|---|---|
| Macro | PEST | political, economic, social, technological |
| Macro | STEEP | social, technological, economic, environmental, political |
| Macro | PESTEL | political, economic, social, technological, environmental, legal |
| Micro | Five Forces | rivalry among existing competitors, bargaining power of suppliers, bargaining power of buyers, threat of new entrants, threat of substitutes |

- Without a framework, summarize the macro and micro environments as free text. Facts record objective phenomena and trends only; leave To-be states, strategies, and solutions out of this step.

## Step 3 Internal status

- The default is free input, and the user may pick VRIO. VRIO assesses resources and capabilities with four questions: Value, Rarity, Imitability, and Organization (whether the organization is set up to use them).
- When demand survey materials arrive (surveys, interviews, RFP requirements), list the requirements.
- Record the internal capabilities and their assessment by category as facts. Leave out To-be states and needs.

## Step 4 Benchmarking

This step is optional on every path; skip it when not needed. Record objective facts about leading cases and extract the CSFs of each case. Benchmark results can support the To-be plans in step 6.

## Step 5 Implications

Implications are the input for deriving issues, so no path skips this step.

- (SWOT, split gap mode) Derive implications from the facts of steps 2-4 and write one bullet line each under four subheadings: macro environment, micro environment, internal status, benchmarking.
- (Integrated gap mode) The user writes the As-is implications freely; if benchmarking was done, add benchmark implications. Use two subheadings, As-is implications and benchmark implications, or only the first if there was no benchmarking.
- Each implication belongs to one source. Split any implication that draws on facts from different sources into one implication per source. This split is the basis for applying the SWOT factor source rules in step 6.
- Write implications as bullets without tables, and get the user's confirmation.
- Check: every fact is used by at least one implication. In SWOT and split mode, every implication rests on at least one fact of its own source, and no implication has the asis source. In integrated mode, facts come only from benchmarking, and implication sources are As-is or benchmarking.

## Step 6 Issue confirmation

First choose how to confirm the issues.

- (Refine, default) Restructure and strengthen the step 1 drafts on the basis of the implications.
- (Keep) Confirm the step 1 drafts as they are and only link the implications.
- (Re-derive) Discard the step 1 drafts and derive new issues by grouping the implications.

When several implications point to the same problem, bundle them into one issue. Build a table linking implications to issues, and when refining or re-deriving, show each draft next to its supporting implications. Then derive strategies along the path chosen earlier.

- Check: every issue is grouped from at least one implication. Every implication is grouped into at least one issue. At least one strategy exists, and strategy numbers are positive integers.

### Gap analysis path

- Describe the overall As-is and To-be states and derive the gaps between them. Pick the key gap for each issue and link it to the strategy that closes it.
- Three or more issues are recommended.

| Issue addressed | As-is implications | Gap | To-be plan | Strategy |
|---|---|---|---|---|
| Issue number and name | Summary of the As-is state | Difference between As-is and To-be | Plan for reaching To-be | Strategy name |

- Check: every gap belongs to exactly one existing issue and records As-is and To-be. Every issue has a gap. Every strategy closes at least one gap, and every gap links to at least one strategy.

### SWOT path

Number every factor. Strengths S, weaknesses W, opportunities O, and threats T default to four each; the count changes on request, but each of the four types needs at least one. The factor table has a type column (strength, weakness, opportunity, threat). Write factor and strategy names as qualitative concepts without figures.

Derive factors from the step 5 implications and follow the source rules below. Internal status describes the organization itself, while the macro and micro environments describe what lies outside it.

| Factor | Implication sources allowed | Sources not allowed |
|---|---|---|
| Strength (S), Weakness (W) | internal status, benchmarking | macro environment, micro environment |
| Opportunity (O), Threat (T) | macro environment, micro environment, benchmarking | internal status |

A strategy candidate combines only the two factor types of its quadrant and uses at least one factor of each. SO combines strengths and opportunities, ST strengths and threats, WO weaknesses and opportunities, and WT weaknesses and threats. Together, the candidates of a quadrant use every factor of that quadrant's two types.

| Mode | Candidates | Follow-up | Final number of strategies |
|---|---|---|---|
| Fixed (default) | One per quadrant, using every factor of both types | Y confirms as is; N restructures toward resolving issues | 4 |
| Flexible | Several per quadrant, each listing the factor numbers it uses | One of the three options below | Depends on the option |
| Issue-linked | Several per quadrant | Restructured one-to-one toward resolving issues | Same as the number of issues |

- (Fixed follow-up) Ask whether to keep the four strategies as they are. Y confirms them without changing their direction and then links the issues to each strategy. N keeps four strategies but distributes the issues to address (more than four is fine) across them and readjusts the strategy names and content.
- (Flexible, as-is) Confirm every candidate as its own strategy.
- (Flexible, representative) Place each quadrant's candidates as strategic tasks and derive one representative strategy per quadrant, four in total.
- (Flexible, cross-combination) Combine candidates from different quadrants, alone or several together, into integrated strategies. There is no limit on how many are combined (for example SO1 alone, ST1 with WO2, or SO3 with ST2 and WT1). The final set of strategies must include every factor.
- (Issue-linked) Build a matrix of which candidates resolve which issues, then select or merge candidates by their contribution. Final strategies and issues correspond one to one; the number of candidates may differ from the number of final strategies.

The strategy type is a naming convention for the character of a strategy, and the default is standard. Standard names each quadrant by its strategic direction: SO uses strengths to seize opportunities, ST uses strengths to reduce threats, WO uses opportunities to make up for weaknesses, and WT reduces weaknesses and threats together. R&BD (research and business development) names each strategy by the program instrument that carries it out and is used in R&BD and public R&D program planning.

| Type | SO | ST | WO | WT |
|---|---|---|---|---|
| Standard | growth | sustaining competitive advantage | innovation | risk management |
| R&BD | infrastructure | non-R&D | R&D | governance |

Summarize the derived strategies in the form below.

| Quadrant | Factors | As-is implications | To-be plan | Strategy |
|---|---|---|---|---|
| SO1, ST2, WO1, etc. | Factor numbers and names | Summary of step 5 implications | Concrete To-be | Strategy name |

- Add a sequence number after SO, ST, WO, or WT in the quadrant column. Fixed mode has one per quadrant, so the number may be left off.
- The factor column shows the number and the name together (for example `S2. Quality control capability built on skilled staff`), never numbers alone.
- The As-is column lists the step 5 implications summarized at keyword level. The To-be plan states a concrete direction for action.
- Put multiple items in a cell on separate lines. For issue-linked mode and fixed N, add an "Issue addressed" column right after the quadrant column.
- Cross-combination adds the table below.

| Strategy number | Combined candidates | Rationale for combining | Strategy name | Factors used |
|---|---|---|---|---|

- Check: factor source rules, candidate combination rules, and full use of each quadrant's factors hold. In fixed mode, each quadrant has one candidate and the four strategies cover SO, ST, WO, and WT one each. As-is maps candidates to strategies one to one. Representative gives each of the four strategies all candidates of one quadrant. Cross-combination's final strategies include every factor. Issue-linked maps strategies to issues one to one.

## Step 7 Vision

Derive the vision, mission, and core values by combining top-down and bottom-up inputs. If the upper alignment is "none", derive them from the bottom-up inputs alone.

| Direction | Inputs |
|---|---|
| Top-down | parent agency strategy, national policy, parent organization vision, laws |
| Bottom-up | what the step 6 strategies have in common, the values beneficiaries care about |

Give each strategy exactly one core value, and do not reuse a core value across strategies, because the final vision house shows one core value per strategy.

| Item | Top-down | Bottom-up | Final |
|---|---|---|---|
| Vision | | | |
| Mission | | | |
| Core values | | | |

Map strategies to core values in the table below.

| Strategy number | Strategy name | Core value |
|---|---|---|

- Check: the vision and mission texts exist. If upper alignments exist, the vision links to at least one of them. The mission links to at least one beneficiary. Every strategy has exactly one core value.

## Step 8 Strategic tasks

| Level | Number format | Example |
|---|---|---|
| Strategy | `N. strategy name` | `1. Low-carbon production shift` |
| Strategic task | `N-M. task name` | `1-1. Upgrade process energy management` |
| Implementation task | `N-M-L. task name` | `1-1-1. Install power metering on key equipment` |

Choose the strategic goal pattern. Strategic goals use the strategy number as is and get no number of their own.

| Pattern | Structure | Typical use |
|---|---|---|
| Integrated (default) | The strategy name doubles as the goal | The strategy name itself works as the goal |
| Dual | One qualitative goal and one quantitative goal | Public mid- to long-term plans, R&D program goals |
| Qualitative | One qualitative goal | Direction-focused vision houses |
| Quantitative | One quantitative goal | Performance management focused on indicator targets |

Write the strategic goals in the form below.

| Strategy number | Strategy name | Qualitative goal | Quantitative goal |
|---|---|---|---|

- Dual fills both columns. Qualitative leaves the quantitative column empty, and quantitative leaves the qualitative column empty. Integrated skips this table.
- Each strategy has one quantitative goal; do not bundle several targets into one cell.

Choose how to derive strategic tasks. The model does not create strategic tasks without the user's instruction.

- (User submission, default) The user submits a list of strategic tasks. Process it in this order: review the list, extract the common aim from a business-goal viewpoint, group the aims into strategies, check consistency with the upper alignment, and flag tasks with weak consistency separately.
- (Fixed count n) Present as many candidates as the user set and get confirmation.
- (Auto-derive) Only when the user picks it, present a candidate pool per strategy with no fixed count and get approval.
- A strategic task is a concrete way to move an issue to its To-be state. Write down how each strategic task links to its strategy.
- Under the representative option, each strategy candidate becomes one strategic task of its strategy.

| Strategy number | Strategic task number | Strategic task name |
|---|---|---|

- Check: every issue maps to at least one strategy, and every strategy resolves at least one issue. On the gap path, the issue of each gap a strategy closes is in that strategy's issue list. Strategic goals match the chosen pattern. Every strategy has strategic tasks, task numbers follow `N-M`, and the parent strategy exists. Under the representative option, each candidate has exactly one strategic task.

## Step 9 Implementation tasks

This step is optional. As in step 8, choose user submission (default), fixed count n, or auto-derive.

- With user submission, group the submitted items by similarity, group those groups into strategic tasks and the strategic tasks into strategies, then check consistency with the upper alignment.
- Write implementation tasks at the level of executable activities and check them against SMART.

| Criterion | Implementation task | KPI (step 10) |
|---|---|---|
| Specific | The activity is clearly defined | The indicator concept and measurement method are clear |
| Measurable | The output can be measured | Measurement data exists |
| Achievable | Feasible with available resources | The target can be reached |
| Relevant | Aligned with the parent strategic task | Linked to the indicator of the level above |
| Time-bound | A deadline is stated | The measurement timing fits |

- (Priority assessment, optional) Assess by need (contribution to achieving the strategy), urgency (need to act at each point in time), overlap (degree of overlap with existing programs and other tasks), and feasibility (availability of resources and capabilities), then build a schedule and a precedence roadmap. Record precedence in the state file's precedes field.

| Strategic task number | Implementation task number | Implementation task name |
|---|---|---|

- Check: every strategic task has implementation tasks. Implementation task numbers follow `N-M-L`, and the parent strategic task exists. Precedence has no self-reference and no cycle. If this step was skipped, no implementation tasks exist.

## Step 10 KPIs

This step is optional. Ask for the KPI levels, then the track.

- (Levels) All levels (default) puts KPIs on strategies, strategic tasks, and implementation tasks. Lower level puts them on implementation tasks only, and strategy level on strategies only. If the implementation task step was skipped, only strategy level is available.
- (Track) If the user does not choose, recommend one by subject: track 2 for public agency policy, track 3 for R&D programs, and track 1 otherwise.

| Track | Name | Applies to |
|---|---|---|
| 1 | BSC | private, nonprofit, general public sector |
| 2 | Korean government performance evaluation | central government agencies, public agency policy |
| 3 | R&D | R&D programs, technology development projects |
| 4 | Model-led | emerging fields where no standard track fits, experimental programs |
| 5 | Qualitative | fields that are hard to quantify |

Apply the common rules below on every track.

- Meet the step 9 SMART criteria. Track 3 adds its own SMART criteria.
- Every KPI aligns with the vision, mission, and strategies, and the sum or contribution of lower KPIs leads to achieving upper KPIs.
- Set two or more KPIs per performance goal or per level.
- Draw up a sufficient candidate pool before selecting.
- Use one track by default. If tracks must be mixed, pick one main track, borrow some rules from a secondary track, and state the reason and scope of the mix.

KPI numbers take the form `1-KPI-1` for strategies, `1-1-KPI-1` for strategic tasks, and `1-1-1-KPI-1` for implementation tasks. At all levels, each lower KPI links through contributes_to to one KPI of the element directly above, and strategy KPIs have no upper KPI.

| Number | Parent element | KPI name | KPI type | Measurement method | Target | Deadline |
|---|---|---|---|---|---|---|

- The parent element is one level above the element being measured: vision or mission for strategy KPIs, the strategy for strategic task KPIs, and the strategic task for implementation task KPIs.
- The KPI type is one of Input, Activity, Output, Outcome, or Impact.
- Write the measurement method as a bracketed label plus the formula or method (for example `(count) annual sum of client firms`, `(formula) spend / total budget × 100`, `(scale) quarterly mean on a 5-point Likert scale`).
- Write deadlines in the chosen time format (short, mid, or long term; dates; or both).
- Check: KPI numbers follow the format, the measured element exists, and no KPI sits outside the chosen levels. Every element at the chosen levels has a KPI. At all levels, strategic task and implementation task KPIs link to a KPI of the element directly above. The government performance evaluation track uses the dual goal pattern. The R&D track has no Impact KPI unless the user chose to include it. All levels and lower level require the implementation task step. If the KPI step was skipped, no KPIs exist.

### Track 1 BSC

| Level | KPI types |
|---|---|
| Strategy | Outcome, Impact |
| Strategic task | Output, short-term Outcome |
| Implementation task | Input, Activity, Output |

- KPIs become more concrete and operational at lower levels.
- Upper levels center on lagging indicators that show results (Outcome); lower levels center on leading indicators that drive results (Output, Activity).
- Spell out the chain from Input through Activity, Output, and Outcome to Impact.
- Balance the four perspectives: financial, customer, internal process, and learning and growth.
- Roll up lower KPIs by weighted average (satisfaction, achievement rate), sum (counts, headcount, budget), or a representative KPI (one key indicator).
- If Impact KPIs are used, the quantitative or dual goal pattern is recommended. Under the integrated or qualitative pattern, mark Impact KPIs separately in the deliverable.

### Track 2 Korean government performance evaluation

This track fits the performance management system of Korean central government agencies (5-year performance management strategic plans and annual implementation plans).

| Government evaluation | This skill | Nature |
|---|---|---|
| Mission (임무) | Mission | Why the organization exists |
| Vision (비전) | Vision | Long-term aim |
| Strategic objective (전략목표) | Strategy and qualitative goal | Policy direction |
| Performance target (성과목표) | Quantitative goal | Concrete measurable target |
| Managed task (관리과제) | Strategic task or implementation task | Unit of execution |
| Performance indicator (성과지표) | KPI | Measures achievement |

- The system's "strategic objective" matches this skill's strategy and qualitative goal, and this skill's quantitative goal matches the "performance target". The same words carry different meanings, so keep them apart in deliverables.
- Map managed tasks to implementation tasks by default, and to strategic tasks when the unit of execution is broad.
- The goal pattern must be dual. If another pattern was chosen in step 8, get the user's confirmation before entering this track and switch to dual.
- Set KPI types for each level by its degree of abstraction; no level-specific type mapping is imposed. KPIs are classed as quantitative, qualitative, input, process, output, and outcome. Qualitative KPIs involve evaluator judgment, so standardize the measurement tools.
- Run 5-year mid- to long-term KPIs alongside annual implementation KPIs, and self-assess at the managed task level.

### Track 3 R&D

This track follows how performance goals and indicators are set for Korean national R&D programs. The classifications and periods below follow the 6th edition (2024) of KISTEP's standard performance indicators for national R&D programs; if a newer edition is published, follow it.

| Type | Definition | Examples |
|---|---|---|
| Input | Funds, staff, and equipment used for research | Total annual research budget, number of master's and PhD-level researchers, number of equipment items |
| Activity | Activities that turn inputs into outputs | Progress rate, degree of progress, roadmap completion rate |
| Output | Quantitative or qualitative results produced directly by the program | Papers, registered patents, citations |
| Outcome | How far the program achieved its intended effects | Technology level gain, employment rate, firm growth rate |

- Derive the candidate pool in the order input, activity, output, outcome, and select with qualitative output KPIs and outcome KPIs at the center. Avoid input and activity KPIs that are met by spending the budget alone, and simple count KPIs such as the number of papers or patents.
- Impact KPIs are handled in the effectiveness analysis after the program ends, so leave them out of the program's KPIs by default. If the user wants to manage long-term effects, include them and mark them as being for effectiveness analysis.
- Class the output KPIs that measure quality, together with outcome KPIs, as qualitative performance indicators. Examples are the mrnIF of papers (a journal's rank within its field standardized to 0-100), grades from the patent evaluation systems K-PEG and SMART, and graded expert assessments. Make their measurement methods objective.
- If the implementation task step ran, treat implementation tasks as the R&D program unit; otherwise treat strategic tasks as the unit, and apply the KPI types and time stages to it.

| Time stage | Period | Main KPI |
|---|---|---|
| Early | Within 3 years of program start | Output |
| Middle | 3 to 5 years | Short-term outcome |
| Late | 6 years or more | Long-term outcome |

Example performance areas at each stage, by program type, are shown below and can be adjusted to the program's characteristics. For programs that need a long time, such as basic research, the period of each stage may also differ.

| Program type | Early | Middle | Late |
|---|---|---|---|
| Basic research | scientific, technological | scientific, technological | scientific, technological, economic, social |
| Short-term industrial technology development | technological, economic | technological, economic | technological, economic |
| Mid- to long-term industrial technology development | scientific, technological | scientific, technological, economic | economic |
| Public technology development | scientific, technological | scientific, technological, social | economic, social |
| Regional R&D | scientific, technological, economic | technological, economic, social | economic, social |
| Defense technology development | technological, economic, infrastructure | technological, economic, infrastructure | technological, economic, infrastructure |
| Human resource development | scientific, technological | scientific, technological | economic, social |
| Facilities and equipment building | infrastructure | infrastructure | economic, social, infrastructure |
| Outcome diffusion | technological, economic, infrastructure | technological, economic, infrastructure | technological, economic, infrastructure |
| International cooperation | scientific, technological | scientific, technological | economic, social |

- Performance areas are scientific (papers, biological resources, chemical compounds), technological (patents, content, software, know-how), economic (technology contracts, revenue, industrial jobs and startups, support for small and medium enterprises, import substitution), social (human resource development, public-sector jobs and startups, public understanding of science, international exchange, policy effects), and infrastructure (facilities and equipment, information systems, weapon systems).
- Build indicators in three tiers: performance area (top), performance type as the tangible or intangible output that represents the program's results within the area (middle), and the indicator measuring the quality of that output (bottom).
- Consider program type, period, and history together. For continuing programs, lower the weight of output KPIs and center on outcome KPIs. For fixed-term programs, shift from outputs early on to outcomes in the middle and later stages. Outside basic research, do not give paper-based KPIs excessive weight.
- Set two or more KPIs per performance goal and select them with the R&D SMART below. It shares the acronym with the general SMART in step 9 but means something different, so keep them apart.

| Criterion | Content |
|---|---|
| Specific | The indicator concept and measurement method are clear and the data is consistent |
| Measurable | Measurement data exists with no restrictions on use |
| Attributable | The result falls within the program's scope and is not distorted by outside factors |
| Reliable | A third-party review gets the same result |
| Timely | The measurement timing fits |

### Track 4 Model-led

- Use it for emerging fields where no standard track fits, for undefined fields where indicators must be found from scratch, or when the user wants indicators derived to fit the program without predefined mapping rules.
- Apply only the common rules (SMART, vertical alignment, balance of quantitative and qualitative KPIs). Do not impose level-specific KPI types, time stages, or program-type criteria.
- Combine the hypothesis, beneficiary needs, and strategy framework to derive KPI candidates, select them with SMART and vertical alignment, and get the user's confirmation.

### Track 5 Qualitative

- Use it for fields that are hard to quantify, such as organizational culture, governance, leadership, partnerships, trust, the arts, education, social cohesion, local communities, and early-stage programs without accumulated quantitative data.
- Derive qualitative KPIs first at every level and use quantitative KPIs as support.
- Pick measurement tools from: Likert scales (satisfaction, awareness, or agreement on a 5- or 7-point scale), rubrics (achievement criteria by level), standardized indices (comparable qualitative scores), case studies (records of change), narrative assessment (evaluating stories of change), expert qualitative review (gathering and reconciling outside expert opinion), in-depth interviews (views of beneficiaries and stakeholders), and focus groups (evaluation through group discussion).
- Standardize the tools in advance, train the assessors, and check consistency between assessors. Cross-checks among several assessors and supporting quantitative KPIs add objectivity.

## Final vision house

After all steps, present the integrated result. If the check method is the script, include the `--chart` output. First show the vision, mission, and core values in a two-column table (item and content), then repeat the two tables below for each strategy under the heading `Strategy N strategy name`.

| Item | Content |
|---|---|
| Core value | |
| Qualitative goal | Only under the matching pattern |
| Quantitative goal | Only under the matching pattern |

Show strategic tasks, implementation tasks, and KPIs in the table below.

| Strategic task | Implementation tasks | Key KPIs |
|---|---|---|
| N-M. task name | N-M-L. task names, one per line | KPI numbers and names, one per line |

- Under the integrated goal pattern, drop the qualitative and quantitative goal rows.
- If the implementation task step was skipped, drop that column; if the KPI step was skipped, drop the KPI column.

## References

- Weihrich, H.(1982), The TOWS Matrix: A Tool for Situational Analysis, Long Range Planning 15(2)(https://doi.org/10.1016/0024-6301(82)90120-0)
- Porter, M. E.(2008), The Five Competitive Forces That Shape Strategy, Harvard Business Review(https://hbr.org/2008/01/the-five-competitive-forces-that-shape-strategy)
- Barney, J. B.(1995), Looking Inside for Competitive Advantage, Academy of Management Executive 9(4)(https://doi.org/10.5465/ame.1995.9512032192)
- Kaplan, R. S., Norton, D. P.(1992), The Balanced Scorecard: Measures That Drive Performance, Harvard Business Review(https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2)
- W.K. Kellogg Foundation(2004), Logic Model Development Guide(https://wkkf.issuelab.org/resources/10124/10124.pdf)
- Doran, G. T.(1981), There's a S.M.A.R.T. Way to Write Management's Goals and Objectives, Management Review 70(11)
- Rockart, J. F.(1979), Chief Executives Define Their Own Data Needs, Harvard Business Review(https://hbr.org/1979/03/chief-executives-define-their-own-data-needs)
- CIPD, PESTLE Analysis(https://www.cipd.org/en/knowledge/factsheets/pestle-analysis-factsheet/)
- Office for Government Policy Coordination, Government Performance Evaluation Portal, performance management strategic and implementation plans(https://www.evaluation.go.kr/web/page.do?menu_id=159)
- Korea Institute of S&T Evaluation and Planning (KISTEP)(2024), Standard Performance Indicators for National R&D Programs (6th edition): Guide to Setting Performance Goals and Indicators(https://www.kistep.re.kr/board.es?mid=a10305080000&bid=0002&act=view&list_no=93091)
