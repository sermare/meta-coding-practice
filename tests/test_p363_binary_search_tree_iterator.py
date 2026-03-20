from problems.p363_binary_search_tree_iterator import solution, build_tree


TEST_CASES = [
    {
        "description": "Standard BST iteration",
        "run": lambda: solution(build_tree([7, 3, 15, None, None, 9, 20])),
        "expected": [3, 7, 9, 15, 20],
    },
    {
        "description": "Single node",
        "run": lambda: solution(build_tree([1])),
        "expected": [1],
    },
    {
        "description": "Left-skewed BST",
        "run": lambda: solution(build_tree([3, 2, None, 1])),
        "expected": [1, 2, 3],
    },
    {
        "description": "Right-skewed BST",
        "run": lambda: solution(build_tree([1, None, 2, None, 3])),
        "expected": [1, 2, 3],
    },
]
