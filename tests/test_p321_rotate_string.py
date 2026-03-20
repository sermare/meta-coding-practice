from problems.p321_rotate_string import solution

TEST_CASES = [
    {
        "description": "Valid rotation: abcde -> cdeab",
        "run": lambda: solution("abcde", "cdeab"),
        "expected": True,
    },
    {
        "description": "Invalid rotation: abcde -> abced",
        "run": lambda: solution("abcde", "abced"),
        "expected": False,
    },
    {
        "description": "Same string",
        "run": lambda: solution("abc", "abc"),
        "expected": True,
    },
    {
        "description": "Different lengths",
        "run": lambda: solution("ab", "abc"),
        "expected": False,
    },
]
