from problems.p161_invert_binary_tree import solution, build_tree, tree_to_list

TEST_CASES = [
    {
        "description": "Invert [4,2,7,1,3,6,9]",
        "run": lambda: tree_to_list(solution(build_tree([4, 2, 7, 1, 3, 6, 9]))),
        "expected": [4, 7, 2, 9, 6, 3, 1],
    },
    {
        "description": "Invert [2,1,3]",
        "run": lambda: tree_to_list(solution(build_tree([2, 1, 3]))),
        "expected": [2, 3, 1],
    },
    {
        "description": "Empty tree",
        "run": lambda: tree_to_list(solution(build_tree([]))),
        "expected": [],
    },
    {
        "description": "Single node",
        "run": lambda: tree_to_list(solution(build_tree([1]))),
        "expected": [1],
    },
]
