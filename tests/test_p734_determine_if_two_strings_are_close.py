from problems.p734_determine_if_two_strings_are_close import solution

TEST_CASES = [
    {
        "description": "Close strings: 'abc' and 'bca'",
        "run": lambda: solution("abc", "bca"),
        "expected": True,
    },
    {
        "description": "Not close: 'a' and 'aa'",
        "run": lambda: solution("a", "aa"),
        "expected": False,
    },
    {
        "description": "Close via transform: 'cabbba' and 'abbccc'",
        "run": lambda: solution("cabbba", "abbccc"),
        "expected": True,
    },
    {
        "description": "Different chars: 'aab' and 'bba'",
        "run": lambda: solution("aab", "bba"),
        "expected": True,
    },
    {
        "description": "Different char sets: 'abc' and 'abd'",
        "run": lambda: solution("abc", "abd"),
        "expected": False,
    },
]
