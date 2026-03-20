from problems.p394_find_eventual_safe_states import solution


TEST_CASES = [
    {
        "description": "Standard graph with cycles",
        "run": lambda: solution([[1, 2], [2, 3], [5], [0], [5], [], []]),
        "expected": [2, 4, 5, 6],
    },
    {
        "description": "Graph with one safe node",
        "run": lambda: solution([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]),
        "expected": [4],
    },
    {
        "description": "All terminal nodes",
        "run": lambda: solution([[], [], []]),
        "expected": [0, 1, 2],
    },
    {
        "description": "Single self-loop",
        "run": lambda: solution([[0]]),
        "expected": [],
    },
]
