from problems.p259_minimum_window_substring import solution

TEST_CASES = [
    {
        "description": "'ADOBECODEBANC', 'ABC' -> 'BANC'",
        "run": lambda: solution("ADOBECODEBANC", "ABC"),
        "expected": "BANC",
    },
    {
        "description": "'a', 'a' -> 'a'",
        "run": lambda: solution("a", "a"),
        "expected": "a",
    },
    {
        "description": "'a', 'aa' -> '' (not enough chars)",
        "run": lambda: solution("a", "aa"),
        "expected": "",
    },
    {
        "description": "'abc', 'cba' -> 'abc'",
        "run": lambda: solution("abc", "cba"),
        "expected": "abc",
    },
    {
        "description": "'ab', 'b' -> 'b'",
        "run": lambda: solution("ab", "b"),
        "expected": "b",
    },
]
