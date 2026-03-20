from problems.p163_ugly_number import solution

TEST_CASES = [
    {
        "description": "6 is ugly (2*3)",
        "run": lambda: solution(6),
        "expected": True,
    },
    {
        "description": "1 is ugly",
        "run": lambda: solution(1),
        "expected": True,
    },
    {
        "description": "14 is not ugly (has factor 7)",
        "run": lambda: solution(14),
        "expected": False,
    },
    {
        "description": "0 is not ugly",
        "run": lambda: solution(0),
        "expected": False,
    },
    {
        "description": "30 is ugly (2*3*5)",
        "run": lambda: solution(30),
        "expected": True,
    },
]
