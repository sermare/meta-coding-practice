from problems.p036_trapping_rain_water import solution

TEST_CASES = [
    {
        "description": "[0,1,0,2,1,0,1,3,2,1,2,1] -> 6",
        "run": lambda: solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]),
        "expected": 6,
    },
    {
        "description": "[4,2,0,3,2,5] -> 9",
        "run": lambda: solution([4, 2, 0, 3, 2, 5]),
        "expected": 9,
    },
    {
        "description": "[1,2,3,4,5] -> 0 (ascending, no water)",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": 0,
    },
    {
        "description": "[5,4,3,2,1] -> 0 (descending, no water)",
        "run": lambda: solution([5, 4, 3, 2, 1]),
        "expected": 0,
    },
    {
        "description": "[3,0,0,2,0,4] -> 10",
        "run": lambda: solution([3, 0, 0, 2, 0, 4]),
        "expected": 10,
    },
]
