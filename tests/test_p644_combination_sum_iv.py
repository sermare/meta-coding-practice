from problems.p644_combination_sum_iv import solution

TEST_CASES = [
    {
        "description": "Standard: nums=[1,2,3] target=4",
        "run": lambda: solution([1, 2, 3], 4),
        "expected": 7,
    },
    {
        "description": "Impossible: nums=[9] target=3",
        "run": lambda: solution([9], 3),
        "expected": 0,
    },
    {
        "description": "Single way: nums=[1] target=3",
        "run": lambda: solution([1], 3),
        "expected": 1,
    },
    {
        "description": "Target zero",
        "run": lambda: solution([1, 2], 0),
        "expected": 1,
    },
]
