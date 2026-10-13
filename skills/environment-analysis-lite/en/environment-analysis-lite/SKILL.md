---
name: environment-analysis-lite
description: "Researches the external environment (macro, industry and market), internal capability, and benchmark cases, and organizes them into traceable facts and implications for any subject (company, public agency, region) and target (industry, technology, market, policy). Covers PEST, PESTEL, STEEP, industry value chain, Five Forces, industry statistics, investment trends, VRIO, an internal review based on Arthur D. Little's SPRO plus culture, and benchmarking. Runs full or partial analysis (e.g., only Five Forces). Screens public, submitted, and internal-system sources by channel-specific quality rules and scales verification to the output's use. Does not produce SWOT or strategy. Use when the user asks for environment analysis, macro or micro environment, industry or market analysis, policy, technology, or investment trends, competitive landscape, PEST, STEEP, Five Forces, VRIO, SPRO, capability assessment, benchmarking, regional industry conditions, or a situation review before strategy planning."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Strategic Environment Analysis

> This English edition is a translation of the Korean original. It may not behave exactly as the original intends. Where the two editions differ, the Korean edition states the intended logic.

Before a strategy or program is planned, this skill researches the external environment and internal capability and organizes the results into facts and implications with traceable sources. The output ends at implications. SWOT factor classification, vision, strategy, action items, and support measures are out of scope. When a request includes them, write the environment analysis and point to a follow-up task for the rest. Terms carry only the meanings in the Definitions table.

## Scope

Most environment analysis requests need one part of the work. Do only the scope the user asked for and do not create modules the user did not request.

| Request type | Example request | Work performed |
|---|---|---|
| Full analysis | "External and internal environment analysis of the XX industry in XX region" | Target overview, all four modules, implications |
| Module analysis | "Five Forces analysis of the XX industry", "Internal capability assessment of our agency" | That module and its implications |
| Item analysis | "Table of overseas XX policy trends over the last five years", "Benchmark three overseas cases" | Table and description for that item, implications only on request |

## Definitions

| Term | Definition |
|---|---|
| Subject | The organization or region that will use the results. It is the reference point for sorting modules. An analysis may have no subject, as in an industry trend report |
| Target | The industry, technology, market, or policy field under study |
| Module | One of four analysis units: macro environment, micro environment, internal capability, benchmarking |
| Fact | A statement of a phenomenon, figure, or event confirmed by a source. It contains no interpretation or prescription |
| Implication | A statement that groups several facts and condenses what they mean for the subject. It contains no action proposal |
| Outlook | A forecast stated by a source. The skill does not create its own forecasts |
| Evidence register | A list of sources used, with number, access channel, publisher, title, reference date, location, and quality grade |
| Verification level | How strictly sources are checked. Three levels: 1, 2, 3 |
| Industry value chain | Industry stages from raw materials and parts to final demand, listed from upstream to downstream. Used in the micro environment to divide markets |
| Organizational value chain | The value-creating activities inside one organization, divided into primary activities (inbound logistics, operations, outbound logistics, marketing and sales, service) and support activities (firm infrastructure, human resource management, technology development, procurement) (Porter, 1985). Used only in internal capability to divide the subject's activities. For organizations with a different activity mix, such as public agencies, relabel them as actual work units |

## Module Sorting Rule

The same data can belong to different modules depending on its relation to the subject. One criterion decides placement: how far the subject can control or influence the factor. Borderline data is placed by the rules below the table.

| Module | Criterion | Typical items |
|---|---|---|
| Macro environment | External factors the subject cannot influence | Policy and institutions (including regulation), economy, society, technology, natural environment, law |
| Micro environment | Industry and market the subject interacts with through trade, competition, or cooperation | Industry value chain, market size, competitors, customers, suppliers, investment flows |
| Internal capability | Resources and capabilities the subject owns or operates | Staff, funding, facilities, ongoing programs, organizational value chain activities, organization, culture, firms and institutions located in the region |
| Benchmarking | Results and practices of other entities used as reference | Overseas cases, other domestic regions, peer organizations |

- Firms, universities, research institutes, and industry statistics of a region go to internal capability when the subject is that region, and to micro environment when the subject is a company
- Directions and institutions stated in policy documents go to macro environment. Money flows such as budget execution and investment attraction go to investment trends in micro environment. Policies set by the subject itself and programs it runs go to internal capability
- Competitors' market share and size go to micro environment. Competitors' practices studied to learn from them go to benchmarking
- With no subject, skip the internal capability module and write the micro environment from the viewpoint of the whole industry

## Workflow

The work runs in five stages. Each stage leaves an output that can be checked, and the next stage starts only after the pass condition is met. Pass conditions are defined as states another person can compare directly, such as tables, numbers, and links.

