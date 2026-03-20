from problems.p568_minimum_remove_to_make_valid_parentheses import solution

TEST_CASES = [
    {
        "description": "Remove trailing paren",
        "run": lambda: solution("lee(t(c)o)de)"),
        "expected": "lee(t(c)o)de",
    },
    {
        "description": "Remove leading paren",
        "run": lambda: solution("a)b(c)d"),
        "expected": "ab(c)d",
    },
    {
        "description": "All invalid: ))((  -> empty",
        "run": lambda: solution("))(("),
        "expected": "",
    },
    {
        "description": "Already valid",
        "run": lambda: solution("(a)(b)"),
        "expected": "(a)(b)",
    },
    {
        "description": "No parentheses",
        "run": lambda: solution("abc"),
        "expected": "abc",
    },
]
