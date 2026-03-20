from problems.p260_largest_rectangle_in_histogram import solution

TEST_CASES = [
    {
        "description": "[2,1,5,6,2,3] -> 10",
        "run": lambda: solution([2, 1, 5, 6, 2, 3]),
        "expected": 10,
    },
    {
        "description": "[2,4] -> 4",
        "run": lambda: solution([2, 4]),
        "expected": 4,
    },
    {
        "description": "[1] -> 1",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "[2,2,2,2] -> 8",
        "run": lambda: solution([2, 2, 2, 2]),
        "expected": 8,
    },
    {
        "description": "[1,2,3,4,5] -> 9",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": 9,
    },
]
