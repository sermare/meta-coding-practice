from problems.p159_contains_duplicate import solution

TEST_CASES = [
    {
        "description": "Has duplicate",
        "run": lambda: solution([1, 2, 3, 1]),
        "expected": True,
    },
    {
        "description": "No duplicates",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": False,
    },
    {
        "description": "Multiple duplicates",
        "run": lambda: solution([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]),
        "expected": True,
    },
    {
        "description": "Single element",
        "run": lambda: solution([1]),
        "expected": False,
    },
]
