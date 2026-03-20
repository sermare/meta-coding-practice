from problems.p596_min_stack import solution

TEST_CASES = [
    {
        "description": "Standard operations",
        "run": lambda: solution(
            ["push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[-2], [0], [-3], [], [], [], []]
        ),
        "expected": [None, None, None, -3, None, 0, -2],
    },
    {
        "description": "Single element",
        "run": lambda: solution(
            ["push", "top", "getMin"],
            [[5], [], []]
        ),
        "expected": [None, 5, 5],
    },
    {
        "description": "Ascending push",
        "run": lambda: solution(
            ["push", "push", "push", "getMin"],
            [[1], [2], [3], []]
        ),
        "expected": [None, None, None, 1],
    },
    {
        "description": "Descending push then pop",
        "run": lambda: solution(
            ["push", "push", "push", "getMin", "pop", "getMin"],
            [[3], [2], [1], [], [], []]
        ),
        "expected": [None, None, None, 1, None, 2],
    },
]
