from problems.p453_merge_two_sorted_lists import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Standard merge: [1,2,4]+[1,3,4]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,4]), list_to_linked([1,3,4]))),
        "expected": [1,1,2,3,4,4],
    },
    {
        "description": "Both empty",
        "run": lambda: linked_to_list(solution(list_to_linked([]), list_to_linked([]))),
        "expected": [],
    },
    {
        "description": "One empty: []+[0]",
        "run": lambda: linked_to_list(solution(list_to_linked([]), list_to_linked([0]))),
        "expected": [0],
    },
    {
        "description": "Single elements: [2]+[1]",
        "run": lambda: linked_to_list(solution(list_to_linked([2]), list_to_linked([1]))),
        "expected": [1,2],
    },
    {
        "description": "Different lengths: [1,3,5]+[2,4]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,3,5]), list_to_linked([2,4]))),
        "expected": [1,2,3,4,5],
    },
]