| Stage | Output | Pass condition |
|---|---|---|
| 1. Scope setting | Scope definition | Purpose, subject, target, geographic scope, research period, outlook horizon, work scope, and verification level are all recorded |
| 2. Data collection | Evidence register | Each research item in scope is linked to a source or has a recorded reason for not being obtained |
| 3. Module analysis | Facts and tables per module | Every fact has a fact ID and an evidence register number |
| 4. Implications | Implication list | Every implication cites fact IDs, and every fact is used by at least one implication (skipped for item analysis unless implications were requested) |
| 5. Check and assembly | Final output | All pre-delivery checks pass |

- If the environment can save files, save each stage output to a file so the work can resume after an interruption
- If a later stage changes an earlier output, re-check the earlier stage's pass condition
- When three minor issues accumulate (unknown source date, figures that differ between sources, unclear scope, and so on), pause and report them to the user together
- Before reporting an issue, confirm it exists in the source text, figures, or link. Do not report unconfirmed suspicions
- For a stage with no means of checking its pass condition, say so and mark its output as unverified

### Stage 1 Scope Setting

The scope definition is the basis for every later judgment. Keep the definitions, criteria, and scope fixed until the end. If they must change, tell the user and redo the affected stages.

| Item | What to decide | Default |
|---|---|---|
| Purpose | Use of the output (trend review, situation review, preparation for strategy planning, and so on) and readers | Inferred from the request, situation review if unclear |
| Subject | A company, a public agency, a region, or none | Inferred from the request, none if unclear |
| Target | Name, inclusions, exclusions (whether adjacent fields are included or treated as substitutes) | Required input |
| Geographic scope | Domestic only, overseas only, domestic and overseas combined, domestic and overseas separate | Domestic and overseas combined |
| Research period | Past period for trend research | Last five years |
| Outlook horizon | Current (no outlook), mid term (up to 3 years), mid to long term (up to 5 years), industry life cycle (up to 10 years), very long term (up to 30 years), user defined, unlimited | Mid to long term |
| Work scope | Full analysis, module analysis, item analysis | From the request |
| Verification level | 1, 2, 3 | From the verification level table |

- If required inputs are missing, ask for all of them in one message and apply defaults to the rest
- If the user cannot respond, proceed with reasonable defaults and record the applied scope in the target overview of the output
- For partial analysis, decide only the items that module needs. For example, a policy trend table needs only the target, geographic scope, and research period
- For full analysis, write a target overview. It covers the target's significance (facts confirmed by sources), definition and scope, working principle or business model, and industry value chain
- Write definitions with a broader category, components, and purpose. Do not repeat the defined word inside its definition
- Skip general definitions the reader already knows. Write only definitions needed to draw the scope

### Stage 2 Data Collection

Search for data in the order below. If an earlier channel yields data within the research period for an item, do not search for that item again in later channels.

1. User-submitted files
2. Connected tools: MCP servers, APIs, database query tools, document repositories, and collaboration tools connected to the environment
3. Web search and page reading: search both Korean and English sources
4. User request: for items not obtained through the channels above, list the data needed and likely holders, then ask the user to submit files or connect a tool

Data that general web search rarely finds needs the connected tool and user request channels prepared from the start.

| Data type | Examples | Typical holders |
|---|---|---|
| Investment trends | Venture investment deal counts and amounts, M&A, government R&D budgets and projects | Venture investment databases, national R&D information services (e.g., NTIS in Korea), budget disclosure systems |
| Internal capability | Staff, budget, program results, work processes, organizational culture | HR, finance, and project management systems, collaborative document tools, spreadsheets, email, messengers, internal databases, ontologies |
| Detailed statistics | Establishments, employees, and output by region and industry | National statistics portals, statistics APIs |
| Facilities and equipment | Research equipment specifications, open access status | National research equipment information services, institution disclosures |

- Mark items not obtained as "not obtained" and do not fill them with estimates. "Not obtained" never means "does not exist"
- Record in the evidence register: number (S-01 format), access channel, publisher, title, publication or reference date, location (full URL or system path), quality grade
- Start searches with one or two core words and narrow down based on results

Databases with complex structures (national R&D information services, venture investment databases, statistics databases, internal databases, and so on) differ in field meanings, code systems, and counting rules, so the rules of this skill alone cannot set the query method. Explore such data in the order below, confirming each step with the user.

- (Exploration plan) Present the items needed, candidate databases, and access method (connected tool, API, or the user querying and exporting), and get confirmation
- (Structure check) Confirm field definitions, classification code tables, query conditions, and update cycles from official documentation or the user's explanation. Ask about fields whose meaning is unclear and do not guess
- (Agreed conditions) Agree with the user before extraction on keywords, classification codes, period, currency unit, and deduplication rules (a multi-year project counted once per year, parent projects and subprojects counted twice, and so on)
- (Pilot extraction) Extract a small sample first, check it with the user for omissions and misclassification, fix the conditions, then extract the full set
- (Record) Write the final conditions, extraction date, and record count in the evidence register so the same extraction can be repeated
- (No access) If no tool can reach the database, ask the user to query and export with the agreed conditions. Do not change conditions or run the full extraction without the user's confirmation

