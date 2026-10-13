# Document structure

> Translated from the Korean original. See the translation notice in SKILL.md.

## Conclusion first

- State the conclusion of the whole text once in the opening. The opening is the document title or the first section, whichever fits the macro structure and length of the text.
- Put the conclusion of each section in its first sentence.
- Do not delay the conclusion or leave it for the end, which forces the reader to infer it.
- Do not fill the opening with a topic introduction or a note about sources.
- SCQA and SCR open the first section with the situation, so place the conclusion in the document title as a proposition. The same applies to texts that follow the order of analysis stages below.

- (Wrong) Heading "## Overview", content "This report analyzes trends in digital transformation"
- (Using the document title) "# Cloud-first adoption needed"
- (Using the first section) Heading "## Cloud-first adoption needed", content "Adopters' gains now recover initial costs within one year"

A document consists of a top level and a section level, with section subdivisions added only when needed. Use the top level once, as the document title, holding the topic, the question, or the conclusion. The first section compresses the conclusion of the whole text, and later sections carry its evidence and elaboration. The Markdown level (`#`, `##`, `###`) for each tier depends on whether the document stands alone or sits inside a larger document, so apply the relative relation between tiers rather than fixed symbols.

## Macro structures

Use one of the three flows below for the whole text. Do not mix two in one text.

| Structure | Parts | Suitable text |
|---|---|---|
| SCQA | Situation (a stable state or agreed background the reader knows), complication (an event or change that disrupts it), question (the question that naturally arises for the reader), answer (the conclusion of the text) | Analytical reports that give decision makers an answer |
| Why-What-How | Need (why action is required, or the driver of change), action (the recommended action or deliverable), execution (the steps or resources to carry it out) | Proposals and recommendations that ask for a change in behavior |
| SCR | Situation (facts about the current state), complication (problems, threats, or changes in the current state), resolution (action that resolves the problem) | Texts that diagnose and propose improvements. In environmental analysis or internal diagnosis, put implications or forecasts from the facts in the resolution slot |

- When the user names a structure, use it.
- Without a named structure, choose by the purpose of the text.
- When the purpose is unclear and nothing is named, confirm the purpose with the user before writing.

## Order of analysis stages

Texts on environmental analysis or strategy move from the outside environment inward to the organization and then forward to execution. Each stage is part of one line of reasoning.

| Order | Stage | Role |
|---|---|---|
| 1 | Macro environment | Changes and trends in the external environment the organization cannot control |
| 2 | Micro environment | The current state of the industry, market, and competition the organization belongs to |
| 3 | Internal status | Diagnosis of the organization's capabilities, resources, and operations |
| 4 | Benchmarking | Implications drawn from the experience of similar organizations and leading cases |
| 5 | Strategy | Direction, goals, and strategic options that combine environment and internal status |
| 6 | Implementation | Tasks, schedules, and resource allocation that make the strategy concrete |

- Choose the stages to include by the purpose of the text. No stage is mechanically required.
- Keep the table order among the included stages. Do not reverse it, for example by placing the macro environment after the micro environment or internal status after strategy.
- Skipping non-adjacent stages is allowed (for example, from macro environment to internal status, or from macro environment through micro environment to strategy).
- When the user names the stages, use that set. Otherwise choose by purpose. Trend monitoring centers on the macro environment and adds the micro environment when needed. Status diagnosis covers macro environment, micro environment, and internal status. Setting direction adds strategy. Strategy development uses all six stages.
- When the purpose is unclear and nothing is named, confirm the purpose with the user before writing.

### Principles per stage

