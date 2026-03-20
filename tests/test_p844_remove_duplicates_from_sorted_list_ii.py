from problems.p844_remove_duplicates_from_sorted_list_ii import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Remove dups: [1,2,3,3,4,4,5] -> [1,2,5]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3,3,4,4,5]))),
        "expected": [1,2,5],
    },
    {
        "description": "All dups: [1,1,1,2,3] -> [2,3]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,1,1,2,3]))),
        "expected": [2,3],
    },
    {
        "description": "No dups: [1,2,3]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3]))),
        "expected": [1,2,3],
    },
    {
        "description": "Empty list",
        "run": lambda: linked_to_list(solution(list_to_linked([]))),
        "expected": [],
    },
]
