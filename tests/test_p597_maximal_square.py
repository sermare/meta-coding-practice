from problems.p597_maximal_square import solution

TEST_CASES = [
    {
        "description": "Standard: 2x2 square found -> area 4",
        "run": lambda: solution([["1", "0", "1", "0", "0"],
                                 ["1", "0", "1", "1", "1"],
                                 ["1", "1", "1", "1", "1"],
                                 ["1", "0", "0", "1", "0"]]),
        "expected": 4,
    },
    {
        "description": "Diagonal ones: area 1",
        "run": lambda: solution([["0", "1"], ["1", "0"]]),
        "expected": 1,
    },
    {
        "description": "All zeros: area 0",
        "run": lambda: solution([["0"]]),
        "expected": 0,
    },
    {
        "description": "All ones 2x2: area 4",
        "run": lambda: solution([["1", "1"], ["1", "1"]]),
        "expected": 4,
    },
]
