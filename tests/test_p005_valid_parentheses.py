from problems.p005_valid_parentheses import solution

TEST_CASES = [
    {
        "description": "Simple valid: '()'",
        "run": lambda: solution("()"),
        "expected": True,
    },
    {
        "description": "Multiple valid types: '()[]{}'",
        "run": lambda: solution("()[]{}"),
        "expected": True,
    },
    {
        "description": "Mismatched types: '(]'",
        "run": lambda: solution("(]"),
        "expected": False,
    },
    {
        "description": "Interleaved invalid: '([)]'",
        "run": lambda: solution("([)]"),
        "expected": False,
    },
    {
        "description": "Nested valid: '{[]}'",
        "run": lambda: solution("{[]}"),
        "expected": True,
    },
]
