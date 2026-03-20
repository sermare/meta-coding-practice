from problems.p843_set_matrix_zeroes import solution

TEST_CASES = [
    {
        "description": "Center zero: [[1,1,1],[1,0,1],[1,1,1]]",
        "run": lambda: solution([[1,1,1],[1,0,1],[1,1,1]]),
        "expected": [[1,0,1],[0,0,0],[1,0,1]],
    },
    {
        "description": "Corner zero: [[0,1,2,0],[3,4,5,2],[1,3,1,5]]",
        "run": lambda: solution([[0,1,2,0],[3,4,5,2],[1,3,1,5]]),
        "expected": [[0,0,0,0],[0,4,5,0],[0,3,1,0]],
    },
    {
        "description": "No zeros: [[1,2],[3,4]]",
        "run": lambda: solution([[1,2],[3,4]]),
        "expected": [[1,2],[3,4]],
    },
    {
        "description": "All zeros: [[0,0],[0,0]]",
        "run": lambda: solution([[0,0],[0,0]]),
        "expected": [[0,0],[0,0]],
    },
]
