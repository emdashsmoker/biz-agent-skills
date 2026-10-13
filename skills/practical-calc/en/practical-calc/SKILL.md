---
name: practical-calc
description: Toolkit that runs common planning and consulting calculations as reproducible Python scripts and exports result tables to CSV or XLSX. Covers CAGR and real-price conversion (references/growth.md), B/C ratio, NPV, IRR, payback and sensitivity (references/appraisal.md), AHP weights (references/ahp.md), income statement summary, EBITDA, OPEX, CAPEX and break-even (references/corporate.md), price, mix and quantity variance (references/variance.md), input-output ripple effects and location quotient (references/industry.md), HHI, CRk and TAM, SAM, SOM sizing (references/market.md), input data preparation (references/data-prep.md) and chart rules (references/charts.md). Use it for growth rates, cost-benefit or feasibility economics, payback, criteria weighting, margins, break-even volume, budget versus actual gaps, output or employment effects, industry specialization, market concentration or market size, even when no tool is named.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Practical Calculation Toolkit

> Translated edition. This skill was translated from the Korean original. Some wording may not carry the exact meaning of the original, and the skill may behave in ways the original does not intend.

This toolkit runs calculations that planners and consultants use often. The `references` folder holds the formulas, definitions and decision rules, and the scripts in the `scripts` folder do every calculation. The same input file and the same command give anyone the same result.

## Tool List

| Subject | Tool | Script | Reference |
|---|---|---|---|
| Time series | CAGR | `cagr.py` | `references/growth.md` |
| Time series | Real-price conversion | `deflate.py` | `references/growth.md` |
| Projects and alternatives | B/C ratio, NPV, IRR, payback period, sensitivity analysis | `appraisal.py` | `references/appraisal.md` |
| Projects and alternatives | AHP weights, consistency ratio | `ahp.py` | `references/ahp.md` |
| Corporate finance | Income statement summary, EBITDA, OPEX | `pl_summary.py` | `references/corporate.md` |
| Corporate finance | CAPEX, free cash flow, depreciation | `capex.py` | `references/corporate.md` |
| Corporate finance | Break-even point (BEP) | `bep.py` | `references/corporate.md` |
| Corporate finance | Price, mix and quantity variance, forecast accuracy | `variance.py` | `references/variance.md` |
| Industries and markets | Economic ripple effects (input-output analysis) | `io_impact.py` | `references/industry.md` |
| Industries and markets | Location quotient (LQ) | `lq.py` | `references/industry.md` |
| Industries and markets | Market concentration (HHI, CRk) | `hhi.py` | `references/market.md` |
| Industries and markets | Market size (TAM, SAM, SOM) | `market_size.py` | `references/market.md` |

Rules for turning submitted material into input files live in `references/data-prep.md`, and chart rules live in `references/charts.md`. The sample input files used in the references live in the `examples` folder. When one request spans several tools, run the procedure below once per tool.

## Calculation Principles

A number that a language model computes in its head can be wrong without any visible sign, so the scripts compute every number, including sums, ratios and rounding. Reports copy the script output as printed.

- Take inputs from material the user supplied or from public statistics with a confirmed source. Values that need official statistics, such as input-output coefficients, price indices and market shares, come from a cited source.
- Attach a unit to every amount. When input and output units differ, state the conversion rule next to the result.
- Save inputs to a file before passing them to a script. A third party can reproduce the result only when the input file and the command survive.
- Use only the decision rules and sources written in the references (for example, a B/C ratio of 1.0 or more).

## Procedure

1. Identify the purpose of the calculation and pick the script and reference from the tool list.
2. Read the definitions, formulas, input format and input collection order in the reference.
3. Collect the inputs. If the request already contains every required value, calculate right away without questions. If values are missing, ask for all of them in one message, following the input collection order in the reference.
4. Save the input file (JSON or CSV) in the working folder. When the submitted material does not match the input format, write conversion code following `references/data-prep.md` and save that code file as well.
5. Run the script.
6. If the script prints "Notes", pass them on together with the results. If the script stops on an input error, show the message to the user and fix the input.
7. Arrange the results in the report format below. If the user did not ask for a chart up front, show the results first and then ask once whether a chart is needed.

## How to Run

Script paths are relative to the skill folder. Every script shares the same common options.

```
python scripts/<script name> --input <input file> [--decimals 2] [--export tables.xlsx] [--out result.json] [--chart chart.png]
```

| Option | Purpose |
|---|---|
| `--decimals` | Decimal places shown in tables (default 2) |
| `--export` | Save the printed tables to a file: one sheet per table for `.xlsx`, one file per table for `.csv` |
| `--out` | Save the full results as a JSON file |
| `--chart` | Save a chart as a PNG file |

Tool-specific options and input formats follow the run examples in each reference. `cagr.py` also accepts values as options instead of an input file, and `variance.py` takes `mix` or `accuracy` as its first argument.

On an input error the script exits with code 2 and prints the cause. Where code cannot run, give the user the input file content and the command so they can run it themselves. Leave result numbers blank in that case.

## Report Format

- (Inputs) Values used, units, data sources and preparation steps that changed values
- (Calculation steps) Intermediate tables printed by the script
- (Results) Key indicator table and a one or two sentence reading based on the decision rules in the reference
- (Notes) Warnings printed by the script, when present
- (Reproduction) Input file content, preparation code and the command in code blocks

When the user wants the tables as files, or the tables run long, create an XLSX or CSV file with `--export` and send it along. Exported files hold unrounded values. Ratios are stored as percentage numbers, with "(%)" added to the matching column name or row label.

## Environment

- Python 3.9 or later with numpy and pandas. Charts also need matplotlib, and XLSX input and export need openpyxl.
- Install with `pip install numpy pandas matplotlib openpyxl`.
- Charts use the NanumGothic font, which covers Latin and Hangul text. Without it the script prints a notice and falls back to the default font.
- Versions used for verification at the time of writing: Python 3.11, numpy 2.4, pandas 3.0, matplotlib 3.10.
