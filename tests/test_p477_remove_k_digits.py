from problems.p477_remove_k_digits import solution

TEST_CASES = [
    {
        "description": ""1432219" k=3 -> "1219"",
        "run": lambda: solution("1432219", 3),
        "expected": "1219",
    },
    {
        "description": ""10200" k=1 -> "200"",
        "run": lambda: solution("10200", 1),
        "expected": "200",
    },
    {
        "description": ""10" k=2 -> "0"",
        "run": lambda: solution("10", 2),
        "expected": "0",
    },
    {
        "description": ""9" k=1 -> "0"",
        "run": lambda: solution("9", 1),
        "expected": "0",
    },
    {
        "description": ""112" k=1 -> "11"",
        "run": lambda: solution("112", 1),
        "expected": "11",
    },
]
