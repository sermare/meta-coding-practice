#!/usr/bin/env python3
"""
META Coding Interview Practice Runner
A LeetCode-style local testing environment for the top 50 META interview questions.
"""

import argparse
import importlib
import json
import os
import sys
import time
import traceback
from pathlib import Path

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class Fore:
        GREEN = RED = YELLOW = CYAN = MAGENTA = WHITE = BLUE = RESET = ""
    class Style:
        BRIGHT = RESET_ALL = ""

try:
    from tabulate import tabulate
except ImportError:
    tabulate = None

from problem_registry import PROBLEMS, get_problem, get_problems_by_difficulty, get_problems_by_category


PROGRESS_FILE = os.path.join(os.path.dirname(__file__), ".progress.json")


def _run_test_case(tc, sol_mod=None):
    """Run a test case, supporting both lambda styles."""
    import inspect
    run_fn = tc["run"]
    if len(inspect.signature(run_fn).parameters) > 0:
        return run_fn(sol_mod.solution if sol_mod else None)
    else:
        return run_fn()


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def difficulty_color(diff):
    colors = {"Easy": Fore.GREEN, "Medium": Fore.YELLOW, "Hard": Fore.RED}
    return colors.get(diff, "") + diff + Style.RESET_ALL


def list_problems(args):
    """List all available problems."""
    problems = PROBLEMS
    if args.difficulty:
        problems = get_problems_by_difficulty(args.difficulty)
    if args.category:
        problems = get_problems_by_category(args.category)

    progress = load_progress()

    if tabulate:
        headers = ["#", "Title", "Difficulty", "Category", "LC#", "Status"]
        rows = []
        for pid, p in sorted(problems.items()):
            status = progress.get(str(pid), {}).get("status", "")
            status_icon = ""
            if status == "passed":
                status_icon = Fore.GREEN + "SOLVED" + Style.RESET_ALL
            elif status == "attempted":
                status_icon = Fore.YELLOW + "ATTEMPTED" + Style.RESET_ALL
            rows.append([
                pid,
                p["title"],
                difficulty_color(p["difficulty"]),
                p["category"],
                p["leetcode_num"],
                status_icon,
            ])
        print(f"\n{Fore.CYAN}{Style.BRIGHT}META Coding Interview Problems ({len(rows)} problems){Style.RESET_ALL}\n")
        print(tabulate(rows, headers=headers, tablefmt="simple"))
    else:
        print(f"\nMETA Coding Interview Problems ({len(problems)} problems)\n")
        print(f"{'#':<4} {'Title':<45} {'Diff':<8} {'Category':<25} {'LC#':<6}")
        print("-" * 90)
        for pid, p in sorted(problems.items()):
            print(f"{pid:<4} {p['title']:<45} {p['difficulty']:<8} {p['category']:<25} {p['leetcode_num']:<6}")
    print()


def describe_problem(args):
    """Show full problem description."""
    pid = args.problem_id
    p = get_problem(pid)
    if not p:
        print(f"{Fore.RED}Problem {pid} not found.{Style.RESET_ALL}")
        return

    try:
        mod = importlib.import_module(f"problems.p{pid:03d}_{_slug(p['title'])}")
        print(f"\n{Fore.CYAN}{Style.BRIGHT}Problem {pid}: {p['title']}{Style.RESET_ALL}")
        print(f"Difficulty: {difficulty_color(p['difficulty'])}")
        print(f"Category: {p['category']}")
        print(f"LeetCode #: {p['leetcode_num']}")
        print(f"Source: {p['source']}")
        print(f"Reference: {p['ref']}")
        print()
        if hasattr(mod, "DESCRIPTION"):
            print(mod.DESCRIPTION)
        print()
    except ModuleNotFoundError:
        print(f"{Fore.RED}Problem file for #{pid} not found.{Style.RESET_ALL}")


def solve_problem(args):
    """Open the problem file for editing."""
    pid = args.problem_id
    p = get_problem(pid)
    if not p:
        print(f"{Fore.RED}Problem {pid} not found.{Style.RESET_ALL}")
        return

    slug = _slug(p["title"])
    filepath = os.path.join(os.path.dirname(__file__), "problems", f"p{pid:03d}_{slug}.py")

    if not os.path.exists(filepath):
        print(f"{Fore.RED}Problem file {filepath} not found.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}Problem {pid}: {p['title']}{Style.RESET_ALL}")
    print(f"File: {filepath}")
    print(f"\nEdit the solution() function in the file above.")

    editor = os.environ.get("EDITOR", "vim")
    print(f"Opening with {editor}...")
    os.system(f"{editor} {filepath}")


