from problems.p043_remove_invalid_parentheses import solution

COMPARATOR = lambda result, expected: sorted(result) == sorted(expected)

TEST_CASES = [
    {
        "description": "Multiple valid results from ()())()",
        "run": lambda: solution("()())()"),
        "expected": ["(())()", "()()()"],
    },
    {
        "description": "Multiple valid results with letters (a)())()",
        "run": lambda: solution("(a)())()"),
        "expected": ["(a())()", "(a)()()"],
    },
    {
        "description": "Only invalid parens )( yields empty string",
        "run": lambda: solution(")("),
        "expected": [""],
    },
    {
        "description": "No parentheses, already valid",
        "run": lambda: solution("x"),
        "expected": ["x"],
    },
    {
        "description": "Already valid ()",
        "run": lambda: solution("()"),
        "expected": ["()"],
    },
]
