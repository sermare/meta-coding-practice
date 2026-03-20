from problems.p471_car_fleet import solution

TEST_CASES = [
    {
        "description": "Three fleets",
        "run": lambda: solution(12, [10,8,0,5,3], [2,4,1,1,3]),
        "expected": 3,
    },
    {
        "description": "Single car",
        "run": lambda: solution(10, [3], [3]),
        "expected": 1,
    },
    {
        "description": "All merge: target=100",
        "run": lambda: solution(100, [0,2,4], [4,2,1]),
        "expected": 1,
    },
    {
        "description": "Two fleets",
        "run": lambda: solution(10, [6,8], [3,2]),
        "expected": 2,
    },
    {
        "description": "Same position different speed",
        "run": lambda: solution(10, [0,0], [1,2]),
        "expected": 1,
    },
]
