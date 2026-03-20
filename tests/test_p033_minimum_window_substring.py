from problems.p033_minimum_window_substring import solution

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
        "description": "'a', 'aa' -> '' (not enough characters)",
        "run": lambda: solution("a", "aa"),
        "expected": "",
    },
    {
        "description": "'aa', 'aa' -> 'aa'",
        "run": lambda: solution("aa", "aa"),
        "expected": "aa",
    },
    {
        "description": "'cabwefgewcwaefgcf', 'cae' -> 'cwae'",
        "run": lambda: solution("cabwefgewcwaefgcf", "cae"),
        "expected": "cwae",
    },
]
