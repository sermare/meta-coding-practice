from problems.p282_arranging_coins import solution

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
        "description": "n=3 -> 2",
        "run": lambda: solution(3),
        "expected": 2,
    },
    {
        "description": "n=10 -> 4",
        "run": lambda: solution(10),
        "expected": 4,
    },
]
