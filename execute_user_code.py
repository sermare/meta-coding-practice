#!/usr/bin/env python3
"""
Subprocess script that executes user code against test cases.
Called by app.py with: python3 execute_user_code.py <problem_id> <temp_code_path>
"""
import sys
import os
import json
import time
import traceback
import inspect

# Ensure project root is on path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

from problem_registry import PROBLEMS


def _slug(title):
    return title.lower().replace(" ", "_").replace("(", "").replace(")", "").replace(",", "").replace("'", "")


def main():
    if len(sys.argv) != 3:
        print(json.dumps({"error": "Usage: execute_user_code.py <pid> <code_path>", "results": []}))
        sys.exit(1)

    pid = int(sys.argv[1])
    code_path = sys.argv[2]

    p = PROBLEMS.get(pid)
    if not p:
        print(json.dumps({"error": "Problem not found", "results": []}))
        sys.exit(1)

    slug = _slug(p["title"])

    # Read user code
    with open(code_path, "r") as f:
        user_code = f.read()

    # Step 1: Import the problem module first
    problem_module_name = "problems.p{:03d}_{}".format(pid, slug)
    test_module_name = "tests.test_p{:03d}_{}".format(pid, slug)

    # Remove from cache if previously imported
    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("problems.") or mod_name.startswith("tests."):
            del sys.modules[mod_name]

    # Import problem module
    import importlib
    problem_mod = importlib.import_module(problem_module_name)

    # Step 2: Execute user code and extract solution
    user_globals = {}
    # Include helpers from the problem module (ListNode, TreeNode, etc.)
    for name in dir(problem_mod):
        obj = getattr(problem_mod, name)
        if not name.startswith("_"):
            user_globals[name] = obj

    try:
        exec(compile(user_code, "<user_code>", "exec"), user_globals)
    except Exception as e:
        print(json.dumps({
            "error": "Compilation error: {}".format(str(e)),
            "results": []
        }))
        sys.exit(0)

    # Find the solution in user code
    if "solution" not in user_globals:
        # Check for class-based solutions (LRUCache, Trie, Codec)
        print(json.dumps({
            "error": "No 'solution' found in your code. Make sure you define a 'solution' function or assign 'solution = YourClass'.",
            "results": []
        }))
        sys.exit(0)

    user_solution = user_globals["solution"]

    # Step 3: Patch the problem module's solution before importing tests
    problem_mod.solution = user_solution
    setattr(problem_mod, "solution", user_solution)

    # For class-based problems, also patch the class name
    for name, obj in user_globals.items():
        if isinstance(obj, type) and name != "solution":
            if hasattr(problem_mod, name):
                setattr(problem_mod, name, obj)

    # Step 4: Now import test module (it will pick up patched solution)
    test_mod = importlib.import_module(test_module_name)

    if not hasattr(test_mod, "TEST_CASES"):
        print(json.dumps({"error": "No TEST_CASES found", "results": []}))
        sys.exit(0)

    # Step 5: Run each test case
    results = []
    for i, tc in enumerate(test_mod.TEST_CASES):
        result = {
            "test_num": i + 1,
            "description": tc.get("description", "Test {}".format(i + 1)),
            "passed": False,
            "expected": None,
            "got": None,
            "error": None,
            "time_ms": 0,
        }

        try:
            run_fn = tc["run"]
            start = time.time()

            # Support both lambda styles
            params = inspect.signature(run_fn).parameters
            if len(params) > 0:
                got = run_fn(user_solution)
            else:
                got = run_fn()

            elapsed = time.time() - start
            result["time_ms"] = round(elapsed * 1000, 1)

            expected = tc["expected"]
            result["expected"] = repr(expected)
            result["got"] = repr(got)

            # Compare
            comparator = tc.get("comparator", None)
            if comparator:
                is_correct = comparator(got, expected)
            elif isinstance(expected, list) and isinstance(got, list):
                try:
                    is_correct = sorted([sorted(x) if isinstance(x, list) else x for x in got]) == \
                                 sorted([sorted(x) if isinstance(x, list) else x for x in expected])
                except TypeError:
                    is_correct = got == expected
            else:
                is_correct = got == expected

            result["passed"] = is_correct

        except Exception as e:
            result["error"] = "{}: {}".format(type(e).__name__, str(e))
            result["got"] = None

        results.append(result)

    all_passed = all(r["passed"] for r in results)
    passed_count = sum(1 for r in results if r["passed"])

    output = {
        "results": results,
        "summary": {
            "passed": passed_count,
            "total": len(results),
            "all_passed": all_passed,
        },
        "error": None,
    }

    print(json.dumps(output))


if __name__ == "__main__":
    main()
