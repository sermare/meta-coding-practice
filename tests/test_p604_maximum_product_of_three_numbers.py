from problems.p604_maximum_product_of_three_numbers import solution

TEST_CASES = [
    {
        "description": "Basic case: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": 6,
    },
    {
        "description": "Four numbers: [1,2,3,4]",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": 24,
    },
    {
        "description": "All negative: [-1,-2,-3]",
        "run": lambda: solution([-1, -2, -3]),
        "expected": -6,
    },
    {
        "description": "Mixed with negatives: [-4,-3,-2,1,2,3]",
        "run": lambda: solution([-4, -3, -2, 1, 2, 3]),
        "expected": 36,
    },
    {
        "description": "Contains zero: [-1,0,1,2,3]",
        "run": lambda: solution([-1, 0, 1, 2, 3]),
        "expected": 6,
    },
]
