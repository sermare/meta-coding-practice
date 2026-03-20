from problems.p061_permutations import solution

TEST_CASES = [
    {
        "description": "Three elements: [1,2,3]",
        "run": lambda: sorted(solution([1, 2, 3])),
        "expected": sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    },
    {
        "description": "Two elements: [0,1]",
        "run": lambda: sorted(solution([0, 1])),
        "expected": sorted([[0, 1], [1, 0]]),
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": [[1]],
    },
    {
        "description": "Count for 4 elements",
        "run": lambda: len(solution([1, 2, 3, 4])),
        "expected": 24,
    },
]
