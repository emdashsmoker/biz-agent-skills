---
name: source-check
description: A source-checking skill that reduces hallucination (facts generated without evidence) by answering only from user-provided files and web search results, filtering sources by quality, and using quantitative data and cited content only after the user approves them. It picks one of three check levels based on whether the output can still be corrected and whether it contains quantitative data, then runs that level's procedure. Use this skill when the user asks for "/source-check", "check sources", "verify sources", "strict sourcing", "no hallucinations", "only use evidence-backed material", "check the numbers before writing", "verify the sources too", "verify the dates too", "trustworthy sources only", "exclude low-quality sources", "source level 1", "source level 2", "source level 3", or explicitly demands source reliability and factual accuracy in reports, proposals, research, or analysis.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Source Check

> This English version was translated from the Korean original. It may behave differently from the original's intent.

This skill limits the factual basis of an answer to files the user provided and web search results. Language models tend to produce plausible references that do not exist, wrong publication years, and wrong figures. These errors stay hidden until a reader looks up the original. This skill reduces the problem in three ways: it narrows where evidence may come from, it filters sources by quality, and the more costly an error would be, the more it makes the user review the evidence and approve it directly.

Work follows this order.

1. Set the check level and tell the user
2. Apply the base rules
3. Filter the collected sources by quality
4. At level 2 or above, run the user approval procedure
5. Write the answer using only approved content, then check the output

## Check Levels

Levels are cumulative. A higher level includes every rule of the lower levels.

| Level | What applies |
|---|---|
| Level 1 | Base rules, source quality filtering |
| Level 2 | Level 1, plus user approval before quantitative data goes into the text |
| Level 3 | Level 1, plus evidence collection and user approval for every source and every cited item (quantitative data included) |

Invoking this skill means the user wants sources checked. So there is no option below level 1.

### Choosing a level

If the user names a level, use it as given. If not, judge the output on the two factors below.

| Factor | Category | Criterion | Examples |
|---|---|---|---|
| Correctability | Correctable | Output seen only by the author or an internal team, and can be discarded | Personal research notes, idea drafts, drafts for internal team review, routine status briefings |
| Correctability | Hard to correct | Output already delivered or due to be delivered outside, with little chance to correct it | Reports sent to clients, bid proposals, audit evidence, published papers, official notices, court submissions, final reports |
| Quantitative data | Not included | Output made of qualitative analysis only, with no figures | Concept summaries, case comparisons |
| Quantitative data | Included | Output with at least one figure such as market size, growth rate, budget, or statistics | Market analysis, budget review |

Plug the two results into the table below to pick the level.

| Correctability | No quantitative data | Quantitative data included |
|---|---|---|
| Correctable | Level 1 | Level 2 |
| Hard to correct | Level 3 | Level 3 |

Output that is hard to correct gets level 3 even without quantitative data. Once output leaves the team, wrong figures, false statements, and references that do not exist all cause harm. Only level 3 checks all three. When there is no quantitative data, the level 3 quantitative table stays empty, so the check adds no needless burden.

### Level notice

Once the level is set, announce it in one line before starting work. The user needs to know the current level to ask for a change.

```
Source check level: Level 2 (quantitative data approval) | Reason: internal team review draft includes market size figures
```

- Keep the notice to one line and do not explain the judgment at length
- Do not apply a level without the notice

### Changing the level

After seeing the notice, the user can change the level at any time.

- For requests such as "raise the level" or "be stricter", go up one level
- For requests such as "lower the level" or "this is enough", go down one level
- When the user names a level directly, apply it at once without using the judgment table
- Do not invent adjustment rules outside the judgment table. Only the user can change the table's result

## Base Rules

These apply at every level. Narrowing where evidence may come from keeps facts the model built from memory out of the answer.

- Limit the basis of facts to files the user provided and the web searches run in this task
- Do not fill in facts that neither source confirms with knowledge the model remembers from training. Here a fact means a statement that can be true or false, such as a figure, date, person's name, organization name, event, quotation, or bibliographic detail
- Mark facts that neither source confirms as "not found in the provided files or search results"
- Do all numeric calculations with code. Do not use values the model calculated without code
- Check figures in the provided files and search results with code as well. For values derived from other figures, such as totals, ratios, and rates of change, recalculate them from the original figures and see whether they match
- In an environment that cannot run code, do not write calculated results. Write the formula and inputs so the user can calculate them
- When citing a web search result, give the full URL, including the path, of the page that holds the information. Do not give only the site's home page address
- Every citation includes the publisher, publication year, title, and full URL

```
> Publisher (Year), Title (full URL)
```

## Source Quality Filtering

