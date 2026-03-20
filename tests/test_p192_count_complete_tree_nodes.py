from problems.p192_count_complete_tree_nodes import solution, build_tree

TEST_CASES = [
    {
        "description": "6 nodes",
        "run": lambda: solution(build_tree([1, 2, 3, 4, 5, 6])),
        "expected": 6,
    },
    {
        "description": "Empty tree",
        "run": lambda: solution(build_tree([])),
        "expected": 0,
    },
    {
        "description": "Single node",
        "run": lambda: solution(build_tree([1])),
        "expected": 1,
    },
    {
        "description": "Perfect tree 7 nodes",
        "run": lambda: solution(build_tree([1, 2, 3, 4, 5, 6, 7])),
        "expected": 7,
    },
]
