# Writing always-on instructions

Always-on instructions sit at the front of every conversation. So shorter is better, and the most important rule must come first. The basis is research showing that adherence drops as instructions increase and that earlier instructions are followed better.

## What goes in

Put only the items below in the always-on instructions, in this order.

1. Module loading rule
2. Common work rules (rules turned on in interview F1-F7)
3. Short preferences for every output (interview F8, only if any)

Rules that depend on the kind of task stay out of the always-on instructions and go into the matching module. For example, chart color rules go into code-standard, and the citation format goes into write-standard.

## Writing principles

- Attach a short reason to each rule. With a reason, the model judges new situations by the rule's purpose.
- Do not use all-caps emphasis or heavy wording such as "never" or "no exceptions." Recent models can overreact to strong wording and apply a rule to unrelated tasks.
- Write what to do rather than what not to do.
- Write each module name exactly as the folder name to be installed, down to every character.
- State that the module loading rule applies to short questions too. Models tend to skip loading skills when a question is short.

If the user reports that the model keeps skipping module loading, move the loading rule further forward and add the sentence "The first action of every response is loading the module." If it still skips, agree with the user on stronger wording.

## Template

Rewrite the template below in the user's output language. Replace the bracketed parts with interview answers and delete lines for modules that will not be installed.

```
# Module loading

Before starting a response, load the matching standard module first. The standard modules hold the standards for writing and code, so skipping them makes the output miss those standards. Apply this even when the question is short or simple.

- For requests involving code, charts, UI, data visualization, or file operations, load code-standard.
- For every other request (writing, research, everyday search, and so on), load write-standard.
- For requests that span both, load both.

After loading the standard module, judge the size of the task.

- For complex work that spans several steps, files, or sources, also load staged-work.
- For token-heavy work such as bulk parsing, mass research, many tool calls, long outputs, or repetitive file operations, also load token-lean.

Follow the rules of loaded modules to the end. Load the standard modules even when the user names another skill. Skip a module only when the user explicitly says not to use it.

# Common work rules

- [Rules turned on in F1-F7, one per line with a reason]

# Other preferences

- [Answer to F8; delete this section if none]
```

If only one standard module is installed, delete the "requests that span both" line and have the remaining module load for every request. If no standard module is installed, keep only the loading conditions for staged-work and token-lean.

## Placement by environment

| Target environment | Always-on instructions | Module install location | Notes |
|---|---|---|---|
| claude.ai (web, desktop, mobile) | The user preferences field in settings | Upload a .skill or zip in the skills menu of settings | Preferences apply to every conversation in the account |
| Claude Code | `~/.claude/CLAUDE.md` for all projects, `CLAUDE.md` in the project root for one project | `~/.claude/skills/module-name/` for all projects, `.claude/skills/module-name/` for one project | CLAUDE.md is recommended to stay under 200 lines |
| Tools that read AGENTS.md (Codex, Cursor, and others) | `AGENTS.md` in the repository root | For Codex and Cursor, `~/.agents/skills/module-name/` or `.agents/skills/module-name/` in the repository | Each tool has extra paths, so check its documentation |

The paths in this table are the values in each tool's official documentation as of 2026. Paths can change when tools change, so when giving directions, add one line telling the user to check the tool's latest documentation.

## Environment notes

- Claude Code's `@path` imports load every imported file into context at session start. Attaching modules to CLAUDE.md with `@path` makes them load every time and cancels the benefit of splitting them into modules. Install modules in the skills folder.
- In its default setting, Claude Code does not read AGENTS.md when a CLAUDE.md exists in the same place. For users who use both files, suggest putting `@AGENTS.md` on the first line of CLAUDE.md and keeping shared content only in AGENTS.md.
- AGENTS.md is often committed to a repository and shared with others. Suggest keeping personal preferences in the user-wide location and only team-agreed rules in AGENTS.md.

## Environments without skills

If the target environment does not support skills, fall back in this order.

1. If the environment supports per-file rules (for example, rule files read only when certain files are opened), move the module body into that feature and delete the loading rule from the always-on instructions.
2. If the model can read files in the environment, keep each module as a plain md file and change "load" in the loading rule to "read the file." Write the file path in the loading rule.
3. If neither works, pick only the most used rules from the user's most used module and add them to the always-on instructions. Tell the user to paste the other modules into the conversation when needed.
