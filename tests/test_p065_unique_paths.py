from problems.p065_unique_paths import solution

TEST_CASES = [
    {
        "description": "3x7 grid",
        "run": lambda: solution(3, 7),
        "expected": 28,
    },
    {
        "description": "3x2 grid",
        "run": lambda: solution(3, 2),
        "expected": 3,
    },
    {
        "description": "1x1 grid",
        "run": lambda: solution(1, 1),
        "expected": 1,
    },
    {
        "description": "2x2 grid",
        "run": lambda: solution(2, 2),
        "expected": 2,
    },
    {
        "description": "3x3 grid",
        "run": lambda: solution(3, 3),
        "expected": 6,
    },
]
