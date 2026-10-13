> This English edition is a translation of the Korean original. Some rules were adapted to English writing conventions, and the skill may behave differently from the intent of the original.

# Internal Status Analysis

The internal status module covers the resources, capabilities, and operations the subject controls directly. For an organization subject, it organizes the organization profile and a capability assessment. For a region subject, it organizes regional innovation resources. Module sections contain facts and procedure-defined ratings, and leave out to-be states, needs, and improvement directions.

## Shared principles

- (Balance) Record both resources that lead the comparison group and resources that fall short. A one-sided record distorts judgments in later stages
- (Link to the micro environment) If the micro environment module also ran, set the industry requirements found there and the internal status side by side on the same basis, so that differences show as facts
- (Profile separate from assessment) The organization profile (history, structure, staffing, budget) introduces the subject, so place it right after the scope section and before the environment sections. The capability assessment compares the subject with the external environment, so place it after the environment sections. If the user sets a position, follow it
- (Data channels) Take internal material only from files the user provides or from connected systems the user has authorized. Quality judgment and security handling follow references/sources.md
- Record each fact in the fact register with an INT- ID

## Organization subject

### Organization profile

| Item | Content |
|---|---|
| History | Founding and major changes |
| Mission and goals | Wording as stated in official documents |
| Structure | Organization chart, departments |
| Staffing | Headcount, job group composition |
| Budget and finance | Budget size, revenue, funding composition |
| Main programs or businesses | List and size, and the stages of the industry value chain where the organization does business |
| Main results | Results confirmed by official material |

### Capability assessment frameworks

| Framework | Nature | When to use |
|---|---|---|
| SPROC | Practitioner checklist that adds culture to Arthur D. Little's SPRO (strategy, process, resources, organization) to review operations | To scan the whole organization area by area and check alignment between areas |
| 7S | Seven-element framework from Waterman, Peters, and Phillips (1980, Structure is not organization) | To examine alignment among elements |
| VRIO | Resource evaluation framework from Barney (1991, 1995) | To judge whether key resources are sources of competitive advantage |
| Organizational value chain | Porter's (1985) split into primary and support activities | To break the current state down by activity inside the organization |
| Free composition | Areas set by the user | When the user supplies their own criteria |

If the user names no framework, organize the current state with SPROC, then rate the key resources identified there with VRIO. If the user prefers 7S, use 7S in place of SPROC. SPROC and 7S decide where to look, and VRIO judges whether a resource gives competitive advantage, so the two frameworks answer different questions. If the user asks for one framework only, run only that one.

### SPROC areas

SPRO is a framework the consulting firm Arthur D. Little introduced in the early 1990s. It treats alignment among strategy, process, resources, and organization as a condition for profitability. Arthur D. Little later extended it to VSPRO by adding vision (V) and to VSPRO-L by adding learning (L). SPROC is a practitioner variant that adds culture (C) to SPRO. Apply it using the definitions below. The 7S column serves as a check for missing areas.

| Area | Definition | Items to check | Example evidence | Matching 7S elements |
|---|---|---|---|---|
| Strategy | The organization's goals and the plan to reach them | Mid- to long-term plans, business portfolio, results against targets | Business plans, board materials | Strategy |
| Process | Work procedures and operating systems that carry out the strategy | Core workflows, decision procedures, information systems, performance management | Work rules, system inventory | Systems |
| Resources | Tangible and intangible assets needed to carry out the strategy and processes | Staff size and expertise, budget, facilities and equipment, technology and intellectual property, data | HR statistics, financial statements, asset lists | Staff, Skills |
| Organization | Structure of authority and responsibility that supports the strategy and processes | Organization chart, positions, collaboration structure, external partnerships, governance | Organizational regulations, organization chart | Structure |
| Culture | Values and behaviors shared by members | Shared values, leadership style, member perceptions | Culture surveys, survey results | Shared values, Style |

### Organizational value chain

With the organizational value chain framework, organize current-state facts by activity following Porter's (1985) split. Do not recast stages of the industry value chain as activities of the organization.

| Group | Activities |
|---|---|
| Primary activities | Inbound logistics, operations, outbound logistics, marketing and sales, service |
| Support activities | Firm infrastructure, human resource management, technology development, procurement |

For organizations without a manufacturing and sales flow, such as public agencies or research institutes, rename the activities to match the organization's actual workflow and record how each new name maps to the original group.

### 7S elements

| Element | Definition | Type |
|---|---|---|
| Strategy | Plans and resource allocation to gain competitive advantage | Hard |
| Structure | Organizational structure, reporting lines, decision flow | Hard |
| Systems | Work procedures, information systems, management systems | Hard |
| Shared values | Core values and mission shared across the organization | Soft |
| Style | Leadership style and organizational climate | Soft |
| Staff | Composition and attitudes of members | Soft |
| Skills | Capabilities and skills the organization holds | Soft |

### VRIO rating

