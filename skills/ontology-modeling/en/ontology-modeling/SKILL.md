---
name: ontology-modeling
description: Ontology modeling skill that designs definitions, classifications, hierarchies and relations with no overlap and no gaps, builds an OWL ontology with owlready2 when needed, checks it with SPARQL and the HermiT reasoner, and reports without meta commentary. Thinking mode checks the classification and reasoning of documents and plans, and engine mode produces OWL files. Use it when the user mentions "ontology", "OWL", "TBox", "ABox", "knowledge graph", "taxonomy", "MECE check", "is-a vs part-of", "competency question", "SPARQL", "HermiT" or "reasoner", or asks to structure complex concepts and relations or to check a classification or argument. Read references/modeling-rules.md when designing, references/reasoning-rules.md when checking arguments, and references/output-rules.md when reporting. In engine mode, also read references/tbox-templates.md, references/axiom-patterns.md, references/sparql-patterns.md and references/check-functions.md through scripts/load_references.py.
compatibility: Thinking mode needs no extra tools. Engine mode needs Python 3 and owlready2, and a Java runtime for the reasoners. HermiT was tested on Java 21. The Pellet libraries bundled with owlready2 0.50 and later need Java 25 or later.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Ontology Modeling

> This English version was translated from the Korean original. Wording and examples may not carry the original intent exactly, so the skill can behave differently from the Korean version.

Structure the concepts, classifications, relations and facts of a subject with no overlap and no gaps, then confirm that the structure answers the questions it has to answer. The LLM interprets language and designs the structure. Python code runs the rule checks and the reasoning. Decisions that involve interpretation go into the model only after the user agrees.

There are two ways to build the structure. Thinking mode builds it without code, as definition lists, classification tables and relation statements, and checks the logic of a document or plan. Engine mode builds it as an OWL file and checks it with SPARQL queries and an OWL reasoner. Both modes follow the same design rules and report rules.

## Terms

These terms keep the same meaning in this file and in every reference file.

| Term | Meaning |
|---|---|
| Ontology | The structure that holds the concepts, classifications, relations and facts of the subject. Thinking mode expresses it as definitions and tables in text; engine mode expresses it as an OWL file |
| Class | A group of individuals that share properties (for example Strategy, Goal) |
| Individual | One member of a class (for example one specific strategy) |
| Object property | A relation between two individuals (for example a strategy achieves a goal) |
| Data property | A value attached to an individual (for example a budget amount) |
| TBox | Definitions of classes and properties (the schema) |
| ABox | Links between individuals and their values (the facts) |
| Axiom | A constraint that a reasoner uses (for example two classes do not overlap) |
| Competency question (CQ) | A concrete question the ontology must be able to answer |
| Fact property | A value anyone would accept after reading the original source (names, numbers, affiliations, dates) |
| Judgment property | A value assigned through interpretation (for example "A counts as B") |
| Missing-entry candidate | An item whose link is not found in the entered facts. Whether the link exists in reality stays unknown |
| Violation | An item where the entered facts conflict with a stated rule or axiom |

## Working principles

Every extra step adds work for the user and cost for the task. Run a step only when it meets all three conditions below. If it fails any of them, drop it or merge it into another step.

- (Necessity) Without this step the output would get worse in a real way
- (Feasibility) The user can run it with the resources they have now. If the constraints are unclear, ask first
- (Proportionality) The effort of the step is smaller than the value it produces

Apply the conditions as follows.

- Do not ask again about a problem, direction, path or competency question the user already set. Do not reopen what was already agreed in the same conversation
- Do not split work that one action finishes into several steps
- Put all questions for the user into one message
- Keep steps with high sensitivity, such as legal, regulatory or safety steps, whatever the three conditions say
- Keep the engine mode agreement checkpoints as well: the TBox design, the ABox entry plan, entering judgment properties, and applying SWRL rules. Skipping them stores the LLM's interpretation as if it were fact
- When the user explicitly asks for the detailed or full process, lift these principles. When the user states constraints, judge feasibility by them

## Workflow

Work moves through mode selection, design, build, check and report. Read only the reference files each stage needs.

| Stage | What happens | Thinking mode | Engine mode | Reference |
|---|---|---|---|---|
| 0. Mode selection | Choose the mode and path, collect competency questions | Answer the pre-classification questions | Choose the path, collect competency questions | this file |
| 1. Design | Set purpose, definitions, criteria, scope, classifications and relations | applies | applies | modeling-rules.md |
| 2. Build | Write down the designed structure | Definition lists, classification tables, relation statements | TBox, ABox, axioms | tbox-templates.md, axiom-patterns.md |
| 3. Check | Check the structure and the arguments | Structure check, argument check | Structure check, argument check, check functions, SPARQL, reasoner | reasoning-rules.md, check-functions.md, sparql-patterns.md |
| 4. Report | Deliver the results to the reader | applies | applies, plus saved files and Mermaid diagrams | output-rules.md |

