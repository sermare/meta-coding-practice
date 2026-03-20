from problems.p355_kth_smallest_element_in_bst import solution, build_tree


TEST_CASES = [
    {
        "description": "k=1 smallest in BST",
        "run": lambda: solution(build_tree([3, 1, 4, None, 2]), 1),
        "expected": 1,
    },
    {
        "description": "k=3 in larger BST",
        "run": lambda: solution(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3),
        "expected": 3,
    },
    {
        "description": "Single node, k=1",
        "run": lambda: solution(build_tree([1]), 1),
        "expected": 1,
    },
    {
        "description": "k equals number of nodes",
        "run": lambda: solution(build_tree([3, 1, 4]), 3),
        "expected": 4,
    },
]
