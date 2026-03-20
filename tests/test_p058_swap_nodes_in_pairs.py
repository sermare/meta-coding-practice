from problems.p058_swap_nodes_in_pairs import solution, build_list, list_to_array

TEST_CASES = [
    {
        "description": "Even length: [1,2,3,4]",
        "run": lambda: list_to_array(solution(build_list([1, 2, 3, 4]))),
        "expected": [2, 1, 4, 3],
    },
    {
        "description": "Empty list",
        "run": lambda: list_to_array(solution(build_list([]))),
        "expected": [],
    },
    {
        "description": "Single node: [1]",
        "run": lambda: list_to_array(solution(build_list([1]))),
        "expected": [1],
    },
    {
        "description": "Odd length: [1,2,3]",
        "run": lambda: list_to_array(solution(build_list([1, 2, 3]))),
        "expected": [2, 1, 3],
    },
]
