from problems.p569_shortest_path_in_binary_matrix import solution

TEST_CASES = [
    {
        "description": "2x2 diagonal: 2",
        "run": lambda: solution([[0, 1], [1, 0]]),
        "expected": 2,
    },
    {
        "description": "3x3 path: 4",
        "run": lambda: solution([[0, 0, 0], [1, 1, 0], [1, 1, 0]]),
        "expected": 4,
    },
    {
        "description": "Blocked start: -1",
        "run": lambda: solution([[1, 0, 0], [1, 1, 0], [1, 1, 0]]),
        "expected": -1,
    },
    {
        "description": "1x1 grid: 1",
        "run": lambda: solution([[0]]),
        "expected": 1,
    },
    {
        "description": "Blocked end: -1",
        "run": lambda: solution([[0, 0], [0, 1]]),
        "expected": -1,
    },
]
