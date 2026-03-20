from problems.p362_sum_root_to_leaf_numbers import solution, build_tree


TEST_CASES = [
    {
        "description": "Two leaf paths: 12 + 13 = 25",
        "run": lambda: solution(build_tree([1, 2, 3])),
        "expected": 25,
    },
    {
        "description": "Three leaf paths: 495 + 491 + 40 = 1026",
        "run": lambda: solution(build_tree([4, 9, 0, 5, 1])),
        "expected": 1026,
    },
    {
        "description": "Single node",
        "run": lambda: solution(build_tree([5])),
        "expected": 5,
    },
    {
        "description": "Two levels: 10 + 11 = 21",
        "run": lambda: solution(build_tree([1, 0, 1])),
        "expected": 21,
    },
]