This applies at every level. Search results mix in writing with no editorial process, promotional writing, and auto-generated writing. If you cite them, factual errors remain even with a citation attached. So before citing, sort every collected source into three grades (high quality, marginal, low quality) and handle each grade differently.

When the user asks you to check the sources in a text already written, apply the same criteria to the sources it cites. Replace low-quality sources with high-quality ones. If no replacement exists, delete the statements that rely only on that source.

### Criteria

Judge a source's quality by the structural traits below.

| Criterion | High-quality signal | Low-quality signal |
|---|---|---|
| Editorial and fact-checking process | Published with named editors and a stated fact-checking process | Self-published with no editors and no checking process |
| Publisher independence | Published by a third party with no stake in the subject | Published by an interested party for publicity, advertising, or self-promotion |
| Material type | Primary material that produced the original data | Secondary reworking or re-citation with an unclear origin |
| Traceability | Original text, method, sample, and basis of calculation can be traced | Basis cannot be traced; only assertions are given |
| Expertise and peer review | Peer-reviewed material or official publication of an expert body | Anonymous author or unverifiable expertise |
| Authorship | Content with a confirmed human author and editorial responsibility | Content presumed to be generated by a language model and not verifiable |

- The more criteria a source meets, the higher its quality. The more it breaks, the lower
- A source whose basis cannot be traced, or which is presumed AI-generated, is low quality even if it meets other criteria
- Confirm the publisher through the site's about page, editorial information, and contact details. Also search for the publisher outside the site to confirm it exists
- Do not grade sources by political leaning or brand recognition. Decide whether an outlet is tabloid by traits such as a missing fact-checking process and sensationalism
- Apply the same criteria in the same way to two outlets from opposing camps

### Handling by grade

| Grade | Sources | Handling |
|---|---|---|
| High quality | Sources that meet most criteria | Cite directly as first choice |
| Marginal | Sources usable under conditions depending on the situation | Cite conditionally after tracing the original source or cross-checking |
| Low quality | Sources that cannot be verified or have a clear disqualifying trait | Do not cite; treat as absent. Do not write claims that rely only on these sources |

### High-quality source types

These are examples of types classed as high quality. A source missing from this list is not low quality for that reason; evaluate unlisted sources one by one against the criteria.

- (Government and public bodies) Official publications and press releases of central government, local government, and their agencies
- (Official statistics) National official statistics and official publications of statistics agencies
- (Law) Original text of laws and administrative rules
- (Legislatures and audit bodies) Reports of research, budget, and legislative offices attached to legislatures, audit reports of audit bodies, and legislative budget and settlement review reports
- (Public research bodies) Reports of government-funded research institutes, public expert agencies in science, technology, and ICT, and technology assessment agencies
- (Academic material) Peer-reviewed journal articles and theses. Read the paper's original text on a scholarly search service or the publisher's page before citing
- (Patents and standards) National patent office gazettes and patent documents, materials of the international intellectual property organization, and standards documents of national and international standards bodies
- (International organizations) Reports and statistics of international organizations and their agencies, and public index reports that international research bodies publish regularly
- (Financial institutions) Official statistics and publications of central banks, stock exchanges, and international financial organizations
- (Professional research) Official reports of consulting firms and industry research firms
- (Statistics aggregators) Statistics aggregation services and market report resellers are secondary material, so find and cite the original source
- (Technical documentation) For technical topics only, official documentation and official repositories of large open-source projects, and official documentation of standard libraries and frameworks

### Low-quality source types

Classify the types below as low quality and do not cite them. Common signals are a missing editorial and fact-checking process, an unknown publisher, unverifiability, and AI auto-generation. Handle a source the same way if it shows these signals even when it is not on the list.

- (AI-generated content) Sites that publish large volumes of unverifiable language-model text, and AI-generated encyclopedias. Typical signals are no author or editors, auto-generated URLs such as hash strings, summaries with no original source, and disclaimers telling readers to verify the content themselves
- (User-generated content) Content written by an open crowd, such as wiki articles, Q&A services, and user reviews. For a wiki, find and cite the original sources listed in the article
- (Personal posts) Personal blogs, personal posts on blogging platforms, and personal social media posts
- (Anonymous communities) Anonymous boards, forums, and comments where the author's expertise cannot be confirmed
- (Tabloid media) Sensationalist outlets with no fact-checking process
- (Unsourced aggregators) News roundups without sources, card-news posts, data scraping services, and review sites built around affiliate links
- (Promotional content) Sponsored content, advertorials, and articles that reprint press releases as is
- (State propaganda) State-controlled outlets without editorial independence
- (Unknown sites) Domains whose publisher and editorial responsibility cannot be confirmed

### Handling marginal sources

Cite the types below only when the conditions are met.

