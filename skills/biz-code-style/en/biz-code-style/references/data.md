# Data analysis

Check the shape and quality of the data first, write down a hypothesis, then calculate. Run every calculation in code and keep the code and environment information so others get the same result. Examples use pandas, and the same principles apply to other tools.

## Checking the runtime

- At the start of work, check for a way to run code in this order: the session's built-in interpreter, a connected external execution tool (such as a Python execution server), then an external code execution API.
- If a way to run code exists, check the versions of Python and key packages (such as pandas) in code and record them.
- If no way to run code exists, only write code. Do not invent results as tables or numbers that were never executed. Provide the full runnable code and state that results are confirmed only after running it.
- Package installation and virtual environment rules follow code.md.

## Version compatibility

- Write code that works in the installed version.
- If the user allowed web search, check the release notes of the installed version (for pandas, https://pandas.pydata.org/docs/whatsnew/) for added features, deprecations, and known issues.
- Without web search, run with warnings shown (for example `python -W default`), check DeprecationWarning and FutureWarning, and switch to the replacement code.
- If the user asks for a feature removed in the installed version, offer replacement code and ask whether to run it. For example, `DataFrame.append`, removed in pandas 2.0, becomes `pd.concat`.
- Account for behavior that changes by version. From pandas 3.0, Copy-on-Write is the default, so chained assignment (`df[col][row] = value`) does not change the original. Use `df.loc[row, col] = value` to change values. From the same version, the default dtype for string columns changed from `object` to `str`.
- Prefer the basic APIs present in every pandas version since 1.0 (read_csv, read_excel, read_json, head, tail, shape, columns, dtypes, info, describe, loc, iloc, drop, rename, fillna, dropna, replace, sort_values, groupby, agg, pivot_table, concat, merge, to_csv, to_excel, to_json). (recommended)

## Turning requests into code

- First classify the request as load, save, view, filter, sort, group and aggregate, modify, statistics, or visualize.
- Split requests that chain several operations into steps. Method chaining can join them.
- Leave the original request and the interpreted conditions in a comment above the code.
- If a request is ambiguous, ask a clarifying question. Cases include several columns that could match a name, or a vague criterion such as "the high ones". Offer concrete criteria to choose from, such as "top 10" or "100 or more".

```python
# Request: age 30 or older, sales department only
# Interpretation: (age >= 30) AND (dept == "Sales")
result = df[(df["age"] >= 30) & (df["dept"] == "Sales")]
```

| Request | Interpretation | Code |
|---------|----------------|------|
| Only age 30 and up | Filter | `df[df["age"] >= 30]` |
| Average salary by department | Group and aggregate | `df.groupby("dept")["salary"].mean()` |
| Sort by name | Ascending sort | `df.sort_values("name")` |
| Top 5 by revenue | Descending top N | `df.nlargest(5, "revenue")` |
| Delete the gender column | Drop column | `df = df.drop(columns="gender")` |

## Loading and saving

- Load with the function that matches the format. Use `read_csv` for csv, `read_excel` for xlsx, xls, and ods, `read_csv` with a separator for tsv and txt, `read_json` for json, and `read_parquet` for parquet.
- Use OCR results for tables in images, and extraction results for tables in PDF and docx files, only after the user confirms them.
- For Excel files, load the first sheet and tell the user the list of sheets if there are others.
- Right after loading, check the row count, column count, file size, and the first 5 rows.
- Save in the requested format (csv, xlsx, json, md, and so on) and report the file name, location, and number of rows and columns.

## Exploration and quality checks

- Before writing analysis code, check the shape of the data (row and column counts, column types).
- Check quality problems such as missing values, duplicates, and outliers first. Do this with check code that runs against the actual data (assert and similar) and record whether it passed.
- Write the hypothesis before calculating. Do not fit the hypothesis to the result after seeing it.
- When asked for a data overview, show row and column counts, memory use, column types, missing counts, unique counts, modes, mean, median, and standard deviation of numeric columns, the overall missing rate, and the number of duplicate rows.

## Showing results

- Show only the result the user asked for. Do not add unrequested information such as summary statistics.
- Show up to 10 rows of a result table by default, or the number of rows the user specifies.
- For a request to print more than 100 rows in full, offer the choices of printing the top 100 rows, printing everything, or saving to a file.
- Truncate long text columns at 30 characters for display. (recommended)
- On screens that render Markdown, show results as Markdown tables and do not put tables inside code blocks. In terminals that do not render Markdown, show a text table with aligned character widths.
- Keep the response short, in this order: current data state (data name, row and column counts), executed code, execution result, and a processing summary (for example, filtered from 100 rows to 2).

## Changing and protecting data

- Before an operation that changes data, keep a copy of the original (`df.copy()`) so it can be undone.
- For operations that shrink data a lot, such as dropping many columns, show the size before and after and run only after the user confirms.
- If a column can identify individuals, such as a national ID number, propose masking (for example keeping only the first 6 digits) or dropping the column, and get confirmation.
- When an error occurs, report the cause, the location, and how to fix it. If the cause is a column name that does not exist, show similar column names and the current column list.

## Reproduction code

- When the user asks, or when no way to run code exists, provide the full runnable code from loading to saving.
- In the header comment of the full code, record the creation time and the runtime environment (Python and key package versions).
- For operations with randomness, such as sampling, data splitting, and model training, declare the random seed as a constant at the top of the code and pass it to every random function.

## Statistical inference

- Do not treat correlation as causation.
- Do not generalize without considering sample size and representativeness.
- Do not use the absence of information as evidence of absence. Mark unconfirmed items as unconfirmed.
- Separate confirmed facts from inferences, and label inferences as inferences.

## Large data

For data that does not fit in memory at once, read less, use efficient types, and process in parts.

- Read only the needed columns (`usecols` for csv, `columns` for parquet).
- Convert string columns with many repeated values to the `category` type, and shrink numeric columns with `pd.to_numeric(..., downcast=...)`.
- Aggregate by file or by chunk, then combine the results.
- For larger scales, consider parallel or distributed libraries compatible with pandas. (recommended)
- Do not have the model read the raw data in full. Check only the results aggregated in code.

## Modeling and machine learning

Prevent leakage that makes evaluation scores look better than reality, and make the same run produce the same result.

- Split the data into training and evaluation sets first, and preprocess after that.
- Fit preprocessing such as imputation, scaling, and feature selection on the training data only. Apply only transform to the evaluation data.
- Bundle preprocessing and the model into one pipeline to prevent missed preprocessing steps and leakage.
- Never fit on the evaluation data.
- Relationships between entities (1:1, 1:N, N:M) and the distinction between kind-of, part-of, and attribute relationships follow structure.md.

## Checklist

- Did you calculate every number in code?
- Did you avoid presenting unexecuted results as results?
- Did you run the data quality check code?
- Did you keep a copy before changing data?
- Did you check for personally identifying information?
- Did you record the random seed and runtime versions?
