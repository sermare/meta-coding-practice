from problems.p656_combination_sum_iv import solution

TEST_CASES = [
    {
        "description": "Basic case: [1,2,3] target=4",
        "run": lambda: solution([1, 2, 3], 4),
        "expected": 7,
    },
    {
        "description": "Single element: [9] target=3",
        "run": lambda: solution([9], 3),
        "expected": 0,
    },
    {
        "description": "Target is zero",
        "run": lambda: solution([1, 2, 3], 0),
        "expected": 1,
    },
    {
        "description": "Only ones: [1] target=5",
        "run": lambda: solution([1], 5),
        "expected": 1,
    },
    {
        "description": "Two elements: [1,2] target=3",
        "run": lambda: solution([1, 2], 3),
        "expected": 3,
    },
]
