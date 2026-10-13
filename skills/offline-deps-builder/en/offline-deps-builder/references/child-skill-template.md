# Dependency skill templates

> This English version is a translation of the Korean original. It may behave differently from what the original intends.

## Name

Name a dependency skill `<parent skill name>-deps`. Name a runtime shared by several parent skills `<runtime name>-runtime`. Use only lowercase letters, digits, and hyphens, and match the folder name.

## Folder layout

```
<parent skill name>-deps/
├── SKILL.md
├── MANIFEST.md
├── scripts/          # activation script (optional)
└── payload/
    ├── python/       # wheels, or package archives extracted and repacked
    ├── node/         # node_modules archive
    ├── bin/          # executables (xz compressed)
    ├── runtime/      # language runtime archives
    ├── fonts/
    ├── data/         # models, caches, templates
    └── licenses/     # license files that must travel with their items
```

Create only the folders you need. To cut the file count, pack subfolders into one archive.

The activation script uses only the Python standard library. zipfile, tarfile, lzma, and shutil can extract the payload. Environment variable settings do not outlive the script, so print export statements or leave them in an env.sh file.

## SKILL.md template

Fill in the angle-bracket parts and delete lines that do not apply.

```markdown
---
name: <parent skill name>-deps
description: "Dependency bundle for using the <parent skill name> skill where outbound network access is blocked. Load it together with the <parent skill name> skill, and run this skill's activation procedure first in place of the parent skill's install step. MANIFEST.md lists the items and their sources."
---

# <parent skill name> dependencies

Carries the <summary of items> the <parent skill name> skill needs. The target environment is <operating system, architecture, glibc, language versions>.

## Activation

1. Check whether everything is already usable: <check commands and pass conditions>. If all pass, skip activation
2. Create the working path: <for example /tmp/<parent skill name>-deps>
3. Extract the payload: <extraction method per item>
4. Set execute permissions and paths: <PATH, PYTHONPATH, NODE_PATH, fonts, caches, offline mode variables>
5. Check that it works: <command and expected result>
6. Print the values the parent skill needs and save them as export statements in <working path>/env.sh: <paths or options>

If an activation script exists, `python3 <this skill folder>/scripts/activate.py` runs the procedure above in one step.

When running the parent skill's commands, prefix them with `. <working path>/env.sh &&`. In target environments that open a new shell for each command, environment variables set once do not carry over to the next command.

## Using it with the parent skill

- Skip the parent skill's install step and use the activation results
- <how to connect parent skill options or environment variables>

## Troubleshooting

- If activation fails, show the user the failed step and its output messages
- If the target environment differs from the target conditions in MANIFEST.md, tell the user the difference and guide them to reassemble for the matching conditions
```

## MANIFEST.md template

```markdown
# <parent skill name> dependency manifest

## Items

| Item | Version | Format | Source address | License | Target conditions | Download date | Size | Used by |
|---|---|---|---|---|---|---|---|---|
| <name> | <version> | <wheel, executable, font, and so on> | <official address> | <license> | <cp312, manylinux_2_17_x86_64, and so on> | <YYYY-MM-DD> | <MB> | <parent skill function> |

## Excluded components

- <component>: <reason for exclusion and empty folders kept>

## Target environment assumptions

- <conditions assumed without checking>

## Items relying on preinstalled packages

- <items excluded because the target environment already has them>

## Verification log

- <date>, <environment>, <checks performed>, <result>
- Unverified: <item and reason>
```
