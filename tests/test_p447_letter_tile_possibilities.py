from problems.p447_letter_tile_possibilities import solution

TEST_CASES = [
    {
        "description": "Basic: AAB",
        "run": lambda: solution("AAB"),
        "expected": 8,
    },
    {
        "description": "All different: ABCDEFGH",
        "run": lambda: solution("ABCDEFGH"),
        "expected": 109600,
    },
    {
        "description": "Single tile: V",
        "run": lambda: solution("V"),
        "expected": 1,
    },
    {
        "description": "Two same: AA",
        "run": lambda: solution("AA"),
        "expected": 3,
    },
    {
        "description": "Two different: AB",
        "run": lambda: solution("AB"),
        "expected": 4,
    },
]
