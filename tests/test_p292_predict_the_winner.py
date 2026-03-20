from problems.p292_predict_the_winner import solution

TEST_CASES = [
    {
        "description": "[1,5,2] -> False",
        "run": lambda: solution([1, 5, 2]),
        "expected": False,
    },
    {
        "description": "[1,5,233,7] -> True",
        "run": lambda: solution([1, 5, 233, 7]),
        "expected": True,
    },
    {
        "description": "[1] -> True",
        "run": lambda: solution([1]),
        "expected": True,
    },
    {
        "description": "[1,1] -> True (tie, P1 wins)",
        "run": lambda: solution([1, 1]),
        "expected": True,
    },
    {
        "description": "[2,4,55,6,8] -> False",
        "run": lambda: solution([2, 4, 55, 6, 8]),
        "expected": False,
    },
]
