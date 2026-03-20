from problems.p616_valid_number import solution

TEST_CASES = [
    {
        "description": "Simple integer: '0'",
        "run": lambda: solution("0"),
        "expected": True,
    },
    {
        "description": "Just e: 'e'",
        "run": lambda: solution("e"),
        "expected": False,
    },
    {
        "description": "Just dot: '.'",
        "run": lambda: solution("."),
        "expected": False,
    },
    {
        "description": "Scientific notation: '2e10'",
        "run": lambda: solution("2e10"),
        "expected": True,
    },
    {
        "description": "Negative decimal: '-0.1'",
        "run": lambda: solution("-0.1"),
        "expected": True,
    },
]
