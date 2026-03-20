from problems.p405_longest_palindromic_substring import solution

TEST_CASES = [
    {
        "description": "Basic: babad",
        "run": lambda: solution("babad") in ("bab", "aba"),
        "expected": True,
    },
    {
        "description": "All same: cbbd",
        "run": lambda: solution("cbbd"),
        "expected": "bb",
    },
    {
        "description": "Single char: a",
        "run": lambda: solution("a"),
        "expected": "a",
    },
    {
        "description": "Full palindrome: racecar",
        "run": lambda: solution("racecar"),
        "expected": "racecar",
    },
    {
        "description": "Two chars same: ac",
        "run": lambda: solution("ac") in ("a", "c"),
        "expected": True,
    },
]
