from problems.p832_maximum_odd_binary_number import solution

TEST_CASES = [
    {
        "description": "Basic: 010",
        "run": lambda: solution("010"),
        "expected": "001",
    },
    {
        "description": "Multiple ones: 0101",
        "run": lambda: solution("0101"),
        "expected": "1001",
    },
    {
        "description": "All ones: 111",
        "run": lambda: solution("111"),
        "expected": "111",
    },
    {
        "description": "Single one: 1",
        "run": lambda: solution("1"),
        "expected": "1",
    },
]
