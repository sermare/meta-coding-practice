from problems.p091_longest_palindromic_substring import solution

TEST_CASES = [
    {
        "description": "Basic: babad -> bab or aba",
        "run": lambda: solution("babad") in ("bab", "aba"),
        "expected": True,
    },
    {
        "description": "Even palindrome: cbbd -> bb",
        "run": lambda: solution("cbbd"),
        "expected": "bb",
    },
    {
        "description": "Single char: a",
        "run": lambda: solution("a"),
        "expected": "a",
    },
    {
        "description": "All same: aaaa",
        "run": lambda: solution("aaaa"),
        "expected": "aaaa",
    },
    {
        "description": "Full palindrome: racecar",
        "run": lambda: solution("racecar"),
        "expected": "racecar",
    },
]
