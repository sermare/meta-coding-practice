from problems.p780_count_subarrays_with_score_less_than_k import solution

TEST_CASES = [
    {
        "description": "Basic: [2,1,4,3,5], k=10",
        "run": lambda: solution([2,1,4,3,5], 10),
        "expected": 6,
    },
    {
        "description": "All valid: [1,1,1], k=5",
        "run": lambda: solution([1,1,1], 5),
        "expected": 5,
    },
    {
        "description": "Single element: [5], k=10",
        "run": lambda: solution([5], 10),
        "expected": 1,
    },
    {
        "description": "None valid: [10], k=5",
        "run": lambda: solution([10], 5),
        "expected": 0,
    },
]
