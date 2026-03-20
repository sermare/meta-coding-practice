from problems.p824_count_number_of_texts import solution

TEST_CASES = [
    {
        "description": "Basic: 22233",
        "run": lambda: solution("22233"),
        "expected": 8,
    },
    {
        "description": "Single digit: 2",
        "run": lambda: solution("2"),
        "expected": 1,
    },
    {
        "description": "Four of same (key 7): 7777",
        "run": lambda: solution("7777"),
        "expected": 8,
    },
    {
        "description": "All different: 234",
        "run": lambda: solution("234"),
        "expected": 1,
    },
]
