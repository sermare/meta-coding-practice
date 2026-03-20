from problems.p096_maximum_product_subarray import solution

TEST_CASES = [
    {
        "description": "Basic: [2,3,-2,4] -> 6",
        "run": lambda: solution([2, 3, -2, 4]),
        "expected": 6,
    },
    {
        "description": "With zero: [-2,0,-1] -> 0",
        "run": lambda: solution([-2, 0, -1]),
        "expected": 0,
    },
    {
        "description": "All negative: [-2,-3,-4] -> 12",
        "run": lambda: solution([-2, -3, -4]),
        "expected": 12,
    },
    {
        "description": "Single element: [5]",
        "run": lambda: solution([5]),
        "expected": 5,
    },
    {
        "description": "Two negatives: [-2,-3] -> 6",
        "run": lambda: solution([-2, -3]),
        "expected": 6,
    },
]
