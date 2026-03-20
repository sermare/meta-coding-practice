from problems.p117_zigzag_conversion import solution

TEST_CASES = [
    {
        "description": "Three rows",
        "run": lambda: solution("PAYPALISHIRING", 3),
        "expected": "PAHNAPLSIIGYIR",
    },
    {
        "description": "Four rows",
        "run": lambda: solution("PAYPALISHIRING", 4),
        "expected": "PINALSIGYAHRPI",
    },
    {
        "description": "Single row (no change)",
        "run": lambda: solution("ABCDEF", 1),
        "expected": "ABCDEF",
    },
    {
        "description": "Rows equal to string length",
        "run": lambda: solution("ABC", 3),
        "expected": "ABC",
    },
    {
        "description": "Two rows",
        "run": lambda: solution("ABCDE", 2),
        "expected": "ACEBD",
    },
]
