from problems.p288_repeated_substring_pattern import solution

TEST_CASES = [
    {
        "description": "'abab' -> True",
        "run": lambda: solution("abab"),
        "expected": True,
    },
    {
        "description": "'aba' -> False",
        "run": lambda: solution("aba"),
        "expected": False,
    },
    {
        "description": "'abcabcabc' -> True",
        "run": lambda: solution("abcabcabc"),
        "expected": True,
    },
    {
        "description": "'a' -> False",
        "run": lambda: solution("a"),
        "expected": False,
    },
    {
        "description": "'aaa' -> True",
        "run": lambda: solution("aaa"),
        "expected": True,
    },
]
