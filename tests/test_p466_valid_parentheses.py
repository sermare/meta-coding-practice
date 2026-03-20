from problems.p466_valid_parentheses import solution

TEST_CASES = [
    {
        "description": "Simple pair: "()"",
        "run": lambda: solution("()"),
        "expected": True,
    },
    {
        "description": "All types: "()[]{}"",
        "run": lambda: solution("()[]{}"),
        "expected": True,
    },
    {
        "description": "Mismatch: "(]"",
        "run": lambda: solution("(]"),
        "expected": False,
    },
    {
        "description": "Nested: "{[]}"",
        "run": lambda: solution("{[]}"),
        "expected": True,
    },
    {
        "description": "Unclosed: "((("",
        "run": lambda: solution("((("),
        "expected": False,
    },
]
