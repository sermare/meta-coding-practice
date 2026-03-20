from problems.p325_long_pressed_name import solution

TEST_CASES = [
    {
        "description": "Valid long press: alex -> aaleex",
        "run": lambda: solution("alex", "aaleex"),
        "expected": True,
    },
    {
        "description": "Invalid: saeed -> ssaaedd",
        "run": lambda: solution("saeed", "ssaaedd"),
        "expected": False,
    },
    {
        "description": "Exact match",
        "run": lambda: solution("abc", "abc"),
        "expected": True,
    },
    {
        "description": "Extra chars at end",
        "run": lambda: solution("a", "aa"),
        "expected": True,
    },
]
