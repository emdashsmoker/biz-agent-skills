# Runtime environment

## Detection order

At the start of a session, look for a place to run code in this order. Stop at the first one found.

1. Test whether `import pandas` works in the built-in code runner. If it does, read the Python version, pandas version, virtual environment status and installed extra packages with `dfo.env_report()`.
2. Look for a Python or Anaconda execution tool (an MCP server or similar) among the connected tools. If one exists, run the same check through it.
3. If an external code execution API is registered, run the same check there.
4. If nothing is found, switch to simulation mode.

The `/env` response shows whether each option (built-in runner, Python execution tool, external API) was found, plus the type of the environment in use, its Python version, its pandas version and whether code can run.

## Virtual environments

Apply this section only when code runs on the user's own computer. A chat service's disposable code runner disappears when the session ends, so skip this procedure there.

### Principles

- Do not install packages directly into the system Python or the conda base environment. Other programs may depend on the package versions there.
- Work inside a virtual environment dedicated to this skill.
- If a dedicated environment already exists, reuse it.

### Finding and choosing

Check with `dfo.env_report()` whether you are already inside a virtual environment. If `isolated` is True, work there and show message 4 below. Otherwise, look for existing environments with `dfo.find_environments()`. It searches these places.

- venv folders: `~/.dataframe_ops_env`, `~/dataframe_ops_env`, `./.dataframe_ops_env`, `./dataframe_ops_env`, `./.venv`, `./venv`
- conda environments whose name contains `dataframe_ops` or `dataframe-ops`
- The last-used time is taken from the environment folder's modification time.

Show message 1, 2 or 3 depending on how many environments were found. `dfo.recommend_environment()` recommends the environment with the highest pandas version. Among equal versions, it picks the most recently used one.

Message 1, several environments found

> Virtual environments found.
>
> | No. | Type | Name or path | Python | pandas | Last used |
> |---|---|---|---|---|---|
> | 1 | venv | ~/.dataframe_ops_env | 3.11.9 | 2.3.3 | 2026-05-02 |
> | 2 | conda | dataframe_ops | 3.12.4 | 3.0.6 | 2026-09-20 |
>
> Enter the number to use. "Create new" makes a new environment. "Skip" uses the system Python (not recommended).
> Recommended: 2 (highest pandas version)

Message 2, one environment found

> Found an existing virtual environment. (venv, ~/.dataframe_ops_env, Python 3.11.9, pandas 2.3.3, last used 2026-05-02)
> Use it? "Yes" uses this environment, "Create new" makes a new one, "Skip" uses the system Python (not recommended).

Message 3, none found

> There is no virtual environment for this skill yet. A dedicated environment prevents package conflicts, so creating one is recommended.
> "Yes" creates a venv at `~/.dataframe_ops_env`, "conda" creates the conda environment `dataframe_ops`, "Skip" uses the system Python (use with care).
> The new environment gets only pandas and openpyxl. Other packages are installed when needed, after asking.

Message 4, already inside a virtual environment

> Working inside a virtual environment. (conda, dataframe_ops, Python 3.12.4, pandas 3.0.6)

### Creating

- Create a venv with `dfo.create_venv()`. It builds the environment with the current Python, upgrades pip, then installs pandas and openpyxl from PyPI.
- Create a conda environment with `dfo.create_conda_env()`. It uses only the conda-forge channel, because Anaconda's default channel may require a paid license for larger organizations.
- pandas 3.x needs Python 3.11 or newer. If the system Python is 3.10 or older, recommend a conda environment or offer pandas 2.x.
- Before creating anything, show the location and the packages to install, and get the user's agreement.

### Virtual environment commands

| Command | Action |
|---|---|
| `/venv` | current environment details |
| `/venv list` | environments found |
| `/venv create` | create a new environment, choosing venv or conda |
| `/venv activate name` | switch to another environment |
| `/venv install package` | install a package in the current environment |
| `/venv delete name` | delete an environment after showing its path and getting confirmation |

### Package installation checks

When the user asks to install something, as in "install seaborn", check the current environment first.

- Inside a virtual environment, show the install command (`pip install seaborn`) and install it.
- On the system Python, warn and offer three choices: "create an environment, then install" (recommended), "install anyway" and "cancel".
- When a feature of this skill needs an extra package (for example xlrd to open an .xls file), say which feature needs it and ask before installing.

## Version check

Once the environment is settled, base your guidance on the installed pandas version.

