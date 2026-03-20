from problems.p648_number_of_islands import solution

TEST_CASES = [
    {
        "description": "Single island",
        "run": lambda: solution([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]),
        "expected": 1,
    },
    {
        "description": "Three islands",
        "run": lambda: solution([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]),
        "expected": 3,
    },
    {
        "description": "All water",
        "run": lambda: solution([["0", "0"], ["0", "0"]]),
        "expected": 0,
    },
    {
        "description": "All land",
        "run": lambda: solution([["1", "1"], ["1", "1"]]),
        "expected": 1,
    },
]
