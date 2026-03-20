from problems.p331_grumpy_bookstore_owner import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3),
        "expected": 16,
    },
    {
        "description": "Never grumpy",
        "run": lambda: solution([1, 2, 3], [0, 0, 0], 1),
        "expected": 6,
    },
    {
        "description": "Always grumpy",
        "run": lambda: solution([1, 2, 3], [1, 1, 1], 3),
        "expected": 6,
    },
    {
        "description": "Single minute",
        "run": lambda: solution([10], [1], 1),
        "expected": 10,
    },
]
