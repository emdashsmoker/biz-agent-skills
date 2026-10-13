> This English edition is a translation of the Korean original. Some rules were adapted to English writing conventions, and the skill may behave differently from the intent of the original.

# Data Channels and Source Verification

These rules for data collection, source quality, verification levels, and computation apply to every module. The citation format is in references/writing.md.

## Sources of knowledge

- Take facts only from user-provided material, web pages opened during this task, and data retrieved from connected systems
- Do not fill anything missing from these three channels with model knowledge. Mark it as unconfirmed
- Do all computation in code, and recheck figures quoted in sources in code
- Cite web material with the full address of the page that carries the information. A top-level domain alone does not let a third party find it

## Data channels

| Channel | Examples | Criteria applied |
|---|---|---|
| Web search and page retrieval | Government releases, official statistics, research reports, academic papers | Public source quality |
| User-provided files | Reports, statistics exports, exports from paid databases, internal documents | Public or internal source quality, depending on the document |
| Connected systems | MCP connectors (document tools, mail, messaging, calendar), public data APIs, internal databases and data warehouses, knowledge graphs | Internal source quality and internal data security. Public APIs use public source quality |

### Material that search engines rarely surface

| Material | Usual channel |
|---|---|
| National R&D program and project information | Public APIs of national R&D information systems, user exports |
| Detailed official statistics tables | Statistics agency APIs, exports from statistics portals |
| Corporate disclosures and financials | Disclosure system APIs |
| Patents | Patent office databases, public patent search services, user exports |
| Papers | Academic database APIs, user exports |
| Corporate R&D spending | R&D activity survey statistics, industry surveys, corporate disclosures |
| Venture investment | Association and government statistics, user exports from paid investment databases |
| Internal capability material | Internal document systems, internal databases, user-provided files |

### Channel rules

- At the start, check which connectors, APIs, and databases are available. If a needed channel is missing, send the user one list of the material required
- Follow each source's terms of use: API key issuance, rate limits, redistribution limits, and attribution conditions (such as open government license types). Terms and pricing change often, so check the official notice at the time of use
- Keep API keys, tokens, and passwords out of outputs, logs, and citations
- Do not collect in bulk by methods the source prohibits
- Do not fill material you did not receive with estimates from other channels. Leave it as unconfirmed
- For counts and amounts drawn from a database (projects, patents, papers, deals, and so on), record the database name, search conditions, and query date in the citation. A third party should be able to run the same query again

### Exploring complex databases

Complex databases, such as national R&D information systems, investment databases, patent databases, detailed tables on statistics portals, and internal databases, each differ in fields, classification schemes, and search methods, and their structure is sometimes reorganized. This skill's guidance alone cannot set the query method for each database, so explore it step by step with the user. The user knows the topic and is best placed to judge whether unrelated records slipped in or needed records are missing.

- (Proposing conditions) Learn the fields and classification scheme from the database's official guide, API documentation, or an export the user provided, then propose search terms, period, classifications, and exclusion criteria to the user
- (Checking a sample) Run a small query with the proposed conditions first, and show the count and a few representative results. If the results do not fit the topic, revise the conditions with the user and query again
- (Extracting) Extract the full set once the user agrees to the conditions. Record the final conditions and query date in the citation
- (Queries by the user) For databases that require a login or paid access, give the user the query conditions and receive the export file. If the meaning or unit of a field in the file is unclear, check with the user

## Search practice

- Search both Korean-language and English-language web
- Short core keywords often return better results than long multi-word queries
- Find and cite the original publisher's page over pages that re-quote it
- Keep internal confidential information and personal information out of web search queries

## Public source quality

Judge the quality of public sources by the structural criteria below. The political leaning and brand recognition of an outlet are not criteria.

| Criterion | High-quality signal | Low-quality signal |
|---|---|---|
| Editorial and fact-checking process | Published with an editorial team and a verification process | Self-published without editors or verification |
| Independence of the publisher | Published by a third party with no stake in the subject of analysis | Published by an interested party for promotion or advertising |
| Material type | Primary material produced by the publisher | Secondary processing or re-quoting with unclear origin |
| Verifiability | Original text, methodology, sample, and calculation basis can be traced | Basis cannot be traced, assertions only |
| Expertise and peer review | Peer-reviewed or officially published by an expert body | Anonymous author, expertise unconfirmed |
| Automated generation | Human authors and editorial responsibility confirmed | Content likely generated by a language model and unverifiable |

