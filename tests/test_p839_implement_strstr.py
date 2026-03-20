from problems.p839_implement_strstr import solution

TEST_CASES = [
    {
        "description": "Found at start: sadbutsad, sad",
        "run": lambda: solution("sadbutsad", "sad"),
        "expected": 0,
    },
    {
        "description": "Not found: leetcode, leeto",
        "run": lambda: solution("leetcode", "leeto"),
        "expected": -1,
    },
    {
        "description": "Found in middle: hello, ll",
        "run": lambda: solution("hello", "ll"),
        "expected": 2,
    },
    {
        "description": "Empty needle",
        "run": lambda: solution("abc", ""),
        "expected": 0,
    },
]
