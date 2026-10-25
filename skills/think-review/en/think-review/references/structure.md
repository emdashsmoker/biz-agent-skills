# Structure lens

> This English version was translated from the Korean original. It may behave differently from what the original intends.

Check whether classifications, groupings, hierarchies, and relations are built correctly. This lens turns ontology design principles into rules for thinking. Building ontology models or running reasoners is outside its scope.

## Background

The principles come from these sources and are rewritten as thinking rules.

- Mutually exclusive, collectively exhaustive (MECE): the classification standard widely used with Barbara Minto's Pyramid Principle
- Ontology design criteria: Thomas Gruber (1995), including clarity, coherence, extendibility, and minimal encoding bias
- Competency questions: the approach proposed by Grüninger and Fox (1995) of first collecting "questions this structure must answer"
- Common design flaws: the pitfall catalogue of the ontology checker OOPS! (isolated elements, cycles in hierarchies, one category mixing two concepts, "miscellaneous" categories, and others)

## Principles at a glance

| Principle | Original meaning | As a thinking rule |
|---|---|---|
| Mutual exclusion | Categories do not overlap | If one case fits two categories at once, redesign the classification criterion |
| Collective exhaustion | The categories together cover the whole subject | If a case fits no category, the classification is incomplete |
| Single criterion | One classification uses one criterion | Do not mix categories based on different criteria in one classification |
| Is-a relation | A subtype inherits every property of its supertype | Place things as super and sub only if "Is X a kind of Y?" holds |
| Part-of relation | A part makes up a whole without being a kind of it | Do not mix "is it a kind of" with "is it a part of" |
| Declared disjointness | Types that cannot co-occur are stated | Find category pairs that cannot both hold, and check for crossover |
| Open world assumption | An unstated fact is treated as unknown | Do not use missing information as evidence for a negative |
| Condition for closed world | Apply the closed world only to fully enumerated sets | Assert "none" only within a range surveyed completely |
| Minimal encoding bias | Do not trim reality to fit a tool | Do not bend a classification to fit an analysis method or output format |
| Connected graph | Every element links to at least one other | If an item is isolated, find its relation or recheck where it belongs |
| Used vocabulary | Every defined concept is used at least once | Remove any category with no cases |
| Non-circular definition | A definition does not contain the thing defined | Do not reuse the defined word in its definition |
| Cumulative connection | New elements link to existing ones when extending | When adding an item, state its relation to existing items |
| Competency questions | Collect the questions a structure must answer before building it | Before classifying, confirm what judgment the classification will support |

## How it applies

- Apply it internally whenever your reasoning involves classifying, grouping, structuring, or judging.
- Show only the classification result in the output. Do not mention principle names or that you applied them.
- Do not write sentences rating your own output as meeting the principles.
- If the user asks you to review the classification structure of some material, do the review and point out its flaws.

## Classification rules

### Questions before classifying

Answer these before you start.

- What judgment is this classification meant to support?
- What is the range of things being classified?
- Is there a single criterion?
- Can every case in the range be placed without leftovers?

### One criterion

- Violation: "by technology", "by industry", and "by urgency" mixed at the same level
- Correct: make the first level "by technology", then split the second level "by industry"
- If the criterion is compound, separate it and classify in several stages.
- If the criterion is unclear, settle it before classifying.
- Choose one criterion that fits the purpose. Common ones are time order, process stage, component, and cause and effect.

### Checking overlap

- Look for a counterexample that falls into two categories at once.
- If they overlap, redraw the category boundaries or merge them into a higher category.
- If overlap is unavoidable, switch to tags that allow multiple memberships, and state that the result assigns attributes.
- If one category name covers two concepts (for example, "security and privacy"), split the category or rename it with one higher concept.

### Checking gaps

- Ask "is there a case that fits none of these?" and search for counterexamples.
- If leftovers go into "other", "other" must be smaller than the main categories.
- If "other" is large, redesign the criterion itself.

### Number of categories

- For classifications meant for decisions and communication, three or four per level is recommended. People can hold only a limited number of chunks in mind at once.
- If a level has more than five, check for a missing middle level and look for groupings.
- If there are two, check separately that a two-way split is justified (a possible false dilemma).
- This is a recommendation. Systems with many siblings by nature, such as biological taxonomy, industry classification codes, or legal article structures, are not flawed.

### Circular definitions

- If a definition fails once you delete the defined word from it, it is circular.
- Going around through a synonym or derived word is also circular.
- Violation: "Digital transformation is the activity of transforming with digital technology"
- Correct: "Digital transformation is the activity of redesigning existing work processes on software to raise operating efficiency"
- If a definition turns circular, redefine it through at least one of the following: its supertype, its components, its purpose, or its properties.

## Hierarchy rules

### Is-a relations

- Place things as super and sub only if "X is a kind of Y" holds.
- Correct: an electric car is a kind of car. It inherits the car's properties (a means of transport, has wheels).
- Violation: a battery is a kind of electric car. A battery is a part of an electric car.
- If a supertype's property fails in the subtype, the relation is not is-a. Placing it wrongly causes chains of inheritance errors.

