from problems.p245_maximum_subarray import solution

TEST_CASES = [
    {
        "description": "Standard: [-2,1,-3,4,-1,2,1,-5,4]",
        "run": lambda: solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
        "expected": 6,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "All negative: [-1,-2,-3]",
        "run": lambda: solution([-1, -2, -3]),
        "expected": -1,
    },
    {
        "description": "All positive: [1,2,3,4]",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": 10,
    },
    {
        "description": "Mixed: [5,4,-1,7,8]",
        "run": lambda: solution([5, 4, -1, 7, 8]),
        "expected": 23,
    },
]
