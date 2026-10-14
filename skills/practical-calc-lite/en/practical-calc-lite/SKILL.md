---
name: practical-calc-lite
description: Computes the figures used in planning, policy research, and consulting reports with Python scripts, covering CAGR and real-price conversion, cost-benefit analysis (NPV, B/C, IRR, payback, sensitivity, Korean preliminary feasibility study benefit method), input-output ripple effects, location quotient (LQ) and shift-share analysis, market concentration (HHI), financial statement analysis (EBITDA, CAPEX, OPEX, FCF, ratios), break-even point (BEP), budget-versus-actual variance analysis, AHP weights and consistency ratio, and TAM-SAM-SOM market sizing. Includes a parser that converts PDF, HWP, HWPX, DOCX, PPTX, and XLSX files to Markdown to extract inputs. Use this skill whenever the user asks to calculate or re-check growth, feasibility, benefit-cost ratios, ripple effects, specialization, concentration, financial ratios, break-even, budget variances, weights, or market size, or when a report needs numbers produced or verified.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# practical-calc-lite

> This English edition was translated from the Korean original. It may behave differently from what the original intends.

Numbers in plans and reports are trustworthy only when someone else can rerun the same inputs and get the same values. This skill fixes common calculations as Python scripts in the `scripts/` folder and writes down the formulas, input rules, and decision criteria next to them. The scripts calculate. The model prepares inputs and explains results.

## Working principles

- Take every number in the report from script output. Figures the model computes in its head or estimates can be wrong without anyone noticing, so do not use them.
- Take inputs only from the user's material or from sources you have confirmed. When a value that moves the result a lot is missing, such as an inducement coefficient, a contribution rate, or a market share, ask the user instead of filling it in.
- When the inputs are complete, calculate right away. When items are missing, ask for all of them in one message.
- Before calculating, settle the unit (KRW, KRW million, KRW 100 million, persons), the base year, and the price basis (current or constant prices). If amounts from different years must be added, first convert them to base-year prices with the growth tool.
- Turn user material into script input with code, following the data preparation steps. Show extracted or prepared figures in a table and get the user's confirmation before calculating. Errors in extraction and preparation spread into every later result.
- When reporting results, include the input JSON. The same JSON in the same script gives the same result, so a third party can check it.

## Setup

Requires Python 3.9 or later. Install the packages once.

```bash
pip install "markitdown[pdf,docx,pptx,xlsx,xls]" python-hwpx olefile pandas openpyxl matplotlib
```

Every calculator runs the same way.

```bash
python scripts/<tool>.py --example > input.json      # get an input template
python scripts/<tool>.py input.json                  # calculate, print a Markdown report
python scripts/<tool>.py input.json --json out.json  # also save results as JSON
python scripts/<tool>.py input.json --xlsx out.xlsx  # also save report tables as Excel sheets
python scripts/<tool>.py input.json --csv out_csv    # also save report tables as CSV files
```

The `--example` output defines the field names and structure of the input JSON. When an input is invalid, the script prints the cause after `[INPUT ERROR]`.

`--xlsx` writes one sheet per report table with numbers stored as numeric cells, and appends the input JSON used in a final `input` sheet. `--csv` writes one CSV file per table, encoded as UTF-8 with BOM so spreadsheet programs read Korean text correctly. The two options can be combined.

| Purpose | Script |
| --- | --- |
| Convert documents to Markdown | parse_input.py |
| Growth rates, real-price conversion, trend projection | growth.py |
| Cost-benefit analysis | feasibility.py |
| Economic ripple effects | io_impact.py |
| Location quotient, shift-share analysis | regional.py |
| Market concentration | concentration.py |
| Financial statement analysis | financials.py |
| Break-even point | bep.py |
| Budget-versus-actual variance analysis | variance.py |
| AHP weights | ahp.py |
| Market sizing | market_size.py |

## Document conversion

Run `python scripts/parse_input.py input_file output.md`. For long documents, add `--chunk --chunk-size 2000` to write heading-based pieces into a folder.

