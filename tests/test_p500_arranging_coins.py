from problems.p500_arranging_coins import solution

TEST_CASES = [
    {
        "description": "n=5 -> 2",
        "run": lambda: solution(5),
        "expected": 2,
    },
    {
        "description": "n=8 -> 3",
        "run": lambda: solution(8),
        "expected": 3,
    },
    {
        "description": "n=1 -> 1",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "Exact: n=6 -> 3",
        "run": lambda: solution(6),
        "expected": 3,
    },
    {
        "description": "Large: n=100 -> 13",
        "run": lambda: solution(100),
        "expected": 13,
    },
]
