from problems.p324_backspace_string_compare import solution

TEST_CASES = [
    {
        "description": "Both become ac: ab#c vs ad#c",
        "run": lambda: solution("ab#c", "ad#c"),
        "expected": True,
    },
    {
        "description": "Both become empty: a## vs #a#",
        "run": lambda: solution("a##", "#a#"),
        "expected": True,
    },
    {
        "description": "Different: a#c vs b",
        "run": lambda: solution("a#c", "b"),
        "expected": False,
    },
    {
        "description": "No backspaces equal",
        "run": lambda: solution("abc", "abc"),
        "expected": True,
    },
]
