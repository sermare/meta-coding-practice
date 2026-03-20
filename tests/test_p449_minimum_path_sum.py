from problems.p449_minimum_path_sum import solution

TEST_CASES = [
    {
        "description": "Basic: [[1,3,1],[1,5,1],[4,2,1]]",
        "run": lambda: solution([[1, 3, 1], [1, 5, 1], [4, 2, 1]]),
        "expected": 7,
    },
    {
        "description": "Single row: [[1,2,3]]",
        "run": lambda: solution([[1, 2, 3]]),
        "expected": 6,
    },
    {
        "description": "Single column: [[1],[2],[3]]",
        "run": lambda: solution([[1], [2], [3]]),
        "expected": 6,
    },
    {
        "description": "Single cell: [[5]]",
        "run": lambda: solution([[5]]),
        "expected": 5,
    },
    {
        "description": "2x2 grid: [[1,2],[3,4]]",
        "run": lambda: solution([[1, 2], [3, 4]]),
        "expected": 7,
    },
]
