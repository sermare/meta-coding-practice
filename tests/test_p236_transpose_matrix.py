from problems.p236_transpose_matrix import solution

TEST_CASES = [
    {
        "description": "Square: 3x3",
        "run": lambda: solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        "expected": [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
    },
    {
        "description": "Rectangular: 2x3",
        "run": lambda: solution([[1, 2, 3], [4, 5, 6]]),
        "expected": [[1, 4], [2, 5], [3, 6]],
    },
    {
        "description": "Single row: [[1,2,3]]",
        "run": lambda: solution([[1, 2, 3]]),
        "expected": [[1], [2], [3]],
    },
    {
        "description": "Single element: [[1]]",
        "run": lambda: solution([[1]]),
        "expected": [[1]],
    },
]
