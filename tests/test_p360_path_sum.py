from problems.p360_path_sum import solution, build_tree


TEST_CASES = [
    {
        "description": "Path exists: 5->4->11->2 = 22",
        "run": lambda: solution(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22),
        "expected": True,
    },
    {
        "description": "No valid path",
        "run": lambda: solution(build_tree([1, 2, 3]), 5),
        "expected": False,
    },
    {
        "description": "Empty tree",
        "run": lambda: solution(build_tree([]), 0),
        "expected": False,
    },
    {
        "description": "Single node matches",
        "run": lambda: solution(build_tree([1]), 1),
        "expected": True,
    },
    {
        "description": "Single node does not match",
        "run": lambda: solution(build_tree([1]), 2),
        "expected": False,
    },
]
