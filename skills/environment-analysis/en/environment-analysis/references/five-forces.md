> This English edition is a translation of the Korean original. Some rules were adapted to English writing conventions, and the skill may behave differently from the intent of the original.

# Five Forces Competitive Structure Analysis

This procedure analyzes an industry's competitive structure with Porter's Five Forces: threat of new entrants, bargaining power of suppliers, bargaining power of buyers, threat of substitutes, and rivalry among existing competitors. Porter (2008, The Five Competitive Forces That Shape Strategy) treated government policy, complements, industry growth rate, and technology as factors that change the strength of the five forces, and did not count them as a sixth force. This procedure follows the same approach and handles government support or regulation inside the rating evidence of each force.

## Mandatory output rules

These rules take precedence over all other rules.

- If the industry value chain is broken down, output a prose section and a competitive environment table separately for each industry value chain market. An output that skips the market tables and shows only a summary table does not count as complete
- If domestic and global are analyzed separately, output prose and a table for each industry value chain market for both global and domestic
- All competitive environment tables use the same standard format (force, intensity, content, evidence, data). Do not use ad hoc formats such as comparison tables
- When domestic and global are separated, label the foreign side "Global"

## Execution

- (Automatic mode) If the user gives only an industry name, run everything from scoping to analysis automatically
- (Guided mode) If the user has already set the scope or units of analysis, apply those values first
- (Evidence) Use material attached by the user as the primary evidence and fill gaps with web search. Do not use quantitative data without a source
- (Confirmation timing) Confirm the scope together with the scope confirmation in Step 1 of SKILL.md, in one round

## Step 1 Scoping

| Item | Description | Example |
|---|---|---|
| Industry name | The industry to analyze | Hydrogen energy industry |
| Industry definition | Scope of the analysis and what is included and excluded | Covers hydrogen production, storage and distribution, and end use. Other energy sources are treated as substitutes |
| Geographic scope | One of: domestic only, foreign only, domestic and global combined, domestic and global separate | Domestic and global combined |
| Time scope | Horizon for the intensity outlook. One of: current (no outlook), medium term (within 3 years), medium to long term (within 5 years), industry life cycle (within 10 years), very long term (within 30 years, long-term investment view), user-defined period, unlimited | Medium to long term |
| Industry value chain breakdown | Breakdown by the stages the industry uses | Production, storage and distribution, end use |
| Unit composition | One of: analysis by industry value chain market, whole-industry analysis, mixed | Market-level analysis followed by an industry summary |

### Scoping principles

- (Industry definition) State clearly what is included and excluded. Decide whether adjacent industries or related technologies are part of the analysis or substitutes, which fixes the boundary of the analysis
- (Time scope) If the user does not set it, use medium to long term (within 5 years). If "current" is chosen, do not output the intensity outlook column
- (Industry value chain breakdown) Use the stage names the industry itself uses. Generic names such as "materials, components, equipment, infrastructure" appear only when the industry uses them widely. Units of analysis must not overlap and together must cover the whole industry
- (Whole-industry analysis) If no breakdown is needed or the user wants a whole-industry analysis, treat the whole industry as one unit of analysis

### Geographic scope options

| Option | Handling |
|---|---|
| Domestic only | Analyze the domestic industry only |
| Foreign only | Analyze foreign industries only |
| Domestic and global combined | Units of analysis follow the industry value chain, and domestic and global trends are described together within each unit |
| Domestic and global separate | For each industry value chain market, run the global analysis first and the domestic analysis separately. Derive intensity and tables for each market on its own |

Porter (2008) advised treating each geographic area as a distinct industry when industry structure differs widely between areas. When global and domestic structures are likely to differ, the separate option fits that criterion.

### Automatic setup when the user does not specify

1. If attachments exist, extract the industry definition and industry value chain structure from them. Otherwise find them through web search. Do not build an industry definition or industry value chain from model knowledge alone
2. Draft the units of analysis from the industry value chain structure found
3. Propose a geographic scope. The default is domestic and global combined
4. Confirm the industry definition, industry value chain breakdown, and geographic scope with the user to fix the scope

