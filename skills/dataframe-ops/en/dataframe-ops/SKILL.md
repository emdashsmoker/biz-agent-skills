---
name: dataframe-ops
description: "Turns plain-language or Excel-style cell reference (A1, B:D) requests about table data into pandas code, runs it, and shows the result table with the code that produced it. Covers loading CSV, Excel, JSON and Parquet files, filtering, sorting, group aggregation, missing values, duplicates, merging, saving, undo and checkpoints. Make sure to use this skill whenever the user asks things like 'filter this CSV', 'summarize this spreadsheet', 'average salary by department', 'average of column B', 'show A1:C5', 'remove duplicate rows', 'fill blanks with 0', 'do this with pandas', or uploads a table file and asks to clean, filter or summarize it. Command tables and natural-language mapping are in references/commands.md, runtime detection, virtual environments and version compatibility in references/environment.md, checkpoints, reproduction code and session recovery in references/session-files.md, and the helper functions in scripts/dataframe_ops.py."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# dataframe-ops

> This English edition is a translation of the Korean original. Some wording may not carry the original intent exactly, and the skill may behave differently from the Korean edition.

This skill turns plain-language or Excel-style cell reference requests about table data into pandas code and runs it. Show the code next to the result table. The shown code alone must reproduce the same result.

## Principles

- Show the pandas code you ran in every response. Users need to see where each result came from.
- Accept plain language, pandas code and Excel-style references. Treat a request that mixes all three as one command.
- Answer the same request in the same format. The format is defined under "Response format".
- Do every numeric calculation in Python code, even for questions unrelated to pandas. Never write down a sum, mean, ratio or row count you worked out yourself.
- Show only what the user asked for. Do not add unrequested information such as summary statistics.

## Helper script

`scripts/dataframe_ops.py` contains functions for coordinate conversion, table rendering, row windows, sensitive-data detection, checkpoints and environment checks. If you can run code, load it at the start of the session.

```python
import sys
sys.path.insert(0, "<this skill folder>/scripts")
import dataframe_ops as dfo
session = dfo.Session()
```

- Settings such as the default row count and page size are constants at the top of the file. They match the numbers in this document.
- Keep `dfo` functions out of the code you show the user. The user must be able to reproduce the result with pandas alone on their own machine. For cell references, show the `df.iloc[...]` code produced by `dfo.ref_to_code()`.
- If the script cannot be imported, read the file and follow the same rules by hand.

## Workflow

Handle each request in four steps.

| Step | What to do |
|---|---|
| Perceive | Decide whether the input is a plain-language command, pandas code or a file upload |
| Remember | Keep the main data `df`, the latest result `result`, the command history and the display settings for the whole session |
| Plan | Run a single command right away. Split a command with several actions into steps and run them in sequence. Ask first when a command is ambiguous |
| Act | Run the code, show the result table and record the command |

- Store the results of lookups, filters, sorts and aggregations in `result` and leave `df` unchanged.
- Change `df` only for commands with a clear intent to modify it, such as adding, deleting, renaming or replacing values. If the user looks at a result and says "use this instead", apply it with `df = result.copy()`.
- One executed code block counts as one command. After running it, call `session.record(code, modifies=...)`. Pass `modifies=True` when the code changed `df`. When the call returns True, save an automatic checkpoint.
- When you change `df`, reassign the result, as in `df = df.drop(...)`. pandas has announced the removal of `inplace=True` from many methods, so do not use that argument.

## Session start

Prepare in this order before the first response. The detailed procedure and message templates are in `references/environment.md`.

1. Find a place to run code. Check a built-in code runner, then a connected Python execution tool (an MCP server or similar), then an external code execution API. If none exists, switch to simulation mode.
2. If the code runs on the user's own computer, check for a virtual environment. Skip this step in a chat service's disposable code runner.
3. Check the installed pandas version. If a web search tool is available, read the official release notes for that version and for the latest stable version.
4. Show the start-up message.

When you receive `/env`, "check environment" or "detect environment again", start over from step 1.

## Reading commands

Decide the intent of a plain-language request first, then translate it into pandas code. The intents are load, save, view, filter, sort, group aggregation, modify, statistics, chart and help. Intent keywords and the full command tables are in `references/commands.md`.

Ask before running in these cases.

- No column name matches exactly, and two or more columns match part of the name. For example, if the data has only "age_group" and "age_band" and the user asks for "age", ask which column they mean.
- A condition has no threshold. Ask whether "the high ones" means "top 10" or "100 or more".
- A column name looks like a cell reference. If a column is named `A` or `B3`, ask whether the user means the reference or the column.

If no column matches at all, answer in the error format and suggest similar column names with `dfo.similar_columns()`.

## Coordinate rules

As in Excel, columns are letters and rows are numbers.

