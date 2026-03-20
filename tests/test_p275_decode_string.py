from problems.p275_decode_string import solution

TEST_CASES = [
    {
        "description": "'3[a]2[bc]' -> 'aaabcbc'",
        "run": lambda: solution("3[a]2[bc]"),
        "expected": "aaabcbc",
    },
    {
        "description": "'3[a2[c]]' -> 'accaccacc'",
        "run": lambda: solution("3[a2[c]]"),
        "expected": "accaccacc",
    },
    {
        "description": "'2[abc]3[cd]ef' -> 'abcabccdcdcdef'",
        "run": lambda: solution("2[abc]3[cd]ef"),
        "expected": "abcabccdcdcdef",
    },
    {
        "description": "'abc' -> 'abc' (no encoding)",
        "run": lambda: solution("abc"),
        "expected": "abc",
    },
    {
        "description": "'10[a]' -> 'aaaaaaaaaa'",
        "run": lambda: solution("10[a]"),
        "expected": "aaaaaaaaaa",
    },
]
