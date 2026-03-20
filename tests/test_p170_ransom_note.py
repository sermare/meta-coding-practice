from problems.p170_ransom_note import solution

TEST_CASES = [
    {
        "description": "'a' from 'b' -> False",
        "run": lambda: solution("a", "b"),
        "expected": False,
    },
    {
        "description": "'aa' from 'ab' -> False",
        "run": lambda: solution("aa", "ab"),
        "expected": False,
    },
    {
        "description": "'aa' from 'aab' -> True",
        "run": lambda: solution("aa", "aab"),
        "expected": True,
    },
    {
        "description": "Empty ransom note -> True",
        "run": lambda: solution("", "abc"),
        "expected": True,
    },
]
