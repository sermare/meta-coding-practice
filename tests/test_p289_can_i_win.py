from problems.p289_can_i_win import solution

TEST_CASES = [
    {
        "description": "max=10, total=11 -> False",
        "run": lambda: solution(10, 11),
        "expected": False,
    },
    {
        "description": "max=10, total=0 -> True",
        "run": lambda: solution(10, 0),
        "expected": True,
    },
    {
        "description": "max=10, total=1 -> True",
        "run": lambda: solution(10, 1),
        "expected": True,
    },
    {
        "description": "max=4, total=6 -> True",
        "run": lambda: solution(4, 6),
        "expected": True,
    },
    {
        "description": "max=20, total=210 -> False (sum too large)",
        "run": lambda: solution(20, 211),
        "expected": False,
    },
]
