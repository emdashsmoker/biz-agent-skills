---
name: offline-deps-builder
description: "Builds and updates dependency skills that carry the libraries, runtimes, executables, fonts, models, and extensions another skill would otherwise download at run time. It applies when a skill stalls at its install step because the container's outbound network is blocked or limited to package registries (claude.ai, ChatGPT, air-gapped agents). Use it when the user asks to 'make an offline dependency skill', 'make this skill work without network', 'bundle the libraries', 'package dependencies for an air-gapped environment', 'update the dependency skill', or to fix network errors in a skill's install step. For dependencies above the size limit it considers partial inclusion, splitting, and hybrid setups. See references/ecosystems.md for acquisition and activation per ecosystem, references/platforms.md for platform limits, network settings, and target probing commands, and references/child-skill-template.md for the dependency skill's SKILL.md and MANIFEST.md formats."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Offline Dependency Skill Builder

> This English version is a translation of the Korean original. It may behave differently from what the original intends.

Some skills download files at run time from pip, npm, GitHub releases, model hubs, and similar sources. When an organization setting or a platform policy blocks the container's outbound network, these skills stall at their install step. This skill builds a dependency skill that carries the files the stalled skill needs. The user loads both skills together, and the original skill runs without outbound network access.

## Terms

The terms below keep one meaning across this file and the reference files.

- (Parent skill) An existing skill that must download files from the network to work
- (Dependency skill) A skill that carries the files a parent skill needs and loads together with it
- (Dependency) Any file or program that must exist in the target environment for the parent skill to work but is missing from the parent skill folder
- (Payload) The bundle of dependency files inside a dependency skill
- (Manifest) MANIFEST.md, which records each payload item's version, source, license, and the assumptions made during assembly
- (Build environment) The place where the dependency skill is assembled
- (Target environment) The place where the dependency skill is loaded and used with the parent skill
- (Activation) Unpacking the payload in the target environment and setting paths so the parent skill can use it

Dependencies go beyond libraries. Language runtimes, executables, fonts, model weights, data files downloaded on first run, templates, and office application extensions all count as dependencies.

The build environment and the target environment can be the same or different. A common case assembles the skill on a networked PC or agent and uploads it to claude.ai or ChatGPT. Another case assembles it inside a network-blocked session from files the user attaches.

## Judgment principles

Dependencies differ by software in form and in install method. Young libraries sometimes change command names and distribution methods between versions. Treat the procedure in this file as the default flow. When a dependency does not fit the procedure, start from the goal below and design the method yourself.

> In the target environment, the parent skill's main functions run to completion without outbound network access, and their output is correct.

When documents and observed results disagree, go with the observed results. A domain that platform documentation lists as allowed can still be blocked in practice. A library whose install command succeeded can still fail on first use while reaching for the network. Record anything you cannot check as an assumption and move on.

Limit questions to the user to items whose answer changes the result. The target platform, the user's willingness to attach large files every session, and permission to change the parent skill's code fall in this group. Proceed on reasonable defaults for everything else and list them in the final report.

## Building a new dependency skill

### 1. List the dependencies

Read the parent skill's SKILL.md, scripts, and reference files in full and find the dependencies. Install commands reveal only part of them, so check the clues below as well.

- Install commands, import statements, require statements
- External programs the scripts call
- URLs, model repository names, and cache paths inside the code
- Fonts, templates, and extensions named in the documents
- Environment variables and file paths outside the skill folder

For each dependency, record which parent skill function uses it. Separate dependencies needed by main functions from those used only by optional functions. For a large library, note the components the parent skill uses. Libraries often ship several reasoning engines or several models while the parent skill uses one of them. This record guides what to exclude during size planning.

If the parent skill already works without outbound network access, tell the user no dependency skill is needed and stop.

### 2. Examine the target environment

The payload works only when its files match the target environment. Check the items below in the target environment. Probing commands are in references/platforms.md.

