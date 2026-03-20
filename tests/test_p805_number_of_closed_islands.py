from problems.p805_number_of_closed_islands import solution

TEST_CASES = [
    {
        "description": "Two closed islands",
        "run": lambda: solution([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]),
        "expected": 2,
    },
    {
        "description": "No closed islands: [[0,0],[0,0]]",
        "run": lambda: solution([[0,0],[0,0]]),
        "expected": 0,
    },
    {
        "description": "Single closed island: [[1,1,1],[1,0,1],[1,1,1]]",
        "run": lambda: solution([[1,1,1],[1,0,1],[1,1,1]]),
        "expected": 1,
    },
    {
        "description": "All water: [[1,1],[1,1]]",
        "run": lambda: solution([[1,1],[1,1]]),
        "expected": 0,
    },
]
