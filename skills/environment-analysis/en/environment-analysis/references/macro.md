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

Frameworks without a legal category, such as PEST and STEEP, place policy and regulation together in the political category and keep the two apart within it. Political maps to policy in the category definitions below, and legal maps to regulation.

Macro frameworks do not cover markets, industries, or competitors. The micro environment module handles those separately.

## Category definitions

Practitioner frameworks put different items under the same category name. This module divides categories by one criterion, the object that changes, and gives each category a question to answer.

| Category | Question it answers | Items to collect | Main source types |
|---|---|---|---|
| Policy | Under what political conditions, and in which direction, are governments at home and abroad moving | Political conditions (elections, changes of government, relations between countries, and so on), national strategies, statutory plans, non-statutory plans, industrial policy, science and technology policy, and so on | Releases from ministries and local governments, legislative records, reports from international organizations |
| Regulation | Which rules set an effective date and a scope and assign obligations and rights | Enactment and amendment of laws, permits, mandatory standards and certification, disclosure duties, deregulation and new regulation, and so on | Legal information systems, legislative records, regulator documents |
| Economy | How does the economy as a whole, at home and abroad, fluctuate | Growth, prices, interest rates, exchange rates, trade, employment indicators, and other economy-wide indicators | Central banks, statistics agencies, international statistics |
| Society | Which social phenomena are at issue at home and abroad | Demographics, values and ways of living, social needs and issues, and so on | National statistics, official surveys, research institute reports |
| Technology | At which stage of the S-curve is the topic technology | Performance trends, technology maturity and technology level, R&D trends, standardization, demonstration and commercialization, technology convergence, and so on | Research institute and expert agency reports, academic papers, standards bodies |
| Environment | What state is the natural environment in at home and abroad, and how is it changing | Climate, greenhouse gas emissions, resource depletion, ecosystems, pollution, and other physical states of the natural environment | Government and international organization reports, official statistics |

### Category boundaries

When a fact seems to span two categories, choose one by the boundaries below.

- (Regulation) Rules that set an effective date and a scope and impose obligations, prohibitions, or permit criteria go under regulation. A statutory plan drawn up under a law states a direction, so it goes under policy. Voluntary standards set by standards bodies go under technology
- (Government funding and purchasing) Programs through which a government allocates funds, and government purchasing, belong to the investment category and the customers and demand category of the micro environment, following the government role criterion in SKILL.md. Investment plan amounts stated in a policy document also go to the micro investment category as plan amounts
- (Whole economy and industry) The economy category holds only indicators of the economy as a whole that are not tied to a particular industry. Market size, growth, company valuations, and fundraising of the topic industry belong to the micro environment
- (Environment and neighboring categories) The environment category holds the physical state of the natural environment. The direction of climate action goes under policy, emissions disclosure duties and carbon pricing schemes go under regulation, and fundraising by green-sector firms goes to the micro investment category
- (Technology and investment) The technology category holds the performance and maturity of the technology itself. R&D spending and program budgets go to the micro investment category, while prototypes and demonstration results that come out of a program go under technology

## Organizing policy trends

Organize policy by jurisdiction level and policy area.

- (Jurisdiction level) Major foreign countries, national, regional
- (Policy area) Industrial policy, science and technology policy, and other areas the topic touches

Build a table for each combination, only where material exists. The default lookback period is the last 5 years.

| Year | Country or agency | Policy or strategy name | Background | Content | Measures | Expected effects |
|---|---|---|---|---|---|---|

The expected effects column carries the effects stated in the policy document itself. Keep the analyst's evaluation out of it.

## Organizing regulation

Organize regulation by jurisdiction level as well. The default lookback period is the same as for policy.

| Year | Country or agency | Law or regulation name | Type (enactment, amendment, entry into force, repeal, and so on) | Main content | Scope | Effective date |
|---|---|---|---|---|---|---|

Use the official full names of policies, laws, regulations, and agencies. If the subject is a region or a local government, move that region's own policies and regulations to internal status. This follows the controllability criterion in SKILL.md.

## Organizing technology trends

