from problems.p760_minimum_sum_of_four_digit_number_after_splitting_digits import solution

TEST_CASES = [
    {
        "description": "num = 2932",
        "run": lambda: solution(2932),
        "expected": 52,
    },
    {
        "description": "num = 4009",
        "run": lambda: solution(4009),
        "expected": 13,
    },
    {
        "description": "num = 1111",
        "run": lambda: solution(1111),
        "expected": 22,
    },
    {
        "description": "num = 1234",
        "run": lambda: solution(1234),
        "expected": 37,
    },
]
