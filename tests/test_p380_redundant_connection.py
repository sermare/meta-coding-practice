from problems.p380_redundant_connection import solution


TEST_CASES = [
    {
        "description": "Triangle: [2,3] is redundant",
        "run": lambda: solution([[1, 2], [1, 3], [2, 3]]),
        "expected": [2, 3],
    },
    {
        "description": "Cycle in larger graph",
        "run": lambda: solution([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]),
        "expected": [1, 4],
    },
    {
        "description": "Last edge creates cycle",
        "run": lambda: solution([[1, 2], [2, 3], [1, 3]]),
        "expected": [1, 3],
    },
    {
        "description": "Four-node cycle",
        "run": lambda: solution([[1, 2], [2, 3], [3, 4], [4, 1]]),
        "expected": [4, 1],
    },
]
