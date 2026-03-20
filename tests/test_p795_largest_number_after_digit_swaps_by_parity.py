from problems.p795_largest_number_after_digit_swaps_by_parity import solution

TEST_CASES = [
    {
        "description": "Basic: 1234",
        "run": lambda: solution(1234),
        "expected": 3412,
    },
    {
        "description": "All odd: 13579",
        "run": lambda: solution(13579),
        "expected": 97531,
    },
    {
        "description": "Single digit: 5",
        "run": lambda: solution(5),
        "expected": 5,
    },
    {
        "description": "Already max: 9876",
        "run": lambda: solution(9876),
        "expected": 9876,
    },
]
