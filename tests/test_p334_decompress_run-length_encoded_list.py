from problems.p334_decompress_run-length_encoded_list import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2,3,4]",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": [2, 4, 4, 4],
    },
    {
        "description": "Single pair: [2,5]",
        "run": lambda: solution([2, 5]),
        "expected": [5, 5],
    },
    {
        "description": "Multiple pairs: [1,1,2,3]",
        "run": lambda: solution([1, 1, 2, 3]),
        "expected": [1, 3, 3],
    },
    {
        "description": "Zero frequency: [0,1,2,3]",
        "run": lambda: solution([0, 1, 2, 3]),
        "expected": [3, 3],
    },
]