## Stage 0. Mode selection

### Choosing the mode

If the mode and path were already agreed in the same conversation, skip this stage and go to design or build.

Engine mode pays off when one or more of these six apply.

- (Knowledge structuring) Relations among many individuals must be formalized and understood as a structure
- (Relation exploration) Causal chains, path tracing, backward tracing or impact ranges are needed
- (Pattern discovery) Structural patterns such as shared targets, missing links or cycles must be found across many individuals
- (Automatic classification) The type of an individual must be decided from a combination of its values
- (Structure check) Cross references, allowed combinations, coverage or broken sequences must be checked in full
- (Cumulative knowledge) Complex domain knowledge must be built up and reused over several turns

Thinking mode is likely more efficient when these apply.

- The items are an independent list with no relations among them
- Interpreting the language is enough for the qualitative judgment
- The relation structure is simple (fewer than 5 classes and fewer than 3 properties)

If the request names an OWL file, TBox, SPARQL or a reasoner, use engine mode. If the request is to check the classification or reasoning of a document or plan, use thinking mode. If there is no engine mode signal but the user wants an ontology built, do not refuse. Offer two options, direct analysis without building and building an ontology followed by reasoning, with the expected effort and the difference in analysis scope.

In thinking mode, answer four questions before you classify: What judgment will this classification support? What is the scope? Is there a single criterion? Can every case in scope be placed? Ask the user only when the request does not answer them.

### Engine mode paths

| Path | Build | Analysis | When analysis runs | Fits when |
|:---:|:---:|:---:|---|---|
| A | O | X | never | Only knowledge structuring is needed |
| B | O | O | In the same turn as the ABox build (one-turn option: everything in one turn) | The user wants results fast |
| C | O | O | In a separate turn after the ABox build | The user wants to review the build before analysis |
| D | X | O | right away, without a build | The user only queries an existing OWL file |

- (Path A) Turn 1 builds the TBox, shows a Mermaid class diagram and the OWL file, and asks the user to confirm the structure. Turn 2 builds the ABox, shows a Mermaid instance graph, gets confirmation, saves the OWL file and ends. Skip every analysis, including SPARQL query suggestions, suggest_sparql_queries and suggest_axioms
- (Path B) Ask whether to split the TBox and ABox. If split, confirm the TBox, then build the ABox and analyze in the same turn. Allow one turn only when the user says they want fast results without checking the TBox first. Even then, the reality-first rule of the design stage still applies
- (Path C) Turn 1 TBox, turn 2 ABox, turn 3 analysis. Build turns skip all analysis. Recommend it when there are many judgment properties or when the user wants to set the analysis scope after seeing the build
- (Path D) Load the existing OWL file, skip the build and go to the check stage

If the request makes the path clear, take that path without asking and state it in one line. Otherwise show the table and ask, so the user chooses knowing what each path does and skips.

### Reasoning direction and competency questions

Unless the path is A, ask three things in the same message as the path question.

- (Purpose) Knowledge structuring, relation exploration, pattern discovery, automatic classification or structure check
- (Expected output) A structured knowledge graph, path results, a list of violations or classification results
- (Scope) A full analysis or a focus on one part

Collect competency questions on every path. Path A collects them too, to record why the TBox looks the way it does and to support reuse. Competency questions serve as the yardstick that keeps needed concepts from going missing in the TBox. Without them, nobody can explain why a class is in the ontology.

- Show examples first and take the questions in natural language (for example "Is every activity linked to at least one goal?", "If assumption X fails, how far does the impact reach?", "Which strategies use both a strength and an opportunity?")
- Route yes/no questions to check functions and list or number questions to SPARQL
- Record the competency questions and the agreed path in the OWL metadata (label, version, comment of create_world)
- If the user cannot provide competency questions, propose up to 3 candidates drawn from the domain and get confirmation
- Do not move on to building the TBox without competency questions
- When extending in a later turn, ask for this turn's reasoning goal, its relation to earlier results (follow-up or new area) and any new competency questions
- Without an agreed direction, the LLM does not decide the build direction on its own

```python
world, onto = create_world(
    label="New project plan review",
    version="1.0",
    comment="Path C | CQ1 Is every activity linked to a goal? | CQ2 Which assumptions lack evidence?")
```

