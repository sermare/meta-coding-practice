from problems.p599_serialize_and_deserialize_binary_tree import solution

TEST_CASES = [
    {
        "description": "Standard tree: [1,2,3,None,None,4,5]",
        "run": lambda: solution([1, 2, 3, None, None, 4, 5]),
        "expected": [1, 2, 3, None, None, 4, 5],
    },
    {
        "description": "Empty tree",
        "run": lambda: solution([]),
        "expected": [],
    },
    {
        "description": "Single node",
        "run": lambda: solution([1]),
        "expected": [1],
    },
    {
        "description": "Left-skewed: [1,2,None,3]",
        "run": lambda: solution([1, 2, None, 3]),
        "expected": [1, 2, None, 3],
    },
]
