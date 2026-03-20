from problems.p237_leaf-similar_trees import solution, build_tree

TEST_CASES = [
    {
        "description": "Leaf-similar trees",
        "run": lambda: solution(
            build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
            build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])),
        "expected": True,
    },
    {
        "description": "Not leaf-similar: [1,2,3] vs [1,3,2]",
        "run": lambda: solution(build_tree([1, 2, 3]), build_tree([1, 3, 2])),
        "expected": False,
    },
    {
        "description": "Single node same",
        "run": lambda: solution(build_tree([1]), build_tree([1])),
        "expected": True,
    },
    {
        "description": "Single node different",
        "run": lambda: solution(build_tree([1]), build_tree([2])),
        "expected": False,
    },
]
