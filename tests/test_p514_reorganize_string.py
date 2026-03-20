from problems.p514_reorganize_string import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution("aab"),
        "expected": "aba",
    },
    {
        "description": "Impossible case",
        "run": lambda: solution("aaab"),
        "expected": "",
    },
    {
        "description": "Single char",
        "run": lambda: solution("a"),
        "expected": "a",
    },
    {
        "description": "Two different chars",
        "run": lambda: solution("ab"),
        "expected": "ab",
    },
    {
        "description": "Already valid",
        "run": lambda: solution("abcabc"),
        "expected": "abcabc",
    },
]
