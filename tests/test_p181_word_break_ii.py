from problems.p181_word_break_ii import solution

TEST_CASES = [
    {
        "description": "catsanddog",
        "run": lambda: sorted(solution("catsanddog", ["cat","cats","and","sand","dog"])),
        "expected": sorted(["cats and dog","cat sand dog"]),
    },
    {
        "description": "pineapplepenapple",
        "run": lambda: sorted(solution("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])),
        "expected": sorted(["pine apple pen apple","pineapple pen apple","pine applepen apple"]),
    },
    {
        "description": "No valid break",
        "run": lambda: solution("catsandog", ["cats","dog","sand","and","cat"]),
        "expected": [],
    },
    {
        "description": "Single word",
        "run": lambda: solution("a", ["a"]),
        "expected": ["a"],
    },
]