| Format | Method |
| --- | --- |
| PDF | markitdown extracts the text and pdfplumber finds tables, saved separately as `sourcename_tables.md`. No table file is written when there are no tables. |
| HWPX | python-hwpx Markdown export first; if that fails, its text extractor; then the text read directly from the document XML. |
| HWP | The HWP 5.0 reader built into the script reads body paragraphs. Text inside tables comes out as ordinary paragraphs. |
| DOCX, PPTX, XLSX, XLS, CSV, JSON, XML, HTML, TXT, MD, EPUB, ZIP | markitdown. |

- Only local files are accepted. URLs are refused.
- Scanned image PDFs yield no text. Tell the user OCR is needed first.
- Password-protected HWP and distribution-locked HWP files cannot be read. Ask the user to save them as HWPX or PDF in Hancom Office.
- If the row and column structure of HWP tables is needed, ask for an HWPX copy. HWPX conversion keeps tables as Markdown tables.
- Save DOC and PPT (legacy formats) as DOCX and PPTX before converting.
- Image and audio files are not supported. Audio transcription sends the file to an external service, and images yield only metadata such as the shooting location.

HWP reader notice: 본 제품은 한컴의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다. (This product was developed with reference to the HWP document file (.hwp) specification published by Hancom.)

## Data preparation

User material arrives in many shapes: spreadsheets, files downloaded from statistics portals, report tables, numbers pasted into the chat. Before calculating, turn it into the form each script reads. Prepare tabular material with pandas code instead of copying values by hand. Hand copying slips digits and rows; code rebuilds the same input from the same source. When the user types only a few values in the chat, write the JSON directly and show it.

Follow these steps.

1. Inspect the source layout: which row holds the header, where the unit is written (table title, column name, footnote), whether years run across columns or down rows, whether total and subtotal rows exist, and whether there are several sheets.
2. Check the target form with `--example` and map the source columns and rows to input fields.
3. Write and run the preparation code, and save it next to the input JSON as a file such as `prepare_<tool>.py`. Read Markdown tables produced by parse_input.py the same way.
4. Show the prepared result as a table. If the source has totals, also show the check of the prepared values against them, and get the user's confirmation.
5. Run the calculator once confirmed.

Preparation rules:

- The calculators read thousands separators, surrounding spaces, full-width digits, parenthesized negatives "(100)", the Korean negative mark "△100", and percentages "4.5%" (read as 0.045). Values with unit words such as "억원" and the marks "▲" and "▼" mean different things in different sources, so the scripts refuse them; convert them to plain numbers during preparation.
- Express every amount in the single unit written in the input JSON's `unit`. "1조 2,000억원" is 12,000 × KRW 100 million. Write conversion factors as named constants in the code.
- Enter ratios such as discount rates, shares, contribution rates, and adoption rates as decimals (4.5% is 0.045). `basis: "share"` in concentration.py accepts both percentages summing to 100 and decimals summing to 1, and prints which it used.
- Turn wide tables with years across columns into long form (one row per year, item, and value) before moving them into the tool's form.
- Convert "2024년", "'24", "2024p", and "2024E" to integer years and keep the provisional (p) and estimate (E) marks in the report's input table. State it when the fiscal year does not start in January.
- Keep total and subtotal rows out of the calculation and set them aside for checks. regional.py, which does use national and total rows, receives their names through `national_label` and `total_label`.
- Do not fill "-", "…", "X", "N/A", or blank cells with zero. Replace "-" with zero only when a footnote defines it as zero or not applicable; otherwise treat it as missing and ask the user. The calculators stop when they meet these marks.
- Unify names written differently for the same thing (for example "서울특별시" and "서울") and keep the mapping in the code. Align industries to one level of the Korean Standard Industrial Classification.
- When only a total project cost exists without yearly amounts, do not split it arbitrarily; ask the user for the allocation basis.
- When current and constant prices, consolidated and separate statements, or provisional and final figures are mixed, align them to one basis before calculating.

Common sources and preparation by tool:

