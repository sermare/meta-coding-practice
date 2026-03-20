from problems.p118_string_to_integer_atoi import solution

TEST_CASES = [
    {
        "description": "Simple positive number",
        "run": lambda: solution("42"),
        "expected": 42,
    },
    {
        "description": "Leading whitespace and negative",
        "run": lambda: solution("   -42"),
        "expected": -42,
    },
    {
        "description": "Trailing non-digit characters",
        "run": lambda: solution("4193 with words"),
        "expected": 4193,
    },
    {
        "description": "Overflow clamps to INT_MAX",
        "run": lambda: solution("91283472332"),
        "expected": 2147483647,
    },
    {
        "description": "Leading non-digit returns 0",
        "run": lambda: solution("words and 987"),
        "expected": 0,
    },
]
