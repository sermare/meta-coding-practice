from problems.p450_maximum_score_from_performing_multiplication_operations import solution

TEST_CASES = [
    {
        "description": "Basic: nums=[1,2,3] multipliers=[3,2,1]",
        "run": lambda: solution([1, 2, 3], [3, 2, 1]),
        "expected": 14,
    },
    {
        "description": "Negative multipliers: nums=[-5,-3,-3,-2,7,1] multipliers=[-10,-5,3,4,6]",
        "run": lambda: solution([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]),
        "expected": 102,
    },
    {
        "description": "Single operation: nums=[1,2] multipliers=[1]",
        "run": lambda: solution([1, 2], [1]),
        "expected": 2,
    },
    {
        "description": "All from left: nums=[1,2,3] multipliers=[1,1,1]",
        "run": lambda: solution([1, 2, 3], [1, 1, 1]),
        "expected": 6,
    },
    {
        "description": "Two operations: nums=[1,5,2] multipliers=[3,1]",
        "run": lambda: solution([1, 5, 2], [3, 1]),
        "expected": 7,
    },
]
