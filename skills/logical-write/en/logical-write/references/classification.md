# Classification and definitions

> Translated from the Korean original. See the translation notice in SKILL.md.

These thinking rules apply when you split, group, or define items. They carry principles from ontology design over into writing. Building ontology models or running reasoners is out of scope. Show only the result of the classification in the output, with no principle names and no mention of applying them.

## Principles

| Principle | Original meaning | Writing rule |
|---|---|---|
| Mutual Exclusion | Classification items share no members | When one case falls into two items at once, redesign the criterion |
| Collective Exhaustion | The union of the items covers the whole subject | When a case fits no item, the classification is incomplete |
| Single Classification Axis | One classification uses one dimension | Do not mix items from different dimensions in one classification |
| is-a Hierarchy | A child concept inherits every property of its parent | Place items as parent and child only when "X is a kind of Y" holds |
| part-of Composition | A part makes up a whole but is not a kind of the whole | Do not confuse "X is a kind of Y" with "X is a part of Y" |
| Disjoint Classes | Mutually exclusive types are declared explicitly | Find category pairs that cannot overlap and check them for crossings |
| Open World Assumption | The truth of an unstated fact stays unknown | Do not use the absence of information as evidence of absence |
| Closed World condition | Closed-world reasoning applies only to fully enumerated sets | Assert "none" only within a range that has been fully surveyed |
| Minimal Encoding Bias | Concepts are not defined to suit a particular encoding | Do not bend a classification to fit an analysis method or output format |
| Connected Graph | Every entity has at least one relation to another | When an item stands isolated, look for its relations or reconsider where it belongs |
| Used Vocabulary | Every defined concept is used at least once | Delete classification items that are never used |
| Non-circular Definition | A definition does not contain the concept it defines | Do not reuse the defined word inside its definition |
| Ontology Integration | New entities join existing ones through relations when the model grows | When you add a classification item, state its relation to existing items |
| Competency Question | Collect the questions the structure must answer before building it | Before classifying, confirm what judgment the classification should support |

## Classification rules

### Questions before classifying

- What is the purpose of this classification? Which judgment should it support?
- How far does the scope of the subject extend?
- Is the criterion a single dimension?
- Can every case within the scope be placed without omission?

### One axis

- Use one dimension for the criterion within one classification. Do not mix "by technology", "by industry", and "by urgency" at the same level.
- When a criterion is compound, split it into a multi-stage classification. Classify by technology first, then by industry at the second stage.
- When the criterion is unclear, settle it before classifying.
- Choose one axis that fits the purpose. Time, process, structure, and causation are common axes.

### Overlap check

- Look for counterexamples to see whether one case falls into two items at once.
- When an overlap appears, redraw the item boundaries or merge into a higher category.
- When overlap cannot be avoided, switch to tags that allow membership in several items, and state that the result assigns attributes.

### Gap check

- Ask "Is there a case this classification does not cover?" If so, the classification is incomplete.
- When you put leftovers in "Other", keep "Other" smaller than the main items. When "Other" is large, redesign the criterion.

### Number of items

- For classifications meant for decisions and communication, three or four items per level are recommended.
- At five or more, check whether an intermediate level is missing and whether the items can be grouped.
- With two, verify separately that the dichotomy holds (check for a false dilemma).
- This guideline is a recommendation. Systems with five or more siblings by nature, such as biological taxonomy, industry classification codes, or statute structures, have no structural defect.

### No circular definitions

- When deleting the defined word from its definition makes the definition collapse, the definition is circular.
- Detours through synonyms or derived forms are also circular.
- A circular definition conveys no new information.
- When a definition goes circular, redefine it through one or more of: the higher concept, components, purpose, or attributes.

