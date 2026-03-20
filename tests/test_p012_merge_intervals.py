from problems.p012_merge_intervals import solution


TEST_CASES = [
    {
        "description": "Multiple overlapping intervals",
        "run": lambda: solution([[1, 3], [2, 6], [8, 10], [15, 18]]),
        "expected": [[1, 6], [8, 10], [15, 18]],
    },
    {
        "description": "Touching intervals merge",
        "run": lambda: solution([[1, 4], [4, 5]]),
        "expected": [[1, 5]],
    },
    {
        "description": "Unsorted intervals with overlap",
        "run": lambda: solution([[1, 4], [0, 4]]),
        "expected": [[0, 4]],
    },
    {
        "description": "One interval contained within another",
        "run": lambda: solution([[1, 4], [2, 3]]),
        "expected": [[1, 4]],
    },
    {
        "description": "Three intervals merging into one",
        "run": lambda: solution([[1, 4], [0, 2], [3, 5]]),
        "expected": [[0, 5]],
    },
]
