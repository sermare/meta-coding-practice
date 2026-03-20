from problems.p632_binary_tree_zigzag_level_order_traversal import solution

TEST_CASES = [
    {
        "description": "Standard tree: [3,9,20,null,null,15,7]",
        "run": lambda: solution([3, 9, 20, None, None, 15, 7]),
        "expected": [[3], [20, 9], [15, 7]],
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution([1]),
        "expected": [[1]],
    },
    {
        "description": "Empty tree",
        "run": lambda: solution([]),
        "expected": [],
    },
    {
        "description": "Two levels: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": [[1], [3, 2]],
    },
]
