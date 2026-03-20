from problems.p365_flatten_binary_tree_to_linked_list import solution, build_tree


TEST_CASES = [
    {
        "description": "Standard tree flattened",
        "run": lambda: solution(build_tree([1, 2, 5, 3, 4, None, 6])),
        "expected": [1, 2, 3, 4, 5, 6],
    },
    {
        "description": "Empty tree",
        "run": lambda: solution(build_tree([])),
        "expected": [],
    },
    {
        "description": "Single node",
        "run": lambda: solution(build_tree([0])),
        "expected": [0],
    },
    {
        "description": "Left-only tree",
        "run": lambda: solution(build_tree([1, 2, None, 3])),
        "expected": [1, 2, 3],
    },
]
