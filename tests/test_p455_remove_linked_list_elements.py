from problems.p455_remove_linked_list_elements import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Remove 6 from [1,2,6,3,4,5,6]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,6,3,4,5,6]), 6)),
        "expected": [1,2,3,4,5],
    },
    {
        "description": "Empty list",
        "run": lambda: linked_to_list(solution(list_to_linked([]), 1)),
        "expected": [],
    },
    {
        "description": "Remove all: [7,7,7,7] val=7",
        "run": lambda: linked_to_list(solution(list_to_linked([7,7,7,7]), 7)),
        "expected": [],
    },
    {
        "description": "No removal: [1,2,3] val=4",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3]), 4)),
        "expected": [1,2,3],
    },
    {
        "description": "Remove from head: [1,1,2,3] val=1",
        "run": lambda: linked_to_list(solution(list_to_linked([1,1,2,3]), 1)),
        "expected": [2,3],
    },
]
