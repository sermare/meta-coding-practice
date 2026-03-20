from problems.p493_first_bad_version import solution

TEST_CASES = [
    {
        "description": "n=5 bad=4 -> 4",
        "run": lambda: solution(5, lambda v: v >= 4),
        "expected": 4,
    },
    {
        "description": "n=1 bad=1 -> 1",
        "run": lambda: solution(1, lambda v: v >= 1),
        "expected": 1,
    },
    {
        "description": "n=10 bad=1 -> 1",
        "run": lambda: solution(10, lambda v: v >= 1),
        "expected": 1,
    },
    {
        "description": "n=10 bad=10 -> 10",
        "run": lambda: solution(10, lambda v: v >= 10),
        "expected": 10,
    },
    {
        "description": "n=100 bad=50 -> 50",
        "run": lambda: solution(100, lambda v: v >= 50),
        "expected": 50,
    },
]
