> This English edition is a translation of the Korean original. Some rules were adapted to English writing conventions, and the skill may behave differently from the intent of the original.

# Bullet Report Rules and Output Templates

These rules govern how the environment analysis report is written in structured bullet style. If the user specifies another style or format, the user's choice comes first. The original rules were designed for Korean report writing, where bullets end in nouns (gaejosik style). This edition restates them as English conventions.

## Report structure

| Order | Part | Content |
|---|---|---|
| 1 | Title | Topic and scope. If the user wants a conclusion-led report, state the main conclusion as a proposition |
| 2 | Summary | Key facts and implications in compressed form, so readers see the conclusion first |
| 3 | Scope | Subject, topic, geography, time frame, data reference date. Includes the topic overview for industry or technology topics |
| 4 | Organization profile | Profile of an organization subject. Moves to another position if the user sets one |
| 5 | Analysis sections | Modules that ran, in the order macro environment, micro environment, internal status, benchmarking |
| 6 | Implications | Implications grouped by source stage |
| 7 | Appendix | Fact register. Included when implications exist or results go to later analysis |

A partial analysis uses only the parts its modules need. A short report on a single category can skip the summary and cut the scope to a line or two.

Each analysis section describes the current state first and recent changes after it. The implications at the end of the report state what both mean.

## Writing sections

- (Summary first) The first bullet of each section compresses the section's facts into a summary. The summary stays within the facts
- (Vertical relation) A parent bullet is the conclusion of its child bullets, and the children are its evidence. Reading down answers "why is that so?", and reading up answers "so what?"
- (Horizontal grouping) Bullets on one level group content of the same kind. Three or four per level is the recommended size. At five or more, create a parent group
- (Cross ordering) When both global and domestic trends appear, write global first within each category and then move to domestic. Put regional last if present

## Titles and headers

- One header holds one topic. Split "Policy and technology trends" into "Policy trends" and "Technology trends"
- Name headers so readers can tell what lies below from the header alone. Choose either keyword style or sentence style and keep it consistent within one report
- Title analysis sections with keywords that carry the category and topic. Do not title analysis sections with stage names such as macro environment or micro environment, or with generic labels such as overview, background, or current status
- Summary, scope, implications, and appendix stay as functional headers. Subheaders inside the implications section use stage names for later analysis
- Name sibling headers in the same pattern. Put "Domestic market trends" next to "Global market trends"
- Review header names once more before the final output

## Bullet structure

```
# Title
## Section title
- (Subtitle) Summary or claim
    + Supporting fact
    + Supporting fact
> Publisher (year), title (link)
```

- `-` bullets have no indentation and carry a summary or claim
- `+` bullets are indented one level and carry supporting facts
- Use child bullets only when two or more parallel items exist. A single child merges into the parent sentence or becomes a separate top-level bullet. A single child is fine when the parent is a proper name or framework and the child gives its one-line definition
- Three or four child bullets is the recommended size
- `>` blocks hold sources and data notes only

## Sentences

- One sentence carries one message. If who, when, where, what, why, or how appears twice in one sentence, split it
- Write bullets as compact statements. Drop filler words and keep a clear subject and verb where the statement needs them. Use a formal tone and no conversational or chatty phrasing
- Close statements with specific nouns. Avoid vague placeholders such as "thing", "aspect", or "part" when a specific noun exists
- Do not chain several facts in one sentence with "and", "but", "while", or "which". Split them into separate sentences
- Use commas to list three or more items of the same category. Join two items with "and"
- Put subtitles in parentheses in the form `(Subtitle) Content`. Do not attach subtitles with colons or hyphens
- Name subtitles by their content. Avoid empty subtitles such as "(Explanation)", "(Evidence)", or "(Claim)", and avoid repeating the same subtitle
- Use the official full names of organizations, policies, programs, and products. Spell out abbreviations at first use
- Some markdown renderers turn the tilde into strikethrough, so write ranges with a hyphen (for example, 2021-2025)
- Report outlooks published by sources with who made them, the publication year, and the outlook period

Do not use the expressions below.

