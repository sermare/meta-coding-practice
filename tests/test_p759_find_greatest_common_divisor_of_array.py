from problems.p759_find_greatest_common_divisor_of_array import solution

TEST_CASES = [
    {
        "description": "GCD of 2 and 10",
        "run": lambda: solution([2, 5, 6, 9, 10]),
        "expected": 2,
    },
    {
        "description": "GCD of 1 and 7",
        "run": lambda: solution([7, 5, 6, 8, 3, 1]),
        "expected": 1,
    },
    {
        "description": "GCD of 3 and 3",
        "run": lambda: solution([3, 3]),
        "expected": 3,
    },
    {
        "description": "GCD of 6 and 12",
        "run": lambda: solution([6, 8, 10, 12]),
        "expected": 6,
    },
]
