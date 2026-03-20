from problems.p067_climbing_stairs import solution

TEST_CASES = [
    {
        "description": "2 stairs",
        "run": lambda: solution(2),
        "expected": 2,
    },
    {
        "description": "3 stairs",
        "run": lambda: solution(3),
        "expected": 3,
    },
    {
        "description": "1 stair",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "5 stairs",
        "run": lambda: solution(5),
        "expected": 8,
    },
    {
        "description": "10 stairs",
        "run": lambda: solution(10),
        "expected": 89,
    },
]
