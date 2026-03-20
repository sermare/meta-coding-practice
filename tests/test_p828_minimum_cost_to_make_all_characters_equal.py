from problems.p828_minimum_cost_to_make_all_characters_equal import solution

TEST_CASES = [
    {
        "description": "Basic: 0011",
        "run": lambda: solution("0011"),
        "expected": 2,
    },
    {
        "description": "Already equal: 0000",
        "run": lambda: solution("0000"),
        "expected": 0,
    },
    {
        "description": "Alternating: 010101",
        "run": lambda: solution("010101"),
        "expected": 9,
    },
    {
        "description": "Single char: 1",
        "run": lambda: solution("1"),
        "expected": 0,
    },
]
