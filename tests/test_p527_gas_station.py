from problems.p527_gas_station import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution([1,2,3,4,5], [3,4,5,1,2]),
        "expected": 3,
    },
    {
        "description": "Impossible",
        "run": lambda: solution([2,3,4], [3,4,3]),
        "expected": -1,
    },
    {
        "description": "Start at 0",
        "run": lambda: solution([5,1,2,3,4], [4,4,1,5,1]),
        "expected": 4,
    },
    {
        "description": "Single station",
        "run": lambda: solution([5], [3]),
        "expected": 0,
    },
    {
        "description": "Equal total",
        "run": lambda: solution([1,2,3], [1,2,3]),
        "expected": 0,
    },
]