## Step 2 Evidence collection

Collect basic industry information first, then force-specific information.

### Basic industry information

Collect the items below for each unit of analysis first. They are the shared base for rating all five forces.

| Item | What to collect |
|---|---|
| Market size | Size in monetary terms per unit of analysis. For separate domestic and global analysis, collect both |
| Market outlook | Growth outlook such as compound annual growth rate. Outlook period and source required |
| Key market indicators | Indicators common in the industry, such as revenue, employment, number of establishments, location quotient |
| Key players | Market share, size such as revenue or headcount, business structure and main products, main customer groups, main competitors |

### Force-specific information

| Force | What to collect |
|---|---|
| Threat of new entrants | Entry barriers (capital requirements, technical difficulty, regulation, permits), economies of scale, likelihood of retaliation by incumbents, recent entries, government support or restriction of entry |
| Bargaining power of suppliers | Number of suppliers, substitutability of inputs, switching costs, potential for forward integration by suppliers, progress of vertical integration |
| Bargaining power of buyers | Number of buyers, purchase concentration, product differentiation, buyer switching costs, potential for backward integration by buyers, progress of vertical integration |
| Threat of substitutes | Existence of substitutes, price-performance, switching costs, growth trend of substitute markets, range of horizontal substitution |
| Rivalry among existing competitors | Number of competitors, market growth, fixed cost structure, product differentiation, exit barriers, government support or regulation, progress of horizontal integration |

Organize the collected information by unit of analysis as input to Step 3, and cite a source for each quantitative data point.

## Step 3 Force-by-force analysis

For each industry value chain market, describe the five forces in turn, then summarize market conditions and key players. Write the intensity rating (conclusion) first, followed by market data and player information (evidence).

```
## Hydrogen production market

### (Threat of new entrants : Medium→High) Technical barriers remain, but falling production costs widen room for new entrants

- (Current) Rating summary
    + Structural evidence, qualitative
    + Structural evidence, quantitative
- (Outlook) Rating summary
    + Structural evidence, qualitative
    + Structural evidence, quantitative
> Source

### (Bargaining power of suppliers : Medium→Medium) Key materials stay concentrated in a few firms, with alternative materials as the variable

(Bargaining power of buyers, threat of substitutes, and rivalry follow the same structure)

### Market conditions

- Market size, outlook, key indicators
> Source

### Key players

(Player table)

- Competitive landscape among the players
```

### Subheadings

- Subheadings follow the format `(Force name : Current→Outlook) Sentence title`. The sentence title briefly states the current condition and then adds the direction of change
- If the time scope is "current", use `(Force name : High/Medium/Low) Sentence title` and give only the current intensity
- Under each subheading, split (Current) and (Outlook) and write the rating summary and evidence for each. If the time scope is "current", write the rating summary and evidence without the prefixes

### Market conditions and key players

- Place market conditions and key players after the five forces. The intensity rating is the conclusion, and market data and player information are the evidence
- Write them from the basic industry information collected in Step 2
- (Market conditions) Organize market size, outlook, and key indicators per unit of analysis, with sources
- (Key players) Use the player table format in references/micro.md. Company, country, and size are required columns, and the other columns are added or dropped to fit the material. After the table, describe the competitive landscape briefly

### Analysis principles

