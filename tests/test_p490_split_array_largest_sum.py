from problems.p490_split_array_largest_sum import solution

TEST_CASES = [
    {
        "description": "[7,2,5,10,8] k=2 -> 18",
        "run": lambda: solution([7,2,5,10,8], 2),
        "expected": 18,
    },
    {
        "description": "[1,2,3,4,5] k=2 -> 9",
        "run": lambda: solution([1,2,3,4,5], 2),
        "expected": 9,
    },
    {
        "description": "[1,4,4] k=3 -> 4",
        "run": lambda: solution([1,4,4], 3),
        "expected": 4,
    },
    {
        "description": "Single split: [1,2,3] k=1 -> 6",
        "run": lambda: solution([1,2,3], 1),
        "expected": 6,
    },
    {
        "description": "Each element: [1,2,3] k=3 -> 3",
        "run": lambda: solution([1,2,3], 3),
        "expected": 3,
    },
]
