from problems.p007_reverse_linked_list import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Five elements: [1,2,3,4,5] -> [5,4,3,2,1]",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2, 3, 4, 5]))),
        "expected": [5, 4, 3, 2, 1],
    },
    {
        "description": "Two elements: [1,2] -> [2,1]",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2]))),
        "expected": [2, 1],
    },
    {
        "description": "Single element: [1] -> [1]",
        "run": lambda: linked_to_list(solution(list_to_linked([1]))),
        "expected": [1],
    },
    {
        "description": "Empty list: [] -> []",
        "run": lambda: linked_to_list(solution(list_to_linked([]))),
        "expected": [],
    },
]
