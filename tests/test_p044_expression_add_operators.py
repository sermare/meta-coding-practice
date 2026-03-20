from problems.p044_expression_add_operators import solution

COMPARATOR = lambda result, expected: sorted(result) == sorted(expected)

TEST_CASES = [
    {
        "description": "123 target 6",
        "run": lambda: solution("123", 6),
        "expected": ["1+2+3", "1*2*3"],
    },
    {
        "description": "232 target 8",
        "run": lambda: solution("232", 8),
        "expected": ["2*3+2", "2+3*2"],
    },
    {
        "description": "3456237490 target 9191 - no solution",
        "run": lambda: solution("3456237490", 9191),
        "expected": [],
    },
    {
        "description": "105 target 5 with leading zero handling",
        "run": lambda: solution("105", 5),
        "expected": ["1*0+5", "10-5"],
    },
    {
        "description": "00 target 0",
        "run": lambda: solution("00", 0),
        "expected": ["0+0", "0-0", "0*0"],
    },
]
