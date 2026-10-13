# Domain TBox templates

These templates are starting points for building a TBox. They impose no particular method, and the structure the user defines takes precedence. Rename classes and properties and reshape the hierarchy to fit the user's terms and method.

The axioms entry of each template is a default axiom set for use with a reasoner. Apply any subset, delete or change them. Check functions and SPARQL checks work without any axioms.

## Notes for all templates

- The dicts in the templates are a notation for the design draft. Build with build_class, build_object_property and build_data_property
- "transitive": True maps to is_transitive=True of build_object_property, and "functional": True maps to is_functional=True
- Declare a property transitive only when its domain and range are the same class. If they differ, an individual in the middle of a chain is inferred to belong to both classes, and if the two classes are disjoint the whole ontology becomes inconsistent
- owl_pattern is a human-readable notation. In code it becomes `&`, `Not(...)`, `prop.some(Class)` and `Inverse(prop)`
- Classification with NOT in owl_pattern cannot be decided from the entries alone under the open world assumption. First find the individuals as missing-entry candidates with a SPARQL check. When the user confirms that the entries in that scope are complete, run close_world_scope and then let the reasoner decide
- A min_cardinality axiom does not catch missing links either. Find missing links with check_provenance or the SPARQL unsupported query

```python
from owlready2 import Not, Inverse
# "Assumption & NOT(supported_by.some(Evidence))"
build_equivalent_class(onto, "UnsupportedAssumption",
    onto["Assumption"] & Not(onto["supported_by"].some(onto["Evidence"])))
# "Objective & NOT(INVERSE(achieves).some(Strategy))"
build_equivalent_class(onto, "OrphanObjective",
    onto["Objective"] & Not(Inverse(onto["achieves"]).some(onto["Strategy"])))
```

## 1. Policy analysis (policy_analysis)

```python
classes = {
    "Policy": None,
    "EconomicPolicy": "Policy",
    "SocialPolicy": "Policy",
    "RegulatoryPolicy": "Policy",
    "Stakeholder": None,
    "Goal": None,
    "Risk": None,
    "Constraint": None,
}

object_properties = {
    "affects":         {"domain": "Policy", "range": "Stakeholder"},
    "implemented_by":  {"domain": "Policy", "range": "Stakeholder", "functional": True},
    "has_goal":        {"domain": "Policy", "range": "Goal"},
    "has_risk":        {"domain": "Policy", "range": "Risk"},
    "conflicts_with":  {"domain": "Policy", "range": "Policy"},
    "constrained_by":  {"domain": "Policy", "range": "Constraint"},
    "mitigates":       {"domain": "Policy", "range": "Risk"},
}

data_properties = {
    "priority_level":  {"domain": "Policy", "range": "int", "functional": True},
    "rationale":       {"domain": "Policy", "range": "str"},
}
```

Checks:

- (Overlap and gaps) The subclasses of Policy
- (Goal and risk conflict) Check whether has_goal and has_risk point to the same target. check_constraint_conflicts finds this pair through the goal and risk keywords in the property names
- (Stakeholder impact) Query the affects relation with SPARQL

```python
axioms = {
    "disjoint_groups": [
        ["EconomicPolicy", "SocialPolicy", "RegulatoryPolicy"]  # policy types do not overlap
    ],
    "min_cardinality": [
        {"class": "Policy", "property": "has_goal", "min": 1, "range_class": "Goal"},
        {"class": "Policy", "property": "affects", "min": 1, "range_class": "Stakeholder"},
    ],
    "equivalent_classes": [
        {"name": "UnmitigatedRiskPolicy", "base_class": "Policy",
         "condition": "Policy with a Risk but no mitigates link",
         "owl_pattern": "Policy & has_risk.some(Risk) & NOT(mitigates.some(Risk))"},
    ],
}
```

## 2. Plan logic (plan_logic)

Analyzes the logical links among the goals, means, assumptions and evidence of a plan. It works with any planning method. Reshape the classes to fit the user's method.

