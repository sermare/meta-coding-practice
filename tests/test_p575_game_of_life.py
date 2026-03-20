from problems.p575_game_of_life import solution

TEST_CASES = [
    {
        "description": "Standard 4x4 board",
        "run": lambda: solution([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]),
        "expected": [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
    },
    {
        "description": "2x2 board",
        "run": lambda: solution([[1, 1], [1, 0]]),
        "expected": [[1, 1], [1, 1]],
    },
    {
        "description": "All dead",
        "run": lambda: solution([[0, 0], [0, 0]]),
        "expected": [[0, 0], [0, 0]],
    },
    {
        "description": "All alive 2x2",
        "run": lambda: solution([[1, 1], [1, 1]]),
        "expected": [[1, 1], [1, 1]],
    },
]
