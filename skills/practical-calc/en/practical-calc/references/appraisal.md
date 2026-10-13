# Project Appraisal

The tool converts a project's costs and benefits into values at one point in time and compares them. Its outputs are the B/C ratio, NPV, IRR, payback period and sensitivity analysis. Financial analysis uses the same arithmetic. Enter cash inflows in place of benefits and cash outflows in place of costs, and the script labels the ratio as the profitability index (PI) and NPV as FNPV.

## Terms

| Term | Definition |
|---|---|
| Discount base year | Year to which present values are brought, valued at the end of that year |
| t | Year - discount base year |
| Discount rate | Yearly rate used to convert future amounts into present value |
| Benefit, cost | In economic analysis, the value society gains and the price it pays |
| Cash inflow, cash outflow | In financial analysis, the cash the project owner receives and pays |
| Project end year | Last year in which project spending occurs |
| Gestation period | Number of years with no benefit, counted from the year after the project end year until the first benefit |
| Benefit duration | Number of years benefits last, counted from the first benefit year |
| Analysis period | From the first cash flow year to the last cash flow year, or to `analysis_end_year` when given |
| Residual value | Asset value left at the end of the analysis period, deducted from the last year's cost |

## Formulas

```
discount factor(t) = 1 / (1 + r)^t
benefit PV = sum of yearly benefit x discount factor
cost PV = sum of yearly cost x discount factor
B/C ratio = benefit PV / cost PV
NPV = benefit PV - cost PV
IRR = discount rate at which the sum of (benefit - cost) / (1 + IRR)^t equals 0
```

- The first benefit year is `project end year + gestation period + 1`. A project that ends in 2028 with a two-year gestation period produces its first benefit in 2031.
- When the discount rate changes partway, discount up to the switch year at the first rate r1 and discount only the later years at the new rate r2. With switch year (`after_year`) T, the discount factor for a year after T is `(1 + r1)^-(T - discount base year) x (1 + r2)^-(year - T)`. The declining discount factor tables in the UK Treasury Green Book follow the same method.
- The script searches for every rate between -90% and 1,000% at which the present value of net benefits equals 0. When the net cash flow changes sign once, the IRR is unique. When the sign changes several times and several IRR candidates appear, the script lists them all and tells the user to judge by NPV and the B/C ratio.
- The discounted payback period is the number of years until the cumulative discounted net benefit first reaches 0 or more. The simple payback period does the same with undiscounted values. Counting starts at the beginning of the first cash flow year, and within the recovery year the script assumes net benefits arrive evenly and interpolates on a straight line.
- Payback periods help compare alternatives. Judge a single project by the B/C ratio, NPV and IRR.

## Decision Rules

| Indicator | Economic analysis | Financial analysis |
|---|---|---|
| Ratio | B/C ratio of 1.0 or more | PI above 1.0 |
| Net present value | NPV of 0 or more | FNPV above 0 |
| Internal rate of return | IRR above the social discount rate | IRR above the cost of capital |

## Korean Preliminary Feasibility Study Values

These values apply when the analysis follows Korea's preliminary feasibility study (PFS) method. The social discount rate is reviewed every three years, so check the latest guideline before use.

| Item | Value | Article |
|---|---|---|
| Social discount rate | 4.5% | Art. 50 |
| Railway and water resource projects | 4.5% for the first 30 operating years, 3.5% after | Art. 50 |
| Discount base year | End of the year before the study starts | Art. 49 |
| Analysis period | Project period + 30 operating years (roads, airports, ports, medical facilities, other large construction), 40 for railways, 50 for water resources, set per project for IT and other fiscal projects | Art. 49 |
| Economic cost | Excludes VAT and sunk costs, includes opportunity costs | Art. 45 |
| Sensitivity variables | Project cost, operating cost, demand, discount rate | Art. 51 |
| Financial analysis | Real financial discount rate 4.5%, taxes and interest counted as costs | Art. 55 |

For railway and water resource projects, set `after_year` in `rate_switch` to the 30th operating year. Operations that start in 2031 give `after_year` 2060.

## Input Collection Order

1. (Basic information) Discount base year, project start year, project period, discount rate, gestation period, benefit duration
2. (Benefit items) Yearly amounts or generation rules
3. (Cost items) Yearly amounts or generation rules

