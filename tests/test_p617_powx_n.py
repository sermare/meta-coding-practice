from problems.p617_powx_n import solution

TEST_CASES = [
    {
        "description": "2^10 = 1024",
        "run": lambda: solution(2.0, 10),
        "expected": 1024.0,
    },
    {
        "description": "2.1^3 = 9.261",
        "run": lambda: round(solution(2.1, 3), 5),
        "expected": 9.261,
    },
    {
        "description": "2^-2 = 0.25",
        "run": lambda: solution(2.0, -2),
        "expected": 0.25,
    },
    {
        "description": "Any number to power 0",
        "run": lambda: solution(5.0, 0),
        "expected": 1.0,
    },
    {
        "description": "1 to any power",
        "run": lambda: solution(1.0, 100),
        "expected": 1.0,
    },
]
