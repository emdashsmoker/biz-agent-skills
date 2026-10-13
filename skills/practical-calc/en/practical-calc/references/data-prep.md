# Preparing Input Data

Users submit material in many shapes: report tables in Excel, files downloaded from statistics portals, accounting system exports, tables in PDFs, or numbers pasted into the conversation. The scripts read fixed formats, so keep the values as they are and change only the shape to match the input format.

## Principles

- Leave the original file untouched. Save the converted result as a new file.
- Convert with pandas code and save the code in a file such as `prep_<tool name>.py`. With the original file and this code, a third party can rebuild the same input file.
- Steps that change only the shape, such as renaming columns or converting to long format, need no more than the code. Steps that change values, such as unit conversion, turning symbols into numbers or dropping rows, also go into the input summary of the report.
- Check the table headers and notes to learn which column holds totals, what the unit is and what each symbol means. When the material cannot settle it, ask the user and leave the value unfilled.
- After converting, print row counts and key totals for the original and the result to confirm that no value went missing or was counted twice.

## Steps

1. (Structure) Check the sheet list, header row position, merged cells, unit notes above or below the table, footnotes, and total and subtotal rows.
2. (Column mapping) Decide which original column feeds each column or field in the input specs below.
3. (Reshape) Turn wide tables, where years or regions run across columns, into long format with `melt`.
4. (Clean values) Apply the number rules below.
5. (Filter and aggregate) Keep only the needed rows, and decide whether to sum keys that appear more than once. When subtotal and total rows sit together, keep one kind.
6. (Save and check) Save as CSV (UTF-8) or JSON and print row counts and totals next to the original's.
7. (Calculate) Run the script on the saved file.

## Number Rules

| Original notation | Handling |
|---|---|
| `1,234` | The scripts treat commas as thousands separators and remove them |
| `(1,234)` | The scripts read accounting parentheses as -1,234 |
| `12.5%` | Ratio fields in JSON (discount rate, market size ratios) take 0.125; the share column of `hhi.py --shares` takes 12.5 |
| Symbols such as `-`, `X`, `…` | Check the table notes, then replace with 0 or drop the row |
| Values with units attached, such as `1.2 bn` | Split number and unit and convert to one unit |
| Years such as `2024` with suffixes like `p` | Convert to an integer year and record provisional marks in the input summary |
| Decimal commas such as `1.234,5` | These clash with the scripts' comma rule, so convert them to decimal points during preparation |

The scripts handle only commas, accounting parentheses and surrounding spaces. Leftover percent signs or symbols stop the calculation with a message naming the value.

## Input Specs by Tool

Most column names can be changed with options (for example `--year-col`). Each reference's input format section lists the fields in detail.

| Script | Format | Required columns or fields |
|---|---|---|
| `cagr.py` | CSV, XLSX or option values | `year`, `value` |
| `deflate.py` | CSV, XLSX | `year`, `nominal`, `index` |
| `appraisal.py` | JSON | `base_year` with the needed items among `costs`, `benefits`, `cost_rules`, `benefit_rules` |
| `ahp.py` | JSON | `criteria`, `respondents[].matrix` |
| `pl_summary.py` | CSV, XLSX | `item` and one column per period |
| `capex.py` | JSON | `periods` or `assets` |
| `bep.py` | JSON | `fixed_cost`, `products[]` |
| `variance.py mix` | CSV, XLSX | `item`, `budget_qty`, `budget_price`, `actual_qty`, `actual_price` |
| `variance.py accuracy` | CSV, XLSX | `period`, `forecast`, `actual` |
| `io_impact.py` | CSV, XLSX | `item`, `amount`, `output_coef`, `va_coef`, `emp_coef` |
| `lq.py` | CSV, XLSX | `region`, `industry`, `value` |
| `hhi.py` | CSV, XLSX | `firm`, `value` |
| `market_size.py` | JSON | `approaches` |

## Conversion by Source Type

- (Statistics portal tables) Open the downloaded file and check the actual layout of header rows, category columns and total rows, then apply the steps above. Copy column names and category values into the code exactly as they appear in the file.
- (Financial statements) For income statements from disclosure systems or accounting software, rename accounts to the names `pl_summary.py` recognizes and leave out sub-accounts. Commas and accounting parentheses can stay.
- (Input-output tables) Find the coefficients for the product groups under analysis in the coefficient tables and collect one row per product group. In an output inducement table in inverse-matrix form, use the column sum for the product group.
- (Tables in PDFs or images) After extracting a table, show it as extracted in the input summary. For numbers read by character recognition, check that their total matches the total in the original table, and ask the user about the numbers when it does not.
- (Numbers pasted in the conversation) Copy values and units as given into an input file and show the copied values in the input summary.
