from problems.p829_minimum_additions_to_make_valid_string import solution

TEST_CASES = [
    {
        "description": "Single b: need a and c",
        "run": lambda: solution("b"),
        "expected": 2,
    },
    {
        "description": "Already valid: abc",
        "run": lambda: solution("abc"),
        "expected": 0,
    },
    {
        "description": "aaa: need 6",
        "run": lambda: solution("aaa"),
        "expected": 6,
    },
    {
        "description": "c: need a and b",
        "run": lambda: solution("c"),
        "expected": 2,
    },
]
