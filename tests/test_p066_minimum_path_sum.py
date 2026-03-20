from problems.p066_minimum_path_sum import solution

TEST_CASES = [
    {
        "description": "3x3 grid: [[1,3,1],[1,5,1],[4,2,1]]",
        "run": lambda: solution([[1, 3, 1], [1, 5, 1], [4, 2, 1]]),
        "expected": 7,
    },
    {
        "description": "2x3 grid: [[1,2,3],[4,5,6]]",
        "run": lambda: solution([[1, 2, 3], [4, 5, 6]]),
        "expected": 12,
    },
    {
        "description": "1x1 grid: [[5]]",
        "run": lambda: solution([[5]]),
        "expected": 5,
    },
    {
        "description": "Single row: [[1,2,3]]",
        "run": lambda: solution([[1, 2, 3]]),
        "expected": 6,
    },
]
