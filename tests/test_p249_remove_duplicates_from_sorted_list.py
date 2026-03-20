from problems.p249_remove_duplicates_from_sorted_list import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Duplicates: [1,1,2] -> [1,2]",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 1, 2]))),
        "expected": [1, 2],
    },
    {
        "description": "Multiple duplicates: [1,1,2,3,3] -> [1,2,3]",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 1, 2, 3, 3]))),
        "expected": [1, 2, 3],
    },
    {
        "description": "No duplicates: [1,2,3]",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2, 3]))),
        "expected": [1, 2, 3],
    },
    {
        "description": "All same: [1,1,1]",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 1, 1]))),
        "expected": [1],
    },
    {
        "description": "Empty list",
        "run": lambda: linked_to_list(solution(list_to_linked([]))),
        "expected": [],
    },
]
