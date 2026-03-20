from problems.p138_concatenation_of_consecutive_binary_numbers import solution

TEST_CASES = [
    {
        "description": "n = 1",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "n = 3",
        "run": lambda: solution(3),
        "expected": 27,
    },
    {
        "description": "n = 12",
        "run": lambda: solution(12),
        "expected": 505379714,
    },
    {
        "description": "n = 2",
        "run": lambda: solution(2),
        "expected": 6,
    },
    {
        "description": "n = 4",
        "run": lambda: solution(4),
        "expected": 220,
    },
]
