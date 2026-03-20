from problems.p349_trapping_rain_water import solution

TEST_CASES = [
    {
        "description": "Basic: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6",
        "run": lambda: solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]),
        "expected": 6,
    },
    {
        "description": "V shape: [4,2,0,3,2,5] -> 9",
        "run": lambda: solution([4, 2, 0, 3, 2, 5]),
        "expected": 9,
    },
    {
        "description": "No water: [1,2,3,4] -> 0",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": 0,
    },
    {
        "description": "Empty: [] -> 0",
        "run": lambda: solution([]),
        "expected": 0,
    },
    {
        "description": "Flat: [3,3,3] -> 0",
        "run": lambda: solution([3, 3, 3]),
        "expected": 0,
    },
]
