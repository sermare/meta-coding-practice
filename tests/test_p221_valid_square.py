from problems.p221_valid_square import solution

TEST_CASES = [
    {
        "description": "Unit square",
        "run": lambda: solution([0, 0], [1, 1], [1, 0], [0, 1]),
        "expected": True,
    },
    {
        "description": "Not a square (rectangle)",
        "run": lambda: solution([0, 0], [2, 0], [2, 1], [0, 1]),
        "expected": False,
    },
    {
        "description": "Degenerate (all same point)",
        "run": lambda: solution([0, 0], [0, 0], [0, 0], [0, 0]),
        "expected": False,
    },
    {
        "description": "Rotated square",
        "run": lambda: solution([1, 0], [0, 1], [-1, 0], [0, -1]),
        "expected": True,
    },
]