The more criteria a source meets, the higher its quality. A source that cannot be verified or is likely machine-generated counts as low quality even if it meets other criteria.

### Handling by tier

- (High quality) Meets most criteria. Cite first
- (Marginal) Usable under conditions depending on the use. Cite after tracing the original source or cross-checking
- (Low quality) Unverifiable or clearly disqualified. Do not cite it, treat it as absent, and do not write claims that rest only on it

### High-quality types

The types below are examples. A source missing from the list is not low quality by default. Judge unlisted sources against the criteria.

| Type | Examples |
|---|---|
| Government and public bodies | Official publications and press releases of ministries, local governments, and their agencies, national approved statistics, legal information |
| Legislature and audit bodies | In Korea: National Assembly Budget Office, National Assembly Research Service, National Assembly Futures Institute, Board of Audit and Inspection reports |
| Government research institutes and expert agencies | In Korea: Korea Development Institute, Korea Institute for International Economic Policy, Korea Institute for Industrial Economics and Trade, Science and Technology Policy Institute, Korea Information Society Development Institute, Korea Institute of S&T Evaluation and Planning, Software Policy and Research Institute, National Information Society Agency, Institute of Information and Communications Technology Planning and Evaluation, Electronics and Telecommunications Research Institute, Korea Institute of Science and Technology Information, Korea Evaluation Institute of Industrial Technology, and others |
| Academic | Peer-reviewed journal articles and theses. Treat preprints as unverified, use them sparingly, and check the original text in academic search services |
| Patents and standards | Patent office gazettes, WIPO material, documents of national and international standards bodies |
| International organizations | Reports and statistics of the OECD, IMF, World Bank, UN and its agencies, IEA, WTO, BIS, Eurostat |
| International indicators | Stanford HAI AI Index, IMD World Competitiveness reports |
| Financial institutions | Official statistics and publications of central banks, exchanges, and other reputable financial institutions |
| Consulting and research | Reports from McKinsey, BCG, Bain, Deloitte, PwC, KPMG, EY, and industry research from Gartner, IDC, Forrester, and similar firms |
| Technical documentation | Official documentation and repositories of major open-source projects and standard libraries (technical topics only) |

Statistics aggregators and resellers of market reports are secondary sources, so find and cite the original source.

### Low-quality types

Shared signals are the absence of editorial and fact-checking processes, unknown publishers, unverifiability, and automated generation. Do not cite the types below.

- (Machine-generated content) Mass-publishing sites and AI-generated encyclopedias with no authors or editors, auto-generated URL patterns, summaries without original sources, or notices asking readers to verify the content themselves
- (User-generated content) Open wiki articles, Q&A services, user reviews. Do not cite wiki articles. Trace the original sources they name and cite those
- (Personal posts) Personal blogs, personal social media posts
- (Anonymous spaces) Anonymous boards, forums, comments
- (Sensationalist outlets) Outlets that put sensation ahead of fact-checking
- (Unattributed collections) News roundups, card news, scraping services, and affiliate-link reviews that do not name their sources
- (Promotional content) Sponsored content, advertorials, articles that reprint press releases unchanged
- (State propaganda) State-controlled propaganda outlets without editorial independence
- (Unknown publishers) Domains whose publisher and editorial responsibility cannot be confirmed

### Handling marginal sources

- (General news reports) Find the original source the report cites and cite it. If the original cannot be found, do not rest a claim on the report alone
- (Company announcements) The company has a stake, so cite them only as the company's own statements
- (Preprints) Keep in mind that they are unverified, and cite them sparingly
- (Single-source claims) Cross-check a claim raised by only one source against an independent source before citing it
- (Opinion pieces) Keep editorials and columns apart from news reporting, and cite them as the author's view
- (Associations and advocacy groups) Cite material from groups that represent a position with their interests in mind

