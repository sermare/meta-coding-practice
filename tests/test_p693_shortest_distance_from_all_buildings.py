from problems.p693_shortest_distance_from_all_buildings import solution

TEST_CASES = [
    {
        "description": "Standard 3x5 grid",
        "run": lambda: solution([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]),
        "expected": 7,
    },
    {
        "description": "Impossible: buildings blocked",
        "run": lambda: solution([[1, 2, 0], [2, 2, 0], [0, 0, 1]]),
        "expected": -1,
    },
    {
        "description": "Single building",
        "run": lambda: solution([[1, 0]]),
        "expected": 1,
    },
    {
        "description": "No empty land",
        "run": lambda: solution([[1]]),
        "expected": -1,
    },
]
