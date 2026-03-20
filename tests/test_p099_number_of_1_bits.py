from problems.p099_number_of_1_bits import solution

TEST_CASES = [
    {
        "description": "11 (binary 1011) -> 3",
        "run": lambda: solution(11),
        "expected": 3,
    },
    {
        "description": "128 (binary 10000000) -> 1",
        "run": lambda: solution(128),
        "expected": 1,
    },
    {
        "description": "7 (binary 111) -> 3",
        "run": lambda: solution(7),
        "expected": 3,
    },
    {
        "description": "1 (binary 1) -> 1",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "255 (binary 11111111) -> 8",
        "run": lambda: solution(255),
        "expected": 8,
    },
]
