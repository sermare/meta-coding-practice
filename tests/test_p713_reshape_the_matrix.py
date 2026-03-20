from problems.p713_reshape_the_matrix import solution

TEST_CASES = [
    {
        "description": "Reshape 2x2 to 1x4",
        "run": lambda: solution([[1, 2], [3, 4]], 1, 4),
        "expected": [[1, 2, 3, 4]],
    },
    {
        "description": "Reshape 2x2 to 4x1",
        "run": lambda: solution([[1, 2], [3, 4]], 4, 1),
        "expected": [[1], [2], [3], [4]],
    },
    {
        "description": "Invalid reshape returns original",
        "run": lambda: solution([[1, 2], [3, 4]], 2, 4),
        "expected": [[1, 2], [3, 4]],
    },
    {
        "description": "Same shape: 2x2 to 2x2",
        "run": lambda: solution([[1, 2], [3, 4]], 2, 2),
        "expected": [[1, 2], [3, 4]],
    },
]
