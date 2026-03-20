from problems.p458_sort_list import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Standard: [4,2,1,3] -> [1,2,3,4]",
        "run": lambda: linked_to_list(solution(list_to_linked([4,2,1,3]))),
        "expected": [1,2,3,4],
    },
    {
        "description": "Negative values: [-1,5,3,4,0]",
        "run": lambda: linked_to_list(solution(list_to_linked([-1,5,3,4,0]))),
        "expected": [-1,0,3,4,5],
    },
    {
        "description": "Empty list",
        "run": lambda: linked_to_list(solution(list_to_linked([]))),
        "expected": [],
    },
    {
        "description": "Already sorted: [1,2,3]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3]))),
        "expected": [1,2,3],
    },
    {
        "description": "Reverse sorted: [3,2,1]",
        "run": lambda: linked_to_list(solution(list_to_linked([3,2,1]))),
        "expected": [1,2,3],
    },
]