## Stage 1. Design

The design rules are in references/modeling-rules.md and apply to both modes. Read it before you start designing. In short:

- Set purpose, definitions, criteria and scope at the smallest unit first, and keep their meaning until the work ends
- Use a single classification criterion and test for overlaps and gaps with real cases
- Tell kind-of (is-a), part-of and has-a relations apart
- Give every relation a direction, a type (causal, correlational, dependency, association) and quantity constraints
- Treat unconfirmed facts as unknown, and conclude absence only where a full survey is done
- Model the real structure first. Do not add or change concepts or relations to suit analysis tools, queries or output formats

In engine mode, extend the existing ontology instead of starting from scratch each turn. Look for an existing ontology in this order.

| Rank | Look for | How to tell | Action |
|:---:|---|---|---|
| 1 | An ontology built in this conversation | An earlier turn called create_world or save_all_outputs | Reload the saved OWL with create_world(path) and extend it |
| 2 | An OWL file from the user | A .owl file is attached | Load it with create_world(path) and go to the check stage |
| 3 | A problem described in natural language | Text describes the subject, relations and constraints | Create a new one with create_world() |
| 4 | A request for a domain template | An analysis type is named | Create a new one with create_world() and use tbox-templates.md |

- Create a new ontology only when nothing matches rank 1 or 2
- If an ontology exists and the user asks for a new analysis, first check whether the existing TBox can be reused. For a follow-up in the same domain, keep the TBox and add or replace only the ABox. For a different domain, create a new one and ask whether to keep the old OWL file
- When adding ABox content to an existing ontology, link new individuals to existing ones
- To continue in another session, save the OWL file and load it again in the next session

## Stage 2. Build

### Thinking mode

Write the designed structure straight into the output. Definition lists, classification tables and relation statements carry the structure. Do not name the principles you applied or rate your own classification.

### Engine mode setup

At the start of engine mode, run these three commands from the skill folder in order. The two scripts print the API list and the reference documents for this task, so read their output in full without head, tail or truncation.

```bash
pip install owlready2        # on a protected system Python, use a virtual environment or add --break-system-packages
python scripts/extract_api.py
python scripts/load_references.py
```

- Add the scripts folder to the import path and load the engine with `from onto_engine import *`
- When the example code in a reference differs from the actual code in onto_engine.py, follow the actual code
- The recommended size is up to 500 classes and 10,000 individuals. Larger ontologies work but take longer to build

### Building the TBox

While designing the TBox, ignore the later analysis tools (SPARQL queries, check functions, reasoners, SWRL, suggest_axioms, suggest_sparql_queries). Do not add a property because it would enable some analysis later. Decide only by asking whether this relation between A and B really exists in the domain. Do not call suggest_axioms or suggest_sparql_queries while designing the TBox. This rule applies to the build stage of every path, including one turn.

Build the TBox in the order design agreement, execution, confirmation. Do not run build code such as build_class or build_object_property until the user confirms. Skip the prior agreement only when the user explicitly chose one turn on path B. Do not skip the agreement because showing a result would be faster.

- (Draft) Extract every concept (class) and relation (property) that actually exists in the user's input. Walk back from the competency questions to fill in missing concepts, and confirm that each added concept exists in the real domain. Do not add artificial properties just to make a query work
- (Agreement) Present the class and property lists as a design draft and apply requested changes
- (Execution) Build exactly the agreed draft. Do not add relations outside the draft for analysis convenience
- (Confirmation) Show the result as a Mermaid class diagram
- (Function matching) Scan the built TBox with auto_route_advanced_checks to see which analysis functions apply. Do not apply a function that assumes a relation the TBox does not have

Build rules:

- Name classes in PascalCase and properties and individuals in snake_case, using ASCII letters
- Store human-readable descriptions in the user's language through the description argument of build_class or the description data property
- Keep proper nouns from the user (policy, organization and program names) in full, without abbreviation
- The parent, domain, range_cls and cls arguments accept class objects or class name strings
- Every class must take part in at least one object property as its domain or range. If a class does not, tell the user it may be a design error
- Remove an object property that no individual uses, or add individuals that use it
- If a domain template fits, start from the structure in references/tbox-templates.md and rename it to the user's terms

### Building the ABox

Enter the ABox after the TBox is final. Paths A and C do it in a separate turn. The one-turn option of path B does it in the same turn as the TBox. Do not run build code such as create_individual until the user confirms.

