from problems.p367_delete_node_in_a_bst import solution, build_tree


TEST_CASES = [
    {
        "description": "Delete node 3 from BST",
        "run": lambda: solution(build_tree([5, 3, 6, 2, 4, None, 7]), 3),
        "expected": [2, 4, 5, 6, 7],
    },
    {
        "description": "Delete non-existent key",
        "run": lambda: solution(build_tree([5, 3, 6, 2, 4, None, 7]), 0),
        "expected": [2, 3, 4, 5, 6, 7],
    },
    {
        "description": "Empty tree",
        "run": lambda: solution(build_tree([]), 0),
        "expected": [],
    },
    {
        "description": "Delete root of single node",
        "run": lambda: solution(build_tree([1]), 1),
        "expected": [],
    },
]
