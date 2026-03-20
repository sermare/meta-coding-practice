from problems.p653_palindrome_permutation import solution

TEST_CASES = [
    {
        "description": "Can form palindrome: tactcoa",
        "run": lambda: solution("tactcoa"),
        "expected": True,
    },
    {
        "description": "Cannot form palindrome: abc",
        "run": lambda: solution("abc"),
        "expected": False,
    },
    {
        "description": "Single character",
        "run": lambda: solution("a"),
        "expected": True,
    },
    {
        "description": "Already palindrome: aabbaa",
        "run": lambda: solution("aabbaa"),
        "expected": True,
    },
    {
        "description": "Two distinct chars odd count: code",
        "run": lambda: solution("code"),
        "expected": False,
    },
]
