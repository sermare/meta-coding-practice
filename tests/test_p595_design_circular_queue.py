from problems.p595_design_circular_queue import solution

TEST_CASES = [
    {
        "description": "Standard operations",
        "run": lambda: solution(
            3,
            ["enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"],
            [[1], [2], [3], [4], [], [], [], [4], []]
        ),
        "expected": [True, True, True, False, 3, True, True, True, 4],
    },
    {
        "description": "Empty queue operations",
        "run": lambda: solution(
            2,
            ["isEmpty", "Front", "Rear", "deQueue"],
            [[], [], [], []]
        ),
        "expected": [True, -1, -1, False],
    },
    {
        "description": "Fill and drain",
        "run": lambda: solution(
            1,
            ["enQueue", "isFull", "deQueue", "isEmpty"],
            [[5], [], [], []]
        ),
        "expected": [True, True, True, True],
    },
    {
        "description": "Wrap around",
        "run": lambda: solution(
            2,
            ["enQueue", "enQueue", "deQueue", "enQueue", "Rear", "Front"],
            [[1], [2], [], [3], [], []]
        ),
        "expected": [True, True, True, True, 3, 2],
    },
]
