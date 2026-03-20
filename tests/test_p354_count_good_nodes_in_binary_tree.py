from problems.p354_count_good_nodes_in_binary_tree import solution, build_tree


TEST_CASES = [
    {
        "description": "Standard tree: 4 good nodes",
        "run": lambda: solution(build_tree([3, 1, 4, 3, None, 1, 5])),
        "expected": 4,
    },
    {
        "description": "Left-heavy tree: 3 good nodes",
        "run": lambda: solution(build_tree([3, 3, None, 4, 2])),
        "expected": 3,
    },
    {
        "description": "Single node: 1 good node",
        "run": lambda: solution(build_tree([1])),
        "expected": 1,
    },
    {
        "description": "All equal values: all good",
        "run": lambda: solution(build_tree([2, 2, 2])),
        "expected": 3,
    },
    {
        "description": "Decreasing values: only root is good",
        "run": lambda: solution(build_tree([5, 3, 4, 1, 2])),
        "expected": 1,
    },
]
