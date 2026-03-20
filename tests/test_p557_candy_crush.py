from problems.p557_candy_crush import solution

TEST_CASES = [
    {
        "description": "Simple horizontal crush",
        "run": lambda: solution([[1, 1, 1], [2, 3, 4]]),
        "expected": [[0, 0, 0], [2, 3, 4]],
    },
    {
        "description": "No crush needed",
        "run": lambda: solution([[1, 2, 3], [4, 5, 6]]),
        "expected": [[1, 2, 3], [4, 5, 6]],
    },
    {
        "description": "Vertical crush",
        "run": lambda: solution([[1, 2], [1, 3], [1, 4]]),
        "expected": [[0, 2], [0, 3], [0, 4]],
    },
    {
        "description": "All zeros board",
        "run": lambda: solution([[0, 0], [0, 0]]),
        "expected": [[0, 0], [0, 0]],
    },
]