- (Macro environment) Write only objective phenomena and trends. Do not put interpretations, forecasts, solutions, or target states in this stage. Choose a classification that fits the topic. Use only the items among policy, economy, society, technology, environment, and law that actually affect the topic. Order the items by the purpose and emphasis of the text. PEST-type frameworks run politics, economy, society, technology, and STEEP-type frameworks run society, technology, economy, environment, politics. Research and development topics often center on policy (including institutions and law) and technology.
- (Micro environment) Stick to facts, as in the macro environment. An environment the organization cannot influence belongs to the macro environment, and one it can interact with belongs to the micro environment. Do not let the macro classification stand in for the micro environment. Write the micro environment separately. Choose a scheme that fits the topic among market, industry, competition, customers, suppliers, investment, and value chain (Five Forces, market and industry, value chain, customers and competition, and so on). Keep the link that shows how macro changes show up in the micro environment.
- (Internal status) Write the diagnosis as facts and leave prescriptions out. Cover strengths and weaknesses together. Show the gap between industry requirements found in the micro environment and internal capabilities. An organizational profile (history, organization chart, budget, staff) may come before the environmental analysis, and a position the user specifies takes priority. Capability diagnosis, such as gap analysis or strengths and weaknesses, comes after the environmental analysis.
- (Benchmarking) State why each case was chosen, and separate the similarities and differences with the organization. Examine failure factors and constraints along with success factors. Connect the implications of the cases to the diagnosis in earlier stages.
- (Strategy) Draw its grounds from earlier analysis. Do not introduce new grounds at this stage that earlier stages did not cover. Choose the derivation method freely by purpose, while keeping the correspondence between strategy and earlier analysis traceable by a third party.
- (Implementation) Derive tasks from the strategy. Do not add tasks unrelated to the strategy. Fit the level of detail to the purpose of the text.

### Implications

- Implications compress the meaning of the facts in each analysis stage by induction. They become the input to strategy, and in texts without a strategy they serve as the conclusion of the analysis.
- Place them at the end of each stage or collect them in a separate section after the analysis. Jumping from analysis straight to strategy without implications is a logical leap.
- Each implication must trace back to the stage its facts came from. Implications from the macro and micro environments are external factors (opportunities or threats), and implications from internal status are internal factors (strengths or weaknesses). Do not mix the two when building the strategy.

### Links between stages

- (Forward) Show which area of the micro environment each macro change affects, which internal capability each industry requirement is compared against, which strategic direction each internal gap produces, and which implementation task each strategy becomes.
- (Backward) Trace the finished text in reverse and confirm the strategy behind each task, the analysis behind each strategy, the industry requirement linked to each internal diagnosis, and the macro change linked to each micro finding. An element without traceable grounds is isolated. Add grounds in an earlier stage or delete it.
- (Boundary between analysis and prescription) Macro environment, micro environment, internal status, and benchmarking describe phenomena and form the analysis area. Strategy and implementation propose action and form the prescription area. Do not bring prescriptions forward into the analysis area, and do not repeat analysis in the prescription area.
- (Mapping completeness) Every fact in the text feeds at least one implication. Delete facts that feed none. In texts with a strategy, every implication feeds at least one strategy. Feed an unused implication into a strategy or delete it.
- (Overseas and domestic) When the macro or micro environment covers overseas and domestic trends together, give each classification item (for example, policy trends) one section, and within it write overseas trends first and domestic trends next. Show the influence, response, or gap between them. This pattern does not apply to texts on domestic trends only.

## Vertical relations and horizontal grouping

### Vertical relations

- A parent message is the conclusion of its children, and the children are evidence for the parent. The parent states the specific result the children produce together. Do not write empty summaries such as "Several problems exist".
- Going down, each level must answer "Why can you say that?" Going up, each level must answer "So what does it mean?" Both directions must hold.
- Abstraction decreases and specificity increases as you go down. Parent items carry context and claims, and child items carry elaboration and examples.
- A message whose response link is broken is isolated. Move it to another tier or delete it.
- Adjacent sentences form response links. Each later sentence plays one role toward the earlier one: elaboration, evidence, example, contrast, or conclusion. Avoid lists that only add unrelated facts.

```markdown
With response links
- The existing management approach faces several limits in a fast-changing technology environment
    + As technology changes faster, timely decisions have become difficult under the existing linear process
    + As technologies converge faster, the range of expertise needed to find and assess opportunities has widened

List only
- Management approach changing
    + AI advances
    + More data
    + Faster convergence
```

### Horizontal grouping

