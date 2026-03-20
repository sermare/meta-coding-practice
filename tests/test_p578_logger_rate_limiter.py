from problems.p578_logger_rate_limiter import solution

TEST_CASES = [
    {
        "description": "Standard rate limiting",
        "run": lambda: solution([[1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]),
        "expected": [True, True, False, False, False, True],
    },
    {
        "description": "Same message at exactly 10 apart",
        "run": lambda: solution([[1, "a"], [11, "a"]]),
        "expected": [True, True],
    },
    {
        "description": "Different messages always print",
        "run": lambda: solution([[1, "a"], [1, "b"], [1, "c"]]),
        "expected": [True, True, True],
    },
    {
        "description": "Same message rapid fire",
        "run": lambda: solution([[1, "x"], [2, "x"], [3, "x"]]),
        "expected": [True, False, False],
    },
]
