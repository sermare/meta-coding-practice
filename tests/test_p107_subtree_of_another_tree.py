from problems.p107_subtree_of_another_tree import solution, build_tree

TEST_CASES = [
    {
        "description": "Subtree exists",
        "run": lambda: solution(build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2])),
        "expected": True,
    },
    {
        "description": "Subtree does not match (extra child)",
        "run": lambda: solution(build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]), build_tree([4, 1, 2])),
        "expected": False,
    },
    {
        "description": "Both are the same tree",
        "run": lambda: solution(build_tree([1, 2, 3]), build_tree([1, 2, 3])),
        "expected": True,
    },
    {
        "description": "Single node match",
        "run": lambda: solution(build_tree([1, 2, 3]), build_tree([2])),
        "expected": True,
    },
    {
        "description": "Single node no match",
        "run": lambda: solution(build_tree([1, 2, 3]), build_tree([4])),
        "expected": False,
    },
]
