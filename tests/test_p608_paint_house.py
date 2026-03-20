from problems.p608_paint_house import solution

TEST_CASES = [
    {
        "description": "Three houses: [[17,2,17],[16,16,5],[14,3,19]]",
        "run": lambda: solution([[17, 2, 17], [16, 16, 5], [14, 3, 19]]),
        "expected": 10,
    },
    {
        "description": "Single house: [[7,6,2]]",
        "run": lambda: solution([[7, 6, 2]]),
        "expected": 2,
    },
    {
        "description": "Two houses: [[1,2,3],[1,2,3]]",
        "run": lambda: solution([[1, 2, 3], [1, 2, 3]]),
        "expected": 3,
    },
    {
        "description": "Empty costs",
        "run": lambda: solution([]),
        "expected": 0,
    },
]
