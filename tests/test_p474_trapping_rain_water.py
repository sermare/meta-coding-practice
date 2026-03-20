from problems.p474_trapping_rain_water import solution

TEST_CASES = [
    {
        "description": "Standard: 6 units",
        "run": lambda: solution([0,1,0,2,1,0,1,3,2,1,2,1]),
        "expected": 6,
    },
    {
        "description": "V-shape: 9 units",
        "run": lambda: solution([4,2,0,3,2,5]),
        "expected": 9,
    },
    {
        "description": "No trap: [1,2,3]",
        "run": lambda: solution([1,2,3]),
        "expected": 0,
    },
    {
        "description": "No trap: decreasing",
        "run": lambda: solution([3,2,1]),
        "expected": 0,
    },
    {
        "description": "Single bar",
        "run": lambda: solution([5]),
        "expected": 0,
    },
]
