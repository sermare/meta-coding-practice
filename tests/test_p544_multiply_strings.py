from problems.p544_multiply_strings import solution

TEST_CASES = [
    {
        "description": "Basic multiply",
        "run": lambda: solution("123", "456"),
        "expected": "56088",
    },
    {
        "description": "Multiply by zero",
        "run": lambda: solution("0", "123"),
        "expected": "0",
    },
    {
        "description": "Single digits",
        "run": lambda: solution("2", "3"),
        "expected": "6",
    },
    {
        "description": "Large numbers",
        "run": lambda: solution("999", "999"),
        "expected": "998001",
    },
    {
        "description": "One and number",
        "run": lambda: solution("1", "12345"),
        "expected": "12345",
    },
]
