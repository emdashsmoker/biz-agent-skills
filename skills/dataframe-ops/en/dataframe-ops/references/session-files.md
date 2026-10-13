# Session files

A checkpoint saves `df` and the command history to a file. Work can continue even after early parts of a long conversation are summarized or the code runner restarts. Save files under `dataframe_ops_checkpoints/` in the working folder.

## When to save

| Moment | Contents | File name |
|---|---|---|
| Every 5 commands (when `session.record()` returns True) | current state | `checkpoint_<date>_<time>.pkl` |
| Right after loading data | original snapshot | `original_<file name>.pkl` |
| Right after the user picks "back up and run" for a deletion that needs confirmation | state before running | `before_<operation>.pkl` |
| When the user types `/save name` | current state | `save_<name>.pkl` |
| At session end, when the user picks "yes" | state and reproduction code | `session_<date>.zip` |

- Date and time use the `YYYYMMDD_HHMMSS` format returned by `dfo.timestamp()`.
- The operation name is the pandas method about to run, such as `dropna` or `drop_duplicates`.
- Keep a copy of the loaded original in `df_original` and include it in every checkpoint.
- If sensitive columns have not been masked or deleted yet, ask the user before the first save (see the sensitive data section of SKILL.md).

## Checkpoint contents

`session.save_checkpoint({'df': df, 'df_original': df_original, 'result': result}, file_name)` writes these items into one pickle file.

| Item | Contents |
|---|---|
| timestamp | time of saving |
| environment | Python version, pandas version, virtual environment name |
| dataframes | `df`, `df_original`, `result` |
| column_map | letters and column names |
| history | every command run in the session, with times |
| macros | saved macros |
| command_count | number of commands run |
| change_count | number of commands that changed `df` |
| full_code | the full reproduction code |

The full history is saved so that reproduction code from the very first step can still be built after a restore.

## Save and restore commands

| Command | Action |
|---|---|
| `/save` | save the current state as `save_<date>_<time>.pkl` |
| `/save name` | save the current state as `save_<name>.pkl` |
| `/save code` | export the reproduction code as `dataframe_ops_session.py` (`session.export_code()`) |
| `/save all` | save a checkpoint and the reproduction code in one zip file (`session.save_all()`) |
| `/load`, `/checkpoints` | list saved files, newest first (`session.list_checkpoints()`) |
| `/load file_name` | restore `df`, `df_original`, `result`, the history and macros from that point |

`session.load_checkpoint()` opens only .pkl files inside the checkpoint folder. Opening a pickle file can run code stored in it, so files of unknown origin are never opened.

After saving, report it like this. If the environment can hand files to the user, provide the file for download.

> Checkpoint saved.
> - File: checkpoint_20260930_143522.pkl
> - Location: ./dataframe_ops_checkpoints/
> - Contents: DataFrame 150 rows × 5 columns, 15 commands in history, column map A=name, B=age, C=dept, D=salary, E=start_date
> - Restore with `/load checkpoint_20260930_143522.pkl`, export code with `/save code`

## Recovery after context compression

Treat earlier work as lost and show the recovery message when either of these is true.

- `df` or `session` no longer exists in the Python runner. This means the runner restarted.
- Early parts of the conversation were replaced by a summary, and earlier code or results are no longer visible.

If the runner restarted, create a new `dfo.Session()` and read the files on disk with `list_checkpoints()`.

> Part of the earlier work was summarized and is no longer visible.
> Three ways to recover: check saved files with `/checkpoints`, restore a point with `/load file_name`, or export the code so far with `/save code`.
> Recent checkpoints
> - checkpoint_20260930_143522.pkl (5 minutes ago)
> - checkpoint_20260930_142815.pkl (12 minutes ago)
>
> Which point should be restored?

## Session end

When the user says they are finished, with words such as "done", "quit", "stop", "wrap up" or "that's all for today", ask about saving.

> Save your work?
> 1. "Yes": save `df`, the reproduction code and the full history (`session_<date>.zip`)
> 2. "Code only": save only the reproduction code
> 3. "No": finish without saving
>
> Automatic checkpoints saved so far: [count]. The newest is [file name].

## Reproduction code

When the user asks for "all the code", "reproduction code" or `/save code`, build the session's full code with `session.full_code()`. The first lines are comments with the creation time and the Python and pandas versions. After them come all executed commands in order, each with its number and time.

In simulation mode, or when the user asks for the code of a single task, use this template. Copy the encoding or sheet name used to read the file.

```python
# dataframe-ops reproduction code
# Created: [YYYY-MM-DD HH:MM:SS]
# Environment: Python [x.y] / pandas [x.y.z]

import pandas as pd

# 1. Load the data (change to your real file path)
df = pd.read_csv('data.csv')

# 2. Check what was loaded
print(f"Original data: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Columns: {df.columns.tolist()}")

# 3. Task: age 30 or more, sales only
result = df[(df['age'] >= 30) & (df['dept'] == 'Sales')]

# 4. Check the result
print(f"Result: {result.shape[0]} rows × {result.shape[1]} columns")
print(result)

# 5. Save (uncomment if needed)
# result.to_csv('result.csv', index=False)
```
