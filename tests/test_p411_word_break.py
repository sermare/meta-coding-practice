from problems.p411_word_break import solution

TEST_CASES = [
    {
        "description": "Basic: leetcode",
        "run": lambda: solution("leetcode", ["leet", "code"]),
        "expected": True,
    },
    {
        "description": "Reuse words: applepenapple",
        "run": lambda: solution("applepenapple", ["apple", "pen"]),
        "expected": True,
    },
    {
        "description": "Impossible: catsandog",
        "run": lambda: solution("catsandog", ["cats", "dog", "sand", "and", "cat"]),
        "expected": False,
    },
    {
        "description": "Single char: a",
        "run": lambda: solution("a", ["a"]),
        "expected": True,
    },
    {
        "description": "Empty dict match fails: abc",
        "run": lambda: solution("abc", ["a", "b"]),
        "expected": False,
    },
]
