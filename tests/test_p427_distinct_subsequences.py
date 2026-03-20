from problems.p427_distinct_subsequences import solution

TEST_CASES = [
    {
        "description": "Basic: rabbbit vs rabbit",
        "run": lambda: solution("rabbbit", "rabbit"),
        "expected": 3,
    },
    {
        "description": "Longer: babgbag vs bag",
        "run": lambda: solution("babgbag", "bag"),
        "expected": 5,
    },
    {
        "description": "No match: abc vs d",
        "run": lambda: solution("abc", "d"),
        "expected": 0,
    },
    {
        "description": "Same strings: a vs a",
        "run": lambda: solution("a", "a"),
        "expected": 1,
    },
    {
        "description": "Repeated chars: aaa vs a",
        "run": lambda: solution("aaa", "a"),
        "expected": 3,
    },
]
