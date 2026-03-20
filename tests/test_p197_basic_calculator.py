from problems.p197_basic_calculator import solution

TEST_CASES = [
    {
        "description": "1 + 1 = 2",
        "run": lambda: solution("1 + 1"),
        "expected": 2,
    },
    {
        "description": "2 - 1 + 2 = 3",
        "run": lambda: solution(" 2-1 + 2 "),
        "expected": 3,
    },
    {
        "description": "Nested parentheses",
        "run": lambda: solution("(1+(4+5+2)-3)+(6+8)"),
        "expected": 23,
    },
    {
        "description": "Single number",
        "run": lambda: solution("42"),
        "expected": 42,
    },
    {
        "description": "Negation with parens",
        "run": lambda: solution("-(3+2)"),
        "expected": -5,
    },
]
