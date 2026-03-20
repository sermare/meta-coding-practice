from problems.p016_word_break import solution


TEST_CASES = [
    {
        "description": "leetcode -> leet + code",
        "run": lambda: solution("leetcode", ["leet", "code"]),
        "expected": True,
    },
    {
        "description": "applepenapple -> apple + pen + apple",
        "run": lambda: solution("applepenapple", ["apple", "pen"]),
        "expected": True,
    },
    {
        "description": "catsandog cannot be segmented",
        "run": lambda: solution("catsandog", ["cats", "dog", "sand", "and", "cat"]),
        "expected": False,
    },
    {
        "description": "Single character matches single word",
        "run": lambda: solution("a", ["a"]),
        "expected": True,
    },
    {
        "description": "aaaaaaa using aaa and aaaa",
        "run": lambda: solution("aaaaaaa", ["aaa", "aaaa"]),
        "expected": True,
    },
]
