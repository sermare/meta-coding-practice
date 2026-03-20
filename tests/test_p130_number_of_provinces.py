from problems.p130_number_of_provinces import solution

TEST_CASES = [
    {
        "description": "Two provinces",
        "run": lambda: solution([[1,1,0],[1,1,0],[0,0,1]]),
        "expected": 2,
    },
    {
        "description": "Three separate provinces",
        "run": lambda: solution([[1,0,0],[0,1,0],[0,0,1]]),
        "expected": 3,
    },
    {
        "description": "All connected, one province",
        "run": lambda: solution([[1,1,1],[1,1,1],[1,1,1]]),
        "expected": 1,
    },
    {
        "description": "Single city",
        "run": lambda: solution([[1]]),
        "expected": 1,
    },
    {
        "description": "Four cities, two provinces",
        "run": lambda: solution([[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]]),
        "expected": 2,
    },
]
