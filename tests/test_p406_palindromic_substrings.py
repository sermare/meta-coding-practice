from problems.p406_palindromic_substrings import solution

TEST_CASES = [
    {
        "description": "Simple: abc",
        "run": lambda: solution("abc"),
        "expected": 3,
    },
    {
        "description": "With palindrome: aaa",
        "run": lambda: solution("aaa"),
        "expected": 6,
    },
    {
        "description": "Single char: a",
        "run": lambda: solution("a"),
        "expected": 1,
    },
    {
        "description": "Two same chars: aa",
        "run": lambda: solution("aa"),
        "expected": 3,
    },
    {
        "description": "Mixed: abba",
        "run": lambda: solution("abba"),
        "expected": 6,
    },
]
