from problems.p230_my_calendar_i import solution

TEST_CASES = [
    {
        "description": "Standard bookings",
        "run": lambda: solution([[10, 20], [15, 25], [20, 30]]),
        "expected": [True, False, True],
    },
    {
        "description": "No overlaps",
        "run": lambda: solution([[1, 5], [5, 10], [10, 15]]),
        "expected": [True, True, True],
    },
    {
        "description": "All overlapping",
        "run": lambda: solution([[1, 10], [2, 5], [3, 8]]),
        "expected": [True, False, False],
    },
    {
        "description": "Single booking",
        "run": lambda: solution([[0, 100]]),
        "expected": [True],
    },
]
