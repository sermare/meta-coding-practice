from problems.p849_interleaving_string import solution

TEST_CASES = [
    {
        "description": "Valid interleaving: aabcc + dbbca = aadbbcbcac",
        "run": lambda: solution("aabcc", "dbbca", "aadbbcbcac"),
        "expected": True,
    },
    {
        "description": "Invalid: aabcc + dbbca = aadbbbaccc",
        "run": lambda: solution("aabcc", "dbbca", "aadbbbaccc"),
        "expected": False,
    },
    {
        "description": "Empty strings",
        "run": lambda: solution("", "", ""),
        "expected": True,
    },
    {
        "description": "One empty: s1=abc, s2='', s3=abc",
        "run": lambda: solution("abc", "", "abc"),
        "expected": True,
    },
]
