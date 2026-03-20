from problems.p434_permutations_ii import solution

TEST_CASES = [
    {
        "description": "With duplicates: [1,1,2]",
        "run": lambda: sorted(solution([1, 1, 2])),
        "expected": sorted([[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
    },
    {
        "description": "All same: [1,1,1]",
        "run": lambda: solution([1, 1, 1]),
        "expected": [[1, 1, 1]],
    },
    {
        "description": "No duplicates: [1,2,3]",
        "run": lambda: len(solution([1, 2, 3])),
        "expected": 6,
    },
    {
        "description": "Two elements: [1,1]",
        "run": lambda: solution([1, 1]),
        "expected": [[1, 1]],
    },
    {
        "description": "Single element: [0]",
        "run": lambda: solution([0]),
        "expected": [[0]],
    },
]
