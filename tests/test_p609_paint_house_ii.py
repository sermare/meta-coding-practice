from problems.p609_paint_house_ii import solution

TEST_CASES = [
    {
        "description": "Two houses, two colors: [[1,5,3],[2,9,4]]",
        "run": lambda: solution([[1, 5, 3], [2, 9, 4]]),
        "expected": 5,
    },
    {
        "description": "Two houses, two colors: [[1,3],[2,4]]",
        "run": lambda: solution([[1, 3], [2, 4]]),
        "expected": 5,
    },
    {
        "description": "Single house: [[5,1,3]]",
        "run": lambda: solution([[5, 1, 3]]),
        "expected": 1,
    },
    {
        "description": "Empty costs",
        "run": lambda: solution([]),
        "expected": 0,
    },
]
