from problems.p813_maximum_score_of_a_good_subarray import solution

TEST_CASES = [
    {
        "description": "Basic: [1,4,3,7,4,5] k=3",
        "run": lambda: solution([1,4,3,7,4,5], 3),
        "expected": 15,
    },
    {
        "description": "Single element: [5] k=0",
        "run": lambda: solution([5], 0),
        "expected": 5,
    },
    {
        "description": "Decreasing: [5,4,3,2,1] k=0",
        "run": lambda: solution([5,4,3,2,1], 0),
        "expected": 5,
    },
    {
        "description": "All same: [3,3,3,3] k=2",
        "run": lambda: solution([3,3,3,3], 2),
        "expected": 12,
    },
]
