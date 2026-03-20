from problems.p815_find_xor_sum_of_all_pairs_bitwise_and import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2,3] and [6,5]",
        "run": lambda: solution([1,2,3], [6,5]),
        "expected": 0,
    },
    {
        "description": "Single elements: [12] and [4]",
        "run": lambda: solution([12], [4]),
        "expected": 4,
    },
    {
        "description": "All ones: [1,1] and [1,1]",
        "run": lambda: solution([1,1], [1,1]),
        "expected": 0,
    },
    {
        "description": "Powers of two: [1,2,4] and [8,16]",
        "run": lambda: solution([1,2,4], [8,16]),
        "expected": 0,
    },
]
