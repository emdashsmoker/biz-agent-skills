# plan.json format and file export

One plan.json is the source for the overview, CSV and XLSX. Editing each file separately makes dates and numbers drift apart, so always edit plan.json and export again. A full example is in `assets/plan_example.json`.

## project

| Field | Required | Meaning |
|---|---|---|
| name | yes | Project name |
| start, end | yes | Contract start and end dates, YYYY-MM-DD |
| buffer_ratio | no | Buffer target ratio. Default 0.15 |
| max_task_days | no | Maximum days for one work row. Default 28 |
| baseline_last_end | no | Last work end date of the original plan. Used to compute buffer used |

## options

| Field | Default | Meaning |
|---|---|---|
| mm | true | Staffing table and M/M checks |
| raci | false | RACI columns on work rows and their checks |

## people

| Field | Meaning |
|---|---|
| id | Identifier used in task owner and raci (e.g. P1) |
| name, role | Name and role shown in the tables |
| rate | Allocation (0.5 means 50%) |
| months | Months on the project |
| contract_mm | M/M in the contract documents. If missing, rate × months |
| mm | Monthly M/M, e.g. {"2026-03": 0.5, "2026-04": 0.4} |

## tasks

| Field | Required | Meaning |
|---|---|---|
| stage | yes | Stage name |
| name | yes | Task name |
| type | yes | work, wait, check (checkpoint), buffer |
| start, end | yes | YYYY-MM-DD. If a date is unknown, enter an assumed date and write `[To confirm: date]` in note |
| owner | yes for work and check | A people id, or plain text such as an agency name |
| output | yes for work and check | Deliverable (done when) |
| status | no | planned, doing, done. Default planned |
| note | no | Notes, such as the standard phrases uncertain result, depends on one person, deadline critical, with the response |
| event | no | kickoff, interim_report, final_report, advisory, hearing, other. Used for event spacing checks |
| allow_long | no | true turns off the long row warning. Use it for monthly recurring management work |
| raci | no | {"P1": "A", "P2": "R"} |

- Rows appear in the order of tasks. Keep rows of the same stage together
- Rows with the same stage name form one stage

## overview

| Field | Format | Place in the overview |
|---|---|---|
| summary | [["Client", "Agency name"], ["Contract type", "Service contract"]] | Extra lines in Basic Information |
| beneficiary | list of sentences | Beneficiaries under Why |
| needs | list of sentences | Needs and problems under Why |
| goals | list of sentences | Project Goals |
| hypotheses | [{"statement": "hypothesis", "solutions": ["solution"]}] | Hypotheses & Solutions |
| success | list of sentences, three or fewer | Success Criteria |
| notes | list of sentences | Notes |

## Checks

`plan.py check` prints errors and warnings separately. With any error, no file is written.

| Kind | Items |
|---|---|
| Error | Missing required field, date format, end before start, allowed values of type, status and event |
| Warning | Dates outside the contract period, missing owner or completion criterion, long work row, buffer below target, no buffer row, buffer used above progress, advisory meeting and hearing spacing, four or more success criteria, M/M total mismatch, monthly M/M above 1.0, RACI without exactly one A |

## File formats

| File | Command | Contents |
|---|---|---|
| Overview MD | `plan.py md plan.json -o overview.md` | All overview sections, WBS detail table, staffing table |
| CSV | `plan.py csv plan.json -o wbs.csv` | One WBS table. With M/M on, also wbs_mm.csv. UTF-8 with BOM |
| XLSX | `plan.py xlsx plan.json -o wbs.xlsx` | WBS sheet, plus a staffing sheet when M/M is on |
| PDF | `md2pdf.py overview.md -o overview.pdf` | Portrait pages, with landscape pages for sections holding tables of 9 or more columns |

XLSX formatting

- Black text, thin borders, gray header fill only (D9D9D9). The row above the Gantt header uses merged cells on a white background. No other colors and no conditional formatting
- Gantt cells are formulas. Changing a start or end date moves the marks
- Gantt marks: ■ work, ○ wait, ● checkpoint, □ buffer
- Projects of about 7 months (30 weeks) or less get weekly columns. The row above the header merges the weeks of each month under a label such as "Mar 2026", and the header shows the Monday date of each week
- Longer projects get monthly columns. The row above the header merges the months of each year under a label such as "2026", and the header shows the month, such as "Mar"
- Total and difference columns on the staffing sheet are formulas. A nonzero difference means the allocation does not match the contract M/M

## Korean labels

The scripts use Korean labels with `--lang ko`. The default language is DEFAULT_LANG at the top of `scripts/plan.py`.
