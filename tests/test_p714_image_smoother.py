from problems.p714_image_smoother import solution

TEST_CASES = [
    {
        "description": "3x3 matrix all ones with zero center",
        "run": lambda: solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
        "expected": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    },
    {
        "description": "3x3 increasing values",
        "run": lambda: solution([[100, 200, 100], [200, 50, 200], [100, 200, 100]]),
        "expected": [[137, 141, 137], [141, 138, 141], [137, 141, 137]],
    },
    {
        "description": "Single cell",
        "run": lambda: solution([[5]]),
        "expected": [[5]],
    },
    {
        "description": "Single row",
        "run": lambda: solution([[1, 2, 3]]),
        "expected": [[1, 2, 2]],
    },
]
