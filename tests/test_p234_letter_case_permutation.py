from problems.p234_letter_case_permutation import solution

TEST_CASES = [
    {
        "description": "Mixed: a1b2",
        "run": lambda: sorted(solution("a1b2")) if solution("a1b2") else None,
        "expected": sorted(["a1b2", "a1B2", "A1b2", "A1B2"]),
    },
    {
        "description": "One letter: 3z4",
        "run": lambda: sorted(solution("3z4")) if solution("3z4") else None,
        "expected": sorted(["3z4", "3Z4"]),
    },
    {
        "description": "All digits: 123",
        "run": lambda: sorted(solution("123")) if solution("123") else None,
        "expected": ["123"],
    },
    {
        "description": "Single letter: a",
        "run": lambda: sorted(solution("a")) if solution("a") else None,
        "expected": sorted(["a", "A"]),
    },
]
