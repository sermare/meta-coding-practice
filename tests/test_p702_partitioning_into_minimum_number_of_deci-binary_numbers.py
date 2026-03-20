from problems.p702_partitioning_into_minimum_number_of_deci-binary_numbers import solution

TEST_CASES = [
    {
        "description": "Basic case: n='32'",
        "run": lambda: solution("32"),
        "expected": 3,
    },
    {
        "description": "Single digit: n='9'",
        "run": lambda: solution("9"),
        "expected": 9,
    },
    {
        "description": "All ones: n='111'",
        "run": lambda: solution("111"),
        "expected": 1,
    },
    {
        "description": "Mixed digits: n='82734'",
        "run": lambda: solution("82734"),
        "expected": 8,
    },
    {
        "description": "Large number: n='27346209830709182346'",
        "run": lambda: solution("27346209830709182346"),
        "expected": 9,
    },
]
