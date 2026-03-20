from problems.p160_power_of_two import solution

TEST_CASES = [
    {
        "description": "1 is 2^0",
        "run": lambda: solution(1),
        "expected": True,
    },
    {
        "description": "16 is 2^4",
        "run": lambda: solution(16),
        "expected": True,
    },
    {
        "description": "3 is not power of 2",
        "run": lambda: solution(3),
        "expected": False,
    },
    {
        "description": "0 is not power of 2",
        "run": lambda: solution(0),
        "expected": False,
    },
    {
        "description": "Negative not power of 2",
        "run": lambda: solution(-16),
        "expected": False,
    },
]
