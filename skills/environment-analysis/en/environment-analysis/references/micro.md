> This English edition is a translation of the Korean original. Some rules were adapted to English writing conventions, and the skill may behave differently from the intent of the original.

# Micro Environment Analysis

The micro environment module covers the markets and industries the subject interacts with through transactions, competition, or cooperation. It records as facts the size and direction of the topic's market, the stage structure of the industry, the competitive landscape, demand, and the flow of money. As in the macro environment module, it contains no interpretation and no prescriptions. Competitive intensity ratings follow the procedure in references/five-forces.md and carry their evidence.

## Categories

| Category | Question it answers | Content |
|---|---|---|
| Market | How much is sold and how fast does it grow | Size, growth rate, outlook, segments, shares by region, and so on |
| Industry value chain | Through which stages and by whom is it supplied | Market stages from upstream to downstream and the main participants at each stage |
| Competition | Who competes and in what structure | Key players, market concentration, Five Forces competitive structure, and so on |
| Customers and demand | Who buys and by what criteria | Customer groups, purchase criteria, material that shows demand, and so on |
| Investment | Who puts how much money where | Public investment, corporate investment, risk capital investment |

Place each fact in the one category whose question it answers. For facts that are easy to misplace at a boundary, follow the placement rules in SKILL.md. Run only the requested categories. Classification schemes vary with the topic (Five Forces, market and industry, industry value chain, customers and competitors, and so on), so the order of categories is not fixed.

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

The investment category covers the flow of funds into the topic field. The governments, firms, and investors that provide funds are parties the subject interacts with by applying, raising funds, competing, and so on, so they belong to the micro environment. Investment divides by source of funds and by use.

| Source of funds | R&D | Other than R&D |
|---|---|---|
| Public | Government R&D budgets, R&D programs and projects, and so on | Demonstration, infrastructure such as facilities and equipment, business support such as commercialization and workforce development, subsidies and policy finance, publicly funded investment funds, and so on |
| Private | R&D spending that firms fund themselves, and so on | Corporate facility investment, equity investment by risk capital such as venture capital and private equity, mergers and acquisitions, and so on |

- (Budget classification) Confirm whether a public investment is R&D from the budget classification stated in budget documents, program announcements, or statistics. Each country's budget classification sets it, and it does not always match the program name or the program content. A program on the R&D budget can include infrastructure or workforce development, and a program outside the R&D budget can support technology development. When the classification cannot be confirmed, record it as unconfirmed
- (Mixed funding) Place programs and funds that combine public and private money under the source of the operating body, and record the funding mix
- Record the nature of each amount: plan, budget, execution, or cumulative funding raised. Do not add amounts of different nature together or join them into one trend. A program's planned amount and actual spending differ in size and timing
- If one source presents public and private investment under the same definition, compute the trend of the private share in code. Do not pair a public amount from one source with a private amount from another to build a share
- If the topic has sub-technologies or industry value chain stages and the data splits along those units, repeat the same format for each unit
- For a region subject, projects carried out by organizations in the region and R&D spending of firms in the region are resources the subject holds, so they belong to the region subject items in references/internal.md
- Organize first what public literature confirms, such as budget documents, program announcements, implementation plans, statistical reports, and investment analyses published by agencies. Add queries of project-level databases or paid investment databases by the procedure in references/sources.md when a data channel exists

### Public investment

Organize program budgets of ministries and funding agencies by year. Budget classification and program type follow different criteria, so record them in separate columns.

| Ministry or agency | Program name | Budget classification | Program type | Program period | Budget by year | Source |
|---|---|---|---|---|---|---|

- Record the budget classification as R&D, other than R&D, or unconfirmed
- Record the program type by program content, such as technology development, demonstration, infrastructure, commercialization support, workforce development, financial support, and so on

When using project counts and research funds drawn from a national R&D database, follow the rules below. Set the search conditions and the breakdown together with the user by the database exploration procedure in references/sources.md.

- Record the search conditions and query date in the citation
- Report the number of projects used as the denominator with any share or ranking
- The database holds projects with government funding, so R&D that firms carry out with their own money alone does not appear. Do not treat the absence of projects as evidence of no investment

### Corporate investment

Organize corporate R&D spending and facility investment by year, at industry or regional level. Add averages per firm or output indicators such as patents when the data has them.

| Year | Industry or region | R&D spending | Facility investment | Source |
|---|---|---|---|---|

### Risk capital investment

- Organize the number and amount of deals by venture capital, private equity, corporate venture capital, and so on by period. Add investment stages, main investors, and focus areas when the data has them
- Terms of paid databases often restrict redistribution, so use exports provided by the user or connected systems, and cite within the terms

| Period | Country or field | Number of deals | Amount invested | Source |
|---|---|---|---|---|

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
- Each investment amount states whether it is a plan, budget, execution, or cumulative amount raised
- Each public investment records budget classification and program type separately, and the budget classification is confirmed from the source
- Figures drawn from a national R&D database state the search conditions and the denominator
- No causal claim goes beyond what sources state
- No interpretation or prescription is mixed in
