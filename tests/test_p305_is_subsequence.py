from problems.p305_is_subsequence import solution

TEST_CASES = [
    {
        "description": "Valid subsequence: abc in ahbgdc",
        "run": lambda: solution("abc", "ahbgdc"),
        "expected": True,
    },
    {
        "description": "Invalid subsequence: axc in ahbgdc",
        "run": lambda: solution("axc", "ahbgdc"),
        "expected": False,
    },
    {
        "description": "Empty s is always subsequence",
        "run": lambda: solution("", "ahbgdc"),
        "expected": True,
    },
    {
        "description": "Equal strings",
        "run": lambda: solution("abc", "abc"),
        "expected": True,
    },
    {
        "description": "s longer than t",
        "run": lambda: solution("abcdef", "abc"),
        "expected": False,
    },
]
