from problems.p432_combination_sum_ii import solution

TEST_CASES = [
    {
        "description": "Basic: candidates=[10,1,2,7,6,1,5] target=8",
        "run": lambda: sorted([sorted(x) for x in solution([10, 1, 2, 7, 6, 1, 5], 8)]),
        "expected": [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
    },
    {
        "description": "Duplicates: candidates=[2,5,2,1,2] target=5",
        "run": lambda: sorted([sorted(x) for x in solution([2, 5, 2, 1, 2], 5)]),
        "expected": [[1, 2, 2], [5]],
    },
    {
        "description": "No solution: candidates=[3,5] target=2",
        "run": lambda: solution([3, 5], 2),
        "expected": [],
    },
    {
        "description": "Single element: candidates=[1] target=1",
        "run": lambda: solution([1], 1),
        "expected": [[1]],
    },
    {
        "description": "All same: candidates=[1,1,1] target=2",
        "run": lambda: solution([1, 1, 1], 2),
        "expected": [[1, 1]],
    },
]
