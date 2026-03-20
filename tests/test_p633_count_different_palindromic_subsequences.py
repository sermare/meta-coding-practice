from problems.p633_count_different_palindromic_subsequences import solution

TEST_CASES = [
    {
        "description": "Basic case: 'bccb'",
        "run": lambda: solution("bccb"),
        "expected": 6,
    },
    {
        "description": "Single char: 'a'",
        "run": lambda: solution("a"),
        "expected": 1,
    },
    {
        "description": "Two same chars: 'aa'",
        "run": lambda: solution("aa"),
        "expected": 2,
    },
    {
        "description": "Two different chars: 'ab'",
        "run": lambda: solution("ab"),
        "expected": 2,
    },
    {
        "description": "Long string with mod",
        "run": lambda: solution("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"),
        "expected": 104860361,
    },
]
