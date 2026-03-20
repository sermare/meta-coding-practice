from problems.p547_set_matrix_zeroes import solution

TEST_CASES = [
    {
        "description": "Center zero",
        "run": lambda: solution([[1,1,1],[1,0,1],[1,1,1]]),
        "expected": [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
    },
    {
        "description": "Multiple zeroes",
        "run": lambda: solution([[0,1,2,0],[3,4,5,2],[1,3,1,5]]),
        "expected": [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
    },
    {
        "description": "No zeroes",
        "run": lambda: solution([[1,2],[3,4]]),
        "expected": [[1, 2], [3, 4]],
    },
    {
        "description": "All zeroes",
        "run": lambda: solution([[0,0],[0,0]]),
        "expected": [[0, 0], [0, 0]],
    },
    {
        "description": "Single element",
        "run": lambda: solution([[0]]),
        "expected": [[0]],
    },
]
