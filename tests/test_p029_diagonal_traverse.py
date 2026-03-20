from problems.p029_diagonal_traverse import solution

TEST_CASES = [
    {
        "description": "3x3 matrix diagonal traversal",
        "run": lambda: solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        "expected": [1, 2, 4, 7, 5, 3, 6, 8, 9],
    },
    {
        "description": "2x2 matrix diagonal traversal",
        "run": lambda: solution([[1, 2], [3, 4]]),
        "expected": [1, 2, 3, 4],
    },
    {
        "description": "1x1 matrix returns single element",
        "run": lambda: solution([[1]]),
        "expected": [1],
    },
    {
        "description": "1x4 single-row matrix",
        "run": lambda: solution([[1, 2, 3, 4]]),
        "expected": [1, 2, 3, 4],
    },
]
