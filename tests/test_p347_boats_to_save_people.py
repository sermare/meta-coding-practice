from problems.p347_boats_to_save_people import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2] limit=3 -> 1",
        "run": lambda: solution([1, 2], 3),
        "expected": 1,
    },
    {
        "description": "Multiple boats: [3,2,2,1] limit=3 -> 3",
        "run": lambda: solution([3, 2, 2, 1], 3),
        "expected": 3,
    },
    {
        "description": "All heavy: [3,5,3,4] limit=5 -> 4",
        "run": lambda: solution([3, 5, 3, 4], 5),
        "expected": 4,
    },
    {
        "description": "All fit in pairs: [1,1,1,1] limit=2 -> 2",
        "run": lambda: solution([1, 1, 1, 1], 2),
        "expected": 2,
    },
]
