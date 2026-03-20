from problems.p141_container_with_most_water import solution

TEST_CASES = [
    {
        "description": "Standard example",
        "run": lambda: solution([1, 8, 6, 2, 5, 4, 8, 3, 7]),
        "expected": 49,
    },
    {
        "description": "Two elements",
        "run": lambda: solution([1, 1]),
        "expected": 1,
    },
    {
        "description": "Increasing heights",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": 6,
    },
    {
        "description": "All same height",
        "run": lambda: solution([3, 3, 3, 3]),
        "expected": 9,
    },
    {
        "description": "Tall ends",
        "run": lambda: solution([10, 1, 1, 1, 10]),
        "expected": 40,
    },
]
