from problems.p579_paint_house import solution

TEST_CASES = [
    {
        "description": "Three houses: 10",
        "run": lambda: solution([[17, 2, 17], [16, 16, 5], [14, 3, 19]]),
        "expected": 10,
    },
    {
        "description": "Single house: 2",
        "run": lambda: solution([[7, 6, 2]]),
        "expected": 2,
    },
    {
        "description": "Two houses",
        "run": lambda: solution([[1, 2, 3], [3, 2, 1]]),
        "expected": 2,
    },
    {
        "description": "Equal costs",
        "run": lambda: solution([[5, 5, 5], [5, 5, 5]]),
        "expected": 10,
    },
]
