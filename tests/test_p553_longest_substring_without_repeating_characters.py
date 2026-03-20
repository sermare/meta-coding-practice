from problems.p553_longest_substring_without_repeating_characters import solution

TEST_CASES = [
    {
        "description": "Basic: abcabcbb -> 3",
        "run": lambda: solution("abcabcbb"),
        "expected": 3,
    },
    {
        "description": "All same: bbbbb -> 1",
        "run": lambda: solution("bbbbb"),
        "expected": 1,
    },
    {
        "description": "Mixed: pwwkew -> 3",
        "run": lambda: solution("pwwkew"),
        "expected": 3,
    },
    {
        "description": "Empty string",
        "run": lambda: solution(""),
        "expected": 0,
    },
    {
        "description": "All unique: abcdef -> 6",
        "run": lambda: solution("abcdef"),
        "expected": 6,
    },
]
