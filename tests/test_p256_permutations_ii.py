from problems.p256_permutations_ii import solution

TEST_CASES = [
    {
        "description": "[1,1,2] -> 3 unique permutations",
        "run": lambda: sorted(solution([1, 1, 2])),
        "expected": sorted([[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
    },
    {
        "description": "[1,2,3] -> 6 permutations (no dups)",
        "run": lambda: len(solution([1, 2, 3])),
        "expected": 6,
    },
    {
        "description": "[1] -> [[1]]",
        "run": lambda: solution([1]),
        "expected": [[1]],
    },
    {
        "description": "[1,1,1] -> [[1,1,1]]",
        "run": lambda: solution([1, 1, 1]),
        "expected": [[1, 1, 1]],
    },
    {
        "description": "[1,1,2,2] -> 6 unique permutations",
        "run": lambda: len(solution([1, 1, 2, 2])),
        "expected": 6,
    },
]