| Question | Content |
|---|---|
| V Value | Does the resource help exploit an external opportunity or reduce a threat? |
| R Rarity | Do only a few competitors hold the resource? |
| I Imitability | Do competitors without the resource face a significant cost disadvantage in obtaining or developing it? |
| O Organization | Are the organization's systems, procedures, and policies set up to capture the value of the resource? |

| V | R | I | O | Result |
|---|---|---|---|---|
| No | - | - | - | Competitive disadvantage |
| Yes | No | - | - | Competitive parity |
| Yes | Yes | No | - | Temporary competitive advantage |
| Yes | Yes | Yes | No | Unexploited competitive advantage |
| Yes | Yes | Yes | Yes | Sustained competitive advantage |

- Rate the key resources and capabilities identified during the area review
- Cite supporting fact IDs for each answer
- Rarity and imitability need a comparison group. Even if the micro environment module did not run, collect the competitor data needed for these answers as rating evidence. If comparison data cannot be found, mark the answer as unconfirmed and the result as undetermined
- Do not use missing data as evidence for "No". Unconfirmed items stay unconfirmed

| Resource or capability | V | R | I | O | Result | Evidence IDs |
|---|---|---|---|---|---|---|

### Demand survey material

When surveys, interviews, or requirement documents such as requests for proposals are provided, list the requesting party, the requirement, the source question or clause, and the number of responses. Record only the requirements stated in the material and add no inferred requirements.

## Region subject

Regional innovation resources fall into four groups following research on regional innovation systems (Autio 1998; Tödtling and Trippl 2005). Firms and the industrial base apply knowledge, universities and research organizations generate knowledge, support organizations and infrastructure connect the two, and policies and program funding drive the system.

| Group | Items |
|---|---|
| Knowledge application | Ecosystem linkages, large firms and SMEs located in the region, anchor innovation organizations, industrial clusters, industry statistics |
| Knowledge generation | Universities and departments, research institutes, regional branches of government-funded research institutes, key research teams |
| Innovation support | Business support organizations, research and demonstration facilities and equipment, data processing facilities |
| Policy and funding | Central government R&D programs won by the region, the region's own R&D programs, non-R&D business support programs, regional industrial policy |

### Knowledge application items

Describe ecosystem linkages, meaning how firms, organizations, and demand-side customers in the region connect through supply chains and cooperation, using confirmed relationships only.

Build separate tables for large firms and for SMEs located in the region.

| Company | Company overview | Business areas | Main customers | Competing industries | Recent developments |
|---|---|---|---|---|---|

| Anchor innovation organization | Type | Main functions | Related fields |
|---|---|---|---|

| Cluster or industrial complex | Location | Main industries | Number of tenant firms | Operator |
|---|---|---|---|---|

Organize industry statistics for the number of establishments, employment, output or revenue, value added, and corporate R&D spending in a table covering at least the last 3 years. Compute the share of the national total and the location quotient in code for the most recent year and report them alongside.

| Indicator | Year 1 | Year 2 | Year 3 | Share of national total | Location quotient | Source |
|---|---|---|---|---|---|---|

### Knowledge generation items

| Organization | Type (university, research institute, branch of a government-funded research institute) | Related department or research unit | Main research fields | Source |
|---|---|---|---|---|

Organize key research teams by firm, university, and research institute, at the level of organizations and labs. Name individuals only when they are principal investigators confirmed through public professional activity such as papers, projects, or official institutional pages. Do not collect contact details or personal information.

| Affiliation type | Organization | Lab or principal investigator | Main research fields | Public evidence |
|---|---|---|---|---|

### Innovation support items

| Business support organization | Support functions | Target users |
|---|---|---|

Organize research and demonstration facilities and equipment and data processing facilities (computing infrastructure, data centers, and similar) in separate tables with the same format.

| Owner | Name | Specifications | Quantity | Purpose |
|---|---|---|---|---|

How the facilities and equipment could serve the topic is a judgment, so it belongs in the implications section.

### Policy and funding items

For national R&D projects carried out by organizations in the region, apply the national R&D database rules in references/micro.md with the scope narrowed to the region.

List central government R&D programs only when organizations in the region have already received central government funding and are carrying them out. Exclude programs the region is preparing to bid for or plans to apply to. List pure R&D programs only, and organize non-R&D programs separately.

| Ministry | Performing organization in the region | Program name | Program period | Program content | Budget by year |
|---|---|---|---|---|---|

Organize the region's own R&D programs and non-R&D business support programs separately in the format below. The region's own R&D programs include pure R&D programs only.

| Lead organization | Program name | Program period | Program content | Budget by year |
|---|---|---|---|---|

Organize the industrial policies and regulations of a region subject here, in the policy table format of references/macro.md.

## Check

- Leading and lagging resources are both recorded
- The organization profile and the capability assessment are separate
- Each VRIO answer cites fact IDs, and items without comparison data are unconfirmed
- SPROC areas were applied as defined in the table
- Activities of the organizational value chain and stages of the industry value chain are not mixed
- Each regional resource sits in exactly one of the four groups
- Central government R&D programs include only ongoing programs
- R&D and non-R&D programs are separated
- Research team information stays within public professional information
- No to-be states, needs, or utilization plans are mixed into the text
