## Review summary

If this goes up as it is, the first objection will likely be that **the approach directly contradicts what the current state and goals say**. The current state says "work documents cannot be entered into external generative AI" and the goals say "comply with security rules," yet the approach says it will "query company documents directly through an external cloud AI." This contradiction has to be resolved first. Only then can staffing, schedule, budget and benefits line up.

Below are 5 must-fix items and 3 nice-to-fix items, followed by the full revised plan.

---

## Must fix

### 1. The security rules and the adoption method conflict

- **Original:** "(Model) Connect the highest-performing external cloud hyperscale AI service by API and query company documents directly"
- **Problem:** This matches neither the current state (no work documents into external services) nor the goal (comply with security rules). The only criterion for choosing a model is "performance," with no sign that security conditions or cost were weighed.
- **There are two ways to fix it.**

| | A. In-house build | B. Enterprise cloud (dedicated contract) |
|---|---|---|
| Method | Install an open-source model on company servers | An external service contracted on the condition that input data is neither used for training nor retained |
| Security rules | Meets the current rules as they are | Requires a rule change or an approved exception |
| Burden | GPU server purchase, staff to run the model | Approval process, checking contract terms |
| Fit for this company | Does not fit an IT team of 5 with no one dedicated to AI | Close to the draft's intent of using a high-performing external model |

- The revised plan **assumes option B**. Approval of a security rule exception is included in the decisions requested from executives. Unless the information security department's view is obtained before the meeting, this item will stall in the room.

### 2. Building and running it in-house is hard with the current staff

- **Original:** "(Build and operations) The IT team develops and runs the integration with company systems in-house"
- **Problem:** The current state right above says "IT team of 5 people, no one dedicated to AI." Integrating company documents means gathering documents, linking access rights and tuning search quality. The question will come right away whether the team can take this on as in-house development on top of its existing work.
- **Revision:** Hand the build to a specialist vendor. The IT team handles integration with company systems and account and permission management, and names one dedicated person for the pilot period.

### 3. A "pilot" that goes company-wide in three months

- **Original:** "(Schedule) Start in January 2027, briefing for all departments in March, company-wide rollout in April"
- **Problem:** There is no pilot period, no step to verify the impact and no step to decide on expansion. The goals name two teams as the pilot, but the schedule runs to a company-wide rollout, so the scope does not match either. No build period is shown. Holding a briefing for all departments in March, before pilot results exist, is also out of order.
- **Revision:** Change the order to kickoff (January), build (February-March), pilot with the two teams (April-June), then impact verification and the expansion decision (July). Company-wide rollout gets a separate approval based on the verification results.

### 4. The 50% cut and KRW 300 million savings have no basis

- **Original:** "(Impact) Cut the two teams' document work time by 50%," "KRW 300 million a year in labor cost savings from cutting document work time by 50%"
- **Problem:**
  - There is no baseline for the time the two teams now spend on document work, so there is no way to verify 50%.
  - For KRW 300 million to hold, the document work labor cost of the people covered must be KRW 600 million a year (KRW 300 million ÷ 50%). If asked where the KRW 600 million comes from, there has to be data to answer with. It also does not say whether this is for the two teams or the whole company.
  - Labor costs do not actually fall unless headcount falls. Writing "savings" invites finance to ask when and by how much costs will really drop. Staff in the two teams may read it as a headcount reduction plan and not cooperate with the pilot.
  - "Document work" mixes search, drafting and review and approval. The time AI saves is mainly in search and drafting, so measuring the two separately is more accurate.
- **Revision:** Change it to "[ ] work hours a year freed up (KRW [ ] million in labor cost terms)" and attach the formula. Set the target figures after measuring the baseline in January.

### 5. The budget has only the service fee

- **Original:** "Service fees of KRW 120 million a year (estimated from the external service's published pricing)"
- **Problem:**
  - Build costs (external vendor), security review costs and training costs are missing. Putting only KRW 120 million of cost next to KRW 300 million of benefit makes the plan look better than it is. If an executive points this out, the whole plan becomes hard to trust.
  - Published pricing may differ from the dedicated contract pricing in item 1.
  - It is unclear whether this is for the two pilot teams or the whole company, and why a pilot is budgeted per year.
- **Revision:** Build a table by cost item for the pilot period. Report company-wide rollout costs separately, together with the pilot results.

---

## Nice to fix

**6. The background is weakly supported.** "Say that ... take a lot of time" and "the cost has dropped sharply" have neither figures nor sources. Adding how many hours a week each person in the two teams spends, and how much pricing has fallen (with a source), makes the case far more convincing. If there is no measurement, I suggest running at least a short survey of the two teams in the days before the meeting. If a source for the price drop is hard to find, the second item can be dropped.

**7. Risks and decisions requested are missing.**
- In quality and design work, an AI error that goes straight into a report does real damage.
- Integrating company documents could let staff without access rights see document contents through AI answers.
- For an executive meeting agenda item, the end should state clearly "what we are asking you to approve."

