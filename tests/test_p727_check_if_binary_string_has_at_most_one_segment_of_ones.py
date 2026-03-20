from problems.p727_check_if_binary_string_has_at_most_one_segment_of_ones import solution

TEST_CASES = [
    {
        "description": "Two segments: '1001'",
        "run": lambda: solution("1001"),
        "expected": False,
    },
    {
        "description": "One segment: '110'",
        "run": lambda: solution("110"),
        "expected": True,
    },
    {
        "description": "Single one: '1'",
        "run": lambda: solution("1"),
        "expected": True,
    },
    {
        "description": "All ones: '111'",
        "run": lambda: solution("111"),
        "expected": True,
    },
    {
        "description": "Separated: '10100'",
        "run": lambda: solution("10100"),
        "expected": False,
    },
]
