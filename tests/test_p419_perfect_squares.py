from problems.p419_perfect_squares import solution

TEST_CASES = [
    {
        "description": "n=12",
        "run": lambda: solution(12),
        "expected": 3,
    },
    {
        "description": "Perfect square n=16",
        "run": lambda: solution(16),
        "expected": 1,
    },
    {
        "description": "n=13",
        "run": lambda: solution(13),
        "expected": 2,
    },
    {
        "description": "n=1",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "n=7",
        "run": lambda: solution(7),
        "expected": 4,
    },
]
