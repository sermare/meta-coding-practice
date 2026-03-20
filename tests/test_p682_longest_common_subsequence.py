from problems.p682_longest_common_subsequence import solution

TEST_CASES = [
    {
        "description": "Basic: abcde and ace",
        "run": lambda: solution("abcde", "ace"),
        "expected": 3,
    },
    {
        "description": "Identical strings",
        "run": lambda: solution("abc", "abc"),
        "expected": 3,
    },
    {
        "description": "No common subsequence",
        "run": lambda: solution("abc", "def"),
        "expected": 0,
    },
    {
        "description": "Single char match",
        "run": lambda: solution("a", "a"),
        "expected": 1,
    },
    {
        "description": "Longer strings: oxcpqrsvwf and shmtulqrypy",
        "run": lambda: solution("oxcpqrsvwf", "shmtulqrypy"),
        "expected": 2,
    },
]
