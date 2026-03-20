from problems.p097_min_stack import solution

TEST_CASES = [
    {
        "description": "Standard operations",
        "run": lambda: solution(
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []]
        ),
        "expected": [None, None, None, None, -3, None, 0, -2],
    },
    {
        "description": "Push and getMin",
        "run": lambda: solution(
            ["MinStack", "push", "push", "getMin"],
            [[], [1], [2], []]
        ),
        "expected": [None, None, None, 1],
    },
    {
        "description": "Pop then getMin",
        "run": lambda: solution(
            ["MinStack", "push", "push", "pop", "getMin"],
            [[], [3], [1], [], []]
        ),
        "expected": [None, None, None, None, 3],
    },
    {
        "description": "Single element operations",
        "run": lambda: solution(
            ["MinStack", "push", "top", "getMin"],
            [[], [42], [], []]
        ),
        "expected": [None, None, 42, 42],
    },
]
