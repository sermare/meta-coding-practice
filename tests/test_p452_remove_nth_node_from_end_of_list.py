from problems.p452_remove_nth_node_from_end_of_list import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Remove 2nd from end: [1,2,3,4,5] -> [1,2,3,5]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3,4,5]), 2)),
        "expected": [1,2,3,5],
    },
    {
        "description": "Remove only node: [1] -> []",
        "run": lambda: linked_to_list(solution(list_to_linked([1]), 1)),
        "expected": [],
    },
    {
        "description": "Remove last: [1,2] -> [1]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2]), 1)),
        "expected": [1],
    },
    {
        "description": "Remove first: [1,2] -> [2]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2]), 2)),
        "expected": [2],
    },
    {
        "description": "Remove 3rd from end: [1,2,3,4,5] -> [1,2,4,5]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3,4,5]), 3)),
        "expected": [1,2,4,5],
    },
]
