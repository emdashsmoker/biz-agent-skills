"""AHP priority weights, consistency ratio, group aggregation, and composite scores.

Weights w = principal eigenvector of the pairwise matrix A (power iteration, sum to 1).
lambda_max = mean((A w)_i / w_i), CI = (lambda_max - n) / (n - 1), CR = CI / RI(n).
RI values: Saaty (2000). Matrices with n <= 2 are always consistent (CR = 0).
Group weights: element-wise geometric mean of the evaluators' matrices (AIJ), then eigenvector.
Composite score per evaluator = sum(own weight_c * rating_c); summary gives the mean and a
trimmed mean that drops the `trim` highest and `trim` lowest evaluator scores.
"""

import math
from fractions import Fraction

from _common import (InputError, build_parser, load_input, md_table, require,
                     run, section, to_number, write_json)

RANDOM_INDEX = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
MAX_ITEMS = max(RANDOM_INDEX)
CR_THRESHOLD_DEFAULT = 0.10
SAATY_MIN, SAATY_MAX = 1 / 9, 9
RECIPROCAL_TOLERANCE = 1e-6
POWER_ITERATIONS = 1000
POWER_TOLERANCE = 1e-12

EXAMPLE = {
    "criteria": ["Economic", "Policy", "Regional balance"],
    "parent_weight": 1.0,
    "cr_threshold": CR_THRESHOLD_DEFAULT,
    "evaluators": {
        "E1": {"upper": [2, 3, 2]},
        "E2": {"upper": ["1/2", 2, 3]},
        "E3": {"matrix": [[1, 3, 5], ["1/3", 1, 2], ["1/5", "1/2", 1]]},
    },
    "ratings": {
        "E1": {"Economic": 0.55, "Policy": 0.70, "Regional balance": 0.40},
        "E2": {"Economic": 0.50, "Policy": 0.60, "Regional balance": 0.45},
        "E3": {"Economic": 0.65, "Policy": 0.55, "Regional balance": 0.50},
    },
    "trim": 0,
}


def parse_value(value, where):
    """Accept numbers or fraction strings such as '1/3'."""
    if isinstance(value, str):
        try:
            return float(Fraction(value.strip()))
        except (ValueError, ZeroDivisionError) as exc:
            raise InputError(f"{where}: cannot read {value!r}") from exc
    return to_number(value, where)


def build_matrix(spec, n, name):
    """Return a full n x n reciprocal matrix from 'upper' (row-wise) or 'matrix'."""
    if "upper" in spec:
        upper = [parse_value(v, f"{name}.upper") for v in spec["upper"]]
        if len(upper) != n * (n - 1) // 2:
            raise InputError(f"{name}: 'upper' needs {n * (n - 1) // 2} values for {n} criteria")
        matrix = [[1.0] * n for _ in range(n)]
        values = iter(upper)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j] = next(values)
                matrix[j][i] = 1 / matrix[i][j]
    else:
        raw = require(spec, "matrix", name)
        matrix = [[parse_value(v, f"{name}.matrix") for v in row] for row in raw]
        if len(matrix) != n or any(len(row) != n for row in matrix):
            raise InputError(f"{name}: matrix must be {n} x {n}")
    for i in range(n):
        for j in range(n):
            a = matrix[i][j]
            if a <= 0:
                raise InputError(f"{name}: entries must be positive")
            if abs(a * matrix[j][i] - 1) > RECIPROCAL_TOLERANCE:
                raise InputError(f"{name}: entry ({i + 1},{j + 1}) is not the reciprocal of "
                                 f"({j + 1},{i + 1})")
            if not SAATY_MIN - 1e-9 <= a <= SAATY_MAX + 1e-9:
                print(f"NOTE: {name} entry ({i + 1},{j + 1}) = {a:.3f} is outside the 1/9-9 scale")
    return matrix


