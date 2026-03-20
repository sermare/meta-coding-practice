from problems.p148_first_missing_positive import solution

TEST_CASES = [
    {
        "description": "Missing 3",
        "run": lambda: solution([1, 2, 0]),
        "expected": 3,
    },
    {
        "description": "Missing 2",
        "run": lambda: solution([3, 4, -1, 1]),
        "expected": 2,
    },
    {
        "description": "Missing 1",
        "run": lambda: solution([7, 8, 9, 11, 12]),
        "expected": 1,
    },
    {
        "description": "Consecutive from 1",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": 6,
    },
    {
        "description": "Single element 1",
        "run": lambda: solution([1]),
        "expected": 2,
    },
]
