from problems.p060_combination_sum import solution

TEST_CASES = [
    {
        "description": "Basic: [2,3,6,7] target=7",
        "run": lambda: sorted([sorted(x) for x in solution([2, 3, 6, 7], 7)]),
        "expected": sorted([[2, 2, 3], [7]]),
    },
    {
        "description": "Multiple combos: [2,3,5] target=8",
        "run": lambda: sorted([sorted(x) for x in solution([2, 3, 5], 8)]),
        "expected": sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    },
    {
        "description": "No solution: [2] target=1",
        "run": lambda: solution([2], 1),
        "expected": [],
    },
    {
        "description": "Single candidate: [3] target=9",
        "run": lambda: solution([3], 9),
        "expected": [[3, 3, 3]],
    },
]
