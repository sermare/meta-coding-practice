from problems.p646_partition_to_k_equal_sum_subsets import solution

TEST_CASES = [
    {
        "description": "Can partition: [4,3,2,3,5,2,1] k=4",
        "run": lambda: solution([4, 3, 2, 3, 5, 2, 1], 4),
        "expected": True,
    },
    {
        "description": "Cannot partition: [1,2,3,4] k=3",
        "run": lambda: solution([1, 2, 3, 4], 3),
        "expected": False,
    },
    {
        "description": "k=1 always true",
        "run": lambda: solution([1, 2, 3], 1),
        "expected": True,
    },
    {
        "description": "Equal elements: [2,2,2,2] k=2",
        "run": lambda: solution([2, 2, 2, 2], 2),
        "expected": True,
    },
]
