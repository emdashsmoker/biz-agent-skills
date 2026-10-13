"""AHP (Analytic Hierarchy Process) weights and consistency ratio.

Weights come from the principal eigenvector of each pairwise comparison
matrix. Group judgments are combined by the element-wise geometric mean.
"""
import argparse
from fractions import Fraction

import chart
from common import InputError, Report, add_common_args, fmt_num, load_json, num, run_main
from labels import T

# Saaty's random index for matrix sizes 1-10
RANDOM_INDEX = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
DEFAULT_CR_THRESHOLD = 0.1
RECIPROCAL_TOLERANCE = 0.01
CR_DECIMALS = 4


def parse_value(value, where):
    if isinstance(value, str):
        try:
            return float(Fraction(value.strip()))
        except (ValueError, ZeroDivisionError):
            raise InputError(T("ahp_bad_value", where=where, value=value))
    return float(value)


def build_matrix(raw, size, where):
    """Accept a full matrix or an upper triangle with null in the lower half."""
    import numpy as np

    if len(raw) != size or any(len(row) != size for row in raw):
        raise InputError(T("ahp_matrix_size", where=where, n=size))
    m = np.ones((size, size))
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            upper = raw[i][j] if i < j else raw[j][i]
            if upper is None:
                raise InputError(T("ahp_missing_cell", where=where, i=i + 1, j=j + 1))
            upper_value = parse_value(upper, where)
            if upper_value <= 0:
                raise InputError(T("ahp_positive", where=where))
            m[i][j] = upper_value if i < j else 1 / upper_value
            given = raw[i][j]
            if i > j and given is not None:
                given_value = parse_value(given, where)
                if abs(given_value * upper_value - 1) > RECIPROCAL_TOLERANCE:
                    raise InputError(T("ahp_not_reciprocal", where=where, i=i + 1, j=j + 1))
    return m


def priority(matrix):
    """Return (weights, lambda_max, CI, CR)."""
    import numpy as np

    n = matrix.shape[0]
    if n > max(RANDOM_INDEX):
        raise InputError(T("ahp_too_many", n=n))
    values, vectors = np.linalg.eig(matrix)
    k = int(np.argmax(values.real))
    weights = np.abs(vectors[:, k].real)
    weights = weights / weights.sum()
    lambda_max = float(values[k].real)
    if n <= 2:
        return weights, lambda_max, 0.0, 0.0
    ci = (lambda_max - n) / (n - 1)
    return weights, lambda_max, ci, ci / RANDOM_INDEX[n]


def geometric_mean(matrices):
    import numpy as np

    stacked = np.array(matrices)
    return np.exp(np.log(stacked).mean(axis=0))


def evaluate_level(names, respondents, threshold, exclude, where):
    """Individual results plus the aggregated group result for one comparison level."""
    individual, used = [], []
    for resp in respondents:
        rid = str(resp.get("id", len(individual) + 1))
        m = build_matrix(resp["matrix"], len(names), f"{where}/{rid}")
        w, lam, ci, cr = priority(m)
        ok = cr <= threshold
        individual.append({"id": rid, "weights": w.tolist(), "lambda_max": lam, "ci": ci,
                           "cr": cr, "consistent": ok})
        if ok or not exclude:
            used.append(m)
    if not used:
        raise InputError(T("ahp_none_consistent", where=where))
    gw, glam, gci, gcr = priority(geometric_mean(used))
    return {"individual": individual, "used": len(used),
            "group": {"weights": gw.tolist(), "lambda_max": glam, "ci": gci, "cr": gcr}}


def main():
    parser = argparse.ArgumentParser(description="AHP weights and consistency")
    parser.add_argument("--input", required=True, help="JSON file, see references/ahp.md")
    add_common_args(parser)
    args = parser.parse_args()
    d = max(args.decimals, 3)
    cfg = load_json(args.input)
    warnings = []

    criteria = cfg["criteria"]
    threshold = float(cfg.get("cr_threshold", DEFAULT_CR_THRESHOLD))
    exclude = bool(cfg.get("exclude_inconsistent", False))
    level = evaluate_level(criteria, cfg["respondents"], threshold, exclude, T("criteria"))

    report = Report(d)
    report.table(T("inputs"), [T("item"), T("value")], [
        [T("criteria"), ", ".join(criteria)], [T("respondents"), len(cfg["respondents"])],
        [T("cr_threshold"), threshold],
        [T("exclude_inconsistent"), T("yes") if exclude else T("no")]])
    report.table(T("ahp_individual"),
                 [T("respondent"), T("lambda_max"), "CI", "CR", T("consistent")] + criteria,
                 [[r["id"], num(r["lambda_max"]), num(r["ci"], CR_DECIMALS), num(r["cr"], CR_DECIMALS),
                   T("yes") if r["consistent"] else T("no")] + [num(w) for w in r["weights"]]
                  for r in level["individual"]])
    inconsistent = [r["id"] for r in level["individual"] if not r["consistent"]]
    if inconsistent:
        warnings.append(T("ahp_inconsistent_list", ids=", ".join(inconsistent), t=threshold))

    group = level["group"]
    order = sorted(range(len(criteria)), key=lambda i: -group["weights"][i])
    report.table(T("ahp_group"), [T("rank"), T("criterion"), T("weight")],
                 [[rank + 1, criteria[i], num(group["weights"][i])] for rank, i in enumerate(order)])
    report.table(T("ahp_group_consistency"), [T("lambda_max"), "CI", "CR", T("respondents_used")],
                 [[num(group["lambda_max"]), num(group["ci"], CR_DECIMALS),
                   num(group["cr"], CR_DECIMALS), level["used"]]])

    output = {"criteria": criteria, "threshold": threshold, "criteria_level": level}
    alternatives = cfg.get("alternatives")
    if alternatives:
        scores = [0.0] * len(alternatives)
        local_rows = []
        output["alternative_levels"] = {}
        for ci_index, name in enumerate(criteria):
            judgments = cfg.get("alternative_judgments", {}).get(name)
            if not judgments:
                raise InputError(T("ahp_missing_alt", criterion=name))
            alt_level = evaluate_level(alternatives, judgments, threshold, exclude, name)
            output["alternative_levels"][name] = alt_level
            local = alt_level["group"]["weights"]
            for a in range(len(alternatives)):
                scores[a] += group["weights"][ci_index] * local[a]
            local_rows.append([name, num(group["weights"][ci_index])] + [num(v) for v in local]
                              + [num(alt_level["group"]["cr"], CR_DECIMALS)])
        report.table(T("ahp_local"), [T("criterion"), T("weight")] + alternatives + ["CR"], local_rows)
        report.table(T("result"), [T("alternative"), T("overall_score")],
                     [[a, num(s)] for a, s in zip(alternatives, scores)])
        output["overall_scores"] = dict(zip(alternatives, scores))
    report.warnings(warnings)
    report.finish(args, output)
    if args.chart:
        chart.barh([criteria[i] for i in order], [group["weights"][i] for i in order],
                   args.chart, lambda v: fmt_num(v, 3))

if __name__ == "__main__":
    run_main(main)
