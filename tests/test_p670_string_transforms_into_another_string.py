from problems.p670_string_transforms_into_another_string import solution

TEST_CASES = [
    {
        "description": "Transformable: aabcc -> ccdee",
        "run": lambda: solution("aabcc", "ccdee"),
        "expected": True,
    },
    {
        "description": "Not transformable: all 26 chars to different",
        "run": lambda: solution("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"),
        "expected": False,
    },
    {
        "description": "Identical strings",
        "run": lambda: solution("abc", "abc"),
        "expected": True,
    },
    {
        "description": "Simple swap: ab -> ba",
        "run": lambda: solution("ab", "ba"),
        "expected": True,
    },
]