```python
classes = {
    "Plan": None,
    "Objective": None,
    "Strategy": None,
    "Action": None,
    "Assumption": None,
    "Evidence": None,
    "Gap": None,
}

object_properties = {
    "achieves":        {"domain": "Strategy", "range": "Objective"},
    "consists_of":     {"domain": "Strategy", "range": "Action"},
    "depends_on":      {"domain": "Action", "range": "Assumption"},
    "supported_by":    {"domain": "Assumption", "range": "Evidence"},
    "causes":          {"domain": "Action", "range": "Objective"},
    "has_gap":         {"domain": "Plan", "range": "Gap"},
}

data_properties = {
    "feasibility":     {"domain": "Action", "range": "str", "functional": True},
}
```

Checks:

- (Overlap and gaps) The subclasses of the classification the user defined
- (Causal chain) Check that causes paths run from actions to objectives
- (Evidence) Check that each Assumption links to Evidence
- (Feasibility) Check for Actions without a feasibility value

```python
axioms = {
    "disjoint_groups": [],
    "min_cardinality": [
        {"class": "Strategy", "property": "achieves", "min": 1, "range_class": "Objective"},
        {"class": "Strategy", "property": "consists_of", "min": 1, "range_class": "Action"},
        {"class": "Assumption", "property": "supported_by", "min": 1, "range_class": "Evidence"},
    ],
    "equivalent_classes": [
        {"name": "UnsupportedAssumption", "base_class": "Assumption",
         "condition": "Assumption without linked Evidence",
         "owl_pattern": "Assumption & NOT(supported_by.some(Evidence))"},
        {"name": "OrphanObjective", "base_class": "Objective",
         "condition": "Objective that no Strategy achieves",
         "owl_pattern": "Objective & NOT(INVERSE(achieves).some(Strategy))"},
    ],
}
```

## 3. Process compliance (process_compliance)

```python
classes = {
    "Process": None,
    "Step": None,
    "Input": None,
    "Output": None,
    "Rule": None,
    "Violation": None,
    "Actor": None,
}

object_properties = {
    "precedes":        {"domain": "Step", "range": "Step", "transitive": True},
    "requires_input":  {"domain": "Step", "range": "Input"},
    "produces_output": {"domain": "Step", "range": "Output"},
    "performed_by":    {"domain": "Step", "range": "Actor"},
    "governed_by":     {"domain": "Step", "range": "Rule"},
    "violates":        {"domain": "Step", "range": "Rule"},
    "part_of":         {"domain": "Step", "range": "Process"},
}

data_properties = {
    "step_order":      {"domain": "Step", "range": "int", "functional": True},
    "is_mandatory":    {"domain": "Step", "range": "bool", "functional": True},
}
```

Checks:

- (Complete process) Check that the precedes relation has a start step and an end step
- (Order match) Check that step_order agrees with the precedes relation
- (Missing mandatory steps) Check that every Step with is_mandatory True was carried out
- (Input and output links) Check that the Output of a step feeds the Input of the next step

```python
axioms = {
    "disjoint_groups": [
        ["Input", "Output"]  # inputs and outputs do not overlap
    ],
    "min_cardinality": [
        {"class": "Step", "property": "produces_output", "min": 1, "range_class": "Output"},
        {"class": "Step", "property": "part_of", "min": 1, "range_class": "Process"},
    ],
    "equivalent_classes": [
        {"name": "DisconnectedStep", "base_class": "Step",
         "condition": "Isolated step with no previous or next step",
         "owl_pattern": "Step & NOT(precedes.some(Step)) & NOT(INVERSE(precedes).some(Step))"},
    ],
}
```

## 4. Problem decomposition (problem_decomposition)

