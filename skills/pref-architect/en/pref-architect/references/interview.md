# Interview questions

The interview sets the values that go into the always-on instructions and the module settings sections. Each question lists its default and the place its answer changes. Do not ask a question whose answer changes nothing.

## How to run it

- Ask at most 4 questions at a time. When there are more, users tend to pick answers carelessly.
- Show the default for each question and put it as the first option.
- Always ask group A (environment). In the first question of group B, offer "Use defaults for all remaining questions." If the user picks it, fill groups B through F with defaults.
- If there are existing assets, put the values read from them in place of the defaults and label them "current setting."
- Skip questions that earlier answers made unnecessary. For example, if code-standard will not be installed, skip group E.
- If the user writes an answer outside the options, use that answer as the setting value. If it conflicts with another setting, explain the conflict and ask again.
- Keep the answers in one table in the conversation and show it as is at the design approval step.

## A. Environment

| No. | Question | Options | Default | What the answer changes |
|---|---|---|---|---|
| A1 | Where will the always-on instructions go? (multiple choice) | claude.ai user preferences, Claude Code's CLAUDE.md, a tool that reads AGENTS.md, other | claude.ai user preferences | Number and format of always-on instruction sets |
| A2 | Can skills be used in the target environment? | Yes, no, not sure | If not sure, the model checks | How modules are delivered |
| A3 | Do you have existing always-on instructions or skills? | None, instructions only, instructions and skills | None | Whether the integration procedure runs |

If the user picks "not sure" in A2, decide based on the placement table in references/router.md and state the reason in one line.

## B. Work and readers

| No. | Question | Options | Default | What the answer changes |
|---|---|---|---|---|
| B1 | What work do you mainly do? (multiple choice) | Reports and planning documents, research and analysis, coding and automation, data visualization and design | Reports and planning documents, research and analysis | Default selection in group C |
| B2 | Who mainly reads your outputs? | Entry-level practitioners in the field, experts in the field, the general public, custom | Entry-level practitioners in the field | (Target reader) in write-standard |
| B3 | From what perspective should the model answer? | A strategy consultant with deep experience in economics, business, and public administration, a practitioner expert in the field, no preference, custom | A strategy consultant with deep experience in economics, business, and public administration | (Writer perspective) in write-standard |
| B4 | In what language do you want outputs? | The language used in the conversation, Korean, English, custom | The language used in the conversation | (Output language) in write-standard and code-standard |
| B5 | In what language should the model do intermediate reasoning and work notes? | English, same as output language | English | (Reasoning language) in write-standard and code-standard |

B5 defaults to English because of token cost. The same content takes very different numbers of tokens in different languages, and English usually takes the fewest. Skip B5 if the output language is English.

## C. Module selection

| No. | Question | Options | Default | What the answer changes |
|---|---|---|---|---|
| C1 | Which bundled modules should be installed? (multiple choice) | write-standard, code-standard, staged-work, token-lean | All | List of modules to generate and the loading rule in the always-on instructions |

Add a one-line description to each module when showing the options.

- write-standard holds standards for sentences, structure, evidence, and wording.
- code-standard holds standards for code quality, security, charts, and design.
- staged-work holds a procedure that splits large tasks into stages and checks each stage.
- token-lean holds a procedure that cuts unneeded file loads, repeated output, and extra turns.

If the user did not pick coding or visualization in B1, drop code-standard from the default selection and say why. Add it back if the user wants it. If an existing skill does the same job, follow the overlap procedure in references/integration.md.

## D. write-standard settings

| No. | Question | Options | Default | What the answer changes |
|---|---|---|---|---|
| D1 | How should sentences end? | Korean report style ending in a noun (e.g., 도입 필요), plain declarative (e.g., 도입이 필요하다), conversational | Korean report style ending in a noun | (Writing style) |
| D2 | How many bullet levels? | Two levels (claims with '-', evidence with indented '+'), one level mixed with prose | Two levels | (Bullet levels) |
| D3 | Which overall structure should be the default? | WWH or SCQA chosen by purpose, always WWH, always SCQA, none | Chosen by purpose | (Document structure) |
| D4 | May the model search the web when not asked? | Only when asked, whenever needed | Only when asked | (Web search) |
| D5 | Limit on key quantitative data points and tables per document? | 3 each, 5 each, no limit | 3 each | (Quantitative data limit), (Table limit) |
| D6 | Apply the Korean word list when the output is Korean? | Apply, do not apply | Apply | (Korean word list) |

D1 applies when the output is Korean. If the user picks one level in D2, write-standard drops the '+' lines and attaches evidence as prose after the claim sentence. The D5 default of 3 comes from the consulting practice of narrowing key points to three or fewer (the rule of three). Working memory research, which finds that people hold about four chunks of information at once, points the same way. No research sets a limit for numbers and tables as such, so the user may change it.

## E. code-standard settings

| No. | Question | Options | Default | What the answer changes |
|---|---|---|---|---|
| E1 | Which shell runs commands? | The shell the environment provides, bash or zsh, PowerShell, custom | The shell the environment provides | (Shell) |
| E2 | What isolates project environments? | venv, conda, uv, none, custom | The tool already in use, otherwise venv | (Environment tool) |
| E3 | What is the default programming language? | Model chooses per task, Python first, JavaScript or TypeScript first, custom | Model chooses per task | (Default language) |
| E4 | What is the default color for charts and design? | Single pastel navy blue family (base #6B8EC2, accent #F5A962), custom company or personal color | Single pastel navy blue family | (Base color), (Accent color) |
| E5 | What is the default font for charts and design? | Model chooses a font that supports the output language, custom | NanumGothic for Korean output, otherwise a font that supports the output language | (Font) |

The E2 default prefers the tool already in use. Switching tools would put the user's other project environments out of step. NanumGothic in E5 is distributed under the SIL Open Font License 1.1 and is free to use.

## F. Common work rules

These rules apply to every conversation regardless of module, so they go into the always-on instructions. Add only the rules the user turns on.

| No. | Rule | Default | Why include it |
|---|---|---|---|
| F1 | Get user approval before running subagents | On | Subagents change output quality, token use, and speed a lot |
| F2 | Ask before creating files the user did not request | On | The user keeps control of the scope of outputs |
| F3 | Ask before loading skills the user did not request, and offer similar skills as alternatives. Load modules named in the always-on instructions without asking | On | Each skill works differently and changes the result |
| F4 | Do not add content to project knowledge or instruction files without user consent | On | Instruction files affect every later conversation |
| F5 | Check all requirements and constraints of the request before final output | On | A final check reduces omissions |
| F6 | Do not add inverse rules, inverse logic, paradoxes, or counterexamples the user did not ask for | On only when neither write-standard nor code-standard is installed | Both standard modules carry the same rule in their bodies, so installing them makes a second copy in the always-on instructions unnecessary |
| F7 | When creating or updating a skill, deliver the install file (.skill), SKILL.md, and every supporting md as files | On only where files can be delivered | The user can review the content and install right away |
| F8 | Short preferences for every output regardless of module (custom) | None | Holds preferences the user wants kept in any task |

For group F, show the table and let the user pick only the rules to turn off. When the user writes F8 or a new rule, first check whether a module to be installed already has the same rule. If it does, do not add it again to the always-on instructions, and tell the user it is in the module. Then check whether every conversation needs the rule. If only specific tasks need it, suggest putting it in the body of the matching module.
