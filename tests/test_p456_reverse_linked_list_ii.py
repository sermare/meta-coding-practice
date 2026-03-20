from problems.p456_reverse_linked_list_ii import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Reverse middle: [1,2,3,4,5] left=2 right=4",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3,4,5]), 2, 4)),
        "expected": [1,4,3,2,5],
    },
    {
        "description": "Single node: [5] left=1 right=1",
        "run": lambda: linked_to_list(solution(list_to_linked([5]), 1, 1)),
        "expected": [5],
    },
    {
        "description": "Reverse entire list: [1,2,3] left=1 right=3",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3]), 1, 3)),
        "expected": [3,2,1],
    },
    {
        "description": "Reverse first two: [1,2,3,4] left=1 right=2",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3,4]), 1, 2)),
        "expected": [2,1,3,4],
    },
    {
        "description": "Reverse last two: [1,2,3,4] left=3 right=4",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3,4]), 3, 4)),
        "expected": [1,2,4,3],
    },
]
