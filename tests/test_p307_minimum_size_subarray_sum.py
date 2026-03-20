from problems.p307_minimum_size_subarray_sum import solution

TEST_CASES = [
    {
        "description": "Basic case: target=7, [2,3,1,2,4,3]",
        "run": lambda: solution(7, [2, 3, 1, 2, 4, 3]),
        "expected": 2,
    },
    {
        "description": "Single element equals target",
        "run": lambda: solution(4, [1, 4, 4]),
        "expected": 1,
    },
    {
        "description": "No valid subarray",
        "run": lambda: solution(11, [1, 1, 1, 1, 1]),
        "expected": 0,
    },
    {
        "description": "Entire array needed",
        "run": lambda: solution(15, [1, 2, 3, 4, 5]),
        "expected": 5,
    },
]
