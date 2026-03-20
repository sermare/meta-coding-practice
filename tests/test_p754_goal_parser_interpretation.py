from problems.p754_goal_parser_interpretation import solution

TEST_CASES = [
    {
        "description": "Mixed: G()(al)",
        "run": lambda: solution("G()(al)"),
        "expected": "Goal",
    },
    {
        "description": "Only G: G()()()",
        "run": lambda: solution("G()()()"),
        "expected": "Gooo",
    },
    {
        "description": "Only (al): (al)(al)(al)",
        "run": lambda: solution("(al)(al)(al)"),
        "expected": "alalal",
    },
    {
        "description": "Complex: (al)G(al)()()G",
        "run": lambda: solution("(al)G(al)()()G"),
        "expected": "alGalooG",
    },
]
