from problems.p716_monotonic_array import solution

TEST_CASES = [
    {
        "description": "Monotone increasing: [1,2,2,3]",
        "run": lambda: solution([1, 2, 2, 3]),
        "expected": True,
    },
    {
        "description": "Monotone decreasing: [6,5,4,4]",
        "run": lambda: solution([6, 5, 4, 4]),
        "expected": True,
    },
    {
        "description": "Not monotonic: [1,3,2]",
        "run": lambda: solution([1, 3, 2]),
        "expected": False,
    },
    {
        "description": "All same: [1,1,1]",
        "run": lambda: solution([1, 1, 1]),
        "expected": True,
    },
    {
        "description": "Single element: [5]",
        "run": lambda: solution([5]),
        "expected": True,
    },
]
