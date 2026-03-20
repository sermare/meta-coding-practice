from problems.p590_binary_tree_level_order_traversal import solution

TEST_CASES = [
    {
        "description": "Standard tree: [3,9,20,None,None,15,7]",
        "run": lambda: solution([3, 9, 20, None, None, 15, 7]),
        "expected": [[3], [9, 20], [15, 7]],
    },
    {
        "description": "Single node",
        "run": lambda: solution([1]),
        "expected": [[1]],
    },
    {
        "description": "Empty tree",
        "run": lambda: solution([]),
        "expected": [],
    },
    {
        "description": "Left-skewed: [1,2,None,3]",
        "run": lambda: solution([1, 2, None, 3]),
        "expected": [[1], [2], [3]],
    },
]