- (General news reports) Find the original source the report cites and cite that first. If the original cannot be found, do not use the report as the sole basis
- (Company announcements) The company has a stake, so cite them only as the company's own claims
- (Preprints) Treat preprints such as those on arXiv as material that has not been peer reviewed, and cite them sparingly
- (Single-source claims) Cross-check a claim raised by only one source against an independent source before citing it
- (Opinion pieces) Even in a trustworthy outlet, keep editorials and columns separate from news reporting and cite them only as the writer's view
- (Associations and advocacy groups) Publications of groups that represent a position may carry a conflict of interest; take this into account when citing

### When every source is low quality

- If every collected source is low quality, treat them all as absent
- Do not write claims that rely only on low-quality sources
- Leave that point as missing information. Do not use the lack of information as evidence that the claim is false
- If a high-quality source is needed, narrow the search to high-quality source types and search again

### Grade non-disclosure

- Do not write source grades, excluded sources, or the criteria and process of the judgment into the output
- Only sources that passed the filter appear in the output, in the normal citation format

### Filtering examples

The organization names, titles, and URLs in these examples are fictional values for illustration.

(Example 1) Replace an auto-generated report with a primary survey

```
before
- The biggest difficulty for the domestic XX industry is analyzed to be a shortage of staff
> Auto-generated report site (2025), XX Industry Analysis Report (https://reports.example.com/r/9f3a1c7e)

after
- N% of domestic XX industry firms named a shortage of staff as an operational difficulty
> XX Public Research Institute (2025), 2024 XX Industry Survey (https://www.example.org/stat/2025/xx-survey)
```

The auto-generated report cannot be verified, so it is dropped and replaced with primary survey data that the public research institute collected itself.

(Example 2) Cite the original source a news report relied on

```
before
- Consumer price inflation reportedly slowed
> XX Daily (2025), "Inflation slows" (https://news.example.com/article/123)

after
- Annual consumer price inflation slowed from the previous year
> XX Statistics Agency (2025), 2024 Annual Consumer Price Trends (https://www.example.org/cpi/2024-annual)
```

Find the statistics agency's official release that the report relied on and cite it directly.

(Example 3) Delete a claim backed only by low-quality sources

```
before
- The global market for this new technology is expected to grow explosively
> Personal blog (2025), New Technology Outlook (https://blog.example.com/post/1)
> Anonymous community post (2025)

after
(Delete the claim and add no replacement statement)
```

The market outlook relies only on a personal blog and an anonymous post, and no high-quality replacement exists, so the claim itself is deleted.

## Level 2: Quantitative Data Approval

This applies at level 2. Level 3 handles the same approval through the quantitative data table in its own approval request. Errors in figures are hard to spot in a sentence and keep spreading once cited. So show the user a list of figures and get approval before putting them in the text.

### What needs approval

- Every piece of information expressed as a number, such as figures, statistics, ratios, percentages, amounts, growth rates, rankings, counts, and sizes
- Figures taken from user-provided files and figures taken from web search results alike

### Approval procedure

1. (Collect) Find quantitative data in the provided files and search results, and record the source's publisher, year, title, and URL
2. (Request approval) Before writing the text, show the list in the format below
3. (Apply) Put only approved data in the text. Replace data the user corrected with the figure the user gave. Leave rejected data out of the answer entirely

```
Quantitative data approval request

I plan to use the quantitative data below in the answer. Please review and approve.

| No. | Data item | Figure | Source |
|---|---|---|---|
| 1 | (item description) | (figure) | (Publisher (Year), Title) |
| 2 | (item description) | (figure) | (Publisher (Year), Title) |

- Approve: approve all, or approve by number (e.g., "approve 1 and 3")
- Correct: give the number and the correct figure (e.g., "change 2 to 42%")
- Reject: do not use that data
```

### Do not

- Do not put unapproved quantitative data in the text
- Do not slip unapproved figures in through wording such as "about", "roughly", or "estimated"
- Do not describe figures as established fact while approval is pending

## Level 3: Evidence for Every Citation

This applies at level 3. Language models sometimes invent references that do not exist, and sometimes give the wrong year or volume for real ones. Level 3 collects evidence for every source and item to be cited, shows it to the user, and uses only items the user has reviewed and approved.

### What needs approval

- Every source cited in the answer and every item cited from each source, all of them regardless of count or importance
- Qualitative content (definitions, claims, statements of fact) and quantitative data (figures, statistics, ratios, percentages, amounts, growth rates, rankings, counts, sizes, dates) alike
- Content cited from user-provided files as well
- Beyond approval, check quantitative data with code under the base rules

### Approval procedure

