from problems.p741_maximum_element_after_decreasing_and_rearranging import solution

TEST_CASES = [
    {
        "description": "Basic case: [2,2,1,2,1]",
        "run": lambda: solution([2, 2, 1, 2, 1]),
        "expected": 2,
    },
    {
        "description": "Large gaps: [100,1,1000]",
        "run": lambda: solution([100, 1, 1000]),
        "expected": 3,
    },
    {
        "description": "Already valid: [1,2,3,4,5]",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": 5,
    },
    {
        "description": "All ones: [1,1,1,1]",
        "run": lambda: solution([1, 1, 1, 1]),
        "expected": 1,
    },
]
