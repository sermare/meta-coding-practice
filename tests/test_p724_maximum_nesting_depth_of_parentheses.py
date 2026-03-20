from problems.p724_maximum_nesting_depth_of_parentheses import solution

TEST_CASES = [
    {
        "description": "Nested: '(1+(2*3)+((8)/4))+1'",
        "run": lambda: solution("(1+(2*3)+((8)/4))+1"),
        "expected": 3,
    },
    {
        "description": "Simple: '(1)+((2))+(((3)))'",
        "run": lambda: solution("(1)+((2))+(((3)))"),
        "expected": 3,
    },
    {
        "description": "No parens: '1'",
        "run": lambda: solution("1"),
        "expected": 0,
    },
    {
        "description": "Single pair: '(1)'",
        "run": lambda: solution("(1)"),
        "expected": 1,
    },
]
