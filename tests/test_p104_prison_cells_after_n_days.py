from problems.p104_prison_cells_after_n_days import solution

TEST_CASES = [
    {
        "description": "7 days simulation",
        "run": lambda: solution([0, 1, 0, 1, 1, 0, 0, 1], 7),
        "expected": [0, 0, 1, 1, 0, 0, 0, 0],
    },
    {
        "description": "1000 days (cycle detection needed)",
        "run": lambda: solution([1, 0, 0, 1, 0, 0, 1, 0], 1000000000),
        "expected": [0, 0, 1, 1, 1, 1, 1, 0],
    },
    {
        "description": "Single day",
        "run": lambda: solution([0, 0, 0, 0, 0, 0, 0, 0], 1),
        "expected": [0, 1, 1, 1, 1, 1, 1, 0],
    },
    {
        "description": "All occupied after 1 day",
        "run": lambda: solution([1, 1, 1, 1, 1, 1, 1, 1], 1),
        "expected": [0, 1, 1, 1, 1, 1, 1, 0],
    },
]
