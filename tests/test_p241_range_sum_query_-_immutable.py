from problems.p241_range_sum_query_-_immutable import solution

TEST_CASES = [
    {
        "description": "Standard queries",
        "run": lambda: solution([-2, 0, 3, -5, 2, -1], [[0, 2], [2, 5], [0, 5]]),
        "expected": [1, -1, -3],
    },
    {
        "description": "Single element range",
        "run": lambda: solution([1, 2, 3], [[1, 1]]),
        "expected": [2],
    },
    {
        "description": "Entire array",
        "run": lambda: solution([1, 2, 3, 4], [[0, 3]]),
        "expected": [10],
    },
    {
        "description": "Multiple same queries",
        "run": lambda: solution([5, 10], [[0, 0], [1, 1], [0, 1]]),
        "expected": [5, 10, 15],
    },
]
