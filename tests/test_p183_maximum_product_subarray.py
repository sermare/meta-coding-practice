from problems.p183_maximum_product_subarray import solution

TEST_CASES = [
    {
        "description": "[2,3,-2,4] -> 6",
        "run": lambda: solution([2, 3, -2, 4]),
        "expected": 6,
    },
    {
        "description": "[-2,0,-1] -> 0",
        "run": lambda: solution([-2, 0, -1]),
        "expected": 0,
    },
    {
        "description": "Single negative",
        "run": lambda: solution([-2]),
        "expected": -2,
    },
    {
        "description": "Two negatives make positive",
        "run": lambda: solution([-2, -3]),
        "expected": 6,
    },
    {
        "description": "All positive",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": 24,
    },
]
