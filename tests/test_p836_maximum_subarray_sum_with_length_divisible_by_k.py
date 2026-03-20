from problems.p836_maximum_subarray_sum_with_length_divisible_by_k import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2] k=1",
        "run": lambda: solution([1,2], 1),
        "expected": 3,
    },
    {
        "description": "Pick subarray: [-1,-2,3,4] k=2",
        "run": lambda: solution([-1,-2,3,4], 2),
        "expected": 7,
    },
    {
        "description": "All negative: [-3,-2,-1] k=1",
        "run": lambda: solution([-3,-2,-1], 1),
        "expected": -1,
    },
    {
        "description": "Exact k: [5,-1,3] k=3",
        "run": lambda: solution([5,-1,3], 3),
        "expected": 7,
    },
]
