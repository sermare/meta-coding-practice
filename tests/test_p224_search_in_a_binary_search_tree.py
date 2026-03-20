from problems.p224_search_in_a_binary_search_tree import solution, build_tree, tree_to_list

TEST_CASES = [
    {
        "description": "Found: val=2 in [4,2,7,1,3]",
        "run": lambda: tree_to_list(solution(build_tree([4, 2, 7, 1, 3]), 2)),
        "expected": [2, 1, 3],
    },
    {
        "description": "Not found: val=5 in [4,2,7,1,3]",
        "run": lambda: tree_to_list(solution(build_tree([4, 2, 7, 1, 3]), 5)),
        "expected": [],
    },
    {
        "description": "Root match: val=4",
        "run": lambda: tree_to_list(solution(build_tree([4, 2, 7, 1, 3]), 4)),
        "expected": [4, 2, 7, 1, 3],
    },
    {
        "description": "Empty tree: val=1",
        "run": lambda: tree_to_list(solution(build_tree([]), 1)),
        "expected": [],
    },
]
