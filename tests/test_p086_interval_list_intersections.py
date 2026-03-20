from problems.p086_interval_list_intersections import solution

TEST_CASES = [
    {
        "description": "Standard intersection",
        "run": lambda: solution([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]),
        "expected": [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
    },
    {
        "description": "One empty list",
        "run": lambda: solution([[1, 3], [5, 9]], []),
        "expected": [],
    },
    {
        "description": "No overlap",
        "run": lambda: solution([[1, 2]], [[3, 4]]),
        "expected": [],
    },
    {
        "description": "Full overlap: same intervals",
        "run": lambda: solution([[1, 5]], [[1, 5]]),
        "expected": [[1, 5]],
    },
]
