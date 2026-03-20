from problems.p149_trapping_rain_water import solution

TEST_CASES = [
    {
        "description": "Standard elevation map",
        "run": lambda: solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]),
        "expected": 6,
    },
    {
        "description": "V-shape",
        "run": lambda: solution([4, 2, 0, 3, 2, 5]),
        "expected": 9,
    },
    {
        "description": "No water (ascending)",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": 0,
    },
    {
        "description": "No water (descending)",
        "run": lambda: solution([4, 3, 2, 1]),
        "expected": 0,
    },
    {
        "description": "Flat surface",
        "run": lambda: solution([0, 0, 0]),
        "expected": 0,
    },
]