**8. Wording.**
- "Hyperscale AI" and "generative AI" are mixed. The revision uses "hyperscale AI" throughout and keeps the rule's own wording only where the security rule is quoted.
- "(Security) Comply with company security rules" is a precondition more than a goal. It is revised into something checkable: "comply with the information security department's approval conditions, zero leaks of work documents."
- The two items under "Current state" are really constraints, so the heading is changed to "Current state and constraints."
- "Past documents" is made specific as "past quality records and design documents."

---

## Full revised plan

`[ ]` marks numbers to fill in.

> # In-house hyperscale AI pilot plan (draft)
>
> ## Background
> - The quality and design teams spend an average of [ ] hours per person a week searching past quality records and design documents and drafting reports ([survey method], as of [ ] 2026)
> - Hyperscale AI pricing has fallen about [ ]% over [period] ([source]), to a cost a mid-sized company can bear
>
> ## Current state and constraints
> - (Security) Company security rules forbid entering work documents into external generative AI services → ordinary external services cannot be used
> - (Staffing) IT team of 5 people, no one dedicated to AI → no capacity to develop and run it in-house
>
> ## Goals
> - (Pilot teams) [ ] people in the quality and design teams, 3-month pilot from April to June 2027
> - (Impact target) Cut document search time by [ ]% and report drafting time by [ ]% (set after measuring the baseline in January)
> - (Security) Comply with the information security department's approval conditions, zero leaks of work documents
> - (Expansion decision) Decide whether and how far to roll out company-wide based on the pilot results
>
> ## Approach
> - (Adoption method) Use an enterprise cloud hyperscale AI service under a dedicated contract
>   - Contract terms: no use of input data for training, no data retention, confirmed data processing location (domestic region preferred)
>   - Requires an approved security rule exception (or a rule change) before use
> - (Model selection) Given that security conditions are met, choose by comparing Korean document handling quality and cost
> - (Document integration) Apply existing document access rights as they are so that answers draw only on documents the user may see, and show the source documents with every answer
> - (Build and operations) A specialist vendor does the build, the IT team handles integration with company systems and account and permission management, and one person in the IT team is dedicated to the pilot
> - (Schedule)
>
> | When | What |
> |---|---|
> | January 2027 | Information security review, build vendor selection, baseline measurement of the two teams' work hours |
> | February-March | System build and document integration, training for pilot users |
> | April-June | Pilot with the quality and design teams |
> | July | Report on impact verification, decision on company-wide rollout |
> | Second half | (If approved) phased rollout by department |
>
> ## Budget (pilot period, January-June 2027)
>
> | Item | Amount | Basis |
> |---|---|---|
> | Service fees | KRW [ ] | [ ] users, dedicated contract quote |
> | Build | KRW [ ] | Document integration and screen development, vendor quote |
> | Security review | KRW [ ] | If an external audit is needed |
> | Training | KRW [ ] | [ ] pilot users |
> | **Total** | **KRW [ ]** | |
>
> - Annual cost of a company-wide rollout reported separately with the pilot results
>
> ## Expected benefits
> - [ ] work hours a year freed up in the two teams (about KRW [ ] million in labor cost terms)
>   - Formula: [ ] people covered × [ ] hours of search and drafting per person a year × [ ]% reduction × KRW [ ] labor cost per hour
> - Freed-up time goes back into core work such as quality improvement and design review
> - Past quality records and design materials stay easy to find after staff move or leave, which eases the loss of work knowledge
>
> ## Risks and responses
>
> | Risk | Response |
> |---|---|
> | AI produces answers that are factually wrong | Show source documents in answers, require staff review for official documents such as reports |
> | Contents of documents the user may not see are exposed | Integrate existing document permissions as they are, check permissions before the pilot |
> | Fees rise with usage | Set a monthly usage cap, review usage monthly |
> | Low use after adoption | Name a usage lead in each team, review usage rates monthly |
>
> ## Decisions requested
> 1. Proceed with the pilot for the quality and design teams (January-July 2027)
> 2. Approve a security rule exception for using an enterprise cloud service (or direct the information security department to review it)
> 3. Pilot budget of KRW [ ]

---

## To confirm before the meeting

1. **Adoption method:** Please confirm that option B (enterprise cloud, dedicated contract) is the way to go. If you prefer option A (in-house build), let me know and I will revise the budget, staffing and schedule on that basis.
2. **Information security department's view in advance:** Get their view beforehand on whether an exception can be approved and on what conditions, so that decision request 2 can pass in the meeting.
3. **Headcount and document work time of the two teams:** If there are no work records, please get figures at least through a short survey. These numbers fill in the benefits formula.
4. **Rough vendor quotes:** The dedicated contract fee and the build cost. If firm quotes are hard to get by next week, a range (for example KRW ○0-○0 million) is fine.
5. **Basis for the draft's KRW 300 million:** If you have the original calculation, send it and I will rework it to fit the revised formula.
