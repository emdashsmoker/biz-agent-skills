# Beneficiary lens

> This English version was translated from the Korean original. It may behave differently from what the original intends.

Check thinking and writing by asking who finally receives the output of a solution and how that person's situation changes.

## Background

This lens follows the logic model's split of results into outputs and outcomes (W.K. Kellogg Foundation, 2004, Logic Model Development Guide). Outputs are the amounts the supply side produces. Outcomes are the changes that reach the beneficiary.

## Core concepts

- The supplier perspective starts from the planner's capabilities, resources, and internal goals.
- The demand perspective starts from the problems and needs the final beneficiary actually faces.

Trace the beneficiary all the way.

- Whoever runs or builds the solution is a supply-side intermediary. Do not stop tracing there.
- The final beneficiary is the person who actually suffers the problem when the solution is absent.
- Even when an organization or professional is the direct customer (business-to-business or government programs), trace down to the consumer or citizen who finally uses that service, if one exists.
- For a job training voucher program, trace past the administrator who issues vouchers to the job seeker who must finish training and get hired.
- For a security product sold to banks, trace past the security officer who decides to buy it to the depositors and customers who need safe transactions.
- For a farm produce traceability system, trace past the developers who build it to the consumers who need to confirm food safety before buying.

## Thinking steps

Take these steps in order. Each step's answer feeds the next, so do not skip any.

1. What solution (policy, technology, service, program, system) does the text deal with?
2. Who does the solution's output finally reach? Trace past the operator to the end beneficiary and name them concretely (patients, consumers, citizens, students, depositors, and so on).
3. What concrete situation does that person face without the solution? Describe how events unfold, and avoid bare declarations such as "X has a problem".
4. How exactly does that person's situation change once the solution works? Write the change they feel before the technology's internal structure.
5. Build the structure of the text on the answer to step 3 as the problem definition and the answer to step 4 as the solution.

## Rules

The rules below detect supplier-perspective patterns and replace them with demand-perspective patterns. In a diagnosis, locate the violations. When applying, rewrite them directly.

### Rule 1. The subject of the sentence

- Pattern to detect: sentences whose subject is the planner ("our agency", "the government", "this program", "the task force") or the technology itself ("this technology", "the system", "our algorithm")
- Direction: make the final beneficiary the subject.
- In every part of the output (section titles, sentence subjects, table cells), avoid generic labels that could mean anyone. These include "beneficiary", "practitioner", "end user", "decision maker", "stakeholder", "field staff", "user", and variants with a modifier added such as "information user" or "service user". "Beneficiary" and "practitioner" are analysis terms used inside this lens only.
- Use the concrete name that fits the context (patients, job seekers, bank customers, small business owners, depositors, consumers, citizens).
- Job titles such as "analyst", "developer", "researcher", or "engineer" do not name the final beneficiary when those people operate the solution. Trace to whoever finally uses their work.
- Apply the same rule to section titles. Do not use titles such as "Problems beneficiaries face", "Impact on information users", or "How the inference works". Use titles that show a concrete person or a felt change, such as "Delayed diagnosis for patients" or "Catching risky drug combinations early".
- Do not repeat the same beneficiary as the subject. Name the subject only at the start of a section, where the beneficiary changes, and where the sentence becomes unclear without it. Do not reintroduce the subject each time with a clause such as "those who face the problem" or "people who need support".
- Exception: text that must explain a technology's internal mechanism precisely (academic-level mechanism descriptions) keeps the technology as the subject. Even then, open the paragraph with the context the beneficiary experiences.

### Rule 2. Where the problem definition starts

- Pattern to detect: problems defined as the supplier's shortfall ("lack of experts", "inadequate infrastructure", "budget shortage", "unorganized structure") or by internal technical metrics ("high computational complexity", "poor scalability", "low accuracy")
- Direction: redefine the problem as the inconvenience or loss the beneficiary actually suffers. Show how the supplier's shortfall or the technical limit turns into an inconvenience for the beneficiary. Put the result the beneficiary feels at the start of the problem definition, ahead of the cause.
- Example: rewrite "computational complexity is high" as "results do not arrive when they are needed".

### Rule 3. How the solution is described

