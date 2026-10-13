---
name: five-forces
description: "Analyzes the competitive environment of an industry with Michael Porter's Five Forces framework. Splits the industry scope and its value chain markets with no overlaps or gaps, rates the threat of new entrants, bargaining power of suppliers, bargaining power of buyers, threat of substitutes, and industry rivalry for each market, and summarizes the results in prose and a standard competitive environment table. Use this skill whenever the user mentions 'Five Forces', '5 Forces', 'Porter analysis', 'competitive environment analysis', 'industry structure analysis', 'competitive structure analysis', or 'industry competitiveness analysis', or asks for an analysis of competition in a specific industry. Do not apply it to general writing that does not ask for a competitive environment analysis."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Five Forces Competitive Environment Analysis

> This skill is an English translation of a Korean original. The translation may cause it to behave differently from the original's intent.

Split an industry into markets and rate the strength of five competitive pressures in each market, with evidence.

## Mandatory Output Rules

Apply these rules before every other instruction. Without the per-market ratings, nobody can trace where the summary ratings came from.

- If you split the value chain, output separate prose and a separate competitive environment table for each market. Do not deliver a result that has only the summary table and skips the per-market tables.
- If the user chose the domestic and global split, output separate per-market prose and tables for global and for domestic.
- Use the same standard layout for every competitive environment table (Force, Strength (Now), Strength (Outlook), Implication, Rationale, Data). Do not invent other layouts, such as cross-market comparison tables.
- Label foreign markets "Global" in headings and tables.

## Terms

This document uses the following terms with these meanings only.

| Term | Meaning |
|------|---------|
| Force | One of the five competitive pressures on industry profitability: threat of new entrants, bargaining power of suppliers, bargaining power of buyers, threat of substitutes, industry rivalry |
| Strength | How hard one Force squeezes the profits of firms in the industry, rated High, Medium, or Low. High means heavy pressure |
| Value chain | The industry stages that run from production to final use. Porter's firm value chain, which splits a single firm's internal activities, is a different concept |
| Market | One stage of the value chain after the split. It is the base unit of analysis and rating, and this skill calls it the unit of analysis internally |
| Domestic | The home country the user names. If the user does not name one, ask |
| Structural evidence | Industry conditions that are hard to change in the short run: economies of scale, capital intensity, learning curves, patents, network effects, regulation and licensing, incumbents' accumulated investment, supplier concentration, switching costs, and similar |
| Potential change factor | A move that has not yet changed industry conditions: an announced government subsidy, an entry attempt by a new firm, a localization push, research on a substitute technology, a firm considering integration, and similar |

## Modes

- (Auto mode) If the user gives only an industry name, the skill proposes and performs every step from scope setting to the summary.
- (Guided mode) If the user sets the scope or the units of analysis in advance, apply those values first.

Use the user's attached material as the first source of evidence and fill gaps with web search. If the environment has no web search tool, ask the user to attach material. Do not build an industry definition, a value chain, or figures from model memory alone. Do not use any figure without a source. Cite sources as "Organization or author (year), Title (link)".

## Step 1. Set the Scope

Fix the boundary of the industry. For any item the user has not set, propose a value and get the user's confirmation.

| Item | What to decide | Example |
|------|---------------|---------|
| Industry name | The industry under analysis | Hydrogen energy industry |
| Industry definition | What is included and excluded. Decide whether each adjacent industry is part of the analysis or a substitute | Includes hydrogen production, storage and distribution, and end use. Treats other energy sources such as solar as substitutes |
| Geographic scope | Pick one: domestic only, foreign only, domestic and global combined, domestic and global split | Domestic and global combined |
| Time horizon | The reference point for Strength (Outlook). Pick one of the options below | Mid to long term |
| Value chain split | The stage breakdown used in the industry | Production, storage and distribution, end use |
| Unit structure | Pick one: per-market analysis, whole-industry analysis, or a mix of both | Per-market analysis followed by a whole-industry summary |

Time horizon options are listed below. If the user does not choose, use mid to long term.

