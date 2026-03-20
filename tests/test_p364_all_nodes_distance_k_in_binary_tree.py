from problems.p364_all_nodes_distance_k_in_binary_tree import solution, build_tree


TEST_CASES = [
    {
        "description": "Distance 2 from node 5",
        "run": lambda: sorted(solution(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), 5, 2)),
        "expected": [1, 4, 7],
    },
    {
        "description": "No nodes at distance 3 from root of single node",
        "run": lambda: solution(build_tree([1]), 1, 3),
        "expected": [],
    },
    {
        "description": "Distance 0 from target",
        "run": lambda: solution(build_tree([3, 5, 1]), 5, 0),
        "expected": [5],
    },
    {
        "description": "Distance 1 from root",
        "run": lambda: sorted(solution(build_tree([1, 2, 3]), 1, 1)),
        "expected": [2, 3],
    },
]
