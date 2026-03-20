from problems.p817_maximum_number_of_points_with_cost import solution

TEST_CASES = [
    {
        "description": "3x3 grid: [[1,2,3],[1,5,1],[3,1,1]]",
        "run": lambda: solution([[1,2,3],[1,5,1],[3,1,1]]),
        "expected": 9,
    },
    {
        "description": "Single row: [[5,3,1]]",
        "run": lambda: solution([[5,3,1]]),
        "expected": 5,
    },
    {
        "description": "1x1: [[7]]",
        "run": lambda: solution([[7]]),
        "expected": 7,
    },
    {
        "description": "Two rows: [[1,5],[5,1]]",
        "run": lambda: solution([[1,5],[5,1]]),
        "expected": 9,
    },
]
