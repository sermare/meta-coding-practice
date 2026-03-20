from problems.p323_buddy_strings import solution

TEST_CASES = [
    {
        "description": "Can swap: ab -> ba",
        "run": lambda: solution("ab", "ba"),
        "expected": True,
    },
    {
        "description": "Same no duplicates: ab -> ab",
        "run": lambda: solution("ab", "ab"),
        "expected": False,
    },
    {
        "description": "Same with duplicates: aa -> aa",
        "run": lambda: solution("aa", "aa"),
        "expected": True,
    },
    {
        "description": "Different lengths",
        "run": lambda: solution("ab", "abc"),
        "expected": False,
    },
    {
        "description": "More than 2 diffs",
        "run": lambda: solution("abcd", "dcba"),
        "expected": False,
    },
]
