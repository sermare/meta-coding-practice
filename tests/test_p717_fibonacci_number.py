from problems.p717_fibonacci_number import solution

TEST_CASES = [
    {
        "description": "F(0) = 0",
        "run": lambda: solution(0),
        "expected": 0,
    },
    {
        "description": "F(1) = 1",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "F(4) = 3",
        "run": lambda: solution(4),
        "expected": 3,
    },
    {
        "description": "F(10) = 55",
        "run": lambda: solution(10),
        "expected": 55,
    },
    {
        "description": "F(20) = 6765",
        "run": lambda: solution(20),
        "expected": 6765,
    },
]
