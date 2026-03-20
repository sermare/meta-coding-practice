from problems.p584_string_to_integer_atoi import solution

TEST_CASES = [
    {
        "description": "Simple number: 42",
        "run": lambda: solution("42"),
        "expected": 42,
    },
    {
        "description": "Negative with spaces: -42",
        "run": lambda: solution("   -42"),
        "expected": -42,
    },
    {
        "description": "Trailing words: 4193",
        "run": lambda: solution("4193 with words"),
        "expected": 4193,
    },
    {
        "description": "Leading words: 0",
        "run": lambda: solution("words and 987"),
        "expected": 0,
    },
    {
        "description": "Overflow clamped to INT_MAX",
        "run": lambda: solution("91283472332"),
        "expected": 2147483647,
    },
]
