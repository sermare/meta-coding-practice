from problems.p431_combination_sum import solution

TEST_CASES = [
    {
        "description": "Basic: candidates=[2,3,6,7] target=7",
        "run": lambda: sorted([sorted(x) for x in solution([2, 3, 6, 7], 7)]),
        "expected": [[2, 2, 3], [7]],
    },
    {
        "description": "Multiple combos: candidates=[2,3,5] target=8",
        "run": lambda: sorted([sorted(x) for x in solution([2, 3, 5], 8)]),
        "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
    },
    {
        "description": "No solution: candidates=[2] target=1",
        "run": lambda: solution([2], 1),
        "expected": [],
    },
    {
        "description": "Single candidate: candidates=[1] target=2",
        "run": lambda: solution([1], 2),
        "expected": [[1, 1]],
    },
    {
        "description": "Target is candidate: candidates=[3,5,8] target=8",
        "run": lambda: sorted([sorted(x) for x in solution([3, 5, 8], 8)]),
        "expected": [[3, 5], [8]],
    },
]
