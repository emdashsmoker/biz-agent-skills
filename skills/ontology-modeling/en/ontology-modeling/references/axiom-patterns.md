# Axiom and reasoner patterns

How to build OWL axioms and run the reasoners (HermiT, Pellet). Apply only the axioms the user picks, after the TBox is final.

## What the reasoner does

Patterns for checking:

- (Automatic classification) Define the necessary and sufficient conditions of a type, and the reasoner decides the type of each individual from its values. A mismatch between the declared type and the inferred type reveals a misclassification
- (Disjointness) Individuals in types that cannot overlap show up as an inconsistency
- (Cardinality) After declaring an upper bound or exact count of links, targets declared different from each other that break the constraint show up as an inconsistency
- (Consistency) A satisfiability test decides whether a combination of axioms contradicts itself

Patterns for deriving new facts:

- (Property chain) Connect relations over two or more steps into an indirect relation
- (Inverse property) Enter one direction and the other direction is filled in
- (Compound classification) Classify by combining value ranges and the presence of relations
- (SWRL rules) Derive new facts through IF-THEN rules

## What the reasoner can decide under the open world assumption

OWL reasoners treat facts that were never entered as unknown, and they do not assume that different names mean different individuals. So the same axiom can decide some things and not others. The behavior below was confirmed by running owlready2 0.51 with HermiT.

| Axiom | Decided from the entries alone | Not decided from the entries alone | How to cover the gap |
|---|---|---|---|
| DisjointClasses | Individuals in two disjoint classes (ontology inconsistency) | nothing | nothing needed |
| MinCardinality | nothing | Individuals missing a link | Find missing-entry candidates with the SPARQL unsupported query or check_provenance. Once the entries are confirmed complete, run close_world_scope and then the reasoner |
| MaxCardinality | Excess links to targets declared different | Excess without a build_all_different declaration | Declare build_all_different on the targets |
| EquivalentClass (some condition) | Classifying individuals that meet the condition | nothing | nothing needed |
| EquivalentClass (Not condition) | nothing | Classification because a link is absent | Run close_world_scope on a scope confirmed complete, then the reasoner |
| Transitive property with different domain and range | Infers that an individual in the middle of a chain belongs to both classes | not applicable | Declare transitive only when domain and range are the same class |

close_world_scope declares "the entries in this scope are complete". Run it only after the user confirms that the survey of that scope is finished, and state the closed scope and its basis in the report.

```python
# after the user confirms that the Assumption list and its evidence links are complete
close_world_scope(onto, class_names=["Assumption"])
result = run_full_analysis(world, onto, use_hermit=True)
```

## Axiom helpers

### Class axioms

| Axiom | Helper | Use |
|---|---|---|
| EquivalentClass | build_equivalent_class | Automatic classification by necessary and sufficient conditions |
| DisjointClasses | build_disjoint_group | Declare mutual exclusion |
| DisjointUnion | build_disjoint_union | Declare that subclasses do not overlap and together make up the parent |
| OneOf | build_one_of | Define a class by listing its individuals |
| AllDifferent | build_all_different | Declare that the listed individuals are all different |
| SWRL | build_swrl_rule | Derive new facts through IF-THEN rules |

### Cardinality and value constraints

| Axiom | Helper | Use |
|---|---|---|
| MinCardinality | build_min_cardinality | Requirement of at least N links |
| MaxCardinality | build_max_cardinality | Limit of at most N links |
| ExactCardinality | build_exact_cardinality | Requirement of exactly N links |
| AllValuesFrom | build_all_values_from | Restrict targets to one class |
| HasValue | build_has_value | Require a link to one named individual |

### Property characteristics

| Characteristic | How to set | Meaning |
|---|---|---|
| Transitive | is_transitive=True | If A precedes B and B precedes C, A precedes C |
| Functional | is_functional=True | At most one value |
| Symmetric | is_symmetric=True | If A cooperates with B, B cooperates with A |
| Asymmetric | is_asymmetric=True | If A reports to B, B cannot report to A |
| Reflexive | is_reflexive=True | Every individual relates to itself |
| Irreflexive | is_irreflexive=True | No individual relates to itself |
| InverseFunctional | is_inverse_functional=True | The value identifies one individual |
| Inverse | onto["B"].inverse_property = onto["A"] | B is the reverse direction of A |
| PropertyChain | prop.property_chain.append(PropertyChain([p1, p2])) | p1 followed by p2 implies prop |

Transitive through InverseFunctional are arguments of build_object_property.

### restriction_expr combinations

Combine these expressions in the restriction_expr argument of build_equivalent_class.

