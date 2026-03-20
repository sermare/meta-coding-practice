from problems.p248_sqrtx import solution

TEST_CASES = [
    {
        "description": "Perfect square: 4",
        "run": lambda: solution(4),
        "expected": 2,
    },
    {
        "description": "Non-perfect: 8",
        "run": lambda: solution(8),
        "expected": 2,
    },
    {
        "description": "Zero: 0",
        "run": lambda: solution(0),
        "expected": 0,
    },
    {
        "description": "One: 1",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "Large: 2147395599",
        "run": lambda: solution(2147395599),
        "expected": 46339,
    },
]
