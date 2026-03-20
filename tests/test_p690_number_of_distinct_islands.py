from problems.p690_number_of_distinct_islands import solution

TEST_CASES = [
    {
        "description": "Two same-shape islands",
        "run": lambda: solution([
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
        ]),
        "expected": 1,
    },
    {
        "description": "Two different-shape islands",
        "run": lambda: solution([
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1],
        ]),
        "expected": 3,
    },
    {
        "description": "No islands",
        "run": lambda: solution([[0, 0], [0, 0]]),
        "expected": 0,
    },
    {
        "description": "Single cell islands",
        "run": lambda: solution([[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        "expected": 1,
    },
]
