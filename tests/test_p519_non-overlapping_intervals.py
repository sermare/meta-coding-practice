from problems.p519_non-overlapping_intervals import solution

TEST_CASES = [
    {
        "description": "Remove one",
        "run": lambda: solution([[1,2],[2,3],[3,4],[1,3]]),
        "expected": 1,
    },
    {
        "description": "Remove two",
        "run": lambda: solution([[1,2],[1,2],[1,2]]),
        "expected": 2,
    },
    {
        "description": "No removal needed",
        "run": lambda: solution([[1,2],[2,3]]),
        "expected": 0,
    },
    {
        "description": "Single interval",
        "run": lambda: solution([[1,5]]),
        "expected": 0,
    },
    {
        "description": "All overlap",
        "run": lambda: solution([[1,4],[2,3],[3,5]]),
        "expected": 1,
    },
]
