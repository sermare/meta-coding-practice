from problems.p179_palindrome_partitioning import solution

TEST_CASES = [
    {
        "description": "aab -> two partitions",
        "run": lambda: sorted(solution("aab")),
        "expected": sorted([["a","a","b"],["aa","b"]]),
    },
    {
        "description": "Single char",
        "run": lambda: solution("a"),
        "expected": [["a"]],
    },
    {
        "description": "All same chars",
        "run": lambda: len(solution("aaa")),
        "expected": 4,
    },
    {
        "description": "aba",
        "run": lambda: sorted(solution("aba")),
        "expected": sorted([["a","b","a"],["aba"]]),
    },
]
