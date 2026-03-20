from problems.p344_longest_repeating_character_replacement import solution

TEST_CASES = [
    {
        "description": "Basic: ABAB k=2 -> 4",
        "run": lambda: solution("ABAB", 2),
        "expected": 4,
    },
    {
        "description": "Mixed: AABABBA k=1 -> 4",
        "run": lambda: solution("AABABBA", 1),
        "expected": 4,
    },
    {
        "description": "All same: AAAA k=0 -> 4",
        "run": lambda: solution("AAAA", 0),
        "expected": 4,
    },
    {
        "description": "Single char: A k=1 -> 1",
        "run": lambda: solution("A", 1),
        "expected": 1,
    },
]
