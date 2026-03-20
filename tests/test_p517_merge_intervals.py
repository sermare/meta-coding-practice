from problems.p517_merge_intervals import solution

TEST_CASES = [
    {
        "description": "Overlapping intervals",
        "run": lambda: solution([[1,3],[2,6],[8,10],[15,18]]),
        "expected": [[1, 6], [8, 10], [15, 18]],
    },
    {
        "description": "All overlap",
        "run": lambda: solution([[1,4],[4,5]]),
        "expected": [[1, 5]],
    },
    {
        "description": "No overlap",
        "run": lambda: solution([[1,2],[3,4],[5,6]]),
        "expected": [[1, 2], [3, 4], [5, 6]],
    },
    {
        "description": "Single interval",
        "run": lambda: solution([[1,5]]),
        "expected": [[1, 5]],
    },
    {
        "description": "Unsorted input",
        "run": lambda: solution([[3,4],[1,2],[2,3]]),
        "expected": [[1, 4]],
    },
]
