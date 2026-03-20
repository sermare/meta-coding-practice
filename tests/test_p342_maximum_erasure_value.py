from problems.p342_maximum_erasure_value import solution

TEST_CASES = [
    {
        "description": "Basic: [4,2,4,5,6] -> 17",
        "run": lambda: solution([4, 2, 4, 5, 6]),
        "expected": 17,
    },
    {
        "description": "Repeated: [5,2,1,2,5,2,1,2,5] -> 8",
        "run": lambda: solution([5, 2, 1, 2, 5, 2, 1, 2, 5]),
        "expected": 8,
    },
    {
        "description": "All unique: [1,2,3,4] -> 10",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": 10,
    },
    {
        "description": "Single element: [7] -> 7",
        "run": lambda: solution([7]),
        "expected": 7,
    },
]
