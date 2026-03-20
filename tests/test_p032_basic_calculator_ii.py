from problems.p032_basic_calculator_ii import solution

TEST_CASES = [
    {
        "description": "'3+2*2' -> 7",
        "run": lambda: solution("3+2*2"),
        "expected": 7,
    },
    {
        "description": "' 3/2 ' -> 1",
        "run": lambda: solution(" 3/2 "),
        "expected": 1,
    },
    {
        "description": "' 3+5 / 2 ' -> 5",
        "run": lambda: solution(" 3+5 / 2 "),
        "expected": 5,
    },
    {
        "description": "'42' -> 42 (single number)",
        "run": lambda: solution("42"),
        "expected": 42,
    },
    {
        "description": "'1-1+1' -> 1",
        "run": lambda: solution("1-1+1"),
        "expected": 1,
    },
]
