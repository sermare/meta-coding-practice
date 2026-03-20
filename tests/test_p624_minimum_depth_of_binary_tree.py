from problems.p624_minimum_depth_of_binary_tree import solution

TEST_CASES = [
    {
        "description": "Balanced tree: [3,9,20,null,null,15,7]",
        "run": lambda: solution([3, 9, 20, None, None, 15, 7]),
        "expected": 2,
    },
    {
        "description": "Right-skewed: [2,null,3,null,4,null,5,null,6]",
        "run": lambda: solution([2, None, 3, None, 4, None, 5, None, 6]),
        "expected": 5,
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "Two levels: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": 2,
    },
]
