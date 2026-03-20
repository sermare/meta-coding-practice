from problems.p207_implement_stack_using_queues import solution

TEST_CASES = [
    {
        "description": "Basic operations: push, push, top, pop, empty",
        "run": lambda: solution(["push", "push", "top", "pop", "empty"], [1, 2, None, None, None]),
        "expected": [None, None, 2, 2, False],
    },
    {
        "description": "Push and pop single element",
        "run": lambda: solution(["push", "pop", "empty"], [1, None, None]),
        "expected": [None, 1, True],
    },
    {
        "description": "Multiple pushes then pops (LIFO order)",
        "run": lambda: solution(["push", "push", "push", "pop", "pop", "pop"], [1, 2, 3, None, None, None]),
        "expected": [None, None, None, 3, 2, 1],
    },
    {
        "description": "Top without pop",
        "run": lambda: solution(["push", "push", "top", "top"], [10, 20, None, None]),
        "expected": [None, None, 20, 20],
    },
]
