from problems.p200_power_of_three import solution

TEST_CASES = [
    {
        "description": "27 is 3^3",
        "run": lambda: solution(27),
        "expected": True,
    },
    {
        "description": "0 is not power of 3",
        "run": lambda: solution(0),
        "expected": False,
    },
    {
        "description": "9 is 3^2",
        "run": lambda: solution(9),
        "expected": True,
    },
    {
        "description": "1 is 3^0",
        "run": lambda: solution(1),
        "expected": True,
    },
    {
        "description": "-1 is not power of 3",
        "run": lambda: solution(-1),
        "expected": False,
    },
]