```python
classes = {
    "Problem": None,
    "SubProblem": "Problem",
    "RootCause": None,
    "Symptom": None,
    "Solution": None,
    "Criterion": None,
    "Resource": None,
}

object_properties = {
    "has_subproblem":  {"domain": "Problem", "range": "SubProblem"},
    "caused_by":       {"domain": "Problem", "range": "RootCause"},
    "manifests_as":    {"domain": "RootCause", "range": "Symptom"},
    "resolved_by":     {"domain": "Problem", "range": "Solution"},
    "evaluated_by":    {"domain": "Solution", "range": "Criterion"},
    "requires":        {"domain": "Solution", "range": "Resource"},
    "causes":          {"domain": "RootCause", "range": "Problem"},
}

data_properties = {
    "severity":        {"domain": "Problem", "range": "str", "functional": True},
}
```

Checks:

- (Overlap and gaps) The breakdown of Problem into SubProblem
- (Causal chain) Check caused_by and causes paths for cycles
- (Solution coverage) Check that every SubProblem has a resolved_by link
- (Resource conflict) Check whether several Solutions require the same Resource

```python
axioms = {
    "disjoint_groups": [
        ["RootCause", "Symptom"]  # causes and symptoms do not overlap
    ],
    "min_cardinality": [
        {"class": "Problem", "property": "caused_by", "min": 1, "range_class": "RootCause"},
        {"class": "Problem", "property": "resolved_by", "min": 1, "range_class": "Solution"},
    ],
    "equivalent_classes": [
        {"name": "UnresolvedProblem", "base_class": "Problem",
         "condition": "Problem without a linked Solution",
         "owl_pattern": "Problem & NOT(resolved_by.some(Solution))"},
    ],
}
```

## 5. Multi-criteria evaluation (multi_axis_evaluation)

Several evaluation criteria are analyzed separately and then combined into an overall result. The analysis checks whether the criteria refer to the same entities and whether every criterion's result reaches the overall result. The user sets the names and number of criteria.

```python
classes = {
    "EvaluationAxis": None,
    "Criterion": None,
    "SharedEntity": None,
    "AxisResult": None,
    "ComprehensiveResult": None,
}

object_properties = {
    "has_criterion":     {"domain": "EvaluationAxis", "range": "Criterion"},
    "references_entity": {"domain": "EvaluationAxis", "range": "SharedEntity"},
    "produces_result":   {"domain": "EvaluationAxis", "range": "AxisResult"},
    "feeds_into":        {"domain": "AxisResult", "range": "ComprehensiveResult"},
}

data_properties = {
    "weight":      {"domain": "EvaluationAxis", "range": "float", "functional": True},
    "score":       {"domain": "AxisResult", "range": "str", "functional": True},
}
```

Checks:

- (Shared references) Use check_shared_reference to see whether the criteria refer to the same SharedEntity
- (Overall result coverage) Use check_coverage to see whether every AxisResult feeds the ComprehensiveResult
- (Preset) run_preset_multi_axis runs these together

```python
axioms = {
    "disjoint_groups": [],
    "min_cardinality": [
        {"class": "EvaluationAxis", "property": "produces_result", "min": 1, "range_class": "AxisResult"},
        {"class": "AxisResult", "property": "feeds_into", "min": 1, "range_class": "ComprehensiveResult"},
    ],
    "equivalent_classes": [
        {"name": "OrphanAxisResult", "base_class": "AxisResult",
         "condition": "AxisResult that does not feed any ComprehensiveResult",
         "owl_pattern": "AxisResult & NOT(feeds_into.some(ComprehensiveResult))"},
    ],
}
```

## 6. Regulated procedure (regulated_procedure)

A procedure whose step order and required outputs per step are fixed by law or guidelines. The user sets the procedure name and number of steps, and the template provides only the structure.

```python
classes = {
    "Procedure": None,
    "Stage": None,
    "MandatoryOutput": None,
    "OptionalOutput": None,
    "Actor": None,
    "LegalBasis": None,
}

object_properties = {
    "precedes":            {"domain": "Stage", "range": "Stage", "transitive": True},
    "produces":            {"domain": "Stage", "range": "MandatoryOutput"},
    "optionally_produces": {"domain": "Stage", "range": "OptionalOutput"},
    "performed_by":        {"domain": "Stage", "range": "Actor"},
    "governed_by":         {"domain": "Procedure", "range": "LegalBasis"},
    "part_of":             {"domain": "Stage", "range": "Procedure"},
}

data_properties = {
    "step_order":      {"domain": "Stage", "range": "int", "functional": True},
    "is_mandatory":    {"domain": "Stage", "range": "bool", "functional": True},
}
```

