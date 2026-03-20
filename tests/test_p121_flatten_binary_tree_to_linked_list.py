from problems.p121_flatten_binary_tree_to_linked_list import solution, build_tree, tree_to_list

TEST_CASES = [
    {
        "description": "Standard tree flatten",
        "run": lambda: (lambda r: (solution(r), tree_to_list(r))[1])(build_tree([1, 2, 5, 3, 4, None, 6])),
        "expected": [1, None, 2, None, 3, None, 4, None, 5, None, 6, None],
    },
    {
        "description": "Single node",
        "run": lambda: (lambda r: (solution(r), tree_to_list(r))[1])(build_tree([1])),
        "expected": [1, None],
    },
    {
        "description": "Empty tree",
        "run": lambda: (lambda r: (solution(r), tree_to_list(r))[1])(build_tree([])),
        "expected": [],
    },
    {
        "description": "Left skewed tree",
        "run": lambda: (lambda r: (solution(r), tree_to_list(r))[1])(build_tree([1, 2, None, 3])),
        "expected": [1, None, 2, None, 3, None],
    },
]
