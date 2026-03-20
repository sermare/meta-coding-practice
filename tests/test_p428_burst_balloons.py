from problems.p428_burst_balloons import solution

TEST_CASES = [
    {
        "description": "Basic: [3,1,5,8]",
        "run": lambda: solution([3, 1, 5, 8]),
        "expected": 167,
    },
    {
        "description": "Single balloon: [5]",
        "run": lambda: solution([5]),
        "expected": 5,
    },
    {
        "description": "Two balloons: [3,5]",
        "run": lambda: solution([3, 5]),
        "expected": 20,
    },
    {
        "description": "All ones: [1,1,1]",
        "run": lambda: solution([1, 1, 1]),
        "expected": 3,
    },
    {
        "description": "Larger: [1,5]",
        "run": lambda: solution([1, 5]),
        "expected": 10,
    },
]
