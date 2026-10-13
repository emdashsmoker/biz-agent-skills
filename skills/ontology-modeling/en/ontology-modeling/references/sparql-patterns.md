# SPARQL query patterns

## Choosing a route

- Use the check function route for yes/no questions
- Use the SPARQL route for questions answered by a list or a number
- For questions no check function covers, write a SPARQL query before writing new Python code

SPARQL and check functions read only the entered facts. Report unlinked individuals found with FILTER NOT EXISTS as missing-entry candidates, and do not conclude that the link is truly absent.

## Built-in queries (SPARQL_CHECKS)

onto_engine.py contains 12 parameterized SPARQL queries. Run them with run_sparql_check(world, "query_name", onto=onto, **params). Check functions call them internally, so calling them directly is optional.

| Query | Pattern | Parameters |
|---|---|---|
| mece_overlap | Individuals in both classes | class_a, class_b |
| unsupported | Individuals with no value for a property (FILTER NOT EXISTS) | target_class, link_property |
| coverage | Individuals that no referring individual points to | source_class, ref_class, link_property |
| edges | All links of a property | property |
| cardinality_count | Links per individual (GROUP BY, COUNT) | parent_class, property_name |
| refs_for_class | Targets referenced per class | subject_class, link_property |
| value_below | Values below a minimum (FILTER) | target_class, value_property, min_val |
| value_above | Values above a maximum (FILTER) | target_class, value_property, max_val |
| downstream | Individuals reachable along a property path | start, order_property |
| conflict_dual_ref | Individuals pointing to the same target through two properties | prop_a, prop_b |
| mandatory_missing | Stages without a required output class (nested FILTER NOT EXISTS) | stage_class, output_property, required_class |
| stage_unlinked | Individuals without a link to the next stage | stage_class, link_property |

The return value is {"check": query name, "sparql": the executed query, "results": rows, "count": number of rows, "pass": True when there are no rows}.

## Free query patterns

Patterns within the range owlready2's SPARQL engine supports.

| Query type | SPARQL pattern | Example question |
|---|---|---|
| Filter | SELECT ?x WHERE { ?x a :Class . ?x :prop ?v . FILTER(?v > N) } | Which programs have a budget of one billion or more? |
| Aggregate | SELECT ?x (COUNT(?y) AS ?cnt) WHERE { ... } GROUP BY ?x | How many factors does each strategy use? |
| Missing link | SELECT ?x WHERE { ?x a :Class . FILTER NOT EXISTS { ?x :prop ?y } } | Which activities have no goal? |
| Path search | SELECT ?x ?y WHERE { ?x :precedes+ ?y } | Which later activities can be reached from activity A? |
| Value comparison | SELECT ?x WHERE { ?x :propA ?a . ?x :propB ?b . FILTER(?a = ?b) } | Which programs reach the same group they declared as their target? |
| Optional | SELECT ?x ?y WHERE { ?x a :Class . OPTIONAL { ?x :prop ?y } } | List the manager of every program, including programs without one |
| Union | SELECT ?x WHERE { { ?x a :TypeA } UNION { ?x a :TypeB } } | Which tasks are short-term or urgent? |

## Code examples

```python
# query_onto: free query with prefixes added automatically (recommended)
rows = query_onto(world, onto,
    "SELECT ?project ?b WHERE { "
    "?project a :Project . ?project :budget ?b . FILTER(?b >= 1000000000) }")

# aggregate
rows = query_onto(world, onto,
    "SELECT ?strategy (COUNT(?factor) AS ?cnt) WHERE { "
    "?strategy a :Strategy . ?strategy :uses_factor ?factor "
    "} GROUP BY ?strategy ORDER BY DESC(?cnt)")

# missing links
rows = query_onto(world, onto,
    "SELECT ?activity WHERE { ?activity a :Activity . "
    "FILTER NOT EXISTS { ?activity :achieves ?obj } }")

# optional
rows = query_onto(world, onto,
    "SELECT ?project ?manager WHERE { ?project a :Project . "
    "OPTIONAL { ?project :managed_by ?manager } }")

# run a built-in query
r = run_sparql_check(world, "coverage", onto=onto,
    source_class="Goal", ref_class="Strategy", link_property="achieves")
print(r["results"], r["pass"])

# run a custom query with the same return format
r = run_sparql_check(world, "_adhoc", onto=onto,
    sparql_body="SELECT ?x WHERE { ?x a :Strategy . "
                "FILTER NOT EXISTS { ?x :achieves ?g } }",
    label="strategy_without_goal")
print(r["results"], r["count"], r["pass"])
```

## Query suggestions

suggest_sparql_queries(onto) scans the current TBox and proposes exploratory queries. Use it at the start of the check stage to show the user what can be asked, and run the suggestions directly with query_onto.

```python
for s in suggest_sparql_queries(onto):
    rows = query_onto(world, onto, s["sparql"])
    print(f"[{s['label']}] {s['description']}: {len(rows)} rows")
```

## Answering competency questions

- Translate a competency question into a SPARQL WHERE clause and run it with query_onto first. It answers the question without new Python code
- For questions a check function already covers, use its result as is
- For answerable competency questions, present the actual result (SPARQL or check function result)
- For unanswerable competency questions, say which classes, properties or individuals to add
- Report competency questions added in later turns the same way

## Result report format

Report SPARQL results in three parts: the query, the result and the interpretation. The query and result are outputs for the user to verify, so show them as they are.

```markdown
### Q1. Activities without a goal

| Part | Content |
|---|---|
| SPARQL | `SELECT ?a WHERE { ?a a :Activity . FILTER NOT EXISTS { ?a :achieves ?o } }` |
| Question | Which activities have no goal? |

| Part | Content |
|---|---|
| Returned | `['activity_3', 'activity_7']` |
| Answer | Two activities are not linked to any goal |

| Returned | Interpretation |
|---|---|
| activity_3 | No goal was entered for the field training activity |
| activity_7 | No goal was entered for the promotion activity |

- Both activities are missing-entry candidates. Whether they are unrelated to any goal has to be confirmed in the source material
```

Write any pattern you find in the results as bullets that a reader without ontology training can understand.
