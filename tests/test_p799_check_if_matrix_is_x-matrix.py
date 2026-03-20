from problems.p799_check_if_matrix_is_x-matrix import solution

TEST_CASES = [
    {
        "description": "Valid X-Matrix",
        "run": lambda: solution([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]),
        "expected": True,
    },
    {
        "description": "Invalid: non-zero off diagonal",
        "run": lambda: solution([[5,7,0],[0,3,1],[0,5,0]]),
        "expected": False,
    },
    {
        "description": "Invalid: zero on diagonal",
        "run": lambda: solution([[0,0],[0,1]]),
        "expected": False,
    },
    {
        "description": "1x1 matrix: [[5]]",
        "run": lambda: solution([[5]]),
        "expected": True,
    },
]
