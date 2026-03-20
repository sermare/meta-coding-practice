from problems.p417_longest_common_subsequence import solution

TEST_CASES = [
    {
        "description": "Basic: abcde vs ace",
        "run": lambda: solution("abcde", "ace"),
        "expected": 3,
    },
    {
        "description": "Same strings: abc vs abc",
        "run": lambda: solution("abc", "abc"),
        "expected": 3,
    },
    {
        "description": "No common: abc vs def",
        "run": lambda: solution("abc", "def"),
        "expected": 0,
    },
    {
        "description": "Single match: a vs a",
        "run": lambda: solution("a", "a"),
        "expected": 1,
    },
    {
        "description": "Longer strings: oxcpqrsvwf vs shmtulqrypy",
        "run": lambda: solution("oxcpqrsvwf", "shmtulqrypy"),
        "expected": 2,
    },
]
