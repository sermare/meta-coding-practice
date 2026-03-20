from problems.p312_candy import solution

TEST_CASES = [
    {
        "description": "Basic: [1,0,2] -> 5",
        "run": lambda: solution([1, 0, 2]),
        "expected": 5,
    },
    {
        "description": "Descending: [1,2,2] -> 4",
        "run": lambda: solution([1, 2, 2]),
        "expected": 4,
    },
    {
        "description": "All same: [1,1,1] -> 3",
        "run": lambda: solution([1, 1, 1]),
        "expected": 3,
    },
    {
        "description": "Strictly increasing: [1,2,3] -> 6",
        "run": lambda: solution([1, 2, 3]),
        "expected": 6,
    },
    {
        "description": "Single child: [5] -> 1",
        "run": lambda: solution([5]),
        "expected": 1,
    },
]
