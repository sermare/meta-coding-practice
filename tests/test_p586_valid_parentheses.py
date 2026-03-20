from problems.p586_valid_parentheses import solution

TEST_CASES = [
    {
        "description": "Simple pair: ()",
        "run": lambda: solution("()"),
        "expected": True,
    },
    {
        "description": "Multiple types: ()[]{}",
        "run": lambda: solution("()[]{}"),
        "expected": True,
    },
    {
        "description": "Mismatched: (]",
        "run": lambda: solution("(]"),
        "expected": False,
    },
    {
        "description": "Nested: {[]}",
        "run": lambda: solution("{[]}"),
        "expected": True,
    },
    {
        "description": "Empty string",
        "run": lambda: solution(""),
        "expected": True,
    },
]