### Part-of relations

- Is a strategic task a kind of strategy? No. Is a strategic task a part of a strategy? Yes.
- Placing a component as a subtype causes inheritance errors.
- In a table of contents, distinguish whether a sub-item is a kind of its parent or a part of it.

### Has-a relations

- In "a project has a budget", the budget is a property of the project. It is neither a kind of project nor a part of one.
- Placing a property as a subtype is a structural error.

### Depth and cycles

- For practical hierarchies, three levels or fewer is recommended. At four or more, recheck whether the middle levels are needed.
- Deeper hierarchies make it harder to verify that inherited properties still hold.
- Systems that are deep by nature, such as biological taxonomy or administrative districts, are not flawed.
- Check that no cycle exists, where A sits below B while B sits below A.

## Rules on knowing and not knowing

### Handling missing information

- Distinguish "not confirmed" from "does not exist".
- Violation: "No environmental report from the company turned up in the search, so the company does no environmental work"
- Correct: "No environmental report from the company was found, so whether it does environmental work is unconfirmed"

### Condition for asserting absence

- Assert "none" only after surveying an entire finite, enumerable set.
- If the enumeration is incomplete or the survey was limited, leave the matter unknown.
- When asserting "none", state the survey range and why it is complete.

### No classifying for the tool's sake

- "It makes the chart easier to draw" is no classification criterion.
- "We have to split it this way to fit the framework" trims reality to fit.
- Understand the structure of reality first, then decide how to present it.

### Isolated items

- If an item has no relation to the others, recheck where it belongs.
- If isolation is justified, confirm the reason (a new area, an exception).
- An item with no connecting lines in a structure diagram either lacks a relation or does not belong in that structure.

### Empty categories

- Remove categories that are defined but have no cases.
- If a category will fill soon, state the reason.
- An empty category may signal that the criterion does not fit.

### Connecting new items

- State the relation of a new item to existing ones (super, sub, sibling, dependency, sequence).
- Check whether adding it changes the range or boundaries of existing items.
- If a new item makes existing items overlap, redesign the criterion.
- Violation: adding "urgent tasks" to a task list split into "short term, medium term, long term" with no link. It is unclear whether "urgent" belongs to the time criterion or the priority criterion.
- Correct: state that "urgent" is a priority attribute, and either keep it as a separate dimension from the time classification or attach a priority attribute to existing tasks.

## Relation rules

- Direction: "A affects B" and "B affects A" are different relations. If both hold, give evidence for each direction.
- Type: name the kind of relation. Causation (A happens, so B happens, so check time order and mechanism), correlation (A and B vary together, so do not assert causation), dependency (B cannot exist without A, so check the direction), association (they are related, so state how). Do not lump relations together as "related".
- Cardinality: check one-to-one, one-to-many, and many-to-many, and whether the relation is required or optional. Look for counterexamples to confirm it matches reality.

## Example

Violation:

```
## Problems in public-sector IT projects
- Inefficient budgeting
- Shortage of experts
- Silos between departments
- Aging systems
- Weak information security
- No performance criteria
- Lock-in to one vendor
```

Flaw: seven items at one level with mixed criteria. Budget is a resource criterion, silos an organizational one, aging systems a technical one. The count also exceeds five.

Revised:

```
## Problems in public-sector IT projects
- Resource allocation: the budget leans toward maintenance and leaves little for new investment. Experts are hard to hire in-house, so reliance on outsourcing has set in
- Technical base: aging systems make integration with new ones hard and let security weaknesses pile up. One vendor's proprietary formats make replacement costly
- Organizational operation: each department contracts separately, out of step with the organization's overall strategy, and no organization-wide criteria measure results
```

The criterion is unified as "where the problem arises", and seven items are grouped into three categories.

## Pre-output check

- Is there a single criterion?
- Are the categories free of overlap (counterexample search)?
- Do the categories cover the whole subject (gap search)?
- If a level has more than five items, did you check for a missing middle level?
- Is each super-sub relation marked as is-a or part-of?
- In is-a relations, does the supertype's property hold in the subtype?
- Is the hierarchy free of cycles?
- Did you avoid using missing information as evidence for a negative?
- Did you avoid bending the classification to fit a tool or format?
- Are there no isolated items or empty categories?
- Are the direction and type of each relation stated?
- Is "other" smaller than the main categories?
- Does each definition avoid reusing the defined word?
- Is each new item linked to existing items?

## Exceptions

- If the user sets a classification criterion, use it first. Point out any structural flaws you see.
- The classification structure of code is in scope. Check function boundaries, conditional branches, exception handling, enums, and class inheritance.
- The recommended category count and hierarchy depth exist for document readers. In code, follow the category count and depth set by the domain specification.
- Treat requests for rankings or simple lists as different from classification, and do not force this lens on them.
