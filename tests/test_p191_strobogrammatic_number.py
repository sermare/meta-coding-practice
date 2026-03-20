from problems.p191_strobogrammatic_number import solution

TEST_CASES = [
    {
        "description": "69 is strobogrammatic",
        "run": lambda: solution("69"),
        "expected": True,
    },
    {
        "description": "88 is strobogrammatic",
        "run": lambda: solution("88"),
        "expected": True,
    },
    {
        "description": "962 is not strobogrammatic",
        "run": lambda: solution("962"),
        "expected": False,
    },
    {
        "description": "1 is strobogrammatic",
        "run": lambda: solution("1"),
        "expected": True,
    },
    {
        "description": "2 is not strobogrammatic",
        "run": lambda: solution("2"),
        "expected": False,
    },
]
