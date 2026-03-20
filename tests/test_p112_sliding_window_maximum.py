from problems.p112_sliding_window_maximum import solution

TEST_CASES = [
    {
        "description": "Standard sliding window",
        "run": lambda: solution([1, 3, -1, -3, 5, 3, 6, 7], 3),
        "expected": [3, 3, 5, 5, 6, 7],
    },
    {
        "description": "Window size equals array",
        "run": lambda: solution([1, 2, 3], 3),
        "expected": [3],
    },
    {
        "description": "Window size 1",
        "run": lambda: solution([1, -1, 3, 2], 1),
        "expected": [1, -1, 3, 2],
    },
    {
        "description": "All same elements",
        "run": lambda: solution([5, 5, 5, 5], 2),
        "expected": [5, 5, 5],
    },
    {
        "description": "Decreasing array",
        "run": lambda: solution([9, 8, 7, 6, 5], 3),
        "expected": [9, 8, 7],
    },
]
