from problems.p429_regular_expression_matching import solution

TEST_CASES = [
    {
        "description": "No match: aa vs a",
        "run": lambda: solution("aa", "a"),
        "expected": False,
    },
    {
        "description": "Star match: aa vs a*",
        "run": lambda: solution("aa", "a*"),
        "expected": True,
    },
    {
        "description": "Dot star: ab vs .*",
        "run": lambda: solution("ab", ".*"),
        "expected": True,
    },
    {
        "description": "Complex: aab vs c*a*b",
        "run": lambda: solution("aab", "c*a*b"),
        "expected": True,
    },
    {
        "description": "Empty pattern: a vs empty",
        "run": lambda: solution("a", ""),
        "expected": False,
    },
]
