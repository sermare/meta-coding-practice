from problems.p473_maximal_rectangle import solution

TEST_CASES = [
    {
        "description": "Standard 4x5 matrix -> 6",
        "run": lambda: solution([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]),
        "expected": 6,
    },
    {
        "description": "Single zero: [["0"]] -> 0",
        "run": lambda: solution([["0"]]),
        "expected": 0,
    },
    {
        "description": "Single one: [["1"]] -> 1",
        "run": lambda: solution([["1"]]),
        "expected": 1,
    },
    {
        "description": "All ones 2x2 -> 4",
        "run": lambda: solution([["1","1"],["1","1"]]),
        "expected": 4,
    },
    {
        "description": "Row of ones -> 3",
        "run": lambda: solution([["1","1","1"]]),
        "expected": 3,
    },
]
