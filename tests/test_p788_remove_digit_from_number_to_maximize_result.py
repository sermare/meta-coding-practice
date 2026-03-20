from problems.p788_remove_digit_from_number_to_maximize_result import solution

TEST_CASES = [
    {
        "description": "Basic: '1231', digit='1'",
        "run": lambda: solution("1231", "1"),
        "expected": "231",
    },
    {
        "description": "Single occurrence: '551', digit='5'",
        "run": lambda: solution("551", "5"),
        "expected": "55",
    },
    {
        "description": "Remove last: '123', digit='3'",
        "run": lambda: solution("123", "3"),
        "expected": "12",
    },
    {
        "description": "Multiple choices: '73197', digit='7'",
        "run": lambda: solution("73197", "7"),
        "expected": "7319",
    },
]