- (Entry plan) Present the list of individuals and the planned links, marking fact properties and judgment properties
- (Agreement) Apply requested changes
- (Execution) In the same code block that calls create_individual, link the new individual to another one through at least one object property
- (Isolated individuals) If some individuals have no link, list them and ask whether to add a relation or leave it unknown. An individual the user chose to leave unknown is a valid state under the open world assumption
- (Confirmation) Show the final state as a Mermaid instance graph
- (Confirm or revise) On confirmation, save the OWL file and move on. On revision, change the individuals and relations and show them again

Enter facts and judgments separately. If anyone reading the original source would agree, it is a fact. If it needs interpretation, it is a judgment.

- Build the ABox first from fact properties that the original source confirms directly
- Do not enter mappings such as "A counts as B" during the build. First check whether axiom-based reasoning or a SPARQL query in the check stage can derive them
- Only when the structure cannot stand on facts alone, ask the user whether to enter judgment properties. If the user agrees, record the reason with set_with_provenance

Use add_to_class, destroy_individual, build_same_as, update_property, remove_property_value and clear_property to edit the ABox.

### Applying axioms

After the TBox is final, call suggest_axioms(onto) for candidate axioms. It scans the class hierarchy, the property structure and the distribution of individuals, and proposes candidates for eight axiom types (DisjointUnion, MinCardinality, IrreflexiveProperty, InverseProperty, PropertyChain, SymmetricProperty, ConstrainedDatatype, SWRL).

- Show the suggestions and apply only the axioms the user picks
- You may propose further axioms from domain judgment, using the axiom tables and restriction_expr combinations in references/axiom-patterns.md
- When a template is used, its axioms entry is the default axiom set
- If one axiom fails, skip only that axiom and continue with the rest
- Show the list of applied axioms and accept deletions or changes
- If at least one axiom is applied, recommend running the reasoner (use_hermit=True) in the check stage by default

OWL reasoners follow the open world assumption, so a missing link is not treated as a problem. Account for this when designing axioms.

- A minimum cardinality axiom (MinCardinality) and classification by absence (a Not condition) cannot catch links that were never entered. Find missing links with SPARQL checks and report them as missing-entry candidates
- If the reasoner must judge missing links, first get the user's confirmation that the entries in that scope are complete, then declare the scope closed with close_world_scope and run the reasoner
- A maximum cardinality axiom (MaxCardinality) catches an excess only when the targets are declared different from each other (build_all_different). OWL does not assume that different names mean different individuals

Use SWRL rules with care.

- SWRL is a W3C Member Submission from 2004 and never became a W3C Recommendation. Combining it with OWL DL removes the guarantee that reasoning finishes in finite time
- Explain this risk and ask whether to apply a rule before proposing one
- First check whether OWL axioms (EquivalentClass, DisjointClasses, restrictions) can achieve the same effect, and use SWRL only when they cannot
- HermiT applies rules only to named individuals (DL-safe) and does not run rules with built-ins such as greaterThan. If built-ins are needed, switch to reasoner="pellet" and warn that reasoning may not finish

## Stage 3. Check

### Both modes

- Check the structure with the checklist in references/modeling-rules.md
- Check the claims in the user's material and in your own output with references/reasoning-rules.md
- Apply the burden of proof to your own findings too. Report only problems whose existence is confirmed by the source material, code output or query results

### Engine mode analysis routes

After the build, pick a route by question type. Routes can be combined.

| Condition | Route | Reason |
|---|---|---|
| Whether predefined rules pass: allowed combinations, broken sequences, coverage, assumption impact | check function | The rule can be written as code |
| Extracting sets, filtering, aggregation, path search, free questions from the user | SPARQL | One declarative query answers it |
| Deciding a type from a combination of values | reasoner | Needs an EquivalentClass axiom |
| Individuals that belong to types that cannot overlap | reasoner | Needs a DisjointClasses axiom |
| Whether rules that pass one by one contradict each other in combination | reasoner | Only a reasoner can test satisfiability |
| Full checks over 1,000 or more individuals | check function | Reasoners slow down at scale |

- When combining check functions and a reasoner, run the check functions for explicit rules first and the reasoner for hidden contradictions after
- If the reasoner fails or times out, report its message and use check functions and SPARQL instead
- run_full_analysis(world, onto) runs the default analysis in one call. The MECE check runs only with run_mece=True. auto_route_advanced_checks always runs and lists the advanced functions that apply. It chooses them from keywords in property and class names, so review the list before running it
- When you recognize a structural pattern, run a preset (cross_factor, multi_axis, regulated_procedure, causal, logic_model, mapping_chain, decision_tree) to run the related checks together
- For a question no check function covers, write a SPARQL query with query_onto before writing new Python code
- Check functions and SPARQL read only the entered facts. Treat unlinked items in their results as missing-entry candidates

