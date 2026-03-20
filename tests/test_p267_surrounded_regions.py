from problems.p267_surrounded_regions import solution

TEST_CASES = [
    {
        "description": "Standard surrounded regions",
        "run": lambda: solution([
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
        ]),
        "expected": [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
        ],
    },
    {
        "description": "All X board",
        "run": lambda: solution([["X"]]),
        "expected": [["X"]],
    },
    {
        "description": "Single O",
        "run": lambda: solution([["O"]]),
        "expected": [["O"]],
    },
    {
        "description": "Border O not captured",
        "run": lambda: solution([
            ["O","X"],
            ["X","O"]
        ]),
        "expected": [
            ["O","X"],
            ["X","O"]
        ],
    },
    {
        "description": "All O board",
        "run": lambda: solution([
            ["O","O"],
            ["O","O"]
        ]),
        "expected": [
            ["O","O"],
            ["O","O"]
        ],
    },
]
