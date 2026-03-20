from problems.p217_island_perimeter import solution

TEST_CASES = [
    {
        "description": "Standard island",
        "run": lambda: solution([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]),
        "expected": 16,
    },
    {
        "description": "Single cell: [[1]]",
        "run": lambda: solution([[1]]),
        "expected": 4,
    },
    {
        "description": "Single row: [[1,1]]",
        "run": lambda: solution([[1, 1]]),
        "expected": 6,
    },
    {
        "description": "L shape: [[1,0],[1,1]]",
        "run": lambda: solution([[1, 0], [1, 1]]),
        "expected": 8,
    },
]
