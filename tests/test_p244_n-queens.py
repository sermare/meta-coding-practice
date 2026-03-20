from problems.p244_n-queens import solution

TEST_CASES = [
    {
        "description": "n=4: two solutions",
        "run": lambda: len(solution(4) or []),
        "expected": 2,
    },
    {
        "description": "n=1: one solution",
        "run": lambda: solution(1),
        "expected": [["Q"]],
    },
    {
        "description": "n=2: no solution",
        "run": lambda: solution(2),
        "expected": [],
    },
    {
        "description": "n=3: no solution",
        "run": lambda: solution(3),
        "expected": [],
    },
    {
        "description": "n=5: ten solutions",
        "run": lambda: len(solution(5) or []),
        "expected": 10,
    },
]
