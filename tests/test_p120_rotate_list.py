from problems.p120_rotate_list import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Rotate right by 2",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2, 3, 4, 5]), 2)),
        "expected": [4, 5, 1, 2, 3],
    },
    {
        "description": "Rotate more than length",
        "run": lambda: linked_to_list(solution(list_to_linked([0, 1, 2]), 4)),
        "expected": [2, 0, 1],
    },
    {
        "description": "Empty list",
        "run": lambda: linked_to_list(solution(list_to_linked([]), 1)),
        "expected": [],
    },
    {
        "description": "Single node",
        "run": lambda: linked_to_list(solution(list_to_linked([1]), 99)),
        "expected": [1],
    },
    {
        "description": "Rotate by 0",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2, 3]), 0)),
        "expected": [1, 2, 3],
    },
]
