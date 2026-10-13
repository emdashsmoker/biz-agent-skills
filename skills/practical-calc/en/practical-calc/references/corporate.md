# Corporate Finance Indicators

The tools compute profitability, investment size and the break-even point from income statement, cash flow statement and balance sheet figures. Account names follow the by-function income statement presentation of Korean IFRS (K-IFRS).

## Income Statement Summary

The script takes line items by period, computes gross profit, operating profit, EBITDA, OPEX and margins, and compares two periods.

### Terms and Formulas

| Indicator | Formula |
|---|---|
| Gross profit | Revenue - cost of sales |
| Operating profit | Gross profit - SG&A (a reported value takes priority) |
| EBITDA (operating profit basis) | Operating profit + depreciation + amortization |
| EBITDA (net income basis) | Net income + income tax expense + interest expense + depreciation + amortization |
| OPEX | Cost of sales + SG&A - depreciation - amortization |
| Margin | Each profit / revenue |
| OPEX to revenue | OPEX / revenue |

- Accounting standards do not define EBITDA, so companies compute it in different ways. This tool uses the operating profit basis by default. IFRS 18, effective from 2027, does not treat "operating profit before depreciation, amortisation and impairments within the scope of IAS 36" as a management-defined performance measure (MPM). Adding impairment losses to this tool's operating profit basis EBITDA gives that measure.
- EBITDA on a net income basis includes non-operating items such as interest income, other income and other expenses. The gap between the two bases equals the total of non-operating items other than interest expense.
- A variant EBITDA that adds back impairment losses needs the added items stated in the report.
- This tool defines OPEX as operating expenses excluding depreciation and amortization, which equals revenue - EBITDA. Depreciation spreads past CAPEX over time, so leaving it out of OPEX keeps OPEX and CAPEX from overlapping. Some practitioners call SG&A alone OPEX, so state the definition in the report.
- When reported operating profit and computed operating profit (gross profit - SG&A) differ by more than 0.5% of revenue, the script flags it. A common cause is other operating income or expenses included in operating profit.

### Comparison and Flags

The script computes the change and change rate of the `--current` period against the `--compare` period. Without these options it compares the last column with the column before it. A line gets an O in the flag column when the absolute change rate reaches `--threshold-pct` (default 10) or the absolute change reaches `--threshold-amount`. The flag shows only the size of a change, so an increase in a cost line and an increase in a profit line read in opposite directions. Use the organization's materiality threshold when one exists. Margin changes appear in percentage points (%p).

### Input Collection Order

1. Line items by period (revenue, cost of sales, SG&A, depreciation and amortization are needed for EBITDA and OPEX)
2. Analysis period and comparison period
3. Flag thresholds (change rate, change amount)

### Input Format

The first column `item` holds account names and the other columns hold amounts by period. Recognized names are revenue, cost of sales, SG&A, operating profit, depreciation, amortization, interest expense, income tax expense and net income, with their Korean account names and the keys revenue, cogs, sga, operating_income, depreciation, amortization, interest_expense, income_tax and net_income. The script leaves out unrecognized accounts and lists them. A missing amortization row counts as 0 with a notice.

```
item,2024,2025
Revenue,1000,1150
Cost of sales,620,700
SG&A,250,270
Depreciation,40,45
Amortization,10,12
```

### Run Example

```
python scripts/pl_summary.py --input examples/pl.csv --unit "100 million KRW" --chart operating_profit_bridge.png
```

The chart is a waterfall from the comparison period's operating profit through the changes in revenue, cost of sales and SG&A to the current period's operating profit.

## CAPEX

CAPEX (capital expenditure) is spending to acquire property, plant and equipment or intangible assets, or to improve their capacity. It goes on the balance sheet as an asset and becomes expense over time through depreciation.

### Formulas

| Indicator | Formula |
|---|---|
| CAPEX (cash flow statement) | Purchases of PP&E + purchases of intangible assets |
| CAPEX (balance sheet roll-forward estimate) | Closing net PP&E - opening net PP&E + depreciation + book value of disposals + impairment |
| CAPEX to revenue | CAPEX / revenue |
| Free cash flow (FCF) | Operating cash flow - CAPEX |

- Use purchase amounts from the investing section of the cash flow statement when available. Estimate from balance sheet movements only when they are missing.
- The roll-forward estimate cannot separate assets added through revaluation, exchange rate changes or business combinations. The script flags periods that use the estimate.
- Opening and closing intangible balances with amortization add the intangible part in the same way.

### Depreciation Schedule

The schedule shows how planned CAPEX turns into yearly expense.

