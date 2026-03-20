from problems.p111_maximum_subarray import solution

TEST_CASES = [
    {
        "description": "Mixed positive and negative",
        "run": lambda: solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
        "expected": 6,
    },
    {
        "description": "Single element",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "All positive",
        "run": lambda: solution([5, 4, -1, 7, 8]),
        "expected": 23,
    },
    {
        "description": "All negative",
        "run": lambda: solution([-3, -2, -1, -4]),
        "expected": -1,
    },
    {
        "description": "Single negative element",
        "run": lambda: solution([-1]),
        "expected": -1,
    },
]
