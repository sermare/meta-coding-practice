from problems.p531_candy import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution([1,0,2]),
        "expected": 5,
    },
    {
        "description": "Equal ratings",
        "run": lambda: solution([1,2,2]),
        "expected": 4,
    },
    {
        "description": "Decreasing",
        "run": lambda: solution([3,2,1]),
        "expected": 6,
    },
    {
        "description": "Increasing",
        "run": lambda: solution([1,2,3]),
        "expected": 6,
    },
    {
        "description": "Single child",
        "run": lambda: solution([5]),
        "expected": 1,
    },
]
