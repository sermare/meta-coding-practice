from problems.p271_water_and_jug_problem import solution

TEST_CASES = [
    {
        "description": "3,5,4 -> True",
        "run": lambda: solution(3, 5, 4),
        "expected": True,
    },
    {
        "description": "2,6,5 -> False",
        "run": lambda: solution(2, 6, 5),
        "expected": False,
    },
    {
        "description": "1,2,3 -> True (fill both)",
        "run": lambda: solution(1, 2, 3),
        "expected": True,
    },
    {
        "description": "0,0,0 -> True",
        "run": lambda: solution(0, 0, 0),
        "expected": True,
    },
    {
        "description": "1,1,2 -> True",
        "run": lambda: solution(1, 1, 2),
        "expected": True,
    },
]
