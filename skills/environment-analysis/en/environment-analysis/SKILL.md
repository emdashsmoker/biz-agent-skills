---
name: environment-analysis
description: Environment analysis for planners and consultants. Runs the macro environment (PEST, STEEP, PESTEL), micro environment (market, industry value chain, Five Forces, competitors, investment), internal status (SPROC, 7S, VRIO, regional innovation resources), and benchmarking as separate modules, then writes traceable implications in a bullet report. Handles full runs, single parts such as Five Forces only, and reviews of existing analyses. Uses web search, user files, and internal systems connected through MCP or APIs, with source quality rules and verification levels. No SWOT or strategy. Use for environment scanning, market, policy, technology, or investment trends, competitive structure, capability assessment, benchmarking, or regional R&BD assessment. Read the relevant files among references/macro.md, references/micro.md, references/five-forces.md, references/internal.md, references/benchmarking.md, references/sources.md (data channels, verification), and references/writing.md (report format).
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

> This English edition is a translation of the Korean original. Some rules were adapted to English writing conventions, and the skill may behave differently from the intent of the original.

# Environment Analysis

This skill organizes evidence on the external environment around a subject and the subject's internal status. The outputs are sourced facts, implications induced from those facts, and a structured bullet report. The analysis stops at implications. SWOT classification and prescriptions such as strategies, initiatives, and targets belong to later stages, and this skill hands over facts and implications in a form those stages can use directly.

An environment analysis does not always need the full process. Every module can run on its own for cases that need only policy trends, only competitive structure, or only an internal capability assessment.

## Core principles

- (Evidence) Factual statements rely only on user-provided material, web pages opened during this task, and data retrieved from connected systems (internal systems, public data APIs, and similar). Do not fill facts from model memory. Mark anything missing from these sources as unconfirmed
- (Facts separate from interpretation) Module sections contain confirmed conditions and trends. Ratings defined by a procedure, such as Five Forces intensity, VRIO results, and critical success factors, appear paired with their supporting facts and never merged into the same sentence as a fact. Interpretation of what the findings mean for the subject goes in the implications section
- (No prescriptions) Do not write to-be states, solutions, support needs, or investment feasibility judgments. Later stages such as SWOT or gap analysis handle those
- (Traceability) Give every fact an ID, a source, and a reference date. Tag every implication with the IDs of its supporting facts. A third party who follows the same procedure with the same material should reach the same conclusions
- (Computation in code) Compute sums, shares, growth rates, and conversions in code, and recheck figures quoted from sources in code. If code execution is unavailable, show the formula and inputs and mark the result as needing a check
- (Requested scope) Run only the requested modules and categories. Collect facts generously and keep interpretation brief

## Definitions

| Term | Definition |
|---|---|
| Subject | The organization, region, or industry and technology area at the center of the analysis |
| Topic | The industry, technology, product, service, or policy field the analysis covers |
| Macro environment | Broad changes the subject cannot control and has no direct exchange with: policy, economy, society, technology, environment, law and regulation |
| Micro environment | Parties the subject interacts with through transactions, competition, or cooperation: markets, industries, competitors, customers, suppliers, funding sources |
| Internal status | Resources, capabilities, and operations the subject controls directly |
| Benchmarking | Cases of comparable subjects and the differences between them and the subject |
| Fact | A single factual statement with a confirmed source and reference date |
| Rating | The result of evaluating facts against defined criteria, as in Five Forces or VRIO. Always recorded with its supporting facts |
| Implication | A one-sentence statement, induced from one or more facts or ratings, of what the findings mean for the subject |
| Industry value chain | The chain of market stages in an industry, from raw material and component supply (upstream) to final demand (downstream). Each stage is a market where several firms compete. It corresponds to what Porter (1985) called the value system, the linked value chains of suppliers, the firm, channels, and buyers. The unit of analysis for the micro environment and Five Forces |
| Organizational value chain | The chain of activities that create value inside one organization. Porter (1985) divided them into primary activities (inbound logistics, operations, outbound logistics, marketing and sales, service) and support activities (firm infrastructure, human resource management, technology development, procurement). The subject controls these activities, so they belong to internal status |
| Data channel | Web search, user-provided files, or connected systems (MCP, API, database) |
| Verification level | The strictness of source checking, from level 1 to level 3, defined in references/sources.md |

