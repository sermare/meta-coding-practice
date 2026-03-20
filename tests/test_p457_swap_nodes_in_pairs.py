from problems.p457_swap_nodes_in_pairs import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Even length: [1,2,3,4] -> [2,1,4,3]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3,4]))),
        "expected": [2,1,4,3],
    },
    {
        "description": "Empty list",
        "run": lambda: linked_to_list(solution(list_to_linked([]))),
        "expected": [],
    },
    {
        "description": "Single node: [1]",
        "run": lambda: linked_to_list(solution(list_to_linked([1]))),
        "expected": [1],
    },
    {
        "description": "Odd length: [1,2,3] -> [2,1,3]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3]))),
        "expected": [2,1,3],
    },
    {
        "description": "Six nodes: [1,2,3,4,5,6] -> [2,1,4,3,6,5]",
        "run": lambda: linked_to_list(solution(list_to_linked([1,2,3,4,5,6]))),
        "expected": [2,1,4,3,6,5],
    },
]
