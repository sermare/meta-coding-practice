from problems.p620_binary_tree_upside_down import solution

TEST_CASES = [
    {
        "description": "Standard tree: [1,2,3,4,5]",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": [4, 5, 2, None, None, 3, 1],
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
        "description": "Two levels: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": [2, 3, 1],
    },
]