One criterion separates macro, micro, and internal: whether the subject can control or interact with the item. The same item moves between categories when the subject changes. Regional industrial policy is part of the macro environment when a firm in the region is the subject, and part of internal status when that region or its local government is the subject. A policy direction document for government R&D programs belongs to the macro environment. The funding flow of individual programs and projects that the subject applies for or competes for belongs to the investment category of the micro environment. Programs the subject has already won and is running are resources it controls, so they belong to internal status.

The industry value chain and the organizational value chain work at different units. The unit of the industry value chain is a market, and the unit of the organizational value chain is an activity inside one organization. Always write both terms with their qualifier and never shorten either to "value chain". Record the stages of the industry value chain where the subject does business as the business scope in its organization profile, and cover the market structure of those stages in the micro environment.

## Modules

| Order | Module | Question it answers | Main categories | Reference file |
|---|---|---|---|---|
| 0 | Scoping | What do we look at, and how far? | Subject, topic, topic overview, geography, time frame, purpose | SKILL.md |
| 1 | Macro environment | What broad changes are happening outside the subject? | Policy, regulation, economy, society, technology, environment | references/macro.md |
| 2 | Micro environment | How are the subject's market and industry structured? | Market, industry value chain, competition, customers, investment | references/micro.md, references/five-forces.md |
| 3 | Internal status | What does the subject have, and how does it operate? | Organization profile, capability assessment, regional innovation resources | references/internal.md |
| 4 | Benchmarking | What did comparable subjects do, and how do they differ from the subject? | Cases, success factors, limiting factors, gaps | references/benchmarking.md |
| 5 | Implications | What do the collected facts mean for the subject? | Implications grouped by source stage | SKILL.md, references/writing.md |

references/sources.md (data collection and source verification) and references/writing.md (report writing) apply to every module.

Place the modules you run in the order of the table. Moving from broad external change toward the subject's inside lets each later module draw on facts from the earlier ones. Skipping modules is allowed. Going straight from the macro environment to internal status is fine as long as the order holds.

## Mapping requests to modules

| Example request | Scope to run |
|---|---|
| Summarize policy trends | Policy category of the macro environment |
| Technology trends, paper and patent trends | Technology category of the macro environment |
| Current regulations | Regulation category of the macro environment |
| Market size and outlook | Market category of the micro environment |
| Competitive structure, Five Forces | Competition category of the micro environment, procedure in references/five-forces.md |
| Key companies | Key players within the competition category of the micro environment |
| R&D investment trends, national R&D project analysis, venture investment trends | Investment category of the micro environment. For a region subject, projects and corporate R&D spending within the region go to internal status |
| Industry value chain structure | Industry value chain category of the micro environment |
| Internal capability assessment, VRIO, SPROC | Internal status for an organization subject |
| Organizational value chain, analysis of internal activities | Internal status for an organization subject, organizational value chain framework |
| Regional innovation resources, regional industry conditions | Internal status for a region subject |
| Overseas best practices, cases from other regions | Benchmarking |
| External and internal environment analysis | Module set chosen from the defaults by purpose |
| Regional R&BD assessment | Full default set for a region subject |
| Implications only, from existing material | Register the provided material as facts, then run the implications module |
| Review of an existing environment analysis report | Review of an existing analysis |

Within a module, run only the requested categories. A request for policy trends does not produce technology, economy, or society sections.

### Defaults by purpose

When the user states a purpose without naming modules, propose the following sets as defaults.

| Purpose | Default modules |
|---|---|
| Trend monitoring | Macro environment, plus the micro environment when needed |
| Situation assessment | Macro environment, micro environment, internal status |
| Preparation for strategy work | Macro environment, micro environment, internal status, benchmarking |
| Preparation for R&D planning | Policy and technology in the macro environment, market and investment in the micro environment |

### Default categories by subject type