Without a discount rate the script applies the social discount rate of 4.5% and records that in the notes. When independent outputs within one project each produce their own benefits, collect a gestation period and duration per benefit item. In that case confirm that the sum of item benefits does not count the same benefit twice. When the user supplies a file with the values (CSV, XLSX, PDF), extract the values into a JSON input file and show the extracted values in the input summary table.

## Input Format

```json
{
  "unit": "100 million KRW",
  "mode": "economic",
  "base_year": 2025,
  "discount_rate": 0.045,
  "rate_switch": {"after_year": 2060, "rate": 0.035},
  "cost_rules": [
    {"item": "Construction cost", "total": 300, "start_year": 2026, "years": 3},
    {"item": "Operating cost", "annual": 12, "start_year": 2029, "end_year": 2058}
  ],
  "benefit_rules": [
    {"item": "Travel time savings", "annual": 40, "project_end_year": 2028, "gestation": 0, "duration": 30, "growth": 0.01}
  ],
  "costs": [{"item": "Residual value", "year": 2058, "amount": -20}],
  "benefits": [],
  "sensitivity": {"rate_delta": 0.01, "cost_changes": [-0.1, 0.1], "benefit_changes": [-0.1, 0.1]}
}
```

| Field | Required | Content |
|---|---|---|
| `unit` | Optional | Label for the amount unit |
| `mode` | Optional | `economic` (default) or `financial` |
| `base_year` | Required | Discount base year |
| `discount_rate` | Optional | Discount rate as a decimal (4.5% is 0.045), 0.045 when omitted |
| `rate_switch` | Optional | Applies `rate` from the year after `after_year` |
| `analysis_end_year` | Optional | Last analysis year; later cash flows drop out of the calculation |
| `costs`, `benefits` | Optional | Yearly amounts `{"item", "year", "amount"}` |
| `cost_rules`, `benefit_rules` | Optional | Generation rules below |
| `sensitivity` | Optional | Sensitivity ranges; defaults are discount rate ±1 percentage point, cost ±10%, benefit ±10% |

### Generation Rules

Rules create yearly amounts without typing each year.

- (Even spread) `total`, `start_year` and `years` assign `total / years` to each of `years` years from `start_year`.
- (Annual amount) `annual` with a start year and an end year assigns the same amount each year. Give the start year as `start_year`, or derive it from `project_end_year` and `gestation`. Give the end year as `end_year`, or derive it from `duration`.
- (Growth) With `growth` in an annual rule, the amount in year k is `annual x (1 + growth)^k`, with k = 0 in the first year.
- (Residual value) Enter it as a negative cost in the last year. The script lists years with negative costs in the notes.

## Run Example

```
python scripts/appraisal.py --input examples/project.json --out appraisal_result.json --chart cumulative_npv.png
```

## Reporting

- (Annual table) Year, t, discount factor, cost, cost PV, benefit, benefit PV, net PV and totals
- (Indicators) Benefit PV, cost PV, B/C ratio, NPV, IRR, discounted payback, simple payback
- (Sensitivity analysis) B/C ratio and NPV for each scenario that changes the discount rate, costs or benefits
- (Reproduction) Input JSON and the command

The cost scenarios in the sensitivity analysis scale every cost item by the same ratio. To change only project cost, only operating cost, or demand, rerun with an input file that carries the changed values.

## Sources

> Ministry of Planning and Budget, Republic of Korea(2026), 예비타당성조사 수행 총괄지침 (General Guidelines for Conducting Preliminary Feasibility Studies) Articles 45, 47, 49, 50, 51, 55, 56(https://www.law.go.kr/행정규칙/예비타당성조사수행총괄지침)

> Korea Institute of S&T Evaluation and Planning(2024), 국가연구개발사업 예비타당성조사 수행 세부지침 (Detailed Guidelines for Preliminary Feasibility Studies of National R&D Programs)(https://www.kistep.re.kr/reportDetail.es?mid=a10305070000&rpt_tp=831-003&rpt_no=RES0220240120)

> HM Treasury(2026), Green Book supplementary guidance: discounting(https://assets.publishing.service.gov.uk/media/698f30a4492ea446ea7f43d3/Green_Book_supplementary_guidance_-_discounting.pdf)
