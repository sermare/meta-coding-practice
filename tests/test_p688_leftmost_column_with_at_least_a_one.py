from problems.p688_leftmost_column_with_at_least_a_one import solution

TEST_CASES = [
    {
        "description": "Basic: [[0,0],[1,1]]",
        "run": lambda: solution([[0, 0], [1, 1]]),
        "expected": 0,
    },
    {
        "description": "All zeros",
        "run": lambda: solution([[0, 0], [0, 0]]),
        "expected": -1,
    },
    {
        "description": "Last column only",
        "run": lambda: solution([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 1]]),
        "expected": 3,
    },
    {
        "description": "All ones",
        "run": lambda: solution([[1, 1], [1, 1]]),
        "expected": 0,
    },
]