- Column letters follow the column order of `df`: A, B, ..., Z, AA, AB and so on.
- The first data row is row 1. The header row does not get a number, so A1 is the first data value in the first column.
- References always point at positions in the current `df`. After a row is deleted, the rows below it move up by one.
- Filtered or sorted result tables keep the row numbers and column letters of `df`. The user can then use a number seen in a result to point at a cell in `df`. `dfo.render(result, base=df)` numbers rows this way.
- Tables built by aggregation get no column letters, and their rows are numbered from 1 (`dfo.render(result)`). References only point at cells of `df`.
- "Average of column B", "average age" and "average of the age column" are the same command.
- Translate references into position-based `iloc` code. Delete rows by position too, as in `df.drop(df.index[2])`. References then stay correct even after earlier deletions make row labels differ from positions.

When you receive `/map`, "column map" or "show coordinates", show a table of letter, column name, data type and sample value (the first non-missing value) using `dfo.column_map_rows(df)`. Add one usage line under it, such as "B3 is the 3rd value of the age column".

## Response format

### Display modes

- Use `markdown` mode where Markdown tables render as tables, such as a chat window. This is the default.
- Use `ascii` mode where Markdown symbols show up as raw text, such as a terminal or raw API output.
- `/render auto` picks the mode based on the screen where the answer is displayed. The code often runs somewhere other than that screen, so do not decide from environment variables on the Python side.
- `/render` shows the current mode. `/render markdown` and `/render ascii` switch it.

### Responses that ran code

In markdown mode, write these five parts in this order.

| Order | Part | Content |
|---|---|---|
| 1 | Current state | Three bullets: environment, data size, column map |
| 2 | Code | A python code block. For a plain-language request, start with `# Input:` and `# Reading:` comments |
| 3 | Result | The result table and one completion line. The completion line says what was done and how many rows are shown out of the total |
| 4 | Main commands | The table below and one line of shortcuts |
| 5 | Status line | One line summarizing environment and data |

Use a code block only for the code. Tables break inside code blocks, so write the current state, result table, completion line, command table and status line as normal text.

Example:

**Current state**
- Environment: Python 3.11 | pandas 3.0.6
- Data: df (100 rows × 3 columns)
- Column map: A=name, B=age, C=dept

**Code**
```python
# Input: age 30 or more, sales only
# Reading: (column B >= 30) and (column C == 'Sales')
result = df[(df['age'] >= 30) & (df['dept'] == 'Sales')]
```

**Result**

|     | A(name) | B(age) | C(dept) |
|:---:|:---:|:---:|:---:|
| 1 | John Doe | 32 | Sales |
| 4 | Jane Doe | 35 | Sales |

Done: 2 of 100 rows selected

**Main commands**

| Plain language | pandas | Meaning |
|:---:|:---:|:---:|
| top N | `df.head(N)` | first N rows |
| select A1:C5 | `df.iloc[0:5, 0:3]` | cell range |
| average of column B | `df['column'].mean()` | column calculation |
| delete row 3 | `df.drop(df.index[2])` | remove a row |
| column map | `/map` | letters and column names |
| save | `df.to_csv('file.csv', index=False)` | save as CSV |

`/?` all commands | `/map` coordinates | `/env` environment | `/venv` virtual environment

venv:.dataframe_ops_env | Py 3.11 | pd 3.0.6 | df: 100×3 | changes: 0 | executable

Build the status line with these rules.

- The environment label at the start is one of `venv:name`, `conda:name`, `system Python (isolation advised)` or `built-in runner`.
- `changes` is the number of commands in this session that changed `df` (`session.change_count`).
- In simulation mode the status line is `simulation | reference: pandas version | code only`.
- Write numbers with thousands separators (`1,234×8`).

### ascii mode

Put all five parts in one code block and write each part's title in square brackets, such as `[Current state]`. Build tables with `dfo.render(..., mode="ascii")`. Columns stay aligned even with wide characters such as Korean or Chinese.

### Simulation mode

With no place to run code, write the code and show results only as examples.

- Write complete code, including `import pandas as pd` and the file loading line (with a comment telling the user to change the path).
- For requests that select rows, such as filters, sorts and top N, show an expected result table labeled "Expected result (simulation)". If the user gave no data, use a small example data set and say so.
- Do not show values that need calculation, such as sums, means or counts. Numbers produced without running code are not allowed.
- Under the result, write "Actual results depend on your data. Run the code above in a Python environment."

### Other responses

- (Partial success) Start with "Partly done", then list what succeeded, what failed with the cause, and a suggested fix.
- (Error) Give the error type, a one-line cause, where it happened, how to fix it and the current state of the data. For a column name error, show similar column names and the current column list, and ask "Did you mean age? (y/n)".
- (How-to questions) For a question such as "how do I use groupby?", show the basic syntax, two or three plain-language examples and one example with several aggregations. End with a sentence the user can try right away, such as "average salary by department".
- End every response with the main commands and the status line.

## How much to display

