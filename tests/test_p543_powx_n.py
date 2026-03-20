from problems.p543_powx_n import solution

TEST_CASES = [
    {
        "description": "Positive power",
        "run": lambda: solution(2.0, 10),
        "expected": 1024.0,
    },
    {
        "description": "Negative power",
        "run": lambda: solution(2.0, -2),
        "expected": 0.25,
    },
    {
        "description": "Zero power",
        "run": lambda: solution(5.0, 0),
        "expected": 1.0,
    },
    {
        "description": "Power of 1",
        "run": lambda: solution(3.0, 1),
        "expected": 3.0,
    },
    {
        "description": "Fractional base",
        "run": lambda: solution(0.5, 2),
        "expected": 0.25,
    },
]