def priority(matrix):
    """Principal eigenvector by power iteration, with lambda_max, CI, CR."""
    n = len(matrix)
    w = [1 / n] * n
    for _ in range(POWER_ITERATIONS):
        product = [sum(matrix[i][j] * w[j] for j in range(n)) for i in range(n)]
        total = sum(product)
        new = [v / total for v in product]
        if max(abs(a - b) for a, b in zip(new, w)) < POWER_TOLERANCE:
            w = new
            break
        w = new
    aw = [sum(matrix[i][j] * w[j] for j in range(n)) for i in range(n)]
    lam = sum(aw[i] / w[i] for i in range(n)) / n
    ci = (lam - n) / (n - 1) if n > 2 else 0.0
    cr = ci / RANDOM_INDEX[n] if RANDOM_INDEX[n] else 0.0
    return w, lam, ci, cr


def geometric_mean_matrix(matrices):
    n, k = len(matrices[0]), len(matrices)
    return [[math.prod(m[i][j] for m in matrices) ** (1 / k) for j in range(n)] for i in range(n)]


def main():
    args = build_parser(__doc__, EXAMPLE).parse_args()
    data = load_input(args)
    criteria = require(data, "criteria")
    n = len(criteria)
    if not 2 <= n <= MAX_ITEMS:
        raise InputError(f"use 2 to {MAX_ITEMS} criteria per matrix (split larger sets into levels)")
    threshold = to_number(data.get("cr_threshold", CR_THRESHOLD_DEFAULT), "cr_threshold")
    parent = to_number(data.get("parent_weight", 1.0), "parent_weight")
    evaluators = require(data, "evaluators")

    results, matrices = {}, {}
    for name, spec in evaluators.items():
        matrices[name] = build_matrix(spec, n, name)
        w, lam, ci, cr = priority(matrices[name])
        results[name] = {"weights": w, "lambda_max": lam, "ci": ci, "cr": cr,
                         "consistent": cr <= threshold}

    print(f"# AHP report ({n} criteria, CR threshold {threshold:g})\n")
    section("Evaluator weights", md_table(
        ["evaluator"] + criteria + ["lambda_max", "CI", "CR", "CR ok"],
        [[e] + r["weights"] + [r["lambda_max"], r["ci"], r["cr"], r["consistent"]]
         for e, r in results.items()], decimals=4))

    passing = [e for e, r in results.items() if r["consistent"]]
    use = passing if data.get("aggregate_consistent_only", False) and passing else list(results)
    group_w, group_lam, _, group_cr = priority(geometric_mean_matrix([matrices[e] for e in use]))
    section(f"Group weights (geometric mean of {len(use)} matrices)", md_table(
        ["criterion", "local weight", f"global weight (x {parent:g})"],
        [[c, w, w * parent] for c, w in zip(criteria, group_w)], decimals=4))
    print(f"Group matrix: lambda_max {group_lam:.4f}, CR {group_cr:.4f}\n")

    payload = {"evaluators": results, "group_weights": dict(zip(criteria, group_w)),
               "group_cr": group_cr}
    ratings = data.get("ratings")
    if ratings:
        trim = int(data.get("trim", 0))
        scores = {}
        for name, r in results.items():
            if name not in ratings:
                raise InputError(f"no ratings for evaluator '{name}'")
            scores[name] = sum(w * to_number(require(ratings[name], c, f"ratings.{name}"), c)
                               for w, c in zip(r["weights"], criteria))
        ordered = sorted(scores.values())
        if len(ordered) <= 2 * trim:
            raise InputError(f"trim={trim} removes every evaluator")
        kept = ordered[trim:len(ordered) - trim]
        section("Composite scores", md_table(
            ["evaluator", "score", "CR ok"],
            [[e, s, results[e]["consistent"]] for e, s in scores.items()], decimals=4))
        print(f"Mean {sum(ordered) / len(ordered):.4f} | trimmed mean (drop {trim} high, {trim} low) "
              f"{sum(kept) / len(kept):.4f}\n")
        payload["scores"] = scores
    write_json(args.json, payload)


if __name__ == "__main__":
    run(main)
