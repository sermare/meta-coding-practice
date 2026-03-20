from problems.p240_n-ary_tree_level_order_traversal import solution, build_nary_tree

TEST_CASES = [
    {
        "description": "Standard N-ary tree",
        "run": lambda: solution(build_nary_tree(
            [1, 3, 2, 4, 5, 6],
            {1: [3, 2, 4], 3: [5, 6]})),
        "expected": [[1], [3, 2, 4], [5, 6]],
    },
    {
        "description": "Single node",
        "run": lambda: solution(build_nary_tree([1], {})),
        "expected": [[1]],
    },
    {
        "description": "Empty tree",
        "run": lambda: solution(None),
        "expected": [],
    },
    {
        "description": "Two levels only",
        "run": lambda: solution(build_nary_tree([1, 2, 3], {1: [2, 3]})),
        "expected": [[1], [2, 3]],
    },
]
