from problems.p421_minimum_falling_path_sum import solution

TEST_CASES = [
    {
        "description": "Basic: [[2,1,3],[6,5,4],[7,8,9]]",
        "run": lambda: solution([[2, 1, 3], [6, 5, 4], [7, 8, 9]]),
        "expected": 13,
    },
    {
        "description": "Negative values: [[-19,57],[-40,-5]]",
        "run": lambda: solution([[-19, 57], [-40, -5]]),
        "expected": -59,
    },
    {
        "description": "Single element: [[5]]",
        "run": lambda: solution([[5]]),
        "expected": 5,
    },
    {
        "description": "All same: [[1,1],[1,1]]",
        "run": lambda: solution([[1, 1], [1, 1]]),
        "expected": 2,
    },
    {
        "description": "Larger: [[1,2,3],[4,5,6],[7,8,9]]",
        "run": lambda: solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        "expected": 12,
    },
]
