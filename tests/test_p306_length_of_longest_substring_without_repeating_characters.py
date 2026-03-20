from problems.p306_length_of_longest_substring_without_repeating_characters import solution

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
        "description": "Empty string -> 0",
        "run": lambda: solution(""),
        "expected": 0,
    },
    {
        "description": "Single char -> 1",
        "run": lambda: solution("a"),
        "expected": 1,
    },
]
