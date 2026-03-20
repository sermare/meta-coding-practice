from problems.p643_word_break import solution

TEST_CASES = [
    {
        "description": "Can break: 'leetcode' with ['leet','code']",
        "run": lambda: solution("leetcode", ["leet", "code"]),
        "expected": True,
    },
    {
        "description": "Reuse words: 'applepenapple'",
        "run": lambda: solution("applepenapple", ["apple", "pen"]),
        "expected": True,
    },
    {
        "description": "Cannot break: 'catsandog'",
        "run": lambda: solution("catsandog", ["cats", "dog", "sand", "and", "cat"]),
        "expected": False,
    },
    {
        "description": "Single character",
        "run": lambda: solution("a", ["a"]),
        "expected": True,
    },
    {
        "description": "Empty string",
        "run": lambda: solution("", ["a"]),
        "expected": True,
    },
]
