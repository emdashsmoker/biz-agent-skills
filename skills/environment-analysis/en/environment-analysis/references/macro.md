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

Category names differ across frameworks, but the questions in the category test below decide which facts go into each category. The political category follows the question of the policy category, and the legal category follows the question of the regulation category. PEST and STEEP have no legal category, so they keep regulation facts as a separate group inside the political category.

Macro frameworks do not cover markets, industries, or competitors. The micro environment module handles those separately.

## Category test

Each category answers one question. Place each fact in the category whose question it answers.

| Category | Question it answers | Items to collect | Main source types |
|---|---|---|---|
| Policy | What is the political situation at home and abroad, and what direction has the government set out | Elections and changes of government, international relations and geopolitical conflict, national strategies, statutory plans, non-statutory plans, industrial policy, science and technology policy, policies of major foreign countries, and so on | Releases from ministries and local governments, plan documents, reports from international organizations, and so on |
| Regulation | How are the rules that bind conduct changing | Enactment and amendment of laws, tighter or looser regulation, permits, standards, certification, taxation, disclosure duties, and so on | Legal information systems, legislative records, standards bodies, and so on |
| Economy | How are the aggregate indicators of the whole economy moving | Growth, prices, interest rates, exchange rates, employment, trade, economy-wide supply chain disruption, and so on | Central banks, statistics agencies, international statistics, and so on |
| Society | How are the state and behavior of people and groups changing | Demographics, values and lifestyles, consumer behavior, social problems and social needs, and so on | National statistics, official surveys, and so on |
| Technology | Where does the topic technology sit on its maturity curve, and in which direction is it changing | Performance trends, TRL, technology level by country, technology trends, technology convergence, stage of standardization and commercialization, and so on | Technology level assessment reports, technology roadmaps, review papers, research institute reports, standards bodies, and so on |
| Environment | How is the physical state of the natural environment changing | Climate change, greenhouse gas emissions, resource depletion, ecosystem change, pollution, and so on | Government and international organization reports, official statistics, and so on |

Names of policies, programs, ministries, and budget terms change across countries and over time. The function of a fact can be tested with the same question even when names change. Apply the rules below, which test function rather than name.

- (One fact, one place) Split even one document into facts and place each fact on its own. For example, the provisions of a law go to regulation, a national strategy based on that law goes to policy, and the budget of a support program the law creates goes to the investment category of the micro environment
- (Policy and program) A document that sets out goals, direction, and a list of measures (strategy, plan, roadmap, action plan, and so on) is policy. A unit that commits a budget and pays it to performers or beneficiaries (calls for proposals, grants, equity contributions, loans, and so on) is a program and goes to the investment category of the micro environment. Test what the document does rather than words such as "investment", "program", or "project" in its title. For example, an investment strategy for a field is policy, and a demonstration call in the same field belongs to the investment category of the micro environment
- (Amounts) Amounts of money directed at the topic go to the investment category of the micro environment, whether they are plans, budgets, or execution. Amounts printed in a policy document go there too. The policy category carries the direction and measures of the policy
- (Aggregate and specific) The economy category covers aggregate indicators of the whole economy. Indicators of parties the subject interacts with, such as growth of the topic market or share prices and fundraising of topic firms, belong to the micro environment
- (Rules and states) Binding rules (laws, regulations, disclosure standards, and so on) go to regulation. Measured values of the natural environment (emissions, temperature, resource reserves, and so on) go to environment. For example, a duty to disclose value chain (Scope 3) emissions is regulation, and the emissions of a country or a whole industry are environment. Reduction targets and strategies a government announces are policy
- (No duplicates) Do not record the same fact under several categories

## Organizing policy trends

Organize policy by jurisdiction level and policy area.

- (Jurisdiction level) Major foreign countries, national, regional
- (Policy area) Industrial and technology policy, science and technology policy, and other areas tied to the topic

A statutory plan is a plan whose drafting rests on a law. A non-statutory plan is a strategy, action plan, roadmap, or similar document drafted without such a law. Both set out direction, so both go to the policy category. The enactment or amendment of the law behind a plan goes to the regulation category.

Record the political situation (elections, changes of government, shifts in international relations, and so on) as bullets with the event, date, and source. Build a table of policy documents for each combination of jurisdiction level and policy area, only where material exists. The default lookback period is the last 5 years.

| Year | Country or agency | Policy name | Document type | Background | Content | Measures | Expected effects |
|---|---|---|---|---|---|---|---|

The document type column records the nature of the document, such as national strategy, statutory plan, or non-statutory plan. The expected effects column carries the effects stated in the policy document itself. Keep the analyst's evaluation out of it. Use the official full names of policies and agencies. Record investment amounts and sub-programs stated in a policy document in the investment category of the micro environment, following the category test rules.

If the subject is a region or a local government, move that region's own policies to internal status. This follows the controllability criterion in SKILL.md.

