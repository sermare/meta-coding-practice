from problems.p328_maximum_sum_circular_subarray import solution

TEST_CASES = [
    {
        "description": "Non-circular: [1,-2,3,-2] -> 3",
        "run": lambda: solution([1, -2, 3, -2]),
        "expected": 3,
    },
    {
        "description": "Circular wrap: [5,-3,5] -> 10",
        "run": lambda: solution([5, -3, 5]),
        "expected": 10,
    },
    {
        "description": "All negative: [-3,-2,-1] -> -1",
        "run": lambda: solution([-3, -2, -1]),
        "expected": -1,
    },
    {
        "description": "Single element: [3] -> 3",
        "run": lambda: solution([3]),
        "expected": 3,
    },
]
