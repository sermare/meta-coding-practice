from problems.p580_minimum_window_substring import solution

TEST_CASES = [
    {
        "description": "Standard: ADOBECODEBANC, ABC -> BANC",
        "run": lambda: solution("ADOBECODEBANC", "ABC"),
        "expected": "BANC",
    },
    {
        "description": "Exact match: a, a -> a",
        "run": lambda: solution("a", "a"),
        "expected": "a",
    },
    {
        "description": "Impossible: a, aa -> empty",
        "run": lambda: solution("a", "aa"),
        "expected": "",
    },
    {
        "description": "Full string is window",
        "run": lambda: solution("abc", "abc"),
        "expected": "abc",
    },
    {
        "description": "Single char target: ab, b -> b",
        "run": lambda: solution("ab", "b"),
        "expected": "b",
    },
]
