from problems.p592_top_k_frequent_elements import solution

TEST_CASES = [
    {
        "description": "Top 2: [1,1,1,2,2,3] k=2",
        "run": lambda: sorted(solution([1, 1, 1, 2, 2, 3], 2)),
        "expected": [1, 2],
    },
    {
        "description": "Single element: [1] k=1",
        "run": lambda: solution([1], 1),
        "expected": [1],
    },
    {
        "description": "Top 2 from mixed",
        "run": lambda: sorted(solution([4, 4, 4, 1, 1, 2, 2, 2, 3], 2)),
        "expected": [2, 4],
    },
    {
        "description": "All same frequency k=2",
        "run": lambda: sorted(solution([1, 2, 3], 2)),
        "expected": sorted(solution([1, 2, 3], 2)),
    },
]
