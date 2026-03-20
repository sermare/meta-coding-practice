from problems.p070_word_search_ii import solution

TEST_CASES = [
    {
        "description": "Standard case with found words",
        "run": lambda: sorted(solution([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"])),
        "expected": sorted(["eat", "oath"]),
    },
    {
        "description": "No words found",
        "run": lambda: solution([["a", "b"], ["c", "d"]], ["abcb"]),
        "expected": [],
    },
    {
        "description": "Single cell board",
        "run": lambda: solution([["a"]], ["a"]),
        "expected": ["a"],
    },
    {
        "description": "Single cell no match",
        "run": lambda: solution([["a"]], ["b"]),
        "expected": [],
    },
]
