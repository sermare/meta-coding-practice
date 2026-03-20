from problems.p598_merge_intervals import solution

TEST_CASES = [
    {
        "description": "Overlapping: [[1,3],[2,6],[8,10],[15,18]]",
        "run": lambda: solution([[1, 3], [2, 6], [8, 10], [15, 18]]),
        "expected": [[1, 6], [8, 10], [15, 18]],
    },
    {
        "description": "Touching: [[1,4],[4,5]]",
        "run": lambda: solution([[1, 4], [4, 5]]),
        "expected": [[1, 5]],
    },
    {
        "description": "No overlap: [[1,2],[3,4]]",
        "run": lambda: solution([[1, 2], [3, 4]]),
        "expected": [[1, 2], [3, 4]],
    },
    {
        "description": "Single interval",
        "run": lambda: solution([[1, 5]]),
        "expected": [[1, 5]],
    },
    {
        "description": "All merge: [[1,4],[2,3],[3,6]]",
        "run": lambda: solution([[1, 4], [2, 3], [3, 6]]),
        "expected": [[1, 6]],
    },
]
