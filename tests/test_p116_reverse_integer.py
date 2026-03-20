from problems.p116_reverse_integer import solution

TEST_CASES = [
    {
        "description": "Positive number",
        "run": lambda: solution(123),
        "expected": 321,
    },
    {
        "description": "Negative number",
        "run": lambda: solution(-123),
        "expected": -321,
    },
    {
        "description": "Trailing zero",
        "run": lambda: solution(120),
        "expected": 21,
    },
    {
        "description": "Zero",
        "run": lambda: solution(0),
        "expected": 0,
    },
    {
        "description": "Overflow returns 0",
        "run": lambda: solution(1534236469),
        "expected": 0,
    },
]