| Subject type | Macro environment | Micro environment | Internal status | Benchmarking |
|---|---|---|---|---|
| Organization | Only categories relevant to the topic | Market, competition, customers | Organization profile, capability assessment | Competing organizations, leading organizations |
| Region | Overseas and national policy and technology | Market, industry value chain, competitive structure | Regional innovation resources | Overseas cases, cases from other regions |
| Industry and technology area | Policy, regulation, technology | Market, industry value chain, competitive structure, investment | Runs as an organization only when the user names a subject organization | Leading countries and leading companies |

To analyze a government program or project, treat the organization that runs it as the subject and apply the organization type.

## Workflow

### Step 1 Scoping

Settle the following items.

| Item | Content | Default |
|---|---|---|
| Subject type and subject | One of organization, region, or industry and technology area, plus the specific name | None. Ask if missing |
| Topic | Industry, technology, product, service, or policy field to analyze | None. Ask if missing |
| Geography | Global, national, regional | Global and national. Add regional for a region subject |
| Time frame | Period for the current situation and period for the outlook | Last 5 years for the current situation, 5 years for the outlook |
| Purpose and use | Internal review, external submission, input to later analysis, and so on | Propose a value inferred from the request. Internal review if there is no clue |
| Modules and categories | Chosen from the request mapping and the defaults | Result of the request mapping |
| Verification level | Level 1 to 3 | Result of the selection rule in references/sources.md |
| Output format | Bullet report in markdown, tables, file format, output language | Bullet report in markdown, written in the user's language |

Fill items the request leaves open with defaults, build a scope proposal, and confirm it in one round. Splitting questions across several turns adds burden for the user. If the subject or the topic is missing, the analysis cannot start, so ask only for that item. When Five Forces is in scope, include industry definition, industry value chain breakdown, geographic scope, and time scope in the same confirmation. If the user says to proceed without confirmation, proceed with the defaults and record the applied scope in the report's scope section.

Once the scope is settled, run to the end on your own. After that point, questions to the user are limited to confirmation steps at verification level 2 or 3, requests for access to internal data, confirmation of query conditions for complex databases, and the internal data confirmation list.

When the topic is an industry or a technology, write a topic overview in the scope section at the start of the report. For a partial analysis covering a single category, write it only if the user wants it. The topic overview covers the topic's definition and what is included and excluded (What), how it works or is implemented (How), and its importance as confirmed by sources (Why). Decide here whether adjacent industries or related technologies are part of the analysis or treated as substitutes. The topic overview also uses sourced facts only.

### Step 2 Checking data channels

Before starting, check which connectors, APIs, and databases are available. If the task needs material that is not on the public web, such as internal data for the internal status module, paid investment databases, exports from national R&D databases, or internal statistics, send the user one list of the material needed. Do not fill missing material with guesses from web results. Leave it as unconfirmed. Explore complex databases while confirming query conditions with the user. Channel rules and the database exploration procedure are in references/sources.md.

### Step 3 Collection and the fact register

Before collecting, set the questions each module needs to answer. Look for material that supports each question and for material that contradicts it. Collecting only one side tilts the conclusion toward the first guess.

Record each collected fact as one row in the fact register.

| Field | Content |
|---|---|
| ID | Format MAC-01, MIC-01, INT-01, BMK-01. Implications use IMP-01 |
| Module and category | For example: macro environment, policy |
| Fact statement | One fact per sentence |
| Figure and unit | If the fact contains a figure |
| Reference date | The year or date the material refers to |
| Source | Citation format from references/writing.md |
| Data channel | Web, provided file, connected system |
| Status | Confirmed, approved by user, unconfirmed |

Split a sentence that mixes two facts. A list organized as a table (policies, companies, facilities, and so on) counts as one bundle of facts with a single ID. If the user provides an earlier fact register or earlier results, keep the existing IDs and append new facts.

### Step 4 Verification

Apply the procedure for the chosen verification level, and select sources using the quality criteria for each data channel. Recheck every figure in code. Details are in references/sources.md.

### Step 5 Module analysis

Follow the procedure in each module's reference file. Module sections contain facts and procedure-defined ratings only.

### Step 6 Deriving implications

Apply the implication rules below.