- (Rating summary separate from evidence) Keep what the force means for industry competition (the rating summary) apart from the evidence. Write the rating summary first and support it with evidence
- (Industry-level rating) Do not extend a single company's case to the whole industry
- (No generalizing from parts) Do not present the traits of one segment as traits of the whole industry. Rate within the unit of analysis
- (Logical link) A third party must be able to follow the causal or inferential link from evidence to rating
- (Causation versus correlation) Do not treat time order as causation
- (Limits on generalization) Do not rate a whole force from a few cases
- (Structure first) Rate from structural conditions such as economies of scale, capital intensity, learning curves, patent barriers, network effects, regulatory permits, accumulated incumbent investment, supply concentration, and switching costs. Potential change factors alone do not change the intensity of an industry with solid structure. Reflect potential change factors in the outlook column, and judge them conservatively there as well
- (Vertical integration) Reflect forward and backward integration by suppliers or buyers in the corresponding bargaining power rating. Bargaining power differs by stage: planned, in progress, completed
- (Horizontal integration) Reflect mergers, acquisitions, and strategic alliances within the same industry value chain stage in the rivalry rating. Take into account fewer competitors and higher concentration
- (Consistency across forces) The five forces in one unit of analysis affect each other. If the threat of new entrants is rated high while rivalry is rated low, confirm that evidence supports both at once
- (Consistency across the industry value chain) The buyer in one unit of analysis is the supplier in the next. If buyer power in the materials market is rated "Low", rating the power of materials suppliers in the components market as "Low" too is a contradiction. After rating each unit, check the buyer and supplier links between adjacent units in reverse

### Applying the structure-first rule by force

The rows below show misjudgments. Identify and weigh structural conditions beyond these examples as well.

| Force | Evidence too weak to change the rating |
|---|---|
| Threat of new entrants | "The government supports entry" or "startups are trying to enter" alone does not raise the threat in an industry with solid economies of scale and capital barriers |
| Bargaining power of suppliers | "Alternative suppliers are appearing" or "localization is under way" alone does not lower power in a market with a confirmed supplier oligopoly |
| Bargaining power of buyers | "Buyers are considering in-house production" alone does not raise power in a structure with high switching costs and no alternatives |
| Threat of substitutes | "A technology is under research" or "substitution is possible in the long run" alone does not raise the threat of a substitute whose commercialization date is uncertain |
| Rivalry among existing competitors | "New firms are entering" alone does not raise rivalry in a market with a confirmed oligopoly of a few firms |

### Intensity rating guide

| Force | High | Medium | Low |
|---|---|---|---|
| Threat of new entrants | Low entry barriers and active entry | Barriers exist, but actual new entries are confirmed | High structural barriers such as economies of scale, capital intensity, accumulated technology, regulation |
| Bargaining power of suppliers | Few suppliers, no substitute inputs, forward integration under way | Many suppliers, but dependence on a few suppliers is confirmed for some key materials | Many suppliers, substitution of inputs is happening, no drivers of forward integration |
| Bargaining power of buyers | High buyer concentration, low switching costs, backward integration under way | Balance of power between buyers and suppliers confirmed in actual terms of trade | Dispersed buyers, high switching costs, no alternative supply |
| Threat of substitutes | Substitutes with better price-performance are commercialized and gaining share | Substitutes are commercialized, but switching costs or performance limits restrict their share | No commercialized substitutes, or excessive switching costs |
| Rivalry among existing competitors | Many competitors, low growth, little differentiation, high exit barriers | Competitors exist, but market growth allows coexistence and actual price competition is limited | Confirmed oligopoly of a few firms, high growth, horizontal integration under way |

This guide is a reference. Rate each unit of analysis from the evidence collected for it. Use only three levels of intensity: High, Medium, Low.

## Step 4 Competitive environment summary

Summarize the results for each industry value chain market in prose, then in a table. Do not merge tables across markets or create separate comparison tables.

### Output order

```
(With industry value chain breakdown)
## [Market A] competitive environment → prose → competitive environment table
## [Market B] competitive environment → prose → competitive environment table
## [Industry] competitive environment summary → prose → industry summary table

(Domestic and global separate)
## Global [market] competitive environment → prose → table
## Domestic [market] competitive environment → prose → table
## [Industry] competitive environment summary → prose → summary table

(Domestic and global separate, with industry value chain breakdown)
## Global [Market A], [Market B] ... competitive environment → prose and table for each market
## Global [industry] competitive environment summary → prose → summary table
## Domestic [Market A], [Market B] ... competitive environment → prose and table for each market
## Domestic [industry] competitive environment summary → prose → summary table
## [Industry] competitive environment summary → prose combining global and domestic → summary table
```

Each prose section describes the traits of that market's competitive structure and the interaction patterns among the forces. Place the table after the prose.

### Table format

Add a summary row after the five force rows.