### Political neutrality

Do not rate outlets by political leaning or camp. Judge only structural properties such as editorial process, verifiability, and sensationalism, so that two outlets from different camps receive the same rating under the same criteria.

### When every source is low quality

If every source collected is low quality, treat them as absent and do not write the claim. Leave the point as a gap in information, without asserting that it is false or absent in reality. If high-quality sources are needed, narrow the search to high-quality types and search again.

### Non-disclosure and exceptions

- Keep source tiers, exclusions, and the judging process out of the output. The output shows only sources that passed, in the usual citation format. If the user asks for the ratings, disclose them
- If the user instructs you to cite a specific source, do not exclude it
- If the subject of analysis is itself low-quality material (for example, a study of how misinformation spreads), citation for analysis is allowed
- Quoting a party's own statements is allowed within the scope of self-statements

## Internal source quality

Internal material is the record a subject keeps about itself. Organizations manage material in different ways. Some run systems of record, internal databases, and data warehouses, and others keep material in document tools, shared drives, and chat. Judge internal material by the checks below regardless of how it is managed or where it is stored. The basis of the checks is whether you can confirm what a record measured and as of when.

| Check | Content |
|---|---|
| Reference date | The date a figure refers to. If the document does not state it, use the creation date or message date and say so in the citation |
| Latest version | If several documents cover the same content, use the most recently modified one |
| Indicator definition | What a figure counted, over what scope, and in what unit. If the organization maintains metric definitions or a data catalog, use those definitions. Do not join figures with different definitions into one trend |
| Duplicates and gaps | Whether combining figures from several documents counts a record twice or leaves a period out |

- Collect figures whose checks cannot be confirmed on the confirmation list. List the document name, location, and what needs confirming, and send the list to the user at once
- If the same figure differs across documents, follow the reference document the user designated or the system of record (accounting, HR, and similar). If neither exists, use the figure from the most recent document. Note on the confirmation list that other figures exist
- Mark figures awaiting the user's answer as "to be confirmed" in the fact register, and do not use them as evidence for implications

## Internal data security

- Query only the systems and scope the user has authorized
- Query only the minimum needed for the analysis
- Keep information that identifies individuals (HR data tied to names, contact details, evaluation results, and similar) out of the output, and aggregate to department or organization level
- Mark connected systems in the data channel field of the fact register, so the user can separate internal material before sharing externally
- Do not use internal material in web search queries or send it to external services
- Follow the organization's security classifications or data policies where they exist

## Verification levels

| Level | Procedure |
|---|---|
| Level 1 Basic | Rules on sources of knowledge, computation and rechecks in code, full page addresses |
| Level 2 Quantitative confirmation | Level 1, plus user confirmation of quantitative data before it enters the text |
| Level 3 Full confirmation | Level 1, plus evidence collection for every source and user confirmation of all qualitative content and quantitative data |

### Selection rule

If the user specifies a level, use it. If not, choose by whether the output can still be corrected and whether it contains quantitative data.

- (Correctable) Output seen only by the author or the internal team that can still be discarded: personal research notes, drafts, material for internal review, regular status briefings
- (Hard to correct) Output delivered or about to be delivered outside, with limited chances to correct it: reports sent to clients, bid proposals, audit evidence, published papers, official notices, court filings, final reports

| Correctability | No quantitative data | Contains quantitative data |
|---|---|---|
| Correctable | Level 1 | Level 2 |
| Hard to correct | Level 3 | Level 3 |

Output that goes outside carries risks beyond numerical errors, such as false factual statements and citations of sources that do not exist, so it uses level 3 whether or not it contains quantitative data. Without quantitative data, the quantitative confirmation part of level 3 drops out on its own.

- Announce the chosen level in one line, in the format `Source verification: level N (one-line reason)`
- If the user says "stricter", raise it one level. If the user says "this is enough", lower it one level. If the user names a level, apply it at once
- Do not explain the selection at length. Do not apply a level without announcing it. Do not choose a level without the table. Do not add adjustment rules beyond user requests

### Level 2 quantitative confirmation

