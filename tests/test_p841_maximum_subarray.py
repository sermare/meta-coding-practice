from problems.p841_maximum_subarray import solution

TEST_CASES = [
    {
        "description": "Mixed: [-2,1,-3,4,-1,2,1,-5,4]",
        "run": lambda: solution([-2,1,-3,4,-1,2,1,-5,4]),
        "expected": 6,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "All negative: [-2,-1,-3]",
        "run": lambda: solution([-2,-1,-3]),
        "expected": -1,
    },
    {
        "description": "All positive: [1,2,3,4]",
        "run": lambda: solution([1,2,3,4]),
        "expected": 10,
    },
]
