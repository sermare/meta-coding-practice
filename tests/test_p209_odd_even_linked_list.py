from problems.p209_odd_even_linked_list import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Five nodes: [1,2,3,4,5] -> [1,3,5,2,4]",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2, 3, 4, 5]))),
        "expected": [1, 3, 5, 2, 4],
    },
    {
        "description": "Seven nodes: [2,1,3,5,6,4,7]",
        "run": lambda: linked_to_list(solution(list_to_linked([2, 1, 3, 5, 6, 4, 7]))),
        "expected": [2, 3, 6, 7, 1, 5, 4],
    },
    {
        "description": "Single node: [1]",
        "run": lambda: linked_to_list(solution(list_to_linked([1]))),
        "expected": [1],
    },
    {
        "description": "Two nodes: [1,2]",
        "run": lambda: linked_to_list(solution(list_to_linked([1, 2]))),
        "expected": [1, 2],
    },
    {
        "description": "Empty list",
        "run": lambda: linked_to_list(solution(list_to_linked([]))),
        "expected": [],
    },
]
