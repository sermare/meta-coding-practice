from problems.p291_total_hamming_distance import solution

TEST_CASES = [
    {
        "description": "[4,14,2] -> 6",
        "run": lambda: solution([4, 14, 2]),
        "expected": 6,
    },
    {
        "description": "[4,14,4] -> 4",
        "run": lambda: solution([4, 14, 4]),
        "expected": 4,
    },
    {
        "description": "[0] -> 0",
        "run": lambda: solution([0]),
        "expected": 0,
    },
    {
        "description": "[0,0,0] -> 0",
        "run": lambda: solution([0, 0, 0]),
        "expected": 0,
    },
    {
        "description": "[1,2,3] -> 4",
        "run": lambda: solution([1, 2, 3]),
        "expected": 4,
    },
]
