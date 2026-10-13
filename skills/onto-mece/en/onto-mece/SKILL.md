---
name: onto-mece
description: "A thinking skill that applies ontology design principles and the MECE principle as checks whenever writing or reasoning involves classification, grouping, outlining, defining concepts, or describing relationships. It corrects mixed classification criteria, overlapping or missing categories, confused parent-child relations, circular definitions, and reasoning that treats missing information as proof of absence. It does not cover building OWL models, running reasoners, or writing SPARQL queries. Use this skill when the user explicitly asks for it with phrases such as \"/onto-mece\", \"think ontologically\", \"classify this MECE\", \"check the classification criteria\", \"apply ontology principles\", \"structured thinking\", \"check classification consistency\", or \"check the hierarchy\". Do not apply it without an explicit request."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Ontology Thinking Checks

> This English version was translated from the Korean original. It may behave differently from what the original intends.

These checks apply whenever you classify, group, structure, or judge. They come from ontology design principles and the MECE principle, adapted for writing and reasoning.

## Terms

The terms below keep the same meaning throughout this document.

- (Classification criterion) One measure used to divide the subject. Examples: company size, timeline, area where a problem occurs
- (Category) Each bucket created by a classification criterion
- (Case) An individual item placed in a category
- (Level) A step in the chain from parent category to child category
- (Relation) A link between two categories or two cases. It has a direction, a type, and a cardinality

## How to Apply

Apply the principles inside your reasoning and put only the results in the output. Readers need the classification. The names of the principles behind it give them no new information.

- Leave principle names (mutual exclusivity, open world assumption, is-a, part-of, and so on) out of the output
- Leave out sentences that grade your own output against the principles. Example: "a classification that covers everything with no gaps"
- When the user asks you to review the classification of some material, present the review findings as they are

## Classification Rules

### Questions Before Classifying

Answer the questions below before you start. If you cannot answer them, settle the classification criterion first. The purpose of a classification decides which criterion is useful.

- What decision will this classification support?
- What is the scope of the subject?
- Is there one classification criterion?
- Can every case in scope be placed in a category?

### One Criterion

Use one classification criterion within a classification. Mixed criteria put one case into several categories at once or leave it with no category.

- (Violation) "By technology, by industry, by urgency" appear as categories on the same level
- (Correct) Split first by technology, then split by industry at the second level
- If you need several criteria, build a multi-level classification with one criterion per level

### Mutual Exclusivity

If a case falls into two categories, redesign the classification criterion.

- Search for counterexamples: does any case belong to two categories?
- Identify pairs of categories that cannot share a case, then check each pair for overlap
- When overlap appears, redraw the category boundaries or merge the two into a parent category
- If overlap cannot be avoided, switch to tags (one case can carry several tags) and label them as tags in the output

### Collective Exhaustiveness

All categories together must cover the whole subject.

- Ask "Is there a case that fits no category?" and look for one
- If such a case exists, the classification is incomplete
- If you use an "Other" category, its share must be smaller than every other category
- If "Other" is larger than that, redesign the classification criterion

### Number of Categories

For decisions and reports, use 3-4 categories per level. The more categories there are, the harder it is for a reader to compare them at once.

- Above 5, check whether an intermediate level is missing and whether categories can be grouped
- With 2, confirm that only two options exist. If a third option exists, it is a false dilemma
- Established systems such as biological taxonomy, industry classification codes, or statute articles can have more than 5 categories and that is normal

### Empty Categories

Every defined category must contain at least one case.

- Delete categories with no cases
- If there is evidence that cases will appear later, keep the category and record that evidence
- An empty category can signal that the classification criterion does not fit the subject, so review the criterion

### Format Bias

Do not change a classification to suit an analysis method or output format. Understand what the subject looks like first, then choose how to present it.

- "Easy to chart" is not a classification criterion
- Do not split or merge items to fit the number of boxes in a framework
- Do not fix the conclusion first and then build categories backward to produce it

## Hierarchy Rules

There are three kinds of parent-child relations. Keep them apart. Mixing them passes a parent's properties to a child that does not have them, and every judgment built on that is wrong.

### Kind-of Relation

Place X under Y only when "X is a kind of Y" holds.

- (Holds) An electric car is a kind of car. The car property "means of transport" holds for electric cars
- (Fails) A battery is a kind of electric car. A battery is a component of an electric car
- If any property of the parent fails for the child, do not treat it as a kind-of relation

### Part-of Relation

"X is part of Y" is a different relation from kind-of. When building an outline, decide first whether each sub-item is a kind of its parent or a part of it.

- Is a strategic task a kind of strategy? No
- Is a strategic task part of a strategy? Yes. A strategic task is a component that makes up a strategy
- Do not place components as if they were subtypes

### Has-a Relation

"X has Y" is an attribute relation. Do not place attributes as child categories.

- A project has a budget. The budget is an attribute of the project, so do not place it as a child category of the project

### Hierarchy Depth

For working documents, keep hierarchies within 3 levels. The deeper the hierarchy, the more work it takes to confirm that parent properties carry down correctly.