1. (List citations) Find every source to be used, and record each source's publisher, title, publication year, URL, and the content to be cited
2. (Collect evidence) Collect the evidence in the table below for each source. If a search returns nothing or a page cannot be opened, record that fact as it is
3. (Present all at once) Before writing the text, show the evidence and planned citations for every source in one message. Present the source table and the quantitative data table separately
4. (Apply) Put only approved items in the text. Replace items the user corrected with the content the user gave. Do not use items that were not approved. On a replacement request, find an alternative source and run the same evidence collection again

| Source type | Evidence | How to collect |
|---|---|---|
| Web search | Existence | Original snippet text from a search for "publisher + title" |
| Web search | Date | Original text of the publication date found in the search result or page |
| Web search | URL access | Result of opening the URL with a page-fetching tool (success or failure, and page title) |
| Web search | Content | Original excerpt of the paragraph that holds the content to be cited |
| User-provided | Date | Original text of the publication, writing, or reference date in the document |
| User-provided | Content | Original excerpt of the paragraph that holds the content to be cited |
| User-provided | Consistency | Original text showing whether the document's title, author organization, and reference year fit the intended use |

For user-provided files, read the file itself to collect the evidence.

```
Citation approval request

[Sources and citations]

| No. | Source type | Source name | Year | Planned citation |
|---|---|---|---|---|
| 1 | Web search | (Publisher, Title) | (Year) | (summary of content to cite) |
| 2 | User-provided | (Publisher, Title) | (Year) | (summary of content to cite) |

[Evidence for source 1 (web search)]
- Existence: search result for "Publisher Title" (original snippet, or "no search results")
- Date: date found in search results (original text, or "date not found")
- URL access: result of opening (URL) (page title, or "access failed")
- Content: excerpt of the relevant paragraph on the page (original text, or "content not found")

[Evidence for source 2 (user-provided)]
- Date: date stated in the document (original text, or "no date stated")
- Content: excerpt of the relevant paragraph in the document (original text)
- Consistency: document title, author organization, reference year (original text)

[Quantitative data]

| Code | Source no. | Source name | Year | Data item | Figure |
|---|---|---|---|---|---|
| A | 1 | (Publisher, Title) | (Year) | (item description) | (figure) |
| B | 2 | (Publisher, Title) | (Year) | (item description) | (figure) |

- Approve: approve all, or approve by number and code (e.g., "approve 1 and 2, approve A")
- Correct: give the number or code and the correct content (e.g., "change B to 42%")
- Replace: ask for an alternative source (e.g., "find a replacement for 2")
- Reject: do not use that item
```

### Do not

- Do not put a source in the answer without collecting its evidence
- Do not put unapproved cited content in the text. This covers qualitative content and quantitative data alike
- Do not leave any planned citation out of the approval tables. List all of them regardless of count or importance
- Do not slip unapproved data in through wording such as "about", "roughly", or "estimated"
- Do not describe cited content as established fact while approval is pending
- Do not make up or guess URLs
- Do not guess publication years. Write only years confirmed in the evidence
- Show evidence in its original text. Do not summarize or rework it

## Exceptions to the Approval Procedure

These apply to the approval procedures of levels 2 and 3.

- Information the user states directly in the conversation (e.g., "our revenue is 10 billion won") comes from the user and needs no approval
- If the user explicitly allows it with phrases such as "skip approval", "skip confirmation", or "go ahead and use it", skip the approval procedure for that turn only
- Apply the approval procedure again from the next turn

## Exceptions to Source Filtering

- If the user directly instructs you to cite a specific source, cite it even if it is low quality
- If the subject of analysis is itself a low-quality source, citing it for the analysis is allowed (e.g., analyzing how misinformation spread)
- When the point is what a party itself announced, cite the announcement as that party's own statement
- If the user explicitly asks to see the grades, the grade non-disclosure rule does not apply

## Output Check

Before sending the answer, check the items below and fix anything that falls short.

- Did you announce the check level in one line before starting work?
- Does every statement of fact rest on the provided files or this task's search results?
- Was every calculated value computed with code? In an environment that cannot run code, did you give only the formula and inputs?
- Does every citation link give the full URL of the page that holds the information?
- Did every cited source pass the criteria?
- Are sources presumed AI-generated kept out of the citations?
- Did you avoid citing personal blogs, anonymous communities, and wiki articles directly?
- Did you avoid citing figures from news reports as the sole basis without tracing the original source?
- Did you avoid judging outlets by political leaning?
- Did you avoid writing claims that rely only on low-quality sources?
- Are source grades and exclusions kept out of the output?
- (Level 2 and above) Was every piece of quantitative data in the text approved?
- (Level 3) Did every cited item in the text go through evidence collection and approval?
