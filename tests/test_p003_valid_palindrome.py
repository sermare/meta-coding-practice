from problems.p003_valid_palindrome import solution

TEST_CASES = [
    {
        "description": "Classic palindrome phrase",
        "run": lambda: solution("A man, a plan, a canal: Panama"),
        "expected": True,
    },
    {
        "description": "Not a palindrome: 'race a car'",
        "run": lambda: solution("race a car"),
        "expected": False,
    },
    {
        "description": "Empty/whitespace string",
        "run": lambda: solution(" "),
        "expected": True,
    },
    {
        "description": "Mixed character types: '0P'",
        "run": lambda: solution("0P"),
        "expected": False,
    },
    {
        "description": "Simple two-char palindrome: 'aa'",
        "run": lambda: solution("aa"),
        "expected": True,
    },
]
