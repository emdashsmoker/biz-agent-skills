# Design rules

Rules for designing and checking an ontology. They apply to both thinking mode and engine mode. Use them while designing, and do not name the rules or say that you applied them in the output.

## Definitions, criteria, scope

Design starts from why the structure is built, what it holds and how it is divided. Set definitions, criteria and scope at a unit that cannot be split further, and keep their meaning until the work ends. If a word changes meaning halfway or definitions and criteria get mixed, nobody can reproduce the classification.

- Write down the purpose (why), the subject (what) and the method (how) first
- A definition says what the subject is, a criterion says how to divide it, and a scope says how far the work reaches. Keep the three in separate sentences
- Do not let common sense, authority, well-known frameworks or buzzwords stand in for a definition
- Do not write definitions that repeat the same content in other words

### Circular definitions

A definition that reuses the word it defines gives the reader nothing new. If the definition collapses once you delete the defined word from it, it is circular. Going around through synonyms or derived words is circular too.

- (Circular) "Digital transformation is a transformation that uses digital technology"
- (Circular) "Innovation capability is the capability to innovate"
- (Fixed) "Digital transformation is the redesign of existing business procedures on a software basis to raise operating efficiency"

To fix a circular definition, define the term through at least one of its parent concept, components, purpose or properties.

## Classification

### Pre-classification questions

Answer four questions before you classify. In engine mode these questions feed into the competency questions.

- What judgment will this classification support?
- What is the scope of the items being classified?
- Is there a single criterion?
- Can every case in scope be placed somewhere?

### One criterion

Divide the items of one classification by the same criterion. When items with different criteria sit side by side, one case can fall into several items or into none.

- (Mixed criteria) "By technology, by industry, by urgency" sit at the same level
- (Fixed) The first level divides by technology, and the second level divides by industry
- Choose the criterion to fit the purpose: time, procedure, composition or causation
- If several criteria are needed, split the levels into a multi-level classification
- If the criterion is unclear, settle it before classifying

### Overlap check

Test real cases to see whether one case fits two items at once.

- If a case overlaps, redraw the item boundaries or merge the items into a parent category
- If overlap cannot be avoided, switch to tags that let a case belong to several items, and state that the tags are attributes attached to each case

### Gap check

Check whether some case fits none of the items.

- Ask yourself whether any case falls outside this classification
- If leftover cases go into "Other", Other must be smaller than the main items
- If Other is large, redesign the criterion

In engine mode, a single DisjointUnion axiom can declare both no overlap and no gaps, and check_mece checks the entered individuals.

### Number of items

- For classifications used in reports and decisions, 3-4 items per level are recommended
- Above 5, check whether a middle level is missing and whether items can be grouped
- With 2 items, check whether other options exist (a false dilemma)
- In OWL class hierarchies, 2 to 12 direct subclasses is a common range. A single subclass signals a modeling problem, and more than 12 suggests a missing intermediate category
- These numbers are recommendations. Systems with many siblings, such as biological taxonomy, industry classification codes or legal article structures, count as normal structures

## Hierarchy

Hierarchical relations come in three kinds. Mixing them passes the properties of a parent to children that do not have them.

### Kind-of relation (is-a)

Put X under Y only if "X is a kind of Y" holds. The child inherits every property of the parent.

- (Holds) An electric car is a kind of car. The car's properties, being a vehicle and having wheels, hold for the electric car
- (Fails) A battery is a component of an electric car, so it fails the kind-of test
- If a parent's property does not hold for the child, the relation is not kind-of

### Part-of relation

"Is X a part of Y" is a different question from kind-of.

- A strategic task is a part that makes up a strategy. Asked "is a strategic task a kind of strategy", the answer fails
- Placing a component as a subclass passes the wrong properties down
- When you build a table of contents, tell whether each child is a kind of its parent or a part of it

### Has-a relation

Keep has-a relations, where an individual holds an attribute, apart from kind-of and part-of. In "a project has a budget", the budget is an attribute the project holds. Placing an attribute as a subclass breaks the structure.

### Depth

- In practice, up to 3 levels are recommended
- At 4 or more levels, ask again whether the middle levels are needed. Deeper hierarchies make it harder to confirm that parent properties hold at the bottom
- Deep systems such as biological taxonomy or administrative districts count as normal structures

## Relations

### Direction

Relations have a direction. "A affects B" and "B affects A" are different relations and each needs its own support. A relation stated without a direction is ambiguous.

### Type

Name the type of a relation instead of lumping it together as "related".

| Type | Meaning | What to confirm |
|---|---|---|
| Causal | B happens because A happens | Time order and mechanism |
| Correlational | A and B change together | Do not claim causation |
| Dependency | B cannot exist without A | Direction of the dependency |
| Association | A and B are connected | The specific nature of the connection |

### Quantity constraints

- Decide whether the relation is 1:1, 1:N or N:M
- Decide whether the relation is required or optional
- Test the constraint against real cases

In engine mode, directions and quantity constraints become property characteristics (transitive, functional, symmetric, asymmetric, irreflexive) and cardinality axioms. See references/axiom-patterns.md.