### Stage 3 Module Analysis

Follow the rules of the module sections in scope. Apply the common rules below to every module.

- Give each fact an ID made of a module code and a sequence number: macro environment MA, micro environment MI, internal capability IN, benchmarking BM (e.g., MA-03)
- Keep interpretation, prescription, and target states out of fact statements. Include an outlook only when a source states it, together with that source
- Do not fill framework items that are irrelevant to the target only to complete the framework
- Run all calculations (change rates, CAGR, shares, location quotients, gaps) in code, and recalculate figures taken from sources in code to cross-check them
- Do not infer causation from time order or co-occurrence alone, and do not generalize from a few cases or one segment to the whole

## Source Rules

### Common Principles

- Knowledge sources are limited to user-submitted files, connected tool results, and web search results. Facts remembered by the model are not sources
- Do not write information that no source confirms. Mark it "unverified"
- Do not treat missing information as evidence of absence. Write "none" only for a scope that was fully surveyed, and state that scope
- Do not justify a claim by an institution's reputation alone. Base it on the content and method of the source
- State who produced a figure, when, and how, so a third party asking for the basis can get an answer. Example: "According to a 2024 survey by XX Institute, the domestic XX market is projected to grow from A in 2023 to B in 2028, a CAGR of N% (sum of industry revenue)"
- Public source format: Institution or author (year), title (URL). The URL is the full path of the page holding the information, never the domain alone
- Internal source format: System or tool name (reference date), document or table name (location in the tool)
- Submitted file format: File name (issuing organization, reference date), page or sheet location

### Public Source Quality

Judge public sources by the six criteria below.

| Criterion | High-quality signal | Low-quality signal |
|---|---|---|
| Editing and fact checking | Editorial responsibility and review process are visible | Self-published with no responsible editor |
| Publisher independence | Third party with no stake in the target | Interested party publishing for promotion or advertising |
| Data type | Primary data produced by the publisher | Reworked content with no original source named |
| Traceability | Original text, method, sample, and calculation basis can be checked | Assertions with no basis |
| Expertise | Peer reviewed or officially published by an expert body | Anonymous or expertise cannot be confirmed |
| Authorship | Human author and editorial responsibility confirmed | Unverifiable content that appears machine generated |

A source without traceability, or one judged machine generated, is graded Exclude even if it meets the other criteria.

| Grade | Handling | Example types |
|---|---|---|
| Cite directly | Cite as is | Official publications and press releases of central and local governments, official statistics, laws, parliamentary and audit reports, government research institute reports, international organization reports and statistics, peer-reviewed papers, patent gazettes, standards documents, official central bank and exchange data, research firm and consulting reports that disclose their methods, official documentation of large open source projects (technology topics) |
| Cite with conditions | Cite after tracing the original source or cross-checking with an independent source | General news reports (cite the original source they quote first), company announcements (limit to the company's own claims), preprints (mark as not peer reviewed), single-source claims, editorials and columns (limit to the author's view), association and interest group publications (note the interest), statistics aggregator sites and market report summaries (confirm the original source) |
| Exclude | Do not cite and treat as absent | Machine-generated reports and content farms, openly editable wiki text (original sources it cites can be traced and used), Q&A sites, personal blogs and personal social media, anonymous communities, sensational outlets with no fact checking, unsourced news roundups and card news, advertorials that copy company press releases, state propaganda outlets without editorial independence, sites with an unknown publisher |

- Judge sources not listed above individually with the six criteria
- Leave an outlet's popularity and political leaning out of the judgment. Apply the same criteria to outlets from opposing camps
- If every collected source is graded Exclude, do not write the claim. Leave it as missing information, then search again within the Cite directly types
- Exceptions: the user orders the use of a specific source, or the source itself is the object of analysis (e.g., a study of how misinformation spread)
- Write quality grades and exclusions in the output only when the user asks

### Internal Source Quality

Data from internal systems, collaborative document tools, spreadsheets, email, messengers, databases, and ontologies has no publisher, so the public source criteria do not fit. Grade internal data by the role the record plays in the organization, and leave the tool type (enterprise systems, collaborative document tools, spreadsheets, and so on) out of the judgment. A document in the same tool is a reference record when it is the project database the whole organization relies on, and an informal record when it is a personal memo.

| Criterion | What to check |
|---|---|
| Reference record | Whether the organization uses this record as the reference when it checks or updates the item (e.g., accounting software for revenue, a project database in a collaborative document tool for project status) |
| Reference time | Reference date and last modified date of the data. State the reference date for data outside the research period |
| Author and finalization | Author or owning unit, and whether the record is final (approval, status value, final mark). Distinguish drafts from final versions |
| Consistency across records | Whether values match when the same item exists in several records |
| Completeness | Whether query conditions or access rights left out some periods, units, or pages |