| Tool | Target form | Common source and preparation |
| --- | --- | --- |
| growth.py | yearly values in `series` | take the row from a statistics table with years across columns and turn it into year-value pairs |
| feasibility.py | year, item, amount in `costs` and `benefits` | make one line per cell of a yearly investment plan with items in rows and years in columns |
| io_impact.py | `allocations`, `coefficients` | extract only the rows of the assigned sectors from the inducement coefficient table |
| regional.py | CSV with region, industry, and value columns | keep only the "total" (계) establishment-type rows and convert to long form |
| concentration.py | sales or shares per firm in `firms` | put the "other" row of a share table into `other` |
| financials.py | account amounts per period in `periods` | rename accounts to input fields with the account mapping in the financial statement section |
| bep.py | price and variable cost per product, fixed costs | split the cost breakdown into fixed and variable and record the basis |
| variance.py | budget and actual quantity and unit price per item | if the budget-versus-actual table has only amounts and quantities, divide amount by quantity in the preparation code to get unit prices |
| ahp.py | `upper` or `matrix` per evaluator | convert survey answers to pairwise values with the survey rule in the AHP section |
| market_size.py | `top_down`, `bottom_up` | move each factor from market reports and attach its source |

## Growth rates

growth.py calculates CAGR, year-over-year growth, real-price conversion, and growth-based projections.

- CAGR = (last value / first value)^(1/n) - 1, where n = last year - first year. For consecutive yearly data, n is the number of data points minus one. Data from 2020 through 2022 gives n = 2, so do not call it a "3-year average".
- CAGR is undefined when the first value is zero or negative or the last value is negative. The script prints n/a; report the absolute change instead.
- Year-over-year growth across skipped years is calculated as the annual average for that interval.
- Real price = nominal price × (base-year index / index of that year). Use the GDP deflator or the consumer price index and state the index name and base year. Korean preliminary feasibility studies use the construction-investment deflator for costs and the CPI for benefits as the rule.
- Projections compound the CAGR from the last observed value. If `projection_rate` is given, it is used instead. CAGR reflects only the two end points, so check the year-over-year table for volatility.

When reporting, show the substituted formula in one line and put only the final percentage in a separate code block so it is easy to copy.

## Economic feasibility

feasibility.py calculates present values, net present value (NPV), benefit-cost ratio (B/C), internal rate of return (IRR), payback, sensitivity, and switching values from yearly costs and benefits.

The decision criteria are B/C of 1.0 or more, NPV of 0 or more, and IRR above the discount rate. When the present value of costs is positive, B/C and NPV always reach the same conclusion. When IRR points the other way, follow NPV.

Discounting works as follows.

- The base date is the end of `base_year`. The present value of an amount in year t is amount / (1 + r)^(t - base_year). Korean preliminary feasibility studies use the end of the year before the analysis starts as the base date.
- The social discount rate for Korean public projects is 4.5%. Rail and water projects with analysis periods of 30 years or more use 4.5% for the first 30 years of operation and 3.5% afterwards. Enter this as `rate_schedule`: `[{"to_year": 30th operating year, "rate": 0.045}, {"rate": 0.035}]`.
- Private projects and financial analyses use the cost of capital or hurdle rate set by the user. The financial analysis in Korean preliminary feasibility studies uses a real rate of 4.5%.
- Discount rate and analysis period rules can be revised, so for public projects check the latest Guidelines for Conducting Preliminary Feasibility Studies (예비타당성조사 수행 총괄지침) before applying them. The figures here follow Ministry of Planning and Budget Directive No. 63 (29 May 2026).

Prepare costs with these rules before entering them.

- VAT is a tax transfer, so remove it from economic costs. Mark items that include VAT with `"vat_included": true` and the script divides them by 1.1. Change the rate with `vat_rate` if it differs.
- Leave out sunk costs, which were already spent regardless of the decision. Leave out transfers such as subsidies and taxes.
- Enter yearly costs such as operation, maintenance, and post-project follow-up research in `recurring_costs` with a period and an annual amount.
- Enter the value of land and equipment left at the end of the analysis period in `residual_values`. The script deducts it from that year's cost. Land counts at its full purchase price; equipment and buildings count for their remaining useful life.
- Express all amounts in constant prices of one base year.

The analysis period depends on the project type. Construction projects such as roads, airports, ports, and medical facilities add 30 years of operation to the project period, rail adds 40 years, and water resources add 50 years. IT projects and other fiscal projects set it case by case. R&D projects add the benefit gestation period and the benefit period to the project period.

