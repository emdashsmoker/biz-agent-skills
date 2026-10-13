# Command reference

When the user types `/?` or "list commands", show the tables in this file. `column`, `value` and `path` in the tables are placeholders. Replace them with the real names from the user's data when running code.

## Load and save

| Plain language | pandas | Example |
|---|---|---|
| Load CSV | `pd.read_csv(path)` | "load sales.csv" |
| Load Excel | `pd.read_excel(path)` | "read report.xlsx" |
| Load JSON | `pd.read_json(path)` | "open data.json" |
| Save CSV | `df.to_csv(path, index=False)` | "save as result.csv" |
| Save Excel | `df.to_excel(path, index=False)` | "export to Excel" |

## Explore

| Plain language | pandas | Example |
|---|---|---|
| Show all | `df` | "print the whole table" |
| Top N | `df.head(N)` | "first 10" |
| Bottom N | `df.tail(N)` | "last 5" |
| Size | `df.shape` | "how many rows and columns" |
| Column list | `df.columns.tolist()` | "list the columns" |
| Data types | `df.dtypes` | "check types" |
| Summary statistics | `df.describe()` | "summary stats" |
| Missing value count | `df.isna().sum()` | "count blanks" |
| Unique values | `df[column].unique()` | "unique departments" |
| Value counts | `df[column].value_counts()` | "count by department" |

## Select and filter

| Plain language | pandas | Example |
|---|---|---|
| Select columns | `df[column]`, `df[[column1, column2]]` | "name column only" |
| Select a row | `df.iloc[position]` | "the 3rd row" |
| Filter | `df[df[column] > value]` | "age over 30" |
| Several conditions | `df[(condition1) & (condition2)]` | "age 30 or more and gender male" |
| Top N by value | `df.nlargest(N, column)` | "top 5 by revenue" |
| Bottom N by value | `df.nsmallest(N, column)` | "lowest 3 scores" |
| Random sample | `df.sample(N)` | "10 random rows" |

## Modify

| Plain language | pandas | Example |
|---|---|---|
| Add a column | `df[new_column] = value` | "add a total column" |
| Delete a column | `df = df.drop(columns=[column])` | "remove the address column" |
| Delete a row | `df = df.drop(df.index[position])` | "delete row 1" |
| Rename a column | `df = df.rename(columns={old: new})` | "rename name to full_name" |
| Replace values | `df = df.replace(old, new)` | "change M to male" |
| Fill missing values | `df = df.fillna(value)` | "fill blanks with 0" |
| Drop rows with missing values | `df = df.dropna()` | "remove rows with blanks" |
| Drop duplicate rows | `df = df.drop_duplicates()` | "remove duplicate rows" |
| Change type | `df[column] = df[column].astype(type)` | "make age an integer" |

## Sort and aggregate

| Plain language | pandas | Example |
|---|---|---|
| Sort ascending | `df.sort_values(column)` | "sort by name" |
| Sort descending | `df.sort_values(column, ascending=False)` | "highest revenue first" |
| Group aggregation | `df.groupby(column)[value_column].agg(function)` | "average salary by department" |
| Pivot table | `df.pivot_table(index=column, columns=column, values=column, aggfunc=function)` | "revenue pivot by year and month" |
| Sum | `df[column].sum()` | "total revenue" |
| Mean | `df[column].mean()` | "average age" |
| Max, min | `df[column].max()`, `df[column].min()` | "highest score" |
| Count | `df[column].count()` | "number of valid entries" |

In group aggregation, select the columns to aggregate first. Since pandas 2.0, `df.groupby(column).mean()` without a column selection raises an error when text columns are present. To aggregate every numeric column, use `df.groupby(column).mean(numeric_only=True)`.

## Combine

| Plain language | pandas | Example |
|---|---|---|
| Stack vertically | `pd.concat([df1, df2], ignore_index=True)` | "append the two tables" |
| Join on a key | `pd.merge(df1, df2, on=key)` | "join on ID" |
| Left join | `pd.merge(df1, df2, on=key, how='left')` | "merge keeping all left rows" |

## Charts

Charts need matplotlib. If it is not installed, ask before installing it.

| Plain language | Code | Example |
|---|---|---|
| Line chart | `df.plot()` | "trend chart" |
| Bar chart | `df.plot.bar()` | "bar chart" |
| Histogram | `df[column].hist()` | "distribution" |
| Scatter plot | `df.plot.scatter(x=column, y=column)` | "scatter of X and Y" |
| Correlation | `df.corr(numeric_only=True)` drawn as a heatmap | "correlation heatmap" |

## Intent keywords

Decide the intent of a plain-language request from these keywords. When keywords point to several intents, check for a modify intent first. With a modify intent, change `df`. Without one, store the outcome in `result`.

| Intent | Keywords |
|---|---|
| Load | load, read, open, import, bring in |
| Save | save, export, write, download |
| View | show, display, print, see, check |
| Filter | filter, where, only, at least, at most, over, under, equal to |
| Sort | sort, order, rank, highest first, lowest first |
| Group aggregation | group, by, per, aggregate, summarize by |
| Modify | edit, change, add, delete, remove, rename, replace, update |
| Statistics | statistics, average, mean, total, sum, max, min, count |
| Chart | chart, graph, plot, visualize |
| Help | help, commands, how do I, how to, ? |

