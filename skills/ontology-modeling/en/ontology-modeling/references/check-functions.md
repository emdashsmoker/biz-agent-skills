# Check functions and presets

## Basic run pattern

```python
import sys
sys.path.insert(0, "path/to/ontology-modeling/scripts")  # the scripts folder of the skill
from onto_engine import *

world, onto = create_world()
# build the TBox and ABox

result = run_full_analysis(world, onto)                   # Python checks
result = run_full_analysis(world, onto, use_hermit=True)  # Python checks, then the reasoner
paths = save_all_outputs(world, onto, base_name="analysis")  # OWL, two Mermaid files, report
```

save_all_outputs writes to an outputs folder under the working folder by default. The output_dir argument changes the location.

## Functions that rely on fixed names

These functions look for fixed class or property names. If the ontology uses other names the results come back empty, so match the names or use a function that takes names as arguments (check_provenance, check_coverage and so on).

| Function | Names it looks for |
|---|---|
| check_unsupported_assumptions | Assumption class, supported_by property |
| check_process_completeness | precedes property |
| check_causal_chain | causes property |
| check_constraint_conflicts | Pairs of properties whose names contain goal or objective and risk or constraint |
| check_assumption_impact | attached_to and precedes by default (changeable through arguments), and output properties whose names contain output or produces |
| auto_route_advanced_checks | The keywords in the automatic routing table below |

## SPARQL-based checks (15)

Every check function takes world as the first argument and onto as the second. Internally they run built-in queries through run_sparql_check.

| Function | Built-in query | What it does |
|---|---|---|
| check_mece(world, onto, parent) | mece_overlap | Finds individuals shared by pairs of subclasses and individuals in no subclass |
| check_causal_chain(world, onto) | edges | Extracts every path along causes, starting from individuals that nothing causes. Branches appear as separate paths |
| check_constraint_conflicts(world, onto) | conflict_dual_ref | Finds individuals where a goal-type property and a risk-type property point to the same target |
| check_unsupported_assumptions(world, onto) | unsupported | Finds assumptions without linked evidence |
| check_process_completeness(world, onto) | edges | Finds the start steps, end steps and steps unreachable from a start along precedes |
| check_coverage(world, onto, source, referencing, prop) | coverage | Finds individuals that no individual of the referring class points to |
| check_cardinality(world, onto, cls, prop, expected) | cardinality_count | Finds individuals whose link count differs from the expected number. No link counts as 0 |
| check_provenance(world, onto, classes, prop) | unsupported | Finds individuals without a value for the given property |
| check_shared_reference(world, onto, classes, prop) | refs_for_class | Compares the sets of targets that several classes reference through one property |
| check_value_range(world, onto, cls, prop, min_val, max_val, range_rules) | value_below, value_above | Finds values outside a range. range_rules sets a different range per class |
| check_bidirectional_coverage(world, onto, a, b, a_to_b, b_to_a) | unsupported, coverage | Finds A individuals without a link and B individuals that nothing refers to |
| check_reverse_chain(world, onto, effect, cause_prop, max_depth) | individual traversal | Traces causes backward from an effect along every branch. Returns chains, roots and has_cycle |
| check_mandatory_outputs(world, onto, stage_cls, output_prop, required) | mandatory_missing | Finds stages without a required output class |
| check_assumption_impact(world, onto, assumption, attached, order) | downstream | Computes the later stages and outputs affected by the stages an assumption is attached to |
| check_pipeline_trace(world, onto, stage_chain) | stage_unlinked | Finds individuals of each stage class without a link to the next stage |

## Python-only checks (3)

Allowed-combination rules and per-level rules are hard to express in one SPARQL query, so Python checks them.

### check_cross_mapping(onto, subject_classes, property_name, target_class_set)

Checks rules that fix which target types each subject type may reference. subject_classes has the form {"TypeName": {"allowed": {"AllowedTarget1", "AllowedTarget2"}}}.

```python
violations = check_cross_mapping(onto,
    {"Strategy": {"allowed": {"Strength", "Opportunity"}}},
    "uses_factor",
    {"Strength", "Weakness", "Opportunity"})
```

### check_mapping_chain(world, onto, chain_rules)

Checks a mapping from A to B, B to C and so on, level by level, and reports the first level that breaks. A level with allowed and target_types checks allowed combinations. A level without them checks only that links exist.

```python
result = check_mapping_chain(world, onto, [
    {"from_class": "Category", "to_class": "Field",
     "link_property": "maps_to",
     "allowed": {"Category": {"allowed": {"Field"}}},
     "target_types": {"Field"}},
    {"from_class": "Field", "to_class": "Item",
     "link_property": "selects_item"},
])
```

### check_conditional_branch(onto, condition_class, condition_property, branch_rules, stage_property)

Defines, for each condition value, the steps that must and must not be present, and compares them with the actual steps.

```python
violations = check_conditional_branch(onto,
    "Project", "project_type",
    {"type_a": {"required": ["Step"], "excluded": ["Activity"]}},
    "has_step")
```

## Presets (7)

When you recognize a structural pattern, a preset runs the related checks together. Every preset takes world and onto as its first two arguments.

| Preset | Included checks | Fits |
|---|---|---|
| run_preset_cross_factor | check_cross_mapping, check_provenance, check_cardinality | Types that may reference only certain factors |
| run_preset_multi_axis | check_coverage, check_shared_reference | Several evaluation criteria combined into one result |
| run_preset_regulated_procedure | check_pipeline_trace, check_mandatory_outputs | Procedures with a fixed order and required outputs |
| run_preset_causal | check_causal_chain, check_unsupported_assumptions, check_reverse_chain | Chains of causes and effects |
| run_preset_logic_model | check_pipeline_trace, check_bidirectional_coverage, check_unsupported_assumptions, check_provenance | Inputs leading to activities, outputs and outcomes |
| run_preset_mapping_chain | check_mapping_chain, check_bidirectional_coverage | Multi-level classification mappings |
| run_preset_decision_tree | check_conditional_branch, check_provenance | Procedures that branch by condition |

