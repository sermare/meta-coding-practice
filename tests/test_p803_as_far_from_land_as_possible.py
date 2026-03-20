from problems.p803_as_far_from_land_as_possible import solution

TEST_CASES = [
    {
        "description": "Center is farthest: [[1,0,1],[0,0,0],[1,0,1]]",
        "run": lambda: solution([[1,0,1],[0,0,0],[1,0,1]]),
        "expected": 2,
    },
    {
        "description": "Corner land: [[1,0,0],[0,0,0],[0,0,0]]",
        "run": lambda: solution([[1,0,0],[0,0,0],[0,0,0]]),
        "expected": 4,
    },
    {
        "description": "All land: [[1,1],[1,1]]",
        "run": lambda: solution([[1,1],[1,1]]),
        "expected": -1,
    },
    {
        "description": "All water: [[0,0],[0,0]]",
        "run": lambda: solution([[0,0],[0,0]]),
        "expected": -1,
    },
]
