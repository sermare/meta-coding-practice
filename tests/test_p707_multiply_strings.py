from problems.p707_multiply_strings import solution

TEST_CASES = [
    {
        "description": "Simple: '2' * '3'",
        "run": lambda: solution("2", "3"),
        "expected": "6",
    },
    {
        "description": "Multi-digit: '123' * '456'",
        "run": lambda: solution("123", "456"),
        "expected": "56088",
    },
    {
        "description": "Multiply by zero: '0' * '0'",
        "run": lambda: solution("0", "0"),
        "expected": "0",
    },
    {
        "description": "One is zero: '999' * '0'",
        "run": lambda: solution("999", "0"),
        "expected": "0",
    },
    {
        "description": "Large numbers: '498828660196' * '840477629533'",
        "run": lambda: solution("498828660196", "840477629533"),
        "expected": "419254329864656431168468",
    },
]
