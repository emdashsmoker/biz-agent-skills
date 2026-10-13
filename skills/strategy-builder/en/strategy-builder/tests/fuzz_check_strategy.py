"""Random type corruption must never raise inside the checker or the charts."""
import copy, random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import test_check_strategy as t
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
import check_strategy as cs

JUNK = [None, 0, 7, True, "", " ", "x", [], ["x"], [None], {}, {"id": None}, 3.5, "1-1", "9-KPI-1"]

def paths(obj, prefix=()):
    yield prefix
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from paths(v, prefix + (k,))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from paths(v, prefix + (i,))

def set_path(obj, path, value):
    for key in path[:-1]:
        obj = obj[key]
    obj[path[-1]] = value

rng = random.Random(20260924)
runs = 0
for name, build in t.ALL_VALID.items():
    base = build()
    all_paths = [p for p in paths(base) if p]
    for _ in range(600):
        state = copy.deepcopy(base)
        for p in rng.sample(all_paths, rng.randint(1, 4)):
            try:
                set_path(state, p, copy.deepcopy(rng.choice(JUNK)))
            except (KeyError, IndexError, TypeError):
                pass
        for step in (1, 5, 6, 7, 8, 9, 10):
            cs.run_checks(state, step, rng.choice(["ko", "en"])).render(step)
        cs.trace_chart(state); cs.vision_chart(state)
        runs += 1
print("fuzz runs without exception:", runs)