- Group messages at the same level by kind. One group is a set of sibling messages forming the same step of the storyline.
- Use one grouping method per group. An inductive group gathers facts or cases of the same kind and draws a common conclusion, sharing the same subject or the same predicate. A deductive group combines a major premise and a minor premise into a conclusion, forming a two- or three-step chain.
- Use one order per group: time order (including cause-to-effect order), structural order (order of component parts), or degree order (order of importance or size).
- Three or four items per level are recommended. At five or more, add a higher category and split them into two tiers. A reader holds about four chunks at a time.
- When one message mixes two or more contents, split them into separate messages.
- For classification criteria and overlap and gap checks, follow `classification.md`.

## Section flow types

- Choose one of the flows below for the development inside a section, according to the purpose of the text.
- (Change flow) From the previous state to the drivers of change, the new pattern, and the implications
- (Problem flow) From the current state to its limits, the alternatives, and the expected effects
- (Diffusion flow) From emergence to spread, cases of application, and the outlook

## Heading names

- When you build the structure, name the headings with care first and set the storyline between them. Check the heading names once more right before final output.
- A reader should know the content under a heading from the heading alone.
- Give each heading one topic. Do not join two topics with "and", "with", "or", or "/".
- Keep headings at the same level in one form: keyword headings or sentence headings.
- Name sibling headings in the same pattern. Put "## Regional market trends" next to "## Global market trends" rather than "## Regional market analysis" next to "## Global trends". Also keep sibling sections similar in length and density.
- Do not repeat generic labels unrelated to the content, such as "Overview", "Background", "Current status", "Conclusion", "Key recommendations", or "Key diagnosis". Carry content, as in "Shift to a multi-site distributed model needed" or "Limits of the single-site model".
- Do not put framework names such as SCQA or MECE, the names of their parts (situation, complication, question, answer), or the names of analysis stages such as "macro environment", "micro environment", or "internal status" into headings as they are. Replace them with keywords or sentences that fit the content.

## One message per unit

When information is laid out with equal weight, the burden of deciding what to look at shifts to the reader. When two or more independent claims are squeezed into one unit, the reader cannot tell what it says. Both problems come from the habit of placing every piece of information you have without choosing what to deliver.

### Units and messages

- A unit is a block of expression the reader sees and digests at once. One section, one `-` item with its `+` items, one paragraph, one table, and one figure are each a unit. In slide scripts, one slide is a unit.
- A message is the one judgment sentence the reader should remember from that unit. A judgment sentence is a claim with a subject and a predicate ("Domestic market profitability falling due to low-price imports"). Topic labels such as "Market status", "Background", or "Key issues" are not messages.
- The test question is "What one sentence should a reader of this unit remember?" No answer means the message is missing. An answer that strings together two or more independent claims means the unit is overloaded.
- When a unit has two or more messages, split it (separate sections, separate paragraphs, split tables, add slides).

### Message position

- Put the message at the head of the unit. In a paragraph the first sentence carries it, in a table or figure the title, in a slide the headline.
- With a sentence heading, the heading carries the message and the first sentence of the body starts the evidence.
- With a keyword heading, the heading names the subject of the message and the first sentence carries the judgment.
- When the subject named by the heading and the message of the first sentence diverge, rename the heading or move the content.

### Selecting components

- By default, keep the key components supporting the message to three or four per unit. Components do not overlap and each covers a different part of the message.
- Do not stretch content that two items cover into three or four to fill a count. Frameworks with a fixed count, such as a four-quadrant matrix or a five-step process, keep their own count.
- When five or more seem necessary, work in this order. First check whether messages are mixed, and split the unit if there are two or more. Next group the items under three or four higher categories and move details down a tier. Last, delete items that do not support the message.
- Compress by selecting components. Choose, discard, and give the remaining components enough room. Keeping every component and only shortening the sentences raises density and leaves the reader's burden in place.
- Delete in this order of priority: information unrelated to the message, background the reader already knows, duplicate evidence supporting the same conclusion, and decorative figures and cases that do not inform the judgment.
- Deletion is the default for content left out by selection. Do not keep it because it took effort to write. When it has value as an independent message, move it to its own unit. When it only has reference value, move it to an appendix, footnote, or attachment. Do not mention it in the body while leaving out the detail.

### Expressing hierarchy