## Handling unknowns

### Open world assumption

Treat facts that are not stated as unknown. Tell "not confirmed" apart from "does not exist", and never use missing information as evidence of absence. OWL follows the same assumption.

- (Wrong inference) "No ESG report was found for the company, so it is judged to have no ESG activity"
- (Fixed) "No ESG report was confirmed for the company, so its ESG activity is unconfirmed"

### Switching to a closed world

Conclude "none" only within a scope where a full survey is done.

- Assert absence only when a countable, finite set was examined completely
- If the listing is incomplete or the survey was limited, keep the matter unknown
- When switching to a closed world, state the surveyed scope and why you consider it complete

In engine mode this rule shows up in three ways.

- Check functions and SPARQL checks read only the entered facts. Report unlinked items in their results as missing-entry candidates
- OWL reasoners do not treat a missing link as a problem. Minimum cardinality axioms and classification by a Not condition cannot catch links that were never entered
- When the user confirms that the entries in a scope are complete, declare that scope closed with close_world_scope and then run the reasoner

## Structure checks

### Reality first

Do not bend the real classification to fit an analysis method or output format. "Easy to chart" and "needed to fit this framework" cannot serve as classification criteria. Understand the real structure first, then choose how to present it. In engine mode, do not add properties to make a query or reasoner work.

### Isolated items

Every item must connect to another item through at least one relation.

- If an item has no relation to the others, review where it belongs
- If isolation is justified, confirm the reason (a new area, an exception)
- An item with no connecting line in a structure diagram either has a missing relation or does not belong to that structure

### Unused categories

Every defined category must hold at least one case.

- An empty category is a candidate for deletion
- If it will be filled later, state the basis
- An empty category can itself signal that the criterion does not fit
- In engine mode, every class must take part in at least one object property as domain or range

### Cumulative linking

When adding a new item to an existing structure, state its relation to the existing items. A new item attached on its own breaks the structure.

- Write down how the new item relates to existing ones (parent, child, sibling, dependency, sequence)
- Check whether the new item changes the scope or boundary of existing items
- If the new item breaks the no-overlap property of existing items, redesign the criterion
- (Broken addition) An "urgent tasks" item is added to a list divided into short, mid and long term without stating its relation. Nobody can tell whether "urgent" is a time criterion or a priority criterion
- (Linked addition) State that "urgent" is a priority criterion and keep it as a separate classification, or attach a priority attribute to the time-based tasks
- In engine mode, do not discard the ontology each time. Load the existing OWL file, extend it, and link new individuals to existing ones

### Versions and metadata

- When extending cumulatively, it must be possible to see what changed from the previous version (diff_ontology in engine mode)
- Record label, versionInfo and comment metadata so external tools can read them

## Examples

### Example 1. Mixed criteria and overlap

(Before)

```markdown
## Problems of public-sector IT projects
- Inefficient budgeting
- Lack of skilled staff
- Silos between departments
- Aging legacy systems
- Weak information security
- No performance evaluation system
- Vendor lock-in
```

Seven items share one level with mixed criteria. Budgeting is a resource problem, silos are an organizational problem, and aging systems are a technical problem. Lack of staff and missing performance evaluation can overlap from a workforce view.

(After)

```markdown
## Problems of public-sector IT projects
- (Resource allocation) IT budgets go mostly to maintenance, leaving little for new projects, and skilled staff are hard to hire in-house, so reliance on outsourcing has become fixed
- (Technical base) Aging systems do not connect to new ones and security weaknesses pile up, and a vendor's proprietary formats make replacement costly
- (Organizational operation) Each department contracts on its own, drifting from the organization-wide IT strategy, and there is no organization-level measure of IT performance
```

The criterion is now one: "where the problem arises". Weak security and vendor lock-in moved to the technical base, and the missing performance evaluation moved to organizational operation, removing the overlap.

### Example 2. Confusing kind-of and part-of

(Before)

```markdown
## Smart city framework
- Smart city: smart transport, smart energy, smart safety, integrated platform, urban data hub, citizen participation governance, IoT sensor network
```

Smart transport is a kind of smart city service. The integrated platform and the IoT sensor network are parts of the smart city. Citizen participation governance is an operating structure the smart city has. Three relations are mixed in one list.

(After)

```markdown
### Service areas (types of smart city services)
- (Smart transport) Controls signals and adjusts public transit with real-time traffic data
- (Smart energy) Meters building energy use and manages distributed energy resources
- (Smart safety) Detects disasters early from CCTV video analysis and triggers emergency response

### Infrastructure (technical parts of the smart city)
- (Integrated platform) Software that links data across services and runs integrated monitoring
- (Urban data hub) Data store that collects, keeps and publishes city operations data
- (IoT sensor network) Device network that collects field data and sends it to the platform

### Operating structure (decision structure for running the smart city)
- (Citizen participation governance) Procedure that brings citizen input into service planning and evaluation
```

The parentheses in each section title name the kind of relation in plain language. Terms such as is-a and part-of stay out of the output.

