from problems.p137_subarray_sum_equals_k import solution

TEST_CASES = [
    {
        "description": "Two subarrays sum to 2",
        "run": lambda: solution([1, 1, 1], 2),
        "expected": 2,
    },
    {
        "description": "Two subarrays sum to 3",
        "run": lambda: solution([1, 2, 3], 3),
        "expected": 2,
    },
    {
        "description": "Negative numbers",
        "run": lambda: solution([1, -1, 0], 0),
        "expected": 3,
    },
    {
        "description": "Single element match",
        "run": lambda: solution([5], 5),
        "expected": 1,
    },
    {
        "description": "No subarray matches",
        "run": lambda: solution([1, 2, 3], 7),
        "expected": 0,
    },
]
