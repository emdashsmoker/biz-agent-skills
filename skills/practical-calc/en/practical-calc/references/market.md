# Market Analysis

HHI and CRk measure how much of a market's sales a few firms hold, and TAM, SAM and SOM estimate how large a market is. Both results depend on how the market is defined, so set the product scope and geographic scope before calculating and state them in the report.

## Market Concentration

### Formulas

```
HHI = sum of squared market shares (%) of each firm
CRk = combined share of the k largest firms
HHI change after a merger = 2 x share of firm a x share of firm b
```

- HHI runs from 0 to 10,000. A single firm holding the whole market gives 10,000.
- With sales amounts as input, the script treats the total of the listed firms as 100% and computes shares. Add `--shares` to enter shares (%) directly.
- When shares add up to less than 100%, the makeup of the remaining firms is unknown. The script shows a range: the value with the remainder spread over many tiny firms (lower bound) and the value with the remainder held by one firm (upper bound).
- `--k` sets the k values for CRk. The default is 1, 3 and 4.
- `--merge "Firm A,Firm B"` computes the HHI change and the post-merger HHI for combining the two firms.

### Reference Thresholds

The thresholds below come from merger review. When quoting them to describe a market, name the agency and the rule.

| Agency | Threshold |
|---|---|
| Korea Fair Trade Commission, merger review guidelines | For horizontal mergers, HHI below 1,200, HHI from 1,200 to below 2,500 with a change below 250, or HHI of 2,500 or more with a change below 150 falls in the range of low competitive concern |
| Korea Fair Trade Commission, merger review guidelines | A combined share of 75% or more held by the top three or fewer firms, with further conditions, leads to a presumption of restricted competition |
| U.S. Department of Justice and Federal Trade Commission, 2023 Merger Guidelines | HHI above 1,800 marks a highly concentrated market, and a merger that raises HHI by more than 100 there is presumed to reduce competition |

### Input Collection Order

1. Market definition (product scope, geographic scope, reference year)
2. Sales or share for each firm, with the data source
3. Names of two firms when a merger is under review

### Input Format

```
firm,value
Firm A,32
Firm B,25
Firm C,18
```

### Run Example

```
python scripts/hhi.py --input examples/shares.csv --shares --merge "Firm C,Firm D" --chart shares.png
```

## Market Size

### Terms

| Term | Definition |
|---|---|
| TAM | Yearly demand in money for the whole product or service category |
| SAM | Part of TAM the business can serve with its products, regions and sales channels |
| SOM | Part of SAM the business expects to win within the plan period, given competition and sales capacity |
| Top-down estimate | Starts from a published total market size and multiplies ratios in turn |
| Bottom-up estimate | Starts from unit values such as customer counts and spend per customer and multiplies upward |

### Formulas

List the steps of each approach in order. The first step's value is the starting value, and every later step multiplies the running product. The running product at the end of the TAM steps is TAM, at the end of the SAM steps is SAM, and at the end of the SOM steps is SOM.

- Steps follow the order TAM, SAM, SOM, and each stage needs at least one step.
- Enter ratios as decimals. 25% is 0.25.
- In a bottom-up estimate, match units so the product of the steps is an amount of money. Target companies x annual spend per company (100 million KRW) gives 100 million KRW.
- Record the data source or the basis of each assumption in the step's `source`. Mark ratios without a source as assumptions, and rerun with changed values to test their effect.
- With two approaches, the script computes the gap for each stage. When the gap is large, find the step that causes it and recheck the assumption.
- With `projection`, the script applies a constant yearly growth rate to each stage to estimate size in the target year. Cite the source of the growth rate as well.

### Input Collection Order

1. Market definition (product category, region, reference year) and money unit
2. Starting value and ratios for the top-down estimate, with sources
3. Unit values and ratios for the bottom-up estimate, with sources
4. Yearly growth rate and years, when a target-year size is needed

### Input Format

```json
{
  "unit": "100 million KRW",
  "approaches": {
    "top-down": [
      {"stage": "TAM", "name": "Domestic business software market", "value": 50000, "source": "Market research report"},
      {"stage": "SAM", "name": "Share of target industries", "value": 0.25},
      {"stage": "SOM", "name": "Target share within 5 years", "value": 0.05}
    ],
    "bottom-up": [
      {"stage": "TAM", "name": "Target companies", "value": 80000},
      {"stage": "TAM", "name": "Annual spend per company (100 million KRW)", "value": 0.6},
      {"stage": "SAM", "name": "Share in serviceable regions", "value": 0.55},
      {"stage": "SOM", "name": "Share of customers reachable per year", "value": 0.06}
    ]
  },
  "projection": {"start_year": 2025, "end_year": 2030, "growth_rate": 0.08}
}
```

### Run Example

```
python scripts/market_size.py --input examples/market.json --chart market.png
```

## Sources

> Korea Fair Trade Commission(2025), 2025 기업결합신고 가이드북 (2025 Merger Notification Guidebook)(https://mna.ftc.go.kr/resources/mna/file/pdfGuide2025.pdf)

> U.S. Department of Justice and Federal Trade Commission(2023), Merger Guidelines(https://www.ftc.gov/system/files/ftc_gov/pdf/2023_merger_guidelines_final_12.18.2023.pdf)
