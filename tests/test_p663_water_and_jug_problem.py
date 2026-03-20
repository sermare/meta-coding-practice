from problems.p663_water_and_jug_problem import solution

TEST_CASES = [
    {
        "description": "Classic 3 and 5 jug, target 4",
        "run": lambda: solution(3, 5, 4),
        "expected": True,
    },
    {
        "description": "Impossible: 2 and 6, target 5",
        "run": lambda: solution(2, 6, 5),
        "expected": False,
    },
    {
        "description": "Target is zero",
        "run": lambda: solution(1, 2, 0),
        "expected": True,
    },
    {
        "description": "Target equals one jug",
        "run": lambda: solution(3, 5, 5),
        "expected": True,
    },
    {
        "description": "Target larger than both jugs combined",
        "run": lambda: solution(3, 5, 9),
        "expected": False,
    },
]
