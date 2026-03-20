from problems.p762_keep_multiplying_found_values_by_two import solution

TEST_CASES = [
    {
        "description": "Basic: [5,3,6,1,12], original=3",
        "run": lambda: solution([5,3,6,1,12], 3),
        "expected": 24,
    },
    {
        "description": "Not found: [2,7,9], original=4",
        "run": lambda: solution([2,7,9], 4),
        "expected": 4,
    },
    {
        "description": "Single doubling: [8,19,4,2], original=2",
        "run": lambda: solution([8,19,4,2], 2),
        "expected": 16,
    },
    {
        "description": "Already absent: [1,2,3], original=5",
        "run": lambda: solution([1,2,3], 5),
        "expected": 5,
    },
]
