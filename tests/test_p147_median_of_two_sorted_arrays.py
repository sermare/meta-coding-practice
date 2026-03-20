from problems.p147_median_of_two_sorted_arrays import solution

TEST_CASES = [
    {
        "description": "Odd total length",
        "run": lambda: solution([1, 3], [2]),
        "expected": 2.0,
    },
    {
        "description": "Even total length",
        "run": lambda: solution([1, 2], [3, 4]),
        "expected": 2.5,
    },
    {
        "description": "One empty array",
        "run": lambda: solution([], [1, 2, 3]),
        "expected": 2.0,
    },
    {
        "description": "Non-overlapping arrays",
        "run": lambda: solution([1, 2], [5, 6, 7]),
        "expected": 5.0,
    },
    {
        "description": "Single elements each",
        "run": lambda: solution([1], [2]),
        "expected": 1.5,
    },
]