### Step 7 Writing and checking

Write the report in the format of references/writing.md, then run the final check at the end of this file.

## Implication rules

Implications are the inductive conclusion of the analysis. When a later stage exists, they become its input.

- (Induction) Draw a shared meaning from one or more facts or ratings, write it as one sentence, and add the IDs of the supporting facts in parentheses at the end. For an implication drawn from a rating, cite the IDs of the facts behind that rating
- (Grouping by source stage) Group implications by stage: macro environment, micro environment, internal status, benchmarking. Implications from the macro and micro stages describe external factors, and implications from internal status describe internal factors. Implications from benchmarking can be either, depending on the comparison. This grouping keeps later stages from mixing external and internal factors
- (No prescriptions) Implications state what the findings mean for the subject: conditions that open opportunities, conditions that create risk, gaps, and prerequisites. They do not state actions to take
- (No SWOT labels) Do not tag implications as strengths, weaknesses, opportunities, or threats
- (Complete coverage) Every fact in the report feeds at least one implication. A fact that feeds no implication has weak relevance to the topic, so remove it from the report body
- (Partial runs) Write implications only for the modules you ran. If the user wants facts only, skip implications

## Review of an existing analysis

When the user asks for a review of an environment analysis that already exists, check the following items without running a new analysis.

| Item | Criterion |
|---|---|
| Order | The order of macro environment, micro environment, internal status, benchmarking, implications is intact |
| Links | Later sections build on facts from earlier sections. No isolated items without links in either direction |
| Analysis and prescription boundary | Analysis sections do not jump ahead to to-be states, solutions, or strategies |
| Implication links | Each implication has supporting facts, and every fact feeds an implication |
| Structure | Conclusions come first, parent and child bullets relate as conclusion and evidence, and items on one level follow one grouping basis |
| Classification | Items do not overlap or leave gaps, and one level holds four items or fewer |
| Sources | Sources pass the quality criteria in references/sources.md. News reports are traced to original sources |
| Figures | Each figure has a source and reference date and matches a recheck in code |
| Sentences | The text passes the writing check in references/writing.md |

- Report the result per item as pass or fail, with the location of each failure and a direction for improvement. If the order needs rearranging, include a proposed arrangement
- Replace low-quality sources with high-quality ones. If no replacement exists, mark the claims that rely only on that source for deletion
- The review evaluates the material under review, so point out problems in concrete terms. Describe the structural problem directly, as in "the conclusion is missing from the start of the section", without naming thinking frameworks
- If the user wants a revised version, deliver it along with the review

## Handing over to later analysis

If the user plans to feed the results into SWOT, gap analysis, strategy work, research topic discovery, or similar tasks, deliver the implications grouped by source stage together with the fact register. The later task can separate external and internal factors by the source stage of each implication.

## Intermediate outputs

If the environment can save files, keep the scope proposal, the fact register, module drafts, and the final report as separate files. This lets work resume after an interrupted session and lets a third party trace the process. If saving files is not possible, keep the same structure within the response.

## Final check

- The modules you ran match the requested scope
- Modules appear in the order macro environment, micro environment, internal status, benchmarking, implications
- Every fact has an ID, a source, and a reference date
- No fact comes from model memory and no figure lacks a source
- Every figure was computed or rechecked in code
- Module sections contain no interpretation, to-be states, or solutions
- The macro, micro, and internal classification follows the controllability criterion
- Each module builds on facts from earlier modules, with no isolated items
- Every implication cites supporting fact IDs and every fact feeds an implication
- The output contains no SWOT labels, strategies, initiatives, or support needs
- The confirmation steps of the chosen verification level were completed
- No personal or confidential information from internal data appears in the output
- The report passes the writing check in references/writing.md

## Reference files

| File | When to read |
|---|---|
| references/macro.md | When running the macro environment module |
| references/micro.md | When running the micro environment module |
| references/five-forces.md | When running competitive structure analysis or Five Forces |
| references/internal.md | When running the internal status module |
| references/benchmarking.md | When running the benchmarking module |
| references/sources.md | In every run, when collecting and verifying material |
| references/writing.md | In every run, when writing the report |
