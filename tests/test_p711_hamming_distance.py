from problems.p711_hamming_distance import solution

TEST_CASES = [
    {
        "description": "Basic case: x=1, y=4",
        "run": lambda: solution(1, 4),
        "expected": 2,
    },
    {
        "description": "Same numbers: x=3, y=3",
        "run": lambda: solution(3, 3),
        "expected": 0,
    },
    {
        "description": "Zero and number: x=0, y=7",
        "run": lambda: solution(0, 7),
        "expected": 3,
    },
    {
        "description": "Adjacent: x=1, y=2",
        "run": lambda: solution(1, 2),
        "expected": 2,
    },
    {
        "description": "Large values: x=93, y=73",
        "run": lambda: solution(93, 73),
        "expected": 2,
    },
]
