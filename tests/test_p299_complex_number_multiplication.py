from problems.p299_complex_number_multiplication import solution

TEST_CASES = [
    {
        "description": "'1+1i' * '1+1i' -> '0+2i'",
        "run": lambda: solution("1+1i", "1+1i"),
        "expected": "0+2i",
    },
    {
        "description": "'1+-1i' * '1+-1i' -> '0+-2i'",
        "run": lambda: solution("1+-1i", "1+-1i"),
        "expected": "0+-2i",
    },
    {
        "description": "'1+0i' * '1+0i' -> '1+0i'",
        "run": lambda: solution("1+0i", "1+0i"),
        "expected": "1+0i",
    },
    {
        "description": "'0+1i' * '0+1i' -> '-1+0i'",
        "run": lambda: solution("0+1i", "0+1i"),
        "expected": "-1+0i",
    },
    {
        "description": "'2+3i' * '4+5i' -> '-7+22i'",
        "run": lambda: solution("2+3i", "4+5i"),
        "expected": "-7+22i",
    },
]
