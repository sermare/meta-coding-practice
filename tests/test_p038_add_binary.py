from problems.p038_add_binary import solution

TEST_CASES = [
    {
        "description": "'11' + '1' -> '100'",
        "run": lambda: solution("11", "1"),
        "expected": "100",
    },
    {
        "description": "'1010' + '1011' -> '10101'",
        "run": lambda: solution("1010", "1011"),
        "expected": "10101",
    },
    {
        "description": "'0' + '0' -> '0'",
        "run": lambda: solution("0", "0"),
        "expected": "0",
    },
    {
        "description": "'1' + '111' -> '1000'",
        "run": lambda: solution("1", "111"),
        "expected": "1000",
    },
    {
        "description": "'1111' + '1111' -> '11110'",
        "run": lambda: solution("1111", "1111"),
        "expected": "11110",
    },
]
