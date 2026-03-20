from problems.p566_maximum_points_on_a_line import solution

TEST_CASES = [
    {
        "description": "Three collinear points",
        "run": lambda: solution([[1, 1], [2, 2], [3, 3]]),
        "expected": 3,
    },
    {
        "description": "Six points, max 4",
        "run": lambda: solution([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]),
        "expected": 4,
    },
    {
        "description": "Single point",
        "run": lambda: solution([[0, 0]]),
        "expected": 1,
    },
    {
        "description": "Two points",
        "run": lambda: solution([[1, 1], [2, 2]]),
        "expected": 2,
    },
    {
        "description": "Vertical line",
        "run": lambda: solution([[0, 0], [0, 1], [0, 2], [1, 1]]),
        "expected": 3,
    },
]
