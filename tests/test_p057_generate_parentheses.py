from problems.p057_generate_parentheses import solution

TEST_CASES = [
    {
        "description": "n=1: single pair",
        "run": lambda: sorted(solution(1)),
        "expected": ["()"],
    },
    {
        "description": "n=2: two pairs",
        "run": lambda: sorted(solution(2)),
        "expected": sorted(["(())", "()()"]),
    },
    {
        "description": "n=3: three pairs",
        "run": lambda: sorted(solution(3)),
        "expected": sorted(["((()))", "(()())", "(())()", "()(())", "()()()"]),
    },
    {
        "description": "n=4: count should be 14",
        "run": lambda: len(solution(4)),
        "expected": 14,
    },
]
