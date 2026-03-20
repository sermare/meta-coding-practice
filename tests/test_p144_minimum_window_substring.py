from problems.p144_minimum_window_substring import solution

TEST_CASES = [
    {
        "description": "Standard minimum window",
        "run": lambda: solution("ADOBECODEBANC", "ABC"),
        "expected": "BANC",
    },
    {
        "description": "Entire string is the window",
        "run": lambda: solution("a", "a"),
        "expected": "a",
    },
    {
        "description": "No valid window",
        "run": lambda: solution("a", "aa"),
        "expected": "",
    },
    {
        "description": "Window at the beginning",
        "run": lambda: solution("abcdef", "abc"),
        "expected": "abc",
    },
    {
        "description": "Duplicate characters in t",
        "run": lambda: solution("aaabbbccc", "abc"),
        "expected": "abbbc",
    },
]
