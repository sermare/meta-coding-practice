from problems.p353_binary_tree_right_side_view import solution, build_tree


TEST_CASES = [
    {
        "description": "Standard tree right side view",
        "run": lambda: solution(build_tree([1, 2, 3, None, 5, None, 4])),
        "expected": [1, 3, 4],
    },
    {
        "description": "Right-only tree",
        "run": lambda: solution(build_tree([1, None, 3])),
        "expected": [1, 3],
    },
    {
        "description": "Empty tree",
        "run": lambda: solution(build_tree([])),
        "expected": [],
    },
    {
        "description": "Single node",
        "run": lambda: solution(build_tree([1])),
        "expected": [1],
    },
    {
        "description": "Left side deeper than right",
        "run": lambda: solution(build_tree([1, 2, 3, 4])),
        "expected": [1, 3, 4],
    },
]
