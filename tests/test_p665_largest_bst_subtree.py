from problems.p665_largest_bst_subtree import solution

TEST_CASES = [
    {
        "description": "Mixed tree: [10,5,15,1,8,None,7]",
        "run": lambda: solution([10, 5, 15, 1, 8, None, 7]),
        "expected": 3,
    },
    {
        "description": "Entire tree is BST: [2,1,3]",
        "run": lambda: solution([2, 1, 3]),
        "expected": 3,
    },
    {
        "description": "Single node",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "Empty tree",
        "run": lambda: solution([]),
        "expected": 0,
    },
]
