from problems.p085_rotting_oranges import solution

TEST_CASES = [
    {
        "description": "Standard: 4 minutes",
        "run": lambda: solution([[2, 1, 1], [1, 1, 0], [0, 1, 1]]),
        "expected": 4,
    },
    {
        "description": "Impossible: isolated fresh orange",
        "run": lambda: solution([[2, 1, 1], [0, 1, 1], [1, 0, 1]]),
        "expected": -1,
    },
    {
        "description": "No fresh oranges: [0,2]",
        "run": lambda: solution([[0, 2]]),
        "expected": 0,
    },
    {
        "description": "All fresh, no rotten: [[1]]",
        "run": lambda: solution([[1]]),
        "expected": -1,
    },
]
