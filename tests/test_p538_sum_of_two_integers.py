from problems.p538_sum_of_two_integers import solution

TEST_CASES = [
    {
        "description": "Positive sum",
        "run": lambda: solution(1, 2),
        "expected": 3,
    },
    {
        "description": "Negative sum",
        "run": lambda: solution(-1, 1),
        "expected": 0,
    },
    {
        "description": "Both negative",
        "run": lambda: solution(-2, -3),
        "expected": -5,
    },
    {
        "description": "Zero and num",
        "run": lambda: solution(0, 5),
        "expected": 5,
    },
    {
        "description": "Large numbers",
        "run": lambda: solution(100, 200),
        "expected": 300,
    },
]
