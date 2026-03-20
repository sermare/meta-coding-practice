from problems.p472_largest_rectangle_in_histogram import solution

TEST_CASES = [
    {
        "description": "Standard: [2,1,5,6,2,3] -> 10",
        "run": lambda: solution([2,1,5,6,2,3]),
        "expected": 10,
    },
    {
        "description": "Two bars: [2,4] -> 4",
        "run": lambda: solution([2,4]),
        "expected": 4,
    },
    {
        "description": "Single bar: [5] -> 5",
        "run": lambda: solution([5]),
        "expected": 5,
    },
    {
        "description": "All same: [3,3,3,3] -> 12",
        "run": lambda: solution([3,3,3,3]),
        "expected": 12,
    },
    {
        "description": "Increasing: [1,2,3,4] -> 6",
        "run": lambda: solution([1,2,3,4]),
        "expected": 6,
    },
]