- Inside a unit, divide weight into three tiers: message, supporting components, details.
- Set one point of emphasis per unit. In tables and figures, highlight one series and show comparison series in low saturation. Attach data labels only to points related to the message.
- When every element has the same weight, treat the unit as lacking emphasis and rearrange it.

### Signs of an undifferentiated list

Rebuild the unit when any of these applies.

- Five or more parallel items sit at the same level.
- One paragraph holds two or more sentences with independent claims.
- The title or headline stays at a topic label with no judgment.
- Every item has the same visual weight and length, leaving no point of emphasis.
- Elements of different kinds, such as cause and effect, phenomenon and measure, or fact and opinion, are mixed in one list.
- The subject named by the heading differs from the message of the first sentence.
- You cannot answer "What one sentence should the reader remember from this unit?"

The count limits do not apply to parts where the user requested an exhaustive or detailed list, to outputs whose purpose is completeness such as statutes, regulations, and checklists, to frameworks and standard forms with a fixed count, or to quotations and transcribed originals. Outputs aimed at completeness still use the hierarchy rules.

## Modular composition

- Write each section so it makes sense when read alone. Sections should be easy to combine with or separate from others.
- Do not use expressions that presume another section, such as "as mentioned above".
- Do not scatter the same figure or definition across several places. Define it in one place so a change or deletion takes one edit.
- Use the fewest sections that hold the content without overlap.

## Tables and quantitative data

- Use tables to summarize the core of the text. Always use them in long texts.
- Three tables or fewer per text are recommended. More tables blur the core.
- Place a table where it best delivers the core message: the beginning, middle, or end of the text. A table right after a claim reads naturally. Do not place two tables back to back. Alternating claims and tables is fine.
- Do not put tables inside `>` blocks or code blocks.
- Build rows, columns, and cell text on one criterion without overlap, and find the most concise combination.
- Three key quantitative data points or fewer per text are recommended.

## Diagnostic items

- (Macro structure) Does the whole text use only one macro structure?
- (Conclusion position) Do the opening and the first sentence of each section hold conclusions?
- (Response links) Do parent and child messages hold in both directions?
- (Grouping consistency) Does each group of same-level messages use one grouping method and one order?
- (Classification consistency) Are items free of overlaps and gaps, under one criterion?
- (Cognitive load) Are there four or fewer messages at each level?
- (Unit message) Does each unit have exactly one judgment message?
- (Stage order) Are the analysis stages free of reversals?
- (Stage links) Does each stage narrow the focus of the next, and are the grounds of strategy and implementation found in earlier stages?
- (Analysis and prescription) Are prescriptions kept out of the analysis area?
- (Implications) Do the implications connect the facts and the strategy?
- (Isolated elements) Are there no elements disconnected from what comes before and after?
- (Mapping completeness) Is the correspondence among facts, implications, and strategies complete?

A diagnostic report gives pass or fail per item, and the location and direction of improvement for each failure. When the structure needs rebuilding, add a rearrangement plan. Point out problems through the structure, without framework names ("The conclusion is missing from the opening").

## Exposure rules

- Do not use framework names in the output, such as Minto, pyramid principle, SCQA, Why-What-How, SCR, MECE, So What, Why So, outside-in, strategic storyline, or deductive flow. Do not use the names of their parts as section labels, as in "## Situation" or "## Complication".
- Do not declare that you applied a method, as in "structured by the pyramid principle", "written the Minto way", "conclusion-first principle applied", "organized outside-in", or "written as a strategic storyline".
- Do not paraphrase a definition to hint at it, as in "each message answers the message above", "classification items operate on a single dimension", or "written in a structure that narrows from the outside environment inward".
- Do not justify yourself, as in "this text covers everything without omission", "each item is mutually exclusive", "covers everything from macro to execution", or "derived through every analysis stage".
- Do not add sections the user did not request, such as "Methodology", "Limitations of the analysis", "Structure explanation", or "Analytical framework".
- Carry out structural diagnosis of material under analysis as requested. Inside a diagnostic report, state problems of the material, such as a missing conclusion, grouping errors, missing stages, or logical breaks.
- Cite external principles unrelated to this file as usual (for example, "prepared under accounting standards").