| Input | Reading | Code |
|---|---|---|
| "age 30 or more only" | filter | `result = df[df['age'] >= 30]` |
| "average salary by department" | group aggregation | `result = df.groupby('dept')['salary'].mean()` |
| "sort by name" | sort | `result = df.sort_values('name')` |
| "top 5 by revenue" | sort and top N | `result = df.nlargest(5, 'revenue')` |
| "delete the gender column" | modify | `df = df.drop(columns=['gender'])` |

## Cell reference commands

Row 1 is the first data row and column letters start at A. Build the code with `dfo.ref_to_code()`.

| Input | Meaning | pandas |
|---|---|---|
| "value of A1" | one cell | `df.iloc[0, 0]` |
| "set B3 to 100" | edit one cell | `df.iloc[2, 1] = 100` |
| "clear C5" | empty one cell | `df.iloc[4, 2] = None` |
| "A1:C3" | cell range | `df.iloc[0:3, 0:3]` |
| "all of column A", `A:A` | one column | `df.iloc[:, 0]` |
| "all of row 3", `3:3` | one row | `df.iloc[2, :]` |
| "columns B to D", `B:D` | several columns | `df.iloc[:, 1:4]` |
| "rows 2 to 5", `2:5` | several rows | `df.iloc[1:5, :]` |
| "only columns A, C and E" | separate columns | `df.iloc[:, [0, 2, 4]]` |
| "delete column B" | delete a column | `df = df.drop(columns=df.columns[1])` |
| "delete row 3" | delete a row | `df = df.drop(df.index[2])` |
| "new column at position D" | add a column at a position | `df.insert(3, 'new', value)` |
| "add after column A" | add a column at a position | `df.insert(1, 'new', value)` |

`df.insert` changes `df` in place, so do not reassign its return value.

## Row windows and pages

All row numbers start at 1 and include both ends.

| Command | Plain-language example | Action | Function |
|---|---|---|---|
| `/h N` | "first 30" | top N rows, 5 when N is missing | `df.head(N)` |
| `/t N` | "last 20" | bottom N rows, 5 when N is missing | `df.tail(N)` |
| `/all` | "show everything" | all rows, ask first above 100 rows | |
| `/range 10 30` | "rows 10 to 30", "rows 10-30" | rows 10-30 | `dfo.rows_between(n, 10, 30)` |
| `/mid 20` | "show the middle part" | the middle 20 rows | `dfo.rows_mid(n, 20)` |
| | "around row 50" | rows 40-60 | `dfo.rows_near(n, 50)` |
| `/next`, `n` | "next" | next page | `dfo.page_rows(n, page)` |
| `/prev`, `p` | "previous" | previous page | |
| `/page 5` | "page 5" | page 5 | |
| `/page first`, `/page last` | "first page", "last page" | first or last page | |
| `/pagesize N` | | change the page size | |

In page view, write "page 1/62, rows 1-20" above the table and one line on how to move between pages below it.

## Display settings

| Command | Action |
|---|---|
| `/rows` | show the current display settings |
| `/rows N` | set the default row count to N, capped at 100 |
| `/rows all` | set the default row count to 100 |
| `/rows reset` | restore the default of 10 rows |

`/rows` shows a table of the default row count, maximum rows, page size, current page, characters per cell and whether row numbers are shown.

## Shortcuts

| Command | Function |
|---|---|
| `/?` | all commands |
| `/env` | check and re-detect the runtime |
| `/venv` | virtual environment status and management |
| `/render` | check or change the display mode |
| `/rows` | display row settings |
| `/map` | letter and column name map |
| `/h`, `/t` | top or bottom rows |
| `/i` | data information, `df.info()` |
| `/d` | summary statistics, `df.describe()` |
| `/c` | column list |
| `/s` | save format menu |
| `/u` | undo |
| `/history` | command history |
| `/run name` | run a macro |
| `/save`, `/load`, `/checkpoints` | save, restore and list checkpoints |
| `/reset` | reset the session, confirm before clearing `df` and the history |

## File formats

| Kind | Extension | How to read | Extra package |
|---|---|---|---|
| Spreadsheet | .csv | `pd.read_csv(path, encoding=encoding)` | none |
| | .xlsx, .xlsm | `pd.read_excel(path, sheet_name=sheet)` | openpyxl |
| | .xls | `pd.read_excel(path)` | xlrd |
| | .ods | `pd.read_excel(path)` | odfpy |
| Text | .tsv | `pd.read_csv(path, sep='\t')` | none |
| | .txt | `pd.read_csv(path, sep=None, engine='python')` detects the separator | none |
| JSON | .json | `pd.read_json(path)` | none |
| Parquet | .parquet | `pd.read_parquet(path)` | pyarrow |
| Image | .png, .jpg | read the table from the image, confirm with the user, then `pd.DataFrame` | none |
| PDF | .pdf | `dfo.pdf_tables(path)`, or tabula-py if Java is installed | pdfplumber |
| Word | .docx | `dfo.docx_tables(path)` | python-docx |

Ask before installing an extra package the first time a format needs it.

## Save formats

| Plain language | pandas | Format |
|---|---|---|
| "save as CSV" | `df.to_csv('output.csv', index=False)` | .csv |
| "save as Excel" | `df.to_excel('output.xlsx', index=False)` | .xlsx |
| "save as JSON" | `df.to_json('output.json', orient='records')` | .json |
| "save as Markdown" | `df.to_markdown('output.md')`, needs tabulate | .md |
| "copy to clipboard" | `df.to_clipboard()` | desktop with a screen only, and Linux needs xclip or xsel |

After saving, report the file name, location and row and column counts. If the environment can hand files to the user, provide the file for download. End with one suggestion for another format, such as "save as CSV too".
