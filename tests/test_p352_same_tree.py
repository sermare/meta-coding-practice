from problems.p352_same_tree import solution, build_tree


TEST_CASES = [
    {
        "description": "Identical trees",
        "run": lambda: solution(build_tree([1, 2, 3]), build_tree([1, 2, 3])),
        "expected": True,
    },
    {
        "description": "Different structure",
        "run": lambda: solution(build_tree([1, 2]), build_tree([1, None, 2])),
        "expected": False,
    },
    {
        "description": "Different values",
        "run": lambda: solution(build_tree([1, 2, 1]), build_tree([1, 1, 2])),
        "expected": False,
    },
    {
        "description": "Both empty",
        "run": lambda: solution(build_tree([]), build_tree([])),
        "expected": True,
    },
    {
        "description": "One empty one not",
        "run": lambda: solution(build_tree([1]), build_tree([])),
        "expected": False,
    },
]
