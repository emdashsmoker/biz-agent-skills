> This English edition is a translation of the Korean original. Some rules were adapted to English writing conventions, and the skill may behave differently from the intent of the original.

# Macro Environment Analysis

The macro environment module covers broad changes the subject cannot control and has no direct exchange with. Its purpose is to record, as facts, the external changes that affect the topic. It contains no interpretation, no evaluation of outlooks, and no solutions.

## Choosing categories

If the user names a framework, follow it. If not, choose only the categories that affect the topic and use a free composition. Do not list categories unrelated to the topic just to fill a template.

| Framework | Categories and order |
|---|---|
| PEST | Political, economic, social, technological |
| STEEP | Social, technological, economic, environmental, political |
| PESTEL | Political, economic, social, technological, environmental, legal |
| Free composition | The categories among policy, regulation, economy, society, technology, and environment that the topic needs. Order follows what the report emphasizes |

R&D topics often use a free composition centered on policy, regulation, and technology. These frameworks grew in practice from Aguilar (1967), who divided the environment into economic, technical, political, and social sectors in his study of how executives scan their environment. They are not theories with a single correct composition, so choose categories by fit with the topic.

The political category of a framework corresponds to the policy category, and the legal category to the regulation category. When the named framework has no legal category, place regulation facts under a separate subheading inside the political category.

Macro frameworks do not cover markets, industries, competitors, or investment. The micro environment module handles those separately.

## Items to collect by category

Fill each category with facts that answer its question below. The category of a fact follows the described-object criterion in SKILL.md.

| Category | Question it answers | Items to collect | Main source types |
|---|---|---|---|
| Policy | What are the political conditions and the directions governments have set, at home and abroad | Political conditions (changes of government, international relations, trade disputes), national strategies, plans required by law, plans drawn up without a legal mandate, policy packages, policies of major foreign countries | Releases from ministries and local governments, plan documents, reports from international organizations |
| Regulation | Which rules set rights, duties, and eligibility | Enactment and amendment of laws, tighter and looser regulation, permits, standards, certification, disclosure duties | Legal information systems, legislative records, standards bodies |
| Economy | How is the economy as a whole moving | Growth, prices, interest rates, exchange rates, trade, commodity prices | Central banks, statistics agencies, international statistics |
| Society | What is changing among people and social groups | Demographics, employment, consumer behavior, social issues, attitudes and values | National statistics, official surveys |
| Technology | Where does the technology stand on its growth curve | Performance metrics and limits, technology level and gaps, TRL, papers, patents, standardization, demonstration results and commercialization, technology convergence | Academic databases, patent databases, standards bodies, research institute reports |
| Environment | How is the state of nature and resources changing | Climate and weather, greenhouse gas emissions, resource reserves and consumption, pollution and waste, natural disasters | Observation statistics and reports from governments and international organizations |

Facts that share a keyword but describe different objects go to different categories, as below.

| Fact | Category |
|---|---|
| Budget, call for proposals, and selection results of a government program | Micro environment, investment |
| R&D investment amounts, project counts, budget trends | Micro environment, investment |
| Market size and growth of a specific industry, share prices of a sector or a company | Micro environment, market or competition |
| Funds raised by companies in environmental or social fields | Micro environment, investment |
| Environmental regulations, emissions disclosure duties | Regulation |
| Carbon reduction strategies, energy plans | Policy |
| Greenhouse gas emissions, temperature observations | Environment |

## Organizing policy trends

Organize policy by jurisdiction level and policy area.

- (Jurisdiction level) Major foreign countries, national, regional
- (Policy area) Industrial and technology policy, science and technology policy

Build a table for each combination, only where material exists. The default lookback period is the last 5 years.

| Year | Country or agency | Policy name | Background | Content | Measures | Expected effects |
|---|---|---|---|---|---|---|

- Each row is a document that sets a direction: a strategy, a plan required by law, a plan drawn up without a legal mandate, or a policy package. For a plan required by law, record the mandating law with the policy name
- When the document names a program as a means of delivery, record only the program's name in the measures column. Record that program's budget, call for proposals, and selection results in the investment category of the micro environment
- Record a planned amount stated in the document in the content column, marked as a planned amount. Record budgeted amounts, executed amounts, and yearly trends in the investment category
- The expected effects column carries the effects stated in the policy document itself. Keep the analyst's evaluation out of it
- Use the official full names of policies and agencies

If the subject is a region or a local government, move that region's own policies to internal status. This follows the controllability criterion in SKILL.md.

## Organizing regulation

Organize regulation in a table separate from policy. A document that sets a direction and a rule that sets duties affect the subject in different ways.

| Year | Country or agency | Law or rule name | Stage | Background | Duties and criteria | Who it applies to |
|---|---|---|---|---|---|---|