| Type | Examples |
|---|---|
| Comments on the text or the writing process | "This report", "Let's look at", "To summarize", "Search results show", "As requested" |
| Contrast framing | "Not just A but B", "Beyond A to B" |
| Number declarations | "Three pillars", "Four directions" |
| Empty connectors | "In this context", "This has significant implications" |
| Exaggeration | "Groundbreaking", "explosive", "unprecedented", "game-changer" |
| Symbol abuse | Em dashes, dramatic ellipses, bold for emphasis |
| Procedure terms | Module, verification level, quality tier, rating |

## Quantitative data

- Write every figure so that who measured what, when, and by which method can be answered. Example: "A 2024 survey by OO Research projects the domestic market to grow from about KRW 1.2 trillion in 2023 to about KRW 2.0 trillion in 2028, a compound annual growth rate of about 10.8% (survey-based estimate, base scenario)"
- Prefer time series of 3 to 5 years or more, and report the compound annual growth rate and the share of the total alongside
- Keep the key figures in section bullets to a few per section, and move the rest into tables
- Use thousands separators and units

## Tables

- Use tables for lists and comparisons of items with the same attributes, such as policies, technology trends, players, facilities and equipment, and programs
- Put a bullet with the table's summary before each table. Do not stack tables without a summary between them
- Keep tables outside `>` blocks and code blocks
- Keep columns from overlapping and cells short

## Citations

- The format is `> Publisher or author (year), title (link)`
- For several sources, use separate `>` blocks with a blank line between them
- Put the source of quantitative data right after the bullet group that contains it. Sources of qualitative statements can be gathered at the end of the section
- Link to the full address of the page that carries the information
- Cite internal material as `> System or document name (reference date), table or document identifier (query conditions)`, with no personally identifying information

```
> Ministry of Science and ICT (2025), title (https://...)

> Statistics Korea (2024), title (https://...)
```

## Implications section

Write the implications section as one-line bullets under stage subheaders. Keep it out of tables so later analysis can read the source stage at a glance.

```
## Implications

### Macro environment
- Implication sentence (evidence MAC-01, MAC-04)

### Micro environment
- Implication sentence (evidence MIC-02)

### Internal status
- Implication sentence (evidence INT-03, MIC-05)

### Benchmarking
- Implication sentence (evidence BMK-01, INT-02)
```

Do not create subheaders for stages that did not run.

Gathering implications at the end of the report is the default. If the user wants it or the analysis sections are long, each analysis section can end with its own implications, and the same rules on evidence IDs and stage grouping still apply.

## Appendix: fact register

| ID | Category | Fact | Reference date | Source | Data channel |
|---|---|---|---|---|---|

## Full report skeleton

```
# [Topic] external and internal environment analysis

## Summary
- Key implications and key facts

## Scope
- (Subject) Subject and topic, topic overview
- (Coverage) Geography, time frame, data reference date

## [Topic] policy trends
- (Global) Summary
    + Supporting fact
    + Supporting fact
- (Domestic) Summary
    + Supporting fact
    + Supporting fact
> Source

## [Topic] market trends
...

## [Subject] capabilities
...

## [Comparison target] cases
...

## Implications
### Macro environment
...

## Appendix
(Fact register)
```

## Partial analysis skeleton

```
# [Topic] policy trends

## Scope
- (Coverage) Geography, time frame, data reference date

## Global [topic] policy
- Summary
    + Supporting fact
    + Supporting fact
(Policy table)
> Source

## Domestic [topic] policy
...

## Implications
### Macro environment
- Implication sentence (evidence MAC-01, MAC-02)
```

## Writing check

- The title carries the topic and scope
- Analysis section titles are content keywords, and each header holds one topic
- The first bullet of each section is a summary, and child bullets are evidence
- Each sentence carries one message
- Statements are compact and formal
- Subtitles use parentheses and describe their content
- Every figure has a source, a reference date, and a method
- Each table is preceded by a summary bullet
- Source links point to the full page address
- No banned expressions or procedure terms appear
- Every implication cites evidence IDs
