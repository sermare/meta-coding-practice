from problems.p093_gas_station import solution

TEST_CASES = [
    {
        "description": "Start at index 3",
        "run": lambda: solution([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
        "expected": 3,
    },
    {
        "description": "Impossible circuit",
        "run": lambda: solution([2, 3, 4], [3, 4, 3]),
        "expected": -1,
    },
    {
        "description": "Start at index 0",
        "run": lambda: solution([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]),
        "expected": 4,
    },
    {
        "description": "Single station with enough gas",
        "run": lambda: solution([2], [1]),
        "expected": 0,
    },
]
