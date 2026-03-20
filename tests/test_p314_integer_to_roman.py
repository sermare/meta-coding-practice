from problems.p314_integer_to_roman import solution

TEST_CASES = [
    {
        "description": "3749 -> MMMDCCXLIX",
        "run": lambda: solution(3749),
        "expected": "MMMDCCXLIX",
    },
    {
        "description": "58 -> LVIII",
        "run": lambda: solution(58),
        "expected": "LVIII",
    },
    {
        "description": "1994 -> MCMXCIV",
        "run": lambda: solution(1994),
        "expected": "MCMXCIV",
    },
    {
        "description": "4 -> IV",
        "run": lambda: solution(4),
        "expected": "IV",
    },
    {
        "description": "9 -> IX",
        "run": lambda: solution(9),
        "expected": "IX",
    },
]
