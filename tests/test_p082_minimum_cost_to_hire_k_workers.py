from problems.p082_minimum_cost_to_hire_k_workers import solution

TEST_CASES = [
    {
        "description": "Basic: quality=[10,20,5] wage=[70,50,30] k=2",
        "run": lambda: round(solution([10, 20, 5], [70, 50, 30], 2), 5),
        "expected": 105.0,
    },
    {
        "description": "Larger: quality=[3,1,10,10,1] wage=[4,8,2,5,6] k=3",
        "run": lambda: round(solution([3, 1, 10, 10, 1], [4, 8, 2, 5, 6], 3), 5),
        "expected": 30.66667,
    },
    {
        "description": "Single worker: k=1",
        "run": lambda: round(solution([5], [10], 1), 5),
        "expected": 10.0,
    },
    {
        "description": "Two workers both hired: k=2",
        "run": lambda: round(solution([1, 1], [5, 5], 2), 5),
        "expected": 10.0,
    },
]
