from problems.p153_excel_sheet_column_number import solution

TEST_CASES = [
    {
        "description": "Single letter A -> 1",
        "run": lambda: solution("A"),
        "expected": 1,
    },
    {
        "description": "AB -> 28",
        "run": lambda: solution("AB"),
        "expected": 28,
    },
    {
        "description": "ZY -> 701",
        "run": lambda: solution("ZY"),
        "expected": 701,
    },
    {
        "description": "Z -> 26",
        "run": lambda: solution("Z"),
        "expected": 26,
    },
    {
        "description": "AAA -> 703",
        "run": lambda: solution("AAA"),
        "expected": 703,
    },
]
