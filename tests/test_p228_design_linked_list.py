from problems.p228_design_linked_list import solution

TEST_CASES = [
    {
        "description": "Basic operations",
        "run": lambda: solution(
            ["addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"],
            [[1], [3], [1, 2], [1], [1], [1]]),
        "expected": [None, None, None, 2, None, 3],
    },
    {
        "description": "Get invalid index",
        "run": lambda: solution(["addAtHead", "get"], [[1], [5]]),
        "expected": [None, -1],
    },
    {
        "description": "Add at head multiple",
        "run": lambda: solution(["addAtHead", "addAtHead", "get", "get"], [[2], [1], [0], [1]]),
        "expected": [None, None, 1, 2],
    },
    {
        "description": "Delete and get",
        "run": lambda: solution(
            ["addAtHead", "addAtHead", "deleteAtIndex", "get"],
            [[2], [1], [0], [0]]),
        "expected": [None, None, None, 2],
    },
]
