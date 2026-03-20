from problems.p410_maximum_product_subarray import solution

TEST_CASES = [
    {
        "description": "Basic: [2,3,-2,4]",
        "run": lambda: solution([2, 3, -2, 4]),
        "expected": 6,
    },
    {
        "description": "Negative start: [-2,0,-1]",
        "run": lambda: solution([-2, 0, -1]),
        "expected": 0,
    },
    {
        "description": "Single element: [3]",
        "run": lambda: solution([3]),
        "expected": 3,
    },
    {
        "description": "Two negatives: [-2,-3,4]",
        "run": lambda: solution([-2, -3, 4]),
        "expected": 24,
    },
    {
        "description": "All negative: [-1,-2,-3]",
        "run": lambda: solution([-1, -2, -3]),
        "expected": 6,
    },
]
