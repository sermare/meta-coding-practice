from problems.p168_serialize_and_deserialize_bst import solution

TEST_CASES = [
    {
        "description": "BST [2,1,3] -> inorder [1,2,3]",
        "run": lambda: solution([2, 1, 3]),
        "expected": [1, 2, 3],
    },
    {
        "description": "Single node",
        "run": lambda: solution([1]),
        "expected": [1],
    },
    {
        "description": "Empty tree",
        "run": lambda: solution([]),
        "expected": [],
    },
    {
        "description": "Larger BST",
        "run": lambda: solution([5, 3, 7, 1, 4, 6, 8]),
        "expected": [1, 3, 4, 5, 6, 7, 8],
    },
]
