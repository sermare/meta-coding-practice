from problems.p681_median_of_two_sorted_arrays import solution

TEST_CASES = [
    {
        "description": "Odd total: [1,3] and [2]",
        "run": lambda: solution([1, 3], [2]),
        "expected": 2.0,
    },
    {
        "description": "Even total: [1,2] and [3,4]",
        "run": lambda: solution([1, 2], [3, 4]),
        "expected": 2.5,
    },
    {
        "description": "One empty array",
        "run": lambda: solution([], [1]),
        "expected": 1.0,
    },
    {
        "description": "Both single element",
        "run": lambda: solution([1], [2]),
        "expected": 1.5,
    },
    {
        "description": "Non-overlapping: [1,2] and [3,4,5]",
        "run": lambda: solution([1, 2], [3, 4, 5]),
        "expected": 3.0,
    },
]
