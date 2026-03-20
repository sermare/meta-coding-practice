from problems.p041_maximal_rectangle import solution

TEST_CASES = [
    {
        "description": "4x5 matrix with maximal rectangle of area 6",
        "run": lambda: solution([
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]),
        "expected": 6,
    },
    {
        "description": "Single cell with 0",
        "run": lambda: solution([["0"]]),
        "expected": 0,
    },
    {
        "description": "Single cell with 1",
        "run": lambda: solution([["1"]]),
        "expected": 1,
    },
    {
        "description": "Single row of zeros",
        "run": lambda: solution([["0", "0"]]),
        "expected": 0,
    },
    {
        "description": "2x2 matrix all ones",
        "run": lambda: solution([["1", "1"], ["1", "1"]]),
        "expected": 4,
    },
]
