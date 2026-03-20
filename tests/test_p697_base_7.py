from problems.p697_base_7 import solution

TEST_CASES = [
    {
        "description": "Positive: 100 -> 202",
        "run": lambda: solution(100),
        "expected": "202",
    },
    {
        "description": "Negative: -7 -> -10",
        "run": lambda: solution(-7),
        "expected": "-10",
    },
    {
        "description": "Zero",
        "run": lambda: solution(0),
        "expected": "0",
    },
    {
        "description": "Small: 7 -> 10",
        "run": lambda: solution(7),
        "expected": "10",
    },
    {
        "description": "One: 1 -> 1",
        "run": lambda: solution(1),
        "expected": "1",
    },
]
