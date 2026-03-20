from problems.p782_minimum_operations_to_make_array_alternating import solution

TEST_CASES = [
    {
        "description": "Basic: [3,1,3,2,4,3]",
        "run": lambda: solution([3,1,3,2,4,3]),
        "expected": 3,
    },
    {
        "description": "Already alternating: [1,2,1,2]",
        "run": lambda: solution([1,2,1,2]),
        "expected": 0,
    },
    {
        "description": "All same: [2,2,2,2]",
        "run": lambda: solution([2,2,2,2]),
        "expected": 2,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": 0,
    },
]
