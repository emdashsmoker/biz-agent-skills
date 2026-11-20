---
name: no-modules
description: "Stops loading the modules that the always-on instructions say to load, at the user's request. Load it only when the user calls \"/no-modules\" or asks for it by name. Do not load it on your own because a question looks short or simple. If the user names modules in the same message, stop loading only the named modules."
metadata:
  generator: pref-architect
  generator-version: "1.1"
---

# no-modules

A skill that turns off, when the user wants, the modules the always-on instructions load for every response. The loading rule in the always-on instructions loads modules even for short questions, so the modules apply even in conversations that do not need their standards. This skill replaces repeated skip requests with one call and fixes what is turned off and for how long.

## Settings

- (Modules to turn off) write-standard, code-standard, staged-work, token-lean

## What is turned off

- If the user calls it without module names, do not load any module listed in (Modules to turn off).
- If the user names modules in the same message, do not load only the named modules. Load the other modules as the loading rule in the always-on instructions says.
- If a module was already loaded before the call, stop applying its rules from the response to the calling message onward.

## Rules that stay

- Keep following the common work rules and other preferences in the always-on instructions. They apply to every task, so they hold regardless of module loading.
- Load other skills the user asks for directly as usual. This skill stops only the loading rule in the always-on instructions.

## Duration

- Apply it from the calling message to the end of the current conversation. The body of this skill stays in context until the conversation ends, so the duration matches the conversation.
- In a new conversation, follow the loading rule in the always-on instructions again from the start.

## Turning modules back on

- If the user asks to use modules again or asks for a module by name, follow the loading rule in the always-on instructions again for that module.
- If the user turns only some modules back on, keep the other modules off.
