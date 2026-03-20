from problems.p189_number_of_digit_one import solution

TEST_CASES = [
    {
        "description": "n=13 -> 6",
        "run": lambda: solution(13),
        "expected": 6,
    },
    {
        "description": "n=0 -> 0",
        "run": lambda: solution(0),
        "expected": 0,
    },
    {
        "description": "n=1 -> 1",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "n=100 -> 21",
        "run": lambda: solution(100),
        "expected": 21,
    },
]
