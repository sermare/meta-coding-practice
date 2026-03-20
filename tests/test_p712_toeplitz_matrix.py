from problems.p712_toeplitz_matrix import solution

TEST_CASES = [
    {
        "description": "Valid Toeplitz: [[1,2,3,4],[5,1,2,3],[9,5,1,2]]",
        "run": lambda: solution([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]),
        "expected": True,
    },
    {
        "description": "Not Toeplitz: [[1,2],[2,2]]",
        "run": lambda: solution([[1, 2], [2, 2]]),
        "expected": False,
    },
    {
        "description": "Single element: [[1]]",
        "run": lambda: solution([[1]]),
        "expected": True,
    },
    {
        "description": "Single row: [[1,2,3]]",
        "run": lambda: solution([[1, 2, 3]]),
        "expected": True,
    },
    {
        "description": "All same values: [[5,5],[5,5]]",
        "run": lambda: solution([[5, 5], [5, 5]]),
        "expected": True,
    },
]
