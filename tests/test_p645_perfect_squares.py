from problems.p645_perfect_squares import solution

TEST_CASES = [
    {
        "description": "12 = 4+4+4",
        "run": lambda: solution(12),
        "expected": 3,
    },
    {
        "description": "13 = 4+9",
        "run": lambda: solution(13),
        "expected": 2,
    },
    {
        "description": "Perfect square: 16",
        "run": lambda: solution(16),
        "expected": 1,
    },
    {
        "description": "Small number: 1",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "Needs 4 squares: 7",
        "run": lambda: solution(7),
        "expected": 4,
    },
]
