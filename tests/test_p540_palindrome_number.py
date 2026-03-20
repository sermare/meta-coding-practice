from problems.p540_palindrome_number import solution

TEST_CASES = [
    {
        "description": "Palindrome",
        "run": lambda: solution(121),
        "expected": True,
    },
    {
        "description": "Not palindrome",
        "run": lambda: solution(123),
        "expected": False,
    },
    {
        "description": "Negative number",
        "run": lambda: solution(-121),
        "expected": False,
    },
    {
        "description": "Single digit",
        "run": lambda: solution(7),
        "expected": True,
    },
    {
        "description": "Ten",
        "run": lambda: solution(10),
        "expected": False,
    },
]
