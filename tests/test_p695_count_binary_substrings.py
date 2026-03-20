from problems.p695_count_binary_substrings import solution

TEST_CASES = [
    {
        "description": "Basic: 00110011",
        "run": lambda: solution("00110011"),
        "expected": 6,
    },
    {
        "description": "Simple: 10101",
        "run": lambda: solution("10101"),
        "expected": 4,
    },
    {
        "description": "All same: 0000",
        "run": lambda: solution("0000"),
        "expected": 0,
    },
    {
        "description": "Minimal: 01",
        "run": lambda: solution("01"),
        "expected": 1,
    },
    {
        "description": "Longer groups: 00011011",
        "run": lambda: solution("00011011"),
        "expected": 4,
    },
]
