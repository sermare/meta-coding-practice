from problems.p115_palindrome_number import solution

TEST_CASES = [
    {
        "description": "Positive palindrome",
        "run": lambda: solution(121),
        "expected": True,
    },
    {
        "description": "Negative number",
        "run": lambda: solution(-121),
        "expected": False,
    },
    {
        "description": "Ends in zero",
        "run": lambda: solution(10),
        "expected": False,
    },
    {
        "description": "Zero is a palindrome",
        "run": lambda: solution(0),
        "expected": True,
    },
    {
        "description": "Single digit",
        "run": lambda: solution(7),
        "expected": True,
    },
]
