from problems.p747_rings_and_rods import solution

TEST_CASES = [
    {
        "description": "One rod with all colors: 'B0B6G0R6R0R6G0'",
        "run": lambda: solution("B0B6G0R6R0R6G0"),
        "expected": 1,
    },
    {
        "description": "No rod with all: 'B0R0G1'",
        "run": lambda: solution("B0R0G1"),
        "expected": 0,
    },
    {
        "description": "Multiple rods: 'G4R0G0B0R4B4'",
        "run": lambda: solution("G4R0G0B0R4B4"),
        "expected": 1,
    },
    {
        "description": "All on same rod: 'R0G0B0'",
        "run": lambda: solution("R0G0B0"),
        "expected": 1,
    },
]
