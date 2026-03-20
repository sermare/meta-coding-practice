from problems.p536_reverse_bits import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution(43261596),
        "expected": 964176192,
    },
    {
        "description": "All ones",
        "run": lambda: solution(4294967293),
        "expected": 3221225471,
    },
    {
        "description": "Zero",
        "run": lambda: solution(0),
        "expected": 0,
    },
    {
        "description": "One",
        "run": lambda: solution(1),
        "expected": 2147483648,
    },
    {
        "description": "Power of 2",
        "run": lambda: solution(4),
        "expected": 536870912,
    },
]
