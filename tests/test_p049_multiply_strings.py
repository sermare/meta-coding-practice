from problems.p049_multiply_strings import solution

TEST_CASES = [
    {
        "description": "2 * 3 = 6",
        "run": lambda: solution("2", "3"),
        "expected": "6",
    },
    {
        "description": "123 * 456 = 56088",
        "run": lambda: solution("123", "456"),
        "expected": "56088",
    },
    {
        "description": "0 * 0 = 0",
        "run": lambda: solution("0", "0"),
        "expected": "0",
    },
    {
        "description": "999 * 999 = 998001",
        "run": lambda: solution("999", "999"),
        "expected": "998001",
    },
    {
        "description": "123456789 * 987654321 = 121932631112635269",
        "run": lambda: solution("123456789", "987654321"),
        "expected": "121932631112635269",
    },
]
