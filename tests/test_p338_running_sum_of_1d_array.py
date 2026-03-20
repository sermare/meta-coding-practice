from problems.p338_running_sum_of_1d_array import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2,3,4] -> [1,3,6,10]",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": [1, 3, 6, 10],
    },
    {
        "description": "With zeros: [1,1,1,1,1] -> [1,2,3,4,5]",
        "run": lambda: solution([1, 1, 1, 1, 1]),
        "expected": [1, 2, 3, 4, 5],
    },
    {
        "description": "Mixed: [3,1,2,10,1] -> [3,4,6,16,17]",
        "run": lambda: solution([3, 1, 2, 10, 1]),
        "expected": [3, 4, 6, 16, 17],
    },
    {
        "description": "Single: [5] -> [5]",
        "run": lambda: solution([5]),
        "expected": [5],
    },
]