def test_problem(args):
    """Run test cases for a problem."""
    if args.problem_id == "all":
        return test_all(args)

    pid = int(args.problem_id)
    p = get_problem(pid)
    if not p:
        print(f"{Fore.RED}Problem {pid} not found.{Style.RESET_ALL}")
        return

    slug = _slug(p["title"])
    verbose = args.verbose

    print(f"\n{Fore.CYAN}{Style.BRIGHT}Testing Problem {pid}: {p['title']}{Style.RESET_ALL}")
    print(f"Difficulty: {difficulty_color(p['difficulty'])}")
    print("-" * 50)

    try:
        test_mod = importlib.import_module(f"tests.test_p{pid:03d}_{slug}")
        sol_mod = importlib.import_module(f"problems.p{pid:03d}_{slug}")
    except ModuleNotFoundError as e:
        print(f"{Fore.RED}Module not found: {e}{Style.RESET_ALL}")
        return

    if not hasattr(test_mod, "TEST_CASES"):
        print(f"{Fore.RED}No TEST_CASES found in test module.{Style.RESET_ALL}")
        return

    if not hasattr(sol_mod, "solution"):
        print(f"{Fore.RED}No solution() function found. Implement it in problems/p{pid:03d}_{slug}.py{Style.RESET_ALL}")
        return

    passed = 0
    failed = 0
    errors = 0
    total = len(test_mod.TEST_CASES)

    progress = load_progress()

    for i, tc in enumerate(test_mod.TEST_CASES, 1):
        try:
            start = time.time()
            result = _run_test_case(tc, sol_mod)
            elapsed = time.time() - start
            expected = tc["expected"]

            # Handle cases where order doesn't matter
            comparator = tc.get("comparator", None)
            if comparator:
                is_correct = comparator(result, expected)
            elif isinstance(expected, list) and isinstance(result, list):
                # For nested lists of lists, try sorting
                try:
                    is_correct = sorted([sorted(x) if isinstance(x, list) else x for x in result]) == \
                                 sorted([sorted(x) if isinstance(x, list) else x for x in expected])
                except TypeError:
                    is_correct = result == expected
            else:
                is_correct = result == expected

            if is_correct:
                passed += 1
                if verbose:
                    print(f"  {Fore.GREEN}Test {i}/{total}: PASSED{Style.RESET_ALL} ({elapsed*1000:.1f}ms)")
            else:
                failed += 1
                print(f"  {Fore.RED}Test {i}/{total}: FAILED{Style.RESET_ALL}")
                if verbose:
                    print(f"    Input:    {tc.get('description', 'N/A')}")
                    print(f"    Expected: {expected}")
                    print(f"    Got:      {result}")
        except Exception as e:
            errors += 1
            print(f"  {Fore.RED}Test {i}/{total}: ERROR - {e}{Style.RESET_ALL}")
            if verbose:
                traceback.print_exc()

    print("-" * 50)
    if failed == 0 and errors == 0:
        print(f"  {Fore.GREEN}{Style.BRIGHT}ALL {total} TESTS PASSED!{Style.RESET_ALL}")
        progress[str(pid)] = {"status": "passed", "passed": passed, "total": total}
    else:
        print(f"  Passed: {Fore.GREEN}{passed}{Style.RESET_ALL}  "
              f"Failed: {Fore.RED}{failed}{Style.RESET_ALL}  "
              f"Errors: {Fore.RED}{errors}{Style.RESET_ALL}  "
              f"Total: {total}")
        progress[str(pid)] = {"status": "attempted", "passed": passed, "total": total}

    save_progress(progress)
    print()


