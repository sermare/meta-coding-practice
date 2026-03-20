from problems.p685_power_of_two import solution

TEST_CASES = [
    {
        "description": "Power of two: 16",
        "run": lambda: solution(16),
        "expected": True,
    },
    {
        "description": "Not power of two: 3",
        "run": lambda: solution(3),
        "expected": False,
    },
    {
        "description": "Power of two: 1",
        "run": lambda: solution(1),
        "expected": True,
    },
    {
        "description": "Zero is not power of two",
        "run": lambda: solution(0),
        "expected": False,
    },
    {
        "description": "Negative number",
        "run": lambda: solution(-4),
        "expected": False,
    },
]
