from problems.p258_spiral_matrix import solution

TEST_CASES = [
    {
        "description": "3x3 matrix",
        "run": lambda: solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5],
    },
    {
        "description": "3x4 matrix",
        "run": lambda: solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
        "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
    },
    {
        "description": "1x1 matrix",
        "run": lambda: solution([[1]]),
        "expected": [1],
    },
    {
        "description": "1x4 single row",
        "run": lambda: solution([[1, 2, 3, 4]]),
        "expected": [1, 2, 3, 4],
    },
    {
        "description": "4x1 single column",
        "run": lambda: solution([[1], [2], [3], [4]]),
        "expected": [1, 2, 3, 4],
    },
]
