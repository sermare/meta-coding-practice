from problems.p329_subarray_sums_divisible_by_k import solution

TEST_CASES = [
    {
        "description": "Basic: [4,5,0,-2,-3,1] k=5 -> 7",
        "run": lambda: solution([4, 5, 0, -2, -3, 1], 5),
        "expected": 7,
    },
    {
        "description": "Single zero: [5] k=9 -> 0",
        "run": lambda: solution([5], 9),
        "expected": 0,
    },
    {
        "description": "All divisible: [5,10,15] k=5 -> 6",
        "run": lambda: solution([5, 10, 15], 5),
        "expected": 6,
    },
    {
        "description": "Single divisible: [0] k=1 -> 1",
        "run": lambda: solution([0], 1),
        "expected": 1,
    },
]
