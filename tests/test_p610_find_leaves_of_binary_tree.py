from problems.p610_find_leaves_of_binary_tree import solution

TEST_CASES = [
    {
        "description": "Standard tree: [1,2,3,4,5]",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": [[4, 5, 3], [2], [1]],
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution([1]),
        "expected": [[1]],
    },
    {
        "description": "Left-skewed: [1,2,null,3]",
        "run": lambda: solution([1, 2, None, 3]),
        "expected": [[3], [2], [1]],
    },
    {
        "description": "Balanced tree: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": [[2, 3], [1]],
    },
]