## Organizing regulation

Organize changes in laws, regulations, standards, and certification in a table for each jurisdiction level. Build tables only for levels where material exists.

| Date | Country or agency | Law or regulation name | Stage | Main content | Who it applies to |
|---|---|---|---|---|---|

- The stage column records the step of the rule, such as bill introduced, enacted, amended, in force, or repealed. Distinguish bills not yet in force from laws in force by stage
- The main content column carries what the provisions, official explanations, or announcements of the responsible agency state

## Technology classification

When the topic is a technology, set the technology classification in the scope step by breaking the topic technology into sub-technologies. Every module uses the same classification. Each cell of the classification is called a node. Maturity and trends differ by node, so mixing nodes makes them impossible to judge. Christensen (1992) showed that component technologies and architectural technologies each follow their own S-curve.

- (One criterion per level) Divide the nodes on one level by a single criterion. Criteria include material, device function, implementation approach, process, application field, and so on. For example, compound semiconductors and silicon semiconductors are nodes by material, while memory and RF devices are nodes by function, so they sit on different levels
- (Technology and product) Treat technologies such as principles and processes, the equipment and products that implement them, and the application fields that use them as separate classifications. For example, additive manufacturing is the process of joining materials to make parts from 3D model data, usually layer upon layer, and a 3D printer is a machine used for 3D printing (ISO/ASTM 52900)
- (Separate approaches) Give each approach its own node when different approaches deliver the same function. For example, superconducting, trapped ion, neutral atom, and photonic quantum computing each become a node
- (Record by node) Set search terms and facts at node level. Record a fact of one node in that node only. For example, record process trends of nickel alloys in the nickel alloy node and keep them out of titanium alloys or metal materials as a whole
- (Source of the classification) Confirm the classification from sources such as technology classifications set by governments or agencies, academic reviews, and industry standards. Classification schemes are revised often, so record the source and base date of the classification used. Do not merge figures from classifications with different definitions into one node

## Organizing technology trends

The technology category answers where the topic technology sits on its maturity curve and in which direction it is changing. The maturity curve is the S-curve that plots technology performance against time or development effort (Foster 1986, Christensen 1992). Early on, performance improves slowly for the effort spent. In the middle range, improvement speeds up. In the mature stage, the technology approaches a natural or physical limit, and each increment of improvement takes more time and effort.

Check technology trends for each node by the evidence types below.

| Evidence type | Items to check |
|---|---|
| Performance trend | Year-by-year change in key performance indicators, distance from known limits, and so on |
| Readiness | TRL, prototypes, demonstration results, commercial product launches, and so on |
| Technology level | Technology level and technology gap by country, and so on |
| Convergence and substitution | Standardization launched and finalized, emergence of a dominant design, emergence of substitute or converging technologies, and so on |
| Research activity | Main research streams, emerging research topics, leading research institutions, and so on |

- Look first for literature that addresses maturity directly, such as technology level assessment reports, technology roadmaps, and review papers
- Use paper and patent statistics as published by the source. When querying a database directly, follow references/sources.md
- Results of demonstration and commercialization (what was demonstrated or launched, in what environment) go to the technology category. The budget of the program that funded the demonstration goes to the investment category of the micro environment
- R&D spending is input on the horizontal axis of the S-curve, so it does not show the position on the curve. Spending goes to the investment category of the micro environment

The maturity stage is a judgment. Record it only when the source states the stage or the supporting facts clearly fit the stage descriptions below, and attach the IDs of the supporting facts. If the basis is thin, record it as unconfirmed. If the source uses a different stage scheme, follow the source.

| Stage | Observed evidence |
|---|---|
| Emerging | Work centered on proof of principle and lab research, several implementation approaches in parallel, no commercial products |
| Growth | Faster performance improvement, more prototypes and demonstrations, first commercial products |
| Mature | Slower performance improvement, a dominant design or standard settled, competition centered on cost and process improvement |
| Saturated | Performance close to known limits, substitute technologies emerging |

A dominant design is a product design that becomes the de facto standard in the market, a concept introduced by Utterback and Abernathy (1975). TRL measures how close a specific technology is to actual operation, and the maturity stage describes the phase of performance improvement. Record the two separately.

Build the table below for each level: overseas, national, and regional.

| Year | Technology node | R&D organization | R&D content | TRL | Basis for TRL |
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
- Record each fact in the fact register with a MAC- ID

## Check

- Categories follow the user's framework or fit with the topic
- Each fact sits in the one category whose question it answers
- No market, industry, or competitor content has slipped into the macro environment
- The policy category holds no program budgets, call details, or investment amounts
- Changes in laws and regulations are organized in the regulation table
- The expected effects in the policy table repeat what the policy documents state
- Technology trends and maturity stages are written at node level of the technology classification
- No TRL or maturity stage is estimated without basis
- Writing moves from overseas to national to regional
- No interpretation or prescription is mixed in
