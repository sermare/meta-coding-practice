from problems.p781_minimum_deletions_to_make_array_beautiful import solution

TEST_CASES = [
    {
        "description": "Basic: [1,1,2,3,5]",
        "run": lambda: solution([1,1,2,3,5]),
        "expected": 1,
    },
    {
        "description": "Already beautiful: [1,2,3,4]",
        "run": lambda: solution([1,2,3,4]),
        "expected": 0,
    },
    {
        "description": "All same: [1,1,1,1,1]",
        "run": lambda: solution([1,1,1,1,1]),
        "expected": 3,
    },
    {
        "description": "Empty result: [1,1]",
        "run": lambda: solution([1,1]),
        "expected": 2,
    },
]
