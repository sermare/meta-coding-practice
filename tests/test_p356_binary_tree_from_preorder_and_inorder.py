from problems.p356_binary_tree_from_preorder_and_inorder import solution, tree_to_list, TreeNode


TEST_CASES = [
    {
        "description": "Standard tree construction",
        "run": lambda: tree_to_list(solution([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])),
        "expected": [3, 9, 20, None, None, 15, 7],
    },
    {
        "description": "Single node",
        "run": lambda: tree_to_list(solution([-1], [-1])),
        "expected": [-1],
    },
    {
        "description": "Left-skewed tree",
        "run": lambda: tree_to_list(solution([3, 2, 1], [1, 2, 3])),
        "expected": [3, 2, None, 1],
    },
    {
        "description": "Right-skewed tree",
        "run": lambda: tree_to_list(solution([1, 2, 3], [1, 2, 3])),
        "expected": [1, None, 2, None, 3],
    },
]
