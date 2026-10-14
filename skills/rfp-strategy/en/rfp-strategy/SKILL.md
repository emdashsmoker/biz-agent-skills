---
name: rfp-strategy
description: Analyzes a request for proposal (RFP) and builds a bid strategy. Analysis mode uses only the RFP to organize project terms, eligibility, evaluation criteria, scope, writing rules, and project type. Strategy mode adds bidder information and web research for the bid decision, client needs, competitors, differentiators, execution strategy, module and task design, storyline, staffing, price direction, and a project charter. Built for research, consulting, IT planning, and support-program bids under Korean public procurement. Use when the user mentions an RFP, statement of work, tender notice, proposal or win strategy, bid preparation, competitor analysis, module design, similar-project screening, or a project charter, or attaches an RFP file. If the request does not say analysis or strategy, ask first. Analysis mode reads references/analysis.md. Strategy mode reads references/analysis.md, references/strategy.md, references/competition.md, and references/modules.md. Converts files with scripts/parse.py.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# RFP Analysis and Proposal Strategy

> This English edition was translated from the Korean original. It may behave differently from the original's intent. The procedures follow Korean public procurement rules and Korean document formats (HWP, HWPX).

This skill turns an RFP into the information needed to decide whether to bid and how to position the proposal. The work runs in two modes, split by the input each one needs. Anything that can be settled from the RFP alone belongs to analysis mode. Anything that needs the bidder's own information or outside research belongs to strategy mode. Strategy mode starts from the output of analysis mode.

## Terms

Every output uses these terms with the same meaning.

| Term | Meaning |
|---|---|
| RFP | The document set the client issues to bidders. Includes the request for proposal, statement of work, tender notice, and evaluation criteria |
| Client | The organization that commissions the project and evaluates proposals |
| Bidder | The user's organization. For a consortium, all members |
| Project | The whole body of work the RFP asks for |
| Requirement | The lowest-level item in the RFP scope that cannot be split further. Tagged with IDs T1, T2, and so on |
| Module | A work package that groups the project by deliverable. Written Module 1, Module 2 |
| Task | A unit of work inside a module. Numbered Task 1-1, carrying the parent module number |
| Deliverable | A document, dataset, or meeting result produced by a module or task |
| Outcome | The change that happens at the client after the project ends. Written as who gets what, by when, in what state |
| Stated need | The need expressed in the RFP's background and purpose sentences |
| Underlying need | The client's reason for commissioning the project at this moment. Handled as a hypothesis backed by public sources |
| Differentiator | A strength of the bidder that competitors cannot claim on the same evidence. Backed by at least one of track record, data, or people |
| Execution strategy | A way of working the bidder adds to get past the hard parts of the project |
| Key wording | The exact terms the RFP uses for project names, deliverable names, phase names, and target names |
| [CONFIRM] | Marker for a cell that the inputs could not fill. Filled only by the user's answer or the RFP text |

## Choosing the mode

| Item | Analysis mode | Strategy mode |
|---|---|---|
| Inputs | RFP | RFP, bidder information, web search permission |
| Outputs | 01_rfp_analysis.md | 01_rfp_analysis.md, 02_proposal_strategy.md, 03_project_charter.md |
| Reference files to read | references/analysis.md | references/analysis.md, references/strategy.md, references/competition.md, references/modules.md |
| Questions to the user | Request the RFP if missing | One intake question round, one storyline review |

If the request shows the mode, go straight to it. "Summarize this RFP" and "pull out the scoring table" are analysis mode. "Build a proposal strategy", "win strategy", "competitor analysis", and "design the modules" are strategy mode. If the mode is unclear, ask once with the message below. While waiting for the answer, only convert the RFP.

> Please tell me which you need: RFP analysis or a proposal strategy. Analysis uses only the RFP to organize project terms, eligibility, evaluation criteria, and scope. Strategy builds on the analysis and uses your company's track record, staff, and strengths to cover the bid decision, competitors, execution strategy, and work structure.

- If there is no RFP, ask: "Please send the RFP (request for proposal, statement of work, tender notice) as a file."
- If the user asks only for similar-project screening, run only the similar-project screening section of references/strategy.md. The screening criteria use the project type and key wording, so run analysis mode first.

## Converting input documents

Convert the RFP and attachments to Markdown with scripts/parse.py before reading. Install the dependencies first.

```bash
pip install "markitdown[all]" python-hwpx pdfplumber olefile beautifulsoup4 lxml pyhwp six
python scripts/parse.py <input file> <output file.md>
python scripts/parse.py <input file> <output folder> --chunk --chunk-size 2000
```

| Format | Engine | Fallback |
|---|---|---|
| PDF | markitdown (body), pdfplumber (tables) | None |
| HWPX | python-hwpx Markdown export | python-hwpx text extraction, direct XML parsing |
| HWP | pyhwp (hwp5txt) | olefile binary parsing |
| DOCX, PPTX, XLSX, HTML, CSV, JSON, XML, TXT, EPUB, ZIP, images, audio | markitdown | None |

- PDF body text and tables are extracted separately. If tables exist, `<file name>_tables.md` is created as well. Scoring tables and submission lists usually sit in tables, so read both files.
- pyhwp replaces HWP tables with `<표>`. If the table content matters, ask the user for an HWPX or PDF copy of the same document.
- If pyhwp fails to install or run, the script switches to the olefile path. That path reads table text too, but some characters may break and Chinese characters may drop out.
- An extracted character count of 0 usually means a scanned image PDF. Tell the user that OCR is needed.
- For a password-protected file, ask for an unlocked copy.
- Split long documents by heading with the `--chunk` option.

