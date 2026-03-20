from problems.p361_path_sum_ii import solution, build_tree


TEST_CASES = [
    {
        "description": "Two valid paths",
        "run": lambda: solution(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22),
        "expected": [[5, 4, 11, 2], [5, 8, 4, 5]],
    },
    {
        "description": "No valid paths",
        "run": lambda: solution(build_tree([1, 2, 3]), 5),
        "expected": [],
    },
    {
        "description": "Empty tree",
        "run": lambda: solution(build_tree([]), 0),
        "expected": [],
    },
    {
        "description": "Single node path",
        "run": lambda: solution(build_tree([1]), 1),
        "expected": [[1]],
    },
]
