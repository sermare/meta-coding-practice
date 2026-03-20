from problems.p469_generate_parentheses import solution

TEST_CASES = [
    {
        "description": "n=1: single pair",
        "run": lambda: sorted(solution(1)),
        "expected": ["()"],
    },
    {
        "description": "n=2: two pairs",
        "run": lambda: sorted(solution(2)),
        "expected": ["(())", "()()"],
    },
    {
        "description": "n=3: five combos",
        "run": lambda: sorted(solution(3)),
        "expected": ["((()))", "(()())", "(())()", "()(())", "()()()"],
    },
    {
        "description": "n=1 count",
        "run": lambda: len(solution(1)),
        "expected": 1,
    },
    {
        "description": "n=4 count",
        "run": lambda: len(solution(4)),
        "expected": 14,
    },
]
