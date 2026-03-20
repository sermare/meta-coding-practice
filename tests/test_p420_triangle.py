from problems.p420_triangle import solution

TEST_CASES = [
    {
        "description": "Basic triangle: [[2],[3,4],[6,5,7],[4,1,8,3]]",
        "run": lambda: solution([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]),
        "expected": 11,
    },
    {
        "description": "Single element: [[-10]]",
        "run": lambda: solution([[-10]]),
        "expected": -10,
    },
    {
        "description": "Two rows: [[-1],[2,3]]",
        "run": lambda: solution([[-1], [2, 3]]),
        "expected": 1,
    },
    {
        "description": "All ones: [[1],[1,1],[1,1,1]]",
        "run": lambda: solution([[1], [1, 1], [1, 1, 1]]),
        "expected": 3,
    },
    {
        "description": "Negative values: [[-1],[-2,-3]]",
        "run": lambda: solution([[-1], [-2, -3]]),
        "expected": -4,
    },
]