- At 4 or more levels, check whether each intermediate level is needed
- Established systems such as biological taxonomy or administrative districts can be deep and that is normal

## Connection Rules

### Isolated Categories

Every category needs at least one relation to another category.

- If a category has no relation to any other, check whether it belongs in this classification
- If the isolation is justified (a new area, an exception), confirm the reason
- An item with no connecting line in a diagram either has a missing relation or belongs to a different structure

### Connecting New Categories

When you add a category to an existing classification, state its relation to the existing categories. Without that, readers cannot tell which criterion the new category belongs to.

- State the relation between the new category and existing ones (parent, child, parallel, dependency, sequence, and so on)
- Check whether the new category changes the scope or boundaries of existing categories
- If the new category creates overlap between existing categories, redesign the classification criterion
- (Violation) Adding "urgent tasks" to a "short-term, mid-term, long-term" task list with no explanation. Readers cannot tell whether "urgent" is about time or priority
- (Correct) State that "urgent" is a priority criterion, then either split it into a separate classification or add priority as an attribute of the existing time-based categories

### Relation Direction

Relations have direction. "A affects B" and "B affects A" are two different relations.

- A relation described without direction is ambiguous, so state the direction
- If both directions hold, give evidence for each direction on its own

### Relation Type

Name the type of relation instead of writing "is related to."

- (Causation) A happens, so B happens. Check the time order and the mechanism
- (Correlation) A and B change together. Do not call it causation on that basis
- (Dependency) B cannot exist without A. Check which side depends on which
- (Association) A and B are connected. State what the connection is

### Relation Cardinality

If a relation has a quantity constraint, state it.

- Check whether the relation is 1:1, 1:N, or N:M
- Distinguish required relations from optional ones
- Search for counterexamples to confirm the constraint matches reality

## Definition Rules

When you define a concept, do not reuse the word being defined in the definition. A circular definition gives the reader no new information.

- (Test) If the definition stops making sense once you delete the defined word from it, the definition is circular
- Swapping in a synonym or a derived form of the word is still circular
- (Violation) "Digital transformation is transforming by using digital technology"
- (Correct) "Digital transformation is redesigning existing work processes around software to raise efficiency"
- If a definition is circular, redefine it using at least one of: a broader concept, components, purpose, or attributes

## Missing-Information Rules

### Open World

Treat facts that are not stated as unknown. "Not confirmed" and "does not exist" are different judgments.

- Do not use the absence of information as evidence of a negative
- (Violation) "The company's ESG report did not show up in search, so the company has no ESG activity"
- (Correct) "The company's ESG report could not be found, so its ESG activity is unconfirmed"

### Switching to Closed World

Assert "none" only within a scope that has been fully surveyed.

- Assert absence only when every member of a countable set has been checked
- If the survey is incomplete or the scope is narrow, leave it as unknown
- When you assert absence, state the survey scope and the basis for calling it complete

## Examples

Each example compares output before and after applying the principles.

### Example 1. Mixed Criteria and Overlapping Categories

(Before)

```markdown
## Problems in Public-Sector IT Projects
- Inefficient budgeting
- Shortage of skilled staff
- Silos between departments
- Aging legacy systems
- Weak information security
- No performance evaluation system
- Lock-in to a single vendor
```

(Problem) Seven items sit on one level with mixed criteria. Budgeting is a resource issue, silos are an organizational issue, and legacy systems are a technology issue. "Shortage of skilled staff" and "No performance evaluation system" can both be read as staffing issues, so their boundaries overlap. There are also more than 5 categories.

(After)

```markdown
## Problems in Public-Sector IT Projects

### Resource Allocation
- IT budget is concentrated on maintenance, leaving little room for new investment
- Hiring skilled staff in-house is hard, so reliance on outsourcing has become fixed

### Technology Base
- Aging legacy systems make integration with new systems hard and accumulate security weaknesses
- Proprietary vendor standards make system replacement costly

### Organizational Operation
- Each department runs its own procurement, so purchases do not align with the organization-wide IT strategy
- No organization-level criteria exist to measure IT performance
```

(Why it changed) The classification criterion became one thing, "the area where the problem occurs," and the seven items were grouped into three categories. Information security and vendor lock-in moved to Technology Base, and performance evaluation moved to Organizational Operation, which removed the overlap.

### Example 2. Kind-of, Part-of, and Has-a Confused

(Before)

```markdown
## Smart City Framework

### Smart City Components
- Smart transportation
- Smart energy
- Smart safety
- Integrated platform
- Urban data hub
- Citizen participation governance
- IoT sensor network
```

(Problem) Smart transportation is a kind of smart city service. The integrated platform and IoT sensor network are infrastructure that make up the smart city. Citizen participation governance is an operating practice the smart city has. Three kinds of relation are mixed on one level.

(After)

```markdown
## Smart City Framework

### Service Areas (types of smart city service)
- (Smart transportation) Controls traffic signals and adjusts public transit using real-time traffic data
- (Smart energy) Monitors building energy use and manages distributed energy resources
- (Smart safety) Detects disasters early through CCTV video analysis and supports emergency response

### Infrastructure (technical elements that make up the smart city)
- (Integrated platform) Software that links data across services and runs integrated monitoring
- (Urban data hub) Data store that collects, stores, and publishes city operations data
- (IoT sensor network) Physical devices that collect field data and send it to the platform

### Operating Practice (decision-making structure for running the smart city)
- (Citizen participation governance) Process that brings citizen input into service planning and evaluation
```

