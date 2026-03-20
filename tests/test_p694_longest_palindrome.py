from problems.p694_longest_palindrome import solution

TEST_CASES = [
    {
        "description": "Basic: abccccdd",
        "run": lambda: solution("abccccdd"),
        "expected": 7,
    },
    {
        "description": "Single character: a",
        "run": lambda: solution("a"),
        "expected": 1,
    },
    {
        "description": "All same: aaaa",
        "run": lambda: solution("aaaa"),
        "expected": 4,
    },
    {
        "description": "All unique: abcdef",
        "run": lambda: solution("abcdef"),
        "expected": 1,
    },
    {
        "description": "Case sensitive: Aa",
        "run": lambda: solution("Aa"),
        "expected": 1,
    },
]