In the stage column, record the stage the source confirms (proposed or announced, enacted, in force) with its date. A legal provision that requires a plan goes in this table, and the plan drawn up under that provision goes in the policy table.

## Technology scope

Before collecting technology trends, define the scope of the technology in a table. Technology classification schemes differ by organization and are revised often, so define the scope with the items below, which apply under any scheme.

| Item | Content |
|---|---|
| Parent technology | The technology one level above the technology under analysis |
| Unit of analysis | The technology under analysis and its sub-technologies. The unit at which facts are collected and compared |
| Dividing basis | One basis that separates technologies on the same level: principle, material, process, function, or use, whichever the field itself uses |
| Adjacent technologies | Technologies on the same level that differ from the unit of analysis, and whether each is included |
| Relation | The relation between the unit of analysis and each adjacent technology: kind, component, alternative, or means |

- Build the scope table from a classification confirmed in provided material or web sources. When you use an official scheme (a patent classification, a standard classification, an agency's technology classification), record its name and edition
- For each source, confirm the technology scope it covers from its definition, classification codes, or search query, and compare it with the scope table. Put only sources with a matching scope in the same table and the same time series
- Record a source with a wider or narrower scope separately, with its scope stated. A figure for the parent technology carried over as a figure for a sub-technology becomes a fact about a different object
- For technologies in an alternative relation, record level and TRL for each unit of analysis. Platforms built on different principles can differ in maturity
- Treat objects in a means relation, such as a process and the equipment that performs it, as separate units of analysis. For example, additive manufacturing is a process and a 3D printer is equipment
- A search query for papers or patents is the operational definition of the technology scope. Record keywords, classification codes, period, and database in the citation, by the rules in references/sources.md

## Organizing technology trends

Build technology trends from evidence that shows where the technology stands on its growth curve. Performance rises slowly at first with cumulative R&D effort, then quickly, and slows again near the physical limit (Foster 1986). The same effort yields different gains at different stages, so the evidence for the stage is indicators of performance and maturity. Money and people put into R&D belong to the investment category of the micro environment.

| Evidence type | Items to check |
|---|---|
| Performance and level | Trend of the key performance metrics, theoretical limits or targets, level and gap against the technology leader |
| Papers | Main research streams, most-cited topics, emerging keywords and convergence fields, leading research institutions |
| Patents | Technology areas with growing filings, top applicants, filing countries, technology concentration |
| Standards | Standardization launched and finalized, participating organizations |
| Demonstration and commercialization | Prototype demonstrations, performance and operating environment confirmed in demonstrations, commercial product launches |

Build the table below for each level: overseas, national, and regional. The unit of analysis column carries the unit from the technology scope table.

| Year | Unit of analysis | R&D organization | R&D content | TRL | Basis for TRL |
|---|---|---|---|---|---|

Record a TRL only when the source states the level or the source's description clearly fits the definitions below. If the basis is thin, record it as unconfirmed. An estimated TRL presented as a confirmed value distorts later judgments of technology maturity.

| TRL | Definition |
|---|---|
| 1 | Basic principles observed |
| 2 | Technology concept formulated |
| 3 | Experimental proof of concept |
| 4 | Technology validated in lab |
| 5 | Technology validated in relevant environment |
| 6 | Technology demonstrated in relevant environment |
| 7 | System prototype demonstration in operational environment |
| 8 | System complete and qualified |
| 9 | Actual system proven in operational environment |

TRL started at NASA. The definitions above are the general definitions in European Commission Horizon 2020 General Annexes G (2017). If the user specifies field-specific TRL definitions (for example, those set by the responsible agency), use those.

## Order of writing

Within each category, write overseas trends first and then national trends. If the geography includes a region, put regional trends last. When a relationship between overseas and domestic trends (influence, response, difference) is confirmed as fact, record it too. Requests limited to domestic trends skip this order.

## Writing principles

- Describe objective conditions and trends only. Leave out to-be states, solutions, and the analyst's evaluation of outlooks
- Outlooks published by a source can be recorded as facts, together with who made the outlook, the publication year, and the outlook period
- Choose only changes that affect the topic
- Do not record the same fact under several categories. Place each fact in the one category that fits the object it describes
- Record each fact in the fact register with a MAC- ID

## Check

- Categories follow the user's framework or fit with the topic
- Each fact sits in the category that fits the object it describes
- Market, industry, competitor, and investment content sits in the micro environment module
- Every row of the policy table is a document that sets a direction, and program budgets and calls sit in the investment category
- Regulation sits in a table separate from policy
- The expected effects in the policy table repeat what the policy documents state
- A technology scope table exists, and the scope of each source behind a technology fact matches it
- Technology facts are indicators of performance and maturity
- No TRL is estimated without basis
- Writing moves from overseas to national to regional
- No interpretation or prescription is mixed in
