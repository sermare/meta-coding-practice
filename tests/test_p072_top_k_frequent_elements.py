from problems.p072_top_k_frequent_elements import solution

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
        "description": "All same frequency: [1,2,3] k=3",
        "run": lambda: sorted(solution([1, 2, 3], 3)),
        "expected": [1, 2, 3],
    },
    {
        "description": "Top 1: [5,5,5,1,1,2,2] k=1",
        "run": lambda: solution([5, 5, 5, 1, 1, 2, 2], 1),
        "expected": [5],
    },
]
