from problems.p370_balance_a_bst import solution, build_tree


TEST_CASES = [
    {
        "description": "Right-skewed BST balanced",
        "run": lambda: solution(build_tree([1, None, 2, None, 3, None, 4])),
        "expected": [1, 2, 3, 4],
    },
    {
        "description": "Already balanced",
        "run": lambda: solution(build_tree([2, 1, 3])),
        "expected": [1, 2, 3],
    },
    {
        "description": "Single node",
        "run": lambda: solution(build_tree([1])),
        "expected": [1],
    },
    {
        "description": "Left-skewed BST balanced",
        "run": lambda: solution(build_tree([4, 3, None, 2, None, 1])),
        "expected": [1, 2, 3, 4],
    },
]
