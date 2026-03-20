from problems.p185_fraction_to_recurring_decimal import solution

TEST_CASES = [
    {
        "description": "1/2 = 0.5",
        "run": lambda: solution(1, 2),
        "expected": "0.5",
    },
    {
        "description": "2/1 = 2",
        "run": lambda: solution(2, 1),
        "expected": "2",
    },
    {
        "description": "4/333 = 0.(012)",
        "run": lambda: solution(4, 333),
        "expected": "0.(012)",
    },
    {
        "description": "1/3 = 0.(3)",
        "run": lambda: solution(1, 3),
        "expected": "0.(3)",
    },
]
