from problems.p810_path_with_minimum_effort import solution

TEST_CASES = [
    {
        "description": "3x3 grid: [[1,2,2],[3,8,2],[5,3,5]]",
        "run": lambda: solution([[1,2,2],[3,8,2],[5,3,5]]),
        "expected": 2,
    },
    {
        "description": "Flat grid: [[1,1,1],[1,1,1]]",
        "run": lambda: solution([[1,1,1],[1,1,1]]),
        "expected": 0,
    },
    {
        "description": "Single cell: [[5]]",
        "run": lambda: solution([[5]]),
        "expected": 0,
    },
    {
        "description": "Steep path: [[1,10,6,7,9,10,4,9]]",
        "run": lambda: solution([[1,10,6,7,9,10,4,9]]),
        "expected": 9,
    },
]
