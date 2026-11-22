> This English edition is a translation of the Korean original. Some rules were adapted to English writing conventions, and the skill may behave differently from the intent of the original.

# Micro Environment Analysis

The micro environment module covers the markets and industries the subject interacts with through transactions, competition, or cooperation. It records as facts the size and direction of the topic's market, the stage structure of the industry, the competitive landscape, demand, and the flow of money. As in the macro environment module, it contains no interpretation and no prescriptions. Competitive intensity ratings follow the procedure in references/five-forces.md and carry their evidence.

## Categories

| Category | Content |
|---|---|
| Market | Size, growth rate, outlook, segments, shares by region |
| Industry value chain | Market stages from upstream to downstream and the main participants at each stage |
| Competition | Key players, market concentration, Five Forces competitive structure |
| Customers and demand | Customer groups, purchase criteria, material that shows demand |
| Investment | Public R&D investment, public non-R&D investment, private R&D investment, private non-R&D investment |

Run only the requested categories. Classification schemes vary with the topic (Five Forces, market and industry, industry value chain, customers and competitors, and so on), so the order of categories is not fixed.

## Link to the macro environment

If the macro environment module also ran, note in which micro category each macro change shows up. For example, record the effective date of a regulation next to the change in the related market figures. Write cause and effect only when a source states the causal relationship. Otherwise record the time order only. Treating an earlier event as the cause without evidence is an unsupported causal claim.

## Industry value chain

- Use the stage names the industry itself uses. Generic names such as "materials, components, equipment, infrastructure" appear only when the industry uses them widely
- Divide stages so they do not overlap and together cover the whole industry
- List stages from upstream to downstream
- Confirm the stage breakdown from provided material or web sources. Do not build an industry value chain from model knowledge alone

| Stage | Main products or services | Main participants | Source |
|---|---|---|---|

## Market size and outlook

- Attach to each figure the publisher, publication year, reference year, unit and currency, estimation method, and outlook period
- Secure a time series of 3 to 5 years or more, compute the compound annual growth rate and shares in code, and report them together. Formulas are in references/sources.md
- Do not splice estimates from different publishers into one time series. Each publisher defines the market differently, so a spliced series does not show real change. When several estimates exist, present them side by side with their definitions
- If the geography includes both global and domestic, organize each separately
- Use the market indicators common in the industry, such as revenue, employment, number of establishments, and location quotient

## Key players

Organize the main companies in the whole market in the table below. For a region subject, companies located in the region belong to the regional industry conditions in references/internal.md.

| Company | Country or location | Size | Market share | Business areas and main products | Main customers | Competitive relations | Recent developments |
|---|---|---|---|---|---|---|---|

- Company, country or location, and size are required columns. Add or drop the other columns to fit the material confirmed
- Report size as revenue or headcount, with the reference year
- Report market share only when a source exists
- In the competitive relations column, write the industries or main rivals the company competes with
- After the table, describe the competitive landscape among the players in a few fact-based sentences

## Competitive structure

- Five Forces analysis follows the procedure in references/five-forces.md
- With share data, concentration can be computed as the combined share of the top firms (CR) and the Herfindahl-Hirschman Index (HHI). Formulas are in references/sources.md

## Customers and demand

- Divide customers into groups and confirm each group's purchase criteria and size from material
- Use public procurement records, published demand surveys, and purchase statistics as evidence of demand
- Do not write demand that material does not confirm

## Investment trends

Investment trends fall into four categories by funding source and by whether the money counts as R&D. Government programs belong here whether or not their budget is classified as R&D. Strategies and plans that set a direction belong to the policy category in references/macro.md.

| Category | Content | Main sources |
|---|---|---|
| Public R&D investment | Programs and projects the government funds from its R&D budget | Budget documents, R&D program implementation plans, national R&D databases |
| Public non-R&D investment | Demonstration, infrastructure, commercialization and business support, and workforce development programs the government funds outside its R&D budget, plus loans, guarantees, and equity contributions to funds | Budget documents, calls for proposals, public finance disclosure systems |
| Private R&D investment | R&D spending that firms fund themselves | R&D activity surveys, industry surveys, corporate disclosures |
| Private non-R&D investment | Capital expenditure, equity investment by venture capital, private equity, and corporate venture capital, mergers and acquisitions | Industry surveys, corporate disclosures, association and government statistics, paid investment databases |

