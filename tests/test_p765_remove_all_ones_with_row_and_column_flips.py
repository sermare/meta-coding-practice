from problems.p765_remove_all_ones_with_row_and_column_flips import solution

TEST_CASES = [
    {
        "description": "Possible: [[0,1,0],[1,0,1],[0,1,0]]",
        "run": lambda: solution([[0,1,0],[1,0,1],[0,1,0]]),
        "expected": True,
    },
    {
        "description": "Not possible: [[1,1,0],[0,0,0],[0,0,0]]",
        "run": lambda: solution([[1,1,0],[0,0,0],[0,0,0]]),
        "expected": True,
    },
    {
        "description": "Not possible: [[1,0,0],[0,1,0],[0,0,0]]",
        "run": lambda: solution([[1,0,0],[0,1,0],[0,0,0]]),
        "expected": False,
    },
    {
        "description": "All zeros",
        "run": lambda: solution([[0,0],[0,0]]),
        "expected": True,
    },
]