Notice for the HWP binary parsing path: 본 제품은 한컴의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다. (This product was developed with reference to the HWP document file (.hwp) specification published by Hancom.)

## Analysis mode

1. Read the converted text from start to finish. Scope, evaluation criteria, and eligibility are scattered across the body, tables, and annex forms.
2. Write 01_rfp_analysis.md using the template and rules in references/analysis.md.
3. Compute score totals, amount conversions, and durations in code and check them against the RFP figures.
4. In the reply, give only the file location, any eligibility conditions that could block participation, and the items that need confirmation.

Extraction relies on judgment after reading the source. RFPs differ in section structure, numbering, and table use, so regex extraction misses items or picks up wrong ones. The script only converts formats.

## Strategy mode

| Step | Work | Output | Condition to move on |
|---|---|---|---|
| 1 Analysis | Run all of analysis mode | 01_rfp_analysis.md | Analysis file complete |
| 2 Intake questions | Present the questions below together with the analysis result | User answers | Answers received |
| 3 Strategy | Write in the order of references/strategy.md. Competition follows references/competition.md and work structure follows references/modules.md | 02_proposal_strategy.md | Only user-judgment items remain as [CONFIRM] |
| 4 Storyline review | Present the storyline section and the module summary table and apply requested changes | Review record in 02_proposal_strategy.md | User confirms |
| 5 Charter | Write the project charter from the confirmed content | 03_project_charter.md | Pre-completion check passes |

Ask these intake questions in a single turn.

- Scope of participation (whole project or part) and whether a consortium is planned, with each member's role
- Bidder information: business areas, headcount, certifications, and track record list (project name, client, period, amount, main content). Pasted table text or a file is enough
- Degrees, experience, and similar-project history of the principal investigator candidate and team member candidates
- Whether a list of advisory committee candidates exists
- Average monthly labor rate and available staff. Used for capacity and cost calculations. Without them, both calculations are skipped
- Any past award results or competitor information the user holds
- Whether web search is allowed. If not, the evidence for underlying needs and the competitive structure are filled only from user-provided material
- Whether the project type judged in analysis mode is correct

Mark unanswered items [CONFIRM] and continue.

The storyline gets its own review because of the cost of change. An argument is easy to fix while it is a table of a few dozen lines. Changing it after the proposal manuscript is written means rewriting the whole manuscript.

Pure software development projects are outside the scope of the module skeletons in references/modules.md. For those, use the RFP's scope structure as the modules. The rest of analysis mode and strategy mode applies unchanged.

## Writing principles

- Before organizing the RFP's requirements, work out why the client commissioned this project now and where the results will be used.
- Separate facts from hypotheses. Facts from the RFP carry their source location (page or clause number). Hypotheses are labeled "hypothesis" and carry supporting sources.
- Leave a cell as [CONFIRM] when there is no evidence to fill it. Do not write estimates as facts.
- Compute totals, ratios, amount conversions, and scores in code. Do not use mentally calculated numbers.
- Keep project names, organization names, deliverable names, and task names exactly as written in the RFP. Evaluators read the proposal against the RFP's wording.
- Split items at the same level by a single criterion. Items should not overlap and together should leave nothing out. Do not name the classification criterion in the output.
- Write output documents in the user's language, in concise bullet style, one point per sentence.
- Use bold only for conditions that could lead to disqualification, point deductions, or exclusion.
- State unknowns as unknown.

## Evidence and sources

- Prefer primary sources on the web: statutes, government and public agency publications, official statistics, notices on organizations' own websites, and academic papers.
- For news reports, find and cite the original source the report used. If the original cannot be found, do not base a conclusion on the report alone.
- Do not use personal blogs, anonymous communities, wiki articles, or AI-generated content sites as evidence. On the self-disclosure path of the competitor search, posts an organization publishes about itself count as that organization's own statement.
- Cite sources as "Organization or author (year), title (URL)". The URL goes down to the page that holds the material.
- Cite only statute articles whose text has been checked, with their article numbers.
- Regulatory figures such as procurement thresholds and participation floors change. Check the value in force on the notice date before using it.
- Use only the staff and advisory candidates the user provides. Do not invent names or compile lists of individuals from the web. Competitor tables list organizations only.

## Replies

- A reply contains only file locations, progress, items for the user to decide, and errors. Do not copy file contents into the reply.
- Group questions into one turn. For items with a sensible default, state the default applied and continue.
- For revisions, report only where things changed.
- If the environment has a file delivery tool, deliver files with it. Without one, give the path. If files cannot be saved at all, put the output document in the reply body.

## Pre-completion check

- Are all lowest-level scope items of the RFP in the requirement table, verbatim?
- Was the score total computed in code and matched to the RFP total?
- Are eligibility conditions that could block participation in bold?
- Do the figures and wording in the outputs match the source?
- (Strategy mode) Is every requirement assigned to at least one task?
- (Strategy mode) Does every underlying-need hypothesis have a module or task that answers it?
- (Strategy mode) Does every differentiator have at least one piece of evidence from track record, data, or people?
- (Strategy mode) Is every execution strategy paired with the risk it resolves and the value it secures?
- (Strategy mode) Is the client's outcome written as who gets what, by when, in what state?
- (Strategy mode) Does every competitor candidate have a source URL?
- (Strategy mode) Are the remaining [CONFIRM] items ones only the user can answer?
