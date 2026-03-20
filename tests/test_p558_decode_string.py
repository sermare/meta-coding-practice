from problems.p558_decode_string import solution

TEST_CASES = [
    {
        "description": "Simple: 3[a]2[bc] -> aaabcbc",
        "run": lambda: solution("3[a]2[bc]"),
        "expected": "aaabcbc",
    },
    {
        "description": "Nested: 3[a2[c]] -> accaccacc",
        "run": lambda: solution("3[a2[c]]"),
        "expected": "accaccacc",
    },
    {
        "description": "Mixed: 2[abc]3[cd]ef -> abcabccdcdcdef",
        "run": lambda: solution("2[abc]3[cd]ef"),
        "expected": "abcabccdcdcdef",
    },
    {
        "description": "No encoding: abc",
        "run": lambda: solution("abc"),
        "expected": "abc",
    },
    {
        "description": "Double digit: 10[a]",
        "run": lambda: solution("10[a]"),
        "expected": "aaaaaaaaaa",
    },
]
