from problems.p261_scramble_string import solution

TEST_CASES = [
    {
        "description": "'great', 'rgeat' -> True",
        "run": lambda: solution("great", "rgeat"),
        "expected": True,
    },
    {
        "description": "'abcde', 'caebd' -> False",
        "run": lambda: solution("abcde", "caebd"),
        "expected": False,
    },
    {
        "description": "'a', 'a' -> True",
        "run": lambda: solution("a", "a"),
        "expected": True,
    },
    {
        "description": "'abc', 'bca' -> True",
        "run": lambda: solution("abc", "bca"),
        "expected": True,
    },
    {
        "description": "'ab', 'ba' -> True",
        "run": lambda: solution("ab", "ba"),
        "expected": True,
    },
]
