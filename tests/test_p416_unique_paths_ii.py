from problems.p416_unique_paths_ii import solution

TEST_CASES = [
    {
        "description": "3x3 with obstacle: [[0,0,0],[0,1,0],[0,0,0]]",
        "run": lambda: solution([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
        "expected": 2,
    },
    {
        "description": "2x2 with obstacle: [[0,1],[0,0]]",
        "run": lambda: solution([[0, 1], [0, 0]]),
        "expected": 1,
    },
    {
        "description": "Blocked start: [[1,0]]",
        "run": lambda: solution([[1, 0]]),
        "expected": 0,
    },
    {
        "description": "No obstacles: [[0,0],[0,0]]",
        "run": lambda: solution([[0, 0], [0, 0]]),
        "expected": 2,
    },
    {
        "description": "Blocked end: [[0,0],[0,1]]",
        "run": lambda: solution([[0, 0], [0, 1]]),
        "expected": 0,
    },
]
