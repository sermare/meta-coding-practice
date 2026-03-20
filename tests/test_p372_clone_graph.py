from problems.p372_clone_graph import solution


TEST_CASES = [
    {
        "description": "4-node cycle graph",
        "run": lambda: solution([[2, 4], [1, 3], [2, 4], [1, 3]]),
        "expected": [[2, 4], [1, 3], [2, 4], [1, 3]],
    },
    {
        "description": "Single node no neighbors",
        "run": lambda: solution([[]]),
        "expected": [[]],
    },
    {
        "description": "Empty graph",
        "run": lambda: solution([]),
        "expected": [],
    },
    {
        "description": "Two connected nodes",
        "run": lambda: solution([[2], [1]]),
        "expected": [[2], [1]],
    },
]
