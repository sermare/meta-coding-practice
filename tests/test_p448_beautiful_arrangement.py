from problems.p448_beautiful_arrangement import solution

TEST_CASES = [
    {
        "description": "n=2",
        "run": lambda: solution(2),
        "expected": 2,
    },
    {
        "description": "n=1",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "n=3",
        "run": lambda: solution(3),
        "expected": 3,
    },
    {
        "description": "n=4",
        "run": lambda: solution(4),
        "expected": 8,
    },
    {
        "description": "n=5",
        "run": lambda: solution(5),
        "expected": 10,
    },
]
