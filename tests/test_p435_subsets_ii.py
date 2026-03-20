from problems.p435_subsets_ii import solution

TEST_CASES = [
    {
        "description": "With duplicates: [1,2,2]",
        "run": lambda: sorted([sorted(x) for x in solution([1, 2, 2])]),
        "expected": sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
    },
    {
        "description": "Single element: [0]",
        "run": lambda: sorted([sorted(x) for x in solution([0])]),
        "expected": [[], [0]],
    },
    {
        "description": "All same: [1,1]",
        "run": lambda: sorted([sorted(x) for x in solution([1, 1])]),
        "expected": [[], [1], [1, 1]],
    },
    {
        "description": "No duplicates: [1,2]",
        "run": lambda: sorted([sorted(x) for x in solution([1, 2])]),
        "expected": sorted([[], [1], [2], [1, 2]]),
    },
    {
        "description": "Count for [4,4,4,1,4]",
        "run": lambda: len(solution([4, 4, 4, 1, 4])),
        "expected": 10,
    },
]