- Now: produce no outlook.
- Mid term within 3 years, mid to long term within 5 years, long term within 10 years, very long term within 30 years (for long-horizon investment review), or a user-defined period: produce the outlook as of that point.
- No limit: do not fix a reference point. For each Force, state the outlook point that the evidence gives.

Scope rules:

- Split the value chain markets so they do not overlap and so that all markets together make up the whole industry.
- Name each market with the term the industry uses. Use generic names such as "materials", "components", "equipment", or "infrastructure" only when the industry uses them widely.
- If the value chain does not need splitting or the user wants a whole-industry analysis, treat the whole industry as one market.
- Pick one of four geographic options.

| Option | Handling |
|--------|---------|
| Domestic only | Analyze only the domestic industry |
| Foreign only | Analyze only the foreign industry |
| Domestic and global combined | Split markets by value chain and describe domestic and foreign trends together inside each market |
| Domestic and global split | For each market, do the global analysis first and a separate domestic analysis after it. The same market can have a different competitive structure in each region, so produce separate strengths and tables |

If the user has not set the scope, proceed in this order.

1. If material is attached, extract the industry definition and value chain from it. Otherwise, find them with web search.
2. Draft the units of analysis from that value chain.
3. Ask the user for the geographic scope. If there is no answer, use domestic and global combined.
4. Confirm the industry definition, value chain split, and geographic scope with the user, then fix the scope.

## Step 2. Collect Evidence

For each market, collect basic industry data first, then the factors for each Force.

| Basic industry data | What to collect |
|--------------------|-----------------|
| Market size | Market size in monetary terms. For the domestic and global split, collect both |
| Market outlook | Growth outlook such as the compound annual growth rate. The outlook period and source are required |
| Key indicators | Indicators used in the industry, such as revenue, employees, number of firms, and location quotient |
| Key firms | Market share, size such as revenue or headcount, business structure and main products, main customers, main competitors |

> (Location quotient) The ratio of a region's employment share in an industry to the same share in a reference area. A value above 1 means the industry is concentrated in that region.

Collect the Force factors with the table below. A confirmed condition in the table is evidence that raises strength. A confirmed opposite condition is evidence that lowers strength.

| Force | Conditions that raise strength |
|-------|-------------------------------|
| Threat of new entrants | Supply-side economies of scale are small. Network effects, where value grows with the number of users, are weak. Capital requirements are low. Technical difficulty, regulation, and licensing barriers are low. Customer switching costs are low. Access to distribution channels is easy. Incumbents' advantages in patents, cost, and location are small. Retaliation by incumbents is unlikely (no history of retaliation, no spare capacity or cash, no slow growth). The government supports entry. New entries keep occurring |
| Bargaining power of suppliers | Suppliers are few and more concentrated than the buying industry. This industry is a small share of supplier revenue. Changing suppliers is costly. Supplied items are differentiated. No substitute material exists for the supplied items. Suppliers have completed or are carrying out forward integration |
| Bargaining power of buyers | Buyers are few or buy large volumes. Products are standardized and barely differentiated. Buyer switching costs are low. Buyers have completed or are carrying out backward integration. Buyers are price sensitive (the product is a large share of their purchasing cost, their profitability is low, the product has little effect on the quality of their own product) |
| Threat of substitutes | A substitute with better price-performance is commercially available. Switching to the substitute is cheap. The substitute market is growing. The range of adjacent products that deliver the same function is wide |
| Industry rivalry | Competitors are many or similar in size. Market growth is low. Fixed costs are a large share of costs. Product differentiation and switching costs are small. Capacity is added in large increments, so oversupply occurs easily. Exit barriers are high |

- Do not treat government policy, complements, market growth, or technology change as a sixth Force. Reflect them through the matching conditions in the table above.
- Horizontal integration such as mergers, acquisitions, and strategic alliances changes the number and size distribution of competitors. Reflect it in the "number and size of competitors" condition under industry rivalry.
- Organize the collected data by market as the input to Step 3, and give a separate source for each figure.

## Step 3. Five Forces Analysis per Market

