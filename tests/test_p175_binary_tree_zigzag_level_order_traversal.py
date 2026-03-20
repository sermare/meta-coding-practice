from problems.p175_binary_tree_zigzag_level_order_traversal import solution, build_tree

TEST_CASES = [
    {
        "description": "Zigzag [3,9,20,None,None,15,7]",
        "run": lambda: solution(build_tree([3, 9, 20, None, None, 15, 7])),
        "expected": [[3], [20, 9], [15, 7]],
    },
    {
        "description": "Single node",
        "run": lambda: solution(build_tree([1])),
        "expected": [[1]],
    },
    {
        "description": "Empty tree",
        "run": lambda: solution(build_tree([])),
        "expected": [],
    },
    {
        "description": "Two levels",
        "run": lambda: solution(build_tree([1, 2, 3])),
        "expected": [[1], [3, 2]],
    },
]
