> This English edition is a translation of the Korean original. Some rules were adapted to English writing conventions, and the skill may behave differently from the intent of the original.

# Macro Environment Analysis

The macro environment module covers broad changes the subject cannot control and has no direct exchange with. Its purpose is to record, as facts, the external changes that affect the topic. It contains no interpretation, no evaluation of outlooks, and no solutions.

## Choosing categories

If the user names a framework, follow it. If not, choose only the categories that affect the topic and use a free composition. Do not list categories unrelated to the topic just to fill a template.

| Framework | Categories and order |
|---|---|
| PEST | Political (policy, regulation), economic, social, technological |
| STEEP | Social, technological, economic, environmental, political (policy, regulation) |
| PESTEL | Political (policy), economic, social, technological, environmental, legal (regulation) |
| Free composition | The categories among policy, regulation, economy, society, technology, and environment that the topic needs. Order follows what the report emphasizes |

The parentheses after a framework category give the matching categories of this document. R&D topics often use a free composition centered on policy, regulation, and technology. These frameworks grew in practice from Aguilar (1967), who divided the environment into economic, technical, political, and social sectors in his study of how executives scan their environment. They are not theories with a single correct composition, so choose categories by fit with the topic.

Markets, industries, competitors, customers, and investment are categories of the micro environment module. Even under a macro framework, write them in the micro environment module.

## Items to collect by category

| Category | Question it answers | Items to collect | Main source types |
|---|---|---|---|
| Policy | What direction have political actors and governments at home and abroad set? | Political situation (elections and changes of government, conflicts and trade disputes between countries), national strategies, statutory and non-statutory plans, directions and targets of industrial and science and technology policy, policies of major foreign countries | Releases from ministries and local governments, statutory plans, reports from international organizations |
| Regulation | How are the rules the subject must follow changing? | Enactment and amendment of laws, permits, mandatory standards and certification, disclosure duties, deregulation and new regulation | Legal information systems, legislative records, standards bodies |
| Economy | How are conditions moving across the national and world economy as a whole? | Growth, prices, interest rates, exchange rates, trade, supply chains | Central banks, statistics agencies, international statistics |
| Society | What demographic changes and social phenomena are appearing? | Demographics, employment, consumer behavior, values, social needs and issues | National statistics, official surveys |
| Technology | Where on its maturity curve (S-curve) is the topic technology? | Performance level and rate of improvement, TRL, trends in papers and patents, standardization, results of demonstration and commercialization, technology convergence | Academic databases, patent databases, standards bodies, research institute reports |
| Environment | How is the physical state of the natural environment changing? | Climate, greenhouse gas emissions, energy and resource supply, ecosystems, natural disasters | Government and international organization reports, official statistics |

## Category boundaries

Place each fact by the kind of thing it describes. Apply the fact placement rules in SKILL.md first to facts that involve government. Split the boundaries that often overlap by the criteria below.

| Boundary | Criterion |
|---|---|
| Policy, regulation | A document that states a direction and targets is policy. A rule that binds the subject's conduct as a duty or grants permission is regulation. A statutory plan is a plan whose drafting a law requires, so it goes to policy |
| Economy, micro environment | Economy holds indicators aggregated over the national or world economy as a whole. The size and growth of the topic market go to the micro environment market category, share prices and stock trading of topic firms go to those firms' entries in the micro environment, and equity investment in topic firms goes to micro environment investment |
| Technology, investment | Technology holds the performance and maturity of the technology itself. Foster's (1986) S-curve shows performance against cumulative R&D effort, so the position on the curve is judged by the rate of performance improvement. R&D budgets and investment amounts are inputs on the horizontal axis of the curve, so they go to micro environment investment |
| Environment, other categories | The state of the natural environment measured in physical quantities, such as temperature, emissions, and resource reserves, is environment. Rules such as emissions disclosure duties and emissions trading schemes go to regulation, carbon neutrality strategies go to policy, and investment in green fields goes to micro environment investment. The emissions of an individual firm are an attribute of that firm, so they go to that firm's entry in the micro environment |

