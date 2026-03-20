from problems.p631_maximum_depth_of_binary_tree import solution

TEST_CASES = [
    {
        "description": "Standard tree: [3,9,20,null,null,15,7]",
        "run": lambda: solution([3, 9, 20, None, None, 15, 7]),
        "expected": 3,
    },
    {
        "description": "Simple tree: [1,null,2]",
        "run": lambda: solution([1, None, 2]),
        "expected": 2,
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "Empty tree",
        "run": lambda: solution([]),
        "expected": 0,
    },
]
