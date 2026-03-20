from problems.p743_maximum_product_difference_between_two_pairs import solution

TEST_CASES = [
    {
        "description": "Basic case: [5,6,2,7,4]",
        "run": lambda: solution([5, 6, 2, 7, 4]),
        "expected": 34,
    },
    {
        "description": "Small array: [4,2,5,9,7,4,8]",
        "run": lambda: solution([4, 2, 5, 9, 7, 4, 8]),
        "expected": 64,
    },
    {
        "description": "Minimum size: [1,2,3,4]",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": 10,
    },
    {
        "description": "Duplicates: [1,1,1,1]",
        "run": lambda: solution([1, 1, 1, 1]),
        "expected": 0,
    },
]
