from problems.p445_splitting_a_string_into_descending_consecutive_values import solution

TEST_CASES = [
    {
        "description": "Basic: 050043",
        "run": lambda: solution("050043"),
        "expected": True,
    },
    {
        "description": "Cannot split: 9080701",
        "run": lambda: solution("9080701"),
        "expected": False,
    },
    {
        "description": "Simple descending: 10",
        "run": lambda: solution("10"),
        "expected": True,
    },
    {
        "description": "Single digit: 1",
        "run": lambda: solution("1"),
        "expected": False,
    },
    {
        "description": "Consecutive: 321",
        "run": lambda: solution("321"),
        "expected": True,
    },
]