- Operating system, CPU architecture, C library type and version
- Python, Node.js, and Java versions and the packages already installed
- Writable paths, free disk space, memory
- Whether the current user is root
- Actual reachability of each source

If you cannot reach the target environment, ask the user for the target platform. If no answer is available, use the default assumptions in references/platforms.md and record them in the manifest. When conditions are unknown, you can also bundle files for several conditions. Wheels for several Python versions install without knowing the version. This raises the size, so weigh it during size planning.

Exclude dependencies the target environment already has. Preinstalled packages can change with platform updates, so record in the manifest which items rely on preinstalled packages.

### 3. Choose acquisition channels

The channels for getting dependency files are below. Channels higher in the list ask less of the user.

- (Build environment network) Download from package managers, git, or official download addresses
- (Session download tool) Some platforms provide a tool that fetches a URL mentioned in the conversation into the container even when the shell's outbound network is blocked. Look for one in the current session's tool list. Such tools sometimes accept only URLs that already appeared in the conversation, so find the official address with web search first
- (User attachment) The user downloads the file and attaches it to the conversation
- (Assembly in the user's environment) The user runs this skill in their own networked environment, assembles the dependency skill there, and uploads it

Most software can be obtained through more than one channel. A release binary address can be blocked while the git repository stays open. Some projects publish the same function through another package registry or as a WASM package. When one channel is blocked, look for another and try it, and record each channel tried with its result.

When you ask the user to download files, follow the rules below.

- Find the official download address with web search and share it. An official address means the project's own site, the package page on a package registry, or the repository the package registry lists as the source. Forks, mirrors, and redistribution sites fall outside official addresses
- Without a web search tool, give the address from model knowledge and state that it may have changed
- Spell out the conditions for picking the right file, such as operating system, architecture, Python version, and C library type
- Ask the user to attach the downloaded file as is, without renaming or extracting it
- For files larger than the attachment limit, explain how to split and upload them

When attachments arrive, compare the platform tags in the file names and the actual contents against the target conditions before using them.

### 4. Plan for size

Each platform limits skill uploads. Per official documentation at the time of writing, the Claude API allows 30MB for all files combined after decompression. The OpenAI API allows 25MB after decompression and 500 files. On claude.ai, users have reported that a zip holding more than 200 files was refused. A dependency skill meant for several platforms targets 25MB or less after decompression and 200 files or fewer by default. When you can read the current official figures, those figures take precedence.

The limit counts the size of the files inside the skill folder. An archive stored in the folder counts at its compressed size, so a higher compression ratio fits more. After assembly, measure the total folder size and the file count.

When the skill exceeds the limit, review the methods below in order. You can combine them.

- (Use preinstalled packages) Exclude dependencies the target environment already has
- (Partial inclusion) Carry only the components the parent skill uses. Keep folders that the library lists at startup as empty folders
- (Recompression) Repack with a high-ratio format such as xz, and pack folders with many files into one archive. Use zip, tar.gz, or tar.xz, which the Python standard library in the target environment can extract
- (Splitting) Split into several dependency skills. Put a runtime shared by several parent skills into one separate dependency skill and share it
- (Hybrid) Supply only the large files that exceed the limit from outside the skill
- (Suggest alternatives) Propose a smaller library or model to the user. This requires changes to the parent skill's code, so leave the decision to the user

Partial inclusion relies on the library's internal layout. After excluding components, run the parent skill's main functions in the verification step to confirm they work. After trimming a shared runtime, check it with every parent skill that uses it. A reduction that suits one consumer can stop another.

Build hybrid setups as follows.

- The user attaches large files every session. Files above the attachment limit go up in parts and get joined in the target environment. Compare the joined file's size with the original's size
- Agent environments such as Kubernetes supply files through volume mounts, pre-filled cache folders, or an internal package mirror
- If the platform offers a setting that allows specific domains, list the domains needed and help the user request them from an administrator

When model weights reach the GB range or the runtime itself takes hundreds of MB, a hybrid setup is in most cases the only option. If no method fits the limit, tell the user the required size, the platform limit, and the available alternatives as they are.

### 5. Assemble the dependency skill

Follow references/child-skill-template.md for the folder layout, the SKILL.md format, and the manifest format. references/ecosystems.md covers how to download files that match the target environment and how to activate them, per ecosystem.

When downloading files in the build environment, state the target conditions. Package managers pick files for the build environment when no conditions are given. A native package downloaded on a Windows PC fails to load in a Linux container.

Put the activation procedure in the dependency skill's SKILL.md. The activation procedure has the properties below.

- It first checks whether the dependency is already usable and extracts the payload only when it is missing
- It extracts the payload into a writable working path. The skill folder can be read-only
- It copies executables into the working path and sets the execute permission. Upload and sync steps sometimes drop execute permissions
- It sets paths and environment variables and prints the paths the parent skill needs
- It also saves the environment variables to a file in the working path. In target environments that open a new shell for each command, commands load this file first
- It runs a short working check
- Running it several times gives the same result

If the activation procedure is long, you can write it as a script that uses only the Python standard library and include it in the dependency skill.

Describe how to connect to the parent skill in SKILL.md as well. Tell the model to skip the parent skill's install step and use the activation results. If the parent skill hard-codes file paths, connect through options or environment variables. If the parent skill's code needs changes, show the changes to the user and get approval.

In the manifest, record each item's version, source address, license, target platform conditions, download date, and size. Also record excluded components with the reasons, and the assumptions about the target environment. The manifest is the basis for updates and for the pre-sharing check.

### 6. Verify

Verification runs the parent skill's main functions to completion under conditions as close to the target environment as possible.

In the build environment, create a state without outbound network access. On Linux, a network namespace or clearing the proxy settings does this. If neither is available, isolate the install step with the package managers' offline options (pip --no-index, npm --offline), and check for first-use downloads in the target environment. Use a new virtual environment and a new working path so that copies already installed do not mask the result. Use the same language version as the target environment, and hide system fonts or runtimes that the target environment lacks.

Judge success by the content of the output. An exit code of 0 and a created file can still hide an empty result. Some document renderers produce a PDF with all text missing and still report success when fonts are absent. For a PDF, extract its text and render pages to images to see the characters. For reasoning or conversion results, compare against expected values.

Libraries that download data on first use fail even after a successful install. Call the real function once with no outbound network access.

Repeat the same checks the first time the dependency skill is activated in the target environment. Mark items you could not check in the build environment as unverified in the manifest and in the final report.

### 7. Final report

When the work is done, tell the user the following.

- The dependency skill built and the parent skill to load with it
- Items included, items excluded with reasons, total size and file count
- Verification results and unverified items
- Assumed target environment conditions
- Actions for the user (upload, per-session attachments, requests to an administrator)

Deliver the dependency skill as a zip of its folder. Opening the zip must show a folder with the skill's name, with SKILL.md inside it.

## Updating an existing dependency skill

On an update request, compare the versions in the manifest with the latest versions. With network access in the build environment, query the package registries and git tags. Without network access, find the latest version on the official page through web search.

Update when there is a reason. Security fixes, new features the parent skill requires, and fixes for defects the user is hitting count as reasons. Without a reason, report only the comparison.

Young libraries sometimes change command names, options, and APIs together with the version. After updating, run the verification step again and keep the previous payload until the new one passes. If the parent skill's code no longer fits the new version, tell the user what needs to change. Update the manifest last.

## Pre-sharing check

If the dependency skill will be shared with others or published, check the following.

- Check each item's license and record in the manifest whether and under what conditions it can be redistributed. Tell the user first about fonts and commercial software that forbid redistribution and about licenses that carry source disclosure obligations
- For items whose license text must travel with them, include the license files in the payload
- Keep files that belong to a specific person or organization, such as signature images, organization templates, certificates, and API keys, outside the payload, and ask the user to attach them at run time
- Look for personal paths, internal organization domains, and account names left in the manifest and SKILL.md
