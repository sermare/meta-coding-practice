from problems.p042_maximal_square import solution

TEST_CASES = [
    {
        "description": "4x5 matrix with maximal square of area 4",
        "run": lambda: solution([
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]),
        "expected": 4,
    },
    {
        "description": "2x2 matrix with diagonal ones",
        "run": lambda: solution([["0", "1"], ["1", "0"]]),
        "expected": 1,
    },
    {
        "description": "Single cell with 0",
        "run": lambda: solution([["0"]]),
        "expected": 0,
    },
    {
        "description": "3x3 matrix all ones",
        "run": lambda: solution([
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"],
        ]),
        "expected": 9,
    },
    {
        "description": "Single cell with 1",
        "run": lambda: solution([["1"]]),
        "expected": 1,
    },
]