| Grade | Handling | Example types |
|---|---|---|
| Reference record | Cite as is with its reference date | Accounting and HR software data, documents finalized by approval or status value, databases in collaborative document tools or spreadsheets that the whole organization relies on, public disclosures |
| Working document | Cite with author and reference date. Cross-check figures when a reference record exists for the same item | Meeting minutes, draft reports, internal wiki and document pages in collaborative document tools, shared spreadsheets |
| Informal record | Never the sole basis for a figure. For qualitative review of work practices and culture, use only patterns confirmed across several records, in aggregate | Messenger chats, personal notes, opinions in email bodies |

- If the reference record for an item is unclear, ask the user about all such items in one message (e.g., whether revenue is referenced in the accounting software or in a revenue table in a collaborative document tool). If no answer is possible, use the latest record with the clearest author and modified date, and note that choice in the output
- When records disagree, use the reference record's value and note the difference. Without a reference record, write both values with their reference dates
- Query only within the user's access rights and never work around them
- Use personally identifiable information only in aggregated form. Do not copy an individual's chat or email text into the output
- Get the user's confirmation before putting data marked confidential into an output meant for external sharing

### User-Submitted Files

- Use submitted files as primary evidence and record the issuing organization and reference date in the evidence register
- If a submitted file is a news report or reworked material, apply the public source criteria for that type
- Use figures the user states in the conversation without confirmation, and cite them as "stated by user"

### Verification Level

Set the verification strictness by two questions: is there a chance to correct the output if it is wrong, and does it contain quantitative data.

| Correctability | No quantitative data | Quantitative data |
|---|---|---|
| Correctable (notes, drafts, and routine briefings seen only by the author or internal team) | 1 | 2 |
| Limited correction (reports sent outside, proposals, audit evidence, published papers, final reports) | 3 | 3 |

An output that has left the organization makes figure errors, factual errors, and citations of nonexistent sources all hard to correct. For that reason the limited correction row applies level 3 whether or not quantitative data is present.

- Announce the level in one line at the start. Example: "Verification level 2: the internal review draft includes market size figures, so quantitative data confirmation applies"
- If the user asks to raise or lower the level, move one step. If the user names a level, apply it. Do not add adjustment rules that are not in the table. If the user says "skip confirmation", skip the confirmation step for that turn only and return to the original level from the next turn
- (Level 1) Apply the source rules only
- (Level 2) Before writing quantitative data into the body, send a quantitative data confirmation request and use only approved figures. Replace figures the user corrects with the user's figures and leave out rejected figures
- (Level 3) Collect evidence for every citation, qualitative and quantitative, send a citation confirmation request, and use only approved items. When the user asks for a replacement, check the alternative source with the same procedure
- Level 3 evidence for web sources: existence (search result text for the institution and title), date (publication date text as found), access (whether the URL opened and the page title), content (text of the paragraph holding the cited content)
- Level 3 evidence for submitted files: date (reference date text in the document), content (text of the paragraph), match (whether the document title, issuing organization, and reference year fit the purpose of the citation)
- Level 3 evidence for internal data: system name and location, reference date, query conditions, text of the record or paragraph
- List every item planned for citation in the request, regardless of importance
- Present evidence as found, without summarizing or editing it. If a search returns nothing or access fails, state that as it happened. Never guess a URL or publication year
- While waiting for confirmation, do not write the content as fact, and do not slip unapproved figures in with hedges such as "about" or "estimated"

```
Quantitative data confirmation request
| No. | Item | Figure | Source |
|---|---|---|---|
| 1 | Domestic XX market size (2024) | 0,000 (currency unit) | XX Institute (2025), XX Market Report |
How to respond: approve (all or by number), correct (number and correct figure), reject (number)
Citation confirmation request
[Source list] number, source type (web, submitted, internal), source name, publication year, content to be cited
[Evidence per source] evidence items for each source type, as found
[Quantitative data] code (A, B, C), source number, source name, publication year, item, figure
How to respond: approve, correct, replace (search for an alternative source), reject
```

### Lawful Data Collection

- Do not work around site terms of use, access controls such as logins or paid subscriptions, or notices that prohibit collection
- Do not repeatedly copy a substantial part of a database or list. Use official APIs, download functions, connected tools, and user submission
- Summarize reports and articles in your own words. Limit direct quotes to short necessary phrases and cite the source
- Limit information about researchers and staff to what they disclosed in their professional role (affiliation, title, research field, published papers and projects) and use it only within the purpose of that disclosure. Do not collect personal contact details or private information

## Macro Environment Module

Record external changes the subject cannot alter, with a focus on facts.

