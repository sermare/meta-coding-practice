from problems.p532_maximum_subarray import solution

TEST_CASES = [
    {
        "description": "Mixed array",
        "run": lambda: solution([-2,1,-3,4,-1,2,1,-5,4]),
        "expected": 6,
    },
    {
        "description": "Single element",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "All negative",
        "run": lambda: solution([-1,-2,-3]),
        "expected": -1,
    },
    {
        "description": "All positive",
        "run": lambda: solution([1,2,3]),
        "expected": 6,
    },
    {
        "description": "Negative then positive",
        "run": lambda: solution([-5,4,3]),
        "expected": 7,
    },
]