| Setting | Default |
|---|---|
| Default rows shown | 10 |
| Maximum rows in one table | 100 |
| Page size | 20 |
| Characters per cell | 30, longer text is cut with `...` |
| Row numbers | on |

- Show all rows when a result has 10 rows or fewer. Above 10 rows, switch to pages of 20 rows and state the position, such as "page 1/62, rows 1-20".
- When the user gives a row count ("just 50", `/h 50`), show that many rows, up to 100.
- When the user asks to see more than 100 rows at once, ask first. The options are the first 100 rows, everything anyway (printed in blocks of 100 rows), page view, or saving to CSV to check there. Recommend page view or CSV.
- Show missing values as `NaN`.
- Row window, paging and display setting commands are in `references/commands.md`.

## Data protection

### Backup and undo

- Right before a command changes `df`, keep a copy with `session.keep_backup(df)`.
- On "undo", "revert", "go back" or `/u`, restore the previous state with `df = session.undo()`.
- Undo goes back one step only. Restore older states from a checkpoint.

### Actions that need confirmation

For deletions where the user cannot know in advance how many rows will disappear, show the size before and after, then let the user choose "cancel" or "back up and run". This covers dropping rows with missing values, dropping duplicate rows, deleting rows that match a condition and deleting two or more columns at once. If the user picks "back up and run", save a `before_<operation>.pkl` checkpoint first.

When the user names a single target, as in "delete row 3" or "delete column B", treat the request itself as the confirmation and run it.

Ask before overwriting a file with the same name, installing packages, or creating or deleting a virtual environment.

### Sensitive data

After loading data, look for columns that seem to hold personal information with `dfo.find_sensitive_columns(df)`. It checks column names (national ID, passport, account, phone, email, address and similar) and value patterns (Korean resident registration numbers, US social security numbers, email addresses).

- If any are found, report the column names and the reason. Leave the actual values out of the warning.
- Suggest masking code (`df['national_id'] = df['national_id'].astype(str).str[:6] + '******'`) and deletion code (`df = df.drop(columns=['national_id'])`), then ask whether to continue.
- A checkpoint saved before masking or deletion keeps the original values in the file. Tell the user this before the first save and ask whether to save.

### Limits

- Ask before loading a file larger than 500 MB. The options are loading some rows (`nrows`), only the needed columns (`usecols`), processing in chunks (`chunksize`) or loading it as is. Also warn when `df` uses more than 500 MB of memory after loading (`dfo.frame_memory_mb(df)`).
- For code that runs a Python function row by row (`apply(axis=1)`, `iterrows`, `for` loops) on data with more than 1,000 rows, first estimate the run time with `dfo.estimate_seconds()`. If the estimate is over 5 seconds, report it and offer vectorized code that works on whole columns. Run the version the user picks.
- Read only files the user uploaded or pointed to by path. Do not use pandas to download data from web addresses.

## Loading files

- When a file arrives, read it by extension with `dfo.read_any(path)`. For CSV, TSV and TXT, it tries utf-8-sig and then cp949 (common in Korean Excel exports). Write the encoding that worked into the shown code.
- After loading, show the file name, sheet name (Excel), row and column counts, file size and the first 5 rows. If there are several sheets, add one line showing how to load another sheet, in words and in code.
- For a table inside an image, read the values into a table, show it, and create `df` only after the user confirms it matches the original.
- Extract PDF tables with `dfo.pdf_tables()` and Word tables with `dfo.docx_tables()`. If there are several tables, list them and let the user choose.
- Save an original snapshot checkpoint right after loading. Checkpoints, reproduction code and session recovery follow `references/session-files.md`.

## More features

- (Chaining) Write a request with several linked steps, such as "sales only, sorted by salary from high to low, top 10", as one method chain wrapped in parentheses.
- (Macros) On "save this task", store the code blocks run for the previous request under a numbered name such as `session.macros["macro_1"]` and summarize the contents in one line. Run it again with "run macro_1" or `/run macro_1`.
- (Profile) On "data profile" or "detailed analysis", show four parts from `dfo.profile(df)`: basic information (rows, columns, memory), a per-column table (type, missing count, unique count, most common value), numeric distributions (mean, median, standard deviation) and data quality (overall missing rate, duplicate row count).
- (History) On `/history` or "command history", show the last 10 commands as a table of number, time, code and a short result summary. "Run number 3 again" or `!3` reruns the code of command 3.

## Reference files

- `references/commands.md` holds the `/?` command tables, intent keywords, cell reference commands, row window and paging commands, display settings, file formats, save formats and chart commands.
- `references/environment.md` holds runtime detection, the virtual environment policy, package installation checks, version checks with the compatibility table, and the start-up messages.
- `references/session-files.md` holds when checkpoints are saved and how they are named, save and restore commands, recovery after context compression, session end handling and the reproduction code format.
- `scripts/dataframe_ops.py` is the set of functions that implements the rules in this document.