Enter benefits as yearly amounts (`benefits`) or build them as benefit streams (`benefit_streams`).

- The gestation period is the number of years after the project ends before benefits appear. A benefit stream starts in `project_end_year + gestation_years + 1` and lasts `benefit_years`. With a 3-year gestation period there are no benefits for 3 years after the project ends and they start in the 4th year. Check the start and end years in the input-item table of the script output.
- If the whole project follows one roadmap, use one benefit stream. If it develops several independent technologies, build one stream per technology with its own gestation and benefit periods, and check that the combined streams do not exceed the benefit of the whole project.
- If the project plan sets no gestation period, start from 5 years for basic research and 3 years for applied and development research, then adjust for the technology readiness level at the end of the project.
- Base the benefit period on the project plan. Without such evidence, the technology cycle time derived from related patents can be used.
- R&D benefits can be calculated with the market demand approach: annual benefit = future market size × project contribution rate × R&D contribution rate × commercialization success rate × value-added ratio. Put `market_size` and `factors` in a stream and the script multiplies them. State a source for all five values.
- Do not add input-output inducement effects to benefits. Adding induced production or value added to benefits counts the same effect twice.

IRR can have several values or none when the sign of the net cash flow changes more than once. The script shows every root it finds and, if there is not exactly one, says to decide by NPV and B/C.

Payback is the number of years from the first cash-flow year until the cumulative net cash flow reaches zero or more. Discounted payback uses present values. Korean public R&D feasibility studies do not usually use it, but it helps when reviewing private projects.

With `--xlsx`, the first sheet `CF formulas` holds yearly costs, benefits, discount rates, discount factors, present values and totals, plus PV cost, PV benefit, NPV, B/C, and IRR as Excel formulas. Discount factors chain from the base date (the year after the base year = 1/(1+r), later years = previous factor/(1+r)), so editing the rate column recalculates every result. Excel's IRR function shows only one root, so for flows whose sign changes more than once, follow the IRR list in the script report.

Sensitivity by default covers the discount rate ±1 percentage point, costs ±10%, and benefits ±10%. Change the ranges with `sensitivity`. Switching values are the benefit change and the cost change that bring B/C to exactly 1.0, which shows how much margin the result has.

## Economic ripple effects

io_impact.py allocates project spending to input-output sectors and multiplies by inducement coefficients to calculate induced production, value added, total employment, and wage employment.

- Induced production = Σ(sector spending × production inducement coefficient); induced value added = Σ(spending × value-added inducement coefficient).
- Induced employment = Σ(spending × amount unit / coefficient basis amount × coefficient). Bank of Korea coefficients are persons per KRW 1 billion of final demand, so spending in KRW 100 million is divided by 10. The script performs this conversion with `amount_unit_krw` (default KRW 100 million) and `labor_basis_krw` (default KRW 1 billion).
- The total-employment coefficient (취업유발계수) counts all employed persons including the self-employed and unpaid family workers; the wage-employment coefficient (고용유발계수) counts wage workers only. They are different measures, so do not mix their names.

Proceed in this order. If the user gives everything at once, calculate right away.

1. Confirm the total project budget and the amount unit.
2. Draft an allocation of budget items to input-output product sectors and get the user's confirmation.
3. Get the sector coefficients from the user. If an input-output table file is provided, extract the relevant rows, show them in a table, and get confirmation. Input-output tables have many sectors and complex layouts, so rows are easy to misread.
4. Record the coefficient source (table year, domestic-goods basis, regional table or not) in `coefficient_source`, then calculate.

Calculation rules:

- Leave out land purchases, which transfer ownership of an existing asset and create no production. Leave out VAT and transfers as well. List the excluded items with reasons in `excluded`. The script reconciles the total budget with allocated and excluded amounts.
- Apply coefficients to final demand. Do not apply them to gross profit or operating profit.
- Induced production already includes the initial spending. Do not add induced production and induced value added together.
- For effects on a specific region, use coefficients from a regional or inter-regional input-output table. Regional economic effects in Korean preliminary feasibility studies use an inter-regional input-output model as the rule.
- Input-output coefficients assume fixed input ratios and no supply constraints. The result is a gross effect that does not subtract spending displaced elsewhere, and the report should say so.