Quantitative data means all information expressed in numbers: figures, statistics, ratios, percentages, amounts, growth rates, rankings, counts, and sizes. The rule applies whether the data came from the web, provided files, or connected systems.

1. Record each quantitative data point and its source (publisher, year, title, address)
2. Before it enters the text, show the list in the format below
3. Put only approved data in the text. Replace corrected data with the value the user gave. Exclude rejected data

```
Quantitative data confirmation request

| No. | Data item | Value | Source |
|---|---|---|---|
| 1 | (item) | (value) | Publisher (year), title |

- Approve: approve all, or approve by number
- Correct: give the number and the correct value
- Reject: do not use the data
```

- (Exception) Figures the user typed in the conversation need no confirmation. If the user says "skip confirmation" or "go ahead", skip it for that turn only and restore the procedure from the next turn
- (Prohibited) Do not put quantitative data in the text without confirmation. Do not slip it in with words such as "about", "roughly", or "estimated". Do not present figures awaiting confirmation as settled facts

### Level 3 full confirmation

Every source to be cited and every piece of content to be cited (definitions, claims, factual statements, figures, dates) is in scope. Quantitative data is also rechecked in code.

| Channel | Evidence to collect |
|---|---|
| Web | Existence (search result snippet for publisher and title), date (publication date shown in the results or on the page), address access (success or failure, page title), content (excerpt of the original text containing the cited content) |
| Provided files | Date (publication, writing, or reference date shown in the document), content (excerpt of the original text), consistency (whether the title, author organization, and reference year match the content to be cited) |
| Connected systems | Identification (system name, document or table identifier), query (query conditions or path, time of retrieval), reference date, content (excerpt of the original text) |

Copy excerpts as they are, without editing or summarizing, and limit them to the minimum needed to confirm the cited content (centered on the relevant sentence). Quotation of copyrighted works must stay within a fair scope. If evidence cannot be found, record that fact as it is.

Before writing the text, show all evidence and planned citations at once. Keep the source table and the quantitative data table separate.

```
Citation confirmation request

[Sources and planned citations]
| No. | Channel | Source | Publication year | Content to cite |
|---|---|---|---|---|

[Evidence for source 1]
- (Existence) search result snippet, or "no search results"
- (Date) confirmed date, or "date unconfirmed"
- (Address access) page title, or "access failed"
- (Content) original excerpt, or "content not found"

[Quantitative data]
| Code | Source no. | Source | Publication year | Data item | Value |
|---|---|---|---|---|---|

- Approve: approve all, or approve by number and code
- Correct: give the number or code and the correct content
- Replace: search for another source in place of this one
- Reject: do not use the item
```

- Put only approved items in the text. Replace corrected items with what the user gave. On a replace request, repeat the same evidence collection for the new source
- (Exception) Information the user typed in the conversation needs no confirmation. A "skip confirmation" request applies to that turn only, as in level 2
- (Prohibited) Do not cite a source without evidence. Do not put cited content in the text without approval. Do not leave any cited content out of the confirmation table. Do not slip content in with hedging words. Do not present content awaiting confirmation as fact. Do not invent or guess addresses. Do not guess publication years, and use only years confirmed in the evidence

## Computation rules

Do all computation in code, and round only after the computation is complete.

| Indicator | Formula |
|---|---|
| Compound annual growth rate | (end value / start value)^(1 / number of years) - 1. The number of years is the difference between the end year and the start year |
| Share | part / total |
| Location quotient | (regional value of the industry / regional value of all industries) / (national value of the industry / national value of all industries). Above 1 means more concentrated than the nation |
| Concentration ratio (CR) of the top n firms | Sum of the market shares of the top n firms |
| Herfindahl-Hirschman Index (HHI) | Sum of the squared market shares (%) of all firms. Maximum 10,000 |

- The location quotient follows the employment-based definition of the US Bureau of Labor Statistics. The same formula works for the number of establishments or output. State which value was used
- Concentration thresholds for HHI differ by authority, so state the threshold used and its source
- For currency conversion, record the reference date and source of the exchange rate. For inflation adjustment, record the base year
- If units are mixed, convert to one unit and record the conversion
