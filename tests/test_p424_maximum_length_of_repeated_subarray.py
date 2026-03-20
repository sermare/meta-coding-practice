from problems.p424_maximum_length_of_repeated_subarray import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2,3,2,1] vs [3,2,1,4,7]",
        "run": lambda: solution([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]),
        "expected": 3,
    },
    {
        "description": "No common: [0,0,0] vs [1,1,1]",
        "run": lambda: solution([0, 0, 0], [1, 1, 1]),
        "expected": 0,
    },
    {
        "description": "Identical: [1,2,3] vs [1,2,3]",
        "run": lambda: solution([1, 2, 3], [1, 2, 3]),
        "expected": 3,
    },
    {
        "description": "Single match: [1] vs [1]",
        "run": lambda: solution([1], [1]),
        "expected": 1,
    },
    {
        "description": "Partial overlap: [0,1,1,1,1] vs [1,0,1,0,1]",
        "run": lambda: solution([0, 1, 1, 1, 1], [1, 0, 1, 0, 1]),
        "expected": 2,
    },
]
