from problems.p779_maximum_xor_after_operations import solution

TEST_CASES = [
    {
        "description": "Basic: [3,2,4,6]",
        "run": lambda: solution([3,2,4,6]),
        "expected": 7,
    },
    {
        "description": "Single element: [1,2,3,9,2]",
        "run": lambda: solution([1,2,3,9,2]),
        "expected": 11,
    },
    {
        "description": "All zeros: [0,0,0]",
        "run": lambda: solution([0,0,0]),
        "expected": 0,
    },
    {
        "description": "Powers of two: [1,2,4,8]",
        "run": lambda: solution([1,2,4,8]),
        "expected": 15,
    },
]
