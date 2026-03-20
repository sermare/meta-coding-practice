from problems.p231_monotone_increasing_digits import solution

TEST_CASES = [
    {
        "description": "Needs adjustment: 10",
        "run": lambda: solution(10),
        "expected": 9,
    },
    {
        "description": "Already monotone: 1234",
        "run": lambda: solution(1234),
        "expected": 1234,
    },
    {
        "description": "Needs adjustment: 332",
        "run": lambda: solution(332),
        "expected": 299,
    },
    {
        "description": "Single digit: 5",
        "run": lambda: solution(5),
        "expected": 5,
    },
    {
        "description": "Large: 668841",
        "run": lambda: solution(668841),
        "expected": 667999,
    },
]