def test_all(args):
    """Test all problems."""
    print(f"\n{Fore.CYAN}{Style.BRIGHT}Running all tests...{Style.RESET_ALL}\n")
    total_passed = 0
    total_failed = 0
    total_errors = 0
    total_not_implemented = 0

    for pid, p in sorted(PROBLEMS.items()):
        slug = _slug(p["title"])
        try:
            test_mod = importlib.import_module(f"tests.test_p{pid:03d}_{slug}")
            sol_mod = importlib.import_module(f"problems.p{pid:03d}_{slug}")
        except ModuleNotFoundError:
            continue

        if not hasattr(sol_mod, "solution") or not hasattr(test_mod, "TEST_CASES"):
            continue

        # Check if solution is implemented (not just pass)
        try:
            first_tc = test_mod.TEST_CASES[0]
            result = _run_test_case(first_tc, sol_mod)
            if result is None:
                total_not_implemented += 1
                print(f"  {pid:>3}. {p['title']:<40} {Fore.YELLOW}NOT IMPLEMENTED{Style.RESET_ALL}")
                continue
        except NotImplementedError:
            total_not_implemented += 1
            print(f"  {pid:>3}. {p['title']:<40} {Fore.YELLOW}NOT IMPLEMENTED{Style.RESET_ALL}")
            continue
        except Exception:
            pass

        passed = 0
        failed = 0
        for tc in test_mod.TEST_CASES:
            try:
                result = _run_test_case(tc, sol_mod)
                expected = tc["expected"]
                comparator = tc.get("comparator", None)
                if comparator:
                    is_correct = comparator(result, expected)
                elif isinstance(expected, list) and isinstance(result, list):
                    try:
                        is_correct = sorted([sorted(x) if isinstance(x, list) else x for x in result]) == \
                                     sorted([sorted(x) if isinstance(x, list) else x for x in expected])
                    except TypeError:
                        is_correct = result == expected
                else:
                    is_correct = result == expected
                if is_correct:
                    passed += 1
                else:
                    failed += 1
            except Exception:
                failed += 1

        total = len(test_mod.TEST_CASES)
        if failed == 0:
            total_passed += 1
            print(f"  {pid:>3}. {p['title']:<40} {Fore.GREEN}PASSED ({passed}/{total}){Style.RESET_ALL}")
        else:
            total_failed += 1
            print(f"  {pid:>3}. {p['title']:<40} {Fore.RED}FAILED ({passed}/{total}){Style.RESET_ALL}")

    print(f"\n{'-'*60}")
    print(f"  Solved: {Fore.GREEN}{total_passed}{Style.RESET_ALL}  "
          f"Failed: {Fore.RED}{total_failed}{Style.RESET_ALL}  "
          f"Not Implemented: {Fore.YELLOW}{total_not_implemented}{Style.RESET_ALL}  "
          f"Total: {len(PROBLEMS)}")
    print()


def show_progress(args):
    """Show solving progress."""
    progress = load_progress()
    solved = sum(1 for v in progress.values() if v.get("status") == "passed")
    attempted = sum(1 for v in progress.values() if v.get("status") == "attempted")
    total = len(PROBLEMS)

    print(f"\n{Fore.CYAN}{Style.BRIGHT}Your Progress{Style.RESET_ALL}")
    print(f"{'='*40}")
    print(f"  {Fore.GREEN}Solved:      {solved}/{total}{Style.RESET_ALL}")
    print(f"  {Fore.YELLOW}Attempted:   {attempted}/{total}{Style.RESET_ALL}")
    print(f"  Not Started: {total - solved - attempted}/{total}")
    print()

    # Breakdown by difficulty
    for diff in ["Easy", "Medium", "Hard"]:
        diff_problems = get_problems_by_difficulty(diff)
        diff_solved = sum(1 for pid in diff_problems if progress.get(str(pid), {}).get("status") == "passed")
        print(f"  {difficulty_color(diff)}: {diff_solved}/{len(diff_problems)}")
    print()


def _slug(title):
    """Convert title to file-safe slug."""
    return title.lower().replace(" ", "_").replace("(", "").replace(")", "").replace(",", "").replace("'", "")


def main():
    parser = argparse.ArgumentParser(
        description="META Coding Interview Practice Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python runner.py list                    # List all problems
  python runner.py list --difficulty easy   # Filter by difficulty
  python runner.py describe 1              # View problem description
  python runner.py solve 1                 # Open problem for editing
  python runner.py test 1                  # Test your solution
  python runner.py test 1 -v               # Test with verbose output
  python runner.py test all                # Test all solutions
  python runner.py progress                # View your progress
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # list
    list_parser = subparsers.add_parser("list", help="List all problems")
    list_parser.add_argument("--difficulty", "-d", choices=["easy", "medium", "hard"])
    list_parser.add_argument("--category", "-c", type=str, help="Filter by category keyword")

    # describe
    desc_parser = subparsers.add_parser("describe", help="View problem description")
    desc_parser.add_argument("problem_id", type=int, help="Problem number")

    # solve
    solve_parser = subparsers.add_parser("solve", help="Open problem for editing")
    solve_parser.add_argument("problem_id", type=int, help="Problem number")

    # test
    test_parser = subparsers.add_parser("test", help="Test your solution")
    test_parser.add_argument("problem_id", type=str, help="Problem number or 'all'")
    test_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    # progress
    subparsers.add_parser("progress", help="Show progress")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "list": list_problems,
        "describe": describe_problem,
        "solve": solve_problem,
        "test": test_problem,
        "progress": show_progress,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
