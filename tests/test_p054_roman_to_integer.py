from problems.p054_roman_to_integer import solution

TEST_CASES = [
    {
        "description": "Simple: III = 3",
        "run": lambda: solution("III"),
        "expected": 3,
    },
    {
        "description": "Mixed: LVIII = 58",
        "run": lambda: solution("LVIII"),
        "expected": 58,
    },
    {
        "description": "Subtraction cases: MCMXCIV = 1994",
        "run": lambda: solution("MCMXCIV"),
        "expected": 1994,
    },
    {
        "description": "Simple subtraction: IV = 4",
        "run": lambda: solution("IV"),
        "expected": 4,
    },
    {
        "description": "Single character: M = 1000",
        "run": lambda: solution("M"),
        "expected": 1000,
    },
]
