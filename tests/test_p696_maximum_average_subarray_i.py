from problems.p696_maximum_average_subarray_i import solution

TEST_CASES = [
    {
        "description": "Basic: [1,12,-5,-6,50,3] k=4",
        "run": lambda: solution([1, 12, -5, -6, 50, 3], 4),
        "expected": 12.75,
    },
    {
        "description": "Single element: [5] k=1",
        "run": lambda: solution([5], 1),
        "expected": 5.0,
    },
    {
        "description": "All same: [3,3,3] k=2",
        "run": lambda: solution([3, 3, 3], 2),
        "expected": 3.0,
    },
    {
        "description": "Negative values: [-1,-2,-3,-4] k=2",
        "run": lambda: solution([-1, -2, -3, -4], 2),
        "expected": -1.5,
    },
]
