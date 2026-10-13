# AHP Weights

AHP (analytic hierarchy process) asks respondents to compare evaluation criteria two at a time and turns the answers into criterion weights. The consistency ratio (CR) checks whether the answers agree with each other. Korea's preliminary feasibility studies use the same method in their comprehensive evaluation to weight economic, policy and balanced regional growth criteria and to score the option of implementing the project.

## Terms

| Term | Definition |
|---|---|
| Pairwise comparison matrix | Square matrix whose cell in row i, column j holds how many times more important criterion i is than criterion j; the cell in row j, column i holds the reciprocal |
| Weight | Eigenvector for the largest eigenvalue of the matrix, scaled to sum to 1 |
| Largest eigenvalue | Largest eigenvalue of the matrix; it equals the number of items n when answers are fully consistent |
| CI | Consistency index = (largest eigenvalue - n) / (n - 1) |
| RI | Average CI of randomly filled matrices |
| CR | Consistency ratio = CI / RI |

## Comparison Scale

| Value | Label | Meaning |
|---|---|---|
| 1 | Equal | Both criteria matter equally |
| 3 | Moderate | Experience and judgment slightly favor one side |
| 5 | Strong | Experience and judgment strongly favor one side |
| 7 | Very strong | One side is favored very strongly and its dominance is demonstrated in practice |
| 9 | Extreme | Evidence favoring one side reaches the highest possible order |
| 2, 4, 6, 8 | Intermediate | Between two adjacent judgments |

When the row criterion is less important than the column criterion, enter the reciprocal, for example "1/3".

## Formulas

- For each respondent the script computes weights, the largest eigenvalue, CI and CR.
- RI follows Saaty's values. For n from 3 to 10, RI is 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45 and 1.49. CR is 0 when n is 2 or less.
- The script refuses more than 10 items in one comparison. Split the criteria into upper and lower levels and enter each level separately.
- Judgments from several respondents combine through the element-wise geometric mean into a group matrix, and the script recomputes weights and CR from that group matrix.
- With alternatives, the script derives alternative priorities from pairwise comparisons under each criterion. An alternative's overall score is the sum over criteria of criterion weight x the alternative's priority under that criterion.
- For a multi-level hierarchy, run the script once per level. The final weight of a sub-criterion is the parent weight x the sub-criterion weight.

## Decision Rules

| Item | Rule | Basis |
|---|---|---|
| Acceptable consistency | CR of 0.1 or less | Saaty (1987) |
| Korean PFS feedback condition | CR above 0.15 allows feedback such as a repeat survey | Korean PFS guideline Art. 75 |
| Korean PFS project feasibility | Overall score of the implementation option of 0.5 or more | Korean PFS guideline Art. 53 |

`cr_threshold` defaults to 0.1. Enter 0.15 to follow the Korean PFS method. With `exclude_inconsistent` set to `true`, respondents above the threshold drop out of the group matrix. The default `false` keeps every respondent and only lists those above the threshold.

## Input Collection Order

1. List of criteria
2. Pairwise comparisons of criteria from each respondent
3. If alternatives are evaluated, the list of alternatives and pairwise comparisons of alternatives per criterion and per respondent
4. CR threshold and whether to exclude inconsistent answers

## Input Format

The diagonal is 1 and only the upper triangle needs values. Leave the lower triangle as `null` and the script fills in reciprocals. Values entered in the lower triangle are checked against the reciprocal of the upper triangle.

```json
{
  "criteria": ["Economic", "Policy", "Regional balance"],
  "cr_threshold": 0.1,
  "exclude_inconsistent": false,
  "respondents": [
    {"id": "R1", "matrix": [[1, 2, 3], [null, 1, 2], [null, null, 1]]},
    {"id": "R2", "matrix": [[1, "1/2", 2], [null, 1, 3], [null, null, 1]]}
  ],
  "alternatives": ["Implement", "Do not implement"],
  "alternative_judgments": {
    "Economic": [{"id": "R1", "matrix": [[1, 2], [null, 1]]}, {"id": "R2", "matrix": [[1, 1], [null, 1]]}],
    "Policy": [{"id": "R1", "matrix": [[1, 3], [null, 1]]}, {"id": "R2", "matrix": [[1, 2], [null, 1]]}],
    "Regional balance": [{"id": "R1", "matrix": [[1, 2], [null, 1]]}, {"id": "R2", "matrix": [[1, 3], [null, 1]]}]
  }
}
```

## Run Example

```
python scripts/ahp.py --input examples/ahp.json --chart ahp_weights.png
```

## Reporting

- (Results by respondent) Largest eigenvalue, CI, CR, consistency check and weights per criterion
- (Group weights) Weights in descending order and the CR of the group matrix
- (Alternatives) Alternative priorities per criterion and overall score per alternative
- (Notes) Respondents above the CR threshold

## Sources

> Saaty, R. W.(1987), The analytic hierarchy process: what it is and how it is used, Mathematical Modelling 9(3-5)(https://doi.org/10.1016/0270-0255(87)90473-8)

> Saaty, T. L.(2008), Decision making with the analytic hierarchy process, International Journal of Services Sciences 1(1)(https://doi.org/10.1504/IJSSCI.2008.017590)

> Aczél, J. and Saaty, T. L.(1983), Procedures for synthesizing ratio judgements, Journal of Mathematical Psychology 27(1)(https://doi.org/10.1016/0022-2496(83)90028-7)

> Ministry of Planning and Budget, Republic of Korea(2026), 예비타당성조사 수행 총괄지침 (General Guidelines for Conducting Preliminary Feasibility Studies) Articles 53, 75(https://www.law.go.kr/행정규칙/예비타당성조사수행총괄지침)
