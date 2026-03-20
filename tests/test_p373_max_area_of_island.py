from problems.p373_max_area_of_island import solution


TEST_CASES = [
    {
        "description": "Multiple islands, max area 6",
        "run": lambda: solution([
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]),
        "expected": 6,
    },
    {
        "description": "No islands",
        "run": lambda: solution([[0, 0, 0, 0, 0, 0, 0, 0]]),
        "expected": 0,
    },
    {
        "description": "Single cell island",
        "run": lambda: solution([[1]]),
        "expected": 1,
    },
    {
        "description": "Entire grid is one island",
        "run": lambda: solution([[1, 1], [1, 1]]),
        "expected": 4,
    },
]