Function lists and usage are in references/check-functions.md, query patterns and the report format in references/sparql-patterns.md, and reasoner settings and axiom code in references/axiom-patterns.md.

## Stage 4. Report

### Both modes

The report rules are in references/output-rules.md. Read it before writing the report. In short:

- Every sentence must pass four tests (subject, deletion, beneficiary, courtesy). Do not write sentences whose subject is the text itself, the writing process, the tools or the user's request, or sentences that lose no information when deleted
- Do not name the principles or frameworks you applied, and do not claim that your own classification or reasoning meets them
- Search for counterexamples during the check. The report contains only counterexamples that are findings (for example an individual in two classes that should not overlap) and counterexamples the user asked for
- Turn analysis jargon into plain factual statements a decision maker understands without explanation. For example, write "coverage shortfall: 3" as "3 strategies have no confirmed link to any program goal"

### Engine mode report

- Keep unlinked individuals in a separate missing-entry candidates section, apart from violations. Raise first only the candidates that affect the agreed reasoning goal, and handle the rest when the user asks to fill them in
- For every competency question, report whether it can be answered and the actual answer (SPARQL or check function result). For questions that cannot be answered, say which classes, properties or individuals to add. Report competency questions added in later turns the same way
- If an existing OWL file was extended, summarize this turn's changes with diff_ontology
- Save the four files below with save_all_outputs

| File | Content |
|---|---|
| {base_name}.owl | OWL ontology (TBox and ABox) |
| {base_name}_class.mermaid | Class hierarchy diagram |
| {base_name}_instance.mermaid | Instance diagram (switches form by size) |
| {base_name}_report.md | TBox definitions, ABox contents, summary statistics |

The instance diagram changes form with the number of individuals. The force_mode argument can set the form.

| Individuals | Form | Content |
|---|---|---|
| 50 or fewer | full | Graph of every individual |
| 51-200 | aggregated | Class-level aggregate graph |
| 201 or more | summary | Summary statistics |

Mermaid diagram rules:

- When building the ontology for the first time, ask once whether to show a Mermaid diagram every turn
- If the user agrees, show one in every turn that builds, extends or analyzes, and in any turn where reasoner reclassification changed the ontology. If the user sets a different visualization, use it
- Skip it in turns where the ontology did not change, and use summary statistics above 200 individuals
- The export_mermaid_* functions return Mermaid code without a code fence. Save it as is in .mermaid files, and wrap it in a mermaid code block when placing it in Markdown

The result of run_full_analysis also includes provenance_check (judgment records), advanced_routing (advanced analyses that apply) and hermit_analysis (reasoner result and reclassifications when use_hermit=True).

After the analysis, save the output of export_tbox_markdown separately as the TBox definition document. When an OWL file from an earlier session comes in, you can keep its TBox and replace only the ABox. The label, version and comment of the OWL file show up in external tools such as Protégé.

## Pre-delivery check

- Are definitions, criteria and scope used with the meaning set at the start?
- Is there a single classification criterion, with no overlaps and no gaps among items?
- Are kind-of, part-of and has-a relations kept apart?
- Does every conclusion have support, and does no conclusion go beyond its support?
- Was unconfirmed information never used as evidence of absence?
- Was the structure left unchanged by the needs of tools or output formats?
- Are there no unlinked items or empty categories, or is the reason for each confirmed?
- In engine mode, were the agreement checkpoints kept?
- In engine mode, are missing-entry candidates and violations reported separately?
- Is the report free of meta commentary, principle names, self-justification and unrequested counterexamples?
- Was analysis jargon turned into plain factual statements?

## Reference files

| File | Content | When to read |
|---|---|---|
| references/modeling-rules.md | Definitions, classification, hierarchy, relations, handling of unknowns, structure checks | Design stage, structure check |
| references/reasoning-rules.md | Premise checks, conclusions and support, fallacies, cognitive biases | Argument check |
| references/output-rules.md | Meta commentary tests, counterexample reporting, plain language, process output format | Report stage |
| references/tbox-templates.md | Domain TBox starting points and default axioms | Engine mode TBox design |
| references/axiom-patterns.md | Axiom helpers, property characteristics, reasoner settings, SWRL | Engine mode axioms and reasoning |
| references/sparql-patterns.md | Built-in queries, free query patterns, result report format | Engine mode check and report |
| references/check-functions.md | Check functions and presets, structural patterns | Engine mode check |
