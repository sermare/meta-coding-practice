from problems.p413_partition_equal_subset_sum import solution

TEST_CASES = [
    {
        "description": "Can partition: [1,5,11,5]",
        "run": lambda: solution([1, 5, 11, 5]),
        "expected": True,
    },
    {
        "description": "Cannot partition: [1,2,3,5]",
        "run": lambda: solution([1, 2, 3, 5]),
        "expected": False,
    },
    {
        "description": "Two equal elements: [1,1]",
        "run": lambda: solution([1, 1]),
        "expected": True,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": False,
    },
    {
        "description": "Larger array: [1,2,3,4,5,6,7]",
        "run": lambda: solution([1, 2, 3, 4, 5, 6, 7]),
        "expected": True,
    },
]
