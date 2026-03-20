from problems.p535_counting_bits import solution

TEST_CASES = [
    {
        "description": "n=5",
        "run": lambda: solution(5),
        "expected": [0, 1, 1, 2, 1, 2],
    },
    {
        "description": "n=2",
        "run": lambda: solution(2),
        "expected": [0, 1, 1],
    },
    {
        "description": "n=0",
        "run": lambda: solution(0),
        "expected": [0],
    },
    {
        "description": "n=1",
        "run": lambda: solution(1),
        "expected": [0, 1],
    },
    {
        "description": "n=8",
        "run": lambda: solution(8),
        "expected": [0, 1, 1, 2, 1, 2, 2, 3, 1],
    },
]
