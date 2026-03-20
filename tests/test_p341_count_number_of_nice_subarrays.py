from problems.p341_count_number_of_nice_subarrays import solution

TEST_CASES = [
    {
        "description": "Basic: [1,1,2,1,1] k=3 -> 2",
        "run": lambda: solution([1, 1, 2, 1, 1], 3),
        "expected": 2,
    },
    {
        "description": "Longer: [2,2,2,1,2,2,1,2,2,2] k=2 -> 16",
        "run": lambda: solution([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2),
        "expected": 16,
    },
    {
        "description": "No odd numbers: [2,4,6] k=1 -> 0",
        "run": lambda: solution([2, 4, 6], 1),
        "expected": 0,
    },
    {
        "description": "All odd: [1,1,1] k=2 -> 2",
        "run": lambda: solution([1, 1, 1], 2),
        "expected": 2,
    },
]