- (Item selection) Use the framework the user names. Without one, pick only the items that affect the target
- (Framework contents) PEST covers political, economic, social, and technological factors. PESTEL adds the natural environment and law to PEST. STEEP covers social, technological, economic, environmental, and political factors in that order
- (Item order) Set it by purpose and emphasis. For R&D and industry analysis, policy and institutions and technology are often central, so review those two first
- (Overseas then domestic) Within each item, write overseas trends first and domestic trends next, showing the influence, response, or gap between them. If regional policy affects the target, write it after national policy even when the region is not the subject
- (Research period) Prefer data from the research period set in stage 1
- (Policy and institutions) Record them in the table below, including regulatory changes. If both industrial policy and science and technology policy apply, separate them with the field column. Record expected effects only as stated in the policy document

| Year | Country | Agency | Field | Policy or institution | Background | Main content | Instruments | Expected effects |
|---|---|---|---|---|---|---|---|---|

- (Technology) Record R&D trends in the table below. Use TRL (the nine-level technology maturity scale) values only as stated by the source. If the source gives none, mark an estimate with its basis and the TRL definition table used, or write "unknown" when the basis is weak. TRL definition tables differ across fields and agencies, so comparisons without a stated basis mislead
- (Papers and patents) When data is available, add time series tables of annual paper publications, patent filings, and major applicants

| Year | Country | Performing organization | R&D content | TRL | TRL basis and definition used |
|---|---|---|---|---|---|

- (Economy, society, natural environment, law) Record only indicators and events directly related to the target. Present indicators as time series of three to five years or more with CAGR

## Micro Environment Module

Record the industry and market in which the subject participates or competes. Show which parts of this market reflect the changes found in the macro environment.

### Industry Value Chain

- The industry value chain follows the definition above. Do not use organizational value chain activities (inbound logistics, operations, marketing and sales, and so on) as industry stage names
- Use stage names the industry uses. Use generic names such as "materials", "components", or "equipment" only when that industry uses them widely
- Divide stages so that they do not overlap and together cover the whole target industry

### Market and Companies

- Record market size (in monetary terms), growth outlook (outlook period and source required), and main indicators (revenue, employees, number of firms, and so on). With separate domestic and overseas scope, research domestic and global markets separately
- Record main companies in the table below. Company name, country or location, and size are required. Add or drop other columns to fit the data obtained. Describe how the companies compete with each other along with the table

| Company | Country or location | Size (revenue or staff, reference year) | Market share | Business areas and main products | Main customers | Competing fields | Latest developments |
|---|---|---|---|---|---|---|---|

### Industry Statistics

- Record establishments, employees, output or revenue, and value added as a time series table of three years or more, and calculate CAGR and share of total in code
- Express regional industry concentration with the location quotient. It is the industry's share of total employment in the region divided by the industry's share of total employment nationwide. A value above 1 means higher concentration than the national average
- State the industry classification standard and its revision with the source. Do not join years classified under different standards into one series

### Investment Trends

- Research public R&D budget execution, venture investment (deal counts and amounts by stage), and M&A
- Investment plans stated in policy documents go to the macro environment. Actual execution and investment results go here
- Follow the stage 2 table for access channels and mark items not obtained as "not obtained"

### Five Forces Competitive Structure

Rate the market's competitive structure with Porter's five competitive forces: threat of new entrants, bargaining power of suppliers, bargaining power of buyers, threat of substitutes, and rivalry among existing competitors.

- (Unit of analysis) Choose markets by industry value chain stage, the whole industry, or a mix. Split product groups or regions with different competitive conditions into separate units
- (Scope confirmation and user settings) If the user did not set units, identify the industry definition and industry value chain from submitted files or web search, draft the units, and confirm them with the user together with the geographic scope. Do not build the industry value chain from model knowledge alone. Follow units or rating criteria set by the user, and point out overlaps or gaps between units if found
- (Separate domestic and overseas) For each unit, analyze the global market first and the domestic market separately, rating each independently. Label it "global", not "overseas"

| Force | Items to collect |
|---|---|
| Threat of new entrants | Entry barriers (capital, technical difficulty, regulation and licensing), economies of scale, likely retaliation by incumbents, recent entries, government support for or restriction of entry |
| Bargaining power of suppliers | Number of suppliers, substitutability of inputs, supplier switching costs, suppliers' ability and progress in forward integration |
| Bargaining power of buyers | Number of buyers and purchase concentration, product differentiation, buyer switching costs, buyers' ability and progress in backward integration |
| Threat of substitutes | Presence of substitutes, price performance, switching costs, growth of substitute markets, extent of horizontal substitution |
| Rivalry among existing competitors | Number of competitors, market growth, fixed cost structure, product differentiation, exit barriers, government support or regulation, progress in horizontal integration |

