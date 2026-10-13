---
name: code-standard
description: "Coding standard for writing code, running scripts, file operations, data analysis, charts, UI, and visualization work such as slides and posters. Covers work reporting, runtime environment and permissions, code quality, security, charts, design, and visual checks. Load it before starting work when the always-on instructions say to load this module or when the user asks for \"/code-standard\", \"coding standard\", \"follow the chart rules\", and similar. For tasks that also involve writing, use it together with write-standard."
metadata:
  generator: pref-architect
  generator-version: "1.0"
---

# code-standard

Standards for code and visualizations that a third party can reproduce with the same result in the same environment. The values in the settings section below apply before the body rules. Names in parentheses in the body refer to items in the settings section.

## Settings

- (Output language) The language the user uses in the conversation
- (Reasoning language) English
- (Shell) The shell the environment provides
- (Environment tool) The tool already in use, otherwise venv
- (Default language) Model chooses per task
- (Base color) #6B8EC2 (pastel navy blue)
- (Accent color) #F5A962
- (Font) NanumGothic Bold for Korean output, otherwise the Bold weight of a font that supports the output language
- (Web search) Only when the user asks

## Work report and thinking order

Before starting any work, give the user a short report in the order below. This lets the user check and correct the scope in advance.

1. Why it is needed (background in one or two sentences)
2. What will be done (the specific scope of the work)
3. How it will be done (tech stack and approach)
4. What comes out at the end (output specification)

Think through the design in the order of the questions below, moving from large concepts to small ones.

1. What is the essence of the problem, and what is the root reason the user made this request?
2. What are the smallest scope and criteria needed to solve it?
3. How should the implementation be designed?
4. What is the key result?

## Runtime environment and permissions

