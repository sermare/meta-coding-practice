from problems.p052_median_of_two_sorted_arrays import solution

TEST_CASES = [
    {
        "description": "Odd total length: [1,3] and [2]",
        "run": lambda: solution([1, 3], [2]),
        "expected": 2.0,
    },
    {
        "description": "Even total length: [1,2] and [3,4]",
        "run": lambda: solution([1, 2], [3, 4]),
        "expected": 2.5,
    },
    {
        "description": "One empty array: [] and [1]",
        "run": lambda: solution([], [1]),
        "expected": 1.0,
    },
    {
        "description": "Single elements: [1] and [2]",
        "run": lambda: solution([1], [2]),
        "expected": 1.5,
    },
    {
        "description": "Larger arrays: [1,2,3] and [4,5,6]",
        "run": lambda: solution([1, 2, 3], [4, 5, 6]),
        "expected": 3.5,
    },
]
