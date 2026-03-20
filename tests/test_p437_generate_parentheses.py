from problems.p437_generate_parentheses import solution

TEST_CASES = [
    {
        "description": "n=3",
        "run": lambda: sorted(solution(3)),
        "expected": sorted(["((()))", "(()())", "(())()", "()(())", "()()()"]),
    },
    {
        "description": "n=1",
        "run": lambda: solution(1),
        "expected": ["()"],
    },
    {
        "description": "n=2",
        "run": lambda: sorted(solution(2)),
        "expected": sorted(["(())", "()()"]),
    },
    {
        "description": "Count for n=4",
        "run": lambda: len(solution(4)),
        "expected": 14,
    },
    {
        "description": "Count for n=5",
        "run": lambda: len(solution(5)),
        "expected": 42,
    },
]