| Expression | Meaning | Kind |
|---|---|---|
| prop.some(Target) | At least one link to Target | existential |
| prop.only(Target) | Links only to Target | universal |
| prop.value(individual) | Link to a specific individual | value |
| prop.min(N, Target) | At least N links | minimum |
| prop.max(N, Target) | At most N links | maximum |
| prop.exactly(N, Target) | Exactly N links | exact |
| prop.has_self() | Refers to itself | self |
| ConstrainedDatatype(int, min_inclusive=N) | Numeric lower bound | data range |
| Class & expr1 & expr2 | All conditions at once | intersection |
| Class1 \| Class2 | Either one | union |
| Not(expr) | Negation of a condition | negation (see the open world table above) |
| Inverse(prop) | Unnamed reverse property | inverse |

## Code examples

### Basic axioms

```python
# automatic classification
build_equivalent_class(onto, "ShortTerm",
    onto["Project"] & onto["has_tag"].some(onto["ShortTag"]))

# mutual exclusion
build_disjoint_group(onto, ["TypeA", "TypeB", "TypeC"])

# no overlap and together the whole
build_disjoint_union(onto, "Factor",
    ["Strength", "Weakness", "Opportunity", "Threat"])

# cardinality
build_min_cardinality(onto, "Objective", "has_indicator", 1, "Indicator")
build_max_cardinality(onto, "Strategy", "uses_factor", 3, "Factor")
build_exact_cardinality(onto, "Step", "performed_by", 1, "Actor")

# target restrictions
build_all_values_from(onto, "InternalProject", "performed_by", "InternalActor")
build_has_value(onto, "RegulatedProject", "governed_by", "gov_agency_1")
```

### Derivation axioms

```python
from owlready2 import PropertyChain

# property chain: manages followed by contains implies responsible_for
with onto:
    onto["responsible_for"].property_chain.append(
        PropertyChain([onto["manages"], onto["contains"]]))

# inverse property
with onto:
    onto["managed_by"].inverse_property = onto["manages"]

# SWRL rule without built-ins (runs on HermiT)
build_swrl_rule(onto,
    "Person(?p), manages(?p, ?proj) -> responsible_for(?p, ?proj)",
    name="manager_responsibility")

# SWRL built-ins (run only on Pellet)
build_swrl_rule(onto,
    "Project(?p), budget(?p, ?b), lessThan(?b, 1000000) -> SmallProject(?p)",
    name="small_project")

# list and delete rules
for r in list_swrl_rules(onto):
    print(f"[{r['label']}] IF {r['body']} THEN {r['head']}")
delete_swrl_rule(onto, "small_project")
```

### Advanced axioms

```python
from owlready2 import ConstrainedDatatype, Inverse

# enumerated class
build_one_of(onto, "PriorityRole", ["role_pm", "role_lead"])

# distinct individuals (passing two declares a single pair)
build_all_different(onto, ["alice", "bob", "charlie"])

# classification by data range
build_equivalent_class(onto, "LargeProject",
    onto["Project"]
    & onto["budget"].some(ConstrainedDatatype(int, min_inclusive=1000000000))
    & onto["duration_years"].some(ConstrainedDatatype(int, min_inclusive=3)))

# self reference
build_equivalent_class(onto, "SelfReviewedDocument",
    onto["Document"] & onto["reviewed_by_self"].has_self())

# compound condition (Not and max 0 are decided only after close_world_scope)
build_equivalent_class(onto, "RiskyProject",
    onto["Project"]
    & onto["budget"].some(ConstrainedDatatype(int, min_inclusive=5000000000))
    & onto["mitigates"].max(0, onto["Risk"]))

# combined property characteristics
build_object_property(onto, "reports_to", "Person", "Person",
    is_asymmetric=True, is_irreflexive=True)
build_object_property(onto, "cooperates_with", "Partner", "Partner",
    is_symmetric=True)
build_object_property(onto, "has_id", "Person", "IDNumber",
    is_inverse_functional=True)

# unnamed inverse inside a restriction
build_equivalent_class(onto, "UnmanagedDepartment",
    onto["Department"] & Inverse(onto["manages"]).max(0, onto["Person"]))
```

## Editing property values

```python
update_property(onto, "proj1", "budget", 3000000000)            # replace all values
remove_property_value(onto, "proj1", "achieves", onto["goal_old"])  # remove one value
clear_property(onto, "proj1", "achieves")                        # remove all values
```

## rdflib bridge

as_rdflib_graph returns the whole World as an rdflib-compatible graph, which gives access to rdflib's SPARQL 1.1 features and RDF serialization.

```python
graph = as_rdflib_graph(onto)
if graph is not None:
    rows = list(graph.query("SELECT ?s WHERE { ?s ?p ?o } LIMIT 5"))
```

## Running the reasoner

