from problems.p110_symmetric_tree import solution, build_tree

TEST_CASES = [
    {
        "description": "Symmetric tree",
        "run": lambda: solution(build_tree([1, 2, 2, 3, 4, 4, 3])),
        "expected": True,
    },
    {
        "description": "Asymmetric tree",
        "run": lambda: solution(build_tree([1, 2, 2, None, 3, None, 3])),
        "expected": False,
    },
    {
        "description": "Single node is symmetric",
        "run": lambda: solution(build_tree([1])),
        "expected": True,
    },
    {
        "description": "Two level symmetric",
        "run": lambda: solution(build_tree([1, 2, 2])),
        "expected": True,
    },
    {
        "description": "Different values, not symmetric",
        "run": lambda: solution(build_tree([1, 2, 3])),
        "expected": False,
    },
]
