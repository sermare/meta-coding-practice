from problems.p585_roman_to_integer import solution

TEST_CASES = [
    {
        "description": "III -> 3",
        "run": lambda: solution("III"),
        "expected": 3,
    },
    {
        "description": "LVIII -> 58",
        "run": lambda: solution("LVIII"),
        "expected": 58,
    },
    {
        "description": "MCMXCIV -> 1994",
        "run": lambda: solution("MCMXCIV"),
        "expected": 1994,
    },
    {
        "description": "IV -> 4",
        "run": lambda: solution("IV"),
        "expected": 4,
    },
    {
        "description": "IX -> 9",
        "run": lambda: solution("IX"),
        "expected": 9,
    },
]