The technology category answers at which stage of the S-curve the topic technology stands. The S-curve traces how performance improves with the R&D effort put in. Improvement starts slowly, speeds up, and slows again as the technology approaches a physical limit (Foster 1986, Christensen 1992). Technologies that rest on different working principles follow their own S-curves, so divide the topic into technology units first and check the stage of each unit.

### Technology classification

Before collecting, divide the topic technology into technology units. If the report has a topic overview, place the classification in its definition and scope. If not, place it at the start of the technology trends section.

- Within one level, divide by one criterion such as working principle, material, function, or process (for example, superconducting, trapped-ion, neutral-atom, and photonic approaches by how the qubit is implemented, and so on)
- Units at the same level do not overlap and together cover the whole topic technology
- Units of different kinds, such as processes, equipment, materials, and products, sit in different levels or classifications (for example, additive manufacturing is a process and a 3D printer is equipment, and so on)
- Confirm the classification from sources such as provided material, standard terminology, academic literature, and official technology classifications, and record the source and reference date. Technology classifications are revised by agency and over time
- Confirm which technology unit a source's term refers to by the source's own definition. Use popular or marketing terms without a definition in facts only when the unit they refer to can be identified

| Parent technology | Technology unit | Classification criterion | Definition | Source |
|---|---|---|---|---|

### Recording by technology unit

- Record the technology unit with each fact, and keep each fact about a unit as a fact about that unit only
- When a source presents a figure or rating that groups several units, record the grouped scope with it
- For technology convergence, record every unit that is combined

### Evidence types

Check the S-curve stage with the evidence below, which shows performance and maturity.

| Evidence type | Items to check |
|---|---|
| Performance | Time series of key performance indicators, theoretical or physical limits stated by sources, and so on |
| Maturity | TRL, technology level assessments (level relative to leading countries, technology gaps, and so on) |
| R&D trends | Research content and results of the main research actors, paper and patent trends analyzed and published by research institutes, and so on |
| Standardization | Voluntary standards launched and finalized, participating organizations |
| Demonstration and commercialization | Prototypes, demonstration results, commercial product launches and diffusion, and so on |
| Technology convergence | Research and product cases that combine other technology units, and so on |

If paper or patent databases must be analyzed directly, follow the database exploration procedure in references/sources.md.

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

### S-curve stage rating

If a source states the stage of a technology unit, record it as a fact with the source. If not, rate the stage by the criteria below and attach the IDs of the supporting facts. If the basis is thin, record it as unconfirmed.

| Stage | Performance change | Observable signals |
|---|---|---|
| Early | Performance improves slowly for the effort put in | Work centered on proof of principle and prototypes, several technical approaches competing, no settled standard, and so on |
| Growth | Performance improves quickly for the effort put in | Rapid gains in performance indicators, standardization under way, expanding commercial products, and so on |
| Mature | Improvement slows as a limit approaches | Shrinking performance gains, a physical limit stated by sources coming close, new technical approaches appearing, and so on |

| Technology unit | S-curve stage | Basis for rating |
|---|---|---|

## Order of writing

Within each category, write overseas trends first and then national trends. If the geography includes a region, put regional trends last. When a relationship between overseas and domestic trends (influence, response, difference) is confirmed as fact, record it too. Requests limited to domestic trends skip this order.

## Writing principles

- Describe objective conditions and trends only. Leave out to-be states, solutions, and the analyst's evaluation of outlooks
- Outlooks published by a source can be recorded as facts, together with who made the outlook, the publication year, and the outlook period
- Choose only changes that affect the topic
- Do not record the same fact under several categories. If a fact spans two categories, place it in one by the category boundaries
- Record each fact in the fact register with a MAC- ID

## Check

- Categories follow the user's framework or fit with the topic
- Each category holds only what its definition covers, and no market, industry, program, or investment amount has slipped into the macro environment
- The expected effects in the policy table repeat what the policy documents state
- Each technology fact names its technology unit, and units at the same level are divided by one criterion
- No TRL or S-curve stage is estimated without basis
- Writing moves from overseas to national to regional
- No interpretation or prescription is mixed in
