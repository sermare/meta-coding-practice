from problems.p833_minimum_number_of_changes_to_make_binary_string_beautiful import solution

TEST_CASES = [
    {
        "description": "Basic: 1001",
        "run": lambda: solution("1001"),
        "expected": 2,
    },
    {
        "description": "Already beautiful: 1100",
        "run": lambda: solution("1100"),
        "expected": 0,
    },
    {
        "description": "Alternating: 0101",
        "run": lambda: solution("0101"),
        "expected": 2,
    },
    {
        "description": "All same: 0000",
        "run": lambda: solution("0000"),
        "expected": 0,
    },
]
