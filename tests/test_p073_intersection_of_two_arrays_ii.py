from problems.p073_intersection_of_two_arrays_ii import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2,2,1] and [2,2]",
        "run": lambda: sorted(solution([1, 2, 2, 1], [2, 2])),
        "expected": [2, 2],
    },
    {
        "description": "Mixed: [4,9,5] and [9,4,9,8,4]",
        "run": lambda: sorted(solution([4, 9, 5], [9, 4, 9, 8, 4])),
        "expected": [4, 9],
    },
    {
        "description": "No intersection: [1,2] and [3,4]",
        "run": lambda: solution([1, 2], [3, 4]),
        "expected": [],
    },
    {
        "description": "All same: [1,1,1] and [1,1]",
        "run": lambda: sorted(solution([1, 1, 1], [1, 1])),
        "expected": [1, 1],
    },
]
