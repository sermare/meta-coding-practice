from problems.p265_valid_palindrome_ii import solution

TEST_CASES = [
    {
        "description": "'aba' -> True",
        "run": lambda: solution("aba"),
        "expected": True,
    },
    {
        "description": "'abca' -> True (remove c)",
        "run": lambda: solution("abca"),
        "expected": True,
    },
    {
        "description": "'abc' -> False",
        "run": lambda: solution("abc"),
        "expected": False,
    },
    {
        "description": "'a' -> True",
        "run": lambda: solution("a"),
        "expected": True,
    },
    {
        "description": "'deeee' -> True",
        "run": lambda: solution("deeee"),
        "expected": False,
    },
]
