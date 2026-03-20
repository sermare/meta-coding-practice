from problems.p198_sliding_window_median import solution

TEST_CASES = [
    {
        "description": "k=3 basic",
        "run": lambda: solution([1,3,-1,-3,5,3,6,7], 3),
        "expected": [1.0,-1.0,-1.0,3.0,5.0,6.0],
    },
    {
        "description": "k=1 each element is median",
        "run": lambda: solution([1, 2, 3], 1),
        "expected": [1.0, 2.0, 3.0],
    },
    {
        "description": "k equals array length",
        "run": lambda: solution([1, 2, 3], 3),
        "expected": [2.0],
    },
    {
        "description": "k=2 even window",
        "run": lambda: solution([1, 3, 5], 2),
        "expected": [2.0, 4.0],
    },
]