## Regional industry analysis

regional.py calculates the location quotient (LQ), the regional share of the national industry, and shift-share components. Choose `lq` or `shift_share` with `mode`.

- LQ = (regional industry value / regional total) / (national industry value / national total). Above 1 means the industry takes a larger share in the region than in the nation. Set the threshold for calling an industry specialized with `threshold` and state it in the report. The default is 1.0.
- Regional share = regional industry value / national industry value. Some reports call this indicator "agglomeration" (집적도), so state the formula with the name.
- Choose one basis among employees, establishments, sales, and value added, and state which one.

Prepare the data as CSV or XLSX with one row per region, industry, and value.

- For tables with an establishment-type breakdown, such as the Korean Census on Establishments, keep only the "total" (계) rows. The script stops when the same region and industry appear twice.
- Use one industry classification level only (section or division). Mixing levels counts totals twice.
- Remove or handle cells suppressed for confidentiality (such as X) and tell the user.
- If there is a national row, put its name in `national_label`; if there is an all-industry total row, put its name in `total_label`. Without them the script sums regions and industries and states that assumption in the output.

Shift-share analysis splits the change of a regional industry between two points in time into three parts. The three parts add up to the actual change, and the script checks this.

- National growth effect = base-year regional industry value × national all-industry growth rate
- Industry mix effect = base-year value × (national growth rate of the industry - national all-industry growth rate)
- Regional shift effect = base-year value × (regional growth rate of the industry - national growth rate of the industry)

A positive regional shift means the industry grew faster in the region than the same industry nationwide.

Set an industry in `target` to compare regions, or a region to compare industries. Tables are sorted by LQ in descending order. After showing the table, ask whether a chart is needed; if so, rerun with a file path in `chart`. The chart holds only horizontal bars ordered from the largest LQ at the top, the threshold line, and value labels. A warning appears when no Korean font (NanumGothic, Malgun Gothic, etc.) is installed.

## Market concentration

concentration.py calculates the Herfindahl-Hirschman Index (HHI), concentration ratios of the largest firms (CR1, CR3, CR4), and changes from a merger.

- HHI = Σ(share in %)², ranging from 0 to 10,000. 10,000 / HHI gives the number of equal-sized firms that would produce the same HHI.
- Define the market first (product, region, period). A wider market lowers HHI, so state the definition in the report.
- Sales are converted to shares; shares are checked to sum to 100%.
- When unlisted firms are entered as one "other" lump, HHI is shown as a range. The lower bound treats "other" as many tiny firms; the upper bound treats it as one firm.
- To test a merger, put two firm names in `merger`. The HHI change = 2 × the product of the two firms' shares.

As reference screens, the script prints the horizontal-merger safe harbor of the Korea Fair Trade Commission merger review guidelines (HHI below 1,200; HHI 1,200 to below 2,500 with a change below 250; HHI 2,500 or more with a change below 150) and the US 2023 Merger Guidelines (post-merger HHI above 1,800 or combined share above 30%, with a change above 100). These results are a first screen; legal conclusions come from the competent authority's review.

## Financial statement analysis

financials.py calculates derived measures, financial ratios, period-to-period changes, and consistency between statements from amounts for several periods. Input field names follow `--example`.

Derived measures are defined as follows.

| Measure | Definition |
| --- | --- |
| EBITDA | operating profit + depreciation + amortization |
| CAPEX | purchases of property, plant and equipment + purchases of intangibles (investing cash flows) |
| Net CAPEX | CAPEX - cash received from disposals |
| OPEX | selling, general and administrative expenses (SG&A) |
| Operating costs | cost of sales + SG&A |
| FCF | operating cash flow - CAPEX |

