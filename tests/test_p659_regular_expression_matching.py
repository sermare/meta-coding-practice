from problems.p659_regular_expression_matching import solution

TEST_CASES = [
    {
        "description": "Star matches zero: c*a*b matches aab",
        "run": lambda: solution("aab", "c*a*b"),
        "expected": True,
    },
    {
        "description": "No match: aa vs a",
        "run": lambda: solution("aa", "a"),
        "expected": False,
    },
    {
        "description": "Star matches all: a* matches aa",
        "run": lambda: solution("aa", "a*"),
        "expected": True,
    },
    {
        "description": "Dot star matches everything",
        "run": lambda: solution("ab", ".*"),
        "expected": True,
    },
    {
        "description": "Complex pattern: mississippi vs mis*is*p*.",
        "run": lambda: solution("mississippi", "mis*is*p*."),
        "expected": False,
    },
]
