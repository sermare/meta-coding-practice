from problems.p315_zigzag_conversion import solution

TEST_CASES = [
    {
        "description": "3 rows: PAYPALISHIRING",
        "run": lambda: solution("PAYPALISHIRING", 3),
        "expected": "PAHNAPLSIIGYIR",
    },
    {
        "description": "4 rows: PAYPALISHIRING",
        "run": lambda: solution("PAYPALISHIRING", 4),
        "expected": "PINALSIGYAHRPI",
    },
    {
        "description": "1 row: no change",
        "run": lambda: solution("ABCD", 1),
        "expected": "ABCD",
    },
    {
        "description": "Single char",
        "run": lambda: solution("A", 1),
        "expected": "A",
    },
]
