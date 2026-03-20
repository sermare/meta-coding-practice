from problems.p346_minimum_operations_to_reduce_x_to_zero import solution

TEST_CASES = [
    {
        "description": "Basic: [1,1,4,2,3] x=5 -> 2",
        "run": lambda: solution([1, 1, 4, 2, 3], 5),
        "expected": 2,
    },
    {
        "description": "Both sides: [3,2,20,1,1,3] x=10 -> 5",
        "run": lambda: solution([3, 2, 20, 1, 1, 3], 10),
        "expected": 5,
    },
    {
        "description": "Impossible: [5,6,7,8,9] x=4 -> -1",
        "run": lambda: solution([5, 6, 7, 8, 9], 4),
        "expected": -1,
    },
    {
        "description": "Single element: [5] x=5 -> 1",
        "run": lambda: solution([5], 5),
        "expected": 1,
    },
]