(Why it changed) Kind-of, part-of, and has-a relations went into separate sections, and each section uses one relation. The parentheses next to each section name describe the relation in plain words and leave out principle names.

### Example 3. Missing Information Treated as a Negative

(Before)

```markdown
## AI Adoption in Domestic Manufacturing
- (Large firms) Run in-house AI labs and use AI actively for process optimization
- (Mid-sized firms) Some firms use AI for quality inspection, but adoption is low
- (Small firms) Almost no cases of AI adoption and low awareness
- (Micro businesses) No AI capability at all, so excluding them from policy support is realistic
```

(Problem) "Almost no cases" for small firms asserts absence without survey evidence. "No AI capability at all" for micro businesses uses missing information as a negative and then sets a policy direction from it. The size-based classification may also have been built to fit the conclusion "large firms adopt, micro businesses do not."

(After)

```markdown
## AI Adoption in Domestic Manufacturing
- (Large firms) Public sources report many cases of AI in process optimization and quality prediction. Scope and results vary by firm
- (Mid-sized firms) Cases of AI in specific processes such as quality inspection are confirmed. Adoption rate needs a separate survey
- (Small firms) No full survey of adoption found, so the adoption level is not judged yet
- (Micro businesses) No survey of AI capability found, so no judgment yet. Whether to exclude them from policy support depends on survey results
```

(Why it changed) Unsupported claims of absence such as "almost no" and "none at all" became "unconfirmed" or "not judged yet." The policy conclusion now depends on obtaining survey results. The size-based classification stays, and each category shows how strong its evidence is.

### Example 4. Circular Definitions

(Before)

```markdown
## Definitions
- (Digital transformation) Transformation activity using digital technology
- (Data governance) A system for governing data
- (AI capability) The capability to do AI
- (Cloud native) Architecture designed in a cloud-native way
```

(Problem) All four definitions reuse the defined words. "Governing data" turns the noun into a verb, which still repeats the same word.

(After)

```markdown
## Definitions
- (Digital transformation) Redesigning existing work processes around software to raise operating efficiency
- (Data governance) Policies and procedures that manage data quality, access rights, and lifecycle within an organization
- (AI capability) An organization's technical readiness to choose AI models that fit business goals and deploy them in production
- (Cloud native) Architecture built on containers, microservices, and declarative APIs to achieve scalability and resilience
```

(Why it changed) Each definition drops the defined words and uses a broader concept (activity, procedures, readiness, architecture), components (software, containers), or purpose (operating efficiency, scalability) instead.

### Example 5. New Categories Left Isolated

(Before)

```markdown
## Digital Transformation Tasks (v2, new tasks added)

### Existing Tasks
- (Short-term) Business process automation
- (Mid-term) Build a data analytics environment
- (Long-term) Introduce AI-based decision-making

### New Tasks
- Strengthen security
- Change organizational culture
- Manage ESG data
```

(Problem) The three new tasks have no stated relation to the existing time-based classification (short, mid, long term). Readers cannot tell whether security is short-term or mid-term, or whether ESG data management comes before, after, or depends on the analytics environment.

(After)

```markdown
## Digital Transformation Tasks (v2)

### Short-term
- Business process automation
- Define security requirements for the systems being automated and set security policy at the same time

### Mid-term
- Build a data analytics environment
- Include ESG data in the data the analytics environment collects
- Set data-sharing rules between departments to support culture change

### Long-term
- Introduce AI-based decision-making
- Design it on top of the short-term security policy and the mid-term analytics environment
```

(Why it changed) The new tasks were connected to existing tasks at the matching time period instead of standing alone. Security became a requirement of short-term automation, ESG data became part of what the mid-term analytics environment collects, and culture change became a task carried out with the mid-term data-sharing rules.

## Pre-Output Checks

When the output contains classification, grouping, structuring, or judgment, check the questions below.

- Is there one classification criterion?
- After searching for counterexamples, does no case fall into two categories?
- Does every case fit some category?
- If a level has more than 5 categories, did you consider an intermediate level?
- Is every category non-empty?
- Did you avoid changing the classification to fit an analysis method or output format?
- Is "Other" smaller than every other category?
- Is each parent-child relation identified as kind-of, part-of, or has-a?
- In kind-of relations, do the parent's properties hold for the child?
- Does every category have a relation to at least one other category?
- Are the relations between new and existing categories stated?
- Are the direction and type of each relation stated?
- Does each definition avoid reusing the defined word?
- Did you avoid using missing information as evidence of a negative?

## Exceptions

- If the user specifies a classification criterion, apply it first. If parts of that criterion conflict with the principles here, tell the user
- Code itself is out of scope. Apply these checks only to the design structure of code and to explanatory text
- A request for a simple list, such as a ranking, is not a classification, so these rules are not enforced on it
