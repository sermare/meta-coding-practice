from problems.p301_valid_anagram import solution

TEST_CASES = [
    {
        "description": "Valid anagram: anagram/nagaram",
        "run": lambda: solution("anagram", "nagaram"),
        "expected": True,
    },
    {
        "description": "Not anagram: rat/car",
        "run": lambda: solution("rat", "car"),
        "expected": False,
    },
    {
        "description": "Empty strings",
        "run": lambda: solution("", ""),
        "expected": True,
    },
    {
        "description": "Single char match",
        "run": lambda: solution("a", "a"),
        "expected": True,
    },
    {
        "description": "Different lengths",
        "run": lambda: solution("ab", "a"),
        "expected": False,
    },
]
