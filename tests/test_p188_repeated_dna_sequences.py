from problems.p188_repeated_dna_sequences import solution

TEST_CASES = [
    {
        "description": "Two repeated sequences",
        "run": lambda: sorted(solution("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")),
        "expected": sorted(["AAAAACCCCC","CCCCCAAAAA"]),
    },
    {
        "description": "All A's repeated",
        "run": lambda: solution("AAAAAAAAAAAAA"),
        "expected": ["AAAAAAAAAA"],
    },
    {
        "description": "No repeats (too short)",
        "run": lambda: solution("ACGT"),
        "expected": [],
    },
    {
        "description": "Exactly 10 chars, no repeat",
        "run": lambda: solution("ACGTACGTAC"),
        "expected": [],
    },
]
