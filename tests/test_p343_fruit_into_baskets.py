from problems.p343_fruit_into_baskets import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2,1] -> 3",
        "run": lambda: solution([1, 2, 1]),
        "expected": 3,
    },
    {
        "description": "Three types: [0,1,2,2] -> 3",
        "run": lambda: solution([0, 1, 2, 2]),
        "expected": 3,
    },
    {
        "description": "Many types: [1,2,3,2,2] -> 4",
        "run": lambda: solution([1, 2, 3, 2, 2]),
        "expected": 4,
    },
    {
        "description": "Single type: [1,1,1,1] -> 4",
        "run": lambda: solution([1, 1, 1, 1]),
        "expected": 4,
    },
]
