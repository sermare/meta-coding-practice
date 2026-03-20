from problems.p119_maximum_points_you_can_obtain_from_cards import solution

TEST_CASES = [
    {
        "description": "Take from both ends",
        "run": lambda: solution([1, 2, 3, 4, 5, 6, 1], 3),
        "expected": 12,
    },
    {
        "description": "All same values",
        "run": lambda: solution([2, 2, 2], 2),
        "expected": 4,
    },
    {
        "description": "Take all cards",
        "run": lambda: solution([9, 7, 7, 9, 7, 7, 9], 7),
        "expected": 55,
    },
    {
        "description": "Best from left side",
        "run": lambda: solution([100, 40, 17, 9, 73, 75], 3),
        "expected": 248,
    },
    {
        "description": "Single card",
        "run": lambda: solution([5], 1),
        "expected": 5,
    },
]