```python
# causal analysis
result = run_preset_causal(world, onto,
    effect_name="funding_gap", cause_property="caused_by")

# allowed factors per type
result = run_preset_cross_factor(world, onto,
    rules={"Strategy": {"allowed": {"Strength", "Opportunity"}}},
    factor_property="uses_factor",
    factor_types={"Strength", "Weakness", "Opportunity"},
    source_property="achieves",
    source_classes=["Strategy"],
    cardinality_property="uses_factor",
    expected_count=2)

# fixed-order procedure
result = run_preset_regulated_procedure(world, onto,
    stage_chain=[{"class": "Step", "link_to_next": "precedes"},
                 {"class": "Step"}],
    output_property="produces",
    mandatory_map={"Step": ["MandatoryOutput"]})

# multi-level classification mapping
result = run_preset_mapping_chain(world, onto,
    chain_rules=[
        {"from_class": "Category", "to_class": "Field",
         "link_property": "maps_to",
         "allowed": {"Category": {"allowed": {"Field"}}},
         "target_types": {"Field"}},
        {"from_class": "Field", "to_class": "Item",
         "link_property": "selects_item"},
    ],
    bidirectional_pairs=[("Category", "Field", "maps_to")])

# conditional branches
result = run_preset_decision_tree(world, onto,
    condition_class="Project",
    condition_property="project_type",
    branch_rules={
        "type_a": {"required": ["StepX", "StepY"], "excluded": ["StepZ"]},
        "type_b": {"required": ["StepZ"], "excluded": ["StepX"]},
    },
    stage_property="has_step",
    prerequisite_property="requires_prerequisite")

# logic model
result = run_preset_logic_model(world, onto,
    stage_chain=[{"class": "Activity", "link_to_next": "precedes"}],
    objective_class="Goal", activity_class="Strategy",
    obj_to_act_property="achieves",
    indicator_property="has_indicator", indicator_classes=["Objective"])

# multi-criteria evaluation
result = run_preset_multi_axis(world, onto,
    axis_classes=["AxisA", "AxisB"],
    result_property="produces",
    comprehensive_class="FinalEvaluation",
    intake_property="uses_result",
    shared_ref_property="references")
```

## Automatic routing rules

auto_route_advanced_checks picks checks by looking at names. Because it relies on names, review its result before running the checks.

| Condition | Recommended check | Level |
|---|---|---|
| A property named precedes, follows, leads_to, next_stage, before or after, or any transitive property | pipeline_trace | required |
| A property name contains supported_by, evidence, based_on, justified_by or grounded_in | provenance | required |
| A property name contains causes, caused_by, results_in or leads_to_effect | causal_chain, reverse_chain | required |
| A class name contains assumption or premise | unsupported_assumptions | required |
| An assumption class and an order property both exist | assumption_impact | recommended |
| Two or more object properties share the same domain and range | bidirectional_coverage | required |
| An object property with a domain exists | cardinality | recommended |
| Two or more properties use one class as their range | shared_reference | recommended |
| A class name contains mandatory, required, output or deliverable and an order property exists | mandatory_outputs | recommended |
| A provenance_note property exists | provenance | required |
| A class has two or more subclasses | mece | recommended |

## Structural patterns

General structural patterns to consult when designing axioms or reading the routing result.

| Pattern | Structure | Related axiom | Cue |
|---|---|---|---|
| Disjoint classification | Subtypes cannot overlap | DisjointClasses | Two or more subclasses under one parent |
| Sequential dependency | The output of a step is the input of the next | MinCardinality (records the next-step link requirement), with breaks found by check_pipeline_trace | Order properties such as precedes or follows |
| Allowed combinations | Each type may reference only certain targets | EquivalentClass (allowed combinations) | Allowed targets are listed per type |
| Required link | Every X must link to at least one Y | MinCardinality (records the requirement), SPARQL check | A relation the domain logic requires |
| Missing link as a problem | No link means a problem state | EquivalentClass with a Not condition (decided after close_world_scope) | A domain where a missing link counts as a problem |
| Declared versus actual target | The declared beneficiary and the actual beneficiary can differ | Comparing two property values. OWL class axioms cannot compare two values of the same individual directly, so use a SPARQL value comparison or a DL-safe SWRL rule | Two or more beneficiary-related properties |

## Turning other analysis results into an ontology

When the input is the result of another analysis, such as a classification table, a procedure or a rule list, design the TBox with the correspondences below.

| Element of the analysis result | Ontology element | Structural pattern |
|---|---|---|
| Type classification without overlap | Subclasses and DisjointClasses | Disjoint classification |
| Steps in order | Individuals and a precedes property | Sequential dependency |
| Allowed combination rules per type | Referring property, check_cross_mapping rules, EquivalentClass | Allowed combinations |
| Relations that must exist | MinCardinality and SPARQL checks | Required link |
| States where a missing link is a problem | EquivalentClass with a Not condition | Missing link as a problem |
| Declared and actual targets | Two properties and a comparison query | Declared versus actual target |

Work in this order.

- Read the structure of the analysis result, draft the TBox with the correspondences above, and agree on it with the user
- Enter the items of the analysis result as ABox individuals
- Record the basis of interpreted properties with set_with_provenance
- Check which checks apply with auto_route_advanced_checks, then run them