```python
# HermiT (default: class classification only)
result = run_full_analysis(world, onto, use_hermit=True)

# HermiT with object property value inference
result = run_full_analysis(world, onto, use_hermit=True,
                           infer_property_values=True)

# Pellet (when SWRL built-ins are needed)
result = run_full_analysis(world, onto, use_hermit=True, reasoner="pellet")

# Pellet with object and data property value inference
result = run_full_analysis(world, onto, use_hermit=True, reasoner="pellet",
                           infer_property_values=True,
                           infer_data_property_values=True)

# run only the reasoner and inspect reclassifications
ha = run_hermit_analysis(world, onto)
for rc in ha["reclassifications"]:
    print(f"{rc['individual']}: {rc['before']} -> {rc['after']}")
```

- A result with mode fallback means the reasoner did not run. Report its message to the user and use check functions and SPARQL instead
- The reasoner timeout (30 seconds by default) works only on the main thread of operating systems that support SIGALRM. On Windows and in other threads the reasoner runs without a timeout
- The Pellet libraries bundled with owlready2 0.50 and 0.51 run on Java 25 or later. On older Java, the Pellet call fails and falls back

| Argument | HermiT | Pellet | Use |
|---|---|---|---|
| infer_property_values | supported | supported | Infer object property values |
| infer_data_property_values | not supported | supported | Infer data property values |
| reasoner | "hermit" | "pellet" | Choose the reasoner |

## External ontologies and IRIs

```python
# create an ontology with a chosen IRI
world, onto = create_world(iri="http://example.org/project.owl")
build_class(onto, "LocalClass")

# import an external ontology from a local file or IRI
ext = import_ontology(world, onto, "external.owl")
if ext is not None:
    build_object_property(onto, "uses_ext", "LocalClass", ext["ExternalClass"])

# query_onto adds prefixes for imported ontologies
rows = query_onto(world, onto, "SELECT ?x WHERE { ?x a :LocalClass }")
```

When an external ontology is imported, the reasoner applies its axioms as well.

## Axiom suggestions

After the TBox is final, get candidate axioms from suggest_axioms and show them to the user.

```python
for s in suggest_axioms(onto):
    print(f"[{s['axiom']}] {s['target']}: {s['description']}")
    print(s["code"])
```

You can also propose axioms outside the suggestions from domain judgment, using the tables and restriction_expr combinations above.

## More helpers

| Function | Use |
|---|---|
| build_annotation_property(onto, name) | Property for documentation only (reasoners ignore it) |
| add_to_class(onto, individual_name, class_name) | Put an individual in one more class |
| destroy_individual(onto, individual_name) | Delete an individual and its links |
| build_same_as(onto, name_a, name_b) | Declare that two individuals are the same thing |
| build_sub_property(onto, child, parent) | Declare a property hierarchy |
| build_equivalent_properties(onto, name_a, name_b) | Declare two properties equivalent (when merging vocabularies) |
| build_class(onto, name, parent=[A, B]) | Several parent classes |
| close_world_scope(onto, class_names, individual_names) | Declare a scope confirmed complete as a closed world |
| list_swrl_rules(onto) | List SWRL rules (label, body, head) |
| delete_swrl_rule(onto, rule_or_label) | Delete a SWRL rule |

## SWRL rules

- SWRL is a W3C Member Submission from 2004 and never became a W3C Recommendation
- Combining SWRL with OWL DL removes the guarantee that reasoning finishes in finite time, so use it conservatively
- Explain this risk and ask whether to apply a rule before proposing one
- First check whether EquivalentClass or restriction axioms can achieve the same effect
- HermiT applies rules only to named individuals (DL-safe) and does not run rules that contain built-ins
- If built-ins are needed, switch to reasoner="pellet" and warn that reasoning may not finish

Built-ins run on Pellet.

| Built-in | Use | Example |
|---|---|---|
| greaterThan(?a, N) | greater than | "age(?p, ?a), greaterThan(?a, 18)" |
| lessThan(?a, N) | less than | "budget(?p, ?b), lessThan(?b, 1000000)" |
| equal(?a, N) | equal | "priority(?p, ?v), equal(?v, 1)" |
| greaterThanOrEqual(?a, N) | at least | "score(?p, ?s), greaterThanOrEqual(?s, 80)" |
| lessThanOrEqual(?a, N) | at most | "score(?p, ?s), lessThanOrEqual(?s, 100)" |
| add(?r, ?a, ?b) | addition (?r = ?a + ?b) | "budget(?p, ?b), add(?total, ?b, 100000)" |
| subtract(?r, ?a, ?b) | subtraction (?r = ?a - ?b) | "subtract(?profit, ?total, ?cost)" |
| multiply(?r, ?a, ?b) | multiplication (?r = ?a × ?b) | "multiply(?amount, ?rate, ?base)" |
| stringConcat(?r, ?a, ?b) | string concatenation | "stringConcat(?s, ?name, '_suffix')" |
