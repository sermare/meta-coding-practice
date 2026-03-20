from problems.p008_number_of_islands import solution

TEST_CASES = [
    {
        "description": "Single island",
        "run": lambda: solution([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]),
        "expected": 1,
    },
    {
        "description": "Three islands",
        "run": lambda: solution([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]),
        "expected": 3,
    },
    {
        "description": "Single cell land: [['1']]",
        "run": lambda: solution([["1"]]),
        "expected": 1,
    },
    {
        "description": "Single cell water: [['0']]",
        "run": lambda: solution([["0"]]),
        "expected": 0,
    },
    {
        "description": "Checkerboard pattern: 5 islands",
        "run": lambda: solution([
            ["1", "0", "1"],
            ["0", "1", "0"],
            ["1", "0", "1"],
        ]),
        "expected": 5,
    },
]
