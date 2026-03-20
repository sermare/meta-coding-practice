from problems.p425_uncrossed_lines import solution

TEST_CASES = [
    {
        "description": "Basic: [1,4,2] vs [1,2,4]",
        "run": lambda: solution([1, 4, 2], [1, 2, 4]),
        "expected": 2,
    },
    {
        "description": "Longer: [2,5,1,2,5] vs [10,5,2,1,5,2]",
        "run": lambda: solution([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]),
        "expected": 3,
    },
    {
        "description": "No match: [1,3,7,1,7,5] vs [2,4,6]",
        "run": lambda: solution([1, 3, 7, 1, 7, 5], [2, 4, 6]),
        "expected": 0,
    },
    {
        "description": "Same arrays: [1,2,3] vs [1,2,3]",
        "run": lambda: solution([1, 2, 3], [1, 2, 3]),
        "expected": 3,
    },
    {
        "description": "Single element match: [1] vs [1]",
        "run": lambda: solution([1], [1]),
        "expected": 1,
    },
]
