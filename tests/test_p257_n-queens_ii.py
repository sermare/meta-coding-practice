from problems.p257_n-queens_ii import solution

TEST_CASES = [
    {
        "description": "n=1 -> 1",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "n=4 -> 2",
        "run": lambda: solution(4),
        "expected": 2,
    },
    {
        "description": "n=5 -> 10",
        "run": lambda: solution(5),
        "expected": 10,
    },
    {
        "description": "n=8 -> 92",
        "run": lambda: solution(8),
        "expected": 92,
    },
    {
        "description": "n=2 -> 0",
        "run": lambda: solution(2),
        "expected": 0,
    },
]