| Force | High | Medium | Low |
|---|---|---|---|
| Threat of new entrants | Low entry barriers and active new entry | Entry barriers exist but actual entries are confirmed | High structural barriers from economies of scale, capital intensity, accumulated technology, regulation, and similar |
| Bargaining power of suppliers | Few suppliers, no substitute inputs, forward integration under way | Many suppliers, but some core inputs depend on a few | Many suppliers, input substitution happening, no drivers of forward integration |
| Bargaining power of buyers | High purchase concentration, low switching costs, backward integration under way | Balance of bargaining power confirmed in actual trade terms | Dispersed buyers, high switching costs, no alternative supply |
| Threat of substitutes | Commercial substitutes with better price performance are gaining share | Commercial substitutes exist but switching costs or performance limits restrict their spread | No commercial substitutes, or excessive switching costs |
| Rivalry among existing competitors | Many competitors, low growth, weak differentiation, high exit barriers | Competitors exist but market growth allows coexistence and price competition is limited | Oligopoly of a few firms confirmed, high growth, horizontal integration under way |

The table above is a reference. Actual ratings follow the evidence collected for each unit, using the rules below.

- Rate current strength by facts of industry structure: economies of scale, capital intensity, learning curve, patent barriers, network effects, licensing, incumbents' accumulated investment, supply concentration, switching costs
- Potential changes alone (government support, startup entry attempts, localization efforts, research on substitute technology, buyers considering in-house production) do not change the current strength of an industry with a solid structure. Reflect potential changes only in the outlook strength, and conservatively
- Do not set up government policy, industry growth, technology change, or complements as separate forces. Reflect them through their effect on the five forces
- Do not rate temporary changes such as business cycles as structural change
- Reflect vertical integration (suppliers' forward integration, buyers' backward integration) in bargaining power according to its stage: planned, in progress, completed. Reflect horizontal integration (M&A and alliances within a stage) in rivalry through changes in the number of competitors and concentration
- Do not extend features of an individual company or one segment to the whole unit
- Write the link from evidence to rating so a third party can check it, and keep implication statements separate from evidence statements
- Check that the five ratings within a unit do not contradict each other. For example, if the threat of new entrants is high and rivalry is low, confirm the evidence that lets both hold
- When units are split by industry value chain stage, the buyer power of an upstream unit and the supplier power of the next downstream unit rate the same transaction from opposite sides. If upstream buyer power is "Low" and the downstream unit also rates the upstream suppliers' power "Low", the pair contradicts itself. Cross-check every pair of adjacent units in reverse
- Do not give the five forces equal weight. Name the force with the largest effect on profitability in the summary row

- (Format) Force headings use `(Force : current→outlook) sentence noting the current state followed by the direction of change`. With a current-only horizon, use `(Force : High, Medium, or Low) sentence`
- Under each heading, split (Current) and (Outlook). Write the implication first and the evidence after it. With a current-only horizon, write without these prefixes
- In each unit, place the market status and main companies after the five forces. The rating is the conclusion and the market data is its evidence
- Give each unit a competitive environment summary and a competitive environment table. When units are split by industry value chain stage, never drop the unit tables in favor of a summary table alone. After the unit tables, add an industry-wide summary and summary table
- With separate domestic and overseas scope, the order is global units, global summary, domestic units, domestic summary, overall summary
- Use only the table format below for every competitive environment table and do not invent comparison tables

| Force | Strength (current) | Strength (outlook) | Content | Evidence | Data |
|---|---|---|---|---|---|
| Threat of new entrants | High, Medium, or Low | High, Medium, or Low | (Current) implication, (Outlook) implication | (Current) structural evidence, (Outlook) evidence of change | (Current) quantitative data, (Outlook) quantitative data |
| Bargaining power of suppliers, bargaining power of buyers, threat of substitutes, rivalry | Same | Same | Same | Same | Same |
| Summary | - | - | Character of the competitive structure from the five ratings, and the force with the largest effect | Structural evidence from interactions among forces | - |

- Keep each cell to one or two sentences and put detailed analysis in the body. Separate (Current) and (Outlook) inside a cell with a `<br>` tag
- With a current-only horizon, set the whole outlook column to "-" and write cells without the (Current) and (Outlook) prefixes or line breaks
- Rate the outlook differently from the current strength only when there is evidence of change
- Do not put unsourced figures in the data column. If data is missing, write the best available information and mark it "not obtained"
- Rate the industry-wide summary on the structure of the whole industry and record its basis separately. Do not use a simple average of unit ratings
- If the user asks for specific forces only, analyze only those. If the user asks for the body without tables, omit the tables

## Internal Capability Module

Record the resources and capabilities the subject holds, with a focus on facts. Cover strengths and weaknesses together and do not write improvement directions or needs. Make visible which items compare with the industry requirements found in the micro environment.

### Asset Inventory

Use the items below as the default research list for each subject type. Mark items without data as "not obtained".

