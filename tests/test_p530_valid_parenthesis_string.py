from problems.p530_valid_parenthesis_string import solution

TEST_CASES = [
    {
        "description": "Star as close paren",
        "run": lambda: solution("(*))"),
        "expected": True,
    },
    {
        "description": "Empty star",
        "run": lambda: solution("(*)"),
        "expected": True,
    },
    {
        "description": "All stars",
        "run": lambda: solution("***"),
        "expected": True,
    },
    {
        "description": "Invalid",
        "run": lambda: solution("((("),
        "expected": False,
    },
    {
        "description": "Empty string",
        "run": lambda: solution(""),
        "expected": True,
    },
]
