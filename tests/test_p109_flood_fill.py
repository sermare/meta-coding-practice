from problems.p109_flood_fill import solution

TEST_CASES = [
    {
        "description": "Standard flood fill",
        "run": lambda: solution([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2),
        "expected": [[2,2,2],[2,2,0],[2,0,1]],
    },
    {
        "description": "Same color, no change",
        "run": lambda: solution([[0,0,0],[0,0,0]], 0, 0, 0),
        "expected": [[0,0,0],[0,0,0]],
    },
    {
        "description": "Single pixel",
        "run": lambda: solution([[1]], 0, 0, 3),
        "expected": [[3]],
    },
    {
        "description": "Corner fill",
        "run": lambda: solution([[0,0,0],[0,1,1]], 1, 1, 2),
        "expected": [[0,0,0],[0,2,2]],
    },
    {
        "description": "Full grid same color",
        "run": lambda: solution([[1,1],[1,1]], 0, 0, 5),
        "expected": [[5,5],[5,5]],
    },
]