- If a web search or web page reading tool is available, check the official sources. The release notes for the installed version are at `https://pandas.pydata.org/docs/whatsnew/v<version>.html` (for example v3.0.6.html). The latest stable version is at the top of `https://pandas.pydata.org/docs/whatsnew/index.html` or in `info.version` of `https://pypi.org/pypi/pandas/json`.
- Summarize the release notes in two or three lines: new features, deprecations, removals and known issues.
- If the installed and latest versions share the same minor version (the first two numbers, as in 3.0.x) and only the last number is lower, recommend upgrading. Patch releases mostly fix bugs.
- If the first two numbers differ, existing code may behave differently. Explain the differences and let the user decide whether to upgrade.
- Without web tools, report the installed version and the official addresses above. If simulation mode cannot find the latest version, write the reference version as "unknown".

## Compatibility check

Before running code, check it against this table. On a match, show a warning with the alternative code and ask whether to run the alternative.

| Target | Change by version | Alternative |
|---|---|---|
| `DataFrame.append`, `Series.append` | removed in 2.0.0 | `pd.concat([df, df2], ignore_index=True)` |
| group aggregation without selecting columns, `df.groupby(column).mean()` | errors on text columns since 2.0.0 | select the columns first, or `numeric_only=True` |
| `DataFrame.applymap` | deprecated in 2.1.0, removed in 3.0.0 | `DataFrame.map` |
| `Series.case_when` | added in 2.2.0 | `numpy.select` before 2.2.0 |
| chained assignment `df['column'][0] = value` | no longer changes the value since 3.0.0 | `df.loc[0, 'column'] = value` |
| dtype of text columns | default is `str` since 3.0.0, `object` before | compare with `pd.api.types.is_string_dtype(df[column])` |
| `pd.options.mode.copy_on_write` | no effect since 3.0.0, to be removed in 4.0 | do not set it on 3.x |
| `inplace=True` | scheduled for removal from `drop`, `dropna`, `rename`, `sort_values` and others under PDEP-8 | reassign, as in `df = df.drop(...)` |

Loading (`read_csv`, `read_excel`, `read_json`), basic exploration (`head`, `tail`, `shape`, `columns`, `dtypes`, `info`, `describe`), selection (`df[column]`, `loc`, `iloc`), modification (`drop`, `rename`, `fillna`, `dropna`, `replace`), sorting and aggregation (`sort_values`, `groupby`, `agg`, `pivot_table`), combining (`concat`, `merge`) and saving (`to_csv`, `to_excel`, `to_json`) exist under the same names in every version since pandas 1.0. Changes in their details follow the table above.

Example warning

> Version compatibility warning
> This environment runs pandas 3.0.6. `DataFrame.append()` was removed in pandas 2.0.
> The alternative is `result = pd.concat([df, df2], ignore_index=True)`. Run this instead? (y/n)

pandas 2.x users who want to try 3.0 behavior early can set these two options. Neither is needed on 3.x.

```python
pd.options.mode.copy_on_write = True    # 2.0 or newer
pd.options.future.infer_string = True   # 2.1 or newer
```

## Start-up message

Fill in this template for the first response. Replace the brackets with real values and omit lines that do not apply.

With a place to run code

> **dataframe-ops ready**
>
> - Runtime: [built-in runner, Python execution tool or external API], [virtual environment name or system Python]
> - Versions: Python [x.y.z], pandas [x.y.z], code can run
> - Notes for this version: [one or two lines from the release notes]
> - Latest stable version: [version], upgrade recommended: [yes or no, with the reason]
> - Display mode: [markdown or ascii], change with `/render markdown` or `/render ascii`
> - Coordinates: A1 is the first data value in the first column (the header row has no number)
>
> Ways to start
> 1. Upload a CSV, Excel or JSON file
> 2. Type code, for example `df = pd.DataFrame({'A': [1, 2, 3]})`
> 3. Type "create example data"
>
> For help, type `/?` or "list commands"

Without a place to run code (simulation mode)

> **dataframe-ops ready (simulation mode)**
>
> - No environment to run Python and pandas was found. Code will be written for you and results shown only as examples.
> - Reference version: pandas [latest stable version or unknown], recommended Python [version]
> - Main features of the latest version: [two or three lines]
> - To run code for real, turn on the code execution feature of your AI service or connect a Python execution tool.
>
> Ways to start
> 1. Paste data as a Markdown table or JSON
> 2. Ask for code, for example "code to read a CSV"
> 3. Type "start with example data"
>
> For help, type `/?` or "list commands"

On "create example data", build a fictional data set of 5-10 rows with name, age, dept and salary columns in code. Use common placeholder names such as John Doe and Jane Doe, and avoid names that could be mistaken for real people.
