from problems.p612_max_stack import solution

TEST_CASES = [
    {
        "description": "Basic operations",
        "run": lambda: solution(
            ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"],
            [[], [5], [1], [5], [], [], [], [], [], []]
        ),
        "expected": [None, None, None, None, 5, 5, 1, 5, 1, 5],
    },
    {
        "description": "Single element push and pop",
        "run": lambda: solution(
            ["MaxStack", "push", "top", "pop"],
            [[], [3], [], []]
        ),
        "expected": [None, None, 3, 3],
    },
    {
        "description": "peekMax with multiple elements",
        "run": lambda: solution(
            ["MaxStack", "push", "push", "peekMax"],
            [[], [1], [10], []]
        ),
        "expected": [None, None, None, 10],
    },
    {
        "description": "popMax removes correct element",
        "run": lambda: solution(
            ["MaxStack", "push", "push", "push", "popMax", "top"],
            [[], [1], [5], [2], [], []]
        ),
        "expected": [None, None, None, None, 5, 2],
    },
]
