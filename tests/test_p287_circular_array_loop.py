from problems.p287_circular_array_loop import solution

TEST_CASES = [
    {
        "description": "[2,-1,1,2,2] -> True",
        "run": lambda: solution([2, -1, 1, 2, 2]),
        "expected": True,
    },
    {
        "description": "[-1,2] -> False",
        "run": lambda: solution([-1, 2]),
        "expected": False,
    },
    {
        "description": "[-2,1,-1,-2,-2] -> False",
        "run": lambda: solution([-2, 1, -1, -2, -2]),
        "expected": False,
    },
    {
        "description": "[1,1,1,1,1] -> True",
        "run": lambda: solution([1, 1, 1, 1, 1]),
        "expected": True,
    },
    {
        "description": "[-1,-1,-1] -> True",
        "run": lambda: solution([-1, -1, -1]),
        "expected": True,
    },
]
