from problems.p250_merge_two_sorted_lists import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Both non-empty: [1,2,4] + [1,3,4]",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2, 4]), list_to_linked([1, 3, 4]))),
        "expected": [1, 1, 2, 3, 4, 4],
    },
    {
        "description": "One empty: [] + [0]",
        "run": lambda: linked_to_list(solution(list_to_linked([]), list_to_linked([0]))),
        "expected": [0],
    },
    {
        "description": "Both empty",
        "run": lambda: linked_to_list(solution(list_to_linked([]), list_to_linked([]))),
        "expected": [],
    },
    {
        "description": "Single elements: [1] + [2]",
        "run": lambda: linked_to_list(solution(list_to_linked([1]), list_to_linked([2]))),
        "expected": [1, 2],
    },
    {
        "description": "No interleaving: [1,2,3] + [4,5,6]",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2, 3]), list_to_linked([4, 5, 6]))),
        "expected": [1, 2, 3, 4, 5, 6],
    },
]
