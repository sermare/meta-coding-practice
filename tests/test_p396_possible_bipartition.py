from problems.p396_possible_bipartition import solution


TEST_CASES = [
    {
        "description": "Possible bipartition",
        "run": lambda: solution(4, [[1, 2], [1, 3], [2, 4]]),
        "expected": True,
    },
    {
        "description": "Odd cycle: impossible",
        "run": lambda: solution(3, [[1, 2], [1, 3], [2, 3]]),
        "expected": False,
    },
    {
        "description": "Odd cycle of 5: impossible",
        "run": lambda: solution(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]),
        "expected": False,
    },
    {
        "description": "No dislikes",
        "run": lambda: solution(5, []),
        "expected": True,
    },
]
