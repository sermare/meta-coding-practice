from problems.p113_longest_palindromic_substring import solution

TEST_CASES = [
    {
        "description": "Odd length palindrome",
        "run": lambda: solution("babad") in ["bab", "aba"],
        "expected": True,
    },
    {
        "description": "Even length palindrome",
        "run": lambda: solution("cbbd"),
        "expected": "bb",
    },
    {
        "description": "Single character",
        "run": lambda: solution("x"),
        "expected": "x",
    },
    {
        "description": "Entire string is palindrome",
        "run": lambda: solution("racecar"),
        "expected": "racecar",
    },
    {
        "description": "Two characters same",
        "run": lambda: solution("aa"),
        "expected": "aa",
    },
]