- (Funding source) Money from the budgets or funds of central and local governments is public, and money from firms and private investors is private. When one program draws on both, record the amount from each source separately and enter the program once, in the category of the side that budgeted it
- (R&D or not) Follow the official classification in the source. For public money, follow the budget documents and government R&D budget statistics. For private money, follow R&D activity surveys and corporate disclosures. Programs that mix activities, such as demonstration, infrastructure, and workforce development, get different verdicts from different analysts when judged by name or content. Record a program whose classification is not confirmed as classification unconfirmed
- (Nature of the amount) Record the nature of each amount: plan, budget, execution, or cumulative funding raised. Do not add amounts of different nature together or join them into one trend. A government's announced investment plan and actual spending differ in size and timing
- (Repayable money) Loans, guarantees, and equity contributions are meant to be recovered, so do not add them to grants and subsidies
- (Double counting) Do not add amounts that count the same money again at a later step. This covers a government's contribution to a fund and that fund's investments, and an equity investment and the R&D spending of the firm that received it
- (Shares) If one source presents public and private investment under the same definition, compute the trend of the private share in code. Do not pair a public amount from one source with a private amount from another to build a share
- (Sub-units) If the topic has sub-technologies or industry value chain stages and the data splits along those units, repeat the same format for each unit
- (Region subject) Projects carried out by organizations in the region and R&D spending of firms in the region are resources the subject holds, so they belong to the region subject items in references/internal.md
- (Data channel) Search engines miss much of this material, so check first the connected-system channel or the user-provided channel in references/sources.md

### Public investment

Organize program budgets of ministries and funding agencies by year. Public R&D investment and public non-R&D investment share one format, separated by the budget class column.

| Ministry or agency | Program name | Budget class | Program type | Budget by year | Source |
|---|---|---|---|---|---|

- The budget class column carries one of R&D, non-R&D, or classification unconfirmed
- Program types follow the activity: technology development, demonstration, commercialization, workforce development, and infrastructure
- Budget class and program type are separate bases. An infrastructure program in the R&D budget and a technology development program in the non-R&D budget can both occur
- For loan, guarantee, and equity programs, record the form of support with the program name

When using project counts and research funds drawn from a national R&D database, follow the rules below. Set the search conditions and the breakdown together with the user by the database exploration procedure in references/sources.md.

- Record the search conditions and query date in the citation
- Report the number of projects used as the denominator with any share or ranking
- The database holds projects funded from the government R&D budget. Confirm non-R&D programs from budget documents and calls for proposals, and confirm R&D that firms carry out with their own money alone from private investment sources. Do not treat the absence of projects as evidence of no investment

### Private investment

Organize corporate R&D spending and capital expenditure by year, at industry or regional level. R&D spending is private R&D investment, and capital expenditure is private non-R&D investment. Add averages per firm or output indicators such as patents when the data has them.

| Year | Industry or region | R&D spending | Capital expenditure | Source |
|---|---|---|---|---|

Organize equity investment and mergers and acquisitions by number and amount for each period. Add investment stages, main investors, and focus areas when the data has them.

| Period | Country or field | Investment type | Number of deals | Amount | Source |
|---|---|---|---|---|---|

- Investment types are venture capital, private equity, corporate venture capital, and mergers and acquisitions
- Terms of paid databases often restrict redistribution, so use exports provided by the user or connected systems, and cite within the terms

## Writing principles

- Describe objective conditions and trends only. Record a source's outlook with who made it, the publication year, and the outlook period
- Do not extend a single company's case to the whole industry
- Do not present the traits of one segment as traits of the whole market
- Record each fact in the fact register with a MIC- ID

## Check

- Industry value chain stages use the industry's own names and cover the whole industry without overlap
- Each market figure has a publisher, reference year, unit, and estimation method
- No estimates from different publishers are spliced into one series
- Compound annual growth rates and shares were computed in code
- The player table has the required columns
- Every row of the investment tables is a program or investment with a funding source and an amount
- Each public program carries a budget class taken from the official classification
- Each investment amount states whether it is a plan, budget, execution, or cumulative amount raised
- Repayable money and double-counted amounts are not added together
- Figures drawn from a national R&D database state the search conditions and the denominator
- No causal claim goes beyond what sources state
- No interpretation or prescription is mixed in
