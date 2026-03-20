from problems.p277_integer_break import solution

TEST_CASES = [
    {
        "description": "n=2 -> 1",
        "run": lambda: solution(2),
        "expected": 1,
    },
    {
        "description": "n=10 -> 36",
        "run": lambda: solution(10),
        "expected": 36,
    },
    {
        "description": "n=3 -> 2",
        "run": lambda: solution(3),
        "expected": 2,
    },
    {
        "description": "n=4 -> 4",
        "run": lambda: solution(4),
        "expected": 4,
    },
    {
        "description": "n=8 -> 18",
        "run": lambda: solution(8),
        "expected": 18,
    },
]
