# Hyperscale AI usage security check

Of the 6 tasks that use AI, **1 is a clear breach of the security rules.** The design team drafts design change reports with external API model C. **1 cannot be judged with the current records.** For model B, which the quality team uses to draft defect cause analysis reports, the status record says it is installed in-house while the IT team records say it is an external API. There are 2 management gaps. Model B's installation information differs between records, and no department owns the meeting minutes task. The other 3 tasks comply with the rules.

The figure comes as `ai_usage_map.png` (for viewing) and `ai_usage_map.svg` (for zooming and editing). It runs from left to right through department, task, document handled and model, and the color of the line between a document and a model is the verdict. Gray is compliant, red is a violation and the orange dashed line needs confirmation.

## Check by task

Rule applied: tasks that handle internal documents may use only models installed on company servers. Tasks that handle public material may use any model. The numbers match those in the figure.

| # | Task | Department | Document handled | Model (installation) | Verdict |
|---|---|---|---|---|---|
| 1 | Organizing meeting minutes | **Not set** | Meeting minutes (internal) | A (company servers) | Compliant with the rule, **management gap** |
| 2 | Searching past quality documents | Quality team | Past quality documents (internal) | A (company servers) | Compliant |
| 3 | Drafting defect cause analysis reports | Quality team | Defect cause analysis report (internal) | B (differs between records) | **To confirm** |
| 4 | Summarizing public specifications | Design team | Public specifications (public) | D (external API) | Compliant |
| 5 | Drafting design change reports | Design team | Design change report (internal) | C (external API) | **Violation** |
| 6 | Industry trend briefing | Planning team | Industry trend material (public) | C (external API) | Compliant |

## Violation: drafting design change reports (design team, model C)

Design change reports are internal documents, while model C is an external vendor API. Assume that internal design information has gone to the external vendor in every draft written so far.

1. Stop drafting design change reports with model C right away.
2. Use model A instead. Model A is currently the only model that both records list as installed in-house. Leave B out of the alternatives until it is confirmed.
3. Establish the period, number and content of the design change reports put into model C so far.
4. Check how long the external vendor's contract lets it keep input data and whether it uses the data for model training, and request deletion if needed. If the company has a security incident reporting procedure, report through it.

## Verdict on hold: drafting defect cause analysis reports (quality team, model B)

Defect cause analysis reports are internal documents, so the verdict depends on where model B actually runs.

| Actual situation | Verdict |
|---|---|
| The status record is right: B is installed only on company servers | Compliant |
| The IT team records are right: B is used only as an external API | Violation (same steps as the design team case) |
| Both are right: an in-house install and an external API are both in use | Depends on which one the quality team connects to |

The IT team can settle it by checking three things.
- Whether the server asset list has a record of model B being installed
- Whether the address the quality team connects to when calling model B is an internal or an external vendor address
- Whether there is an API contract or usage billing with model B's vendor

Until this is confirmed, I recommend moving this task to model A temporarily as well. If it turns out to be a violation, apply steps 3 and 4 of the design team case in the same way.

## Management gaps

**1. Model B's installation information differs between records.** There is a bigger problem than not being able to reach a verdict. The company is not managing, against a single standard, which models send data outside the company. Choose one reference record for each model's installation (the IT team's asset list is recommended), and correct the other records, including the status record, to match it.

**2. No department owns the meeting minutes task.** It uses model A, installed in-house, so it is not a violation now. But no one decides who may use it, which meeting minutes may go in or where the output is kept. It also means no one would stop it if someone later moved the task to an external model. The most natural owner is the department that manages the original meeting minutes.

## Points to note

- **The same model C is compliant for the planning team's task and a violation for the design team's task.** The rule turns on the documents a task handles, not on the model. So a "list of approved models" alone cannot prevent a violation like this one. A register that records and checks the documents each task handles and the model it uses is needed, and the table above can serve as its first edition.
- **The design team case suggests that there is no pre-check when AI is added to a new task, or that it is not working** (this is an inference, not a fact confirmed from the records).
- **Internal document tasks may pile onto model A.** Four tasks, numbers 1, 2, 3 and 5, handle internal documents. If model B is confirmed as an external API, model A will carry all four. A is now used only for search and meeting minutes, so its report drafting quality and capacity need checking in advance.

## Order of actions

| Order | Action | Owner (proposed) | When |
|---|---|---|---|
| 1 | Stop using model C for design change report drafts, switch to model A | Design team | Immediately |
| 2 | Move defect cause analysis report drafts to model A temporarily | Quality team | Immediately |
| 3 | Confirm model B's installation, set the reference record for installation information | IT team | Within 1 week |
| 4 | Establish the scope of internal documents sent to model C (and B if confirmed external), check the vendor's data retention and training terms | Design team, quality team, IT team | Within 1 week |
| 5 | Check model A's capacity and report drafting quality | IT team | Within 2 weeks |
| 6 | Name an owner department for organizing meeting minutes | Executive in charge of AI use | Within 2 weeks |
| 7 | Run a register of AI use by task, with new tasks used only after registration and checking | Security officer, IT team | Within 1 month |

## Assumptions and what could not be checked

- The "compliant" verdicts assume that each task handles only the documents listed in the table. For example, putting internal sales data into an industry trend briefing would make it a violation at that moment.
- The records mention a discrepancy only for model B, so I assumed the IT team records also list model A as installed in-house. If A is listed differently, verdicts 1 and 2 and the recommended replacement model need another look.
- The terms of the contracts with external vendors (retention of input data, use for training) are not in the records, so I could not judge them.
