from problems.p051_longest_substring_without_repeating_characters import solution

TEST_CASES = [
    {
        "description": "Basic case: abcabcbb",
        "run": lambda: solution("abcabcbb"),
        "expected": 3,
    },
    {
        "description": "All same characters: bbbbb",
        "run": lambda: solution("bbbbb"),
        "expected": 1,
    },
    {
        "description": "Repeating pattern: pwwkew",
        "run": lambda: solution("pwwkew"),
        "expected": 3,
    },
    {
        "description": "Empty string",
        "run": lambda: solution(""),
        "expected": 0,
    },
    {
        "description": "Single character: a",
        "run": lambda: solution("a"),
        "expected": 1,
    },
]
