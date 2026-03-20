from problems.p222_longest_univalue_path import solution, build_tree

TEST_CASES = [
    {
        "description": "Mixed tree: [5,4,5,1,1,None,5]",
        "run": lambda: solution(build_tree([5, 4, 5, 1, 1, None, 5])),
        "expected": 2,
    },
    {
        "description": "All same: [1,1,1,1,1]",
        "run": lambda: solution(build_tree([1, 1, 1, 1, 1])),
        "expected": 2,
    },
    {
        "description": "Single node",
        "run": lambda: solution(build_tree([1])),
        "expected": 0,
    },
    {
        "description": "Empty tree",
        "run": lambda: solution(build_tree([])),
        "expected": 0,
    },
]