| Method | Yearly depreciation |
|---|---|
| Straight-line (`straight`) | (Cost - residual value) / useful life |
| Declining balance (`declining`) | Opening book value x rate, rate = 1 - (residual value / cost)^(1 / useful life) |

With this rate the closing book value in the last year equals the residual value. A residual value of 0 makes the rate 100%, so the declining balance method needs a residual value above 0.

### Input Collection Order

1. PP&E and intangible purchases by period, or opening and closing balances with depreciation
2. Revenue and operating cash flow by period (for CAPEX to revenue and FCF)
3. For each asset that needs a schedule: cost, residual value, useful life, start year and method

### Input Format

```json
{
  "unit": "100 million KRW",
  "periods": [
    {"period": "2024", "ppe_purchase": 90, "intangible_purchase": 8, "revenue": 1000, "operating_cash_flow": 150},
    {"period": "2025", "net_ppe_begin": 400, "net_ppe_end": 440, "depreciation": 45, "ppe_disposals_nbv": 5, "revenue": 1150, "operating_cash_flow": 175}
  ],
  "assets": [
    {"name": "Production equipment", "cost": 100, "residual": 10, "life": 5, "start_year": 2026, "method": "straight"}
  ]
}
```

The intangible roll-forward uses `net_intangible_begin`, `net_intangible_end`, `amortization`, `intangible_disposals_nbv` and `intangible_impairment`, and PP&E impairment goes in `ppe_impairment`.

### Run Example

```
python scripts/capex.py --input examples/capex.json --chart capex.png
```

## Break-Even Point

The break-even point (BEP) is the sales volume or revenue at which sales cover fixed and variable costs and operating profit is 0.

### Formulas

| Indicator | Formula |
|---|---|
| Contribution margin per unit | Price - variable cost per unit |
| Contribution margin ratio | Contribution margin per unit / price |
| Break-even units | Fixed cost / contribution margin per unit |
| Break-even sales | Fixed cost / contribution margin ratio |
| Units for target profit | (Fixed cost + target pre-tax profit) / contribution margin per unit |
| Target pre-tax profit | Target after-tax profit / (1 - tax rate) |
| Margin of safety (sales) | Current sales - break-even sales |
| Margin of safety ratio | Margin of safety / current sales |
| Degree of operating leverage (DOL) | Contribution margin / operating profit |

- With several products, the script uses price and contribution margin weighted by the unit sales mix (`mix`). Splitting break-even units by the mix gives break-even units per product. When the mix does not add up to 1, the script rescales it and says so.
- With `tax_rate`, `target_profit` counts as after-tax profit and the script converts it to pre-tax profit. Without `tax_rate`, `target_profit` counts as pre-tax profit.
- `current_units` is total volume at the given mix.
- DOL shows the percentage change in operating profit for a 1% change in sales. The script skips it when operating profit is 0 or below.
- The calculation assumes price, variable cost per unit, fixed cost and mix stay constant over the volume range.

### Input Collection Order

1. Fixed cost
2. Price, variable cost per unit and unit mix for each product
3. Target profit and tax rate (when target volume is needed)
4. Current volume (when margin of safety and DOL are needed)

### Input Format

```json
{
  "unit": "KRW",
  "fixed_cost": 120000000,
  "products": [
    {"name": "Standard", "price": 30000, "variable_cost": 18000, "mix": 0.7},
    {"name": "Premium", "price": 50000, "variable_cost": 27000, "mix": 0.3}
  ],
  "target_profit": 40000000,
  "tax_rate": 0.2,
  "current_units": 12000
}
```

### Run Example

```
python scripts/bep.py --input examples/bep.json --chart bep.png
```

The chart shows the revenue line and the total cost line against volume, and the break-even point where they cross.

## Sources

> IFRS Foundation(2024), IFRS 18 Presentation and Disclosure in Financial Statements: Effects Analysis(https://www.ifrs.org/content/dam/ifrs/publications/amendments/english/2024/effect-analysis-ifrs18-april2024.pdf)

> OpenStax(2022), Principles of Finance 5.6 Operating Cash Flow and Free Cash Flow to the Firm(https://openstax.org/books/principles-finance/pages/5-6-operating-cash-flow-and-free-cash-flow-to-the-firm-fcff)

> OpenStax(2019), Principles of Accounting Volume 2 3.2 Calculate a Break-Even Point in Units and Dollars(https://openstax.org/books/principles-managerial-accounting/pages/3-2-calculate-a-break-even-point-in-units-and-dollars)

> OpenStax(2019), Principles of Accounting Volume 2 3.5 Calculate and Interpret a Company's Margin of Safety and Operating Leverage(https://openstax.org/books/principles-managerial-accounting/pages/3-5-calculate-and-interpret-a-companys-margin-of-safety-and-operating-leverage)
