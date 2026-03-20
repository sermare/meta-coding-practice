from problems.p667_two_sum_less_than_k import solution

TEST_CASES = [
    {
        "description": "Basic case: max sum < 60",
        "run": lambda: solution([34, 23, 1, 24, 75, 33, 54, 8], 60),
        "expected": 58,
    },
    {
        "description": "No valid pair",
        "run": lambda: solution([10, 20, 30], 20),
        "expected": -1,
    },
    {
        "description": "All pairs valid: [1,2,3] k=10",
        "run": lambda: solution([1, 2, 3], 10),
        "expected": 5,
    },
    {
        "description": "Two elements: [1,1] k=3",
        "run": lambda: solution([1, 1], 3),
        "expected": 2,
    },
]
