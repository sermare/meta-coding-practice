from problems.p733_minimum_limit_of_balls_in_a_bag import solution

TEST_CASES = [
    {
        "description": "Basic case: nums=[9], maxOps=2",
        "run": lambda: solution([9], 2),
        "expected": 3,
    },
    {
        "description": "Multiple bags: nums=[2,4,8,2], maxOps=4",
        "run": lambda: solution([2, 4, 8, 2], 4),
        "expected": 2,
    },
    {
        "description": "No operations: nums=[7,17], maxOps=0",
        "run": lambda: solution([7, 17], 0),
        "expected": 17,
    },
    {
        "description": "Large values: nums=[1,1,100], maxOps=3",
        "run": lambda: solution([1, 1, 100], 3),
        "expected": 25,
    },
]