## Examples

### Decision report (SCQA)

```markdown
# Shift to a multi-site distributed supply chain model needed

## Change in the global division of labor
- Single-site concentration models that put cost efficiency first long served as the industry standard
- Pandemics and geopolitical change exposed the risk of supply disruption under single-site dependence
- Stronger supply chain diversification policies of major governments reshaping the industrial environment

## Structural limits of the single-site model
- (Concentrated risk) An incident at the single site stops every supply line at once
- (Response speed) Limited supply adjustment at a single site slows the market response to demand swings
- (Policy exposure) No alternative site to spread the impact of policy changes in the host country

## Decision needed on how to restructure the supply chain model
- Keeping the single-site model means continued build-up of risk
- A full switch may bring cost burdens and operational shocks
- Comprehensive review needed on timing, scope, and approach of the transition

## Phased transition to a multi-site distributed model
- (Direction) Geographic distribution, functional distribution, and supplier diversification pursued together
    + Additional sites in main market regions to build supply capacity within each region
    + Separate sites for core and general components to manage them by risk grade
    + Gradual reduction of single-supplier dependence and a multi-supplier operating system
- (Easing the burden) Phased rollout by priority to spread the cost burden
    + Core components with high risk grades set as the first transition targets
    + Expansion to main market regions after the core component transition stabilizes
    + Gradual reduction of existing sites during expansion to soften the shock to staff and assets
```

### Direction-setting text (order of analysis stages)

```markdown
# Online-linked content programs of a regional cultural foundation need expansion

## Change in how cultural content is consumed
- Consumption of cultural content through online platforms settled into everyday habit after the pandemic
- Demand rising for participatory content where audiences create and share
- Central government support for regional culture shifting from one-off events to sustainable program models

## Competition among regional cultural foundations
- Program structures centered on offline events such as festivals, exhibitions, and performances repeated across most foundations
    + Duplicate planning of similar programs leaves little room for differentiation
    + Limited experience working with private content companies weakens online platform programs

## Current operations of Foundation B
- Online content programs a small share, with most annual programs being offline events
    + No dedicated online content planners, leaving the foundation dependent on outside contractors
    + Contact with content companies at an early stage
- Stable collaboration network with local artists and creators
    + Festival and exhibition planning experience serves as an asset that keeps offline content quality high
    + Artist network usable as a creative talent pool for online content planning

## Implications for restructuring content programs
- (External opportunity) Settled online consumption and a policy shift toward sustainable models widen room for online-linked programs
- (Internal weakness) Lack of online planners and of collaboration channels with content companies limits the use of this opportunity
- (Internal strength) Offline planning experience and the artist network can become sources of online content

## Direction for restructuring content programs
- (More online programs) Plan online content linked to existing offline events first to lower the entry burden
    + Existing assets reused by turning the planning process of offline events into online content
    + Dedicated online planners hired in stages to reduce dependence on outside contractors
- (Regular collaboration with content companies) Joint planning programs with local content companies run on a regular cycle
    + Artist network and content company network linked to lay the ground for converged content
    + Collaboration scope widened gradually based on joint planning results
- (Audience participation) Participation built into the planning stage to secure differentiation from other foundations
```

### Separating messages per paragraph

```markdown
Before
Our new product launch is delayed because of unstable parts supply. The supplier's capacity is also insufficient. Meanwhile, a competitor has launched a similar product first and taken the market, and its marketing budget is twice ours. Therefore we should move the launch date up, increase the marketing budget, and diversify suppliers.

After (cause, competition, and response split into separate items)
- Launch delay caused by unstable parts supply
    + Sourcing of key parts concentrated in a single supplier
    + That supplier's capacity falls short of our order volume
- Competitive position worsening during the delay
    + Competitor absorbed early demand by launching a similar product first
    + Competitor's marketing budget about twice ours
- Sourcing diversification as the first response priority
    + Stable parts supply is the precondition for a shorter launch schedule and a larger marketing budget to take effect
    + Launch schedule and marketing increase to be reviewed in turn after securing multiple suppliers
```
