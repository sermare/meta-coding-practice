from problems.p618_maximum_subarray import solution

TEST_CASES = [
    {
        "description": "Mixed array: [-2,1,-3,4,-1,2,1,-5,4]",
        "run": lambda: solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
        "expected": 6,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "All positive: [5,4,-1,7,8]",
        "run": lambda: solution([5, 4, -1, 7, 8]),
        "expected": 23,
    },
    {
        "description": "All negative: [-3,-2,-1]",
        "run": lambda: solution([-3, -2, -1]),
        "expected": -1,
    },
    {
        "description": "Single negative: [-1]",
        "run": lambda: solution([-1]),
        "expected": -1,
    },
]