| Subject type | Research items |
|---|---|
| Region | Large firms and small and medium firms located in the region (separate tables in the main company table format), links among innovation actors, anchor innovation institutions, industrial complexes and clusters, industry statistics, universities and related departments, research institutes, business support agencies, branches of public research institutes, testbed facilities and research equipment, data processing facilities, policies set by the region itself, ongoing programs, principal investigator level researchers |
| Company or public agency | History and organization, staff, budget and finances, businesses and products, facilities and equipment, data and intellectual property, ongoing programs |

Record list-type assets with the columns below.

| Table | Columns | Rules |
|---|---|---|
| Facilities and equipment | Owner, name, type (testbed, research equipment, data processing facility), specifications, quantity, use, open access status and terms of use | Specifications and quantities follow the owner's public disclosures |
| Ongoing programs | Category (externally funded R&D, self-funded R&D, non-R&D support program; externally funded means R&D run by regional institutions with central government funds when the subject is a region), ministry or managing agency, performing organization, program name, period, content, annual budget | List only programs currently under way and leave out planned applications or unselected programs. Keep R&D and non-R&D programs apart |
| Researchers | Affiliation type (company, university, research institute), name, affiliation, research field, representative public papers or projects | Limited to the public information defined in Lawful Data Collection |

### Capability Assessment

The internal review checks the subject's current state in five areas: the four areas of SPRO proposed by Arthur D. Little (strategy, process, resource, organization) plus culture. Culture is not part of SPRO and is added to review shared values and behavioral norms separately.

| Area | What to review |
|---|---|
| Strategy | Vision, goals, priority programs, direction of resource allocation |
| Process | Main work procedures (can be divided by organizational value chain activities), decision procedures, information systems, performance management |
| Resource | Staff size and expertise, funding, facilities and equipment, data, intellectual property, external partner networks |
| Organization | Structure, authority and responsibility, cooperation across units, governance |
| Culture | Shared values, leadership style, behavioral norms |

The VRIO assessment answers four questions with yes or no for each main resource and capability, then classifies the result with the table below (Barney, 1995).

- (Value) Does it help exploit opportunities or reduce threats
- (Rarity) Do few competing entities hold the same resource
- (Imitability) Does an entity without it face a cost disadvantage in obtaining it
- (Organization) Are the organization, procedures, and systems in place to use it

| Value | Rarity | Costly to imitate | Organization | Result |
|---|---|---|---|---|
| No | - | - | - | Competitive disadvantage |
| Yes | No | - | - | Competitive parity |
| Yes | Yes | No | - | Temporary competitive advantage |
| Yes | Yes | Yes | No | Unexploited competitive advantage |
| Yes | Yes | Yes | Yes | Sustained competitive advantage |

- Cite the supporting fact IDs for each result
- Rate rarity and imitability only when comparison data from the micro environment or benchmarking exists. Without it, write "undetermined"
- Collect facts in both directions, covering strengths and weaknesses together

## Benchmarking Module

Research the results and practices of other entities used as reference. Performance comparison measures the level gap with the same indicators. Practice comparison examines the methods and conditions that produced the results.

- (Case selection) Pick cases whose conditions (size, industry, stage of development, institutional setting) are comparable with the subject and whose results are public. Record the reason for selection and the differences from the subject
- (Case range) Pick overseas cases, other domestic regions, or peer organizations to fit the geographic scope. When the subject is a region, review both overseas cases and other regions
- (Practice comparison) Record in the table below

| Case | Country or region | Lead organization | Period | Actions | Results (quantitative basis) | Success factors | Constraints and failure factors | Differences from the subject |
|---|---|---|---|---|---|---|---|---|

- (Performance comparison) Align the subject's and the case's figures to the same indicator, reference year, and unit, then calculate the gap in code. If they cannot be aligned, write the difference in basis and leave out the comparison figures
- (Gap summary) Summarize gaps between domestic and overseas, and between the subject and other regions, with the performance comparison method
- (Balance) Research failure factors and constraints along with success factors
- (Link) Record which fact IDs in internal capability or the micro environment each case fact compares with
- Do not write adoption recommendations or application plans

## Writing Implications

An implication is a conclusion that groups several facts and condenses what they mean for the subject. Put the effort into gathering facts and keep implications short, enough to show direction.

- Format: `- (implication title) implication sentence [IM-01, basis: MA-02, MI-05]`
- Module codes of the supporting facts show whether an implication is an external factor (MA, MI) or an internal factor (IN). Implications based on benchmarking (BM) can serve either side
- Check that every fact is used by at least one implication. Delete facts no implication uses, since they are unrelated to the topic. Check list-type tables through the fact statements placed before or after them
- Do not write action proposals ("should be pursued", "needs expansion"). Keeping analysis apart from prescription lets later strategy work trace its evidence
- Keep the conclusion within the range of its supporting facts
- Trace back from implications to facts and from facts to the evidence register, and confirm that no link is broken

