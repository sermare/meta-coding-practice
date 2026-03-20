from problems.p382_graph_valid_tree import solution


TEST_CASES = [
    {
        "description": "Valid tree",
        "run": lambda: solution(5, [[0, 1], [0, 2], [0, 3], [1, 4]]),
        "expected": True,
    },
    {
        "description": "Has cycle: not a tree",
        "run": lambda: solution(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]),
        "expected": False,
    },
    {
        "description": "Single node: valid tree",
        "run": lambda: solution(1, []),
        "expected": True,
    },
    {
        "description": "Disconnected: not a tree",
        "run": lambda: solution(4, [[0, 1], [2, 3]]),
        "expected": False,
    },
]
