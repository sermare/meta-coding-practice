from problems.p742_reduction_operations_to_make_the_array_elements_equal import solution

TEST_CASES = [
    {
        "description": "Basic case: [5,1,3]",
        "run": lambda: solution([5, 1, 3]),
        "expected": 3,
    },
    {
        "description": "Already equal: [1,1,1]",
        "run": lambda: solution([1, 1, 1]),
        "expected": 0,
    },
    {
        "description": "Larger array: [1,1,2,2,3]",
        "run": lambda: solution([1, 1, 2, 2, 3]),
        "expected": 4,
    },
    {
        "description": "Single element: [5]",
        "run": lambda: solution([5]),
        "expected": 0,
    },
]