## Output Rules

### Report Structure

- For full and module analysis, state the overall conclusion as a proposition in the document title and put the implication list in the first section. Write implications only in that section and do not repeat them later. Item analysis without implications starts with its item section
- The order after that is target overview, macro environment, micro environment, internal capability, benchmarking. Skip modules not performed but keep the order
- An introduction of the subject (history, organization, budget, staff) may follow the target overview. Place the capability assessment after the environment analysis
- Put each section's conclusion in its first sentence
- Name headings so the content below is clear from the heading alone, and give each heading one topic. Do not combine two topics as in "Policy Trends and Technology Trends"
- Use either keyword headings or sentence headings throughout the document (Five Forces headings follow their set format). Name sibling headings in parallel (e.g., "Overseas Policy Trends", "Domestic Policy Trends"). Avoid repeating generic labels such as "Overview", "Background", or "Status"
- Keep three or four items at the same level where possible. With five or more, add a grouping level, and use one classification criterion
- Keep fact IDs and implication IDs in the output. If the user asks for a clean copy without IDs, make a separate version with the IDs removed

### Sentences and Format

- Write in concise report style with one message per sentence. Each of who, when, where, what, why, and how appears at most once in a sentence. Split the sentence if one appears twice
- Do not join clauses with conjunctions such as "and", "but", or "while", and do not use commas to join sentences. Use commas when listing three or more items of the same kind
- Write subheadings in the form "(subheading) content". Do not attach them with a colon or hyphen
- Use Markdown as follows: `#` document title, `##` sections, `###` subsections only when needed, `-` statements, `>` sources. Do not use indented sub-lists. Show relations between items with subheadings and IDs
- Place a source block right under the statement it supports. Separate multiple sources into blocks with blank lines
- Put list-type data (policies, companies, institutions, facilities, programs, researchers, statistics) in tables and interpretive facts in statements. Describe what a table shows before or after it, do not place tables back to back, and do not put tables inside quote or code blocks
- Pick at most three figures for the main messages and move the rest to tables. Use time series of three to five years or more, with CAGR and share
- Replace tildes with hyphens. Do not use em dashes, contrast constructions that negate one thing to assert another, unsupported count announcements ("three pillars" and similar), or inflated modifiers
- Do not write sentences about the output or the writing process ("This report", "Our research found", "The table below summarizes")
- Keep working terms (module, stage, evidence register, verification level, quality grade, unit of analysis, rating) out of the output. Framework names such as PEST, Five Forces, and VRIO, and the names of the five forces, may appear as section names
- Write the full name of technical terms and abbreviations at first use, and add a one-line explanation block `> (term) explanation` when needed

### Output Skeleton Example

```markdown
# XX industry in XX region: regional production base expands slower than overseas demand
## Implications of Environmental Change
- (Stalled domestic supply base) Number of domestic volume producers flat against rising overseas demand [IM-01, basis: MA-02, MI-05]
- (Regional testbed available) Regional testbed open to outside firms, able to absorb prototype validation demand [IM-02, basis: IN-04, BM-01]
## XX Industry Overview
- (Definition) Industry that produces B from raw material A and supplies it to C
- (Exclusions) D treated as a substitute and excluded from the target
- (Scope) Domestic and overseas combined, trends for 2021-2025, five-year outlook horizon
## Overseas Policy Trends
- (EU) XX regulation in force, tightening XX requirements for products sold in the EU [MA-01]
> Institution (year), title (full URL path)
## Competitive Structure
### (Threat of new entrants : Low→Medium) High equipment investment barrier persists, process standardization opens room for entry
- (Current) implication statement [MI-06]
- (Outlook) implication statement [MI-07]
```

## Pre-Delivery Checks

Confirm each item below by code or by comparison with source text. If any item fails, fix that part and check again.

- The work performed matches the requested scope, with no unrequested modules
- Every fact has a fact ID and a source, every public source URL is a full path, and database extracts have their conditions and extraction date in the evidence register
- Every figure in the body matches the value recalculated in code
- Every implication cites fact IDs, and every fact is used by at least one implication (checked by code that matches IDs)
- Each fact's module placement follows the module sorting rule, and industry and organizational value chains are not mixed
- Analysis sections and implications contain no prescriptions, target states, or recommendations
- If Five Forces was performed, unit tables, summary rows, cross-checks among forces, and cross-checks between adjacent units are all complete
- At verification level 2 or 3, no unapproved citation appears in the body
- No statement rests only on Exclude-grade sources, and no figure rests only on informal internal records
- Personal information and data marked confidential are used only within the rules
- No banned expressions or working terms remain (checked by string search)

Finally, reread the output as a critical reviewer. Fix or report only weaknesses that are confirmed, and do not invent weaknesses that are not.
