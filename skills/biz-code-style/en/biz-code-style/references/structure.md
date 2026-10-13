# Classification and hierarchy design

These rules apply to any thinking that involves classification, grouping, structuring, or judgment. Splitting functions, classifying exceptions, designing enums, data models, chart categories, screen division, tables of contents, and lists inside sentences are all in scope. The rules carry ontology design principles over as a discipline of thought. Building OWL models and running reasoners are out of scope.

## Principles

| Principle | Original definition | How it applies to thinking |
|-----------|--------------------|-----------------------------|
| Mutual exclusion | The intersection of categories is empty | If one case falls into two categories at once, redesign the classification criterion |
| Collective exhaustion | The union of categories covers the whole subject | If a case falls into no category, the classification is incomplete |
| Single classification criterion | One classification uses a criterion of one dimension | Do not mix items of different dimensions in one classification |
| Kind-of relation (is-a) | A subconcept inherits every property of its superconcept | Place items as upper and lower only if "Is X a kind of Y?" holds |
| Part-of relation | A part is a component of the whole | Distinguish "Is X a kind of Y?" from "Is X a part of Y?" |
| Disjoint classes | Declare types that cannot hold at the same time | Find category pairs that cannot hold together and check for overlap |
| Open world assumption | A fact not stated is treated as unknown | Do not use the absence of information as evidence of absence |
| Closed world condition | Apply a closed world only to fully enumerated sets | State "none" only within a range that has been fully surveyed |
| No tool bias | Do not cut reality to fit the tool | Do not distort a classification to fit an analysis method or output format |
| Connected graph | Every entity is linked to at least one other by a relation | Find relations for isolated items or reconsider where they belong |
| Used vocabulary | Every defined concept is used at least once | Delete categories with no cases |
| Non-circular definition | The definition does not contain the thing defined | Do not reuse the defined word in its definition |
| Ontology integration | When extending, link new entities to existing ones by relation | When adding a category, state its relation to existing categories |
| Competency questions | Before building, collect the questions the structure must answer | Before classifying, confirm what judgment the classification should support |

## How to apply

- These principles work inside the reasoning process. The output shows only the classification result and does not reveal principle names or the fact that they were applied.
- If the user asks for a review of the classification structure of something under analysis, carry out that review as asked.
- Do not write sentences that evaluate your own classification as meeting the principles.

## Classification rules

### One criterion

- Use one dimension as the criterion within one classification. Do not mix "by technology, by industry, by urgency" at one level. Classify first "by technology", then split "by industry" at the second level.
- If the criterion is compound, separate the criteria and classify in several levels.
- If the criterion is unclear, fix it before classifying.

### Checking overlap

- Check whether one case falls into two categories by searching for counterexamples.
- If there is an intersection, redraw the category boundaries or merge them into a higher category.
- If the intersection cannot be avoided, switch to tags that allow membership in several places and state that this is attribute tagging.

### Checking gaps

- If a case falls into no category, the classification is incomplete. Ask yourself "Is there a case that does not fit this classification?"
- If leftovers go into "Other", Other must be smaller than the main categories. If Other is too large, redesign the criterion itself.

### Number of categories

- For classifications meant for decisions and communication, 3-4 per level is recommended.
- Above five, check whether a middle level is missing and whether items can be grouped.
- With two, check separately whether the dichotomy is valid (whether it is a false dilemma).
- Systems where more than five siblings are natural, such as biological taxonomy, industry classification codes, and legal article structures, are not structural defects.

### Questions before classifying

- What judgment is this classification meant to support?
- How far does the scope of this classification reach?
- Is the classification criterion one-dimensional?
- Can every case within the scope be placed without omission?

### Preventing circular definitions

- If a definition no longer holds when the defined word is removed from it, it is circular. Detours through synonyms or derived words count too.
- "Digital transformation is activity that transforms using digital technology" is circular. Write it with attributes and actions and without the defined words, such as "activity that redesigns existing business processes around software to raise operating efficiency".
- If a definition is circular, redefine it using one or more of the superconcept, components, purpose, or attributes.

## Hierarchy rules

