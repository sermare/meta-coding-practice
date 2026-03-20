from problems.p255_wildcard_matching import solution

TEST_CASES = [
    {
        "description": "'cb' matches '?a' -> False",
        "run": lambda: solution("cb", "?a"),
        "expected": False,
    },
    {
        "description": "'adceb' matches '*a*b' -> True",
        "run": lambda: solution("adceb", "*a*b"),
        "expected": True,
    },
    {
        "description": "'aa' matches 'a' -> False",
        "run": lambda: solution("aa", "a"),
        "expected": False,
    },
    {
        "description": "'aa' matches '*' -> True",
        "run": lambda: solution("aa", "*"),
        "expected": True,
    },
    {
        "description": "Empty string matches empty pattern -> True",
        "run": lambda: solution("", ""),
        "expected": True,
    },
]