- EBITDA is not a profit defined by accounting standards. Companies may calculate it differently, so state the definition above in the report. It differs from a figure built up from net income by the amount of non-operating items.
- OPEX means different things in different settings. In financial statement analysis it is SG&A; in a business plan it is the recurring cash cost of each operating year (staff, maintenance, rent, etc., excluding depreciation). CAPEX in a business plan is the initial investment. Use business-plan figures as `costs` and `recurring_costs` in the feasibility tool and as the depreciation input of the break-even tool.
- Stability ratios follow the Bank of Korea Financial Statement Analysis definitions: debt ratio = liabilities / equity × 100, interest coverage = operating profit / interest expense × 100, borrowings dependence = borrowings / total assets × 100. Borrowings include bonds.
- ROA and ROE use net income. When comparing with statistics based on pre-tax income, align the numerator.
- ROA, ROE, and turnover ratios use the average of opening and closing balances when the previous period is given, otherwise the closing balance. The parentheses in the table show which.
- Inventory turnover uses cost of sales when available, otherwise revenue, and the table says which.
- Consistency checks cover assets = liabilities + equity, closing cash = opening cash + operating, investing, and financing cash flows + FX effect, and the gap between operating profit and (revenue - cost of sales - SG&A). A gap in operating profit can mean other operating income or expenses exist.
- Change flags mark items that exceed both the rate and the amount thresholds. If the user gives no thresholds, a 10% change is used as a screening default and the output says so. Materiality is judged by the user's own thresholds.
- From annual periods beginning on or after 1 January 2027, K-IFRS 1118 (IFRS 18) changes the scope of operating profit. When comparing figures from 2026 or earlier with 2027 or later, check that they were prepared on the same basis.
- Do not mix consolidated and separate statements; state which one in `statement_basis`.

Account mapping follows K-IFRS statement line items (Korean names in parentheses).

| Input field | Account |
| --- | --- |
| revenue, cogs, sga | revenue (매출액), cost of sales (매출원가), SG&A (판매비와관리비) |
| operating_income, pretax_income, income_tax, net_income | operating profit (영업이익), profit before tax (법인세비용차감전순이익), income tax expense (법인세비용), net income (당기순이익) |
| depreciation, amortization, interest_expense | depreciation (감가상각비), amortization (무형자산상각비) from cash-flow adjustments or notes, interest expense (이자비용) from finance-cost notes |
| total_assets, current_assets, receivables, inventory, cash | total assets, current assets, trade receivables, inventories, cash and cash equivalents |
| total_liabilities, current_liabilities, equity | total liabilities, current liabilities, total equity |
| borrowings | short-term borrowings + current portion of long-term debt + long-term borrowings + bonds (state whether lease liabilities are included) |
| cfo, cfi, cff, fx_effect, cash_begin, cash_end | operating, investing, and financing cash flows, effect of exchange rate changes, opening cash, closing cash |
| capex_ppe, capex_intangible, disposal_proceeds | acquisition of PP&E, acquisition of intangibles, disposal of PP&E and intangibles |

## Break-even point

bep.py uses contribution margin to calculate the break-even point, the volume for a target profit, the margin of safety, and the degree of operating leverage.

- Unit contribution margin = selling price - unit variable cost. With several products, weight by the unit sales mix (`mix`, summing to 1).
- Accounting break-even volume = (cash fixed costs + depreciation) / weighted unit contribution margin. Cash break-even volume uses fixed costs without depreciation and marks the volume at which cash outflow stops.
- Enter depreciation as an amount, or enter CAPEX, useful life, and salvage value to use straight-line depreciation.
- Enter the target profit as a pre-tax amount (`pre_tax`) or as an after-tax amount with a tax rate (`after_tax`, `tax_rate`). Pre-tax target = after-tax target / (1 - tax rate).
- With an expected volume, the script calculates the margin of safety (the share of expected volume above break-even) and the degree of operating leverage (contribution margin / operating profit).
- The calculation assumes price, unit variable cost, and product mix stay constant regardless of volume. State the basis for splitting costs into fixed and variable in the report.

## Variance analysis

variance.py splits the difference between budget (or prior period) and actual by item and decomposes it into price, mix, and volume effects.