- (Kind-of) Place items as upper and lower only if the properties of the superconcept (a means of transport, has wheels) also hold for the subconcept, as in "An electric car is a kind of car". "A battery is a kind of electric car" does not hold. A battery is a component of an electric car.
- Placing something as kind-of when it is not causes property inheritance errors that cascade.
- (Part-of) A strategic task is a part that makes up a strategy, so do not place it as a subcategory of strategy. Misplacing components as subcategories causes property inheritance errors. In tables of contents too, distinguish whether a lower item is a kind of or a part of the upper item.
- (Attribute) In "A project has a budget", the budget is an attribute the project has. Do not place attributes as subcategories.
- In code, carry kind-of relations over as inheritance, and part-of and attribute relations as composition or fields.
- A practical hierarchy depth is three levels or fewer. At four or more, reconsider whether a middle level is needed. Systems where deep hierarchies are natural, such as biological taxonomy and administrative districts, are not defects.

## Judgment rules

- (Missing information) Distinguish "not confirmed" from "does not exist". Do not write "No ESG report was found, so the company does no ESG activity". Write "No ESG report was confirmed, so whether the company does ESG activity is unconfirmed".
- (Asserting absence) Assert absence only when a finite, enumerable set has been fully surveyed, and state the survey scope and the basis for completeness. If the enumeration is incomplete, leave it as unknown.
- (Tool bias) "Easy to chart" and "this is how it must be split to fit the framework" are not classification criteria. Understand the structure of reality first, then decide how to express it.
- (Isolated items) Reconsider where an item with no relation to other items belongs. If the isolation is justified, confirm the reason, such as a new area or an exception. In a structure diagram, an item with no connecting lines either has a missing relation or does not belong to that structure.
- (Empty categories) Delete categories that are defined but have no cases. If they may be filled later, state the basis. An empty category can signal an unsuitable criterion.
- (Ontology integration) When adding an item to an existing classification, state its relation to existing items (upper, lower, parallel, dependency, sequence). Check whether the new item changes the boundaries of existing items. If the new item creates overlap, redesign the criterion.

## Relation rules

- (Direction) "A affects B" and "B affects A" are different relations. If both hold, give evidence for each direction separately.
- (Type) Distinguish causation (A happens and B follows, check timing and mechanism), correlation (A and B change together, do not assert causation), dependency (B cannot exist without A, check the direction of dependency), and association (A and B are related, state the specific nature). Do not lump them together as "related".
- (Cardinality) State whether a relation is 1:1, 1:N, or N:M, and whether it is mandatory or optional, and check against reality with counterexamples.

## Examples

Chart categories (before): A chart of problems in IT projects shows seven bars side by side: inefficient budgeting, lack of skilled staff, silos between departments, aging legacy systems, weak information security, no performance evaluation system, and vendor lock-in. Resource, organization, and technology dimensions are mixed at one level.

Chart categories (after): Unify the criterion as "the area where the problem arises" and group them into three categories: resource allocation (budgeting, staff), technology base (aging systems, information security, vendor lock-in), and organizational operation (silos between departments, performance evaluation).

Data model (before): Under the `SmartCity` class, `Transport`, `Energy`, `Safety`, `IntegratedPlatform`, `IoTSensorNetwork`, and `CitizenGovernance` are all subclasses.

Data model (after): Transport, energy, and safety are kinds of service, so they are subclasses of `Service`. The integrated platform and sensor network are parts that make up the city, so they are composition fields of `SmartCity`. Citizen participation governance is an operating system the city has, so it is an attribute field.

Enum extension (before): `URGENT` was added to `Term = {SHORT, MID, LONG}`. Urgency is a different dimension from duration, so it creates overlap inside one enum.

Enum extension (after): Create a separate enum `Priority = {URGENT, NORMAL}` and give task data separate fields for duration and priority.

## Checklist

- Is the classification criterion unified in one dimension?
- Is there no intersection between categories (counterexample search)?
- Do the categories together cover the whole subject (gap search)?
- If one level has more than five items, did you check for a missing middle level?
- Are upper and lower relations distinguished as kind-of or part-of?
- In kind-of relations, do the upper properties hold for the lower?
- Did you avoid using the absence of information as evidence of absence?
- Did you avoid distorting the classification to fit an analysis tool or output format?
- Are there no isolated items without relations?
- Are there no empty categories without cases?
- Are the direction and type of relations specified?
- Is "Other" smaller than the main categories?
- Does the defined word stay out of its definition?
- Are new items linked to existing items by relation?

## Exceptions

- If the user specifies a classification criterion, apply it first and report any structural defect you find.
- Code itself is exempt. Apply these rules to the design structure of code and to explanatory text.
- Requests for rankings or simple lists are distinct from classification, and these rules are not enforced on them.