## Organizing policy trends

Organize policy by jurisdiction level and policy area.

- (Jurisdiction level) Major foreign countries, national, regional
- (Policy area) Industrial and technology policy, science and technology policy

Build a table for each combination, only where material exists. The default lookback period is the last 5 years.

| Year | Country or agency | Policy name | Document type | Background | Content | Measures | Expected effects |
|---|---|---|---|---|---|---|---|

- The document type column carries the nature of the document as the source states it, such as strategy, statutory plan, non-statutory plan, or roadmap
- Target investment amounts stated in a policy document go in the measures column. Individual programs with an allocated budget go in the public investment table in references/micro.md
- The expected effects column carries the effects stated in the policy document itself. Keep the analyst's evaluation out of it

Organize regulation by jurisdiction level in the table below.

| Effective date | Country or agency | Law or regulation name | Enactment or amendment | Main content | Who it applies to |
|---|---|---|---|---|---|

Use the official full names of policies, laws, and agencies. If the subject is a region or a local government, move that region's own policies and regulations to internal status. This follows the controllability criterion in SKILL.md.

## Organizing technology trends

The technology category gathers the basis for judging where on the S-curve the topic technology stands. If the source states the stage, record it as a fact. A stage the analyst judges goes in the implications section with the IDs of its supporting facts.

### Technology units

Define technology units first, then write technology trends unit by unit. A technology unit is the range of technology that improves the same performance metric through the same working principle, and it shares one S-curve. Technologies with different working principles or core performance metrics mature at different speeds, so they form separate units. Define a converged technology as one unit and name the units it combines.

- (Splitting units) Split into separate units when any one of working principle, base material, or core performance metric differs. For example, superconducting, trapped ion, neutral atom, and photonic quantum computers differ in the physical principle and critical equipment that realize their qubits, so each is a separate unit
- (Like siblings) Units at the same level belong to the same object type (material, device, process, equipment, software, application, and so on) and are split by one criterion. Additive manufacturing goes under the process type, and a 3D printer goes under the equipment type. When both a material criterion (silicon semiconductors, compound semiconductors) and a function criterion (memory, logic, RF, power) are needed, classify in separate levels
- (Official classification) Confirm the name and scope of each unit in an official classification, such as a patent classification, a national technology classification, or a standard terminology, and record the classification name and edition in the fact register. Official classifications get revised (for example, the IPC began moving semiconductor device classes from H01L to the new class H10 in stages from its 2023 edition), so the edition lets a third party query the same scope again
- (Counting by unit) Record paper counts, patent counts, and TRL by unit. If a source gives only a figure that combines several units, record the scope the source set and do not estimate a split into lower units

### Evidence types

Check the evidence types below for each technology unit.

| Evidence type | Items to check |
|---|---|
| Performance | Level and rate of improvement of the core performance metric, level against physical limits |
| Papers | Main research streams, most-cited topics, emerging keywords, leading research institutions |
| Patents | Technology areas with growing filings, top applicants, filing countries, technology concentration |
| Standards | Standardization launched and finalized, participating organizations |
| Demonstration and commercialization | Prototypes, demonstration results, commercial product launches |

The budget and selection results of demonstration programs go to public investment in references/micro.md.

Build the table below for each level: overseas, national, and regional.

| Year | Technology unit | R&D organization | R&D content | TRL | Basis for TRL |
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
- Do not record the same fact under several categories. If a fact seems to span two categories, choose one by the criteria in the category boundaries
- Record each fact in the fact register with a MAC- ID

## Check

- Categories follow the user's framework or fit with the topic
- Market, industry, competitor, customer, and investment content sits in the micro environment module
- Facts in each category meet the criteria in the category boundaries
- The policy table and the regulation table are separate
- Technology trends are organized by technology unit, and each unit carries its official classification name and edition
- The expected effects in the policy table repeat what the policy documents state
- No TRL is estimated without basis
- Writing moves from overseas to national to regional
- No interpretation or prescription is mixed in