Checks:

- (Step order) Use check_pipeline_trace to see whether the precedes chain runs from start to end without breaks
- (Required outputs) Use check_mandatory_outputs to check every Stage for its MandatoryOutput
- (Preset) run_preset_regulated_procedure runs these together

```python
axioms = {
    "disjoint_groups": [
        ["MandatoryOutput", "OptionalOutput"]  # required and optional outputs do not overlap
    ],
    "min_cardinality": [
        {"class": "Stage", "property": "produces", "min": 1, "range_class": "MandatoryOutput"},
        {"class": "Stage", "property": "part_of", "min": 1, "range_class": "Procedure"},
    ],
    "equivalent_classes": [
        {"name": "IncompleteStage", "base_class": "Stage",
         "condition": "Stage without a linked MandatoryOutput",
         "owl_pattern": "Stage & NOT(produces.some(MandatoryOutput))"},
    ],
}
```

## 7. Logic model (logic_model)

Analyzes how inputs fund activities that produce outputs and outcomes. Use it for program planning, policy design and program evaluation, anywhere inputs lead to activities, outputs, outcomes and impact. The user sets the names and number of stages.

```python
classes = {
    "Problem": None,
    "Objective": None,
    "Beneficiary": None,
    "InputResource": None,
    "Activity": None,
    "Output": None,
    "Outcome": None,
    "Impact": None,
    "Assumption": None,
    "Evidence": None,
    "Indicator": None,
}

object_properties = {
    "addresses":      {"domain": "Activity", "range": "Problem"},
    "achieves":       {"domain": "Activity", "range": "Objective"},
    "targets":        {"domain": "Objective", "range": "Beneficiary"},
    "requires":       {"domain": "Activity", "range": "InputResource"},
    "produces":       {"domain": "Activity", "range": "Output"},
    "leads_to":       {"domain": "Output", "range": "Outcome"},
    "contributes_to": {"domain": "Outcome", "range": "Impact"},
    "precedes":       {"domain": "Activity", "range": "Activity", "transitive": True},
    "attached_to":    {"domain": "Assumption", "range": "Activity"},
    "supported_by":   {"domain": "Assumption", "range": "Evidence"},
    "measured_by":    {"domain": "Objective", "range": "Indicator"},
}

data_properties = {}
```

Checks:

- (Activity chain) Use check_pipeline_trace to find breaks in the Activity chain
- (Two-way coverage) Use check_bidirectional_coverage to find objectives and activities without links between them
- (Unsupported assumptions) Use check_unsupported_assumptions to find Assumptions without Evidence
- (Assumption impact) Use check_assumption_impact to find the later stages affected if an assumption fails
- (Indicators) Use check_provenance to check that each Objective has an Indicator
- (Preset) run_preset_logic_model runs these together

```python
axioms = {
    "disjoint_groups": [
        ["InputResource", "Output", "Outcome", "Impact"]  # inputs, outputs, outcomes and impacts do not overlap
    ],
    "min_cardinality": [
        {"class": "Activity", "property": "produces", "min": 1, "range_class": "Output"},
        {"class": "Activity", "property": "achieves", "min": 1, "range_class": "Objective"},
        {"class": "Objective", "property": "measured_by", "min": 1, "range_class": "Indicator"},
        {"class": "Assumption", "property": "supported_by", "min": 1, "range_class": "Evidence"},
    ],
    "equivalent_classes": [
        {"name": "UnsupportedAssumption", "base_class": "Assumption",
         "condition": "Assumption without linked Evidence",
         "owl_pattern": "Assumption & NOT(supported_by.some(Evidence))"},
        {"name": "UnmeasuredObjective", "base_class": "Objective",
         "condition": "Objective without a linked Indicator",
         "owl_pattern": "Objective & NOT(measured_by.some(Indicator))"},
    ],
}
```

