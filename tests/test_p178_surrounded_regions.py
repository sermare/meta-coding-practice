from problems.p178_surrounded_regions import solution

TEST_CASES = [
    {
        "description": "Standard surrounded region",
        "run": lambda: solution([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]),
        "expected": [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]],
    },
    {
        "description": "Single X",
        "run": lambda: solution([["X"]]),
        "expected": [["X"]],
    },
    {
        "description": "All O (border) stays O",
        "run": lambda: solution([["O","O"],["O","O"]]),
        "expected": [["O","O"],["O","O"]],
    },
    {
        "description": "No O's",
        "run": lambda: solution([["X","X"],["X","X"]]),
        "expected": [["X","X"],["X","X"]],
    },
]
