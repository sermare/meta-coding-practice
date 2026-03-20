from problems.p627_repeated_dna_sequences import solution

TEST_CASES = [
    {
        "description": "Two repeated sequences",
        "run": lambda: sorted(solution("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")),
        "expected": sorted(["AAAAACCCCC", "CCCCCAAAAA"]),
    },
    {
        "description": "All same character",
        "run": lambda: solution("AAAAAAAAAAAAA"),
        "expected": ["AAAAAAAAAA"],
    },
    {
        "description": "No repeats",
        "run": lambda: solution("ACGTACGTAC"),
        "expected": [],
    },
    {
        "description": "Short string (less than 10)",
        "run": lambda: solution("ACGT"),
        "expected": [],
    },
]
