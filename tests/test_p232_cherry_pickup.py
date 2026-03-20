from problems.p232_cherry_pickup import solution

TEST_CASES = [
    {
        "description": "Standard: [[0,1,-1],[1,0,-1],[1,1,1]]",
        "run": lambda: solution([[0, 1, -1], [1, 0, -1], [1, 1, 1]]),
        "expected": 5,
    },
    {
        "description": "All thorns block: [[1,1,-1],[-1,-1,1],[1,1,1]]",
        "run": lambda: solution([[1, 1, -1], [-1, -1, 1], [1, 1, 1]]),
        "expected": 0,
    },
    {
        "description": "Single cell: [[1]]",
        "run": lambda: solution([[1]]),
        "expected": 1,
    },
    {
        "description": "Empty single cell: [[0]]",
        "run": lambda: solution([[0]]),
        "expected": 0,
    },
]
