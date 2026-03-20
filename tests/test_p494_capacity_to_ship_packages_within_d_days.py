from problems.p494_capacity_to_ship_packages_within_d_days import solution

TEST_CASES = [
    {
        "description": "Standard: 5 days -> 15",
        "run": lambda: solution([1,2,3,4,5,6,7,8,9,10], 5),
        "expected": 15,
    },
    {
        "description": "[3,2,2,4,1,4] 3 days -> 6",
        "run": lambda: solution([3,2,2,4,1,4], 3),
        "expected": 6,
    },
    {
        "description": "[1,2,3,1,1] 4 days -> 3",
        "run": lambda: solution([1,2,3,1,1], 4),
        "expected": 3,
    },
    {
        "description": "Single day: [1,2,3] -> 6",
        "run": lambda: solution([1,2,3], 1),
        "expected": 6,
    },
    {
        "description": "Each day: [5,5,5] 3 days -> 5",
        "run": lambda: solution([5,5,5], 3),
        "expected": 5,
    },
]