| Force | Intensity (current) | Intensity (outlook) | Content | Evidence | Data |
|---|---|---|---|---|---|
| Threat of new entrants | High/Medium/Low | High/Medium/Low | - (Current) Rating summary<br>- (Outlook) Rating summary | - (Current) Evidence<br>- (Outlook) Evidence | - (Current) Quantitative data<br>- (Outlook) Quantitative data |
| Bargaining power of suppliers | High/Medium/Low | High/Medium/Low | Same format | Same format | Same format |
| Bargaining power of buyers | High/Medium/Low | High/Medium/Low | Same format | Same format | Same format |
| Threat of substitutes | High/Medium/Low | High/Medium/Low | Same format | Same format | Same format |
| Rivalry among existing competitors | High/Medium/Low | High/Medium/Low | Same format | Same format | Same format |
| **Summary** | - | - | Traits of the competitive structure across the five forces | Structural evidence for the overall judgment | - |

### Column definitions

| Column | Rule |
|---|---|
| Force | The five fixed forces plus the summary row |
| Intensity (current) | One of High, Medium, Low as of now. "-" for the summary row |
| Intensity (outlook) | One of High, Medium, Low over the time scope. "-" for the summary row. If the time scope is "current", fill the whole column with "-" |
| Content | What the force means for industry competition (rating summary). Separate (Current) and (Outlook) with `<br>`. If the time scope is "current", write without prefixes or line breaks |
| Evidence | Qualitative evidence for the intensity. (Current) gives present structural evidence, (Outlook) gives evidence of change. If "current", write without prefixes |
| Data | Quantitative evidence for the intensity, with sources. If "current", write without prefixes. If no data exists after a real search, record the best information available |

### Summary row and table writing

- The content column of the summary row combines the five ratings into a description of the competitive structure of the unit of analysis
- The evidence column of the summary row cites interactions or structural patterns among the forces
- No clear rule exists for combining the five forces into one indicator, so the intensity columns and the data column of the summary row stay "-"
- Keep each cell to 1 or 2 sentences. Detailed analysis stays in the Step 3 text
- Do not put figures without sources in the data column
- Rate the outlook differently from the current level only when evidence of a direction of change exists
- If the industry value chain was broken down, add an industry summary table after the unit tables. Do not compute the industry rating as a simple average of unit ratings. Weigh the structure of the whole industry and describe the evidence for the rating separately. The industry summary table also has a summary row

## Writing the output

Write the output at the level of an industry analysis report that can go to external readers.

- Keep an objective tone, and use the proper names of the industry and markets in titles and subheadings
- Do not describe the analysis process or explain the structure of the report
- Keep procedure terms ("unit of analysis", "rating", "basic industry information", "summary table", "force analysis structure") and thinking tool names ("MECE", "So What", "Why So") out of the text and titles
- "Competitive environment analysis", "industry structure analysis", "Five Forces", and the names of the five forces can appear in text and subheadings
- If the user asks to show specific terms, follow the request

## Check

- Units of analysis do not overlap and together cover the whole industry
- For each force, the rating summary and the evidence are separate
- A third party can follow the link from evidence to rating
- No trait of one segment is extended to the whole industry
- No force is rated from a few cases
- Potential change factors alone did not change the intensity of an industry with solid structure
- Vertical integration is reflected in bargaining power ratings, and horizontal integration in the rivalry rating
- Ratings of the forces within a unit do not contradict each other
- Buyer power and supplier power ratings of adjacent units are consistent
- Quantitative data has sources
- Only High, Medium, and Low are used for intensity
- Table cells match the text analysis
- Every table has a summary row, and its intensity columns are "-"
- With an industry value chain breakdown, each market has its own prose and table
- With an industry value chain breakdown, an industry summary table exists
- No procedure terms or process descriptions appear in the text

## Exceptions

- If the user specifies units of analysis, apply them first, and point out any overlaps or gaps between units
- If the user sets separate rating criteria, apply those criteria
- If the user asks for specific forces only, analyze only those forces
- If the user asks for text without tables, omit the tables
