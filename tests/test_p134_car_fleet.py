from problems.p134_car_fleet import solution

TEST_CASES = [
    {
        "description": "Three fleets",
        "run": lambda: solution(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),
        "expected": 3,
    },
    {
        "description": "Single car",
        "run": lambda: solution(10, [0], [5]),
        "expected": 1,
    },
    {
        "description": "All merge into one fleet",
        "run": lambda: solution(10, [0, 2, 4], [2, 3, 1]),
        "expected": 1,
    },
    {
        "description": "No merges",
        "run": lambda: solution(100, [0, 10, 20], [1, 1, 1]),
        "expected": 3,
    },
    {
        "description": "Two fleets",
        "run": lambda: solution(10, [6, 8], [3, 2]),
        "expected": 2,
    },
]
