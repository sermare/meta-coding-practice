from problems.p607_factor_combinations import solution

TEST_CASES = [
    {
        "description": "Factor combinations of 12",
        "run": lambda: sorted([sorted(x) for x in solution(12)]),
        "expected": [[2, 2, 3], [2, 6], [3, 4]],
    },
    {
        "description": "Factor combinations of 1",
        "run": lambda: solution(1),
        "expected": [],
    },
    {
        "description": "Prime number 37",
        "run": lambda: solution(37),
        "expected": [],
    },
    {
        "description": "Factor combinations of 8",
        "run": lambda: sorted([sorted(x) for x in solution(8)]),
        "expected": [[2, 2, 2], [2, 4]],
    },
    {
        "description": "Factor combinations of 32",
        "run": lambda: len(solution(32)),
        "expected": 7,
    },
]
