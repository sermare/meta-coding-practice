from problems.p146_reverse_nodes_in_k-group import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Reverse in groups of 2",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2, 3, 4, 5]), 2)),
        "expected": [2, 1, 4, 3, 5],
    },
    {
        "description": "Reverse in groups of 3",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2, 3, 4, 5]), 3)),
        "expected": [3, 2, 1, 4, 5],
    },
    {
        "description": "k equals list length",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2, 3]), 3)),
        "expected": [3, 2, 1],
    },
    {
        "description": "k = 1, no change",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2, 3]), 1)),
        "expected": [1, 2, 3],
    },
    {
        "description": "Single node",
        "run": lambda: linked_to_list(solution(list_to_linked([1]), 1)),
        "expected": [1],
    },
]