| Circular definition | Revised definition |
|---|---|
| Digital transformation: transformation using digital technology | Activity that redesigns existing work processes on a software basis to improve operational efficiency |
| Data governance: a system for governing data | Policies and procedures that manage the quality, access rights, and life cycle of data within an organization |
| AI capability: capability to perform AI | An organization's technical readiness to choose AI models that fit business goals and apply them in operations |
| Cloud native: architecture designed in a cloud-native way | Architecture designed on containers, microservices, and declarative APIs to secure scalability and resilience |

## Hierarchy rules

- (is-a, classification hierarchy) Check that parent and child satisfy "X is a kind of Y". An electric car is a kind of car, so it inherits a car's properties such as being a means of transport with wheels. A battery is a component of an electric car and cannot be a kind of electric car. When a parent's properties do not hold in the child, the is-a relation fails. A misplaced item sets off a chain of inheritance errors.
- (part-of, composition hierarchy) Distinguish "X is a part of Y" from "X is a kind of Y". A strategic task is a part of a strategy and cannot be a kind of strategy. In tables of contents, distinguish whether a child item is a kind or a part of its parent.
- (has-a, attribute) Do not confuse an entity holding an attribute with is-a or part-of. A budget is an attribute a project holds. Placing an attribute as a subclass is a structural error.
- (Depth) Three levels or fewer are recommended for practical use. At four or more, check whether the intermediate levels are really needed. Deep systems such as biological taxonomy or administrative districts have no defect.

## Information and judgment rules

- (Missing information) Leave the truth of an unstated fact unknown. Distinguish "not confirmed" from "does not exist". "The company's ESG report was not found, so it does no ESG activity" is wrong, and "The company's ESG report was not confirmed, so its ESG activity is unconfirmed" is right.
- (Switching to a closed world) Assert absence only after a full survey of an enumerable, finite set. When the survey range is limited, leave it unknown. When you assert absence, state the survey range and the grounds for completeness.
- (Tool bias) Do not reshape the real classification to fit an analysis method or output format. "A classification that makes the chart easy" or "a classification needed to fit this framework" cuts reality to size. Understand the real structure first and decide the presentation later.
- (Isolated items) Every item needs at least one relation to another item. Reconsider where an unrelated item belongs. When isolation is justified, as with a new area or an exception, confirm the reason. An item with no connecting line in a structure diagram either lacks a relation or does not belong to that structure.
- (Empty categories) Every defined category needs at least one case. Delete categories without cases. When there are grounds to expect future cases, state them. An empty category can signal an unsuitable criterion.
- (Cumulative linking) When you add a new item to an existing classification, state its relation to existing items (parent, child, parallel, dependency, sequence). Check whether the scope or boundaries of existing items change. When the new item breaks the no-overlap property of existing items, redesign the criterion. When you add "urgent tasks" to a short-term, mid-term, long-term task system, state whether urgency belongs to the time axis or a priority axis, and either separate it as its own dimension or attach a priority attribute to existing items.
- (Facts and judgments) Do not mix facts and judgments in one classification.

## Relation rules

- (Direction) Relations have direction. "A affects B" and "B affects A" are different relations. When both hold, give grounds for each direction. Relations stated without direction cause ambiguity.
- (Type) Specify the nature of the relation. Causation means A happens and then B happens, and needs verification of sequence and mechanism. Correlation means A and B vary together, and must not be asserted as causation. Dependency means B cannot exist without A, and needs the direction confirmed. Association means A and B are related, and needs the specific nature stated. Do not lump everything into "is related".
- (Constraints) Check whether a relation is one-to-one, one-to-many, or many-to-many, and whether it is mandatory or optional. Test the constraints against reality with counterexamples.

## Examples

### Mixed axes

