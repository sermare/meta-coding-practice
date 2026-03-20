from problems.p671_sliding_puzzle import solution

TEST_CASES = [
    {
        "description": "One move to solve",
        "run": lambda: solution([[1, 2, 3], [4, 0, 5]]),
        "expected": 1,
    },
    {
        "description": "Already solved",
        "run": lambda: solution([[1, 2, 3], [4, 5, 0]]),
        "expected": 0,
    },
    {
        "description": "Five moves",
        "run": lambda: solution([[4, 1, 2], [5, 0, 3]]),
        "expected": 5,
    },
    {
        "description": "Unsolvable puzzle",
        "run": lambda: solution([[1, 2, 3], [5, 4, 0]]),
        "expected": -1,
    },
]
