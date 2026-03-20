from problems.p676_largest_rectangle_in_histogram import solution

TEST_CASES = [
    {
        "description": "Standard case: [2,1,5,6,2,3]",
        "run": lambda: solution([2, 1, 5, 6, 2, 3]),
        "expected": 10,
    },
    {
        "description": "Single bar: [5]",
        "run": lambda: solution([5]),
        "expected": 5,
    },
    {
        "description": "Uniform heights: [3,3,3,3]",
        "run": lambda: solution([3, 3, 3, 3]),
        "expected": 12,
    },
    {
        "description": "Descending: [5,4,3,2,1]",
        "run": lambda: solution([5, 4, 3, 2, 1]),
        "expected": 9,
    },
    {
        "description": "Ascending: [1,2,3,4,5]",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": 9,
    },
]
