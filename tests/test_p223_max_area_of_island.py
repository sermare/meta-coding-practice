from problems.p223_max_area_of_island import solution

TEST_CASES = [
    {
        "description": "Standard grid",
        "run": lambda: solution([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0]]),
        "expected": 3,
    },
    {
        "description": "No islands: all zeros",
        "run": lambda: solution([[0, 0, 0], [0, 0, 0]]),
        "expected": 0,
    },
    {
        "description": "Single cell island",
        "run": lambda: solution([[0, 1, 0], [0, 0, 0]]),
        "expected": 1,
    },
    {
        "description": "Entire grid is island",
        "run": lambda: solution([[1, 1], [1, 1]]),
        "expected": 4,
    },
    {
        "description": "Two islands: pick larger",
        "run": lambda: solution([[1, 0, 1, 1], [1, 0, 1, 0]]),
        "expected": 3,
    },
]
