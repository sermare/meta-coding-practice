from problems.p165_sum_of_two_integers import solution

TEST_CASES = [
    {
        "description": "1 + 2 = 3",
        "run": lambda: solution(1, 2),
        "expected": 3,
    },
    {
        "description": "2 + 3 = 5",
        "run": lambda: solution(2, 3),
        "expected": 5,
    },
    {
        "description": "Negative: -1 + 1 = 0",
        "run": lambda: solution(-1, 1),
        "expected": 0,
    },
    {
        "description": "Both negative: -2 + -3 = -5",
        "run": lambda: solution(-2, -3),
        "expected": -5,
    },
]
