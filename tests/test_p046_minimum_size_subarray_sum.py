from problems.p046_minimum_size_subarray_sum import solution

TEST_CASES = [
    {
        "description": "target=7, nums=[2,3,1,2,4,3] -> 2",
        "run": lambda: solution(7, [2, 3, 1, 2, 4, 3]),
        "expected": 2,
    },
    {
        "description": "target=4, nums=[1,4,4] -> 1",
        "run": lambda: solution(4, [1, 4, 4]),
        "expected": 1,
    },
    {
        "description": "No subarray meets target",
        "run": lambda: solution(11, [1, 1, 1, 1, 1, 1, 1, 1]),
        "expected": 0,
    },
    {
        "description": "Entire array needed",
        "run": lambda: solution(15, [1, 2, 3, 4, 5]),
        "expected": 5,
    },
    {
        "description": "Single element meets target",
        "run": lambda: solution(6, [10, 2, 3]),
        "expected": 1,
    },
]
