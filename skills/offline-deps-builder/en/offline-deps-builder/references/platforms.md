# Platform constraints

> This English version is a translation of the Korean original. It may behave differently from what the original intends.

The figures and setting names in this file reflect September 2026. Platform policies change often, so when web search is available, check the current values in each item's official documentation.

## Skill upload limits

| Platform | Limit | Official documentation |
|---|---|---|
| Claude API | 30MB for all files combined after decompression | https://platform.claude.com/docs/en/build-with-claude/skills-guide |
| claude.ai | No size figure in the official documentation. Description up to 1,024 characters, folder name must match name | https://claude.com/docs/skills/how-to |
| OpenAI API | 25MB after decompression, 50MB zip, 500 files | https://developers.openai.com/api/docs/guides/tools-skills |
| ChatGPT | No size figure in the official help article | https://help.openai.com/en/articles/20001066-skills-in-chatgpt |

A user has reported that claude.ai refused to install a zip holding more than 200 files (https://github.com/Imbad0202/academic-research-skills/discussions/21). For platforms without official figures, use the smallest official figure, 25MB, and the reported count of 200 files.

## Network settings

The table below shows the network levels for code execution on claude.ai. Administrators set the level for Team and Enterprise organizations, and users set it on individual plans. Enterprise defaults to disabled, and Team defaults to package managers only (https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude).

| Level | Reachable scope |
|---|---|
| Disabled | Preinstalled packages only |
| Package managers only | npm, PyPI, GitHub, crates.io, Ubuntu archives, Yarn |
| Package managers plus specific domains | The list above plus domains an administrator adds |
| All domains | The whole internet except domains on the legal blocklist |

Even at the package-managers-only level, Maven repositories, model hubs, font distribution sites, office extension sites, and the CPU-only indexes of deep learning frameworks are missing from the allow list. Dependency skills are often needed at this level as well.

A domain allowed on paper can be blocked in a real environment. Some environments block HTTPS downloads from a host while letting the git protocol through to the same host. Judge by the result of an actual request to each source.

The Claude API skill environment has no network access and cannot install packages at run time. Put every needed file in the skill or rely on preinstalled packages.

The official documentation for ChatGPT and the OpenAI API does not detail the container's network scope. Judge by the current session's tool list and by actual requests.

Agent environments such as Kubernetes vary with organization policy. Ask the user whether an internal package mirror or a shared volume exists.

## Attachment limits

| Platform | Limit | Official documentation |
|---|---|---|
| claude.ai chat | 500MB per file, 20 files per chat | https://support.claude.com/en/articles/8241126-upload-files-to-claude |
| claude.ai project files | 30MB per file | Same as above |
| ChatGPT | 512MB per file | https://help.openai.com/en/articles/8555545-file-uploads-faq |

The container path where attachments land differs by platform. Find them by file name.

## Skill folder behavior

- Skill folders are sometimes mounted read-only. Extract the payload into a writable working path
- Zip upload and sync steps can drop execute permissions. Copy executables into the working path and set the execute permission
- The absolute path of the skill folder differs by platform. Locate files inside the dependency skill relative to its SKILL.md

## Target probing commands

These examples assume a Linux container. Skip commands that are missing.

```
uname -m                          # CPU architecture
ldd --version | head -1           # glibc version (musl environments show musl)
cat /etc/os-release | head -3     # distribution and version
python3 -m pip debug --verbose | grep -A8 "Compatible tags"   # installable wheel tags
node --version; java -version
id -u                             # 0 means root
df -h /tmp; free -m               # disk and memory
python3 -m pip list               # preinstalled Python packages
curl -sS -m 10 -o /dev/null -w "%{http_code}\n" https://pypi.org/simple/   # reachability per source
```

## Default assumptions

If you cannot reach the target environment and the user cannot answer, use the assumptions below and record them in the manifest.

- Linux, x86_64, glibc family
- Treat the glibc version as unknown and pick builds that run on old glibc
- Treat the Python and Node.js versions as unknown and prefer version-independent formats (pure Python wheels, abi3 wheels, WASM). If only version-specific files exist, weigh bundling several versions against the size
- The writable path is /tmp
