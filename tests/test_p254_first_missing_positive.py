from problems.p254_first_missing_positive import solution

TEST_CASES = [
    {
        "description": "[3,4,-1,1] -> 2",
        "run": lambda: solution([3, 4, -1, 1]),
        "expected": 2,
    },
    {
        "description": "[1,2,0] -> 3",
        "run": lambda: solution([1, 2, 0]),
        "expected": 3,
    },
    {
        "description": "[7,8,9,11,12] -> 1",
        "run": lambda: solution([7, 8, 9, 11, 12]),
        "expected": 1,
    },
    {
        "description": "[1] -> 2",
        "run": lambda: solution([1]),
        "expected": 2,
    },
    {
        "description": "[1,2,3,4,5] -> 6",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": 6,
    },
]