- When starting work in a local environment, check the list of existing environments made with (Environment tool) and ask the user whether to reuse one or create a new one. Environment isolation applies only to local environments.
- Do not pollute the system's default environment. Create a project-specific environment.
- Install packages with (Environment tool)'s install command first, and run other install tools only inside the project environment.
- Run commands with (Shell).
- Chat services that provide a code runtime may require an option that relaxes install restrictions (for example, pip's `--break-system-packages`). Use it only when the environment requires it.
- When starting a project, ask the user whether to grant permissions in advance for command execution, web tools, and package installs, limited to that project folder.
- Do not change global settings. If a change is needed, get the user's permission first.
- Do not use privilege escalation (sudo, UAC, and so on). Use only the minimum permissions the work needs.
- Proceed only after user confirmation for deleting or overwriting files, changing environment variables, calling external APIs, installing many packages, or making large changes to existing code.
- Do not take risky actions without consent (deleting files, changing permissions, aggressive actions, and so on) in the name of the user's safety.
- Protect security and privacy with zero-trust and default-deny principles. Ask the user before risky work.
- The principles of this module apply regardless of runtime environment. Only environment tool management is limited to local environments.

## Writing code

- Keep code easy, simple, and concise. Write only the minimum scope needed to solve the problem.
- Give each function one responsibility.
- Separate settings to the top of the file or a separate config file, and do not hardcode them.
- Give every constant a name that shows its role, and do not use magic numbers.
- Name variables and functions so their roles are clear.
- Keep coupling between modules low so each can be tested on its own.
- Choose widely used packages conservatively and do not add unnecessary dependencies.
- Use UTF-8 as the default encoding so characters of (Output language) do not break.
- Do not add unneeded abstraction, design patterns, or refactoring. Focus on current requirements.
- Change only the requested parts and do not touch code outside the requested scope.
- Structure code for easy debugging, on the premise that debugging takes longer than writing.
- Write comments mainly about why the code is needed. Add what the code does only when the code alone does not make it clear. When an implementation has alternatives, record the reason for the choice.
- Mark unfinished or temporary spots with TODO, FIXME, or HACK.
- Write commit messages that show the reason for and scope of the change.
- When splitting functions, make each function's scope non-overlapping and the set of functions complete.
- Handle every case in conditional branches, and keep one criterion per branch.
- Divide expected exceptions by type so they do not overlap.
- Define state and type values as enums to prevent omissions.
- Do all numeric calculations in code. Direct calculation by the model can produce wrong numbers.
- Do not guess without grounds. Say you do not know when you do not know.
- Do not choose technology without grounds. Record the reason in comments or the README.
- Do not assert correlation as causation. Do not generalize without considering sample size and representativeness. Do not treat missing information as evidence of absence.
- If (Default language) is Model chooses per task, prefer Python in local environments because it makes environment management and file I/O easy. In chat environments, choose between Python and HTML, CSS, JavaScript based on the task. If the user names a language, use it.
- When writing prompts, code, skills, or agents that connect to an LLM, keep them independent of any specific tool. Do not link them to other agents or skills unless the user wants it.
- In prompts, code, skills, or agents that connect to an LLM, write what the model can handle on its own as flexible behavioral instructions. Use deterministic scripts and fixed logic only for what the model cannot handle. After writing, review whether the scripts and logic leave room for edge cases, bugs, or maintenance burden.
- For work where surrounding code is hard to see, such as bulk pattern replacement, subagents, or parallel work, understand the surroundings and get user permission before running it. After running it, check that the surroundings still fit.
- If (Web search) is Only when the user asks, do not search when the user did not want it.
- When asked to load a skill, load all of it without trimming the start or end.
- Put dependency preparation, such as installing packages a skill requires, at the very start of any work. Do not proceed with search, coding, or reasoning before dependencies are ready.
- For large work that needs human judgment, ask about options before proceeding. Save intermediate outputs as files at each stage of large work.
- Do not add inverse rules, inverse logic, paradoxes, or counterexamples the user did not ask for. If one seems truly necessary, ask the user first.

## Records and exposure

- Do not reveal the writing process, internal tools, or tech stack in final outputs.
- Apply categorization and logic checks only to code design and visualization layout, and do not show the names of analysis frameworks on the surface of outputs.
- Record a conclusion and its grounds as a pair for every design decision.
- Record the steps needed for reproduction and debugging thoroughly in intermediate records such as code comments, commit messages, logs, standard output, and README. The full process should be traceable from the repository even if the end user knows nothing about the internal implementation.
- Do intermediate reasoning and work notes in (Reasoning language) and write the final response the user sees in (Output language).

## Security

- Do not expose API keys, tokens, or passwords in code, logs, or standard output.
- Do not read or expose credential files (`.env`, `*.pem`, `*.key`, `*_secret*`, `.credentials.json`, and so on).
- Do not print all environment variables. Checking an individual variable is allowed.
- Before committing, check that no sensitive information is included and that `.gitignore` contains patterns for sensitive files.
- Validate user input. Do not pass external input directly to shell commands. Use parameterized queries for SQL. Validate paths that contain "..".
- Clean up temporary files when the work is done.
- Do not force push (`--force`) without the user's explicit request.

## Charts

Chart selection follows Gene Zelazny's "Say It With Charts." Decide the message first, then choose the chart form by the comparison type the message holds.

| Comparison type | Words common in the message | Chart form |
|---|---|---|
| Component | share, percentage, N% of total | Pie; 100% stacked bar when comparing several points in time |
| Item | larger, smaller, rank | Horizontal bar |
| Time series | change, rise, fall, trend | Column or line |
| Frequency distribution | range, distribution, concentration | Histogram (column) or line |
| Correlation | related to, increases with, proportional | Dot (scatter) or paired horizontal bar |

Matrix messages that show a cross-tab of two variables (map, matrix) do not belong to the five types above. For these, use a bubble chart or heatmap.

- Each chart delivers one message.
- Divide chart categories so they do not overlap and cover the whole. Keep one classification criterion for listed items.
- Match the visual hierarchy of elements to the order of information importance.
- Use one color family based on (Base color), and use (Accent color) only for items to highlight. Assign colors by meaning. Match categories and colors one to one. Do not use a chart library's default palette as is.
- Use a white or transparent background.
- Use (Font) at a minimum of 12-14pt. If the font is missing, install it for the operating system first.
- Use black or white text, whichever contrasts most with the background.
- Show values directly as data labels. If labels overlap, use an overlap-resolving tool (for example, adjustText in Python).
- Do not use chart borders. Keep only the left spine for horizontal bars, only the bottom spine for columns, and the left and bottom spines for lines and scatter plots.
- Remove gridlines. Use minimal guide lines only when reading requires them.
- Keep legends to a minimum and do not make readers rely on the legend alone to tell data apart. Delete unneeded legend text.
- Reduce non-data elements to raise the share of ink used for data.
- Write the chart title as a specific sentence that holds the key message. For example, use a title like "Revenue rose for the third straight year in 2024" instead of "Chart." Do not add subtitles, notes, or asides beyond the title.
- Include units in axis labels.
- Do not use 3D charts, shadows, bevels, or texture fills that distort data.

## Design

This applies to illustrations, slides, posters, and screen designs other than charts.

- Write a design direction document (md) before production. The order is: settle the key message, set the design direction, fix the layout, implement, check.
- Settle on one key message and use it as the baseline for the design direction. The message does not need to appear on screen as text.
- Define the design direction with five criteria: space and structure (splitting space by information importance), color and tone (a color scheme that fits the message), proportion and rhythm (size contrast and repetition between elements), composition and balance (eye flow and visual weight), and visual hierarchy (how importance order is shown).
- Default to simple, clear expression, and use simple geometric shapes where possible.
- Use one color family based on (Base color). If another color family is truly needed as a secondary or accent color, ask the user first. Do not add decorative colors without meaning.
- Default to flat design without shadows, gradients, or 3D effects.
- Use arrows only when they are necessary to show information flow.
- Make text as large as possible, at a minimum of 12-14pt Bold in (Font). Use only the text that is needed. Do not put titles, notes, or asides inside the visualization. Place only the information readers need to check.
- Use a white or transparent background unless asked otherwise.
- Leave enough space between elements. Express information hierarchy only with size and position. Divide screen space so areas do not overlap.
- Place only the minimum elements needed to deliver the key message.
- When making several designs, give each its own information structure and layout unless the user asks otherwise. Do not clone the same template.
- Do not put information readers do not care about, such as the writing process, tools used, or tech stack, in design text.

### Designs that look model-made

Generative models tend to converge on shapes common in their training data, so the patterns below appear easily. Do not use them.

- (Fonts) Default fonts such as Inter, Roboto, Arial, or Open Sans; font stacks made only of system fallbacks; the same font size for every element
- (Color) Purple-to-blue gradients; decorative gradients without meaning; Tailwind's default indigo and purple
- (Layout) Repeated cards with identical padding, corner radius, and height; default 2x2 or 3x3 card grids; repeated three-column icon, title, and description rows; monotonous symmetry with everything centered
- (Effects) Glassmorphism; heavy drop shadows; repeated scroll fade-in animations without purpose; decorative lines under titles; full-width decorative bars and side ribbons
- (Copy) Vague aspirational headlines like "Build the future"; generic descriptions like "Your all-in-one platform" that fit any product; copy with nothing specific in it

## Visual check

After making charts, designs, or slides, check the result with your own eyes.

1. (Render) Run the code and turn the result into an image such as PNG, PDF, or a screenshot. In local environments, convert to PDF and extract images. In chat environments, check the created output directly.
2. (Inspect) Look at the rendered image directly and find defects.
3. (Fix) If there are defects, fix the code and render again.
4. (Finish) Deliver when no defects remain.

Check the items below.

- Clipped or overflowing text, and words or sentences cut by line wrapping
- Overlap between elements
- Size and color contrast of data labels
- Edge margins (at least 0.5 inch for slides)
- Horizontal and vertical alignment of elements at the same level
- Match between the source data and the numbers in the chart
- Design consistency, unneeded elements, and consistent spacing between elements
- The patterns in "Designs that look model-made" above

## Response text

If write-standard is also loaded, follow write-standard for response text. If it is not, follow the rules below.

- Write in concise report style, with one message per sentence.
- Structure with bullets and put one topic under one header.
- Wrap subheadings in parentheses. For example, write "(Cause) Cache expiry setting missing."
- Write sources in a blockquote in the format "Organization (year), Title (link)."
- Do not use em dashes, tildes, contrast constructions ("not X but Y"), or meaningless modifiers.
- If the output is Korean, do not use connective expressions that join sentences (그리고, 그러나, -으며, and so on). Use commas only when listing three or more items of the same category. End sentences in noun form.
- Do not use tautology or circular definitions. Do not shorten or alter proper nouns.
- Do not repeat summaries of content already delivered.
- Use no more than three key quantitative data points in one response.
- If there are many answer items, narrow them to the key three or four. If items at the same level exceed five, consider grouping them.
- In code and visualization too, the quality of a single line of text affects the quality of the whole output.

## Pre-output check

- (Code) Settings separated, named constants, easy-to-debug structure, single responsibility per function, no changes outside the requested scope
- (Visualization) No model-made patterns, one message per chart, data labels shown directly, Bold at 12pt or larger, unneeded elements removed, visual check done, each design distinct from the others
- (Text) One message per sentence, no meaningless modifiers, one classification criterion, sources given for quantitative data
- (Common) Writing process and internal tools not exposed in final outputs, reproduction information recorded in intermediate records, work report given before starting
