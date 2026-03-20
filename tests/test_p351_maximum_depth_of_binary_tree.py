from problems.p351_maximum_depth_of_binary_tree import solution, build_tree


TEST_CASES = [
    {
        "description": "Standard tree: depth 3",
        "run": lambda: solution(build_tree([3, 9, 20, None, None, 15, 7])),
        "expected": 3,
    },
    {
        "description": "Right-skewed tree: depth 2",
        "run": lambda: solution(build_tree([1, None, 2])),
        "expected": 2,
    },
    {
        "description": "Empty tree: depth 0",
        "run": lambda: solution(build_tree([])),
        "expected": 0,
    },
    {
        "description": "Single node: depth 1",
        "run": lambda: solution(build_tree([1])),
        "expected": 1,
    },
    {
        "description": "Left-skewed tree: depth 4",
        "run": lambda: solution(build_tree([1, 2, None, 3, None, 4])),
        "expected": 4,
    },
]
