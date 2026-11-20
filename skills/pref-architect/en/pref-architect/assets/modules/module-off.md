---
name: module-off
description: "Keeps the modules listed in the settings section, out of those named in the always-on instructions, from loading in this conversation. Load it only when the user asks for \"/module-off\", \"work without modules\", \"answer without the standard modules\", and similar."
metadata:
  generator: pref-architect
---

# module-off

A skill that lets the user choose which conversations run without modules. Always-on instructions apply to every conversation, so the user calls this skill to run one conversation differently. Names in parentheses in the body refer to items in the settings section.

## Settings

- (Modules to turn off) write-standard, code-standard, staged-work, token-lean

## Rules

- From the response in which this skill is called, do not load the modules in (Modules to turn off). Keep them off for the rest of the conversation until the user asks for a module again.
- If a module in (Modules to turn off) was already loaded in the same conversation, do not apply its rules to later responses.
- Load modules that are not in (Modules to turn off) as the loading rule in the always-on instructions says.
- Keep applying the common work rules and other preferences in the always-on instructions. Every conversation needs these rules regardless of module.
- If the user calls a module in (Modules to turn off) directly by name, load that module. The direct call is the user's later decision.
