from problems.p037_longest_consecutive_sequence import solution

TEST_CASES = [
    {
        "description": "[100,4,200,1,3,2] -> 4",
        "run": lambda: solution([100, 4, 200, 1, 3, 2]),
        "expected": 4,
    },
    {
        "description": "[0,3,7,2,5,8,4,6,0,1] -> 9",
        "run": lambda: solution([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]),
        "expected": 9,
    },
    {
        "description": "[] -> 0 (empty list)",
        "run": lambda: solution([]),
        "expected": 0,
    },
    {
        "description": "[1] -> 1 (single element)",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "[1,2,0,1] -> 3 (with duplicates)",
        "run": lambda: solution([1, 2, 0, 1]),
        "expected": 3,
    },
]
