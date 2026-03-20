from problems.p534_number_of_1_bits import solution

TEST_CASES = [
    {
        "description": "Binary 1011",
        "run": lambda: solution(11),
        "expected": 3,
    },
    {
        "description": "Power of 2",
        "run": lambda: solution(128),
        "expected": 1,
    },
    {
        "description": "All ones (31 bits)",
        "run": lambda: solution(2147483647),
        "expected": 31,
    },
    {
        "description": "Zero",
        "run": lambda: solution(0),
        "expected": 0,
    },
    {
        "description": "One",
        "run": lambda: solution(1),
        "expected": 1,
    },
]
