from problems.p376_rotting_oranges import solution


TEST_CASES = [
    {
        "description": "All rot in 4 minutes",
        "run": lambda: solution([[2, 1, 1], [1, 1, 0], [0, 1, 1]]),
        "expected": 4,
    },
    {
        "description": "Impossible to rot all",
        "run": lambda: solution([[2, 1, 1], [0, 1, 1], [1, 0, 1]]),
        "expected": -1,
    },
    {
        "description": "No fresh oranges",
        "run": lambda: solution([[0, 2]]),
        "expected": 0,
    },
    {
        "description": "Already all rotten",
        "run": lambda: solution([[2, 2], [2, 2]]),
        "expected": 0,
    },
    {
        "description": "Single fresh, no rotten: impossible",
        "run": lambda: solution([[1]]),
        "expected": -1,
    },
]
