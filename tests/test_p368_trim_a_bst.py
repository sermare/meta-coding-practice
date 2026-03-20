from problems.p368_trim_a_bst import solution, build_tree


TEST_CASES = [
    {
        "description": "Trim [1,0,2] to [1,2]",
        "run": lambda: solution(build_tree([1, 0, 2]), 1, 2),
        "expected": [1, 2],
    },
    {
        "description": "Trim [3,0,4,None,2,None,None,1] to [1,3]",
        "run": lambda: solution(build_tree([3, 0, 4, None, 2, None, None, 1]), 1, 3),
        "expected": [1, 2, 3],
    },
    {
        "description": "No trimming needed",
        "run": lambda: solution(build_tree([2, 1, 3]), 1, 3),
        "expected": [1, 2, 3],
    },
    {
        "description": "Trim everything except root",
        "run": lambda: solution(build_tree([2, 1, 3]), 2, 2),
        "expected": [2],
    },
]
