from problems.p619_serialize_and_deserialize_bst import solution

TEST_CASES = [
    {
        "description": "Simple BST: [2,1,3]",
        "run": lambda: solution([2, 1, 3]),
        "expected": [2, 1, 3],
    },
    {
        "description": "Empty tree",
        "run": lambda: solution([]),
        "expected": [],
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution([1]),
        "expected": [1],
    },
    {
        "description": "Left-skewed: [3,2,null,1]",
        "run": lambda: solution([3, 2, None, 1]),
        "expected": [3, 2, None, 1],
    },
]