- Revenue items are favorable when actual exceeds budget; cost items are favorable when actual is below budget. Put `revenue` or `cost` in `kind`.
- Price effect = Σ(actual unit price - budget unit price) × actual quantity
- Mix effect = Σ(actual quantity - total actual quantity × budget mix) × budget unit price
- Volume effect = (total actual quantity - total budget quantity) × budget average unit price
- The three effects add up to the total variance, and the script checks this.
- The mix effect only makes sense when items share the same quantity unit. If units differ, set `"separate_mix": false` to calculate only item-level volume effects.
- Without quantities, enter only `budget` and `actual` amounts. The output then holds item variances and the bridge table only.
- Flags work as in the financial statement analysis: an item is flagged when it exceeds both the user's rate and amount thresholds.
- For staff costs, put headcount as the quantity and average cost per person as the unit price. The price effect is then the rate difference and the volume effect the headcount difference.
- To compare budget, forecast, and actual together, run twice: actual versus budget and actual versus forecast.

For each flagged item, write two or three sentences covering the amount and rate, favorable or unfavorable, which effect dominated, whether it is one-off or likely to continue, and the follow-up needed. Do not explain a result by restating it, as in "revenue variance arose because revenue rose". The bridge table starts at budget, adds each effect, and arrives at actual; the script checks that the arrival value matches actual.

## Weighting with AHP

ahp.py derives criterion weights and the consistency ratio (CR) from AHP pairwise comparison matrices and combines several evaluators.

- Weights are the principal eigenvector of the pairwise matrix, summing to 1. CI = (λmax - n) / (n - 1), CR = CI / RI. RI values follow Saaty (2000): 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45 for n = 3 to 9.
- Keep 2 to 9 items per matrix. With more items, split them into upper and lower levels and run each level. Get global weights of a lower level by entering `parent_weight` (the weight of the parent item).
- Enter a matrix in full (`matrix`) or as the values above the diagonal (`upper`). `upper` is read row by row: with three items the order is row 1 column 2, row 1 column 3, row 2 column 3. Values lie between 1/9 and 9, and fraction strings such as "1/3" are accepted.
- Convert 9-point scale surveys with the left item as i and the right item as j. A mark of k on the left side gives a_ij = k, a mark of k on the right side gives a_ij = 1/k, and the middle (equal) gives 1. If the survey order differs from `criteria`, reorder when building the matrix.
- The usual CR threshold is 0.1. Korean preliminary feasibility studies allow a re-survey when CR exceeds 0.15. Set the threshold with `cr_threshold` and suggest a re-survey for evaluators above it.
- Group weights come from the element-wise geometric mean of the evaluators' matrices. Set `aggregate_consistent_only` to true to combine only evaluators who pass the CR threshold.
- With evaluator ratings per criterion (0 to 1) in `ratings`, the script calculates each evaluator's composite score = Σ(own weight × rating). Setting `trim` drops that many of the highest and the lowest scores before averaging. The comprehensive evaluation of Korean preliminary feasibility studies drops two on each side and treats a score of 0.5 or more for implementing the project as feasible.

## Market sizing

market_size.py calculates TAM, SAM, and SOM top-down and compares them with a bottom-up estimate.

- TAM is the annual demand of the whole defined market. Enter the figure directly, or build it as users × adoption rate × annual spend per user.
- SAM is the part of TAM the offering can serve given its product scope, region, and sales channels. Enter each filter's share and source in `sam_filters`.
- SOM is the part of SAM that can be won within a set period given competition and capacity. State the basis of the target share (such as early shares of comparable entrants).
- Bottom-up estimate = Σ(customers × adoption rate × units per customer × unit price × purchases per year). Compare its ratio to the top-down SOM; when they differ widely, explain which assumptions differ before choosing one.
- Projections use the CAGR in `projection`. The growth rate needs a source too.
- The script lists inputs without sources. When converting foreign market data to KRW, state the exchange rate and its date.

## Reporting results

- State the verdict in the first line, with indicator, value, and criterion together, for example "B/C is 1.16, above the 1.0 criterion".
- Then give the input table (with sources), the substituted formulas, the result tables, and sensitivity and assumptions, in that order.
- Put units in table headers and use thousands separators. Show ratios to two decimals and B/C and AHP weights to four.
- Carry the script's warnings and assumptions (sums built by the script, default screening thresholds, etc.) into the report.
- End with the commands run and the input JSON so a third party can reproduce the result.
- When the user asks for the calculation tables as files, or the tables are too long to read in the chat, save them with `--xlsx` or `--csv` and hand them over. For economic feasibility results, hand over the Excel file with the `CF formulas` sheet by default.
