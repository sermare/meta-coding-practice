from problems.p243_combination_sum_ii import solution

TEST_CASES = [
    {
        "description": "Standard: target=8",
        "run": lambda: sorted(solution([10, 1, 2, 7, 6, 1, 5], 8) or []),
        "expected": sorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
    },
    {
        "description": "Duplicates: target=5",
        "run": lambda: sorted(solution([2, 5, 2, 1, 2], 5) or []),
        "expected": sorted([[1, 2, 2], [5]]),
    },
    {
        "description": "No solution: target=100",
        "run": lambda: solution([1, 2], 100),
        "expected": [],
    },
    {
        "description": "Single match: target=1",
        "run": lambda: solution([1], 1),
        "expected": [[1]],
    },
]