### Example 3. Turning missing information into absence

(Before)

```markdown
## AI adoption in manufacturing
- (Large firms) Run in-house AI labs and use AI heavily for process optimization
- (Mid-sized firms) Some adopted AI for quality inspection, but adoption is low
- (Small firms) Almost no adoption cases and low awareness
- (Micro businesses) No capacity at all to adopt AI, so excluding them from policy support is realistic
```

"Almost no cases" for small firms asserts absence without a systematic survey. "No capacity at all" for micro businesses uses missing information as evidence of absence and then even sets a policy direction. The size-based classification may also have been reverse-engineered to fit the conclusion.

(After)

```markdown
## AI adoption in manufacturing
- (Large firms) Many cases report in-house AI labs applying AI to process optimization and quality prediction, and the scope and results differ across public sources
- (Mid-sized firms) Cases of AI in specific processes such as quality inspection are confirmed, and the adoption rate needs a systematic survey
- (Small firms) No full survey was confirmed, so judgment on the adoption level is withheld, and there are cases of adoption attempts through government support programs
- (Micro businesses) No systematic survey of adoption capacity was confirmed, so judgment is withheld, and exclusion from policy support can be decided only after survey results exist
```

### Example 4. Circular definitions

(Before)

```markdown
- (Digital transformation) Transformation activity using digital technology
- (Data governance) A system that governs data
- (AI capability) The capability to do AI
- (Cloud native) An architecture designed in a cloud-native way
```

(After)

```markdown
- (Digital transformation) The redesign of existing business procedures on a software basis to raise operating efficiency
- (Data governance) Policies and procedures that manage the quality, access rights and life cycle of data in an organization
- (AI capability) An organization's technical readiness to pick AI models that fit its tasks and deploy them in operation
- (Cloud native) An architecture built on containers, microservices and declarative APIs to be scalable and resilient
```

Each definition drops the defined word and uses a parent concept (activity, policies and procedures, readiness, architecture), components (software, containers) and purpose (operating efficiency, scalability).

### Example 5. An isolated new item

(Before)

```markdown
## Digital transformation tasks (round 2)
- (Short term) Automate business procedures
- (Mid term) Build a data analysis environment
- (Long term) Introduce AI-based decision making
- (New) Strengthen security
- (New) Innovate organizational culture
- (New) Manage ESG data
```

The three new tasks have no stated relation to the time-based criterion. Nobody can tell whether security is short or mid term, or whether ESG data management comes before, after or alongside the data analysis environment.

(After)

```markdown
## Digital transformation tasks (round 2)
- (Short term) Automate business procedures and define the security requirements of the systems being automated first
- (Mid term) Build the data analysis environment with ESG data in its collection scope, and set data-sharing rules across departments to drive the culture change along with it
- (Long term) Design AI-based decision making on top of the security policy and data analysis environment secured in the short and mid term
```

The time criterion stays, and each new task links to an existing task of the same period through dependency and sequence relations.

## Sources for the design principles

| Principle | Source |
|---|---|
| Reality first (minimal encoding bias) | Gruber, T. R. (1995), Toward principles for the design of ontologies used for knowledge sharing, International Journal of Human-Computer Studies 43(5) |
| Competency questions | Grüninger, M. and Fox, M. S. (1995), The Role of Competency Questions in Enterprise Engineering. Noy, N. F. and McGuinness, D. L. (2001), Ontology Development 101 |
| Kind-of versus part-of, number of direct subclasses | Noy, N. F. and McGuinness, D. L. (2001), Ontology Development 101 |
| Open world assumption | W3C (2012), OWL 2 Web Ontology Language Primer, section 2 |
| One axiom for no overlap and no gaps | W3C (2012), OWL 2 Structural Specification, section 9.1.4 DisjointUnion |
| Isolated elements, circular definitions, missing disjointness | OOPS! ontology pitfall catalogue P04, P24, P10 |
| No overlap and no gaps (MECE) | Classification principle formulated by Barbara Minto at McKinsey |
| 3-4 items, 3 levels | Practical recommendations for reports and decisions |

## Checklist

Check outputs that contain classification, grouping, structure or judgment.

- Is the classification criterion unified into one?
- Does no case overlap two items?
- Does no case fall outside every item?
- If a level has more than 5 items, was a missing middle level checked?
- Are hierarchical relations marked as kind-of or part-of?
- In kind-of relations, do parent properties hold for the child?
- Was missing information never used as evidence of absence?
- Was the classification left unbent by analysis tools or output formats?
- Are there no isolated items without relations?
- Are there no empty categories without cases?
- Do relations have a set direction and type?
- Is "Other" smaller than the main items?
- Does no definition reuse the word it defines?
- Are new items linked to existing items?

## Exceptions

- When the user sets the classification criterion, apply it first, and report any structural defect you find
- The classification structure of code is in scope. Check function boundaries, conditional branches, exception handling, enums, and class inheritance
- A request for a plain list, such as a ranking, differs from a classification, and these rules do not have to be enforced on it
