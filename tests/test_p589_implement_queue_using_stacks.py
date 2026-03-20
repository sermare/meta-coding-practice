from problems.p589_implement_queue_using_stacks import solution

TEST_CASES = [
    {
        "description": "Basic push/peek/pop/empty",
        "run": lambda: solution(
            ["push", "push", "peek", "pop", "empty"],
            [[1], [2], [], [], []]
        ),
        "expected": [None, None, 1, 1, False],
    },
    {
        "description": "Single element",
        "run": lambda: solution(
            ["push", "pop", "empty"],
            [[5], [], []]
        ),
        "expected": [None, 5, True],
    },
    {
        "description": "Multiple pushes then pops",
        "run": lambda: solution(
            ["push", "push", "push", "pop", "pop", "pop"],
            [[1], [2], [3], [], [], []]
        ),
        "expected": [None, None, None, 1, 2, 3],
    },
    {
        "description": "Interleaved push/pop",
        "run": lambda: solution(
            ["push", "pop", "push", "peek"],
            [[1], [], [2], []]
        ),
        "expected": [None, 1, None, 2],
    },
]
