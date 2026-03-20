from problems.p357_binary_tree_maximum_path_sum import solution, build_tree


TEST_CASES = [
    {
        "description": "Simple tree: path 2->1->3 = 6",
        "run": lambda: solution(build_tree([1, 2, 3])),
        "expected": 6,
    },
    {
        "description": "Negative root: path 15->20->7 = 42",
        "run": lambda: solution(build_tree([-10, 9, 20, None, None, 15, 7])),
        "expected": 42,
    },
    {
        "description": "Single node",
        "run": lambda: solution(build_tree([5])),
        "expected": 5,
    },
    {
        "description": "All negative: pick least negative",
        "run": lambda: solution(build_tree([-3, -2, -1])),
        "expected": -1,
    },
    {
        "description": "Single negative node",
        "run": lambda: solution(build_tree([-1])),
        "expected": -1,
    },
]