For each market, rate and describe the five Forces in order, then summarize the market status and key firms. The strength rating is the conclusion. Market data and firm status are the evidence behind it.

### How to Rate Strength

For each Force, check each condition in the Step 2 table and sort the conditions that have evidence into raising factors and lowering factors. Then rate strength with the criteria below.

| Strength | Criteria |
|----------|---------|
| High | A raising factor is confirmed by structural evidence, and no structural lowering factor offsets it |
| Low | A lowering factor is confirmed by structural evidence, and no structural raising factor offsets it |
| Medium | Structural raising and lowering factors are both confirmed, or the evidence does not lean either way |

The table below lists condition combinations that often appear at each strength. Rate each market individually on the evidence collected for it.

| Force | High | Medium | Low |
|-------|------|--------|-----|
| Threat of new entrants | Entry barriers are low and new entry is active | Entry barriers exist, but actual new entries are confirmed | Structural barriers such as economies of scale, capital intensity, accumulated technology, and regulation are high |
| Bargaining power of suppliers | Suppliers are few, no substitute material exists, and forward integration is underway | Suppliers are many, but dependence on a few suppliers is confirmed for some key items | Suppliers are many, material substitution is happening, and there is no driver for forward integration |
| Bargaining power of buyers | Buyer concentration is high, switching costs are low, and backward integration is underway | Actual trading terms show a balance of power between buyers and suppliers | Buyers are dispersed, switching costs are high, and no alternative supply source exists |
| Threat of substitutes | A substitute with better price-performance is commercially available and gaining share | A substitute is commercially available, but switching costs or performance limits hold back its share | No commercial substitute exists, or switching costs are excessive |
| Industry rivalry | Competitors are many, growth is low, differentiation is weak, and exit barriers are high | Competitors exist, but market growth lets them coexist and actual price competition is limited | An oligopoly of a few firms is confirmed, firm sizes differ widely, market growth is high, and horizontal integration is underway |

Firms of similar size in an oligopoly tend to fight for share because no leader sets the pace. For that reason, the Low condition for industry rivalry also checks the size gap between firms.

### Rating Rules

