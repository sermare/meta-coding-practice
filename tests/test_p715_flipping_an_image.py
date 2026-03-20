from problems.p715_flipping_an_image import solution

TEST_CASES = [
    {
        "description": "3x3 matrix",
        "run": lambda: solution([[1, 1, 0], [1, 0, 1], [0, 0, 0]]),
        "expected": [[1, 0, 0], [0, 1, 0], [1, 1, 1]],
    },
    {
        "description": "4x4 matrix",
        "run": lambda: solution([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]),
        "expected": [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]],
    },
    {
        "description": "All zeros",
        "run": lambda: solution([[0, 0], [0, 0]]),
        "expected": [[1, 1], [1, 1]],
    },
    {
        "description": "All ones",
        "run": lambda: solution([[1, 1], [1, 1]]),
        "expected": [[0, 0], [0, 0]],
    },
]
