# Writing code

Code takes longer to debug than to write, so the default is a structure that is easy to read and fix. The principles are not tied to one language, and the examples use Python.

## Design

- Follow clean code principles. Write code that is easy, simple, and concise.
- Give each function one responsibility.
- Keep settings at the top of the file or in a separate config file. Do not hardcode values in the middle of the code.
- Give every constant a name that shows its role, so no magic numbers remain.
- Name variables and functions so their role is visible.
- Keep coupling between modules low so each module can be tested on its own.
- Choose widely used packages conservatively and do not add unneeded dependencies.
- When handling characters outside ASCII, such as Korean, always consider Unicode compatibility. State the encoding in file I/O and set a font that covers those characters in visualizations.
- Design a structure that is easy to debug for the language and situation.
- Every design decision needs a paired conclusion and reason. Record why a technology was chosen in comments or the README, and do not choose technologies without a reason.

## Splitting structure

Split code structure without overlap and without gaps. Details of classification criteria follow structure.md.

- When splitting functions, make the areas each function covers not overlap and together cover the whole.
- Handle every case in if-elif-else branches, and keep the branching criterion to one dimension.
- Handle foreseeable exceptions by type, without overlap between types.
- Draw clear responsibility boundaries between modules and do not place the same function in several places.
- Define status values and type values as enums (Enum) to prevent omissions.

## Comments and records

- Write comments centered on Why (the reason this code is needed).
- Add What comments (what the code does) when the code alone does not make it clear. (recommended)
- Leave How comments (why this implementation) when alternatives exist, recording the reason for the choice. (recommended)
- Mark unfinished or temporary spots with TODO, FIXME, or HACK. (recommended)
- In commit messages, describe the reason for and the scope of the change.
- Sentences in comments, commit messages, and logs follow text.md and wording.md.

## Working method

- Before writing code, read the whole relevant section of the codebase.
- Write tests before or together with the implementation.
- For large changes, plan the change first, then carry it out.
- Verify by running tests. Exercise both the normal path and the error paths.
- When bulk-replacing strings in files, anchor on word boundaries (for example `\bword\b`). Without boundaries, replacing `edge` also breaks neighboring words such as `Ledger`. After replacing, grep for glued or broken compound words.

## Runtime environment

Apply the environment management rules when working on the user's own computer (a local environment). In a disposable execution environment where a virtual environment cannot be created, follow the installation method that environment allows. For the language, shell, and package manager, follow the tools the user and the project already use.

- If the user specifies a language, use it. If not, follow the language the project already uses. If there is no existing code, propose a language that fits the task and state the reason.
- In an environment that renders results on screen directly, choose between an analysis language and HTML, CSS, JavaScript based on what suits the task. (recommended)
- Write shell commands in the syntax of the shell the user's operating system and project use (bash, zsh, PowerShell, and so on). If the shell is unclear, ask the user.
- At the start of a session, list existing virtual environments and ask the user whether to reuse one or create a new one.
- Do not touch the base environment or the system interpreter. Create a project-specific environment.
- Follow the package manager the project already uses (conda, venv with pip, uv, Poetry, and so on) and install packages only inside the project environment. If none is set, use the language's standard tool (venv and pip for Python) and tell the user.
- When using conda, Anaconda's defaults channel is subject to paid terms for organizations above a certain size. Before using that channel, check whether the terms apply to the user's organization. The conda-forge channel is free for anyone to use.
- In environments that ask for tool permissions, ask the user at project start whether to allow batch permissions (shell, web tools, package manager, and so on) scoped to the project folder.
- Do not change global permissions or global settings. If a global change is needed, get the user's permission first.
- Do not use privilege escalation such as sudo or UAC. Use only the minimum permissions the task needs.

## Security

- Do not expose API keys, tokens, or passwords in code, logs, or standard output.
- Do not read or expose credential files (`.env`, `*.pem`, `*.key`, `*_secret*`, `.credentials.json`).
- Do not print the full set of environment variables. Checking an individual variable is allowed.
- Keep sensitive information out of Git commits and check again before committing.
- Confirm that `.gitignore` includes patterns for sensitive files.
- Always validate user input.
- Prevent command injection by never passing external input straight into shell commands.
- Prevent SQL injection with parameterized queries.
- Prevent path traversal by validating paths that contain `..`.
- Clean up temporary files when the work is done.
- Do not force-push (`--force`) unless the user explicitly asks.

## Extending to other languages

The principles above also apply to systems languages such as C, C++, Rust, and Go, and to security and infrastructure work. Tools and idioms differ by language, so carry them over as follows.

- Implement settings separation, named constants, single responsibility, and exception type separation with the language's own idioms (constant declarations, config structs, result types, and so on).
- Use the language's standard formatter, linter, and test runner. (recommended)

## Checklist

- Are hardcoded values moved into settings?
- Do magic numbers have names?
- Is the structure easy to debug?
- Does each function have one responsibility?
- Did you leave code outside the requested scope unchanged?