## 8. Decision tree (decision_tree)

A structure where procedures or options branch by condition. Use it for adoption procedures, branching by program type or pre-check lists. The user sets the conditions and option names.

```python
classes = {
    "DecisionPoint": None,
    "Condition": None,
    "Option": None,
    "Prerequisite": None,
}

object_properties = {
    "has_condition":   {"domain": "DecisionPoint", "range": "Condition"},
    "leads_to":        {"domain": "Condition", "range": "Option"},
    "requires":        {"domain": "Option", "range": "Prerequisite"},
    "excludes":        {"domain": "Option", "range": "Option"},
    "precedes":        {"domain": "DecisionPoint", "range": "DecisionPoint", "transitive": True},
}

data_properties = {
    "condition_value": {"domain": "DecisionPoint", "range": "str", "functional": True},
}
```

Checks:

- (Conditional branches) Use check_conditional_branch to check required and excluded steps for each condition value
- (Prerequisites) Use check_provenance to check that each Option has a Prerequisite
- (Exclusive choice) Check that Options linked by excludes are not chosen together
- (Preset) run_preset_decision_tree runs these together

```python
axioms = {
    "disjoint_groups": [],
    "min_cardinality": [
        {"class": "DecisionPoint", "property": "has_condition", "min": 1, "range_class": "Condition"},
        {"class": "Condition", "property": "leads_to", "min": 1, "range_class": "Option"},
    ],
    "equivalent_classes": [
        {"name": "DeadEndCondition", "base_class": "Condition",
         "condition": "Condition without a linked Option",
         "owl_pattern": "Condition & NOT(leads_to.some(Option))"},
    ],
}
```

## 9. Multi-level classification mapping (classification_chain)

A multi-level mapping of allowed links from a type through sub-fields to detailed items. Use it to pick indicators, evaluation criteria or allocation items according to a classification. The user sets the number of levels and the category names.

```python
classes = {
    "Category": None,
    "Field": None,
    "Item": None,
    "MeasurementMethod": None,
}

object_properties = {
    "maps_to_field":   {"domain": "Category", "range": "Field"},
    "selects_item":    {"domain": "Field", "range": "Item"},
    "measured_by":     {"domain": "Item", "range": "MeasurementMethod"},
}

data_properties = {
    "item_name":       {"domain": "Item", "range": "str", "functional": True},
    "formula":         {"domain": "MeasurementMethod", "range": "str"},
}
```

Checks:

- (Allowed mapping per level) Use check_mapping_chain to check the allowed rules at each level from Category through Field to Item
- (Two-way coverage) Use check_bidirectional_coverage to find Items that belong to no Field
- (Item and measurement method) Use check_shared_reference to see whether Item and MeasurementMethod refer to the same entities
- (Preset) run_preset_mapping_chain runs these together

```python
axioms = {
    "disjoint_groups": [],
    "min_cardinality": [
        {"class": "Category", "property": "maps_to_field", "min": 1, "range_class": "Field"},
        {"class": "Field", "property": "selects_item", "min": 1, "range_class": "Item"},
        {"class": "Item", "property": "measured_by", "min": 1, "range_class": "MeasurementMethod"},
    ],
    "equivalent_classes": [
        {"name": "UnmappedCategory", "base_class": "Category",
         "condition": "Category not mapped to any Field",
         "owl_pattern": "Category & NOT(maps_to_field.some(Field))"},
    ],
}
```

## Merging and adapting templates

- If the user has their own analysis method, build the TBox from scratch without a template
- If several templates have a class with the same name, use the one with the more detailed parent structure
- Merge all properties whose names do not clash
- If names clash, use the more domain-specific one after the user confirms
- Rename classes and properties and reshape the hierarchy to fit the user's vocabulary
- Merge disjoint_groups, min_cardinality and equivalent_classes from axioms when names do not clash. If axioms on the same class conflict, proceed only after the user confirms
