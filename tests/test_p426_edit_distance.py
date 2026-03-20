from problems.p426_edit_distance import solution

TEST_CASES = [
    {
        "description": "Basic: horse -> ros",
        "run": lambda: solution("horse", "ros"),
        "expected": 3,
    },
    {
        "description": "Longer: intention -> execution",
        "run": lambda: solution("intention", "execution"),
        "expected": 5,
    },
    {
        "description": "Same string: abc -> abc",
        "run": lambda: solution("abc", "abc"),
        "expected": 0,
    },
    {
        "description": "Empty to string: '' -> abc",
        "run": lambda: solution("", "abc"),
        "expected": 3,
    },
    {
        "description": "Single char: a -> b",
        "run": lambda: solution("a", "b"),
        "expected": 1,
    },
]
