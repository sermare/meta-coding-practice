from problems.p491_find_peak_element import solution

TEST_CASES = [
    {
        "description": "Peak at index 2: [1,2,3,1]",
        "run": lambda: solution([1,2,3,1]) in [2],
        "expected": True,
    },
    {
        "description": "Multiple peaks: [1,2,1,3,5,6,4]",
        "run": lambda: solution([1,2,1,3,5,6,4]) in [1, 5],
        "expected": True,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": 0,
    },
    {
        "description": "Increasing: [1,2,3] -> peak at end",
        "run": lambda: solution([1,2,3]),
        "expected": 2,
    },
    {
        "description": "Decreasing: [3,2,1] -> peak at start",
        "run": lambda: solution([3,2,1]),
        "expected": 0,
    },
]
