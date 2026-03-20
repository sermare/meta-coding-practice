from problems.p014_binary_tree_level_order_traversal import solution, build_tree


TEST_CASES = [
    {
        "description": "Standard tree: [3,9,20,None,None,15,7]",
        "run": lambda: solution(build_tree([3, 9, 20, None, None, 15, 7])),
        "expected": [[3], [9, 20], [15, 7]],
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution(build_tree([1])),
        "expected": [[1]],
    },
    {
        "description": "Empty tree: []",
        "run": lambda: solution(build_tree([])),
        "expected": [],
    },
    {
        "description": "Complete binary tree: [1,2,3,4,5]",
        "run": lambda: solution(build_tree([1, 2, 3, 4, 5])),
        "expected": [[1], [2, 3], [4, 5]],
    },
]