- Set the current strength on structural evidence. Do not change the current strength of a structurally solid industry on potential change factors alone.
- To set an outlook strength that differs from the current one, you need evidence that the change will happen within the time horizon (capital spending under way, a commercialization schedule, a signed contract, a law's effective date, and similar). Record factors without such evidence in the outlook text only and keep the strength unchanged.
- Reflect vertical integration by stage. If it is complete, or underway with capital being spent, reflect it in the current strength. If it is only announced as a plan, record it in the outlook text.
- Do not extend a single firm's case or one segment's traits to the whole industry. Rate within the market's scope.
- Do not rate a whole Force on a handful of cases. Do not treat a sequence in time as cause and effect.
- A third party must be able to follow the link from evidence to rating.

The table below shows typical cases where potential change factors get too much weight. Outside these cases, apply the same principle and check structural evidence first.

| Force | Evidence that does not change strength | Structural evidence |
|-------|---------------------------------------|---------------------|
| Threat of new entrants | The government supports entry, startups are trying to enter | Economies of scale and capital barriers are solid |
| Bargaining power of suppliers | Alternative suppliers are appearing, a localization push is underway | An oligopoly of a few suppliers is confirmed |
| Bargaining power of buyers | Buyers are considering in-house production | Switching costs are high and no alternative exists |
| Threat of substitutes | A technology is under research, substitution may happen in the long run | The commercialization date is uncertain |
| Industry rivalry | New firms are entering | An oligopoly of a few firms is confirmed |

### Consistency Checks

- (Across Forces) The five Forces in one market affect each other. Check that their ratings do not contradict each other. For example, if the threat of new entrants is High while industry rivalry is Low, check for evidence that lets both ratings hold together.
- (Across markets) In two adjacent markets, the buyers of the upstream market are the firms of the downstream market, and the suppliers of the downstream market are the firms of the upstream market. If the downstream market is a main buyer of the upstream market, buyer power in the upstream market and supplier power in the downstream market must point in opposite directions. Low buyer power upstream together with Low supplier power downstream is a contradiction. If the downstream market accounts for only part of upstream revenue, the two ratings may not point in opposite directions, so state that revenue share in the rationale.
- After finishing the per-market ratings, recheck the buyer and supplier links between adjacent markets from the opposite direction.

### Writing Format

Write each Force subheading as `(Force name : current strength→outlook strength) sentence-style title`. The sentence-style title names the current state briefly and adds the direction of change after it. If the time horizon is Now, write `(Force name : High/Medium/Low) sentence-style title`, and in the body write the implication and rationale directly without the (Now) and (Outlook) prefixes.

In each Force body, write the implication first and attach the rationale below it. The implication is what this Force means for competition in the industry. The rationale is the reason for the rating. Do not mix the two in one sentence.

```
## Hydrogen Production Market

### (Threat of new entrants : Medium→High) Technical barriers remain, but falling production costs open room for new entrants

- (Now) Implication
    + Structural rationale, qualitative
    + Structural rationale, backed by figures
- (Outlook) Implication
    + Structural rationale, qualitative
    + Structural rationale, backed by figures
> Source

### (Bargaining power of suppliers : Medium→Medium) A few firms still control key materials, and alternative materials are the variable to watch

(Same structure for bargaining power of buyers, threat of substitutes, and industry rivalry)

### Market Status

- Describe market size, market outlook, and key indicators
> Source

### Key Firms

| Firm | Country | Market share | Size | Business structure and main products | Main customers | Notes |
|------|---------|-------------|------|-------------------------------------|---------------|-------|
| Firm A | United States | 20% | Revenue $00M | ... | ... | ... |

- Describe the competitive landscape among firms briefly
```

- You may drop or add columns in the key firms table to fit the data collected. Keep the firm, country, and size columns.
- If the user chose the domestic and global split, write a global section and a domestic section for the same market. Order the sections as in Step 4.

## Step 4. Competitive Environment Summary

Summarize the per-market results in prose for each market, and place the standard competitive environment table right after the prose. The prose describes the traits of the market's competitive structure and the pattern that interactions between Forces create.

### Document Order

Place the whole Step 3 body first and the Step 4 summary after it. Order the Step 4 sections as follows.

1. Place the per-market competitive environment sections in value chain order. Title each "OO Market Competitive Environment".
2. If the user chose the domestic and global split, place all global market sections first and all domestic market sections after them.
3. If the user chose both the domestic and global split and the value chain split, place "Global OO Industry Competitive Environment Summary" after the global market sections and "Domestic OO Industry Competitive Environment Summary" after the domestic market sections.
4. If you split the value chain or chose the domestic and global split, place "OO Industry Competitive Environment Summary" at the very end. If you analyzed a single market, omit this section.

The order for the case with both the domestic and global split and the value chain split looks like this.

```
## Global Hydrogen Production Market Competitive Environment
## Global Hydrogen Storage and Distribution Market Competitive Environment
## Global Hydrogen End-Use Market Competitive Environment
## Global Hydrogen Energy Industry Competitive Environment Summary
## Domestic Hydrogen Production Market Competitive Environment
## Domestic Hydrogen Storage and Distribution Market Competitive Environment
## Domestic Hydrogen End-Use Market Competitive Environment
## Domestic Hydrogen Energy Industry Competitive Environment Summary
## Hydrogen Energy Industry Competitive Environment Summary
```

Each section places the prose first and the standard competitive environment table after it.

### Standard Competitive Environment Table

Add a summary row after the five Force rows.

| Force | Strength (Now) | Strength (Outlook) | Implication | Rationale | Data |
|-------|---------------|-------------------|-------------|-----------|------|
| Threat of new entrants | High/Medium/Low | High/Medium/Low | - (Now) Implication<br>- (Outlook) Implication | - (Now) Rationale<br>- (Outlook) Rationale | - (Now) Figures<br>- (Outlook) Figures |
| Bargaining power of suppliers | High/Medium/Low | High/Medium/Low | (Same layout) | (Same layout) | (Same layout) |
| Bargaining power of buyers | High/Medium/Low | High/Medium/Low | (Same layout) | (Same layout) | (Same layout) |
| Threat of substitutes | High/Medium/Low | High/Medium/Low | (Same layout) | (Same layout) | (Same layout) |
| Industry rivalry | High/Medium/Low | High/Medium/Low | (Same layout) | (Same layout) | (Same layout) |
| Summary | - | - | Traits of the competitive structure across the five Forces | Interactions between Forces and structural patterns | - |

| Column | Rule |
|--------|------|
| Force | Fixed to the five Forces plus the summary row |
| Strength (Now) | Strength at the present time. One of High, Medium, Low |
| Strength (Outlook) | Strength at the time horizon. One of High, Medium, Low. If the time horizon is Now, fill the whole column with "-" to keep the layout |
| Implication | What this Force means for competition in the industry. Separate (Now) and (Outlook) with `<br>` |
| Rationale | Qualitative evidence for the strength. (Now) gives the structural evidence for the current strength, (Outlook) gives the evidence for the change |
| Data | Quantitative evidence for the strength, with sources |

- If the time horizon is Now, write the Implication, Rationale, and Data cells directly without the (Now) and (Outlook) prefixes or line breaks.
- Put "-" in both strength cells and the data cell of the summary row. No rule exists for merging five Forces into one strength.
- Keep each cell to one or two sentences and leave the detailed analysis in the Step 3 body. Every cell must match the body analysis.
- Do not put figures without sources in the Data column. If no direct indicator exists, use a sourced proxy indicator and say that it is a proxy. If no proxy exists either, write "No data found".

### Whole-Industry Summary Table

If you split the value chain, add a whole-industry summary table after the per-market tables. It uses the same layout as the standard table, including the summary row.

- Do not set whole-industry strength as a simple average of the per-market strengths. Give priority to the ratings of markets with a large share of industry profits (check with market size share or similar measures).
- If strengths differ across markets, state the difference and the reason for your weighting in the Rationale cell.

## Output Writing Standard

Write the output in an objective, report-style voice. Use the real names of the industry and markets in headings and subheadings, and let the content show the structure on its own.

Keep the following out of the output.

| Type | Examples |
|------|---------|
| Exposing the skill | "Following this skill's workflow", "We performed a four-step analysis" |
| Self-justification | "We analyzed every Force without omission", "We split the markets with no overlaps or gaps" |
| Exposing internal terms | "unit of analysis", "rating" used as a process term |
| Exposing internal section names | Using "summary table", "Force analysis structure", or "basic industry data" as headings |
| Describing the analysis process | "First we analyze the threat of new entrants, and next we examine the bargaining power of suppliers" |

General framework names such as "competitive environment analysis", "industry structure analysis", and "Five Forces", and the names of the five Forces, may appear in subheadings. If the user asks to show a specific term, follow the request.

## Pre-Output Checklist

- Do the markets avoid overlap and add up to the whole industry?
- Is the implication separate from the rationale in each Force?
- Can a third party follow the link from evidence to rating?
- Did you avoid extending one segment or a handful of cases to the whole industry?
- Did you avoid changing a current strength on potential change factors alone?
- Does every changed outlook strength have evidence of realization within the time horizon?
- Is vertical integration reflected in supplier and buyer power, and horizontal integration in industry rivalry?
- Do the five Force ratings in one market avoid contradicting each other?
- Do buyer power and supplier power ratings avoid contradiction between adjacent markets?
- Are only three strengths used: High, Medium, Low?
- Does every figure have a source?
- Does every table cell match the body analysis?
- Does every table have a summary row, with "-" in its strength cells?
- If you split the value chain, does each market have its own prose and table, and is there a whole-industry summary table?
- Is the output free of internal terms and descriptions of the analysis process?

## Exceptions

- If the user sets the units of analysis in advance, apply them. If you find overlaps or gaps between markets, tell the user.
- If the user sets separate rating criteria, apply those criteria.
- If the user asks for specific Forces only, analyze only those Forces.
- If the user asks for body analysis without tables, omit the tables.