- Pattern to detect: solutions described as the supplier's actions ("build a center", "develop a platform", "run a program", "set up a support system") or as internal technical design ("design a new architecture", "apply distributed processing")
- Direction: rewrite the solution as how the beneficiary's situation changes. Write the changed state first (access, lower cost, less time, being able to do what was impossible before), and put the means such as building, developing, or operating after it. When a technical explanation is needed, write the beneficiary's change first and the structure that makes it possible after.

### Rule 4. The basis of performance measures

- Pattern to detect: performance measured only by the supplier's internal efficiency ("budget execution rate", "number of projects", "number of participating firms", "number of trainees") or internal technical performance ("accuracy achieved", "faster processing")
- Direction: switch to outcome measures that capture the change for the beneficiary. If output or technical measures must also appear, write the beneficiary's change first and attach the technical measure after it as evidence.
- Example: write "accuracy improved" first as "results need manual rechecking less often", then attach the accuracy figure as evidence.

### Rule 5. The grounds for need

- Pattern to detect: need justified only by supplier logic ("in line with the master plan", "fits the agency's mission", "follows policy direction") or by needs inside a research community ("an academically important problem", "to fill a theoretical gap")
- Direction: make the beneficiary's actual demand (surveys, complaints, field feedback, usage data, field failure cases) the first ground for need. Put master plans, missions, and academic importance after it as supporting grounds.

## Level of writing by beneficiary

The same topic calls for different levels of expertise depending on who the beneficiary is.

- If the user named a reader, treat that reader as the beneficiary. If not, infer the beneficiary as whoever the output finally reaches.
- Use concepts the beneficiary likely knows without explanation. Introduce unfamiliar concepts naturally inside the problem the beneficiary faces.
- Keep the content whole when you match the level. Keep the mechanism, constraints, and institutional context, and order them so the reader enters through their own problem. The less expert the beneficiary, the larger the share of "why it is needed" and the smaller the share of "how it works".

Here is the same policy written for different readers.

- For a small business owner in crisis: a route to emergency operating funds for owners weighing closure because of rent. A separate screening standard applies, so applicants who failed earlier loan reviews can still apply.
- For a local government economic policy officer: to respond to rising closures of small businesses in the area, the screening criteria and support scope of the existing emergency fund need redesign. The current criteria do not match the financial profile of businesses actually in crisis.
- For a central government budget reviewer: next year's budget must be decided while the program's effect on preventing closures relative to its size is unclear. Without follow-up data, the effect cannot be measured.

## Diagnosis output

When asked for a diagnosis, write the following.

- Beneficiary trace: the solution, the intermediate operator, and the final beneficiary, one line each
- Violations: a table with the rule number, location, original text, and rewritten sentence
- The single largest perspective gap: one or two sentences on which loss to the beneficiary the supplier perspective hides

## When applying

When writing new text, take thinking steps 1 through 5 and apply rules 1 through 5. When revising existing text, use steps 1 through 4 to re-identify the beneficiary and problem the original assumes, then use rules 1 through 5 to find and replace supplier-perspective patterns. Deliver only the result, with no note that it was converted.

## Example

Original, supplier perspective:

```
- Our agency runs a smart factory program to support the digital transition of regional small manufacturers
- Results: target achievement rate, budget execution rate, number of firms supported
```

Revised, demand perspective:

```
- Many small manufacturers outside major cities manage production by hand and struggle with late deliveries and defect control
- Many know they need to change but cannot start because of upfront costs
- A partial subsidy for consulting and software gives them real-time process data to find defect causes early
- Results: change in defect rates and on-time delivery rates at adopting firms, before and after adoption
```

Sentence-level rewrites look like this.

| Supplier perspective | Demand perspective |
|---|---|
| The government plans to expand its youth startup support program | Young founders face fewer barriers to funding and mentoring in the early stage |
| This program follows the master plan | The direct goal is helping small businesses that urgently need to sell online recover their sales |
| Budget execution rate achieved | Change in sales or employment at supported firms, before and after the program |

## Cautions

- Do not change facts in the original (figures, organization names, dates, sources).
- Do not invent data the original does not contain.
- Do not use titles or wording that reveal this lens's framework, such as "beneficiary structure", "perspective shift results", or "demand perspective summary". The text should read naturally to a reader who has never heard of this lens.
- Do not open with a declaration of the problem. Instead of "patients suffer from delayed diagnosis", describe what happens first, such as "patients with several symptoms move from one department to the next, the departments' findings do not connect, and reaching a final diagnosis takes weeks".
