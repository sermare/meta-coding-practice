from problems.p479_decode_string import solution

TEST_CASES = [
    {
        "description": ""3[a]2[bc]" -> "aaabcbc"",
        "run": lambda: solution("3[a]2[bc]"),
        "expected": "aaabcbc",
    },
    {
        "description": "Nested: "3[a2[c]]" -> "accaccacc"",
        "run": lambda: solution("3[a2[c]]"),
        "expected": "accaccacc",
    },
    {
        "description": "Mixed: "2[abc]3[cd]ef"",
        "run": lambda: solution("2[abc]3[cd]ef"),
        "expected": "abcabccdcdcdef",
    },
    {
        "description": "No encoding: "abc"",
        "run": lambda: solution("abc"),
        "expected": "abc",
    },
    {
        "description": "Single repeat: "1[a]"",
        "run": lambda: solution("1[a]"),
        "expected": "a",
    },
]
