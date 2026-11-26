---
name: no-standard
description: "Makes the model answer without loading write-standard and code-standard. Use it when the user calls \"/no-standard\" or asks for an answer without write-standard and code-standard. Do not load it without a user request."
metadata:
  generator: pref-architect
  generator-version: "1.3"
---

# no-standard

In a conversation where this skill is called, do not load the target modules in the settings section. This call counts as the case in the module loading rule of the always-on instructions where the user explicitly says not to use a module.

## Settings

- (Target modules) write-standard, code-standard

## Scope

- Apply it from the response where it is called until the conversation ends.
- After the call, stop applying the rules of target modules already loaded in the conversation.
- If the user asks for a target module again, load that module from that request on.
- Keep applying modules outside the targets and the common work rules in the always-on instructions.

## When to load

Load this skill only on a user request. If the model loads it on its own, the standards of the target modules stop applying without the user knowing.
