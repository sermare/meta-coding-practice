from problems.p823_minimum_white_tiles_after_covering_with_carpets import solution

TEST_CASES = [
    {
        "description": "Basic: 10110101, 2 carpets, len=2",
        "run": lambda: solution("10110101", 2, 2),
        "expected": 2,
    },
    {
        "description": "All black: 0000, 1 carpet, len=2",
        "run": lambda: solution("0000", 1, 2),
        "expected": 0,
    },
    {
        "description": "All white, enough carpets: 111, 1 carpet, len=3",
        "run": lambda: solution("111", 1, 3),
        "expected": 0,
    },
    {
        "description": "No carpets: 111, 0 carpets, len=2",
        "run": lambda: solution("111", 0, 2),
        "expected": 3,
    },
]