```markdown
Before
## Problems in public agency IT projects
- Inefficient budgeting
- Shortage of specialists
- Silos between departments
- Aging systems
- Weak information security
- No performance evaluation system
- Lock-in to a specific vendor

After
## Problems in public agency IT projects
- (Resource allocation) IT budgets tilted toward maintenance leave little room for new projects
    + Difficulty hiring specialists in-house entrenches dependence on outsourcing
    + Budgets split by project cause duplicate investment
- (Technology base) Aging systems hinder links with new systems and accumulate security weaknesses
    + Security measures stay reactive because of the structural limits of aging systems
    + Proprietary specifications of a specific vendor make system replacement costly
- (Organizational operation) Separate procurement by each department weakens alignment with the agency-wide IT strategy
    + Silos between departments keep shared use of systems and data low
    + No agency-level criteria to measure IT performance
```

The original puts seven items from the resource, organization, and technology dimensions at one level. The revision groups them on one axis, "where the problem arises", into resource allocation, technology base, and organizational operation, and moves the rest down a level.

### Confusing is-a and part-of

```markdown
Before
## Smart city program
- Smart city
    + Smart transport
    + Smart energy
    + Smart safety
    + Integrated platform
    + Urban data hub
    + Citizen participation governance
    + IoT sensor network

After
## Types of smart city services
- (Smart transport) Traffic signals and transit operations adjusted with real-time traffic data
- (Smart energy) Building energy use measured and distributed energy resources managed
- (Smart safety) Early detection of disaster signs through video analysis, with emergency response

## Technical infrastructure of a smart city
- (Integrated platform) Software layer for data links and integrated control across services
- (Urban data hub) Data layer for collecting, storing, and opening urban operations data
- (Sensor network) Physical layer that collects field data and sends it to the platform

## Operating system of a smart city
- (Citizen participation governance) Decision structure that feeds citizen input into service planning and evaluation
    + Quarterly citizen panels select service improvement tasks
    + Panel results reflected in the next year's service planning
```

The original mixes three relations at one level: kinds of service, parts of the infrastructure, and the operating system. The revision splits sections by relation and keeps one relation per section. Relation names (is-a, part-of) stay out of the output and show up in plain language in the headings.

### Turning missing information into absence

```markdown
Before
## AI adoption in domestic manufacturing
- (Large firms) Run their own AI research teams and actively use AI for process optimization
- (Mid-sized firms) Some adopted AI for automated quality inspection, but the adoption rate is low
- (Small firms) Almost no adoption cases and low awareness
- (Microbusinesses) No capacity for AI adoption at all, so excluding them from policy support is realistic

After
## AI adoption in domestic manufacturing
- (Large firms) Many reported cases of AI applied to process optimization and quality prediction by in-house AI research teams
- (Mid-sized firms) Cases confirmed of AI adoption in specific processes such as automated quality inspection
- (Small firms) No full survey of AI adoption confirmed, so judgment on adoption level withheld
- (Microbusinesses) No systematic survey of AI adoption capacity confirmed, so judgment withheld
```

The original asserts absence ("almost none", "none at all") without survey grounds and even concludes exclusion from policy. The revision turns the parts without full-survey grounds into "unconfirmed" and "judgment withheld".

## Checklist

- Is the classification criterion unified into one dimension?
- Did you look for counterexamples to confirm there is no overlap between items?
- Did you look for missing areas to confirm the whole is covered?
- With five or more items at one level, did you check for a missing intermediate level?
- Are parent-child relations distinguished as kind or part?
- In kind relations, do the parent's properties hold in the child?
- Did you avoid using missing information as evidence of absence?
- Did you avoid reshaping the classification to fit an analysis tool or output format?
- Are there no isolated items without relations to others?
- Are there no empty categories without cases?
- Are the direction and type of each relation specified?
- Is "Other" smaller than the main items?
- Does the defined word stay out of its own definition?
- Are new items linked to existing items through relations?

## Scope

- When the user specifies a classification criterion, apply it first. Tell the user when you find a structural defect.
- Code itself is out of scope. Apply the rules to the design structure of the code and to explanatory sentences.
- Simple lists such as rankings or catalogs are distinct from classifications, and these rules are not enforced on them.
